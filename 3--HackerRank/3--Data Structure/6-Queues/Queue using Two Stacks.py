# Enter your code here. Read input from STDIN. Print output to STDOUT
class Solve:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        self.items.pop(0)

    def print_front_val(self):
        print(self.items[0])


if __name__ == "__main__":
    solve = Solve()
    queries = int(input())
    for i in range(queries):
        query = input()
        if int(query[0]) is 1:
            a, x = map(int, query.split())
            solve.enqueue(x)
        elif int(query[0]) is 2:
            solve.dequeue()
        else:
            solve.print_front_val()
