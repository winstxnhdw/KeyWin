#define PY_SSIZE_T_CLEAN
#include <Python.h>
#include <Windows.h>

static PyObject* dispose_and_fail(void* memory) {
    free(memory);
    Py_RETURN_FALSE;
}

static PyObject* send_keyboard_events(PyObject* self, PyObject* args) {
    PyObject* key_tuple;

    if (!PyArg_ParseTuple(args, "O", &key_tuple)) {
        Py_RETURN_FALSE;
    }

    const Py_ssize_t keys_length = PyObject_Length(key_tuple);

    if (keys_length == -1) {
        Py_RETURN_FALSE;
    }

    const UINT number_of_keys = (UINT)keys_length;
    const UINT inputs_length = number_of_keys * 2;
    const int input_size = sizeof(INPUT);
    INPUT* inputs = calloc(input_size, inputs_length);

    if (!inputs) {
        Py_RETURN_FALSE;
    }

    int overflow = 0;

    for (UINT i = 0, j = number_of_keys; i < number_of_keys; i++, j++) {
        PyObject* key = PyTuple_GetItem(key_tuple, i);
        const WORD key_code = (WORD)PyLong_AsLongAndOverflow(key, &overflow);

        if (overflow) {
            return dispose_and_fail(inputs);
        }

        inputs[i].type       = INPUT_KEYBOARD;
        inputs[i].ki.wVk     = key_code;

        inputs[j].type       = INPUT_KEYBOARD;
        inputs[j].ki.wVk     = key_code;
        inputs[j].ki.dwFlags = KEYEVENTF_KEYUP;
    }

    if (!SendInput(inputs_length, inputs, input_size)) {
        return dispose_and_fail(inputs);
    }

    free(inputs);
    Py_RETURN_TRUE;
}

static PyObject* send_unicode_events(PyObject* self, PyObject* args) {
    const char* string;
    Py_ssize_t string_length;

    if (!PyArg_ParseTuple(args, "s#", &string, &string_length)) {
        Py_RETURN_FALSE;
    }

    const UINT number_of_characters = (UINT)string_length;
    const UINT inputs_length = number_of_characters * 2;
    const int input_size = sizeof(INPUT);
    INPUT* inputs = calloc(input_size, inputs_length);

    if (!inputs) {
        Py_RETURN_FALSE;
    }

    for (UINT i = 0, j = number_of_characters; i < number_of_characters; i++, j++) {
        const WORD unicode = string[i];

        inputs[i].type       = INPUT_KEYBOARD;
        inputs[i].ki.wScan   = unicode;
        inputs[i].ki.dwFlags = KEYEVENTF_UNICODE;

        inputs[j].type       = INPUT_KEYBOARD;
        inputs[j].ki.wScan   = unicode;
        inputs[j].ki.dwFlags = KEYEVENTF_UNICODE | KEYEVENTF_KEYUP;
    }

    if (!SendInput(inputs_length, inputs, input_size)) {
        return dispose_and_fail(inputs);
    }

    free(inputs);
    Py_RETURN_TRUE;
}

static PyObject* send_generic_events(PyObject* self, PyObject* args, DWORD event_type) {
    PyObject* event_list;

    if (!PyArg_ParseTuple(args, "O", &event_list)) {
        Py_RETURN_FALSE;
    }

    const Py_ssize_t events_length = PyObject_Length(event_list);

    if (events_length == -1) {
        Py_RETURN_FALSE;
    }

    const UINT number_of_events = (UINT)events_length;
    const int input_size = sizeof(INPUT);
    INPUT* inputs = calloc(input_size, number_of_events);

    if (!inputs) {
        Py_RETURN_FALSE;
    }

    int x_overflow          = 0;
    int y_overflow          = 0;
    int mouse_data_overflow = 0;
    int key_overflow        = 0;

    for (UINT i = 0; i < number_of_events; i++) {
        PyObject* event = PyTuple_GetItem(event_list, i);
        PyObject* key = PyDict_GetItemString(event, "key");

        if (!key) {
            const LONG x = PyLong_AsLongAndOverflow(PyDict_GetItemString(event, "x"), &x_overflow);
            const LONG y = PyLong_AsLongAndOverflow(PyDict_GetItemString(event, "y"), &y_overflow);
            const DWORD mouse_data = PyLong_AsLongAndOverflow(PyDict_GetItemString(event, "data"), &mouse_data_overflow);
            const DWORD flags = PyLong_AsUnsignedLong(PyDict_GetItemString(event, "flags"));

            if (x_overflow || y_overflow || mouse_data_overflow) {
                return dispose_and_fail(inputs);
            }

            inputs[i].type         = INPUT_MOUSE;
            inputs[i].mi.dx        = x;
            inputs[i].mi.dy        = y;
            inputs[i].mi.mouseData = mouse_data;
            inputs[i].mi.dwFlags   = flags;
        }

        else {
            const WORD key_code = (WORD)PyLong_AsLongAndOverflow(key, &key_overflow);
            const DWORD flags = PyLong_AsUnsignedLong(PyDict_GetItemString(event, "release"));

            if (key_overflow) {
                return dispose_and_fail(inputs);
            }

            inputs[i].type       = INPUT_KEYBOARD;
            inputs[i].ki.wVk     = key_code;
            inputs[i].ki.dwFlags = flags;
        }
    }

    if (!SendInput(number_of_events, inputs, input_size)) {
        return dispose_and_fail(inputs);
    }

    free(inputs);
    Py_RETURN_TRUE;
}

static PyObject* send_mouse_events(PyObject* self, PyObject* args) {
    PyObject* mouse_event_list;

    if (!PyArg_ParseTuple(args, "O", &mouse_event_list)) {
        Py_RETURN_FALSE;
    }

    const Py_ssize_t mouse_events_length = PyObject_Length(mouse_event_list);

    if (mouse_events_length == -1) {
        Py_RETURN_FALSE;
    }

    const UINT number_of_events = (UINT)mouse_events_length;
    const int input_size = sizeof(INPUT);
    INPUT* inputs = calloc(input_size, number_of_events);

    if (!inputs) {
        Py_RETURN_FALSE;
    }

    int x_overflow          = 0;
    int y_overflow          = 0;
    int mouse_data_overflow = 0;

    for (UINT i = 0; i < number_of_events; i++) {
        PyObject* mouse_event  = PyTuple_GetItem(mouse_event_list, i);
        const LONG x           = PyLong_AsLongAndOverflow(PyTuple_GetItem(mouse_event, 0), &x_overflow);
        const LONG y           = PyLong_AsLongAndOverflow(PyTuple_GetItem(mouse_event, 1), &y_overflow);
        const DWORD mouse_data = PyLong_AsLongAndOverflow(PyTuple_GetItem(mouse_event, 2), &mouse_data_overflow);
        const DWORD flags      = PyLong_AsUnsignedLong(PyTuple_GetItem(mouse_event, 3));

        if (x_overflow || y_overflow || mouse_data_overflow) {
            return dispose_and_fail(inputs);
        }

        inputs[i].type         = INPUT_MOUSE;
        inputs[i].mi.dx        = x;
        inputs[i].mi.dy        = y;
        inputs[i].mi.mouseData = mouse_data;
        inputs[i].mi.dwFlags   = flags;
    }

    if (!SendInput(number_of_events, inputs, input_size)) {
        return dispose_and_fail(inputs);
    }

    free(inputs);
    Py_RETURN_TRUE;
}

static PyObject* send_mouse_flag(PyObject* self, PyObject* args) {
    DWORD flags;

    if (!PyArg_ParseTuple(args, "I", &flags)) {
        Py_RETURN_FALSE;
    }

    INPUT input      = {0};
    input.type       = INPUT_MOUSE;
    input.mi.dwFlags = flags;

    if (!SendInput(1, &input, sizeof(INPUT))) {
        Py_RETURN_FALSE;
    }

    Py_RETURN_TRUE;
}

static PyMethodDef send_input_methods[] = {
    {"send_keyboard_events", send_keyboard_events, METH_VARARGS, "Press and release keyboard keys"},
    {"send_unicode_events", send_unicode_events, METH_VARARGS, "Send unicode events"},
    {"send_generic_events", send_generic_events, METH_VARARGS, "Send generic events"},
    {"send_mouse_events", send_mouse_events, METH_VARARGS, "Send mouse events"},
    {"send_mouse_flag", send_mouse_flag, METH_VARARGS, "Send mouse flags"},
    {NULL, NULL, 0, NULL}
};

static struct PyModuleDef send_input_module = {
    PyModuleDef_HEAD_INIT,
    "send_input",
    "send_input module",
    -1,
    send_input_methods
};

PyMODINIT_FUNC PyInit_send_input() {
    return PyModule_Create(&send_input_module);
}
