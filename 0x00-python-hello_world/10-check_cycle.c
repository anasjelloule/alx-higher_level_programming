#include "lists.h"

/**
 * check_cycle - checks if a singly linked list had a cycle in it
 * @list: singly linked list
 * Return: if there is no cycle, 1 if there is a cycle
 */

int check_cycle(listint_t *list)
{
	listint_t *slw = list;
	listint_t *fst = list;

	if (list == NULL)
		return (0);

	while (fst != NULL && fst->next != NULL)
	{
		slw = slw->next;
		fst = fst->next->next;
		if (slw == fst)
		  return (1);
	}
	return (0);
}
