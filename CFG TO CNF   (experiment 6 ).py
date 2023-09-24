import string

def remove_char(string,pos):
  new_string = ""
  for i in range(len(string)): 
    if str(i) not in pos:
      new_string += string[i]
  return new_string

from itertools import permutations

NT_symbol=input("Enter the NonTerminal Symbols : ").split(" ")
T_symbol=input("Enter the Terminal Symbols : ").split(" ")

main = {}
# this is nullable variable
n = []
for i in NT_symbol:
  main[i] = input(i+" -> ").split("/")
try:
  c=main[i].index("^")
  n.append(i)  
except:
  c = 0

# find the nullable symbols
for z in range(len(main)):
  for k in main:
    for i in main[k]:
      for u in i:
        if u in n:
          n.append(k)
          break
  n=[*set(n)]
      
for i in main:
  for k in main[i]:
    pos ="" 
    m = []
    possible_comb=[]
    # print(k,end=" : ")
    for u in range(len(k)):
      if i == 'A':
        if k[u] in n and k[u] != 'A':
          pos+=str(u)
        else:
          if k[u] in n:
            pos+=str(u)
    # eleminating null symbols        
    for b in range(len(pos)):
      temp = [''.join(p) for p in permutations(pos,b+1)]
      
      possible_comb = possible_comb+temp
    for b in possible_comb:
      new_k = k
      if k != "^":
        m.append(remove_char(k,b))
    main[i] = main[i] + list(set(m))
main[i] = list(map(lambda x: x.replace('^', ''), main[i]))

# find unit production
unit_prod = {}
for i in main:
  for b in main[i]:
    if b in T_symbol:
      unit_prod[i] = b
    if b == "^":
      unit_prod[i] = ""
      
print("Removed unit and null production : \n\n")      
# remove unit production
for i in main:
  for ele in range(len(main[i])):
    b = main[i][ele] 
    temp = ""
    for c in b:
      try:
        temp += unit_prod[c]
      except:
        temp+=c
    if temp != "":
      b = temp
    print("Converting to CNF form: ")
    
    letter = len(string.ascii_uppercase)
    for sym in NT_symbol:
      for i in range(len(main[sym])):
        b = main[sym][i]
        count_NT = 0
        count_T = 0
        for j in b:
          if j.isupper():
            count_NT+=1
          elif j.islower():
            count_T+=1
        if count_NT > 2:
          New_NT = string.ascii_uppercase[letter-1]  
          for c in range(0,len(b)-2,2):
            letter-=1
          NT_symbol+=New_NT
          main[New_NT]= [b[c:c+2]]
          main[sym][i] = New_NT+b[-2]
        elif count_T == 1 and count_NT == 2:
          New_NT = string.ascii_uppercase[letter-1]
          letter-=1
          NT_symbol+= New_NT
          main[New_NT] = [b[0]]
          main[sym][i] = New_NT+b[1:]
          b = main[sym][i]
          New_NT = string.ascii_uppercase[letter-1]
          letter-=1
          main[New_NT] = [b[0:2]]
          main[sym][i] = New_NT+b[2:]
        elif count_T == 1 and count_NT == 1:
          New_NT = string.ascii_uppercase[letter-1]
          letter-=1
          NT_symbol+= New_NT
          main[New_NT] = [b[0]]
          main[sym][i] = New_NT+b[1]
          
    for i in main:
      print(i+" -> ",end="")
      for ele in range(len(main[i])):
        b = main[i][ele]
        # for b in main[i]:
        print(b,end="/")
      print()
