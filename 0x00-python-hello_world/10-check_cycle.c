#include "lists.h"
/**
 * check_cycle -  function that checks if a
 * singly linked list has a cycle in it
 * @list: head of linked list
 * Return: 1 if a cycle, 0 if not a cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *first, *second;

	if (list == NULL)
	{
		return (0);
	}
	first = list;
	second = list->next;
	while (first != NULL && second != NULL && second->next != NULL)
	{
		if (first == second)
		{
			return (1);
		}
		first = first->next;
		second = second->next->next;
	}
	return (0);
}
