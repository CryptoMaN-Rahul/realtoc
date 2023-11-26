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
        self.transitions.setdefault(current_state, {})[input_symbol] = (next_state, output_symbol)

    def set_initial_state(self, initial_state):
        self.current_state = initial_state

    def transition(self, input_symbol):
        if input_symbol not in self.inputs or self.current_state not in self.transitions:
            raise ValueError("Invalid input symbol or current state")

        next_state, output = self.transitions[self.current_state].get(input_symbol, (None, None))

        if next_state is None:
            raise ValueError("No transition defined for the current state and input")

        self.current_state = next_state

        return output

def main():
    mealy_machine = MealyMachine()

    # Input states, inputs, and transitions dynamically
    mealy_machine.states.update(input("Enter states (comma-separated): ").split(','))
    mealy_machine.inputs.update(input("Enter input symbols (comma-separated): ").split(','))

    for state in mealy_machine.states:
        num_transitions = int(input(f"Enter the number of transitions for state {state}: "))
        mealy_machine.transitions[state] = {
            input_symbol: (input("Enter next state: "), input("Enter output symbol: "))
            for _ in range(num_transitions)
        }

    mealy_machine.set_initial_state(input("Enter the initial state: "))

    # Input string
    input_string = input("Enter an input string: ")

    # Process the input string and print the outputs
    output_sequence = "".join(mealy_machine.transition(symbol) for symbol in input_string)
    output_details = [
        f"Input: {symbol}, Current State: {mealy_machine.current_state}, Output: {mealy_machine.transition(symbol)}"
        for symbol in input_string
    ]

    print("\n".join(output_details))
    print("Output Sequence:", output_sequence)

if __name__ == "__main__":
    main()
