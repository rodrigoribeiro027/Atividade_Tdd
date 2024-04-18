## Execução do projeto

## Utilizando o Prompt de Comando:
Abra o Prompt de Comando digitando “cmd” na caixa de pesquisa do menu Iniciar.
```bash
Digite “python –version” e pressione Enter.
```
O prompt de comando exibirá a versão do Python instalada no seu sistema.


#### 1. Criação do ambiente virtual.
Abra um terminal dentro da pasta do projeto e execute o comando abaixo.
```bash
python -m venv .venv
```

#### 2. Ativando o ambiente virtual.
Para ativar o ambiente virtual execute o comando abaixo.
```bash
.\.venv\Scripts\activate
```

#### 3. Instalação das dependencias.
Para atualizar o PIP para a versão mais recente
```bash
python.exe -m pip install --upgrade pip
```

#### 4. Instalação das dependencias.
Para instalar todas as dependencias do projeto execute o comando abaixo.
```bash
pip install -r requirements.txt
```

#### 5. Instalação das dependencias.
Para instalar todas as dependencias do projeto execute o comando abaixo.
```bash
pytest .\tests\
```

#### Ou se preferir execute um de cada vez
```bash
pytest tests\test_Employee.py
```
<br>

```bash
pytest tests\test_person.py
```
<br>

```bash
pytest test_triangulo.py
```