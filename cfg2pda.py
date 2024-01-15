rules = [input().split() for _ in range(int(input("Enter number of production rules: ")))]

non_terminals = {rule[0] for rule in rules}
terminals = set()
for rule in rules:
    for prod in rule[1].split('|'):
        for ch in prod:
            if ch.islower() or ch.isdigit():
                terminals.add(ch)
terminals.add('#')

print("PDA Production Rules:")
for non_term in non_terminals:
    print(f"dl(q,null,{non_term}) --> ", end='')
    first = True
    for rule in rules:
        if rule[0] == non_term:
            for prod in rule[1].split('|'):
                if not first:
                    print(" | ", end='')
                print(f"dl(q,{prod})", end='')
                first = False
    print()

for term in terminals:
    if term == '#':
        print("dl(q,null,null) --> dl(q,null)")
    else:
        print(f"dl(q,{term},{term}) --> dl(q,null)")
'''


Algorithm:
Step 1: Input Production Rules

Take the number of production rules as input (num_rules).
Read production rules into a list (rules).

Step 2: Identify Non-terminals and Terminals

Create a set of non-terminals (non_terminals) from the left side of each production rule.
Create a set of terminals (terminals) from the right side of each production rule.

Step 3: Print PDA Production Rules

For each non-terminal in non_terminals:

Print the PDA production rule for that non-terminal.


For each terminal in terminals:

Print the PDA production rule for that terminal.



PDA Production Rule Printing:

For each non-terminal:

Print the PDA transition rule in the form dl(q,null,non_term) --> dl(q,prod1 | prod2 | ...).


For each terminal:

Print the PDA transition rule in the form dl(q,term,term) --> dl(q,null).



'''

