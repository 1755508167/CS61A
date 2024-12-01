class Link:
    empty=()
    def __init__(self,first,rest=empty):
        assert rest is Link.empty or isinstance(rest,Link)
        self.first=first
        self.rest=rest
    def __repr__(self):
        def helper(l):
            if len(l) > 1:
                s = ('Link({},{})'.format(l[0], helper(l[1:])))
                return s
            elif len(l) == 1:
                return 'Link({})'.format(l[0])
            else:
                return ''
        #先转化为普通列表
        l=[self.first]
        while True:
            if self.rest != Link.empty:
                l.append(self.rest.first)
                self.rest=self.rest.rest
            else:
                break
        s=helper(l)
        return s

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
