import math
import pdb
import random

#general purpose min max heap, used for 60sec sliding window and extracting the median
class min_max_heap:
    def __init__(self):
        self.arr = [0]
        self.val = [None]
        self.size = 0

    def is_empty(self):
        return self.size == 0

    def construct_heap(self,keys,vals):
        assert(len(keys) == len(vals))

        self.arr = [0] + keys
        self.val = [None] + vals
        self.size = len(keys)

        i = self.size//2
        while i > 0:
            self.trickledown(i)
            i -= 1

    def insert(self,key,val):
        self.arr.append(key)
        self.val.append(val)
        self.size += 1
        
        self.bubbleup(self.size)

    def delete_min(self):
        if not self.is_empty():
            min_val = self.val[1]
            self.__swap(1,self.size)
            self.size -= 1
            self.arr.pop()
            self.val.pop()

            self.trickledown(1)

            return min_val
        else:
            return None

    def delete_max(self):
        if not self.is_empty():
            if self.size > 2:
                max_ix = 2 if self.arr[2] > self.arr[3] else 3
            elif self.size > 1:
                max_ix = 2 
            else:
                max_ix = 1

            max_val = self.val[max_ix]
            self.__swap(max_ix,self.size)
            self.size -= 1
            self.arr.pop()
            self.val.pop()

            self.trickledown(max_ix)
            
            return max_val
        else:
            return None

    def get_min(self):
        return self.val[1] if self.size > 0 else None

    def get_max(self):
        if self.size > 2:
            return max(self.val[2],self.val[3])
        elif self.size > 1:
            return self.val[2]
        elif self.size > 0:
            return self.val[1]
        else:
            return None

    #returns indexes and values of children and grandchildren
    def children_grandchildren(self,i):
        children = [2*i,2*i+1]
        left_gc = [2*c for c in children] 
        right_gc = [2*c + 1 for c in children]
       
        indexes = filter(lambda x: x <= self.size,children + left_gc + right_gc)
        values = map(lambda x:self.arr[x], indexes)
        return indexes,values

    #returns the index of the largest child/grandchild 
    def largest_child_grandchild(self,i):
        indexes,values = self.children_grandchildren(i)
        indexes_values = zip(indexes,values)
        indexes_values.sort(key=lambda x:x[1])

        return indexes_values[-1][0]
    #returns the index of the smallest child/grandchild 
    def smallest_child_grandchild(self,i):
        indexes,values = self.children_grandchildren(i)
        indexes_values = zip(indexes,values)
        indexes_values.sort(key=lambda x:x[1])

        return indexes_values[0][0]

    #swaps key and value
    def __swap(self,i,k):
        tmp = self.arr[i]
        self.arr[i] = self.arr[k]
        self.arr[k] = tmp

        tmp_val = self.val[i]
        self.val[i] = self.val[k]
        self.val[k] = tmp_val

    def __parent(self,i):
        return i//2

    def __grandparent(self,i):
        return self.__parent(i)//2

    #general trickle down
    def __minlevel(self,i):
        level = math.floor(math.log(i,2))
        return level % 2 == 0

    def trickledown(self,i):
        if self.__minlevel(i) == True:
            self.trickledownmin(i)
        else:
            self.trickledownmax(i)

    #trickle down for min heap
    def trickledownmin(self,i):
        #has children
        if 2*i <= self.size: 
            m = self.smallest_child_grandchild(i)
            
            #if grand child
            if m > 2*i + 1:
                if self.arr[m] < self.arr[i]:
                    self.__swap(m,i)
                    if self.arr[m] > self.arr[self.__parent(m)]:
                        self.__swap(m,self.__parent(m))
                    self.trickledownmin(m)
            #is a child
            else:
                if self.arr[m] < self.arr[i]:
                    self.__swap(m,i)

    #trickle down for max heap
    def trickledownmax(self,i):
        #has children
        if 2*i <= self.size: 
            m = self.largest_child_grandchild(i)
            
            #if grand child
            if m > 2*i + 1:
                if self.arr[m] > self.arr[i]:
                    self.__swap(m,i)
                    if self.arr[m] < self.arr[self.__parent(m)]:
                        self.__swap(m,self.__parent(m))
                    self.trickledownmax(m)
            #is a child
            else:
                if self.arr[m] > self.arr[i]:
                    self.__swap(m,i)


    def bubbleup(self,i):
        if self.__minlevel(i):
            if i > 1 and self.arr[i] > self.arr[self.__parent(i)]:
                self.__swap(i,self.__parent(i))
                self.bubbleupmax(self.__parent(i))
            else:
                self.bubbleupmin(i)
        else:
            if i > 1 and self.arr[i] < self.arr[self.__parent(i)]:
                self.__swap(i,self.__parent(i))
                self.bubbleupmin(self.__parent(i))
            else:
                self.bubbleupmax(i)

    def bubbleupmax(self,i):
        #has grandparents    
        if i > 3:
            if self.arr[i] > self.arr[self.__grandparent(i)]:
                self.__swap(i,self.__grandparent(i))
                self.bubbleupmax(self.__grandparent(i))

    def bubbleupmin(self,i):
        #has grandparents    
        if i > 3:
            if self.arr[i] < self.arr[self.__grandparent(i)]:
                self.__swap(i,self.__grandparent(i))
                self.bubbleupmin(self.__grandparent(i))
       
if __name__ == '__main__':
    heap = min_max_heap()
    vals = [random.randint(1,100) for i in range(16)]

    heap.construct_heap(vals,vals)
    print heap.arr

    while not heap.is_empty():
        heap.delete_max()
        print "min: {} max: {}".format(heap.get_min(),heap.get_max())
        print heap.arr
    

