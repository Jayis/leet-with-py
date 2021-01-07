class MaxHeap():
    def __init__(self):
        self.heap = [] ## 0-index

    def max(self):
        if len(self.heap) > 0:
            return self.heap[0].val
        else:
            return 0

    def add(self, h):
        node = Nodes(len(self.heap), h)
        self.heap.append(node)

        self.update(node)

        return node

    def remove(self, node):
        last_node = self.heap.pop(-1)
        if node.ind < len(self.heap):
            self.heap[node.ind] = last_node
            last_node.ind = node.ind
            self.update(last_node)

    def update(self, node):            
        ## go up
        if node.ind > 0:
            parent_node = self.heap[(node.ind - 1)//2]
            if node.val > parent_node.val:
                self.swap_node(node, parent_node)
                self.update(node)

        ## go down
        child_idx1, child_idx2 = node.ind*2 + 1, node.ind*2 + 2
        child_node = None
        if child_idx2 < len(self.heap):
            ## 2 child
            child_node1 = self.heap[child_idx1]
            child_node2 = self.heap[child_idx2]

            if child_node1.val > child_node2.val:
                child_node = child_node1
            else:
                child_node = child_node2

        elif child_idx1 < len(self.heap):
            ## 1 child
            child_node = self.heap[child_idx1]
        else:
            ## 0 child
            pass

        if child_node is not None and child_node.val > node.val:
            self.swap_node(node, child_node)
            self.update(node)                

    def swap_node(self, node1, node2):
        tmp_ind = node1.ind

        self.heap[node2.ind] = node1
        node1.ind = node2.ind

        self.heap[tmp_ind] = node2
        node2.ind = tmp_ind
        
    def __str__(self):
        out = []
        for node in self.heap:
            out.append(node.val)
        
        return str(out)
    
class Nodes():
    def __init__(self, ind, val):
        self.ind = ind
        self.val = val

    def __str__(self):
        return 'ind:{}, val:{}'.format(self.ind, self.val)