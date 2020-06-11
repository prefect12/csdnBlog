
class BinaryTree:

    class Node:
        def __init__(self,num):
            self.val = num
            self.left = None
            self.right = None


    def __init__(self,num):
        self.head = self.Node(num)

    @property
    def root(self):
        return self.head

    def add(self,num):
        cur = self.head
        while True:
            if cur.val > num:
                if not cur.left:
                    cur.left = self.Node(num)
                    return
                else:
                    cur = cur.left
            if cur.val < num:
                if not cur.right:
                    cur.right = self.Node(num)
                    return
                else:
                    cur = cur.right
            else:
                raise ValueError('number is already exists')

    def delete(self,num):

        def deleteNode(node):
            if not node.left:
                return node.right
            if not node.right:
                return node.left
            cur = node.right
            while cur.left:
                cur = cur.left
            cur.left = node.left
            return node.right

        def aux(root):
            if not root:
                return None
            if root.val == num:
                self.flag = 1
                return deleteNode(root)
            root.left = aux(root.left)
            root.right = aux(root.right)
            return root
        self.flag = 0
        self.head = aux(self.head)
        if self.flag == 0:
            raise ValueError('number not exists')

    def __str__(self):
        def aux(root):
            if not root:
                return ''
            return aux(root.left) + str(root.val) + ' ' + aux(root.right)
        return aux(self.head)

Tree = BinaryTree(5)
Tree.add(3)
Tree.add(6)
# Tree.add(3)
Tree.add(1000)
Tree.delete(5)
# Tree.delete(100)
print(Tree)