import requests
from bs4 import BeautifulSoup


def scrape_data(cnpj: str):
    response = requests.post("https://www.consultasintegra.go.gov.br", data={"cnpj": cnpj})
    soup = BeautifulSoup(response.content, "html.parser")

    # Parsear os dados relevantes (razão social, endereço, etc.)
    # Exemplo fictício:
    data = {
        "razao_social": soup.find(id="razao_social").get_text(),
        "endereco": soup.find(id="endereco").get_text(),
        "situacao_cadastral": soup.find(id="situacao").get_text()
    }
    return data
