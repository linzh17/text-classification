from random import shuffle
f = open('testdata/testlabel.txt')
f2 = open('testdata/testdata.txt')
f3 = open('testdata/new_testdata.txt','a')
f4 = open('testdata/new_testlabel.txt','a')
lists = []
data = []
label = []
while 1:
    
    line1 = f.readline()
    line2 = f2.readline()
    if not line1:
        break
    dict = {'data':line2.strip('\n'),'label':line1.strip('\n')}
    lists.append(dict)
    
#print (list)
#shuffle(list)
#lists.pop()
shuffle(lists)
for list in lists:
    data.append(list['data'])
    label.append(list['label'])
    #f3.write(list['data'])
    #f4.write(list['label'])

f3.write('\n'.join(data))
f4.write('\n'.join(label))

print(len(data))
'''i=0
for i in range(29857):
    #i = i+1
    print(i)
    print(data[i])
    if data[i] == '':
        print(i)
        break
    f3.write(data[i])
for label1 in label:
    f4.write(label1)
'''

