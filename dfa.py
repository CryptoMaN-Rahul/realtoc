class Utility:
    @staticmethod
    def show_error(message):
        print("Output: Your string is not valid")
        print("Reason: " + message)

    @staticmethod
    def get_input(message):
        while True:
            input_string = input(message)
            if len(input_string) == 0:
                print("Input can not be empty")
            else:
                return input_string


class DFAValidateString:
    @staticmethod
    def main():
        message = "Enter valid input symbols (∑) (comma-separated): "
        valid_input_string = Utility.get_input(message)
        valid_inputs = set(valid_input_string.split(","))

        message = "Enter states (Q) (comma-separated): "
        state_string = Utility.get_input(message)
        states = set(state_string.split(","))

        message = "Enter starting state (q0): "
        starting_state = Utility.get_input(message)

        message = "Enter all final states (F) (comma-separated): "
        final_state_string = Utility.get_input(message)
        final_states = set(final_state_string.split(","))

        transitions = {}

        for state in states:
            transitions[state] = {}
            for valid_input in valid_inputs:
                message = f"Enter transition (δ) for state '{state}' having input '{valid_input}': "
                next_state = Utility.get_input(message)
                transitions[state][valid_input] = next_state

        dfa = DFA(starting_state, final_states, transitions)

        while True:
            message = "Enter string to be validated: "
            input_sequence = Utility.get_input(message)
            dfa.process_input_sequence(input_sequence)

            choice = input("Do you want to validate another string? (y/n): ")
            if choice.lower() == "n":
                break


class DFA:
    def __init__(self, starting_state, final_states, transitions):
        self.starting_state = starting_state
        self.final_states = final_states
        self.transitions = transitions

    def process_input_sequence(self, input_sequence):
        current_state = self.starting_state
        traversal_path = [current_state]

        for input_symbol in input_sequence:
            current_state_transition = self.transitions.get(current_state, {})
            if input_symbol in current_state_transition:

              next_state = current_state_transition.get(input_symbol)

              traversal_path.append(f"{input_symbol} -> {next_state}")
              current_state = next_state
              
            else:
                Utility.show_error(f"Invalid transition: State '{current_state}' with input '{input_symbol}'")
                return

        if current_state in self.final_states:
            print("Output: Your string is valid")
        else:
            Utility.show_error(f"Your string ends at state '{current_state}' which is not a final state")

        print("Traversal Path: " + " - ".join(traversal_path))


if __name__ == "__main__":
    DFAValidateString.main()




''' Algorithm Overview: DFA String Validation

Initialization:

Get the set of valid input symbols (∑).
Get the set of states (Q).
Get the starting state (q0).
Get the set of final states (F).
Initialize an empty dictionary for transitions.


Transition Table Construction:
For each state in Q:
For each valid input symbol in ∑:
Get the next state for the given input symbol.
Populate the transition table.


DFA Object Initialization:
Create a DFA object with the starting state, final states, and transitions.


String Validation:
For each character in the input string:
Check if there is a transition for the current state and the input symbol.
If yes, update the current state.
If no, show an error indicating an invalid input symbol.

Result Analysis:
After processing the entire string:

If the final state is in the set of final states, the string is valid.
If not, show an error indicating an invalid final state.


Traversal Path Recording:
Record the traversal path, showing each transition from state to state.
'''



