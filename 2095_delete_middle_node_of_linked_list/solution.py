class Solution:
    def deleteMiddle(self, head):
        # navigate to end of list, keep a second node that updates once every 
        # two times lead mode does.

        if (head.next == None):
            return None

        node = head
        prevMidNode = head
        while (node != None):
            node = node.next
            if (node != None):
                node = node.next
                # Delay the first iteration so that prevMidNode remains the node before the mid node.
                if (node != prevMidNode.next.next):
                    prevMidNode = prevMidNode.next
            
        if (prevMidNode.next == None):
            return prevMidNode
        prevMidNode.next = prevMidNode.next.next
        return head

    def solve(self, inputs):
        return self.deleteMiddle(inputs['head'])
