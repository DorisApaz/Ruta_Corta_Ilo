#include <iostream>
#define max 200
using namespace std;
int main()
{
    int A[max],j,b,c,i,k,n;
    cout<<"Ingresa la cantidad de ordenamiento: ";
    cin>>n;
    for(i=1;i<=n;i++)
    cin >> A[i];
    for(k=n;k>0;k--)
    {
        for(i=1;i<=k;i++)
        {
            b=A[i];
            j=i/2;
            while(j>0 && A[j]<b)
            {
                A[i]=A[j];
                i=j;
                j=j/2;
            }
            A[i]=b;
        }
        c=A[1];
        A[1]=A[k];
        A[k]=c;
    }
    cout<<"El orden es:"<<endl;
    for(i=1;i<=n;i++)
    cout<<A[i] << endl;
    return 0;
}
