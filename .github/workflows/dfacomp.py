class Utility:
    @staticmethod
    def show_error(message):
        print("Output: Your string is not valid\nReason: " + message)

    @staticmethod
    def get_input(message):
        while True:
            input_string = input(message)
            if not input_string:
                print("Input can not be empty")
            else:
                return input_string


class DFAValidateString:
    @staticmethod
    def main():
        valid_inputs = set(Utility.get_input("Enter valid input states (∑) (comma-separated): ").split(","))
        states = set(Utility.get_input("Enter states (Q) (comma-separated): ").split(","))
        starting_state = Utility.get_input("Enter starting state (q0): ")
        final_states = set(Utility.get_input("Enter all final states (F) (comma-separated): ").split(","))

        transitions = {state: {valid_input: Utility.get_input(f"Enter transition (δ) for state '{state}' having input '{valid_input}': ") for valid_input in valid_inputs} for state in states}

        dfa = DFA(starting_state, final_states, transitions)

        while True:
            validate_string = Utility.get_input("Enter string to be validated: ")
            dfa.validate_string(validate_string)

            if input("Do you want to validate another string? (y/n): ").lower() != "y":
                break


class DFA:
    def __init__(self, starting_state, final_states, transitions):
        self.starting_state, self.final_states, self.transitions = starting_state, final_states, transitions

    def validate_string(self, validate_string):
        current_state, traversal_path = self.starting_state, [self.starting_state]

        for c in validate_string:
            current_state_transition = self.transitions.get(current_state, {})
            next_state = current_state_transition.get(c)

            if next_state is None:
                Utility.show_error(f"Your string contains value '{c}' not present in the input set")
                return

            traversal_path.append(f"{c} -> {next_state}")
            current_state = next_state

        is_valid = current_state in self.final_states
        print(f"Output: Your string is {'valid' if is_valid else 'not valid'}")
        print("Traversal Path: " + " - ".join(traversal_path))


if __name__ == "__main__":
    DFAValidateString.main()
