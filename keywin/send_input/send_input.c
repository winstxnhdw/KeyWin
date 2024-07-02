#define PY_SSIZE_T_CLEAN
#include <Python.h>
#include <Windows.h>

static PyObject* dispose_and_fail(void* memory) {
    free(memory);
    Py_RETURN_FALSE;
}

static PyObject* press_keyboard(PyObject* self, PyObject* args) {
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
    INPUT* inputs = malloc(input_size * inputs_length);

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
        inputs[i].ki.dwFlags = 0;

        inputs[j].type       = INPUT_KEYBOARD;
        inputs[j].ki.wVk     = key_code;
        inputs[j].ki.dwFlags = KEYEVENTF_KEYUP;
    }

    if (SendInput(inputs_length, inputs, input_size) != inputs_length) {
        return dispose_and_fail(inputs);
    }

    free(inputs);
    Py_RETURN_TRUE;
}

static PyObject* send_mouse_event(PyObject* self, PyObject* args) {
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
    INPUT* inputs = malloc(input_size * number_of_events);

    if (!inputs) {
        Py_RETURN_FALSE;
    }

    int x_overflow = 0;
    int y_overflow = 0;

    for (UINT i = 0; i < number_of_events; i++) {
        PyObject* mouse_event  = PyTuple_GetItem(mouse_event_list, i);
        const LONG x           = PyLong_AsLongAndOverflow(PyTuple_GetItem(mouse_event, 0), &x_overflow);
        const LONG y           = PyLong_AsLongAndOverflow(PyTuple_GetItem(mouse_event, 1), &y_overflow);
        const DWORD mouse_data = PyLong_AsUnsignedLong(PyTuple_GetItem(mouse_event, 2));
        const DWORD flags       = PyLong_AsUnsignedLong(PyTuple_GetItem(mouse_event, 3));

        if (x_overflow || y_overflow) {
            return dispose_and_fail(inputs);
        }

        inputs[i].type         = INPUT_MOUSE;
        inputs[i].mi.dx        = x;
        inputs[i].mi.dy        = y;
        inputs[i].mi.mouseData = mouse_data;
        inputs[i].mi.dwFlags   = flags;
        inputs[i].mi.time      = 0;
    }

    if (SendInput(number_of_events, inputs, input_size) != number_of_events) {
        return dispose_and_fail(inputs);
    }

    free(inputs);
    Py_RETURN_TRUE;
}

static PyMethodDef send_input_methods[] = {
    {"press_keyboard", press_keyboard, METH_VARARGS, "Press and release keyboard keys"},
    {"send_mouse_event", send_mouse_event, METH_VARARGS, "Send mouse events"},
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
