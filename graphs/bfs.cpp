#include <bits/stdc++.h>
using namespace std;
vector<int> v[100];
bool visited[100];
int level;
queue<int> q;
int main(){
    int a, b, n, e, s, i, j, k, l;
    cin >> n >> e >> s;
    for (i = 1; i <= e; i++){
        cin >> a >> b;
        v[a].push_back(b);
        v[b].push_back(a);
    }
    for (i = 0; i <= n; i++){
        visited[i] = false;
    }
    q.push(s);
    visited[s] = true;
    level = 0;
    int siz = 0;
    while (!q.empty()){
        printf("Level = %d\n", level);
        siz = q.size();
        while (siz--){
            int f = q.front();
            q.pop();
            printf("%d\n", f);
            for (i = 0; i < v[f].size(); i++){
                if (visited[v[f][i]] == false){
                    visited[v[f][i]] = true;
                    q.push(v[f][i]);
                }
            }
        }
        level++;
    }
}
