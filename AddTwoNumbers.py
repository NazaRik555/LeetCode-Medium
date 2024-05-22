
def addTwoNumbers(l1,l2):
        lst1 = ''
        lst2 = ''
        l1.reverse()
        l2.reverse()
        for el1, el2 in zip(l1, l2):
            lst1+=str(el1)
            lst2+=str(el2)
        a = int(lst1)+int(lst2)
        a = str(a)
        print (''.join(reversed(a)))

l1 = [2,4,3]
l2 = [5,6,4]
addTwoNumbers(l1,l2)