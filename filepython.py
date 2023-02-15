content = file.read()

file=open('words.txt','r')
print(content)
file.close()
file =open('words.txt, a+')
file.write("\nhello")
file.close()

file=open('words.txt','r')
print(content)