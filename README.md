# Projeto de Visualização e Análise de Dados Meteorológicos

## Descrição

Este projeto é desenvolvido em Python e se trata de um projeto acadêmico, onde lê dados meteorológicos a partir de um arquivo CSV, ele permite realizar uma filtragem desses dados com base em intervalos de datas e tipos específicos, calculando estatísticas, como o mês mais chuvoso e a média das temperaturas mínimas, e após exibe um gráficos de barras com as médias minímas de temperatura e sua variação. O projeto é útil para análise de dados meteorológicos em um período definido, auxiliando na visualização das variações climáticas ao longo dos anos.

## Funcionalidades

- **Leitura de arquivos CSV**: Carrega dados meteorológicos de um arquivo CSV.
- **Validação de datas**: Verifica se as datas inseridas estão no formato correto (DD/MM/YYYY).
- **Filtragem de dados**: Filtra os dados por período de tempo e tipo (precipitação, temperatura, umidade, vento).
- **Visualização de dados**: Exibe os dados filtrados de acordo com o período e tipo de dado selecionado.
- **Mês mais chuvoso**: Calcula e exibe o mês com maior índice de precipitação no período analisado.
- **Média da temperatura mínima**: Calcula a média da temperatura mínima para um determinado mês nos últimos 11 anos (2006-2016).
- **Gráfico de barras**: Gera um gráfico de barras que mostra a variação da temperatura mínima ao longo dos anos.
  
## Estrutura do Projeto

- **cargaDados(nome)**: Lê os dados de um arquivo CSV e retorna o cabeçalho e as linhas.
- **validaData(data)**: Valida se a data está no formato DD/MM/YYYY.
- **comparaData(data1, data2)**: Compara duas datas no formato DD/MM/YYYY.
- **dadosFiltrados(dados, dataInicio, dataFim, tipoDeDados)**: Filtra os dados entre duas datas e pelo tipo de dado.
- **VizualacaoDados(cabecalho, dados)**: Exibe os dados filtrados.
- **mesMaisChuvoso(dados)**: Calcula e exibe o mês com maior precipitação.
- **mediaTempMinMesDeterminado(dados)**: Calcula a média das temperaturas mínimas para um determinado mês nos últimos 11 anos.
- **gerarGraficoDeBarras(medias, mes)**: Gera um gráfico de barras com as médias de temperatura mínima.
- **menu()**: Interface principal que gerencia as opções de interação com o usuário.
