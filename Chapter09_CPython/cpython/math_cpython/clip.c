#define PY_SSIZE_T_CLEAN
#include "Python.h"

static PyObject *method_add_vectors(PyObject *self, PyObject *args)
{
    PyObject *const list_a = NULL;
    PyObject *const list_b = NULL;

    if (!PyArg_ParseTuple(args, "OO", &list_a, &list_b))
    {
        PyErr_SetString(PyExc_TypeError, "error");
        return NULL;
    }

    if (!PyList_Check(list_a) || !PyList_Check(list_b))
    {
        PyErr_SetString(PyExc_ValueError, "error");
        return NULL;
    }

    const Py_ssize_t len_a = PyList_Size(list_a);
    const Py_ssize_t len_b = PyList_Size(list_b);

    if (len_a != len_b)
    {
        PyErr_SetString(PyExc_ValueError, "error");
        return NULL;
    }

    PyObject *result = PyList_New(len_a);

    for (Py_ssize_t i = 0U; i < len_a; ++i)
    {
        PyObject *const item_a = PyList_GetItem(list_a, i);
        PyObject *const item_b = PyList_GetItem(list_b, i);

        if (!PyFloat_Check(item_a) || !PyFloat_Check(item_b))
        {
            PyErr_SetString(PyExc_ValueError, "Items must be 64bit floats..");
            return NULL;
        }

        PyList_SetItem(result, i, PyNumber_Add(item_a, item_b));
    }

    return result;
}

static PyObject *method_clip_vector(PyObject *self, PyObject *args)
{
    PyObject *const list = NULL;
    double min_value = 0.0;
    double max_value = 0.0;

    if (!PyArg_ParseTuple(args, "Odd", &list, &min_value, &max_value))
    {
        PyErr_SetString(PyExc_TypeError, "error");

        return NULL;
    }

    const Py_ssize_t len = PyList_Size(list);

    for (Py_ssize_t i = 0U; i < len; ++i)
    {
        const PyObject *const item = PyList_GetItem(list, i);

        if (!PyFloat_Check(item))
        {
            PyErr_SetString(PyExc_ValueError, "Items must be 64bit floats..");
            return NULL;
        }

        const double temp = PyFloat_AsDouble(item);

        if (temp < min_value)
        {
            PyList_SetItem(list, i, PyFloat_FromDouble(min_value));
        }
        else if (temp > max_value)
        {
            PyList_SetItem(list, i, PyFloat_FromDouble(max_value));
        }
    }

    return Py_None;
}

static PyMethodDef math_cpythonMethods[] = {
    {"add_vectors", method_add_vectors, METH_VARARGS, "CPython Function"},
    {"clip_vector", method_clip_vector, METH_VARARGS, "CPython Function"},
    {NULL, NULL, 0, NULL}
};

static struct PyModuleDef math_cpythonmodule = {
    PyModuleDef_HEAD_INIT, "math_cpython", "CPython Module", -1, math_cpythonMethods
};

PyMODINIT_FUNC PyInit_math_cpython(void)
{
    return PyModule_Create(&math_cpythonmodule);
}
