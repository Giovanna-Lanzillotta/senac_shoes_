# 4. **Controle de Estoque**  
# `Crie` um `dicionário com os estoques` de cada sabor.
#  `Decremente` o estoque conforme os pedidos feitos e 
# exiba uma `mensagem se o estoque acabar.`

estoque = {
    "mussarela": 10,
    "presunto": 5,
    "calabresa": 3,
    "portuguesa": 2
}

pedido = int(input("qual sabor você quer? \n 1 - mussarela \n 2 - presunto \n 3 - calabresa \n 4 - portuguesa \n"))

if pedido == 1:
    estoque["mussarela"] -=1
elif pedido == 2:
    estoque["presunto"] -=1
elif pedido == 3:
    estoque["calabresa"] -=1
elif pedido == 4:
    estoque["portuguesa"] -=1
else:
    print("valor invalido")

if estoque[pedido] == 0:
     print("O estoque acabou!")
 

            #TERMINAR DE FAZER