import ctypes

class Empty(Exception):
    pass

class KindaDynamicArray:
    def __init__(self):
        self._n = 0 #liczba elementów
        self._capacity = 1 #rozmiar tablicy
        self._A = self._make_array(self._capacity) #właściwa tablica
        
    def __len__(self):
        return self._n
    
    def __getitem__(self,k):
        if not 0 <= k < self._n:
            raise IndexError('invalid index')
        return self._A[k]
    
    def append(self,obj):
        if self._n == self._capacity:
            self._resize(2*self._capacity)
        self._A[self._n] = obj
        self._n += 1
        
    def _resize(self,c):
        B = self._make_array(c)
        for k in range(self._n):
            B[k] = self._A[k]
        self._A = B
        self._capacity = c
        
    def _make_array(self,c):
        return (c*ctypes.py_object)()

    def insert(self,index,value):
        self._A[index] = value
    
    def __str__(self):
        represent = ""
        for i in range(self._n):
            represent+=f"{self._A[i]},"
        return(represent)


class BinaryTree:
    """
    Contains various functions to perform operations on binary tree represented in array.
    """
    def __init__(self):
        self.tree = KindaDynamicArray()
        self.size = 0

    def __len__(self):
        """
        Function return length of binary tree

        Args:
            No argument

        Returns:
            int: length of binary tree
        """
        return len(self.tree)
    
    def add(self, pos, el):
        """
        Function adds element el on position pos.

        If length equals 0 function adds el on position 0. 
        If for node on position pos parent do not exsist rasie Exception.

        Args:
            pos (int): postion on which the element will be add
            el (any): function adds this element to tree
        """
        if len(self.tree) == 0:
            self.size += 1
            self.tree.append(el)
        elif pos < len(self.tree):
            if pos%2==0:
                parent = int((pos-2)/2)
            else:
                parent = int((pos-1)/2)
            if self.tree[parent]==None:
                raise Exception("index is not empty")
            else:
                if (pos-1)/2==None or (pos-2)/2==None:
                    raise Exception("pos has no parent")    
                else:
                    self.tree.insert(pos, el)
        else:
            if pos%2==0:
                parent = int((pos-2)/2)
            else:
                parent = int((pos-1)/2)
            if self.tree[parent]==None:
                raise Exception("pos has no parent") 
            else:
                for i in range(pos-self.size+1):
                    if 1<pos-self.size+1:
                        self.size += 1
                        self.tree.append(None)
                    else:
                        self.size += 1
                        self.tree.append(el)

    def set(self, pos, el):
        """
        Function changes element on position pos to element el. 

        If position is empty raise Exception.

        Args:
            pos (int): postion on which the given element will be add
            el (any): function changes old element on given position to el
        """
        if pos<len(self.tree):
            self.tree.insert(pos, el)
        else:
            raise Exception("there is no such index as given pos") 

    def pop(self, pos):
        if pos<len(self.tree):
            return self.tree[pos]
        else:
            raise Exception("there is no such index as given pos") 
        

    def remove(self, pos):
        """
        Function removes branch that stars with given position pos.

        Args:
            pos (int): position from which the function deletes branches and leafs
        """
        def remove_children(node, size):
            self.tree.insert(node, None)
            if (2*node)+1 <= size:                
                self.tree.insert((2*node)+1,None)
                remove_children((2*node)+1, size)
                if (2*node)+2 <= size:                
                    self.tree.insert((2*node)+2,None)
                    remove_children((2*node)+2, size)
        if pos<len(self.tree):
            remove_children(pos, len(self.tree)-1)
        else:
            raise Exception("there is no such index as given pos") 

    def get_left_child(self, pos):
        """
        Functions return element on position of left child of given pos.

        Args:
            pos (int): position of element from which the left child is taken

        Returns:
            any : element on the postion of left child of the position pos
        """
        if pos<len(self.tree):
            if (2*pos)+1 < len(self.tree):
                return self.tree[(2*pos)+1]
            else:
                return 
        else:
            raise Exception("there is no such index as given pos")

    def get_right_child(self, pos):
        """
        Functions return element on position of right child of given pos.

        Args:
            pos (int): position of element from which the right child is taken

        Returns:
            any: element on the postion of right child of the position pos
        """
        if pos<len(self.tree):
            if (2*pos)+2 < len(self.tree):
                return self.tree[(2*pos)+2]
            else:
                return 
        else:
            raise Exception("there is no such index as given pos")
            
    def has_left_child(self, pos):
        """
        Functions checks if the node has left child.

        Args:
            pos (int): position of element from which the information on the left child is taken

        Returns:
            bool : true if pos has left child, false if pos does not have left child
        """
        if pos < len(self.tree):
            if (2*pos)+1 < len(self.tree):
                if self.tree[(2*pos)+1]!=None:
                    return True
                else: 
                    return False
            else:
                return False
        else:
            raise Exception("there is no such index as given pos")

    def has_right_child(self, pos):
        """
        Functions checks if the node has right child.

        Args:
            pos (int): position of element from which the information on the right child is taken

        Returns:
            bool : true if pos has right child, false if pos does not have right child
        """
        if pos < len(self.tree):
            if (2*pos)+2 < len(self.tree):
                if self.tree[(2*pos)+2]!=None:
                    return True
                else: 
                    return False
            else:
                return False

        else:
            raise Exception("there is no such index as given pos")

    def get_left_child_pos(self,pos):
        """
        Funtion returns position of the left child of given pos.

        Args:
            pos (int): position of the parent of the left child function is looking

        Returns:
            int : position of the left child of given parent on position pos
        """
        if pos<len(self.tree):
            if (2*pos)+1 < len(self.tree):
                return (2*pos)+1
            else:
                return
        else:
            raise Exception("there is no such index as given pos")

    def get_right_child_pos(self,pos):
        """
        Funtion returns position of the right child of given pos.

        Args:
            pos (int): position of the parent of the right child function is looking

        Returns:
            int : position of the right child of given parent on position pos
        """
        if pos<len(self.tree):
            if (2*pos)+2 < len(self.tree):
                return (2*pos)+2
            else:
                return False
        else:
            raise Exception("there is no such index as given pos")

    def inorder(self):
        """
        Function returns elements of tree in inorder.

        Args:
            Function takes no args.

        Returns:
            str : string of elements in inorder
        """
        def inner_inorder(pos, traveled: list):
            if pos>len(self.tree)-1:
                return 
            inner_inorder((2*pos)+1, traveled)
            traveled.append(self.tree[pos])
            inner_inorder((2*pos)+2, traveled)
            return traveled
        elements_array = inner_inorder(0, [])
        elements = ','.join(str(x) for x in elements_array)
        return elements

    def preorder(self):
        """
        Function returns elements of tree in preorder.

        Args:
            Function takes no args.

        Returns:
            str : string of elements in preorder
        """
        def inner_preorder(pos, traveled: list):
            if pos>len(self.tree)-1:
                return 
            traveled.append(self.tree[pos])
            inner_preorder((2*pos)+1, traveled)
            inner_preorder((2*pos)+2, traveled)
            
            return traveled
        elements_array = inner_preorder(0, [])
        elements = ','.join(str(x) for x in elements_array)
        return elements

    def display(self):
        def height(pos):
            if (2*pos+1)<len(self.tree) and (2*pos+2)>=len(self.tree):
                return 1 + height(self.tree[(2*pos)+1] if self.tree[(2*pos)+1] is not None else 0)
            if (2*pos+1)>=len(self.tree) and (2*pos+2)<len(self.tree):
                return 1 + height(self.tree[(2*pos)+2] if self.tree[(2*pos)+1] is not None else 0)
            if (2*pos+1)>=len(self.tree) and (2*pos+2)>=len(self.tree):
                return 1
            if (2*pos+1)<len(self.tree) and (2*pos+1)<len(self.tree):
                return 1 + max(height(self.tree[(2*pos)+1]) if self.tree[(2*pos)+1] is not None else 0, height(self.tree[(2*pos)+2]) if self.tree[(2*pos)+1] is not None else 0)
        nlevels = height(0)
        width =  pow(2,nlevels+1)

        q = [(0,0,width,'c')]
        levels=[]

        while(q):
            index, level, x, align = q.pop(0)
            if index<len(self.tree):            
                if len(levels)<=level:
                    levels.append([])
            
                levels[level].append([self.tree[index],level,x,align])
                seg = width//(pow(2,level+1))
                if (2*index)+1<len(self.tree):
                    q.append(((2*index)+1,level+1,x-seg,'l'))
                    if (2*index)+2<len(self.tree):
                        q.append(((2*index)+2,level+1,x+seg,'r'))

        for i,l in enumerate(levels):
            pre = 0
            preline = 0
            linestr = ''
            pstr = ''
            seg = width//(pow(2,i+1))
            for n in l:
                valstr = str(n[0])
                if n[3] =='r':
                    linestr +=' '*(n[2]-preline-1-seg-seg//2)+ '¯'*(seg +seg//2)+'\\'
                    preline = n[2] 
                if n[3]=='l':
                    linestr+=' '*(n[2]-preline-1)+'/' + '¯'*(seg+seg//2)  
                    preline = n[2] + seg + seg//2
                pstr +=' '*(n[2]-pre-len(valstr))+valstr 
                pre = n[2]
            print(linestr)
            print(pstr)   
        
    def __str__(self):
        represent = ""
        for i in range(self.size):
            if i==self.size-1:
                represent+=f"{self.tree[i]}"
            else:
                represent+=f"{self.tree[i]},"
        return represent


# Driver code

if __name__=="__main__":
    t = BinaryTree()
    for i in range(10):
        t.add(i,i+1)
    # print(t)
    # t.display()
    D = BinaryTree()
    l = [30, 40, 24, 58, 48, 26, 11, 13]
    index = 0
    for item in l:
        D.add(index, item)
        D.display()
        index += 1

    
