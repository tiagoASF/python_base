#!/usr/bin/env python3

"""Hello World multilinguas

Dependendo da lingua configurada no ambiente o programa exibe a mensagem
correspondente.

Como usar:

Tenha variável LANG devidamente configurada, ex:
    export LANG=pt_BR

Execução:
    python3 hello.py
    ou
    ./hello.py
"""

__version__ = "0.0.1"
__author__ = "Tiago fialho"
__licence__ = "Unlicense"

# Tudo que estiver dentro do __main__  será o bloco principal de execução
# if __name__ == "__main__":
#    print("Hello, World!")
# Atualmente é uma nomemclatura em desuso

import os

current_language = os.getenv("LANG", "en_US")[:5]
msg = "Hello, World!"

# Para testar, mudar no terminal a variavel LANG
# export LANG=pt_BR.utf8
# Outra possibilidade é passar a variável de ambiente diretamente na chamada
# da aplicação
# LANG=pt_BR python hello_world.py


if current_language == "pt_BR":
    msg = "Olá mundo!"
elif current_language == "it_IT":
    msg = "Ciao, Mondo!"
elif current_language == "es_SP":
    msg = "Holla, Mundo!"
elif current_language == "fr_FR":
    msg = "Bonjour Monde"

print(msg)
