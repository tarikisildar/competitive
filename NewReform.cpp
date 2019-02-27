#include<bits/stdc++.h>
using namespace std;

void addEdge(vector<int> adj[], int u, int v)
{
    adj[u].push_back(v);
    adj[v].push_back(u);
}
int count1=0;
int count2=1;

void BFSUtil(int u, vector<int> adj[],
            vector<bool> &visited)
{

    list<int> q;

    visited[u] = true;
    q.push_back(u);
    
    while(!q.empty())
    {

        u = q.front();
        q.pop_front();
        
        for (int i = 0; i != adj[u].size(); ++i)
        {
            count1++;
            if (!visited[adj[u][i]])
            {
                count2++;
                visited[adj[u][i]] = true;
                q.push_back(adj[u][i]);
            }
        }
    }
}
int ans = 0;
void BFS(vector<int> adj[], int V)
{
    vector<bool> visited(V, false);
    for (int u=0; u<V; u++)
        if (visited[u] == false) {
            BFSUtil(u, adj, visited);
            ans+=(count1/2<count2);

            count1= 0;
            count2=1;
        }
}
int main(){
    int n,m;
    cin >> n >>m;

    vector<int> adj[n];
    for(int i=0;i<m;i++){
        int u,v;
        cin >> u >>v;
        addEdge(adj,u-1,v-1);

    }
    BFS(adj,n);
    cout << ans;
}
//https://codeforces.com/problemset/problem/659/E
