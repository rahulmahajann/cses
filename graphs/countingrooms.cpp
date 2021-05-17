/*
    No matter how long a night, dawn will always break.
*/
#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
typedef long double LD;
#define FR(i,a,b)               for(int i=(a);i<(b);i++)
#define nl                      cout<<"\n";
#define int                     long long
#define double                  long double
#define inf                     (1e18)
 
const int mod=1000000007;
const int MAX=1e3+5;
int n=0,i=0,j=0,m;
 
bool vist[1002][1003];
char ar[1002][1002];
 
pair<ll,ll> path_moves[4]={{1,0},{-1,0},{0,1},{0,-1}};
 
bool valid_move(ll x,ll y)
{
    if(x<1 or x>n or y<1 or y>m)return false;
 
    if(vist[x][y]==true)return false;
    if(ar[x][y]=='#')return false;
 
    return true;
}
 
void dfs(ll x,ll y)
{
    vist[x][y]=true;
    for(ll k=0;k<4;k++)
    if(valid_move(x+path_moves[k].first,y+path_moves[k].second))
    dfs(x+path_moves[k].first,y+path_moves[k].second);
}
 
void solve()
{
    cin>>n>>m;
 
    for(i=1;i<=n;i++)for(j=1;j<=m;j++)
    {
        cin>>ar[i][j];
        if(ar[i][j]=='#'){
            vist[i][j]=true;
        }
    }
    ll ans=0;
 
    for(i=1;i<=n;i++)
    for(j=1;j<=m;j++)
    if(ar[i][j]=='.' and vist[i][j]==false)
    dfs(i,j),ans++;
    cout<<ans;
}
 
signed main()
{   
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);  cout.tie(NULL);
    
    // int N27;cin>>N27; while(N27--){ solve(); nl }
 
    solve();
 
    return 0;
}
