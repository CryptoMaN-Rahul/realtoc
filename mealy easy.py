class MealyMachine:
    def __init__(self):
        self.states = set()
        self.inputs = set()
        self.transitions = {}
        self.current_state = None

    def add_state(self, state):
        self.states.add(state)

    def add_input(self, input_symbol):
        self.inputs.add(input_symbol)

    def add_transition(self, current_state, input_symbol, next_state, output_symbol):
        if current_state not in self.transitions:
            self.transitions[current_state] = {}
        self.transitions[current_state][input_symbol] = (next_state, output_symbol)

    def set_initial_state(self, initial_state):
        self.current_state = initial_state

    def transition(self, input_symbol):
        if input_symbol not in self.inputs:
            raise ValueError("Invalid input symbol")

        if self.current_state not in self.transitions:
            raise ValueError("Invalid current state")

        next_state, output = self.transitions[self.current_state].get(input_symbol)
        if next_state is None:
            raise ValueError("No transition defined for the current state and input")

        self.current_state = next_state

        return output

def main():
    mealy_machine = MealyMachine()

    # Input states, inputs, and transitions dynamically
    num_states = int(input("Enter the number of states: "))
    for _ in range(num_states):
        state = input("Enter a state: ")
        mealy_machine.add_state(state)

    num_inputs = int(input("Enter the number of input symbols: "))
    for _ in range(num_inputs):
        input_symbol = input("Enter an input symbol: ")
        mealy_machine.add_input(input_symbol)

    for _ in range(num_states):
        current_state = input("Enter the current state: ")
        num_transitions = int(input(f"Enter the number of transitions for state {current_state}: "))
        for _ in range(num_transitions):
            input_symbol = input("Enter an input symbol for this transition: ")
            next_state = input("Enter the next state: ")
            output_symbol = input("Enter the output symbol for this transition: ")
            mealy_machine.add_transition(current_state, input_symbol, next_state, output_symbol)

    initial_state = input("Enter the initial state: ")
    mealy_machine.set_initial_state(initial_state)

    # Input string
    input_string = input("Enter an input string: ")

    # Process the input string and print the outputs
    output_sequence = ""
    for symbol in input_string:
        output = mealy_machine.transition(symbol)
        output_sequence += output
        print(f"Input: {symbol}, Current State: {mealy_machine.current_state}, Output: {output}")

    print("Output Sequence:", output_sequence)

if __name__ == "__main__":
    main()



'''
Create a MealyMachine instance with an empty set for states, inputs, and an empty dictionary for transitions.

Add States, Inputs, and Transitions:
2. Take user input for the number of states (num_states).
3. For each state:

Take user input for the state name (state).
Add the state to the Mealy Machine using add_state.



Take user input for the number of input symbols (num_inputs).


For each input symbol:

Take user input for the input symbol (input_symbol).
Add the input symbol to the Mealy Machine using add_input.



For each state in the Mealy Machine:

Take user input for the current state (current_state).
Take user input for the number of transitions for that state (num_transitions).
For each transition:

Take user input for the input symbol for this transition (input_symbol).
Take user input for the next state (next_state).
Take user input for the output symbol for this transition (output_symbol).
Add the transition using add_transition.


Set Initial State:
7. Take user input for the initial state (initial_state).
8. Set the initial state using set_initial_state.
Process Input String:
9. Take user input for the input string (input_string).
10. Initialize an empty string for output_sequence.
Main Loop:
11. For each symbol in the input string:
- Perform the transition using transition and update the current state.
- Accumulate the output in the output_sequence.
- Print the input symbol, current state, and output.
Print Output:
12. Print the final output_sequence.
'''
