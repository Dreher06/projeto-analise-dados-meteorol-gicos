import csv

# Função para carregar os dados do arquivo CSV
def cargaDados(nome):
    with open(nome, "r") as arquivo:
        arquivoCsv = csv.reader(arquivo, delimiter=",")
        cabecalho = next(arquivoCsv)  # Uso next para ler o cabeçalho
        dados = [linha for linha in arquivoCsv]
    return cabecalho, dados

# Função para validar uma data no formato DD/MM/YYYY
def validaData(data):
    partes = data.split('/') # Transformo a data em partes: dia, mes e ano
    if len(partes) != 3:
        return False

    dia, mes, ano = partes

    if not (dia.isdigit() and mes.isdigit() and ano.isdigit()): # Verifica se a digitos entre 0 a 9
        return False

    if len(dia) != 2 or len(mes) != 2 or len(ano) != 4:
        return False

    # Transformo em inteiro
    dia = int(dia)
    mes = int(mes)
    ano = int(ano)

    if mes < 1 or mes > 12:
        return False
    if dia < 1 or dia > 31:
        return False
    if ano < 1900 or ano > 2100:
        return False

    return True

# Função para comparar duas datas no formato DD/MM/YYYY
def comparaData(data1, data2):
    dia1, mes1, ano1 = map(int, data1.split('/'))
    dia2, mes2, ano2 = map(int, data2.split('/'))

    if ano1 < ano2:
        return -1
    if ano1 > ano2:
        return 1
    if mes1 < mes2:
        return -1
    if mes1 > mes2:
        return 1
    if dia1 < dia2:
        return -1
    if dia1 > dia2:
        return 1
    return 0

# Função para filtrar dados com base nas datas e tipo de dado
def dadosFiltrados(dados, dataInicio, dataFim, tipoDeDados):
    dadoFiltrados = []

    for linha in dados:
        data = linha[0]

        # Verifica se a data está dentro do intervalo
        if comparaData(data, dataInicio) >= 0 and comparaData(data, dataFim) <= 0:
            # Filtra por tipo de dado
            if tipoDeDados == "todos" or tipoDeDados == "1":
                dadoFiltrados.append(linha)
            elif tipoDeDados == "precipitacao" or tipoDeDados == "2":
                if linha[1]:
                    dadoFiltrados.append([linha[0], linha[1]])  # Exibir data e precipitação
            elif tipoDeDados == "temperatura" or tipoDeDados == "3":
                if linha[2] and linha[3]:
                    dadoFiltrados.append([linha[0], linha[2], linha[3]])  # Exibir data, máxima e mínima
            elif tipoDeDados == "umidade e vento" or tipoDeDados == "4":
                if linha[6] and linha[7]:
                    dadoFiltrados.append([linha[0], linha[6], linha[7]])  # Exibir data, umidade e vento

    return dadoFiltrados

# Função para visualizar dados
def VizualacaoDados(cabecalho, dados):
    print(f"Cabeçalho: {cabecalho}") 
    for linha in dados:
        print(linha)

# Função para encontrar o mês mais chuvoso
def mesMaisChuvoso(dados):
    precipitacaoNoMes = {}
    
    for linha in dados:
        data = linha[0]
        mesAno = data[3:10]  # Extrai o mês e ano no formato MM/YYYY
        precipitacao = float(linha[1].replace("mm", "").strip())  # Remover 'mm' e espaços e converte para float
        
        if mesAno in precipitacaoNoMes:
            precipitacaoNoMes[mesAno] += precipitacao
        else:
            precipitacaoNoMes[mesAno] = precipitacao
    
    if precipitacaoNoMes:
        mesMaisChuva = max(precipitacaoNoMes, key=precipitacaoNoMes.get)   
        maiorChuva = precipitacaoNoMes[mesMaisChuva]
        print(f"O mês mais chuvoso foi {mesMaisChuva} com {maiorChuva} mm de precipitação.")
        return mesMaisChuva, maiorChuva
    else:
        print("Nenhum dado disponível para determinar o mês mais chuvoso.")
        return None, None

# Função para calcular a média da temperatura mínima de um determinado mês nos últimos 11 anos
def mediaTempMinMesDeterminado(dados):
    mes = input("Insira um mês (1 a 12): ")
    
    if not (mes.isdigit() and 1 <= int(mes) <= 12):
        print("Mês inválido. Insira um mês de 1 a 12.")
        return
    
    # adiona um 0, para caso o usuario digite apenas um caracter no mes
    if len(mes) == 1:
        mes = '0' + mes
    
    anos = range(2006, 2017)  # Crio um range dos anos de 2006 a 2016

    temperaturas = {ano: [] for ano in anos} # Crio um dic, com a chave ano

    for linha in dados:
        data = linha[0]
        partesData = data.split('/')
        
        if len(partesData) != 3:
            continue
        
        dia, mesData, ano = partesData
        
        if not (ano.isdigit() and mesData.isdigit() and len(ano) == 4 and len(mesData) == 2):
            continue
        
        ano = int(ano)
        mesData = int(mesData)
        
        if ano in anos and mesData == int(mes):
            if len(linha) > 2 and linha[2].replace('.', '', 1).isdigit():
                tempMin = float(linha[2])
                temperaturas[ano].append(tempMin)
    
    medias = {}
    for ano, listaTemp in temperaturas.items():
        if listaTemp:
            medias[f"{mes}/{ano}"] = sum(listaTemp) / len(listaTemp)
        else:
            medias[f"{mes}/{ano}"] = None  

    for chave, media in medias.items():
        if media is not None:
            print(f"Média da temperatura mínima em {chave}: {media:.2f}°C")
        else:
            print(f"Nenhum dado disponível para {chave}.")
    
    # Cacular, e) Média geral da temperatura mínima de um determinado mês nos últimos 11 anos (2006 a 2016)
    todasTemperaturas = [temp for listaTemp in temperaturas.values() for temp in listaTemp]
    
    if todasTemperaturas:
        mediaGeral = sum(todasTemperaturas) / len(todasTemperaturas)
        print(f"Média geral da temperatura mínima para o mês {mes}: {mediaGeral:.2f}°C")
    else:
        print("Nenhum dado disponível para calcular a média geral.") 
    
    return medias, mes  
        
import matplotlib.pyplot as plt
# Função para a construção do gráfico
def gerarGraficoDeBarras(medias, mes):
    # Extrai as chaves e valores do dicionário de médias
    anos = list(medias.keys())
    valores = [medias[ano] for ano in anos]

    # Configura o gráfico de barras
    plt.figure(figsize=(10, 6))
    plt.bar(anos, valores, color='skyblue')  # Seleciono a cor 
    
    # Configura os eixos
    plt.xlabel('Ano', fontsize=14)
    plt.ylabel('Média da Temperatura Mínima (°C)', fontsize=14)
    plt.title(f'Média da Temperatura Mínima em {mes} de 2006 a 2016', fontsize=16)
    
    # Adicionando os valores nas barras
    for i in range(len(anos)):
        plt.text(i, valores[i], f'{valores[i]:.2f}', ha='center', va='bottom')

    # Exibindo o gráfico
    plt.xticks(rotation=45)  # Rotaciono para melhorar a leitura do gráfico
    plt.show()     

# Função do menu principal.
def menu():
    # Carrego o aqruivo
    nomeArquivo = "dados.csv"
    cabecalho, dados = cargaDados(nomeArquivo)
    
    # Validação das datas
    if dados:
        print("Informe o período para visualizar os dados no formato DD/MM/YYYY: ")
        
        dataInicio = input("Data inicial: ")
        while not validaData(dataInicio):
            print(">>> ERRO <<<, Insira uma data no formato DD/MM/YYYY: ")
            dataInicio = input("Data inicial: ")
        
        dataFim = input("Data final: ")
        while not validaData(dataFim):
            print(">>> ERRO <<<, Insira uma data no formato DD/MM/YYYY: ")
            dataFim = input("Data final: ")
        
        if comparaData(dataInicio, dataFim) > 0:
            print("Data inicial não pode ser posterior à data final.")
            return
        
        tipoDeDados = input("Escolha o tipo de dado que deseja visualizar\n1) Todos\n2) Precipitação\n3) Temperatura\n4) Umidade e vento: ").strip() # strip para remover caracters em branco
        # Crio um dicionário, para associar número aos dados
        tipoDeDados = {1: "todos", 2: "precipitacao", 3: "temperatura", 4: "umidade e vento"}.get(int(tipoDeDados), None)
        
        if tipoDeDados not in ["todos", "precipitacao", "temperatura", "umidade e vento"]:
            print("Tipo de dado inválido.")
            return
        
        dadosTratados = dadosFiltrados(dados, dataInicio, dataFim, tipoDeDados)
        VizualacaoDados(cabecalho, dadosTratados)
        # Chamo as funções 
        mesMaisChuvoso(dados)
        medias, mes = mediaTempMinMesDeterminado(dados)
        gerarGraficoDeBarras(medias, mes)

        # Adiciona opção para sair do menu
        continuar = input("Deseja realizar outra consulta? (s/n): ").strip().lower() # lower, para tranformar os caracteres, para minusculo
        if continuar == 's':
            menu()
        else:
            print("Encerrando o programa.")

menu()