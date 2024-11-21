# asyncAPI
Async API, desenvolvida com FastAPI para buscar dados de CNPJ, 
utilizando RabbitMQ para gerenciamento de filas e Redis para armazenamento temporário de resultados, 
com suporte a implantação via Docker.

---

## 📋 Funcionalidades

1. **Envio de tarefas de scraping**:
   - Endpoint: `POST /scrape`
   - Recebe um **CNPJ** como entrada e envia uma tarefa para a fila RabbitMQ.

2. **Consulta do status e resultado de uma tarefa**:
   - Endpoint: `GET /results/{task_id}`
   - Retorna o status da tarefa (`pending`, `in_progress`, `completed`, `failed`) e, caso concluída, os dados extraídos.

3. **Processamento assíncrono**:
   - Tarefas são processadas por workers que consomem a fila RabbitMQ.
   - Resultados e status são armazenados temporariamente no Redis.

---

## 🏗️ Tecnologias Utilizadas

- **FastAPI**: Framework para desenvolvimento da API.
- **RabbitMQ**: Fila de mensagens para tarefas assíncronas.
- **Redis**: Armazenamento temporário para status e resultados.
- **Docker & Docker Compose**: Orquestração dos serviços.
- **Python**: Linguagem de desenvolvimento.

---

## ⚙️ Configuração e Execução  

### Pré-requisitos  

- **Docker** e **Docker Compose** instalados no sistema.

### Passos para execução  

1. **Clone o repositório**:

    ```bash
    git clone https://github.com/seu-usuario/web-scraping-api.git
    cd web-scraping-api
    ```

2. **Inicie os serviços** com Docker Compose:

    ```bash
    docker-compose up --build
    ```

3. **Acesse a API**:

    - Acesse a documentação interativa do FastAPI em: [http://localhost:8000/docs](http://localhost:8000/docs).

---


```shell
fastapi dev main.py
```
