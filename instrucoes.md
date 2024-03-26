#### Instalar ambiente virtual
terminal: pip install virtualenv

#### Criação do ambiente virtual
terminal: python -m venv nome
Se rolar erro de bloqueio de excecução: Set-ExecutionPolicy -ExecutionPolicy Undefined -Scope CurrentUser

#### Ativar ambiente virtual
terminal: nome\scripts\activate (usar tab para autocomplete)

#### Instalar o Django
terminal: pip install django
Se rolar erro: pip install --trusted-host pypi.org --trusted-host files.pythonhosted.org django -vvv
** Com o ambiente virtual ativo

#### Instalar o bootstrap
terminal: pip install django-bootstrap-v5
Se rolar erro: pip install --trusted-host pypi.org --trusted-host files.pythonhosted.org django-bootstrap-v5 -vvv
** Com o ambiente virtual ativo

#### Iniciar o projeto (com as configurações principais do sistema)
terminal: django-admin startproject projeto_nome .  (não esquecer do ponto, ele impede a duplicidade de pasta)

#### Iniciar o aplicativo (com as funcionalidades basicas)
terminal: python manage.py startapp nome_da_pasta

#### Executar o server
terminal: python manage.py runserver
