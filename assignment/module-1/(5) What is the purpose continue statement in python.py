# Python Continue statement is a loop control statement
# The continue statement is used to end the current iteration in loop (for or while) and continues to the next iteration

for i in range(11):
    if i<5:
     continue
    print(i)

a="i learning in python"

for j in a:
   if j=='n':
    continue
   print(j,end="")