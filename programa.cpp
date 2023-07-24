#include <iostream>
#define max 100
using namespace std;
int main()
{
    int A[max],j,item,temp,i,k,n;
    cout<<"Ingresa la cantidad de elementos del arreglo: ";
    cin>>n;
    for(i=1;i<=n;i++)//para determinar que el usuario  ingrese la cantidad de elementos que se guardó en n//
    cin >> A[i];//para leer los numeros ingresados//
    for(k=n;k>0;k--)//para controlar los numeros que se vayan comparando//
    {
        for(i=1;i<=k;i++)//j vale 0 cuando i vale 1//
        {
            item=A[i];
            j=i/2;
            while(j>0 && A[j]<item)//mientras//
            {
                A[i]=A[j];
                i=j;
                j=j/2;
            }
            A[i]=item;
        }
        temp=A[1];
        A[1]=A[k];
        A[k]=temp;
    }
    cout<<"El orden es:"<<endl;
    for(i=1;i<=n;i++)//para imprimir en el orden deseado//
    cout<<A[i] << endl;
    return 0;
}
