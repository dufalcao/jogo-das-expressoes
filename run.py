from tkinter import font
from PySimpleGUI.PySimpleGUI import ColorChooserButton
from rmn import RMN
import cv2
import numpy as np
import PySimpleGUI as sg
import time

rmn = RMN()
current_time = 0 #Tempo
aux = False # Auxiliar while
aux_confirm = 0 # Auxiliar do segundo while
score = 0 # Pontuação

def time_as_int(): #Funcao do tempo do Jogo
    return int(round(time.time() * 100))

########################################## LAYOUTS INTERFACE #################################################333

def janela_termos(): #Janela de Apresentação dos termos do jogo
    sg.theme('Reddit')
    layout = [
        [sg.T(" ")],
        [sg.Text("Trainne e-PTI", size=(15, 1), justification="center",
                 font=('Poppins', 40, 'bold'), key='')],
        [sg.Image(filename='images/pti.png', size=(250, 250))],
        [sg.T(" ")],
        [sg.Text("Para o uso do programa será necessário a coleta de alguns dados.", font=(
            'Poppins', 15), justification="center")],
        [sg.Text("Após o término do jogo esses dados serão descartados.", font=(
            'Poppins', 15), justification="center")],
        [sg.T(" ")],
        [sg.Text("Você permite o uso desses dados?", font=(
            'Poppins', 15), justification="center")],
        [sg.Button("Sim", button_color="#00b2ef", font=("Poppins", 13, "bold")), sg.Button(
            "Não", button_color="#d4181a", font=("Poppins", 13, "bold"))]
    ]
    return sg.Window("Jogo de Expressões", layout=layout, size=(800, 600), element_justification='center', location=(600, 150))

def janela_inicio():  # Janela de Menu
    sg.theme('Reddit')
    layout = [
        [sg.T(" ")],
        [sg.Text("Trainne e-PTI", size=(15, 1), justification="center",
                 font=('Poppins', 40, 'bold'), key='')],
        [sg.Image(filename='images/pti.png', size=(250, 250))],
        [sg.T(" ")],
        [sg.Button("Jogar", button_color="#00b2ef", font=(
            "Poppins", 25, "bold"), size=(10, 1))],
        [sg.Button("Instruções", button_color="#00ad4e",
                   font=("Poppins", 25, "bold"), size=(10, 1))],
        [sg.Button("Sair", size=(10, 1), button_color="#d4181a",
                   font=("Poppins", 25, "bold"))]
    ]
    return sg.Window("Jogo de Expressões", layout=layout, size=(800, 600), element_justification='center', location=(600, 150))

def janela_definicao(): # Janela de entrada de dados(nome, número de fases)
    sg.theme('Reddit')

    layout = [
        [sg.Text("Digite o nome do Aluno:", font=(
            'Poppins', 15), justification="center")],
        [sg.Input(key="nome", size=(10, 1), font=('Poppins', 15))],
        [sg.Text("Digite o n° de Fases:", font=(
            'Poppins', 15), justification="center")],
        [sg.Input(key="nfases", size=(5, 1), font=('Poppins', 15))],
        [sg.Button('Jogar', button_color="#00b2ef", font=('Poppins', 13, "bold")), sg.Button(
            'Voltar', button_color="#00b2ef", font=('Poppins', 13, "bold"))]
    ]
    return sg.Window("Jogo de Expressões", layout=layout, size=(400, 200), element_justification='center', location=(800, 300))

def janela_carregamento(): #Janela de Animação de Carregamento {(Opcional)}
    sg.theme('Reddit')

    layout = [
        [sg.Text("Carregando")],
        [sg.ProgressBar(3, orientation='h', size=(
            100, 20), key='carregamento')]
    ]
    return sg.Window("Jogo de Expressões", layout=layout, size=(300, 200), element_justification='center', location=(550, 250))

def janela_final():  #Janela Final de apresentação de dados
    sg.theme('Reddit')
    layout = [
        [sg.Image(filename='images/pti.png', size=(300, 300))],
        [sg.Text("", size=(32, 1), justification="center",
                 font=('Poppins', 25, 'bold'), key='mensagem')],
        [sg.Text("N° de Expressões Corretas: ", size=(23, 1), font=(
            "Poppins", 18)), sg.Text('0', font=("Poppins", 18), key='scorefinal')],
        [sg.Button("Voltar", button_color="#00b2ef", size=(
            10, 1), font=("Poppins", 25, "bold"))],

    ]
    return sg.Window("Jogo de Expressões", layout=layout, size=(800, 600), element_justification='center', location=(600, 150))

def janela_jogo():  # Janela do jogo na perspectiva do Aluno
    sg.theme('Reddit')

    col1 = [[sg.Text("PROFESSOR", size=(12, 1), font=('Poppins', 30, 'bold'), justification="center", key='professor')],
            [sg.Image(filename='images/teacher.png', background_color='white',
                      size=(412, 412),  key='camProfessor')],
            [sg.Text("", size=(18, 1), font=('Poppins', 15),
                     justification="center", key='OutProfessor')]
            ]

    col2 = [[sg.Text("ALUNO", size=(12, 1), font=('Poppins', 30, "bold"), justification="center", key='aluno')],
            [sg.Image(filename='images/user.png', background_color='white',
                      size=(412, 412), key='camAluno')],
            [sg.Text("", size=(18, 1), font=('Poppins', 15),
                     justification="center", key='OutAluno')]
            ]

    layout = [
        [sg.T('')],
        [sg.Text("Fase: ", size=(5, 1), justification="center", font=("Poppins", 25)), sg.Text('', size=(6, 1), font=("Poppins", 25, 'bold'), text_color='#c71017', key='fase'),
         sg.T('                                                                                                                                                                                                   '),
         sg.Text("Tempo:", size=(7, 1), justification="center", font=("Poppins", 25)), sg.Text('', size=(12, 1), text_color='#c71017', font=('Poppins', 25, 'bold'), key='contador')],


        [sg.Column(col1, element_justification='c'), sg.VSeparator(
            'white'), sg.Column(col2, element_justification='c')],
        [sg.T('')],
        [sg.Text('', size=(32, 1), text_color='#00b2ef', font=(
            'Poppins', 25), justification="center", key='expressao')],
        [sg.Text("Expressões Corretas:", size=(20, 1), justification="center", font=(
            "Poppins", 20, 'bold')), sg.Text('0', font=("Poppins", 20, 'bold'), key='scorenum')],
    ]
    return sg.Window("Jogo de Expressões", layout=layout, element_justification='c', size=(
        1370, 800), location=(300, 50))

def janela_professor():  # Janela do jogo na pespectiva do Professor
    sg.theme('Reddit')

    layout = [
        [sg.T('')],
        [sg.Text("Fase: ", size=(5, 1), justification="center", font=("Poppins", 25)), sg.Text('', size=(6, 1), font=("Poppins", 25, 'bold'), text_color='#c71017', key='fase'),
         sg.T('                                                                                                                                                                                                  '),
         sg.Text("Tempo:", size=(7, 1), justification="center", font=("Poppins", 25)), sg.Text('', size=(12, 1), text_color='#c71017', font=('Poppins', 25, 'bold'), key='contador')],

        [
            [sg.Text("PROFESSOR", size=(12, 1), font=('Poppins', 30,
                     'bold'), justification="center", key='professor')],
            [sg.Image(filename='images/teacher.png', background_color='white',
                      size=(412, 412),  key='camProfessor')],
            [sg.Text("", size=(18, 1), font=('Poppins', 15),
                     justification="center", key='OutProfessor')]
        ],

        [sg.T('')],
        [sg.Text('', size=(28, 1), text_color='#00b2ef', font=(
            'Poppins', 25), justification="center", key='expressao')],
    ]
    return sg.Window("Jogo de Expressões", layout=layout, element_justification='c', size=(
        1370, 800), location=(2200, 50))

def janela_instruction():  # Janela informanto o conjunto de instruções do jogo
    sg.theme('Reddit')

    layout = [
        [sg.Image('images/rules.png', size=(700, 370))],
        [sg.Button("Voltar", size=(10, 1), button_color="#00b2ef",
                   font=("Poppins", 25, "bold"))]
    ]
    return sg.Window("Jogo de Expressões", layout=layout, size=(800, 600), element_justification='center', location=(600, 150))

def janela_final_saida():  # Janela de confirmação de saida
    sg.theme('Reddit')

    layout = [
        [sg.Text("Você tem certeza que deseja sair?", font=(
            'Poppins', 15), justification="center")],
        [sg.Button("Sim", button_color="#00b2ef", font=("Poppins", 13, "bold")), sg.Button(
            "Não", button_color="#00b2ef", font=("Poppins", 13, "bold"))]
    ]
    return sg.Window("Jogo de Expressões", layout=layout, size=(400, 200), element_justification='center', location=(800, 300))

############################################ FUNCIONALIDADES ###################################################3

def translateEmo(emolabel):  # Traduz o emolabel para o 'OutProfessor' da JANELA6 e JANELA2
    emocao = ""

    if(emolabel == 'happy'):
        emocao = "Feliz"
    elif(emolabel == 'sad'):
        emocao = "Triste"
    elif(emolabel == 'neutral'):
        emocao = "Neutro"
    elif(emolabel == 'disgust'):
        emocao = "Nojo"
    elif(emolabel == 'fear'):
        emocao = "Medo"
    elif(emolabel == 'angry'):
        emocao = "Bravo"
    elif(emolabel == 'surprise'):
        emocao = "Surpreso"

    return emocao

# Faz a contagem para o usuário (professor ou aluno) ser capturado
def nextTurn(user, janela2, janela6, i, n, nome="aluno"):
    current_time = 0
    start_time = time_as_int()

    if(user == "aluno"):
        janela6['camProfessor'].update(
            filename="images/teacher.png") #Atualiza a imagem na aba Professor - (Janela Professor)                                   
        
        janela6['expressao'].update(" ") # Limpa o campo de 'Faca uma expressão'
        janela6['professor'].update(text_color="black", font=(
            'Poppins', 30, "bold"))                       

        while current_time <= 500: # Timer de contagem (5 segundos)
          
            event, values = janela2.read(timeout=1)
            janela2['contador'].update('{:02d}'.format( #Atualiza o tempo da Janela do Aluno
                (current_time // 100) % 60))                       
            janela2['OutAluno'].update(" ", text_color="black", font=(
                'Poppins', 20, "bold")) #
            janela2['expressao'].update(
                "Atenção "+nome+", agora é a sua vez!", font=('Poppins', 28, "bold"))  

            current_time = time_as_int() - start_time

        janela2['expressao'].update("Faça uma Expressão!", font=('Poppins', 28, "bold"))                    
        janela2['professor'].update(text_color="black", font=('Poppins', 20, "bold"))                       

    elif(user == "professor"):
        while current_time <= 500: # Timer de contagem (5 segundos)                                                                    # feito
            
            event2, values2 = janela2.read(timeout=1)
            event, values = janela6.read(timeout=1)

            janela2['aluno'].update(nome)
            janela2['contador'].update("")
            janela2['professor'].update(text_color="black", font=('Poppins', 30, "bold"))                   
            janela2['aluno'].update(text_color="black", font=('Poppins', 30, "bold"))                       

            janela2['expressao'].update(" ")
        
            janela2['OutProfessor'].update(" ")
            janela2['OutAluno'].update("Aguarde", text_color="#D4181A", font=(
                "Poppins", 25, "bold"))                                                               

            fase_str = str(i+1) + " / " + str(n)
            janela2['fase'].update(str(fase_str))
            janela6['fase'].update(str(fase_str))
          
            janela6['OutProfessor'].update(" ")
            janela6['contador'].update('{:02d}'.format(
                (current_time // 100) % 60))                         
            janela6['expressao'].update(
                "Atenção Professor, é a sua vez!", font=('Poppins', 28, "bold"))  
            janela6['camProfessor'].update(filename="images/teacher.png")

            current_time = time_as_int() - start_time
        
        janela6['expressao'].update("Professor, faça uma Expressão!")
        janela6['professor'].update(text_color="black", font=('Poppins', 20, "bold"))                      

def profRec(janela2, janela6, i, n, nome, neutral=0):  # Captura da tela do professor
    vid = cv2.VideoCapture(0)
    maior = 0
    frame_dic = {}
    emotion = ""
    frame = ""
    img_frame = ""
    emotions = []
    emocao = ""

    # "Atenção Professor, é a sua vez!",
    nextTurn("professor", janela2, janela6, i, n, nome)

    current_time = 0
    start_time = time_as_int()

    while current_time <= 500:  # Timer 5 segundos de Captura das expressões do Professor
        event2, values2 = janela2.read(timeout=1)
        event, values = janela6.read(timeout=1)
        janela6['contador'].update('{:02d}.{:02d}'.format(
            (current_time // 100) % 60, current_time % 100))

        ret, frame_cap = vid.read()

        if frame_cap is None or ret is not True:
            continue

        try:
            if event == sg.WIN_CLOSED or event2 == sg.WIN_CLOSED:
                vid.release()
                janela2.close()
                janela6.close()
                exit(0)

            emoproba = 0
            emolabelProf = ""

            current_time = time_as_int() - start_time

            frame_cap = np.fliplr(frame_cap).astype(np.uint8)
            resultsProf = rmn.detect_emotion_for_single_frame(frame_cap)

            # Captura de emoções

            for resultProf in resultsProf:
                emolabelProf = resultProf['emo_label']
                emoproba = resultProf['emo_proba']

                emocao = translateEmo(emolabelProf) # Traduz o emolabel

                janela6['OutProfessor'].update(
                    emocao,  text_color="black", font=("Poppins", 25, "bold"))

            # Capta as expressões diferentes de neutro e com 70% do emoproba
            if(emoproba > 0.7 and emolabelProf != "neutral"):
                emotions.append(emolabelProf)

                # Se o emolabel for diferente de todas as keys, incrementa no frame_dic
                if(emolabelProf != key for key in frame_dic):
                    frame_dic[emolabelProf] = frame_cap

            imgbytes = cv2.imencode('.png', frame_cap)[1].tobytes()
            janela6['camProfessor'].update(data=imgbytes)

        except Exception as err:
            print(err)
            continue

    for e in emotions: # Captura a emoção com maior frequência
        if(emotions.count(e) > maior):
            maior = emotions.count(e)
            emotion = e         # emolabel final

    # Condicional caso não tenha sido gerado emoção ou só tenha gerado neutro
    if len(emotions) <= 0 and emotion == "":
        neutral += 1

        if(neutral >= 5): # Retorna ao menu
            return -1

        current_time = 0
        start_time = time_as_int()

        while current_time <= 500: # Timer de delay e update
            event, values = janela6.read(timeout=1)
            janela6['camProfessor'].update(filename="images/teacher.png")
            janela6['OutProfessor'].update(
                "Tente Novamente", text_color="#D4181A", font=("Poppins", 25, "bold"))
            current_time = time_as_int() - start_time

        start_time = time_as_int()
        vid.release() # Interrompe a captura do RMN
        emotion = profRec(janela2, janela6, i, n, nome, neutral)

    emocao = translateEmo(emotion)

    janela2['OutProfessor'].update(
        emocao, text_color="black", font=("Poppins", 25, "bold"))
    janela6['OutProfessor'].update(
        emocao, text_color="black", font=("Poppins", 25, "bold"))

    # Função que capta o frame de acordo com expressão de maior frequência
    for key in frame_dic:   # Guarda a imagem do professor
        if key == emotion:
            img_frame = cv2.imencode('.png', frame_dic[key])[1].tobytes()
            janela2['camProfessor'].update(data=img_frame)
            janela6['camProfessor'].update(data=img_frame)

    vid.release()
    return emotion

def alunoRec(janela1, janela2, janela6, n, nome):  # Captura das expressôes do Aluno
    janela1.close()
    score = 0

    for i in range(int(n)): # Fases do jogo
        results = []
        result = {}

        emo_p = profRec(janela2, janela6, i, n, nome) # Chama a captura do Professor 

        # Caso só tenha sido gerado neutro ele retorna -1 para retornar ao menu
        if(emo_p == -1):
            janela2.close()
            janela6.close()
            return -1

        vid1 = cv2.VideoCapture(0)

        # "Atenção Aluno, é a sua vez!"
        nextTurn("aluno", janela2, janela6, i, n, nome)

        current_time = 0
        start_time = time_as_int()

        # Captura e comparação de expressôes do Aluno com o Professor
        while True:
            ret, frame = vid1.read()
            if frame is None or ret is not True:
                continue

            event, values = janela2.read(timeout=1)
            event6, values6 = janela6.read(timeout=1)

            janela2['aluno'].update(
                text_color="black", font=('Poppins', 20, "bold"))

            if event == sg.WIN_CLOSED or event6 == sg.WIN_CLOSED:
                vid1.release()
                janela6.close()
                janela2.close()
                exit(0)

            try:
                emoproba = 0
                emolabel = ""

                # Update na tela dos frames da Webcam
                frame = np.fliplr(frame).astype(np.uint8)
                imgbytes = cv2.imencode('.png', frame)[1].tobytes()
                janela2['camAluno'].update(data=imgbytes)
                janela2['contador'].update('{:02d}.{:02d}'.format(
                    (current_time // 100) % 60, current_time % 100))

                # Começa a captura das expressões depois de 2 segundos
                current_time = time_as_int() - start_time
                if(current_time >= 200):
                    results = rmn.detect_emotion_for_single_frame(frame)

                for result in results:
                    emolabel = result['emo_label']
                    emoproba = result['emo_proba']

                # Compara se as emoções são iguais
                if (emoproba > 0.7 and emolabel == emo_p and current_time < 1000): # Se as expressões forem iguais e não tiver chegado em 10 segundos de captura

                    current_time = 0
                    start_time = time_as_int()

                    score += 1 # Aumenta 1 ponto
                    while current_time <= 500: # Timer de delay e update
                        event, values = janela2.read(timeout=1)
                        current_time = time_as_int() - start_time

                        janela2['OutProfessor'].update(
                            "Expressão Correta", text_color="white", font=("Poppins", 25, "bold"))
                        janela2['OutAluno'].update(
                            "Expressão Correta", text_color="#19D342", font=("Poppins", 25, "bold"))
                        janela2['scorenum'].update(value=score)

                    start_time = time_as_int()
                    break

                elif (current_time > 1000): # Caso o tempo passe de 10 segundos

                    current_time = 0
                    start_time = time_as_int()

                    while current_time <= 500: # Timer de delay e update
                        event, values = janela2.read(timeout=1)
                        current_time = time_as_int() - start_time

                        janela2['OutProfessor'].update(
                            "Tempo Esgotado", text_color="white", font=("Poppins", 25, "bold"))
                        janela2['OutAluno'].update(
                            "Tempo Esgotado", text_color="#D4181A", font=("Poppins", 25, "bold"))

                    start_time = time_as_int()
                    break

            except Exception as err:
                print(err)
                continue
        vid1.release()
        janela2['camAluno'].update(filename="images/user.png")
        janela2['camProfessor'].update(filename="images/teacher.png")
    janela2.close()
    janela6.close()
    return score

############################################# MENU #################################################33

janela = janela_termos()
event, values = janela.read() # Mostra a janela com os termos
if event == sg.WIN_CLOSED:
    janela.close()

if event == "Sim":

    while aux == False:

        # Chama as janelas
        aux_confirm = 0

    
        janela1 = janela_inicio()
        janela5 = janela_final_saida()

        
        janela.close()
        event, values = janela1.read() # Mostra a janela do Menu

        if event == "Sair":
            event5, values5 = janela5.read() # Mostra a janela de confirmação de saida
            if event5 == "Sim":
                exit(0)
            if event5 == "Não":
                janela5.close()
                janela1.close()
            if event5 == sg.WIN_CLOSED:
                janela5.close()
                janela1.close()

        if event == sg.WIN_CLOSED:
            aux = True
            exit(0)

        if event == "Instruções":
            janela1.close()
            janela3 = janela_instruction() 
            event, values = janela3.read() # Nostra a janela com as Instruções
            if event == "Voltar":
                janela3.close()
        elif event == "Jogar":
            start_time = time_as_int()
            
            janela1.close()

            janela2 = janela_jogo()
            janela6 = janela_professor()
            janela7 = janela_definicao()
            janela8 = janela_carregamento()

            while aux_confirm == 0:

                event7, values7 = janela7.read(timeout=1) # Mostra a janela de definição do nome e número de fases 
                if event7 == 'Jogar':
                    nome = values7['nome']
                    n = values7['nfases']

                    # Impede do usuário iniciar o programa com um nome e um número de fases inválido

                    if(n != ''):
                        if(int(n) > 0 and int(n) <= 10 and len(nome) > 0 and len(nome) <= 10): 
                            janela7.close()
                            
                            # Chama o jogo 
                            score = alunoRec(janela1, janela2, janela6, n, nome)
                            
                            # Retorna pro Menu
                            if score == -1:
                                break
                            else:

                                janela4 = janela_final()

                                while True:
                                    event, values = janela4.read(timeout=10) # Mostra a janela final com os pontos

                                    if score == 0:
                                        janela4['mensagem'].update(
                                            "Mais sorte na próxima!")
                                    elif score <= int(n)/2:
                                        janela4['mensagem'].update("Quase lá, tente novamente!")
                                    elif score == int(n):
                                        janela4['mensagem'].update("Parabéns "+ nome +"!")

                                    janela4['scorefinal'].update(score)

                                    if event == sg.WIN_CLOSED:
                                        exit(0)

                                    if event == "Voltar":
                                        janela4.close()
                                        aux_confirm = 1
                                        break

                        else:
                            continue

                elif event7 == 'Voltar':
                    janela7.close()
                    break
                    # continue

elif event == 'Não':
    janela.close()
cv2.destroyAllWindows()