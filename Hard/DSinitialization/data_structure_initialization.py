#Initializing Singly Linked List
class Node:
    def __init__(self,val = 0):
        self.val = val
        self.next = None

class Linkedlist:
    def append(self,arr):
        if arr:
            head = Node(arr[0])
        else:
            head = Node()
        curr = head
        for ele in arr[1:]:
            curr.next = Node(ele)
            curr = curr.next


        return head

#Initializing Binary Tree
import collections
# define tree
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class BinaryTree:
    #Converting Leetcode's level order traversal
    def deserialize(self, string):
        if string == '{}':
            return None
        nodes = [None if val == 'null' else TreeNode(int(val))
                 for val in string.strip('[]{}').split(',')]
        kids = nodes[::-1]
        root = kids.pop()
        for node in nodes:
            if node:
                if kids: node.left = kids.pop()
                if kids: node.right = kids.pop()
        return root

    def drawtree(self, root):
        def height(root):
            return 1 + max(height(root.left), height(root.right)) if root else -1

        def jumpto(x, y):
            t.penup()
            t.goto(x, y)
            t.pendown()

        def draw(node, x, y, dx):
            if node:
                t.goto(x, y)
                jumpto(x, y - 20)
                t.write(node.val, align='center', font=('Arial', 12, 'normal'))
                draw(node.left, x - dx, y - 60, dx / 2)
                jumpto(x, y - 20)
                draw(node.right, x + dx, y - 60, dx / 2)

        import turtle
        t = turtle.Turtle()
        t.speed(0);
        turtle.delay(0)
        h = height(root)
        jumpto(0, 30 * h)
        draw(root, 0, 30 * h, 40 * h)
        t.hideturtle()
        turtle.mainloop()