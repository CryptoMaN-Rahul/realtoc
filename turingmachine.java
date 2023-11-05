import java.util.Arrays;
import java.util.Scanner;

public class TuringMachine {
    public static void main(String[] args) {
        int[][] transitions = {
            {1, 5, 4, 5, 3},
            {1, 2, 5, 5, 1},
            {2, 5, 5, 0, 2},
            {5, 5, 4, 5, 3},
            {4, 4, 4, 4, 4},
            {5, 5, 5, 5, 5}
        };

        String[] symbols = {"0", "1", " ", "x", "y"};

        int[][] pointer = {
            {1, 1, 0, 1, 1},
            {1, 0, 1, 1, 1},
            {0, 1, 1, 1, 0},
            {1, 1, 0, 1, 1},
            {1, 1, 1, 1, 1},
            {1, 1, 1, 1, 1}
        };

        int[][] replace = {
            {3, 3, 3, 3, 4},
            {0, 4, 3, 3, 4},
            {0, 3, 3, 3, 4},
            {0, 1, 2, 3, 4},
            {0, 1, 2, 3, 4},
            {0, 1, 2, 3, 4}
        };

        int state = 0;

        Scanner scanner = new Scanner(System.in);
        System.out.print("Enter the string: ");
        String input = scanner.nextLine();
        input = input + " ";
        char[] tape = input.toCharArray();
        int head = 0;

        System.out.print("Tape: ");
        System.out.println(Arrays.toString(tape));
        System.out.println("State = " + state + ", Head = " + head);

        while (state < 4) {
            int c = state;
            int symbol = Arrays.asList(symbols).indexOf(String.valueOf(tape[head]));

            tape[head] = symbols[replace[c][symbol]].toCharArray()[0];
            state = transitions[c][symbol];

            if (pointer[c][symbol] == 0) {
                head -= 1;
            } else {
                head += 1;
            }

            System.out.print("Tape: ");
            System.out.println(Arrays.toString(tape));
            System.out.println("State = " + state + ", Head = " + head);

            if (state == 4) {
                System.out.println("The given string passes");
            } else {
                System.out.println("The given string does not pass");
            }
        }
    }
}
