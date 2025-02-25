# AULA 01 

## Nomeclatura
- Um arquivo .py em python, chamamos de módulo.
- Uma pasta dentro do workspace, chamamos de diretório.

1. Cases
``snake_case`` -> Tudo minúsculo, palavras separadas por underline.
``cammelCase `` -> Primeira letra da primeira palavra em minúsculo, e toda próxima palavra a primeira letra em maiuscúlo.

# Observações
1. Python é uma linguagem fracamente tipada.

# AULA 02

1. Para informar quantas casas decimais você quer após a virgula,utilizamos o comando :.2f
2. Ao dividirmos dois números inteiros, caso necessário, ocorre uma conversão implicita[casting].

# AULA 03

1. Em Python, temos no momento que vamos realizar alguma operação, existe uma predcedência.
Primeiramente, realizamos a * e a /
Depois a + e a -
Podemos utilizar os () para quebrar ou organizar uma operação.

2. Em Python toda vez que utilizamos o método ``input()`` a entrada automaticamente será do tipo ``string``.

3. Para converter uma string para ``int`` ou ``float``, podemos utlizar os métodos  ``int()`` ou ``float()``.

# AULA 05

## ESTRUTURAS DE REPETIÇÃO

1. for
=> Você irá utilizar quando de antemão se sabe a quantidade de vezes que a repetição irá acontecer.Normalmente é utilizado para ``iterar`` sobre elementosde uma sequência.
1.1 - range() => Gera uma sequência de números.(inclusive,exclusivo).

2. while
=> Será utilizado quando você não sabe ao certo quantas vezes a repetição irá acontecer.Será executada enquanto a condição for verdadeira.

# AULA 06

## COMANDOS DE DESVIO

1. continue -> Significa continuar,basicamente se uma condição for favorável, ela será descontinuada.
2. break -> Significa quebrar, quando utilizado irá finalizar o loop mais próximo.

## FUNÇÕES
=> É um bloco de código que é reutilizável serve para deixar o código mais organizado e eficiente. `Executam uma tarefa específica.`

# AULA 07

## PRINCÍPIOS DA PROGRAMAÇÃO ORIENTADA A OBJETOS (P.O.O) 

1. Encapsulamento
2. Herança -> É um conceito de POO que permite que uma classe herde atributos e métodos de outra,evitando a repetição do código.
3. Polimorfismo
4. Abstração

## PALAVRAS RESERVADAS EM POO

1. class -> É uma palavra-chave em python onde você cria um `molde`. Toda classe pode ter atributos e métodos,sendo que os atributos precisam estar dentro de um método chamado construtor (__init__)  
2. object -> É um nome dado a cada `cópia` criada da classe. Também conhecido como instância.
3. __init__ -> É um inicializador (construtor) onde você informe que toda cópia precisa passar aqueles valores no momento da criação.É um método especial.
4. self -> referencia o atributo atual da classe(o valor). 

##  TERMOS UTILIZADOS EM POO

1. método -> É uma função que está dentro de uma classe. É uma ação.
2. atributo -> São as caracteristicas de uma classe.

## HERANÇA

Teremos dois tipos de classes:
- superclass -> É a classe pai, é a que oferece a herança.
- subclass -> É a classe filha, que herda a herança.


## Atalhos no VScode
``CTRL + B`` => Oculta ou exibe o explorador.
``CTRL + ;`` => Comenta ou descomenta um código.
``CTRL + C`` => Copiar.
``CTRL + V`` => Colar.
``CTRL + Z`` => Desfazer a última alteração.
``SHIFT + ALT + SETA `` => Duplica a linha.
``CTRL + " `` => Oculta ou exibe o terminal.
``CTRL + D `` => Seleciona a próxima ocorrência da palavra.
``ALT + Z`` => Realiza uma quebra de linha.

## ATALHOS WINDOWS
``WINDOWS + Ç`` => Exibe icones e emotions.
``WINDOWS + R`` e escrever cmd abre terminal