# class for creating nodes
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


# function for printing linked list
def printLinkedList(temp):
    while temp is not None:
        print(temp.data, end="")
        temp = temp.next
        if temp is not None:
            print("->", end="")
    print()


# function for finding length
def length(temp):
    ans = 0
    while temp is not None:
        ans += 1
        temp = temp.next
    return ans


# function for searching an element in list
def search(temp, element):
    i, ans, a = 0, 0, False
    while temp is not None:
        if temp.data == element:
            ans = i
            a = True
            break
        temp = temp.next
        i += 1
    return f"element found in index : {ans}" if a else "element not found in list"


# updating linked list
def replaceElement(temp, i, val):
    for _ in range(0, i - 1):
        temp = temp.next
    temp.data = val


# adding new element at end
def newElement(temp, val):
    newNode = Node(val)
    while temp.next is not None:
        temp = temp.next
    temp.next = newNode


# adding new element at starting
def newElementStart(temp, val):
    newNode = Node(val)
    newNode.next = temp
    return newNode


# adding new element at specific index
def newElementAtIndex(temp, i, val):
    newNode = Node(val)
    sample = temp

    if i != 0:
        for _ in range(0, i - 1):
            if temp.next is None:
                break
            temp = temp.next
        newNode.next = temp.next
        temp.next = newNode
        return sample
    else:
        newNode.next = sample
        return newNode


# creating nodes
node1 = Node("A")
node2 = Node("B")
node3 = Node("C")
node4 = Node("D")


# linking nodes
node1.next = node2
node2.next = node3
node3.next = node4


# checking
print(node1.data)
print(node2.data)
print(node2.next.data)
print(node1.next.next.data)


# by using head
head = node1

# function to print linked list
printLinkedList(head)

# finding length of linked list
print(length(head))

# search element in linked list
print(search(head, "C"))

# update linked list with new element
replaceElement(head, 4, "E")
printLinkedList(head)

# add new element at end
newElement(head, "F")
printLinkedList(head)

# add new element at start
head = newElementStart(head, "S")
printLinkedList(head)

# add new element at index
head = newElementAtIndex(head, 10, "p")
printLinkedList(head)
