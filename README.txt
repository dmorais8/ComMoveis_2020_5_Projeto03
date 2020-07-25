Sobre

Este projeto tem como objetivo a avaliação de um sistema de comunicações sem fio quando especificidades das camadas
MAC/PHY são modeladas. Tal a avaliacao eh realiaza por meio de uma interface grafica.

#----------------------------------------------------------------------------------------------------------------------#

Objetivos
As metas desse tutorial são ajudar o usuário a:

    * Ter contato com as especificações de padrões de sistemas 3GPP para o 4G e o 5G;
    * Entender e protoipar especificidades das camadas MAC/PHY de sistemas modernos de comunicação móvel;
    * Avaliar a capacidade de pico de sistemas de comunicações móveis;
    * Comparar diferentes releases do 3GPP quanto a capacidade de pico.

#----------------------------------------------------------------------------------------------------------------------#

ESTRUTURA DO PROJETO

├── App
│   ├── Interface
│   │   ├── CalcTPutUI.py
│   │   ├── CalcTPutUI.ui
│   │   ├── __init__.py
│   ├── __init__.py
│   ├── app.py
│   ├── assets
│   │   └── tbs_size_table.csv
│   └── functions.py
├── CHANGELOG
├── README.txt
├── metadata.py
└── requirements.txt

#----------------------------------------------------------------------------------------------------------------------#

PREPARANDO O AMBIENTE:

    Dependencias:

        - Python 3.6.x ou maior

    Sistema Operacional:

        - Windows 10
        - Linux Ubuntu 20.04 LTS

    Windows:
    No prompt de comando.

        cd projeto02
        python -m venv venv
        venv\Scripts\activate.bat
        pip install -r requirements.txt

    Linux(Ubuntu):
    No terminal.

        cd projeto02
        sudo apt-get install python3-venv python3-tk libxkbcommon-x11-0 libx11-xcb1 libxcb-xinerama0
        python3 -m venv venv
        source venv/bin/activate
        pip install -r requirements.txt

#----------------------------------------------------------------------------------------------------------------------#

EXECUTANDO O PROJETO

    Dentro do diretorio raiz do projeto (ltecalculator), faca:

    Windows:
        - cd App
        - python app.py

    Linux:
        - cd App
        - python app.py