# Programação Python 

Aqui estara todos os códigos disponíveis aprendidos durante a disciplina de Programação Python na Universidade Federal de Santa Maria. 

# Criando funções no Python

A sintaxe de uma função é definida por três partes: nome, parâmetros e corpo, o qual agrupa uma sequência de linhas que representa algum comportamento. No código abaixo, temos um exemplo de declaração de função em Python:

```Python
def hello(meu_nome):
  print('Olá',meu_nome)
```
Essa função, de nome hello, tem como objetivo imprimir o nome que lhe é passado por parâmetro (também chamado de argumento). A palavra reservada def, na primeira linha, explicita a definição da função naquele ponto. Em seguida, entre parênteses, temos o parâmetro meu_nome. Ainda na mesma linha, observe a utilização dos dois pontos (:), que indicam que o código identado nas linhas abaixo faz parte da função que está sendo criada. Aqui, é importante ressaltar que, para respeitar a sintaxe da linguagem, a linha 2 está avançada em relação à linha 1.

Para executar a função, de forma semelhante ao que ocorre em outras linguagens, devemos simplesmente chamar seu nome e passar os parâmetros esperados entre parênteses, conforme o código a seguir.
```Python
>>> hello('Fabio')
Olá Fabio
>>> meu_nome
'Fabio'
```
Caso seja necessário, também é possível definir funções com nenhum ou vários argumentos, como no código abaixo:
```Python
def hello(meu_nome,idade):
   print('Olá',meu_nome,'\nSua idade é:',idade)
```
# Divisão e conquista 
Escrevendo um algoritmo recursivo que conta quantos elementos existem em um vetor. Antes pensa no caso base quando o vetor tem tamanho 0 ou 1 e o caso recursivo que divide o vetor em 2 pra fazer as somas indepedente pra depois somar os dois resultados no final como demonstrado no algortimo abaixo: 

```Python
def conta_elementos(vetor):
    # Caso base: se o vetor estiver vazio, retorne 0
    if len(vetor) == 0:
        return 0

    elif len(vetor) == 1:
        return 1
    else:
        # Divida o vetor ao meio
        meio = len(vetor) // 2
        # Conquiste: conte os elementos na primeira metade e na segunda metade
        return conta_elementos(vetor[:meio]) + conta_elementos(vetor[meio:])

# Testando a função
vetor = [1, 2, 3, 4, 5]
print(conta_elementos(vetor))  # Deve imprimir 5
```
