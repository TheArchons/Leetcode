# make sure to keep the indent level because this function is in a class
    def insert(self, val):
        curr = self.root

        if curr is None:
            self.root = Node(val)
            return

        while (True):
            if (val < curr.info):
                if (curr.left is not None):
                    curr = curr.left
                else:
                    curr.left = Node(val)
                    break
            else:
                if (curr.right is not None):
                    curr = curr.right
                else:
                    curr.right = Node(val)
                    break
