#include "lists.h"

/**
 * check_cycle - checks if a singly linked list has a cycle
 * @head: pointer to the head of the linked list
 * Return: 1 if a cycle is present, 0 otherwise
 */
int check_cycle(listint_t *head)
{
	listint_t *slow_runner = head;
	listint_t *fast_runner = slow_runner;

	while (slow_runner && fast_runner && fast_runner->next)
	{
		slow_runner = slow_runner->next;
		fast_runner = fast_runner->next->next;
		if (slow_runner == fast_runner)
			return (1);
	}
	return (0);
}
