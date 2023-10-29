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
