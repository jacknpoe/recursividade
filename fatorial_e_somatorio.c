#include<stdio.h>

long somatorio(long numero)
{
	if(numero == 1) return 1;
	return somatorio(numero - 1) + numero;
}

long fatorial(long numero)
{
	if(numero == 1 || numero == 0) return 1;
	return fatorial(numero - 1) * numero;
}

int main(void)
{
	printf("%d\n", somatorio(10));
	printf("%d\n", fatorial(10));
}
