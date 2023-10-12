alphabets=[0,'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
word=input("Enter word:")
value=0
iter=0
for i in range(-1,-len(word)-1,-1):
    value+=alphabets.index(word[i])*(26**iter)
    iter+=1
print(value)
