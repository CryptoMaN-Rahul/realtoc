import java.util.*;

class Main {
    public static void main(String[] args) {
        MealyMachineValidateString.main();
    }
}

class Utility {
    
    public static String get_input(String message) {
        Scanner scanner = new Scanner(System.in);
        String inputString;

        do {
            System.out.print(message);
            inputString = scanner.nextLine();
            if (inputString.length() == 0) {
                System.out.println("Input can not be empty");
            }
        } while (inputString.length() == 0);

        return inputString;
    }
}

class MealyMachineValidateString {
    public static void main() {
        String inputString, message;

        message = "Enter valid input symbols (comma-separated): ";
        inputString = Utility.get_input(message);
        Set<String> validInputs = new HashSet<>(Arrays.asList(inputString.split(",")));

        message = "Enter states (Q) (comma-separated): ";
        inputString = Utility.get_input(message);
        Set<String> states = new HashSet<>(Arrays.asList(inputString.split(",")));

        message = "Enter starting state: ";
        String startingState = Utility.get_input(message);

        Map<String, Map<String, String>> transitions = new HashMap<>();

        for (String state : states) {
            Map<String, String> transition = new HashMap<>();
            for (String validInput : validInputs) {
                message = String.format("Enter next state and output for transition '%s' with input '%s': ", state, validInput);
                String next_state_and_output = Utility.get_input(message);
                transition.put(validInput, next_state_and_output);
            }
            transitions.put(state, transition);
        }

        MealyMachine mealyMachine = new MealyMachine(startingState, transitions);

        while (true) {
            message = "Enter input sequence to be processed: ";
            String input_sequence = Utility.get_input(message);
            mealyMachine.process_input_sequence(input_sequence);

            System.out.print("Do you want to process another input sequence? (y/n): ");
            String choice = new Scanner(System.in).nextLine();
            if (choice.equalsIgnoreCase("n")) {
                break;
            }
        }
    }
}

class MealyMachine {
    private String startingState;
    private Map<String, Map<String, String>> transitions;

    public MealyMachine(String startingState, Map<String, Map<String, String>> transitions) {
        this.startingState = startingState;
        this.transitions = transitions;
    }

    public void process_input_sequence(String input_sequence) {
        String current_state = startingState;
        String output_sequence = "";
        List<String> traversal_path = new ArrayList<>();
        traversal_path.add(current_state);

        for (int i = 0; i < input_sequence.length(); i++) {
            String input_symbol = String.valueOf(input_sequence.charAt(i));
            Map<String, String> current_transitions = transitions.get(current_state);

            if (current_transitions.containsKey(input_symbol)) {
                String next_state_and_output = current_transitions.get(input_symbol);
                String[] next_state_and_output_arr = next_state_and_output.split(",");
                String next_state = next_state_and_output_arr[0];
                String output = next_state_and_output_arr[1];

                output_sequence += output;
                traversal_path.add(current_state + "(" + input_symbol + "," + output + ")->" + next_state);
                current_state = next_state;
            } 
        }

        System.out.println("Output Sequence: " + output_sequence);
        System.out.println();
        System.out.println("Traversal Path: " + String.join(" -> ", traversal_path));
    }

    
}
