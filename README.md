# rox_case
Como solução para o case foi proposto uma abordagem baseada em GCP (Google Cloud Platform) com utilização do ambiente BigQuery para análise de dados.

1° Passo: Carregamento dos daos em bucket do Cloud Storage
2° Passo: etapa de pré-processamento efetuada em ambiente DataPrep
3° Passo: carregamento de dados transformados em bucket do Cloud storage
4° Passo: definição de esquema em BigQuery
5° Passo: Criação de batch de transferência para ambiente BigQuery
6° Passo: realização de consultas SQL para visualização
7° Passo: criação de modelo de Machine Learning via BigQuery

Acesse a plataforma BigQuery:
  https://console.cloud.google.com/bigquery?project=rox-bike&ws=!1m0
  
  
Nota Importante:
Neste momento o projeto foi concebido de modo estático devido ao não conhecimento de domínio da aplicação, no entanto o processo para automatzá-lo é bem simples, mostrando mais uma das vantagens da plataforma GCP. Primeiramente é necessário o cadastramento (via inserção de email) dos agentes que terão acesso aos buckets de ingestão; logo em seguida é possível configurar a periodicidade (diária, semanal, mensal) dos bacthes de migração; e por fim definir o acesso ao ambiente de BigQuery pela equipe de Análise de Dados por exemplo.

Projeto BIKE: https://console.cloud.google.com/home/dashboard?folder=&organizationId=&project=rox-bike

No ambiente de BigQuery foi criado um modelod de ML bem simples a título de exemplificação.
