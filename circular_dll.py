class CircularListNode:
    def __init__(self, value):
        #storing actual data
        self.value = value

        #storing the next node 
        #initially it is set as none
        self.next_node = None

        #we will also have a previous node pointing to the previous in the list
        self.previous_node = None


class CircularDoublyLinkedList:
    def __init__(self):
        #we will have a head node which points to the first chainlink
        #in this code start_node will keep track of the the first nod ein the list(head)
        #if list is empty start node will be none
        self.start_node = None

    #we will also have a tail which points to the last chainlink
    def insert_at_end(self, value):
        #first create a new node with a given value
        new_node = CircularListNode(value)

        #second we check iif the list is empty, which means start node is none
        if self.start_node is None:
            #we only enter this if block list is empty
            #since it is empty the new node will be the only one in the lis
            #for a circular list this node points itself in both directions
            new_node.next_node = new_node
            #the next node after new node is itself
            new_node.previous_node = new_node

            #we update the start node pointer to the new node
            self.start_node = new_node

        else:
            #here in the else clause the list has contents . so the list is not empty thus we need a new node at the end
            #last node comes after start node
            #we access it by by following the previous nodeof start node
            last_node = self.start_node.previous_node
            #we link the new node to the last node
            last_node.next_node = new_node
            #new nodes previous node will point to the last node
            new_node.previous_node = last_node

            #new nodes next node should point to the start node to maintain circularity
            new_node.next_node = self.start_node

            #start nodes previous node should point to the new node
            self.start_node.previous_node = new_node

    #insering a new node with a given value
    def insert_at_beginning(self, value):
        self.insert_at_end(value)
        #we will set start node to the new node by start_node.previos_npde
        self.start_node = self.start_node.previous_node

    #remove the node with a given value
    def remove_by_value(self, value):
        #if list is empty there is nothing to remove
        if self.start_node is None:
            print("the list is empty. cannot remove any node.")
            return

        #if not we search from first node
        current_node = self.start_node

        #we will iterate through the list until we come back to start_node
        while True:
            if current_node.value == value:
                #we only enter this block if we find the node to remove
                #if the node has no next node it means its the only node
                if current_node.next_node == current_node:
                    self.start_node = None
                else:
                    #if the list has multiple nodes
                    #we need to update the links of the neighbours
                    current_node.previous_node.next_node = current_node.next_node
                    #the node after current node should now point backward to the node before the current node
                    current_node.next_node.previous_node = current_node.previous_node

                    #if we are removing the start node move the pointer forward
                    if current_node == self.start_node:
                        self.start_node = current_node.next_node

                #we can now exit the method
                return

            #move to the netx node
            current_node = current_node.next_node

            if current_node == self.start_node:
                print(f"Value {value} not found in the list.")
                break

    #display the list
    def show_list_forward(self):
        if self.start_node is None:
            print("the list is empty")
            return

        #set a temp loop to aid by assigning it to tje start node
        current_node = self.start_node

        #then we create an empty list to gather string representations of node calues
        values_list = []

        #we go through the list till start node
        while True:
            values_list.append(str(current_node.value))
            #str() is an inbuilt method that converts a value to a string
            current_node = current_node.next_node

            #we then check a condition to break the loop
            if current_node == self.start_node:
                break

        #we can format output but its not a must
        #Here's how to do it, We Join all the values in 'values_list' into a single string separated by ' -> '
        # Explanation of join inbuilt method:
        # - ' -> ' is a string separator
        # - '.join(values_list)' takes all elements in 'values_list' and joins them into a single string 
        output_string = " -> ".join(values_list)
        print(output_string)

    def show_list_backward(self):
        #if the list is empty , print a message and exit the method via (return)
        if self.start_node is None:
            print("the list is empty")
            return

        last_node = self.start_node.previous_node
        current_node = last_node
        values_list = []

        while True:
            values_list.append(str(current_node.value))
            current_node = current_node.previous_node
            if current_node == last_node:
                break

        # Join all the values in 'values_list' into a single string separated by ' <- '
        # - ' <- ' is our separator that now indicates backward direction
        output_string = " <- ".join(values_list)
        print(output_string)


if __name__ == "__main__":
    #create an instance of the CircularDoublyLinkedList class
    my_circular_list = CircularDoublyLinkedList()

    #insert some values at the end
    my_circular_list.insert_at_end("QUICK")
    my_circular_list.insert_at_end("BROWN")
    my_circular_list.insert_at_end("FOX")

    print("List after inserting at the end")
    #call the print forward method
    my_circular_list.show_list_forward()

    my_circular_list.insert_at_beginning("THE")
    print("List after inserting at the beginning:")
    my_circular_list.show_list_forward()

    print("List displayed backward:")
    my_circular_list.show_list_backward()

    my_circular_list.remove_by_value("QUICK")
    print("List after removing QUICK:")
    my_circular_list.show_list_forward()

    my_circular_list.remove_by_value("QUICK")  # Not found
    my_circular_list.remove_by_value("SLOW")   # Not found

    my_circular_list.remove_by_value("BROWN")
    print("List after removing BROWN:")
    my_circular_list.show_list_forward()

    # Attempting to empty the LList by removing the remining elements
    my_circular_list.remove_by_value("THE")
    my_circular_list.remove_by_value("FOX")
    print("List after removing all:")
    my_circular_list.show_list_forward()
