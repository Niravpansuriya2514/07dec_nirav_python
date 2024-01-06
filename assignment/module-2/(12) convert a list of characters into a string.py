characters=[]

n=int(input("how many charecter enter in your list: "))

for i in range(n):
    x=input(f"enter character {i+1}: ")
    characters.append(x)
print(characters)

str=""
for i in characters:
    str+=i
print(str)


