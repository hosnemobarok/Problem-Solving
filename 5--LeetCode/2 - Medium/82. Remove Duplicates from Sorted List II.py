'''
 Not Accepted
'''

# Remove_Duplicates function work
from collections import Counter

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Linkedlist:
    def __init__(self):
        self.head = None

    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node



    def Remove_Duplicates(self):
        arr = []
        current = self.head
        while current is not None:
            arr.append(current.data)
            current = current.next

        res = Counter(arr)
        for i in res:
            if res[i] == 2:
                continue

            print(i, end=" ")


    '''def deleteDuplicates(self):
        current_node = self.head
        d = []
        s = []
        while current_node is not None:
            if current_node.data not in d:
                d.append(current_node.data)
            else:
                s.append(current_node.data)

            current_node = current_node.next


        for j in d:
            if j not in s:
                print(j, end=" ")'''
if __name__ == '__main__':
    ll = Linkedlist()
    arr = [1, 2, 3, 3, 4, 4, 5]
    #arr = [1, 1, 1, 2, 3]
    for i in arr[::-1]:
        ll.push(i)

    ll.Remove_Duplicates()
