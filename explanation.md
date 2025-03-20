# Desafio Técnico - Squad "Melhorias Estruturantes"
## Objetivo:
Criar uma API que permita realizar web scraping de informações de uma página pública e processar os dados de forma assíncrona utilizando filas de mensagens. A API deve ser escalável e preparada para ser implantada em um ambiente Docker com RabbitMQ e Redis.

---

### Requisitos Técnicos:
1. API com FastAPI 
2. Criar uma API utilizando o framework FastAPI com os seguintes endpoints:
   3. POST /scrape: Recebe um CNPJ como entrada e envia a tarefa de scraping para uma fila (RabbitMQ). 
   4. GET /results/{task_id}: Retorna o status da tarefa de scraping e, caso esteja concluída, os dados processados.
5. **Processamento Assíncrono com RabbitMQ:** Utilizar o RabbitMQ para gerenciar as tarefas de web scraping de forma assíncrona. O serviço de scraping deve pegar as tarefas da fila e processá-las.
6. **Armazenamento Temporário com Redis:** Armazenar o status das tarefas e os resultados no Redis para consulta posterior através do endpoint GET /results/{task_id}.
7. **Docker e Docker Compose:** Preparar o projeto para ser executado com Docker e Docker Compose. Todos os serviços (API, workers de scraping, RabbitMQ, Redis) devem estar devidamente configurados nos containers.

### Instruções para Implementação:
1. **Web Scraping:** Realizar o scraping dos dados no seguinte site:
2. URL: Consulta Sintegra - Goiás 
3. Dados de entrada: CNPJ
4. Exemplos de CNPJs para consulta:
   5. 00006486000175 
   6. 00012377000160 
   7. 00022244000175 
8. Extrair as informações principais apresentadas na página para cada CNPJ consultado (razão social, endereço, situação cadastral, etc.). 
9. **Tarefas Assíncronas:** As tarefas de scraping devem ser enviadas para o RabbitMQ e processadas por workers assíncronos. 
10. **Redis:** Utilize o Redis para armazenar temporariamente o status e os resultados das tarefas, que poderão ser recuperados via a API. 
11. **Estrutura do Projeto:** Organize o projeto de forma modular, com arquivos e pastas bem definidas (por exemplo, app/, worker/, docker-compose.yml).

### Critérios de Avaliação:
1. Funcionalidade e Corretude:
   2. A API funciona conforme o esperado? O scraping é realizado corretamente? 
   3. O sistema de filas e processamento assíncrono está bem implementado? 
4. Qualidade do Código:
   5. O código é limpo, modular e fácil de entender? 
   6. Segue boas práticas de desenvolvimento Python (PEP8)? 
7. Uso de Docker:
   8. O projeto está corretamente configurado para rodar com Docker e Docker Compose? 
   9. A arquitetura é escalável e extensível? 
10. Testes:
    11. O candidato incluiu testes automatizados? (Testes unitários para as funções principais são um diferencial)
12. Documentação:
    13. O projeto está bem documentado, com instruções claras de como rodar o ambiente localmente e explicações sobre a arquitetura?
