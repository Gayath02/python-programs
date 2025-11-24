    #user input into a file
n=input("enter a string of sentences:")
f=open('sample.txt','w+')
f.write(n)
f.seek(0) 
data=f.read()
print(data)
f.close()
