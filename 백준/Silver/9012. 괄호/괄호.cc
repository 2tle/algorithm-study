#include <stack>
#include <stdlib.h>
#include <stdio.h>
#include <iostream>
#include <string>
using namespace std;
bool isVPS(string t) {
    int tlength = (int)t.length();
    stack<char> tstack;
    for(int i=0;i<tlength;i++){
        char a = t[i];
        if(a=='('){
            tstack.push(a);
        } else {
            if(!tstack.empty())
                tstack.pop();
            else return false;
        }
    }
    if(tstack.empty()) return true;
    else return false;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    int t;
    cin >> t;
    for(int i=0;i<t;i++) {
        string str;
        cin >> str;
        if(isVPS(str)) std::cout << "YES" << std::endl;
        else std::cout << "NO" << std::endl;
        
    }
    return 0;
}