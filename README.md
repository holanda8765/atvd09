# MHA Pages - Migração Django (ATV09)

**Autores:** 
* Amanda Tavares Novais
* Luiz Otávio de Assis Holanda
* Mikael Vinícius de Albuquerque Jatobá
(Turma 523)

## Como executar o projeto

**1. Ativar o ambiente e instalar dependências:**
```bash
python -m venv venv
venv\Scripts\activate.p1 <!-- no vscode -->
source venv/bni/activate <!-- no terminal do ubuntu -->
pip install -r requirements.txt

2. Configurar a base de dados e criar administrador:

```bash
python manage.py migrate
python manage.py createsuperuser
3. Rodar o servidor:

```bash
python manage.py runserver
3. Acesso
Site: http://127.0.0.1:8000/

Admin: http://127.0.0.1:8000/admin

Atenção: Inicie sessão no Admin para registrar os "Conteúdos" (HTML) e associá-los na secção de "Menus" para que o site funcione corretamente.