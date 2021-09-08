#include "lists.h"
/**
 * check_cycle - check a singly linked list inside of a cycle
 * @list: pointer to list
 * Return: (1) if there is a cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *fast;
	listint_t *slow;

	slow = list;
	fast = list->next;

	if (list == NULL)
	{
		return (0);
	}
	while (slow && fast && fast->next)
	{
		if (slow == fast)
		{
			return (1);
		}
		slow = slow->next;
		fast = fast->next->next;
	}
	return (0);
}
