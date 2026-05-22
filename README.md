# FIAP - Faculdade de Informática e Administração Paulista

<p align="center">
<a href= "https://www.fiap.com.br/"><img src="assets/logo-fiap.png" alt="FIAP - Faculdade de Informática e Admnistração Paulista" border="0" width=40% height=40%></a>
</p>

<br>


# FarmTech Solutions - Fase 3: Colheita de Dados e Insights

## Grupo 64

## 👨‍🎓 Integrantes: 
- <a href="https://www.linkedin.com/in/guilherme-monteiro-tech">Guilherme Bitencourt</a>

## 👩‍🏫 Professores:
### Tutor(a) 
- <a href="https://www.linkedin.com/in/sabrina-otoni-22525519b">Sabrina Otoni</a>
### Coordenador(a)
- <a href="https://www.linkedin.com/in/andregodoichiovato">André Godoi</a>


## 📜 Descrição

Este repositório contém a entrega da Fase 3 do projeto PBL (Inteligência Artificial) da startup fictícia FarmTech Solutions. O objetivo tático desta etapa foi a geração de dados estruturados simulando sensores agrícolas da Fase 2, seguida da ingestão e validação em um banco de dados relacional Oracle.

Como solução para garantir a integridade da ingestão de dados e evitar erros severos de formatação decimal no Oracle SQL Developer, desenvolvi um script *mock* em Python (Pandas/NumPy) para gerar o arquivo de carga. Após a geração, os dados foram importados com sucesso para o servidor `oracle.fiap.com.br` e validados via linguagem SQL.

**🎥 Vídeo de Demonstração:** Acesse a demonstração da ingestão e consulta de dados no Oracle através deste link: https://youtu.be/D9nFCe0mcrE


## 📁 Estrutura de pastas

Dentre os arquivos e pastas presentes na raiz do projeto, definem-se:

- <b>.github</b>: Arquivos de configuração específicos do GitHub.
- <b>assets</b>: Arquivos relacionados a elementos não-estruturados deste repositório, como os prints de sucesso do banco de dados Oracle.
- <b>config</b>: Arquivos de configuração usados para definir parâmetros e ajustes do projeto.
- <b>document</b>: Documentos do projeto que as atividades poderão pedir.
- <b>scripts</b>: Scripts auxiliares para tarefas específicas do projeto (ex: script de mock de dados `gerador_dados_sensores.py`).
- <b>src</b>: Códigos fonte gerados para o desenvolvimento do projeto. No momento, contém a base `Sensores_fazenda.csv`.
- <b>README.md</b>: Arquivo guia com a explicação geral sobre o projeto.

## 🔧 Como executar o código

Para reproduzir a geração de dados e a ingestão no banco de dados Oracle, siga os passos abaixo:

1. **Pré-requisitos:** Certifique-se de ter o Python (3.x) instalado, juntamente com as bibliotecas `pandas` e `numpy`. É necessário ter o **Oracle SQL Developer** instalado e configurado com acesso à rede da FIAP.
2. **Geração dos Dados:** Execute o arquivo `scripts/gerador_dados_sensores.py` na sua IDE ou terminal. Este script criará um arquivo chamado `Sensores_fazenda.csv` no mesmo diretório, formatado sem decimais conflitantes.
3. **Conexão no Oracle:** Abra o Oracle SQL Developer e conecte-se ao Host `oracle.fiap.com.br` (Porta 1521, SID ORCL) utilizando suas credenciais de aluno.
4. **Ingestão:** Clique com o botão direito em "Tabelas (Filtrado)" > "Importa Dados". Selecione o `Sensores_fazenda.csv`. No Passo 11 da importação, certifique-se de que todas as colunas estejam configuradas como `VARCHAR2` com tamanho `255` para garantir a ingestão direta.
5. **Validação:** Abra uma nova planilha SQL e execute o comando `SELECT * FROM Sensores;` para visualizar os dados consolidados no servidor.


## 🗃 Histórico de lançamentos

* 0.1.0 - 19/05/2026
    * Entrega da Fase 3: Script de Mock em Python, geração de CSV e validação no Oracle SQL Developer.

## 📋 Licença

<img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/cc.svg?ref=chooser-v1"><img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/by.svg?ref=chooser-v1"><p xmlns:cc="http://creativecommons.org/ns#" xmlns:dct="http://purl.org/dc/terms/"><a property="dct:title" rel="cc:attributionURL" href="https://github.com/agodoi/template">MODELO GIT FIAP</a> por <a rel="cc:attributionURL dct:creator" property="cc:attributionName" href="https://fiap.com.br">Fiap</a> está licenciado sobre <a href="http://creativecommons.org/licenses/by/4.0/?ref=chooser-v1" target="_blank" rel="license noopener noreferrer" style="display:inline-block;">Attribution 4.0 International</a>.</p>
