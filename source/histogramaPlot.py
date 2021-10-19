import json
import matplotlib.pyplot as plot

with open('data\data_histograma.json', 'r') as fp:
    dados_dic=json.load(fp)
lista=[]
for ano in range(2009,2013):
    
    print(ano)
    for mes in range(12):
        print (mes)
        lista.append(dados_dic[str(ano)][str(mes+1)])
   
print(lista)



n,bins,patches = plot.hist(lista,ec='black')
plot.xticks(bins)
plot.title("Distribuição mensal das corridas pagas em Dinheiro ")
plot.xlabel("Quantidade mensal")
plot.ylabel("Frequência")
plot.grid(True,linestyle='dotted',axis='y')
plot.savefig('output\histograma.png')
