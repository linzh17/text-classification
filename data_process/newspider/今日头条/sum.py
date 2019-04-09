f = open('testdata/testlabel.txt')
it = car = money = war = travel = sport = health = ent = fashion = 0
f_lines = f.read().split('\n')
for f_line in f_lines:
    #print(f_line)
    if f_line == '1':
        car = car + 1
    elif f_line == '2':
        money = money + 1
    elif f_line == '10':
        ent = ent + 1
    elif f_line == '8':
        war = war + 1
    elif f_line == '3':
        it = it + 1
    elif f_line =='5':
        sport = sport+1
    elif f_line =='4':
        health = health + 1
    elif f_line == '11':
        fashion = fashion + 1
    elif f_line == '6':
        travel = travel + 1

print('car',car)
print('money',money)
print('ent',ent)
print('war',war)
print('it',it)
print('sport',sport)
print('health',health)
print('fashion',fashion)
print('travel',travel)