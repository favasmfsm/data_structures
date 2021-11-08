import stack
import random
#finding max of an array at O(1) 
array=[]
max_stk = stack.Stack()
max_stk.push(-1)
for i in range(30):
    k=random.randint(1,50)
    array.append(k)
    if(k > max_stk.peep()):
        max_stk.push(k)

print(array)
print(max_stk.peep())