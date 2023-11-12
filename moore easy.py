class MooreMachine:
    def __init__(self):
        self.states = set()
        self.inputs = set()
        self.outputs = {}
        self.transitions = {}
        self.current_state = None

    def add_state(self, state):
        self.states.add(state)

    def add_input(self, input_symbol):
        self.inputs.add(input_symbol)

    def add_output(self, state, output_symbol):
        self.outputs[state] = output_symbol

    def add_transition(self, current_state, input_symbol, next_state):
        if current_state not in self.transitions:
            self.transitions[current_state] = {}
        self.transitions[current_state][input_symbol] = next_state

    def set_initial_state(self, initial_state):
        self.current_state = initial_state

    def transition(self, input_symbol):
        if input_symbol not in self.inputs:
            raise ValueError("Invalid input symbol")

        if self.current_state not in self.transitions:
            raise ValueError("Invalid current state")

        next_state = self.transitions[self.current_state].get(input_symbol)
        if next_state is None:
            raise ValueError("No transition defined for the current state and input")

        output = self.outputs.get(next_state)
        self.current_state = next_state

        return output

def main():
    moore_machine = MooreMachine()

    # Input states, inputs, outputs, and transitions dynamically
    num_states = int(input("Enter the number of states: "))
    for _ in range(num_states):
        state = input("Enter a state: ")
        moore_machine.add_state(state)

    num_inputs = int(input("Enter the number of input symbols: "))
    for _ in range(num_inputs):
        input_symbol = input("Enter an input symbol: ")
        moore_machine.add_input(input_symbol)

    for state in moore_machine.states:
        output_symbol = input(f"Enter the output symbol for state {state}: ")
        moore_machine.add_output(state, output_symbol)

    for _ in range(num_states):
        current_state = input("Enter the current state: ")
        num_transitions = int(input(f"Enter the number of transitions for state {current_state}: "))
        for _ in range(num_transitions):
            input_symbol = input("Enter an input symbol for this transition: ")
            next_state = input("Enter the next state: ")
            moore_machine.add_transition(current_state, input_symbol, next_state)

    initial_state = input("Enter the initial state: ")
    moore_machine.set_initial_state(initial_state)

    # Input string
    input_string = input("Enter an input string: ")

    # Initialize output_sequence with the initial state's output
    output_sequence = moore_machine.outputs[initial_state]

    # Process the input string and print the outputs
    for symbol in input_string:
        output = moore_machine.transition(symbol)
        output_sequence += output
        print(f"Input: {symbol}, Current State: {moore_machine.current_state}, Output: {output}")

    print("Output Sequence:", output_sequence)

if __name__ == "__main__":
    main()


'''

Create a MooreMachine instance with empty sets for states, inputs, and empty dictionaries for outputs and transitions.

Add States, Inputs, and Outputs:
2. Take user input for the number of states (num_states).
3. For each state:

Take user input for the state name (state).
Add the state to the Moore Machine using add_state.



Take user input for the number of input symbols (num_inputs).


For each input symbol:

Take user input for the input symbol (input_symbol).
Add the input symbol to the Moore Machine using add_input.



For each state in the Moore Machine:

Take user input for the output symbol for that state (output_symbol).
Add the output symbol to the Moore Machine using add_output.



Add Transitions:
7. For each state in the Moore Machine:

Take user input for the current state (current_state).
Take user input for the number of transitions for that state (num_transitions).
For each transition:

Take user input for the input symbol for this transition (input_symbol).
Take user input for the next state (next_state).
Add the transition using add_transition.



Set Initial State:
8. Take user input for the initial state (initial_state).
9. Set the initial state using set_initial_state.
Process Input String:
10. Take user input for the input string (input_string).
11. Initialize an empty string for output_sequence with the initial state's output.
Main Loop:
12. For each symbol in the input string:

Perform the transition using transition and update the current state.
Accumulate the output in the output_sequence.

Print Output:
13. For each step in the input string processing:

Print the input symbol, current state, and output.


Print the final output_sequence.

'''
