import java.util.*;


class Main {
    public static void main(String[] args) {
        DFAValidateString.main();
    }
}


class Utility {
    public static void show_error(String message) {
        System.out.println("Output: Your string is not valid");
        System.out.println("Reason: " + message);
    }

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

class DFAValidateString {
    public static void main() {
        String inputString, message;

        message = "Enter valid input states (∑) (comma-separated): ";
        inputString = Utility.get_input(message);

        Set<String> validInputs = new HashSet<>(Arrays.asList(inputString.split(",")));

        message = "Enter states (Q) (comma-separated): ";
        inputString = Utility.get_input(message);

        Set<String> states = new HashSet<>(Arrays.asList(inputString.split(",")));

        message = "Enter starting state (q0): ";
        String startingState = Utility.get_input(message);

        message = "Enter all final states (F) (comma-separated): ";
        inputString = Utility.get_input(message);

        Set<String> finalStates = new HashSet<>(Arrays.asList(inputString.split(",")));

        Map<String, Map<String, String>> transitions = new HashMap<>();

        for (String state : states) {
            Map<String, String> transition = new HashMap<>();
            for (String validInput : validInputs) {
                message = String.format("Enter transition (δ) for state '%s' having input '%s': ", state, validInput);
                String nextState = Utility.get_input(message);
                transition.put(validInput, nextState);
            }
            transitions.put(state, transition);
        }

        DFA dfa = new DFA(startingState, finalStates, transitions);

        while (true) {
            message = "Enter string to be validated: ";
            String validateString = Utility.get_input(message);
            dfa.validateString(validateString);

            Scanner scanner = new Scanner(System.in);
            System.out.print("Do you want to validate another string? (y/n): ");
            String choice = scanner.nextLine();
            if (choice.equalsIgnoreCase("n")) {
                break;
            }
        }
    }
}

class DFA {
    private String startingState;
    private Set<String> finalStates;
    private Map<String, Map<String, String>> transitions;

    public DFA(String startingState, Set<String> finalStates, Map<String, Map<String, String>> transitions) {
        this.startingState = startingState;
        this.finalStates = finalStates;
        this.transitions = transitions;
    }

    public void validateString(String validateString) {
        String current_state = startingState;
        List<String> traversal_path = new ArrayList<>();
        traversal_path.add(current_state);

        for (char c : validateString.toCharArray()) {
            Map<String, String> current_state_transition = transitions.get(current_state);
            String next_state = current_state_transition.get(String.valueOf(c));

            if (next_state == null) {
                Utility.show_error("Your string contains value '" + c + "' which is not present in the input set");
                return;
            }

            traversal_path.add(c + " -> " + next_state);
            current_state = next_state;
        }

        if (finalStates.contains(current_state)) {
            System.out.println("Output: Your string is valid");
        } else {
            Utility.show_error("Your string ends at state '" + current_state + "' which is not a final state");
        }

        System.out.println("Traversal Path: " + String.join(" - ", traversal_path));
    }
}

