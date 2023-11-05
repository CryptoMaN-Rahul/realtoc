transitions = [[1,5,4,5,3], 
              [1,2,5,5,1],
              [2,5,5,0,2],
              [5,5,4,5,3],
              [4,4,4,4,4],
              [5,5,5,5,5]]

symbols = ["0","1"," ","x","y"]

pointer = [[1,1,0,1,1], [1,0,1,1,1],
           [0,1,1,1,0], 
           [1,1,0,1,1],
           [1,1,1,1,1],
           [1,1,1,1,1]]
           
replace = [[3,3,3,3,4], [0,4,3,3,4],
           [0,3,3,3,4],
           [0,1,2,3,4],
           [0,1,2,3,4],
           [0,1,2,3,4]]
           
state = 0

s = input("enter the string: ")
s = list(s + " ")

acc = 4
dec = 5 

tape = s
head = 0
i = 20

print("Tape: ", end="")
print(tape)
print("State = "+str(state) + ", Head = "+ str(head))

while state < 4:
  c = state
  
  symbol = symbols.index(tape[head]) # get index of symbol
  
  tape[head] = symbols[replace[c][symbol]] 
  state = transitions[c][symbol]
  
  if pointer[c][symbol] == 0:
    head -= 1
  else:
    head += 1
    
  print("Tape: ", end="")
  print(tape)
  
  print("State = "+str(state) + ", Head = "+ str(head))
  
  if state == 4:
    print("the given string passes")
  else:
    print("the given string does not pass")
