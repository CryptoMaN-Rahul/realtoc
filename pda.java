import java.util.*;

public class tocexp7 {

    private Stack<Character> stack;
    private String input;
    private int index;
    private Map<Character, List<String>> cfgProductions;
    private List<String> steps;

    public tocexp7(Map<Character, List<String>> cfgProductions, String input) {
        this.stack = new Stack<>();
        this.input = input;
        this.index = 0;
        this.cfgProductions = cfgProductions;
        this.steps = new ArrayList<>();
    }

    public boolean isAccepted() {
        stack.push('S');
        steps.add("Start: Stack = [S], Input = " + input);

        while (index < input.length()) {
            char currentSymbol = input.charAt(index);
            List<String> productions = cfgProductions.get(stack.peek());

            if (productions != null) {
                boolean transition = false;

                for (String production : productions) {
                    char firstProductionSymbol = production.charAt(0);

                    if (firstProductionSymbol == currentSymbol) {
                        stack.pop();

                        for (int i = production.length() - 1; i >= 1; i--) {
                            stack.push(production.charAt(i));
                        }

                        transition = true;
                        break;
                    }
                }

                if (transition) {
                    steps.add("Matched: Stack = " + stack.toString() + ", Input = " + input.substring(index));
                    index++;
                } else {
                    steps.add("Rejected: Stack = " + stack.toString() + ", Input = " + input.substring(index));
                    return false;  
                }
            } else {
                steps.add("Rejected: Stack = " + stack.toString() + ", Input = " + input.substring(index));
                return false; 
            }
        }

        while (!stack.isEmpty()) {
            char top = stack.pop();
            if (top != 'S') {
                steps.add("Accepted: Stack = " + stack.toString() + ", Input = " + input.substring(index));
                return true;  
            }
        }

    
        return stack.isEmpty();
    }

    public void printSteps() {
        for (String step : steps) {
            System.out.println(step);
        }
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.println("Enter the CFG productions :");
        String cfgInput = scanner.nextLine();

        Map<Character, List<String>> cfgProductions = new HashMap<>();
        String[] productions = cfgInput.split(", ");
        for (String production : productions) {
            String[] parts = production.split("->");
            char variable = parts[0].charAt(0);
            String[] rightHandSides = parts[1].split("\\|");
            List<String> productionList = new ArrayList<>();
            for (String rhs : rightHandSides) {
                productionList.add(rhs);
            }
            cfgProductions.put(variable, productionList);
        }

        System.out.print("Enter the input string: ");
        String inputString = scanner.nextLine();

        tocexp7 pda = new tocexp7(cfgProductions, inputString);

        if (pda.isAccepted()) {
            System.out.println("The input string is accepted.");
        } else {
            System.out.println("The input string is rejected.");
        }

        System.out.println("Steps:");
        pda.printSteps();
    }
}
