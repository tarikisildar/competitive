#include <limits>
#include<bits/stdc++.h>
#define min(x,y,z) (x < y ? (x < z ? x : z) : (y < z ? y : z))
using namespace std;

int main(){
    int imax = std::numeric_limits<int>::max();
    int n,m;
    cin >> n;
    int arr[n];
    for(int i=0;i<n;i++){
        cin >> m;
        arr[i]=m;
    }

    int dist[n][n][2];
    for(int i = 0; i<n; i++){
        for(int e = 0; e<n; e++) {
            if(i == e){
                dist[i][i][0] = 0;
                dist[i][i][1] = 0;
            }
            else{
                dist[i][e][0] = imax-1;
                dist[i][e][1] = imax-1;
            }
        }
    }
    for(int r =0;r<n;++r){
        for(int l = r; l>=0;--l){
            if(l){
                dist[l-1][r][0] = min(dist[l-1][r][0],dist[l][r][0] + int(arr[l-1] != arr[l]),dist[l][r][1]+int(arr[l-1]!=arr[r]));
            }
            if(r+1 < n){
                dist[l][r+1][1] = min(dist[l][r+1][1],dist[l][r][0] + int(arr[l] != arr[r+1]),dist[l][r][1] + int(arr[r] != arr[r+1]));
            }
        }
    }
    cout << (dist[0][n-1][0] < dist[0][n-1][1] ? dist[0][n-1][0] : dist[0][n-1][1]);

}
//https://codeforces.com/contest/1114/problem/D
