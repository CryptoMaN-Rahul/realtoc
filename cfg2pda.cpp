#include <bits/stdc++.h>
using namespace std;

int main() {
    int n;
    cout << "Enter the number of Production Rules of CFG: ";
    cin >> n;
    string s1;
    string s2;
    vector<pair<string, string>> v;

    cout << "Please enter the Production rules of CFG:\n";

    for (int i = 0; i < n; i++) {
        cin >> s1 >> s2;
        v.push_back(make_pair(s1, s2));
    }

    set<string> terminalSymbols;
    set<string> nonTerminalSymbols;

    for (int i = 0; i < n; i++) {
        string nonTerminal = v[i].first;
        nonTerminalSymbols.insert(nonTerminal); // Populate nonTerminalSymbols
        string production = v[i].second;

        // Split the production string by '|' to handle multiple production rules
        istringstream productionStream(production);
        string rule;
        while (getline(productionStream, rule, '|')) {
            for (char ch : rule) {
                if (isalpha(ch) && isupper(ch)) {
                    nonTerminalSymbols.insert(string(1, ch));
                } else if (isalnum(ch)) {
                    terminalSymbols.insert(string(1, ch));
                }
            }
        }

        if (production == "#") {
            terminalSymbols.insert("#"); // Use '#' to represent epsilon
        }
    }

    cout << "The Corresponding Production Rules For PDA are:" << endl;

    cout << "Rules For Non-Terminal Symbols are:" << endl;

    for (const string &nonTerminal : nonTerminalSymbols) {
        int flag = 0;
        cout << "dl(q,null," << nonTerminal << ") --> ";

        for (int i = 0; i < n; i++) {
            if (v[i].first == nonTerminal) {
                if (flag == 1) {
                    cout << " | ";
                }
                cout << "dl(q," << v[i].second << ")";
                flag = 1;
            }
        }

        if (flag != 0) {
            cout << endl;
        }
    }

    cout << "Rules For Terminal Symbols are:" << endl;
    for (const string &terminal : terminalSymbols) {
        if (terminal == "#") {
            cout << "dl(q,null,null) --> dl(q,null)" << endl; // Handle epsilon production
        } else {
            cout << "dl(q," << terminal << "," << terminal << ") --> dl(q,null)" << endl;
        }
    }
}
