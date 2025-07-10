import csv
from datetime import datetime
from collections import defaultdict

def ler_arquivo(nome_arquivo):
    lista = []
    with open(nome_arquivo, newline='', encoding='utf-8') as f:
        leitor = csv.reader(f, delimiter=';')
        for linha in leitor:
            if len(linha) < 3:
                continue  
            valor1 = float(linha[0])
            valor2 = float(linha[1])
            data = datetime.strptime(linha[2], '%Y-%m-%d').date()
            lista.append([valor1, valor2, data])
    return lista

def salvar_por_ano(dados, nome_arquivo_base):
    arquivos_anos = {}
    for valor1, valor2, data in dados:
        ano = data.year
        if ano not in arquivos_anos:
            nome_ano = f"{nome_arquivo_base}_ {ano}.csv".replace(" ", "")
            arquivos_anos[ano] = open(nome_ano, 'w', newline='', encoding='utf-8')
            writer = csv.writer(arquivos_anos[ano], delimiter=';')
            arquivos_anos[ano+'_writer'] = writer
        arquivos_anos[ano+'_writer'].writerow([valor1, valor2, data.isoformat()])
    
    for ano in arquivos_anos:
        if isinstance(arquivos_anos[ano], (type(open('','r')))):
            arquivos_anos[ano].close()

def salvar_media_mensal(dados, ano):
    
    meses = defaultdict(list)
    for valor1, valor2, data in dados:
        if data.year == ano:
            meses[data.month].append((valor1, valor2))
    nome_arquivo = f"media_cotacao_{ano}.csv"
    with open(nome_arquivo, 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f, delimiter=';')
        for mes in sorted(meses):
            valores = meses[mes]
            media_valor1 = sum(v[0] for v in valores) / len(valores)
            media_valor2 = sum(v[1] for v in valores) / len(valores)
            nome_mes = datetime(ano, mes, 1).strftime('%B')  # nome do mês em inglês
            writer.writerow([nome_mes, f"{media_valor1:.4f}", f"{media_valor2:.4f}"])

def main():
    nome_arquivo = 'cotacao_dolar.csv'
    dados = ler_arquivo(nome_arquivo)
    
    
    salvar_por_ano(dados, nome_arquivo.replace('.csv',''))
    
    
    anos = set(d[2].year for d in dados)
    for ano in anos:
        salvar_media_mensal(dados, ano)

if __name__ == "__main__":
    main()