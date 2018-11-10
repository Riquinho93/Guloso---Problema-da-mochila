'''''
    FOI DESENVOLVIDO POR HENRIQUE DAS VIRGENS E BORELOI INDI
'''''
print("PROBLEMA DA MOCHILA COM GULOSO\n")

#Lista dos pesos
peso  = [1,2,3,4,5,6,7]
#Lista do valores de cada peso
valor = [12, 14, 30, 49, 37, 9, 22]
#Valores que vão entrar na mochila
mochila = list()

#Capacididade da mochila
capacidade = 15
print('CAPACIDADE DA MOCHILA = ',capacidade)

#Recebendo os valores da lista dos pesos
print('LISTA DE ITENS')
for i in range (len(peso)):
    print('| Peso: {} | Valor:| {} |'.format(peso[i],valor[i]))

total_pesos = 0
valor_total = 0
aux1 = peso[:]
aux1 = valor[:]

while len(aux1) != 0:
    #Pegando o maior valor
     i = valor.index(max(aux1))
    #Verifica se o peso maior valor é maior do que a capacidade da mochila
     if (capacidade  - peso[i]) < 0:
         aux1.remove(max(aux1))     #Se for remove da lista auxiliar
     else:
         capacidade -= peso[i]     #Se não subtrai a capacidade da mochila e peso
         mochila.append([i+1,peso[i],valor[i]])     #Colocando o iten na mochila
         aux1.remove(max(aux1))

print('\n---------------------------------------')
print('\n GULOSO POR MAIOR VALOR')
for i in mochila:
    print( f'peso = |{i[1]}| e 'f'valor |{i[2]}| ')
    total_pesos += i[1]
    valor_total += i[2]
#Valores total
print('Total: {}    Total:{}'.format(total_pesos,valor_total))
print('\n---------------------------------------')