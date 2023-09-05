#include <stdio.h>
#include "lists.h"

/**
 * check_cycle - checks if a linked list has cycle
 * @list: head of list
 * Return: 1 if cycled, else 0.
*/
int check_cycle(listint_t *list)
{
    listint_t *slow, *fast;

    if (list == NULL || list->next == NULL)
    return (0);
    fast = list->next;
    slow = list;

    while ((fast != NULL && fast->next != NULL && slow)) {
    if (slow == fast)
    {
        return (1);
    }
    slow = slow->next;
    fast = fast->next->next;
    }
    return (0);
}
