nstate = int(input("Enter the number of states: "))
ntransition = int(input("Enter the number of transition states: "))
pda = {}
stack = []
print("state input top stack new_state")

for i in range(ntransition):
    transition = input().split(" ")
    temp = []
    try:
        pda[transition[0]].append(transition[1:])
    except KeyError:
        pda[transition[0]] = [transition[1:]]

input_string = input("Enter the input string")
final_state = input("Enter the final state")
print(pda)

state = '0'
for i in input_string:
    print(i, end=" - ")
    trans = pda[state]
    for b in trans:
        if b[2] == "^":
            stack.pop()
        print(" | ".join(n for n in b))
        state = b[3]
        break

    if len(stack) == 0 and b[0] == '^':
        state = b[3]
        break

    if i == b[0]:
        stack.append(b[1])
        print(" | ".join(n for n in b))
        state = b[3]
        break

    if len(stack) == 0 or b[1] != stack[len(stack) - 1]:
        continue

    print("state is " + state)

if state == final_state or len(stack) == 0:
    print("accepted")
else:
    print("not accepted")
