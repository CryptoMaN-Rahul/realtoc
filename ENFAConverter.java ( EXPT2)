
 use java ENFAConverter " your string ( note: here  + means | ) " to run 



import java.util.*;

public class ENFAConverter {

    static class Edge {
        int state;
        Character transition;

        public Edge(int state, Character transition) {
            this.state = state;
            this.transition = transition;
        }
    }

    static class RegexToENFA {
        static List<List<Edge>> enfa = new ArrayList<>();
        static Deque<Integer> stack = new ArrayDeque<>();
        static Character epsilon = '\u03b5';
       
        static int initialState;
        static int finalState;

        private static void addState() {
            List<Edge> adjList = new ArrayList<Edge>();
            enfa.add(adjList);
        }
    
        private static void addTransition(int source, int destination, Character character) {
            List<Edge> adjList = enfa.get(source);
            Edge edge = new Edge(destination, character);
            adjList.add(edge);
        }
    
        private static void basicMachine(Character character) {
            for(int i = 0; i < 2; i++) {
                addState();
            }
    
            addTransition(enfa.size() - 2, enfa.size() - 1, character);
    
            stack.addFirst(enfa.size() - 1);
            stack.addFirst(enfa.size() - 2);
        }
    
        private static void kleeneClosure() {
            int head = stack.removeFirst();
            int tail = stack.removeFirst();
    
            for(int i = 0; i < 2; i++) {
                addState();
            }
    
            addTransition(enfa.size() - 2, head, epsilon);
            addTransition(enfa.size() - 2, enfa.size() - 1, epsilon);
    
            addTransition(tail, head, epsilon);
            addTransition(tail, enfa.size() - 1, epsilon);
    
            stack.addFirst(enfa.size() - 1);
            stack.addFirst(enfa.size() - 2);
        }
    
        private static void concatenation() {
            int head2 = stack.removeFirst();
            int tail2 = stack.removeFirst();
            int head1 = stack.removeFirst();
            int tail1 = stack.removeFirst();
    
            addTransition(tail1, head2, epsilon);
    
            stack.addFirst(tail2);
            stack.addFirst(head1);
        }
    
        private static void alternation() {
            int head2 = stack.removeFirst();
            int tail2 = stack.removeFirst();
            int head1 = stack.removeFirst();
            int tail1 = stack.removeFirst();
    
            for(int i = 0; i < 2; i++) {
                addState();
            }
    
            addTransition(enfa.size() - 2, head1, epsilon);
            addTransition(enfa.size() - 2, head2, epsilon);
    
            addTransition(tail1, enfa.size() - 1, epsilon);
            addTransition(tail2, enfa.size() - 1, epsilon);
    
            stack.addFirst(enfa.size() - 1);
            stack.addFirst(enfa.size() - 2);
        }
    
        private static void printAdjList() {
            System.out.println("Adjacency List");
            for(int i = 0; i < enfa.size(); i++) {
                List<Edge> edgeList = enfa.get(i);
                System.out.println(i);
                for(int j = 0; j < edgeList.size(); j++) {
                    Edge edge = edgeList.get(j);
                    System.out.println(edge.transition + " -> " + edge.state);
                }
            }
        }
    
        
    
        public static void regexToENFA(String postfixRegex) {
            for(int i = 0; i < postfixRegex.length(); i++) {
                char c = postfixRegex.charAt(i);
                switch(c) {
                    case '*':
                        kleeneClosure();
                        break;
    
                    case '.':
                        concatenation();
                        break;
    
                    case '|':
                        alternation();
                        break;
    
                    default:
                        basicMachine(c);
                }
            }
    
            // Find initial and final states by popping the contents of the stack
            if(!stack.isEmpty()) {
                initialState = stack.removeFirst();
                finalState = stack.removeFirst();
            }
    
            System.out.println("Initial State: " + initialState);
            System.out.println("Final State: " + finalState);
    
           
            printAdjList();
            System.out.println();
        }
        // ... (rest of the RegexToENFA methods and logic)
    }

    static class Helpers {
        public static String useDotForConcatenation(String regex) {
            // ... (useDotForConcatenation method)
            for(int i = 0; i < regex.length() - 1; i++) {
                char cur = regex.charAt(i);
                if(cur != '|' && cur != '(') { // Don't add '.' after '|' and '('
                    char next = regex.charAt(i + 1);
                    if(next != '|' && next != '*' && next != ')') { // Don't add '.' if '|', '*', ')' are the next characters
                        regex = new StringBuilder(regex).insert(i + 1, ".").toString();
                        i++;
                    }
                }
            }
            return regex;
        }

        private static int precedence(char operator) {
            switch(operator) {
                case '.':
                    return 2;
                case '|':
                    return 1;
                default:
                    return -1;
            }
        }

        public static String infixToPostfix(String infixRegex) {
            Deque<Character> stack = new ArrayDeque<Character>();

        String postfixRegex = "";
        for(int i = 0; i < infixRegex.length(); i++) {
            char c = infixRegex.charAt(i);
            switch(c) {
                case '.':
                case '|':
                    while(!stack.isEmpty() && precedence(c) <= precedence(stack.peek())) {
                        postfixRegex += stack.removeFirst();
                    }
                    stack.addFirst(c);
                    break;

                case '(':
                    stack.addFirst(c);
                    break;

                case ')':
                    while(!stack.isEmpty() && stack.peek() != '(') {
                        postfixRegex += stack.removeFirst();
                    }
                    stack.removeFirst();
                    break;

                default:
                    postfixRegex += c;
            }
        }

        while(!stack.isEmpty()) {
            postfixRegex += stack.removeFirst();
        }

        return postfixRegex;
    }
    }

    public static void main(String args[]) {
        String regex = args[0];
        String infixRegex = Helpers.useDotForConcatenation(regex);
      
        String postfixRegex = Helpers.infixToPostfix(infixRegex);
       
        RegexToENFA.regexToENFA(postfixRegex);
    }
}
