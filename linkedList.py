class Node:
    def __init__(self, node):
        self.data = node
        self.next = None


n1 = Node(10)
n2 = Node(20)
n3 = Node(30)
n4 = Node(40)
n5 = Node(50)


class linkedList:
    # print, insert, delete, search

    def __init__(self):
        self.head = None

    # print
    def print_ll(self):

        while self.head != None:
            print(self.head.data)
            self.head = self.head.next

    def print_ll(self):

        temp = self.head
        while temp != None:
            print(temp.data)
            temp = temp.next

    # insert
    def insert_after(self, data, prev_node):
        new_node = Node(data)
        temp_node = prev_node.next
        prev_node.next = new_node
        new_node.next = temp_node

        # delete
    def delete(self, position):
        temp = self.head

        if position == 1:  # 20
            self.head = temp.next
            return
        elif():
            pass
        else:
            temp = self.head  # 10
            for i in range(position-2):
                temp = temp.next  # 20
                print(".......")
                print(temp.data)
                temp.next = temp.next.next  # 30 -> 50
                print(".........")
                print(temp.next.data)
                print("Print ll after deleting element" +
                      str(position)+"position element")
            self.print_ll()

            # search

    def search(self, data):
        temp = self.head
        while temp != None:
            if(temp.data == data):
                print("element is found")
                return
            temp = temp.next
        print("element not found")


ll = linkedList()


ll.head = n1

n1.next = n2
n2.next = n3
n3.next = n4
n4.next = n5


def print_ll():
    while ll.head != None:
        print(ll.head.data)
        ll.head = ll.head.next


# ll.print_ll()
ll.insert_after(35, n3)
ll.print_ll()
ll.delete(3)
ll.search(20)
ll.search(44)
