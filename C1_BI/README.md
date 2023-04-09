#EXECUÇÃO DO WEB SCRAPING 

Para agendar a execução do script Python diariamente no Windows, você pode usar o Agendador de Tarefas. Aqui está um passo a passo:

Abra o Agendador de Tarefas. 

No Agendador de Tarefas, clique em "Criar Tarefa Básica" no painel de navegação à direita.

Na janela de criação de tarefa, dê um nome para a tarefa e uma descrição opcional. Em seguida, clique em "Avançar".

Escolha a frequência com que deseja que a tarefa seja executada. No seu caso, selecione "Diariamente". Clique em "Avançar".

Escolha a hora em que deseja que a tarefa seja executada. Escolha um horário em que você sabe que o computador estará ligado e conectado à Internet. Clique em "Avançar".

Escolha "Iniciar um programa" como a ação a ser realizada pela tarefa. Clique em "Avançar".

Na caixa de diálogo digite o caminho completo para o arquivo Python que você deseja executar "C:\Users\PH\Desktop\BI\scrape.py".

Clique em "Avançar".

Verifique as configurações da tarefa na próxima tela e clique em "Concluir" para criar a tarefa.


#TRATAMENTO DOS DADOS 

Para fazer o tratamento dos dados, basta você rodar o consulta.py

Antes de rodar, baixe os requerimentos.txt 

Execute o comando '''pip install -r requerimentos.txt'''


Após a instalação, execute o consulta.py
O código vai gerar um arquivo .db na pasta que foi executado o código. 
o código vai ter na sua tabela fato a quantidade de mortes, e suas dimensões são: 'Municipio', 'ViagemBrasil', 'ViagemInternacional', 'Sexo', 'ComorbidadeTabagismo', 'ComorbidadeCardio', 'ComorbidadeRenal','ComorbidadeObesidade', 'ComorbidadeDiabetes'.


Para abrir o arquivo .db eu usei o DB Browser. 

Link para instalar: https://sqlitebrowser.org/dl/

A partir disso voce consegue criar as consultas dentro do SQLITE.




