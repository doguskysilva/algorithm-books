#### Código base para o capítulo 2
O livro apresenta versões do algoritmo abaixo para diversas linguagens. Abaixo implementei o código em Python

 > Entrada: dado um número inteiro (tamanho da lista), maior que 0 e menor que 100, seguido por valores inteiros do tamanho da lista.
 > Saída: o número de valores de entrada que são maiores que a média de todos os valores de entrada

```python
list_numbers = []
result = 0
average = 0
list_sum = 0

size_list = int(input("Size of list: "))

if size_list > 0 and size_list < 100:
    for counter in range(0, size_list):
        list_numbers.append(int(input("Put a number: ")))
        list_sum = list_sum + list_numbers[counter]

    average = list_sum / size_list

    for counter in range(0, size_list):
        if list_numbers[counter] > average:
            result = result + 1

    print(f"The numbers above the average is {result}")
else:
    print("Length to list is not legal")
```