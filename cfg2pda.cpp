#include <bits/stdc++.h>
using namespace std;

int main() {
    int n;
    cout << "Enter the number of Production Rules of CFG: ";
    cin >> n;
    char s1;
    string s2;
    vector<pair<char, string>> v;

    cout << "Please enter the Production rules of CFG:\n";

    for (int i = 0; i < n; i++) {
        cin >> s1 >> s2;
        v.push_back(make_pair(s1, s2));
    }

    set<char> terminalSymbols;
    set<char> nonTerminalSymbols; // Corrected declaration

    for (int i = 0; i < n; i++) {
        char nonTerminal = v[i].first;
        nonTerminalSymbols.insert(nonTerminal); // Populate nonTerminalSymbols
        string production = v[i].second;
        for (char ch : production) {
            if (isalpha(ch) && islower(ch)) {
                terminalSymbols.insert(ch);
            }
            if (ch == '#') {
                terminalSymbols.insert('#'); // Use '#' to represent epsilon
            }
        }
    }

    cout << "The Corresponding Production Rules For PDA are:-" << endl;

    cout << "Rules For Non-Terminal Symbols are:-\n";

    for (const char &nonTerminal : nonTerminalSymbols) {
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

    
    for (const char &terminal : terminalSymbols) {
        if (terminal == '#') {
            cout << "dl(q,null,null) --> dl(q,null)" << endl; // Handle epsilon production
        } else {
            cout << "dl(q," << terminal << "," << terminal << ") --> dl(q,null)" << endl;
        }
    }
}
