from collections import deque

class Edge:
    def __init__(self, state=None, transition=None):
        self.state = state
        self.transition = transition

class RegExpToENFAConverter:

    enfa = []
    stack = deque()
    epsilon = 'ε'

    @staticmethod
    def add_state():
        adj_list = []
        RegExpToENFAConverter.enfa.append(adj_list)

    @staticmethod
    def add_transition(source, destination, character):
        adj_list = RegExpToENFAConverter.enfa[source]
        edge = Edge(destination, character)
        adj_list.append(edge)

    @staticmethod
    def basic_machine(character):
        for _ in range(2):
            RegExpToENFAConverter.add_state()
        RegExpToENFAConverter.add_transition(len(RegExpToENFAConverter.enfa)-2, len(RegExpToENFAConverter.enfa)-1, character)
        RegExpToENFAConverter.stack.appendleft(len(RegExpToENFAConverter.enfa)-1)
        RegExpToENFAConverter.stack.appendleft(len(RegExpToENFAConverter.enfa)-2)

    @staticmethod
    def kleene_closure():
        head = RegExpToENFAConverter.stack.popleft()
        tail = RegExpToENFAConverter.stack.popleft()
        for _ in range(2):
            RegExpToENFAConverter.add_state()
        RegExpToENFAConverter.add_transition(len(RegExpToENFAConverter.enfa)-2, head, RegExpToENFAConverter.epsilon)
        RegExpToENFAConverter.add_transition(len(RegExpToENFAConverter.enfa)-2, len(RegExpToENFAConverter.enfa)-1, RegExpToENFAConverter.epsilon)
        RegExpToENFAConverter.add_transition(tail, head, RegExpToENFAConverter.epsilon)
        RegExpToENFAConverter.add_transition(tail, len(RegExpToENFAConverter.enfa)-1, RegExpToENFAConverter.epsilon)
        RegExpToENFAConverter.stack.appendleft(len(RegExpToENFAConverter.enfa)-1)
        RegExpToENFAConverter.stack.appendleft(len(RegExpToENFAConverter.enfa)-2)

    @staticmethod
    def concatenation():
        head2 = RegExpToENFAConverter.stack.popleft()
        tail2 = RegExpToENFAConverter.stack.popleft()  
        head1 = RegExpToENFAConverter.stack.popleft()
        tail1 = RegExpToENFAConverter.stack.popleft()
        RegExpToENFAConverter.add_transition(tail1, head2, RegExpToENFAConverter.epsilon)
        RegExpToENFAConverter.stack.appendleft(tail2)
        RegExpToENFAConverter.stack.appendleft(head1)

    @staticmethod
    def alternation():
        head2 = RegExpToENFAConverter.stack.popleft()
        tail2 = RegExpToENFAConverter.stack.popleft()
        head1 = RegExpToENFAConverter.stack.popleft()
        tail1 = RegExpToENFAConverter.stack.popleft()
        for _ in range(2):
            RegExpToENFAConverter.add_state()
        RegExpToENFAConverter.add_transition(len(RegExpToENFAConverter.enfa)-2, head1, RegExpToENFAConverter.epsilon)
        RegExpToENFAConverter.add_transition(len(RegExpToENFAConverter.enfa)-2, head2, RegExpToENFAConverter.epsilon)
        RegExpToENFAConverter.add_transition(tail1, len(RegExpToENFAConverter.enfa)-1, RegExpToENFAConverter.epsilon)
        RegExpToENFAConverter.add_transition(tail2, len(RegExpToENFAConverter.enfa)-1, RegExpToENFAConverter.epsilon)
        RegExpToENFAConverter.stack.appendleft(len(RegExpToENFAConverter.enfa)-1)
        RegExpToENFAConverter.stack.appendleft(len(RegExpToENFAConverter.enfa)-2)

    @staticmethod
    def print_nfa_table():
    
        print("e-NFA Table:")
        
        print("{:<10} {:<20}".format('State', 'Transitions'))
        for i in range(len(RegExpToENFAConverter.enfa)):
            transitions = []
            for edge in RegExpToENFAConverter.enfa[i]:
                transitions.append("{} -> {}".format(edge.transition, edge.state))
            print("{:<10} {:<20}".format(i, ", ".join(transitions)))
    
        print()
        print("Start state: {}".format(RegExpToENFAConverter.initial_state))
        print("Accept state: {}".format(RegExpToENFAConverter.final_state))
        
    @staticmethod
    def precedence(operator):
        if operator == '.':
            return 2
        elif operator == '|':
            return 1
        else:
            return -1

    @staticmethod
    def use_dot_for_concatenation(regex):
        new_regex = ""
        for i in range(len(regex)-1):
            cur = regex[i]
            if cur != '|' and cur != '(':
                next = regex[i+1]
                if next != '|' and next != '*' and next != ')':
                    new_regex += regex[i] + "."
                else:
                    new_regex += regex[i]
            else:
                new_regex += regex[i]
        new_regex += regex[-1]
        return new_regex

    @staticmethod
    def infix_to_postfix(infix_regex):
        stack = deque()
        postfix_regex = ""
        for c in infix_regex:
            if c in ['.', '|']:
                while stack and RegExpToENFAConverter.precedence(c) <= RegExpToENFAConverter.precedence(stack[-1]):
                    postfix_regex += stack.pop()
                stack.append(c)
            elif c == '(':
                stack.append(c)
            elif c == ')':
                while stack and stack[-1] != '(':
                    postfix_regex += stack.pop()
                stack.pop()
            else:
                postfix_regex += c
        while stack:
            postfix_regex += stack.pop()
        return postfix_regex

    @staticmethod
    def regex_to_enfa(postfix_regex):
        for c in postfix_regex:
            if c == '*':
                RegExpToENFAConverter.kleene_closure()
            elif c == '.':
                RegExpToENFAConverter.concatenation()
            elif c == '|':
                RegExpToENFAConverter.alternation()
            else:
                RegExpToENFAConverter.basic_machine(c)
        if RegExpToENFAConverter.stack:
            RegExpToENFAConverter.initial_state = RegExpToENFAConverter.stack.popleft()
            RegExpToENFAConverter.final_state = RegExpToENFAConverter.stack.popleft()
        
        RegExpToENFAConverter.print_nfa_table()

if __name__ == '__main__':
    regex = input("Enter regex: ")
    infix_regex = RegExpToENFAConverter.use_dot_for_concatenation(regex)
    print("Using . for concatenation:")
    print(infix_regex)
    postfix_regex = RegExpToENFAConverter.infix_to_postfix(infix_regex)
    print("Postfix notation:")
    print(postfix_regex)
    RegExpToENFAConverter.regex_to_enfa(postfix_regex)
