# Data engineer Test por Guilherme Henrique Alves Ribeiro

Para reproduzir as análises começamos com a instalação do PostgreSQL na máquina, foi usado para estes testes a versão 13
Criar um banco de dados e colocar a senha.
No arquivo database.py na linha 49 podemos configurar em qual banco de dados conectar assim como senha e usuário.

Inserir as bases de dados na pasta Data do projeto. 

Inicialmente executar o arquivo databaseCrete.py que vai fazer a criação da tabela.
Após isso executar o arquivo databaseGen.py para inserir a base de dados no banco.

Ao executar o arquivo mediaDist.py este printa a média das distâncias para viagens com no máximo 2 passageiros.

Ao executar o arquivo vendorsArrecadacao.py este printa uma tupla da empresa de maior arrecadação e o valor arrecadado.

Ao executar o arquivo histograma.py este gera um json com os valores para cada mês de cada ano das corridas pagas em dinheiro, após executar este arquivo podemos executar o arquivo histogramaPlot.py para gerar a imagem do histograma a partir do json.

Ao executar o arquivo data_serie.py este mostra na tela o gráfico de série temporal com a soma dos valores das gorgetas para cada dia dos últimos 3 meses do ano de 2012.


Ao executar o arquivo corridas_fds.py ele printa o tempo médio para as corridas nos dias de sábado e domingo em minutos e segundos

Ao executar o arquivo map_points plot.py ele mostra na tela um mapa de nova york com os pontos de subida e descida nos taxis.

O arquivo Análise.html se encontra na pasta output deste repositório.
