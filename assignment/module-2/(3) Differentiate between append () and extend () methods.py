        #  APPPEND ()              EXTENd ()
#                           |
#(1)use in add one object   | (1)use in merge a two list
#   in one list             |
#(2)default object add in   | (2)default list add in last
#   last eliment            |    in first list


# use append() function in one list

list=['python','c','c++','java','android']
print("list before add object")
print(list)
list.append("php")
print("list after add object")
print(list)

# use extend() function in add other list
print("your nuw list")
list2=['flutter','node js','react js']
print(list2)
list.extend(list2)
print("merge in new list and first list")
print(list)