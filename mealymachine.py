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


class MealyMachineValidateString:
    @staticmethod
    def main():
        message = "Enter valid input symbols (comma-separated): "
        valid_input_string = Utility.get_input(message)
        valid_inputs = set(valid_input_string.split(","))

        message = "Enter states (Q) (comma-separated): "
        state_string = Utility.get_input(message)
        states = set(state_string.split(","))

        message = "Enter starting state (q0): "
        starting_state = Utility.get_input(message)

        transitions = {}

        for state in states:
            transitions[state] = {}
            for valid_input in valid_inputs:
                message = f"Enter next state for transition '{state}' with input '{valid_input}': "
                next_state = Utility.get_input(message)
                message = f"Enter output for transition '{state}' with input '{valid_input}': "
                output = Utility.get_input(message)
                transitions[state][valid_input] = (next_state, output)

        mealy_machine = MealyMachine(starting_state, transitions)

        while True:
            message = "Enter input sequence to be processed: "
            input_sequence = Utility.get_input(message)
            mealy_machine.process_input_sequence(input_sequence)

            choice = input("Do you want to process another input sequence? (y/n): ")
            if choice.lower() == "n":
                break


class MealyMachine:
    def __init__(self, starting_state, transitions):
        self.starting_state = starting_state
        self.transitions = transitions

    def process_input_sequence(self, input_sequence):
        current_state = self.starting_state
        output_sequence = ""
        traversal_path = [current_state]

        for input_symbol in input_sequence:
            current_state_transition = self.transitions.get(current_state, {})
            if input_symbol in current_state_transition:
                next_state, output = current_state_transition[input_symbol]
                output_sequence += output
                traversal_path.append(f"{current_state}({input_symbol},{output})->{next_state}")
                current_state = next_state
            else:
                Utility.show_error(f"Invalid transition: State '{current_state}' with input '{input_symbol}'")
                return

        print("Output Sequence:", output_sequence)
        print("Traversal Path:", " -> ".join(traversal_path))


if __name__ == "__main__":
    MealyMachineValidateString.main()
