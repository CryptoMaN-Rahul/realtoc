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


