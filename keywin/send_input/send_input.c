#define PY_SSIZE_T_CLEAN
#define INPUT_SIZE sizeof(INPUT)

#include <Python.h>
#include <Windows.h>

static PyObject* free_and_fail(void* memory, PyThreadState* thread_state) {
    free(memory);
    PyEval_RestoreThread(thread_state);
    Py_RETURN_FALSE;
}

static PyObject* restore_and_fail(PyThreadState* thread_state) {
    PyEval_RestoreThread(thread_state);
    Py_RETURN_FALSE;
}

static PyObject* free_and_succeed(void* memory, PyThreadState* thread_state) {
    free(memory);
    PyEval_RestoreThread(thread_state);
    Py_RETURN_TRUE;
}

static PyObject* restore_and_succeed(PyThreadState* thread_state) {
    PyEval_RestoreThread(thread_state);
    Py_RETURN_TRUE;
}

static PyObject* send_keyboard_events(PyObject* self, PyObject* args) {
    PyObject* keyboard_events;

    if (!PyArg_ParseTuple(args, "O", &keyboard_events)) {
        Py_RETURN_FALSE;
    }

    const Py_ssize_t keys_length = PyObject_Size(keyboard_events);

    if (keys_length == -1) {
        Py_RETURN_FALSE;
    }

    const UINT number_of_keys = (UINT)keys_length;
    INPUT* inputs = calloc(number_of_keys, INPUT_SIZE);

    if (!inputs) {
        Py_RETURN_FALSE;
    }

    int key_overflow  = 0;
    int scan_overflow = 0;

    for (UINT i = 0; i < number_of_keys; i++) {
        PyObject* keyboard_event = PyTuple_GetItem(keyboard_events, i);
        const WORD key_code = (WORD)PyLong_AsLongAndOverflow(PyTuple_GetItem(keyboard_event, 0), &key_overflow);
        const WORD scan_code = (WORD)PyLong_AsLongAndOverflow(PyTuple_GetItem(keyboard_event, 1), &scan_overflow);
        const DWORD flags = PyLong_AsUnsignedLong(PyTuple_GetItem(keyboard_event, 2));

        inputs[i].type       = INPUT_KEYBOARD;
        inputs[i].ki.wVk     = key_code;
        inputs[i].ki.wScan   = scan_code;
        inputs[i].ki.dwFlags = flags;
    }

    PyThreadState* thread_state = PyEval_SaveThread();

    if (key_overflow || scan_overflow) {
        return free_and_fail(inputs, thread_state);
    }

    return SendInput(number_of_keys, inputs, INPUT_SIZE)
        ? free_and_succeed(inputs, thread_state)
        : free_and_fail(inputs, thread_state);
}

static PyObject* send_keyboard_press_events(PyObject* self, PyObject* args) {
    PyObject* keys;

    if (!PyArg_ParseTuple(args, "O", &keys)) {
        Py_RETURN_FALSE;
    }

    const Py_ssize_t keys_length = PyObject_Size(keys);

    if (keys_length == -1) {
        Py_RETURN_FALSE;
    }

    const UINT number_of_keys = (UINT)keys_length;
    const UINT inputs_length = number_of_keys * 2;
    INPUT* inputs = calloc(inputs_length, INPUT_SIZE);

    if (!inputs) {
        Py_RETURN_FALSE;
    }

    int overflow = 0;

    for (UINT i = 0, j = number_of_keys; i < number_of_keys; i++, j++) {
        PyObject* key = PyTuple_GetItem(keys, i);
        const WORD key_code = (WORD)PyLong_AsLongAndOverflow(key, &overflow);

        inputs[i].type       = INPUT_KEYBOARD;
        inputs[i].ki.wVk     = key_code;

        inputs[j].type       = INPUT_KEYBOARD;
        inputs[j].ki.wVk     = key_code;
        inputs[j].ki.dwFlags = KEYEVENTF_KEYUP;
    }

    PyThreadState* thread_state = PyEval_SaveThread();

    if (overflow) {
        return free_and_fail(inputs, thread_state);
    }

    return SendInput(inputs_length, inputs, INPUT_SIZE)
        ? free_and_succeed(inputs, thread_state)
        : free_and_fail(inputs, thread_state);
}

static PyObject* send_unicode_events(PyObject* self, PyObject* args) {
    const char* string;
    const Py_ssize_t string_length;

    if (!PyArg_ParseTuple(args, "s#", &string, &string_length)) {
        Py_RETURN_FALSE;
    }

    PyThreadState* thread_state = PyEval_SaveThread();
    const UINT number_of_characters = (UINT)string_length;
    const UINT inputs_length = number_of_characters * 2;
    INPUT* inputs = calloc(inputs_length, INPUT_SIZE);

    if (!inputs) {
        return restore_and_fail(thread_state);
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

    return SendInput(inputs_length, inputs, INPUT_SIZE)
        ? free_and_succeed(inputs, thread_state)
        : free_and_fail(inputs, thread_state);
}

static PyObject* send_mouse_events(PyObject* self, PyObject* args) {
    PyObject* mouse_events;

    if (!PyArg_ParseTuple(args, "O", &mouse_events)) {
        Py_RETURN_FALSE;
    }

    const Py_ssize_t mouse_events_length = PyObject_Size(mouse_events);

    if (mouse_events_length == -1) {
        Py_RETURN_FALSE;
    }

    const UINT number_of_events = (UINT)mouse_events_length;
    INPUT* inputs = calloc(number_of_events, INPUT_SIZE);

    if (!inputs) {
        Py_RETURN_FALSE;
    }

    int x_overflow          = 0;
    int y_overflow          = 0;
    int mouse_data_overflow = 0;

    for (UINT i = 0; i < number_of_events; i++) {
        PyObject* mouse_event  = PyTuple_GetItem(mouse_events, i);
        const DWORD flags      = PyLong_AsUnsignedLong(PyTuple_GetItem(mouse_event, 0));
        const LONG x           = PyLong_AsLongAndOverflow(PyTuple_GetItem(mouse_event, 1), &x_overflow);
        const LONG y           = PyLong_AsLongAndOverflow(PyTuple_GetItem(mouse_event, 2), &y_overflow);
        const DWORD mouse_data = PyLong_AsLongAndOverflow(PyTuple_GetItem(mouse_event, 3), &mouse_data_overflow);

        inputs[i].type         = INPUT_MOUSE;
        inputs[i].mi.dx        = x;
        inputs[i].mi.dy        = y;
        inputs[i].mi.mouseData = mouse_data;
        inputs[i].mi.dwFlags   = flags;
    }

    PyThreadState* thread_state = PyEval_SaveThread();

    if (x_overflow || y_overflow || mouse_data_overflow) {
        return free_and_fail(inputs, thread_state);
    }

    return SendInput(number_of_events, inputs, INPUT_SIZE)
        ? free_and_succeed(inputs, thread_state)
        : free_and_fail(inputs, thread_state);
}

static PyObject* send_mouse_flag(PyObject* self, PyObject* args) {
    const DWORD flags;

    if (!PyArg_ParseTuple(args, "I", &flags)) {
        Py_RETURN_FALSE;
    }

    PyThreadState* thread_state = PyEval_SaveThread();

    INPUT input      = {0};
    input.type       = INPUT_MOUSE;
    input.mi.dwFlags = flags;

    return SendInput(1, &input, INPUT_SIZE)
        ? restore_and_succeed(thread_state)
        : restore_and_fail(thread_state);
}

static PyMethodDef send_input_methods[] = {
    {"send_keyboard_events",       send_keyboard_events,       METH_VARARGS, "Send keyboard events"},
    {"send_keyboard_press_events", send_keyboard_press_events, METH_VARARGS, "Press and release keyboard keys"},
    {"send_unicode_events",        send_unicode_events,        METH_VARARGS, "Send unicode events"},
    {"send_mouse_events",          send_mouse_events,          METH_VARARGS, "Send mouse events"},
    {"send_mouse_flag",            send_mouse_flag,            METH_VARARGS, "Send mouse flags"},
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
