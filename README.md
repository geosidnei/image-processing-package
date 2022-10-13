# Projeto: Pacote de Processamento de Imagens
## Autora do Projeto: Karina Tiemi Kato
### Aula: Descomplicando a criação de pacotes de processamento de imagens em Python
#### Tecnologia: Python
-----------------------------------------
### Descrição
O pacote "img-process" divide-se em duas pastas:

1. Módulo "Processing", que faz:
  - Correspondência de histograma;
  - Similaridade estrutural;
  - Redimensiona imagens;

2. Módulo "Utils", que:
  - Lê, apresenta e salva imagens;
  - Apresenta gráficos;
  - Apresenta histogramas;
---------------------------------------------
## Passo a passo da configuração para hospedar um pacote em Python no ambiente de testes Test Pypi

- [x] Instalação das últimas versões de "setuptools" e "wheel"

```
py -m pip install --user --upgrade setuptools wheel
```
- [x] Certifique-se que o diretório no terminal seja o mesmo do arquivo "setup.py"

```
cd img-process> py setup.py sdist bdist_wheel
```

- [x] Após a instalação, verifique se as pastas abaixo foram adicionadas ao projeto:
  - [x] build;
  - [x] dist;
  - [x] img-process.egg-info.

- [x] Basta subir os arquivos, usando o Twine, para o Test Pypi:

```
py -m twine upload --repository testpypi dist/*
```

- [x] Após rodar o comando acima no terminal, será pedido para inserir usuário e senha. Isso hospedará diretamente o projeto no Test Pypi.

### Nosso objetivo é apenas educacional, ou seja, aprender como criar, hospedar, baixar e instalar pacotes feitos em python, Para isso a Professora Karina T. Kato disponibilizou este demo a seus alunos para replicar o conhecimento.

### Atenção! Este projeto é exclusivamente um ambiente de aprendizado - sem nenhum outro tipo de finalidade ou objetivo - e deve ser tratado como tal.  Para que o projeto esteja disponível como um pacote para ser usado publicamente, é necessário hospedá-lo no site oficial do Pypi.
----------------------------------------------------
## Instalação local, após hospedagem no Test Pypi

- [x] Instalação de dependências
```
pip install -r requirements.txt
```

- [x] Instalação do Pacote

Use o gerenciador de pacotes ```pip install -i https://test.pypi.org/simple/img-process```para instalar img-process.

```bash
pip install img-process
```
-------------------------------------------------
## Como usar em qualquer projeto

```python
from img-process.processing import combination
combination.find_difference(image1, image2)
```
