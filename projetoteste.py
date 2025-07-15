pes = {}
v = 0
while True:
    pes['gmail'] = str(input('gmail: '))
    if '@' in pes['gmail']:
        v = 1
    else:
        v = 0
    pes['idade'] = int(input('Idade: '))
    if 0 < pes['idade']:
        v = 1
    else:
        v = 0
    pes['Nome'] = str(input('Nome: '))

    if v == 1:
        break
    else:
        print('Faz de novo mula')
print(pes)
for c, v in pes:
    print(c)
