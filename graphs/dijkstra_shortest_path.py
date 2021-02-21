# directed weighted graph
# (V+E)logV
INF  = 999

def dijkstra(start, stop, G):
    d = [INF for _ in range(len(G))]
    p = [i for i in range(len(G))] # parent
    d[start] = 0
    q = [[start, 0]]

    while len(q) != 0:
        # not needed should be heap but whatever
        q = sorted(q, key=lambda x: x[1])

        x = q.pop(0)[0]
        for y in range(len(G)):
            if G[x][y] != 0 and d[y] > d[x] + G[x][y]:
                d[y] = d[x] + G[x][y]
                p[y] = x
                # will enter multiple times but not processed
                q.append([y, d[y]])
    print(p)
    print(d)
    print(d[stop])


def uniform(start, stop, G):
    # for infinite graphs
    p = [i for i in range(len(G))] # parent
    u = [0 for i in range(len(G))]
    q = [[start, 0]]

    while len(q) != 0:
        # not needed should be heap but whatever
        q = sorted(q, key=lambda x: x[1])

        x, d = q.pop(0)
        u[x] = 1

        if x == stop:
            print(d)
            return

        for y in range(len(G)):
            if G[x][y] != 0 and u[y] == 0:
                p[y] = x
                q.append([y, d + G[x][y]])

G = [
[0, 4, 0, 0, 0, 0, 0, 8, 0],
[4, 0, 8, 0, 0, 0, 0, 11, 0],
[0, 8, 0, 7, 0, 4, 0, 0, 2],
[0, 0, 7, 0, 9, 14, 0, 0, 0],
[0, 0, 0, 9, 0, 10, 0, 0, 0],
[0, 0, 4, 14, 10, 0, 2, 0, 0],
[0, 0, 0, 0, 0, 2, 0, 1, 6],
[8, 11, 0, 0, 0, 0, 1, 0, 7],
[0, 0, 2, 0, 0, 0, 6, 7, 0]
]

dijkstra(0, 7, G)
uniform(0, 7, G)




#### DIJKSTRA HEAP C++


##include <cstdio>
##include <vector>
##include <algorithm>

#using namespace std;

##define INF 99999999
##define N 1000

#int n,m,nn,h[N],p[N];
#vector <int> f[N],v[N];
#int d[N]; //distance

#void heap_swap(int x,int y) {
#    swap(h[x],h[y]);
#    p[h[x]]=x;
#    p[h[y]]=y;
#}

#void heap_up(int x) {
#    if(x>1 && d[h[x]]<d[h[x/2]])
#    {
#        heap_swap(x,x/2);
#        heap_up(x/2);
#    }
#}

#void heap_down(int x) {
#    if(2*x+1<=n)
#    {
#        if(d[h[x]]>d[h[2*x]] && d[h[2*x]]<=d[h[2*x+1]])
#        {
#            heap_swap(x,2*x);
#            heap_down(2*x);
#        }
#        if(d[h[x]]>d[h[2*x+1]] && d[h[2*x+1]]<=d[h[2*x]])
#        {
#            heap_swap(x,2*x+1);
#            heap_down(2*x+1);
#        }
#    }
#    if(2*x<=n && d[h[x]]>d[h[2*x]])
#    {
#         heap_swap(x,2*x);
#         heap_down(2*x);
#    }
#}

#int main()
#{
#    freopen("input.in","r",stdin);
#    freopen("output.out","w",stdout);
#    int i,x,y,k;
#    scanf("%d%d",&n,&m);
#    nn=n;
#    for(i=1;i<=m;i++)
#    {
#        scanf("%d%d%d",&x,&y,&k);
#        f[x].push_back(y); // friend of x
#        v[x].push_back(k); // weight from x to friend
#    }
#    for(i=1;i<=n;i++)
#    {
#        h[i]=i;
#        d[i]=INF;
#        p[i]=i;
#    }
#    d[1]=0; // source node 1
#    while(n)
#    {
#        x=h[1]; // the min
#        heap_swap(1,n);
#        n--;
#        heap_down(1); // restore the heap
#        for(i=0;i<f[x].size();i++)
#            if((v[x][i]+d[x])<d[f[x][i]])
#            {
#                d[f[x][i]]=v[x][i]+d[x];
#                heap_up(p[f[x][i]]);
#            }
#    }
#    for(i=2;i<=nn;i++) // distence from source to every node
#    {
#        if(d[i]==INF)
#            printf("0 ");
#        else
#            printf("%d ",d[i]);
#    }
#    printf("\n");
#    return 0;
#}

