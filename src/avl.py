#!/usr/bin/env python3

import sys
import bst
import logging

log = logging.getLogger(__name__)

class AVL(bst.BST):
    def __init__(self, value=None):
        '''
        Initializes an empty tree if `value` is None, else a root with the
        specified `value` and two empty children.
        '''
        self.set_value(value)
        if not self.is_empty():
            self.cons(AVL(), AVL())

    def add(self, v):
        '''
        Example which shows how to override and call parent methods.  You
        may remove this function and overide something else if you'd like.
        '''
        log.debug("calling bst.BST.add() explicitly from child")
        bst.BST.add(self, v)
        return self.balance() 

    def bf(self):
        left_subtree = self.lc().height() if self.lc() is not None else 0
        right_subtree = self.rc().height() if self.rc() is not None else 0
        return left_subtree - right_subtree

    def balance(self):
        '''
        AVL-balances around the node rooted at `self`.  In other words, this
        method applies one of the following if necessary: slr, srr, dlr, drr.
        '''
        weight = self.bf()
        if abs(weight) != 2:
            return self

        if weight == 2:# left heavy
            if self.lc().bf() >= 0:
                return self.srr()
            else:
                return self.drr()
        else:           # right heavy
            if self.rc().bf() <= 0:
                return self.slr()
            else:
                return self.dlr()

        return self

    def slr(self):
        '''
        Performs a single-left rotate around the node rooted at `self`.
        '''
        rc = self.rc()
        self.set_rc(rc.lc())
        rc.set_lc(self)
        return rc

    def srr(self):
        '''
        Performs a single-right rotate around the node rooted at `self`.
        '''
        lc = self.lc()
        self.set_lc( lc.rc() )
        lc.set_rc( self )
        return lc

    def dlr(self):
        '''
        Performs a double-left rotate around the node rooted at `self`.
        '''
        rc = self.rc().srr()
        self.set_rc(rc)
        return self.slr()

    def drr(self):
        '''
        Performs a double-right rotate around the node rooted at `self`.
        '''
        lc = self.lc().slr()
        self.set_lc(lc)
        return self.srr()

    def delete(self, v):
        self = bst.BST.delete(self, v);
        return self.balance()

if __name__ == "__main__":
    log.critical("module contains no main module")
    sys.exit(1)
