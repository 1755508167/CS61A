class Link:
    empty=()
    def __init__(self,first,rest=empty):
        assert rest is Link.empty or isinstance(rest,Link)
        self.first=first
        self.rest=rest
    def __repr__(self):
        if self.rest:
            rest_repr=','+repr(self.rest)
        else:
            rest_repr=''
        return "Link("+repr(self.first)+rest_repr+")"
    def __str__(self):
        string='<'
        while self.rest is not Link.empty:
            string +=str(self.first)+' '
            self=self.rest
        return string+str(self.first)+'>'

def square(x):
    return x**2
def odd(x):
    return x % 2 == 1

def range_link(start,end):
    """
    返回一个链表形式的rangee()
    """
    if start >= end:
        return Link.empty
    else:
        return Link(start,range_link(start+1,end))

def add(s,v):
    """s是一个链表(内部元素有序)，v是一个数，将v无重复的添加到链表s中
    如果v已经存在于s中，则直接return s就可以了
    """
    assert s is not Link.empty
    #检查v是否存在于s中
    if s.first > v:
        #print(s.first,s.rest)
        s.first,s.rest=v,Link(s.first,s.rest)
    elif s.first < v and s.rest is Link.empty:
        s.rest=Link(v)
    elif s.first < v:
        add(s.rest,v)
    return s

s=Link(1,Link(3,Link(5)))
result=add(s,0)
print(result)


class Tree:
    def __init__(self):
        pass
    def __repr__(self):
        pass