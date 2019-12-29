import math

###################################################
#
# Data structure, def for singly-linked
# list and some useful functions
#
###################################################

# Definition for singly-linked list:
# A singly-linked is None or ListNode(node, a singly-linked) 
# where node is a python object
class ListNode(object):
    def __init__(self, x, rest=None):
        self.val = x
        self.next = rest
        
# A positive integer is represented by a ListNode
# such that each node is a digit in the following manner:
# ListNode(1, None) is 1
# ListNode(1, ListNode(2, None)) is 21
# ListNode(1, ListNode(2, ListNode(3, None)) is 321
    
# ListNodeToNum : ListNode --> int
# returns the numerical value of a positive integer
# represented by a singly-linked list LNode
def ListNodeToNum(LNode):
    
    # base case where LNode represents a single digit
    n = LNode.val
    curNode = LNode.next
    i = 1
    
    # recursively add to n more digits from LNode
    # until curNode becomes None
    while curNode != None:
        n = n+ (10 ** i) * curNode.val
        curNode = curNode.next
        i += 1

    return n

# numToListNode : int --> ListNode
# construct a singly-linked list to represent the 
# number num
def numToListNode(num):
    if num == 0: # base case
        return ListNode(0)
    else:
        
        # initialize the exponent e = int(log10(num)), 
        # i.e. (the number of digits of num) - 1
        # the ans to be returned
        e = int(math.log10(num))
        ans = ListNode(int(num/ 10 ** int(math.log10(num))))
        num = num - ans.val * (10 ** e)
        e -= 1
        
        # recursively contruct the singly-linked list
        # until all digits are exhausted i.e. e < 0
        while e >= 0:
            if num > 0:
                curNode = ListNode(int(num/ 10 ** e))
            else:
                curNode = ListNode(0)
            
            num = num - curNode.val * (10 ** e)
            e -= 1
            
            curNode.next = ans
            ans = curNode

        return ans

###################################################
#
# addTwoNumbers adds two numbers represented
# by singly-linked list and return a 
# singly-linked list that represents the result
#
###################################################

# addTwoNumbers : ListNode, ListNode, int, --> ListNode
# carrying is a flag to indicate if sum of two digits
# is larger than 10 so that 1 is added to the next
# digit
# result of l1 + l2 is returned as a ListNode
def addTwoNumbers(l1, l2, carrying=0):
    # ans is to be returned
    # cur_digit (current digit) is used for loop/recursion
    # initialize
    ans = ListNode(0)
    cur_digit = ans 

    while l1 != None:
        if l2 == None: # None is treated as ListNode(0) i.e. None is 0
            l2 = ListNode(0)
        
        # computes the sum of the two current digit
        cur_sum = l1.val + l2.val + carrying
        if cur_sum < 10: 
            new_digit = ListNode(cur_sum)
            carrying = 0
        else:
            new_digit = ListNode(cur_sum % 10) # takes the one's position digit
            carrying = 1

        l1 = l1.next
        l2 = l2.next

        cur_digit.next = new_digit # append the new digit
        cur_digit = cur_digit.next # moves one digit down
    
    # from the end of the last while loop, l1 is None
    # if l2 is not None, call the function again and switch the position of
    # l1 and l2 in the argument so that the above code can be recycled
    if l2 != None:
        cur_digit.next = addTwoNumbers(l2, None, carrying=carrying)
    # otherwise if carrying, add the carried 1
    elif carrying:
        cur_digit.next = ListNode(1)

    return ans.next

# test to add i + j for
# i in range(0, 1000) and
# j in range(0, 1000)
# print the result of addTwoNumbers if its added incorrectly
def test_addTwoNumbers():
    for i in range(0, 1000):
        for j in range(0, 1000):
            a = ListNodeToNum(addTwoNumbers(numToListNode(i), numToListNode(j))) 
            if a != i + j:
                print(a)


#test_addTwoNumbers()