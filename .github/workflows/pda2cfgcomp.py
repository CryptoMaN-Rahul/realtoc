# Input production rules
num_rules = int(input("Enter the number of production rules: "))
rules = [input().split() for _ in range(num_rules)]

# Extract non-terminals and terminals
non_terminals = {rule[0] for rule in rules}
terminals = {ch for rule in rules for prod in rule[1].split('|') for ch in prod if ch.islower() or ch.isdigit()}
terminals.add('#')

# Print PDA Production Rules for non-terminals
print("PDA Production Rules:")
for non_term in non_terminals:
    print(f"dl(q, null, {non_term}) --> ", end='')
    first = True
    for rule in rules:
        if rule[0] == non_term:
            for prod in rule[1].split('|'):
                if not first:
                    print(" | ", end='')
                print(f"dl(q, {prod})", end='')
                first = False
    print()

# Print PDA Production Rules for terminals
for term in terminals:
    if term == '#':
        print("dl(q, null, null) --> dl(q, null)")
    else:
        print(f"dl(q, {term}, {term}) --> dl(q, null)")
