// RMQ - Range Minimum Query


#include <cstdio>
#include <vector>

using namespace std;

#define INF 100001
#define LOG 30

int n,m,l,lg2[INF],v[LOG][INF],x,y,d;

int main()
{

    freopen("input.in","r",stdin);
    freopen("output.out","w",stdout);
    int i,j;
    scanf("%d%d",&n,&m);
    lg2[0]=-1;
    for(i=1;i<=n;i++)
    {
        scanf("%d",&v[0][i]);
        lg2[i]=lg2[i/2]+1; // compute log
    }
    for(i=1;i<=lg2[n]+1;i++)
    {
        x=1<<i-1; // power
        for(j=1;j<=n-x*2+1;j++)
            v[i][j]=min(v[i-1][j],v[i-1][j+x]);
    }
    while(m--)
    {
        scanf("%d%d",&x,&y);
        i=y-x+1;  //diferenta
        j=i-(1<<lg2[i]);
        printf("%d\n",min(v[lg2[i]][x],v[lg2[i]][x+j]));
    }
    return 0;
}





// LCA - Lowest Common Ancestor


#include <cstdio>
#include <vector>

using namespace std;

#define NR 200010

int er=1,u[NR],q[NR],lg[NR],e[20][NR];
vector <int> v[NR];

void dfs(int k) // generate first line for RMQ
{
    int i;
    if(!q[k])
        q[k]=er;
    e[0][er++]=k;
    for(i=0;i<v[k].size();i++)
        if(u[v[k][i]]==0)
        {
            u[v[k][i]]=1;
            dfs(v[k][i]);
            e[0][er++]=k;
        }
}

void rmq() // range minimum query
{
    int x,i,j;
    for(i=1;i<=lg[er]+1;i++)
    {
        x=1<<i-1;
        for(j=1;j<=er-2*x+1;j++)
            e[i][j]=min(e[i-1][j],e[i-1][j+x]);
    }
}

int query(int x, int y)
{
    x=q[x];
    y=q[y];
    if(x>y)
        swap(x,y);
    int i=y-x+1;
    int j=i-(1<<lg[i]);
    return min(e[lg[i]][x],e[lg[i]][x+j]);
}

int main()
{
    freopen("input.in","r",stdin);
    freopen("input.out","w",stdout);
    int n,m,x,y,i;
    scanf("%d%d",&n,&m);
    for(i=2;i<=n;i++)
    {
        scanf("%d",&x);
        v[x].push_back(i);
    }

    u[i]=1;
    dfs(1);
    er--;

    lg[1]=0;
    for(i=2;i<=er;i++)
        lg[i]=lg[i/2]+1;
    rmq();

    while(m--)
    {
        scanf("%d%d",&x,&y);
        printf("%d\n",query(x,y));
    }
    return 0;
}
