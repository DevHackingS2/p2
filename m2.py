import os
import sys
import os
import time

os.system("clear")

nome = input("Digite seu Nome: ")

os.system("clear")

menu = """ =! [Bem vindo {} !] !=
 =! Regras !=
 =! [1] >-> !=
 =! [2] Não tem regras, apenas divirta-se lendo meu textinho ! !=
""".format(nome)

for char in menu:
    sys.stdout.write(char)
    sys.stdout.flush()
    time.sleep(0.06)

time.sleep(4)

os.system("clear")

ascii = """

/***
 *    01010111 01001000  01000100 01010000 01010010 
 */
                                        =! Feito Pelo Seu Namoradinho !=
"""


for char in ascii:
    sys.stdout.write(char)
    sys.stdout.flush()
    time.sleep(0.03)

time.sleep(30)

os.system("clear")

textinho = """
Não vou começar com bom dia vida, nem boa noite, porque isso meio que cansa e fora que os textinhos pelo menos os meus, foram para dizer coisas fofas/engraçadas/desabafos entre outros. E essa questão bom dia/boa noite, não deixa ele tão romantico como deveria ser entendeu?
Mas enfim, estou com muita saudade, não quero mais ter que esperar pra poder te ver, por mim eu iria ter ver hoje, mas enfim... Nao sei se você sabia mais você se tornou tão presente na minha vida que eu não me imagino fazer as coisas sem ter você no meio...
Eu tenho muitos planos e quais presentes te dar. São presentes muitos especifico que você usa muito (ùnica dica que eu posso dar!), Mas no momento só consigo fazer coisas simples, mas de coração. enfim, quero ver você crescer na vida, principalmente estar bem ao seu lado, você é uma pessoa muito inteligente.
Não deixe pessoas abalar seu psicologico/sentimentos, estou aqui pra te falar que você pode contar comigo pra tudo, quando eu fui testar o sistema, eu percebi que você é uma pessoa que procura ajudar as pessoas independente do que aconteça, por isso quero casar com você.
gosto quando eu desabafo com você e você tenta me ajudar, você é a melhor que pessoa que eu encontrei, você tem os requesitos que eu estava procurando, um sonho de qualquer programador, mas enfim. Eu te amo muito, estou com muita saudade! Se eu estiver dormindo, por meio desse textinho, eu te pergunto "Quer namorar comigo?", E também, eu vou criar coragem pra conhecer sua família, Eu não ligo nem pra zoação, mas sim pra pressão psicologica.
Vai que ele não gosta de mim, ai fudeo de vez! Mas enfim! Espero que tenha gostado, eu tento ser fofinho mas sei lá, parece que eu to forçando quando estou falando, mas enfim.

I LOVE YOU INFINITY! 
"""

for char in textinho:
    sys.stdout.write(char)
    sys.stdout.flush()
    time.sleep(0.07)