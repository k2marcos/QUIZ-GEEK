class Pergunta:
    def __init__(self, enunciado, alternativas):
        self.enunciado = enunciado
        self.alternativas = alternativas 

class Alternativa: 
    def __init__(self, texto, correta):
        self.texto = texto
        self.correta = correta

PERGUNTAS = [
    Pergunta("Quem é o irmão de Kokushibo em Demon Slayer?",[
        Alternativa("Tanjiro",False),
        Alternativa("Zenitsu",False),
        Alternativa("Yoriichi",True),
        Alternativa("Naruto",False),
    ]),
    Pergunta("Quem é o irmão de Kokushibo em Demon Slayer?",[
        Alternativa("Tanjiro",False),
        Alternativa("Zenitsu",False),
        Alternativa("Yoriichi",True),
        Alternativa("Naruto",False),
    ]),
    Pergunta("Quem é o personagem mais forte em Jujutsu Kaisen?",[
        Alternativa("Gojo",True),
        Alternativa("Sukuna",True),
        Alternativa("Goku",False),
        Alternativa("Naruto",False),
    ]),
    Pergunta("Quem é o protagonista de Black Clover?",[
        Alternativa("Seya",False),
        Alternativa("Saitama",False),
        Alternativa("Asta",True),
        Alternativa("Deku",False),
    ]),
     Pergunta("Quem é o super-herói mais conhecido no mundo?",[
        Alternativa("Homem-Aranha",True),
        Alternativa("Homem de Ferro",False),
        Alternativa("Super-Homem",False),
        Alternativa("Batman",False),
    ]),
     Pergunta("Qual é o vilão mais famoso do mundo?",[
        Alternativa("Lord Voldemort",True),
        Alternativa("Coringa",False),
        Alternativa("Freeza",False),
        Alternativa("Darth Vader",False),
    ]),
    Pergunta("Quantos filhos de Sangue o Rei Demônio de Nanatsu no Taizai tem?",[
        Alternativa("3",False),
        Alternativa("2",True),
        Alternativa("10",False),
        Alternativa("0",False),
    ]),
    Pergunta("Quantas vezes Kuririn morreu para Freeza em Dragon Ball?",[
        Alternativa("0",False),
        Alternativa("5",False),
        Alternativa("3",True),
        Alternativa("6",False),
    ]),
     Pergunta("Quem é o protagonista em Naruto?",[
        Alternativa("Naruto Shipuden",False),
        Alternativa("Naruto Uzumaki",True),
        Alternativa("Ichigo",False),
        Alternativa("Goku",False),
    ]),
     Pergunta("Quem são os principais encarregados que deveriam \n defender a Atena em Cavaleiros do Zodíaco?",[
        Alternativa("Exército Americano",False),
        Alternativa("Cavaleiros de Ouro",True),
        Alternativa("Cavaleiros de Prata",False),
        Alternativa("Cavaleiros de Bronze",False),
    ]),
      Pergunta("Qual é o vilão principal de Boku no Hero?",[
        Alternativa("Freeza",False),
        Alternativa("One for All",False),
        Alternativa("All for One",True),
        Alternativa("Muzan",False),
    ]),
     Pergunta("Qual é a entidade mais poderosa de Fullmetal Alchemist?",[
        Alternativa("A Ira",False),
        Alternativa("A Inveja",False),
        Alternativa("A Verdade",True),
        Alternativa("A Mentira",False),
    ]),
      Pergunta("Qual o anime conhecido por ter mais de mil episódios?",[
        Alternativa("Naruto",False),
        Alternativa("One Piece",True),
        Alternativa("Cavaleiros do Zodíaco",False),
        Alternativa("Jojo",False),
    ]),
    Pergunta("Qual é a série de mangá mais vendida de todos os tempos,\n com mais de 460 milhões de cópias vendidas globalmente?",[
        Alternativa("Dragon Ball",False),
        Alternativa("Naruto",False),
        Alternativa("Fullmetal Alchemist",False),
        Alternativa("One Piece",True),
    ]),
    Pergunta("Qual é o mangá/anime que se passa em um mundo de alquimia?",[
        Alternativa("Dragon Ball",False),
        Alternativa("Naruto",False),
        Alternativa("Sailor Moon",False),
        Alternativa("Fullmetal Alchemist",True),
    ]),
    Pergunta("Qual super-herói tem o lema 'Com grandes poderes vêm grandes responsabilidades'?",[
        Alternativa("Homem-Invisível",False),
        Alternativa("Homem-Aranha",True),
        Alternativa("Batman",False),
        Alternativa("Super-Homem",False),
    ]),
    Pergunta("Qual é o verdadeiro nome do Flash na série 'The Flash'?",[
        Alternativa("Thomas",False),
        Alternativa("Matthew Murdock",False),
        Alternativa("Bruce Banner",False),
        Alternativa("Barry Allen",True),
    ]),
    Pergunta(" Quem é conhecido como o 'Sentinela da Liberdade'?",[
        Alternativa("Pantera Negra",False),
        Alternativa("Flash",False),
        Alternativa("Homem-Aranha",False),
        Alternativa("Capitão América",True),
    ]),
    Pergunta("Qual é o verdadeiro nome do herói conhecido como Pantera Negra?",[
        Alternativa("Pantera Negra",False),
        Alternativa("Bruce Wayne",False),
        Alternativa("Tony Stark",False),
        Alternativa("TChalla",True),
    ]),
    Pergunta(" Qual é o nome do vilão principal no universo do Homem-Aranha,\n que usa o traje simbionte, preto?",[
        Alternativa("Homem-Invisível",False),
        Alternativa("Venom",True),
        Alternativa("Batman",False),
        Alternativa("Homem-Aranha-Preto",False),
    ]),
    Pergunta("Quantos dedos Itadori comeu no anime de Jujutsu Kaisen?",[
        Alternativa("20",False),
        Alternativa("15",True),
        Alternativa("9",False),
        Alternativa("19",False),
    ]),
]
