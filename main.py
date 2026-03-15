from linked_list import LinkedList

if __name__ == "__main__":
    """
    Use this file to create a LinkedList instance and perform operations 
    like insertion, recursion-based sum, search, and reverse.
    """

    # TODO: 1) Create a LinkedList instance
    linked_list = LinkedList()
    

    # TODO: 2) Insert some sample data using insert_at_front or insert_at_end
    linked_list.insert_at_front(5)
    linked_list.insert_at_end(3)
    
    # TODO: 3) Display the list to verify insertion
    print(linked_list.display())
    

    # TODO: 4) Call recursive_sum and print the result
    print(linked_list.recursive_sum())
    

    # TODO: 5) Call recursive_search with a target and print result
    print(linked_list.recursive_search(5))

    # TODO: 6) Call recursive_reverse, then display the reversed list
    print(linked_list.recursive_reverse().display())
    


# 