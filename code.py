filenames = ['a.txt', 'b.txt', "c.txt"]

for i in filenames:
    file = open(i,'r')
    content=file.read()
    print(content)
