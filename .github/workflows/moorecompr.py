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
        self.transitions.setdefault(current_state, {})[input_symbol] = next_state

    def set_initial_state(self, initial_state):
        self.current_state = initial_state

    def transition(self, input_symbol):
        if input_symbol not in self.inputs or self.current_state not in self.transitions:
            raise ValueError("Invalid input symbol or current state")

        next_state = self.transitions[self.current_state].get(input_symbol)
        if next_state is None:
            raise ValueError("No transition defined for the current state and input")

        output = self.outputs.get(next_state)
        self.current_state = next_state

        return output

def main():
    moore_machine = MooreMachine()

    # Input states, inputs, outputs, and transitions dynamically
    moore_machine.states.update(input(f"Enter states (comma-separated): ").split(','))
    moore_machine.inputs.update(input(f"Enter input symbols (comma-separated): ").split(','))

    moore_machine.outputs = {state: input(f"Enter output symbol for state {state}: ") for state in moore_machine.states}

    for state in moore_machine.states:
        num_transitions = int(input(f"Enter the number of transitions for state {state}: "))
        moore_machine.transitions[state] = {input_symbol: input("Enter next state: ") for _ in range(num_transitions)}

    moore_machine.set_initial_state(input("Enter the initial state: "))

    # Input string
    input_string = input("Enter an input string: ")

    # Initialize output_sequence with the initial state's output
    output_sequence = moore_machine.outputs[moore_machine.current_state]

    # Process the input string and print the outputs
    for symbol in input_string:
        output = moore_machine.transition(symbol)
        output_sequence += output
        print(f"Input: {symbol}, Current State: {moore_machine.current_state}, Output: {output}")

    print("Output Sequence:", output_sequence)

if __name__ == "__main__":
    main()
