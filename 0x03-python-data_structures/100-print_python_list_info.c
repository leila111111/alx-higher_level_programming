#include <Python.h>
#include <object.h>
#include <listobject.h>
void print_python_list_info(PyObject *p)
{
	int size = PyList_Size(p);
	int i;

	printf("[*] Size of the Python List = %li\n", size);
	printf("[*] Allocated = %ld\n", ((PyListObject *)p)->allocated);
	for (i = 0; i < size; i++)
	{
		printf("Element %d: ", i);
		printf("%s\n", Py_TYPE(PyList_GetItem(p, i))->tp_name);
	}
}
