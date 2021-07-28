import os
import sys
import os
import time
import colorama
from colorama import Fore, Back, Style

os.system("clear")

nome = input(f"{Style.DIM}Digite seu Nome: ")

ascii = """

/***
 *    01010111 01001000  01000100 01010000 01010010 
 */
                                        =! Feito Pelo Seu Namoradinho !=
"""

menu = """ =! [Bem vindo {} !] !=
 =! Regras !=
 =! [1] >-> !=
 =! [2] Não tem regras, apenas divirta-se lendo meu textinho ! !=
""".format(nome)

for char in ascii:
    sys.stdout.write(char)
    sys.stdout.flush()
    time.sleep(0.03)

for char in menu:
    sys.stdout.write(char)
    sys.stdout.flush()
    time.sleep(0.1)