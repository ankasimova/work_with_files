# f = open('example.txt', 'w')
# f.write('Hello, World!')
# f.close()

f = open('example.txt')
for row in f:
    print(row)