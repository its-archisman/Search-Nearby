class PointDatabase:
    def __init__(self, pointlist):
        pointlist.sort()
        self.real=MakeTree2d(pointlist,True)
    def searchNearby(self, q, d):
        if d==0:
            return []
        x1=q[0]-d
        x2=q[0]+d
        y1=q[1]-d
        y2=q[1]+d
        g=search_2d(self.real,x1,x2,y1,y2,2)
        if g!=None:
            return g
        else:
            return []

class Node(object):

    def __init__(self, value) -> None:
        self.coor = value
        self.left = None
        self.right = None
        self.isLeaf = False
        self.limb = None


def MakeTree1d(data):   
    if not data:
        return None
    if len(data) == 1:
        node = Node(data[0])
        node.isLeaf = True
    else:
        mid = len(data)//2
        node = Node(data[mid])
        node.left = MakeTree1d(data[:mid])
        node.right = MakeTree1d(data[mid+1:])
    return node

def MakeTree2d(data, enable=True):
    
    if not data:
        return None
    if len(data) == 1:
        node = Node(data[0])
        node.isLeaf = True
    else:
        mid = len(data)//2
        node = Node(data[mid]) 
        node.left = MakeTree2d(data[:mid], enable)
        node.right = MakeTree2d(data[mid+1:], enable)
    if enable:
        node.limb = sorted(data, key=lambda x: x[1])
    return node

def inRange(point, range , check):

    if check == 1:
        x = point
        if (x >= range[0][0]  and x <= range[0][1] ) :
            return True
        else:
            return False

    elif check == 2:
        x = point[0]
        y = point[1]

        if (x >= range[0][0]   and x <= range[0][1]  and y >= range[1][0]  and y <= range[1][1] ) :
            return True
        else:
            return False

def getValue (point, enable, dim ):

    if dim == 1:
        value = point.coor
    elif dim == 2:
        if enable:
            value = point.coor[0]
        else:
            value = point.coor[1]
    return value

def Findsnode(root, p_min , p_max,dim, enable ):

    snode = root
    while snode != None:
        node = getValue(snode, enable, dim)
        if p_max < node:
            snode = snode.left
        elif p_min > node:
            snode = snode.right
        elif p_min <= node <= p_max :
            break
    return snode

def binarySearch(arr,y1,y2):
    n=len(arr)
    if arr==[] or arr[n-1][1]<y1 or arr[0][1]>y2:
        return []
    lb=0
    ub=n-1
    m=(lb+ub)//2
    
    while(lb<ub):
        if y1<arr[m][1]:
            ub=m-1
        if y1>arr[m][1]:
            lb=m+1
        if y1==arr[m][1]:
            lb=ub=m
            break
        m=(lb+ub)//2
    
    k1=lb
    if arr[k1][1]<y1:
        k1+=1

    if y1<arr[0][1]:
        k1=0
    lb=0
    ub=n-1
    m=(lb+ub)//2
    while(lb<ub):
        
        if y2<arr[m][1]:
            ub=m-1
        if y2>arr[m][1]:
           lb=m+1
        if y2==arr[m][1]:
            lb=ub=m
            break
        m=(lb+ub)//2
    k2=ub
    if arr[k2][1]>y2:
        k2-=1
    
    if y2>arr[n-1][1]:
        k2=n-1
    return arr[k1:k2+1]
        

def search_2d (tree, x1, x2, y1, y2, dim ):

    
    results = []
    snode = Findsnode(tree, x1, x2, 2, True)
    
    if snode:
        
        bol=inRange(snode.coor[0], [(x1, x2)], 1)
    if (snode == None):
        
        return results
    elif snode.coor[0]==x2 or bol:
        
        if inRange(snode.coor, [(x1, x2), (y1, y2)], 2):
            results.append(snode.coor)
        
        # Searching left part
        tl = snode.left 
        while ( tl != None ):
            if inRange(tl.coor, [(x1, x2), (y1, y2)], 2):
                results.append(tl.coor)
            
            if (x1 <= tl.coor[0]):
                if tl.right != None:
                    results += binarySearch(tl.right.limb, y1, y2)
                tl = tl.left
            else:
                tl = tl.right
        
        # Searching right part
        tr = snode.right
        
        while ( tr != None ):
            if inRange(tr.coor, [(x1, x2), (y1, y2)], 2):
                    results.append(tr.coor)
            if ( x2 >= tr.coor[0] ):
                if tr.left != None:
                    results += binarySearch(tr.left.limb, y1, y2)
                tr = tr.right
            else:
                    tr = tr.left
        return results