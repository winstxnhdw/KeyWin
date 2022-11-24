#include <Python.h>
#include <Windows.h>

static PyObject* press_keyboard(PyObject *self, PyObject *args) {
    PyObject* key_tuple;
    
    if (!PyArg_ParseTuple(args, "O", &key_tuple)) return NULL;

    const UINT key_list_length = (UINT)PyObject_Length(key_tuple);
    const UINT inputs_length = key_list_length * 2;
    const int input_size = sizeof(INPUT);
    INPUT* inputs = malloc(input_size * inputs_length);
    
    for (UINT i = 0; i < key_list_length; i++) {
        PyObject* key        = PyTuple_GetItem(key_tuple, i);
        inputs[i].type       = INPUT_KEYBOARD;
        inputs[i].ki.wVk     = (WORD)PyLong_AsLong(key);
        inputs[i].ki.dwFlags = 0;
    }

    for (UINT i = key_list_length; i < inputs_length; i++) {
        inputs[i].type       = INPUT_KEYBOARD;
        inputs[i].ki.wVk     = inputs[i - key_list_length].ki.wVk;
        inputs[i].ki.dwFlags = KEYEVENTF_KEYUP;
    }

    if (SendInput(inputs_length, inputs, input_size) != inputs_length) {
        free(inputs);
        PyErr_SetString(PyExc_RuntimeError, "press_keyboard failed.");
        return NULL;
    }

    Py_RETURN_NONE;
}

static PyObject* send_mouse_event(PyObject *self, PyObject *args) {
    PyObject* mouse_event_list;
    
    if (!PyArg_ParseTuple(args, "O", &mouse_event_list)) return NULL;

    const Py_ssize_t mouse_events_length = PyObject_Length(mouse_event_list);
    const int input_size = sizeof(INPUT);
    INPUT* inputs = malloc(input_size * mouse_events_length);

    for (Py_ssize_t i = 0; i < mouse_events_length; i++) {
        PyObject* mouse_event = PyTuple_GetItem(mouse_event_list, i);

        inputs[i].type         = INPUT_MOUSE;
        inputs[i].mi.dx        = PyLong_AsLong(PyList_GetItem(mouse_event, 0));
        inputs[i].mi.dy        = PyLong_AsLong(PyList_GetItem(mouse_event, 1));
        inputs[i].mi.mouseData = PyLong_AsUnsignedLong(PyList_GetItem(mouse_event, 2));
        inputs[i].mi.dwFlags   = PyLong_AsUnsignedLong(PyList_GetItem(mouse_event, 3));
        inputs[i].mi.time      = 0;
    }

    if (SendInput((UINT)mouse_events_length, inputs, input_size) != mouse_events_length) {
        free(inputs);
        PyErr_SetString(PyExc_RuntimeError, "send_mouse_event failed.");
        return NULL;
    }
    
    Py_RETURN_NONE;
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
