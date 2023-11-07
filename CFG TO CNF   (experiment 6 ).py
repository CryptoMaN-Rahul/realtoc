import string

def remove_char(string, pos):
    new_string = ""
    for i in range(len(string)):
        if str(i) not in pos:
            new_string += string[i]
    return new_string

from itertools import permutations

NT_symbol = input("Enter the NonTerminal Symbols: ").split(" ")
T_symbol = input("Enter the Terminal Symbols: ").split(" ")

main = {}

#Eliminating NULL Production
n = []
for i in NT_symbol:
    main[i] = input(i + " -> ").split("/")

for i in main:
    for k in main[i]:
        for u in k:
            if u=="^":
                n.append(i)
                break

n = [*set(n)]
for i in main:
    for k in main[i]:
        pos = ""
        m = []
        possible_comb = []

        for u in range(len(k)):
            if k[u] in n:
                    pos += str(u)

        for b in range(len(pos)):
            temp = [''.join(p) for p in permutations(pos, b + 1)]
            possible_comb = possible_comb + temp

        for b in possible_comb:
            new_k = k
            if k != "^":
                m.append(remove_char(k, b))
        main[i] = main[i] + list(set(m))
    main[i] = [production.replace('^', '') for production in main[i]]

# Removing unit productions
unit_prod = {}

for i in NT_symbol:
    unit_prod[i] = []

for i in main:
    for b in main[i]:
        if b in NT_symbol:
            unit_prod[i].append(b)

for i in unit_prod:
    for j in unit_prod[i]:
        for k in main[i]:
            if k == j:
                main[i].remove(k)

for i in unit_prod:
    for mt in unit_prod[i]:
                for k in main[mt]:
                    main[i].append(k)

print("\nAFTER REMOVING NULL AND UNIT PRODUCTION")
for i in main:
    print(i + " -> ", end="")
    for ele in range(len(main[i])):
        if(main[i][ele]!=""):
            b = main[i][ele]
            print(b, end="/")
    print()

print("\nConverting to CNF form: ")

letter = len(string.ascii_uppercase)

for sym in NT_symbol:
    for i in range(len(main[sym])):
        b = main[sym][i]
        count_NT = 0
        count_T = 0

        for j in b:
            if j.isupper():
                count_NT += 1
            elif j.islower():
                count_T += 1

        if count_NT == 3:
            New_NT = string.ascii_uppercase[letter - 1]
            letter -= 1
            NT_symbol.append(New_NT)
            main[New_NT] = [b[0:2]]
            main[sym][i] = New_NT + b[2]

        elif count_T == 1 and count_NT == 2:
            New_NT = string.ascii_uppercase[letter - 1]
            letter -= 1
            NT_symbol.append(New_NT)
            main[New_NT] = [b[0]]
            New_NT2 = string.ascii_uppercase[letter - 1]
            letter -= 1
            NT_symbol.append(New_NT2)
            main[New_NT2] = [b[1:]]
            main[sym][i] = New_NT + New_NT2

        elif count_T == 1 and count_NT == 1:
            New_NT = string.ascii_uppercase[letter - 1]
            letter -= 1
            NT_symbol.append(New_NT)
            main[New_NT] = [b[0]]
            main[sym][i] = New_NT + b[1]
        
        elif count_T == 2 and count_NT == 1:
            New_NT = string.ascii_uppercase[letter - 1]
            letter -= 1
            NT_symbol.append(New_NT)
            main[New_NT] = [b[0]]
            New_NT1 = string.ascii_uppercase[letter - 1]
            letter -= 1
            NT_symbol.append(New_NT1)
            main[New_NT1] = [b[1]]
            main[sym][i] = New_NT + New_NT1+b[2]
            b=main[sym][i]
            New_NT2 = string.ascii_uppercase[letter - 1]
            letter -= 1
            NT_symbol.append(New_NT2)
            main[New_NT2] = [b[0:2]]
            main[sym][i] = New_NT2+b[2]
        elif count_T == 2 and count_NT == 0:
            New_NT = string.ascii_uppercase[letter - 1]
            letter -= 1
            NT_symbol.append(New_NT)
            main[New_NT] = [b[0]]
            New_NT1 = string.ascii_uppercase[letter - 1]
            letter -= 1
            NT_symbol.append(New_NT1)
            main[New_NT1] = [b[1]]
            main[sym][i] = New_NT + New_NT1
        elif count_T == 2 and count_NT == 2:
            New_NT = string.ascii_uppercase[letter - 1]
            letter -= 1
            NT_symbol.append(New_NT)
            main[New_NT] = [b[0]]
            New_NT1 = string.ascii_uppercase[letter - 1]
            letter -= 1
            NT_symbol.append(New_NT1)
            main[New_NT1] = [b[1]]
            main[sym][i] = New_NT + New_NT1 + b[2:]
            
            b=main[sym][i]
            New_NT = string.ascii_uppercase[letter - 1]
            letter -= 1
            NT_symbol.append(New_NT)
            main[New_NT] = [b[0:2]]
            New_NT1 = string.ascii_uppercase[letter - 1]
            letter -= 1
            NT_symbol.append(New_NT1)
            main[New_NT1] = [b[2:]]
            main[sym][i] = New_NT + New_NT1


for i in main:
    print(i + " -> ", end="")
    unique_productions = set()
    for ele in range(len(main[i])):
        if main[i][ele] != "":
            b = main[i][ele]
            if b not in unique_productions:
                print(b, end="/")
                unique_productions.add(b)
    
    print()

    
    
    
