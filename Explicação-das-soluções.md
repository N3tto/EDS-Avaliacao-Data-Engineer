# Problema 1
Apenas um simples CREATE TABLE utilizando as requisições passadas no problema. Adicionei um DROP TABLE IF EXISTS apenas para testes, assim como em outras resoluções.

# Problema 2
Também uma solução bem simples inserindo dados na tabela de paciente do schema stg_protuario, pegando os dados das outras tabelas, sem se preocupar muito com dados repetidos já que os próximos problemas tratam disso.

# Problema 3
Um SELECT que faz a contagem de cada CPF para verificar se há valores repetidos. Achei que seria melhor verificar pelo CPF.

# Problema 4
Neste problema decidi usar uma subconsulta criando a tabela repetidos, primeiro é feito um SELECT na tabela Paciente, onde é retornado nome, CPF e o dt_atualizado, então utilizei a função ROW_NUMBER(), que divide a tabela em partições, que no caso foi definido pelo CPF e então dá um número sequencial a cada um, onde a sequência foi definida pelo dt_atualizado de forma decrescente. Então fiz um SELECT nessa subconsulta procurando os valores de nome, CPF e dt_atualizado onde o row_num fosse igual a 1.

# Problema 5
Neste problema eu utilizei o pandas para ler o csv e o pyodbc para conectar ao banco. Criei uma variável com todas as configurações do banco, depois abri a conexão, peguei os dados de um csv e tratei eles para o formato desejado, criei um script SQL e utilizei um for para inserir de linha a linha dos dados que recuperei do csv, utilizando o script SQL e por último encerrei a conexão com o banco.

# Problema 6
Esse foi igual ao anterior com a exceção da utilização da biblioteca requests para leitura dos dados a partir de uma API e do tratamento dos dados, já que ele vem como json.

# Problema 7
Criei as duas tabelas pedidas utilizando as requisições necessárias. Criei uma chave estrangeira, id_atendimento, na tabela diagnostico para que um diagnóstico tenha um atendimento, enquanto um atendimento pode ter múltiplos diagnósticos como não depende da tabela diagnostico, como foi solicitado.

# Problema 8
Nesta consulta eu utilizei um SELECT simples com a função AVG() para retornar a quantidade média de diagnósticos dos atendimentos do tipo U.

# Problema 9
Neste problema criei uma função que dada duas listas, sendo uma a prescrição e outra o estoque de remédios, retornaria se há remédios disponíveis para a prescrição. Basicamente utilizei um for para iterar por toda prescrição e um if para verificar se cada item da prescrição está no estoque. Como criei a variável avaliable anteriormente como true, se o medicamento não estiver disponível no estoque ela será alterada para false e no final a função retorna a variável avaliable.

# Problema 10
Neste problema eu criei uma visualização utilizando as bibliotecas pandas, para o tratamento de dados, plotly para plotagem de gráficos e streamlit para criação de um dashboard simples, por uma aplicação web. Criei dois arquivos csv para testar e demonstrar a aplicação, utilizando um gerador simples na internet, os dados estão no formato "YYYY-mm-dd HH:MM:SS". Deixei um drag and drop para carregar um csv com os dados das datas dos atendimentos, quando inserido algum arquivo, o pandas faz a leitura e o tratamento dos dados, preferi por separá-los em data e hora, para facilitar a visualização. E utilizei o plotly para criar um gráfico de barras com os dados tanto de data quanto de horário do atendimento. Os dados que utilizei estão na pasta dados_e_resultados_problema_10 assim como os prints da tela com os resultados.