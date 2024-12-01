# Tree Data Abstraction
def tree(label, branches=[]):
    """Construct a tree with the given label value and a list of branches."""
    for branch in branches:
        assert is_tree(branch), 'branches must be trees'
    return [label] + list(branches)

def label(tree):
    """Return the label value of a tree."""
    return tree[0]

def branches(tree):
    """Return the list of branches of the given tree."""
    return tree[1:]

def is_tree(tree):
    """Returns True if the given tree is a tree, and False otherwise."""
    if type(tree) != list or len(tree) < 1:
        return False
    for branch in branches(tree):
        if not is_tree(branch):
            return False
    return True

def is_leaf(tree):
    """Returns True if the given tree's list of branches is empty, and False
    otherwise.
    """
    return not branches(tree)

def print_tree(t, indent=0):#提供了一种遍历树的方法
    print('  ' * indent + str(label(t)))
    for b in branches(t):
        print_tree(b, indent + 1)

def copy_tree(t):
    return tree(label(t), [copy_tree(b) for b in branches(t)])

#遍历树t
def traverse(t,out=''):
    out = out + '{}+'.format(label(t))  # 根节点的值
    if  not is_leaf(t):
        for branch in branches(t):
            new_out=out
            new_out=traverse(branch,new_out)
            #print(new_out)
    else:
        print(out[:-1])
    return out

#t = tree(5, [tree(4, [tree(1), tree(3)]), tree(2, [tree(10), tree(3)])])
#traverse(t)
#result=max_path_sum(t)
#print(result)
#print(is_tree(branches(tree(5))))

class Account():
    interest=0.02
    def __init__(self,account_holder):
        self.balance=0
        self.account_holder=account_holder

    def deposit(self, count):
        self.balance = self.balance + count

    def withdraw(self, count):
        if count > self.balance:
            return "Insufficient funds"
        else:
            self.balance = self.balance - count
            return self.balance

class CheckingAccount(Account):
    #这是一个需要收取手续费的银行
    withdraw_fee=1
    interest=0.01#利率
    def withdraw(self, count):
        # 这样使用的好处在于当Account中的withdraw方法改变时，此处也会改变
        return Account.withdraw(self,count+self.withdraw_fee)

class Bank():
    def __init__(self):
        #用于存放银行中的账户
        self.accounts=[]
    #开户
    def open_account(self,holder,amount,kind=Account):
        account=kind(holder)
        account.deposit(amount)
        self.accounts.append(account)
        return account
    #支付利息
    def pay_interest(self):
        for a in self.accounts:
            a.deposit(a.balance*a.interest)

    def too_big_to_fail(self):
        return len(self.accounts) >1

class SavingAccount(Account):
    deposit_fee=2
    def deposit(self,amount):
        return Account.deposit(self,amount-self.deposit_fee)

class AsSeenOnTvAccount(CheckingAccount,SavingAccount):
    def __init__(self,account_holder):
        self.account_holder=account_holder
        self.balance

def sprout_leaves(t, leaves):
    #先找出树中的所有叶子，然后用tree()转换为树
    def helper(branch,leaves):
        #如果是叶子的话，则把leaves加入进去，生成一个树
        if is_leaf(branch):
            t_new = tree(branch[0], [tree(i) for i in leaves])
            return t_new
        #如果不是叶子的话，继续往下遍历
        else:
            new_branches = []#用于储存新的分支
            #print('  helper branches:',branches(branch))
            for sub_branch in branches(branch):
                #print('     helper sub_branch:',sub_branch)
                new_branches.append(helper(sub_branch, leaves))
            return tree(branch[0], new_branches)  # 返回新的树，其子节点是新分支列表

    if is_leaf(t):  # 如果是叶子节点
        return tree(t[0], [tree(leaf) for leaf in leaves])  # 创建一个新的树，其子节点是leaves中的每个元素
    else:
        # 递归地为每个子树的叶子节点添加新分支
        new_branches = []
        for branch in branches(t):
            #print('branch:',branch)
            new_branches.append(helper(branch, leaves))
        #print('new_branches:',new_branches)
        return tree(t[0], new_branches)  # 返回新的树，其子节点是新分支列表

l=[2,3,4,5,6]
s="Link()"
s_1="Link({})".format(l[-1])
#print(s_1)
s_2="Link({},{})".format(l[-2],s_1)
#print(s_2)

def helper(l):
    if len(l) > 1:
        s=('Link({},{})'.format(l[0],helper(l[1:])))
        return s
    elif len(l) == 1:
        return 'Link({})'.format(l[0])
    else:
        return ''

result=helper(l)
print(result)


