#include <stdlib.h>
#include <string.h>
#include <stdio.h>
#include "lists.h"
/**
 * instert_node - inserts in ordered list
 * @head: head of list
 * @number: number to put in
 * Return: address of new node
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *tmmp,*anas;

	tmmp = *head;
	anas = malloc(sizeof(listint_t));
	if(anas == NULL)
		return(NULL);
	anas->n = number;
	anas->next = NULL;
	if((*head) == NULL)
	{
		*head = anas;
		return(anas);
	}
	else if((*head)->n >= number)
	{
		anas->next = *head;
		*head = anas;
		return(anas);
	}
	else
	{
		while(tmmp->next != NULL)
		{
			if(tmmp->next->n >= number)
			{
			       anas->next = tmmp->next;
				tmmp->next = anas;
				return (anas);
			}
			tmmp = tmmp->next;
		}
		anas->next = NULL;
		tmmp->next = anas;
		return(anas);
	}
	return(NULL);
}
