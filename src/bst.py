#!/usr/bin/env python3

import bt
import sys
import logging
import itertools

log = logging.getLogger(__name__)

global counter

class BST(bt.BT):
    def __init__(self, value=None):
        '''
        Initializes an empty tree if `value` is None, else a root with the
        specified `value` and two empty children.
        '''
        self.set_value(value)
        if not self.is_empty():
            self.cons(BST(), BST())

    def is_member(self, v): 
        '''
        Returns true if the value `v` is a member of the tree.
        '''
        if self.is_empty():
            return False

        if(self.value() == v):
            return True
        elif(self.lc().is_member(v)):
            return True
        elif(self.rc().is_member(v)):
            return True

        return False



    def size(self):
        '''
        Returns the number of nodes in the tree.
        '''
        
        if self.is_empty():
            return 0
        else:
            return 1 + self.lc().size() + self.rc().size()


    def height(self):
        '''
        Returns the height of the tree.
        '''
        if self.is_empty():
            return 0
        else:
            return 1 + max(self.lc().height(), self.rc().height())

            

    def preorder(self):
        '''
        Returns a list of all members in preorder.
        '''
        if self.is_empty():
            return []
        return [self.value()] + self.lc().preorder() + self.rc().preorder()

    def inorder(self):
        '''
        Returns a list of all members in inorder.
        '''
        if self.is_empty():
            return []
        
        return self.lc().inorder() + [self.value()] + self.rc().inorder() 

    def postorder(self):
        '''
        Returns a list of all members in postorder.
        '''
        if self.is_empty():
            return []
        return self.lc().postorder() + self.rc().postorder() + [self.value()]
    

    
    
    def bfs_order_star(self):
        '''
        Returns a list of all members in breadth-first search* order, which
        means that empty nodes are denoted by "stars" (here the value None).

        For example, consider the following tree `t`:
                    10
              5           15
           *     *     *     20

        The output of t.bfs_order_star() should be:
        [ 10, 5, 15, None, None, None, 20 ]
        '''
        if self.is_empty():
            return []
        
        
        queue = []
        lista_value = []
        total_nodes = (2**self.height() - 1)
        
        queue.append(self) # Först har vi root noden i kö
        while (len(queue) > 0) and (len(lista_value) < total_nodes): # While loopen läser trädet
            if queue[0] is None:
                lista_value.append(None)
            else:
                lista_value.append(queue[0].value())

            node = queue.pop(0) # Vi poppar elementet från kö
            
            if node is None or node.is_empty():
                queue.append(None)
                queue.append(None)
            else:
                queue.append(node.lc())
                queue.append(node.rc())

        
            
        return lista_value
        
        

    def add(self, v):
        '''
        Adds the value `v` and returns the new (updated) tree.  If `v` is
        already a member, the same tree is returned without any modification.
        '''
        if self.is_empty():
            self.__init__(value=v)
            return self
        if v < self.value():
            return self.cons(self.lc().add(v), self.rc())
        if v > self.value():
            return self.cons(self.lc(), self.rc().add(v))
        return self
    
    def remove_root(self):
        if self.lc().is_empty() and self.rc().is_empty(): #Case 1: If leaf - remove!
            self._value = None
            return self.cons(None, None)
        elif self.lc().is_empty() and not self.rc().is_empty(): #Case 2: If there is just right child
            self._value = self.rc().value()
            return self.cons(self.rc().lc(), self.rc().rc())
        elif self.rc().is_empty() and not self.lc().is_empty(): #Case 3: If there is just left child
            self._value = self.lc().value()
            return self.cons(self.lc().lc(), self.lc().rc())
        else:                                                   #Case 4: If there is both right and left child
            if self.lc().height() >= self.rc().height():
                self.large = self.lc().largest_node()
                self._value = self.large.value()
                self.large.remove_root()
            else:
                self.small = self.rc().smallest_node()
                self._value = self.small.value()
                self.small.remove_root()
            
            return self
            
            
        
    def smallest_node(self):
        if self.lc().is_empty():
            return self
        else:
            return self.lc().smallest_node()
        
    def largest_node(self):
        if self.rc().is_empty():
            return self
        else:
            return self.rc().largest_node()
        
    
    def delete(self, v):
        '''
        Removes the value `v` from the tree and returns the new (updated) tree.
        If `v` is a non-member, the same tree is returned without modification.
        '''
        if self.is_empty() or not self.is_member(v):
            return self
        elif v < self.value():
            return self.cons(self.lc().delete(v), self.rc())
        elif v > self.value():
            return self.cons(self.lc(), self.rc().delete(v))
        else:
            return self.remove_root()

if __name__ == "__main__":
    log.critical("module contains no main module")
    sys.exit(1)
