import java.io.*;
import java.util.*;

class Main {

  public static void main(String[] args) throws IOException {

    // Take production rules input
    Scanner sc = new Scanner(System.in);

    System.out.print("Enter number of production rules: ");
    int n = sc.nextInt();

    Vector<Pair> rules = new Vector<>();
    System.out.println("Enter production rules:");

    for(int i=0; i<n; i++) {
      String left = sc.next();
      String right = sc.next();
      rules.add(new Pair(left, right)); 
    }

    // Extract symbols
    Set<String> nonTerminals = new HashSet<>();
    Set<String> terminals = new HashSet<>();

    for(Pair rule: rules) {
      
      String production = rule.right;

      if(production.contains("|")) {
        StringTokenizer st = new StringTokenizer(production, "|");
        while(st.hasMoreTokens()) {
          String prod = st.nextToken();
          getSymbols(prod, nonTerminals, terminals);
        }
      }
      else {
        getSymbols(production, nonTerminals, terminals);
      }

      if(production.equals("#")) {
        terminals.add("#");
      }

    }

    // Print PDA rules
    System.out.println("PDA Production Rules:");

    for(String nonTerm: nonTerminals) {

      System.out.print("dl(q,null," + nonTerm + ") --> ");
      
      boolean first = true;

      for(Pair rule: rules) {

        if(rule.left.equals(nonTerm)) {

          String production = rule.right;

          if(production.contains("|")) {
            StringTokenizer st = new StringTokenizer(production, "|");
            while(st.hasMoreTokens()) {
              if(!first) {
                System.out.print(" | ");
              }
              System.out.print("dl(q," + st.nextToken() + ")");
              first = false;
            }
          }
          else {
            if(!first) {
              System.out.print(" | ");
            }
            System.out.print("dl(q," + production + ")");
            first = false;
          }

        }

      }

      System.out.println();

    }

    // Print terminal rules
    for(String term: terminals) {
      if(term.equals("#")) {
        System.out.println("dl(q,null,null) --> dl(q,null)");
      } else {
        System.out.println("dl(q," + term + "," + term + ") --> dl(q,null)");
      }
    }

  }

  static void getSymbols(String production, Set<String> nonTerminals, Set<String> terminals) {
    for(char ch: production.toCharArray()) {
      if(Character.isUpperCase(ch)) {
        nonTerminals.add(String.valueOf(ch));
      } else if(Character.isLetterOrDigit(ch)) {
        terminals.add(String.valueOf(ch));  
      }
    }
  }

}

class Pair {
  String left;
  String right;

  public Pair(String left, String right) {
    this.left = left;
    this.right = right;
  }
}
