import java.util.*;

public class CFGtoPDAConversion {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.print("Enter the number of Production Rules of CFG: ");
        int n = scanner.nextInt();
        scanner.nextLine(); // Consume the newline

        String s1, s2;
        List<Pair<String, String>> v = new ArrayList<>();

        System.out.println("Please enter the Production rules of CFG:");
        for (int i = 0; i < n; i++) {
            s1 = scanner.next();
            s2 = scanner.next();
            v.add(new Pair<>(s1, s2));
        }

        Set<String> terminalSymbols = new HashSet<>();
        Set<String> nonTerminalSymbols = new HashSet<>();

        for (int i = 0; i < n; i++) {
            String nonTerminal = v.get(i).getKey();
            nonTerminalSymbols.add(nonTerminal); // Populate nonTerminalSymbols
            String production = v.get(i).getValue();

            // Split the production string by '|' to handle multiple production rules
            Scanner productionScanner = new Scanner(production);
            productionScanner.useDelimiter("\\|");
            while (productionScanner.hasNext()) {
                String rule = productionScanner.next();
                for (char ch : rule.toCharArray()) {
                    if (Character.isLetter(ch) && Character.isUpperCase(ch)) {
                        nonTerminalSymbols.add(String.valueOf(ch));
                    } else if (Character.isLetterOrDigit(ch)) {
                        terminalSymbols.add(String.valueOf(ch));
                    }
                }
            }

            if (production.equals("#")) {
                terminalSymbols.add("#"); // Use '#' to represent epsilon
            }
        }

        System.out.println("The Corresponding Production Rules For PDA are:");
        System.out.println("Rules For Non-Terminal Symbols are:");

        for (String nonTerminal : nonTerminalSymbols) {
            int flag = 0;
            System.out.print("dl(q,null," + nonTerminal + ") --> ");

            for (int i = 0; i < n; i++) {
                if (v.get(i).getKey().equals(nonTerminal)) {
                    if (flag == 1) {
                        System.out.print(" | ");
                    }
                    System.out.print("dl(q," + v.get(i).getValue() + ")");
                    flag = 1;
                }
            }

            if (flag != 0) {
                System.out.println();
            }
        }

        System.out.println("Rules For Terminal Symbols are:");
        for (String terminal : terminalSymbols) {
            if (terminal.equals("#")) {
                System.out.println("dl(q,null,null) --> dl(q,null)"); // Handle epsilon production
            } else {
                System.out.println("dl(q," + terminal + "," + terminal + ") --> dl(q,null)");
            }
        }
    }

    static class Pair<K, V> {
        private K key;
        private V value;

        public Pair(K key, V value) {
            this.key = key;
            this.value = value;
        }

        public K getKey() {
            return key;
        }

        public V getValue() {
            return value;
        }
    }
}
