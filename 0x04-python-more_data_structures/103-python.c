#include <Python.h>
#include <stdio.h>
/**
* print_python_list - Prints the size of python list
* @p: Parameter for the python list argument
* Return: it returns nothing
*/

void print_python_list(PyObject *p)
{
Py_ssize_t size = PyList_Size(p);
Py_ssize_t i;

printf("[*] Python list info\n");
printf("[*] Size of the Python List = %ld\n", size);
printf("[*] Allocated = %ld\n", ((PyListObject *)p)->allocated);

for (i = 0; i < size; i++)
{
PyObject *item = PyList_GetItem(p, i);
const char *item_type = item->ob_type->tp_name;

printf("Element %ld: %s\n", i, item_type);
}
}
/**
* print_python_bytes - prints python byte for list
* @p: argument for the python list
* Return: returns nothing
*/

void print_python_bytes(PyObject *p)
{
Py_ssize_t size = PyBytes_Size(p);
Py_ssize_t i;
char *bytes = PyBytes_AsString(p);

printf("[.] Bytes object info\n");
if (!PyBytes_Check(p))
{
printf("  [ERROR] Invalid Bytes Object\n");
return;
}

printf("  [*] Size of the Python Bytes = %ld\n", size);
printf("  [*] Bytes object contents: ");

if (size > 10)
{
printf("first 10 bytes: ");
for (i = 0; i < 10; i++)
{
printf("%02x", bytes[i] & 0xff);
if (i < 9)
printf(" ");
}
printf("\n");
}
else
{
for (i = 0; i < size; i++)
{
printf("%02x", bytes[i] & 0xff);
if (i < size - 1)
printf(" ");
}
printf("\n");
}
}
