#include <fstream>
using namespace std;
#define N 100000

char s[N];
int i=0;

int termen();
int factor();

int eval() // + -
{
    int r=termen();
    while(s[i]=='+'||s[i]=='-')
    {
        if(s[i]=='+')
        {
            i++;
            r+=termen();
        }
        else if(s[i]=='-')
        {
            i++;
            r-=termen();
        }
    }
    return r;
}

int termen() // * /
{
    int r=factor();
    while (s[i]=='*'||s[i]=='/')
    {
        if(s[i]=='*')
        {
            i++;
            r*=factor();
        }
        else if(s[i]=='/')
        {
            i++;
            r/=factor();
        }
    }
    return r;
}

int factor() // paranteze
{
    int r=0;
    if(s[i]=='(')
    {
        i++;
        r=eval();
        i++;
    }
    else
    {
        while(s[i]>='0'&&s[i]<='9')
        {
            r=r*10+s[i]-'0';
            i++;
        }
    }
    return r;
}

int main()
{
    ifstream in("input.in");
    ofstream out("output.out");
    in>>s;
    out<<eval()<<endl;
    return 0;
}
