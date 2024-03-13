#include <stdio.h>
#include "lists.h"

/**
 *insert_node = A list of integers
 *@number: The number to be inserted
 *@head: The head of the listint_t list.
 *
 *Return: The address of the new node, or NULL if it failed
 *
 *
*/

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *insert_node = malloc(sizeof(listint_t));

	if (insert_node == NULL)
	{
		return (NULL);
	}
	insert_node->n = number;
	insert_node->next = *head;
	*head = insert_node;
	return (insert_node);
}
