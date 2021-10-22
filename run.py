from tkinter import font
from PySimpleGUI.PySimpleGUI import ColorChooserButton
import cv2
import numpy as np
import PySimpleGUI as sg
import time
from rmn import RMN

rmn = RMN()
current_time = 0  # [?]


def time_as_int():
    return int(round(time.time() * 100))


def janela_inicio():  # JANELA 1
    sg.theme('Reddit')
    layout = [
        [sg.T(" ")],
        [sg.Text("LabdeIA-TEA", size=(10, 1), justification="center",
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


def janela_definicao():
    sg.theme('Reddit')

    layout = [
        [sg.Text("Digite o n° de Fases:", font=(
            'Poppins', 15), justification="center")],
        [sg.Input(key="nfases", size=(5, 1), font=('Poppins', 15))],
        [sg.Button('Iniciar', button_color="#00b2ef", font=('Poppins', 13, "bold")), sg.Button(
            'Voltar', button_color="#00b2ef", font=('Poppins', 13, "bold"))]
    ]
    return sg.Window("Jogo de Expressões", layout=layout, size=(400, 200), element_justification='center', location=(800, 300))


def janela_carregamento():
    sg.theme('Reddit')

    layout = [
        [sg.Text("Carregando")],
        [sg.ProgressBar(3, orientation='h', size=(
            100, 20), key='carregamento')]
    ]
    return sg.Window("Jogo de Expressões", layout=layout, size=(300, 200), element_justification='center', location=(550, 250))


def janela_final():  # JANELA 4
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


def janela_jogo():  # JANELA 2
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
        [sg.Text('', size=(28, 1), text_color='#00b2ef', font=(
            'Poppins', 25), justification="center", key='expressao')],
        [sg.Text("Expressões Corretas:", size=(20, 1), justification="center", font=(
            "Poppins", 20, 'bold')), sg.Text('0', font=("Poppins", 20, 'bold'), key='scorenum')],
    ]
    return sg.Window("Jogo de Expressões", layout=layout, element_justification='c', size=(
        1370, 800), location=(300, 50))


def janela_professor():  # JANELA 6
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


def janela_instruction():  # JANELA 3
    sg.theme('Reddit')

    layout = [
        [sg.Image('images/rules.png', size=(700, 370))],
        [sg.Button("Voltar", size=(10, 1), button_color="#00b2ef",
                   font=("Poppins", 25, "bold"))]
    ]
    return sg.Window("Jogo de Expressões", layout=layout, size=(800, 600), element_justification='center', location=(600, 150))


def janela_final_saida():  # JANELA 5
    sg.theme('Reddit')

    layout = [
        [sg.Text("Você tem certeza que deseja sair?", font=(
            'Poppins', 15), justification="center")],
        [sg.Button("Sim", button_color="#00b2ef", font=("Poppins", 13, "bold")), sg.Button(
            "Não", button_color="#00b2ef", font=("Poppins", 13, "bold"))]
    ]
    return sg.Window("Jogo de Expressões", layout=layout, size=(400, 200), element_justification='center', location=(800, 300))


def translateEmo(emolabel):  # traduz o emolabel para o 'OutProfessor' da JANELA6 e JANELA2
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


# faz a contagem para o usuário (professor ou aluno) ser capturado
def nextTurn(user, janela2, janela6, i, n):
    current_time = 0
    start_time = time_as_int()

    if(user == "aluno"):
        janela6['camProfessor'].update(
            filename="images/teacher.png")                                       # feito
        # feito
        janela6['expressao'].update(" ")
        janela6['professor'].update(text_color="black", font=(
            'Poppins', 30, "bold"))                       # feito

        while current_time <= 500:
            # feito
            event, values = janela2.read(timeout=10)
            janela2['contador'].update('{:02d}'.format(
                (current_time // 100) % 60))                       # feito
            janela2['OutAluno'].update(" ", text_color="black", font=(
                'Poppins', 20, "bold"))               # não feito
            janela2['expressao'].update(
                "Atenção Aluno, agora é a sua vez!", font=('Poppins', 28, "bold"))  # feito

            # feito
            current_time = time_as_int() - start_time

        janela2['expressao'].update("Faça uma Expressão!", font=(
            'Poppins', 28, "bold"))                    # feito
        janela2['professor'].update(text_color="black", font=(
            'Poppins', 20, "bold"))                       # feito

    elif(user == "professor"):
        while current_time <= 500:                                                                          # feito
            # feito
            event2, values2 = janela2.read(timeout=10)
            # feito
            event, values = janela6.read(timeout=10)

            # janela6['qt_fases'].update(str(n))
            # janela2['qt_fases'].update(str(n))

            janela2['contador'].update("")
            janela2['professor'].update(text_color="black", font=(
                'Poppins', 30, "bold"))                   # feito
            janela2['aluno'].update(text_color="black", font=(
                'Poppins', 30, "bold"))                       # especifico, não feito

            # feito
            janela2['expressao'].update(" ")
            # [???] específico, não feito
            janela2['OutProfessor'].update(" ")
            janela2['OutAluno'].update("Aguarde", text_color="#D4181A", font=(
                "Poppins", 25, "bold"))       # específico, não feito
            # janela2['fase'].update(value=(i+1)+str("/"))                                                             # feito

            fase_str = str(i+1) + " / " + str(n)
            janela2['fase'].update(str(fase_str))
            # feito
            janela6['fase'].update(str(fase_str))

            # [???] específico, não feito
            janela6['OutProfessor'].update(" ")
            janela6['contador'].update('{:02d}'.format(
                (current_time // 100) % 60))                         # feito
            janela6['expressao'].update(
                "Atenção Professor, é a sua vez!", font=('Poppins', 28, "bold"))    # feito
            # específico para a janela6, não feito.
            janela6['camProfessor'].update(filename="images/teacher.png")

            # feito
            current_time = time_as_int() - start_time

        # feito
        janela6['expressao'].update("Professor, faça uma Expressão!")
        janela6['professor'].update(text_color="black", font=(
            'Poppins', 20, "bold"))                       # feito


def profRec(janela2, janela6, i, n, neutral=0):  # captura da tela do professor
    vid = cv2.VideoCapture(2)
    maior = 0
    frame_dic = {}
    emotion = ""
    frame = ""
    img_frame = ""
    emotions = []
    emocao = ""

    # "Atenção Professor, é a sua vez!",
    nextTurn("professor", janela2, janela6, i, n)

    current_time = 0
    start_time = time_as_int()

    while current_time <= 500:  # professor
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

            for resultProf in resultsProf:
                emolabelProf = resultProf['emo_label']
                emoproba = resultProf['emo_proba']

                emocao = translateEmo(emolabelProf)

                janela6['OutProfessor'].update(
                    emocao,  text_color="black", font=("Poppins", 25, "bold"))

            if(emoproba > 0.7 and emolabelProf != "neutral"):
                emotions.append(emolabelProf)

                # se o emolabel for diferente de todas as keys, incrementa no frame_dic
                if(emolabelProf != key for key in frame_dic):
                    frame_dic[emolabelProf] = frame_cap

            imgbytes = cv2.imencode('.png', frame_cap)[1].tobytes()
            janela6['camProfessor'].update(data=imgbytes)

        except Exception as err:
            print(err)
            continue

    for e in emotions:                                      # pega a emoção de maior frequência
        if(emotions.count(e) > maior):
            maior = emotions.count(e)
            emotion = e         # emolabel final

    if len(emotions) <= 0 and emotion == "":
        neutral += 1

        if(neutral >= 2):
            return -1

        current_time = 0
        start_time = time_as_int()

        while current_time <= 500:
            event, values = janela6.read(timeout=1)
            janela6['camProfessor'].update(filename="images/teacher.png")
            janela6['OutProfessor'].update(
                "Tente Novamente", text_color="#D4181A", font=("Poppins", 25, "bold"))
            current_time = time_as_int() - start_time

        start_time = time_as_int()
        vid.release()
        emotion = profRec(janela2, janela6, i, n, neutral)

    emocao = translateEmo(emotion)

    janela2['OutProfessor'].update(
        emocao, text_color="black", font=("Poppins", 25, "bold"))
    janela6['OutProfessor'].update(
        emocao, text_color="black", font=("Poppins", 25, "bold"))

    for key in frame_dic:                                   # guarda a imagem do professor
        if key == emotion:
            img_frame = cv2.imencode('.png', frame_dic[key])[1].tobytes()
            janela2['camProfessor'].update(data=img_frame)
            janela6['camProfessor'].update(data=img_frame)

    vid.release()
    return emotion


def alunoRec(janela1, janela2, janela6, n):  # captura da tela do aluno
    janela1.close()
    score = 0

    for i in range(int(n)):
        # emo_p = ""
        results = []
        result = {}

        emo_p = profRec(janela2, janela6, i, n)

        if(emo_p == -1):
            janela2.close()
            janela6.close()
            return -1

        vid1 = cv2.VideoCapture(-1)

        # "Atenção Aluno, é a sua vez!"
        nextTurn("aluno", janela2, janela6, i, n)

        current_time = 0
        start_time = time_as_int()

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

                frame = np.fliplr(frame).astype(np.uint8)
                imgbytes = cv2.imencode('.png', frame)[1].tobytes()
                janela2['camAluno'].update(data=imgbytes)
                janela2['contador'].update('{:02d}.{:02d}'.format(
                    (current_time // 100) % 60, current_time % 100))

                current_time = time_as_int() - start_time
                if(current_time >= 200):
                    results = rmn.detect_emotion_for_single_frame(frame)

                for result in results:
                    emolabel = result['emo_label']
                    emoproba = result['emo_proba']

                if (emoproba > 0.7 and emolabel == emo_p and current_time < 1000):

                    current_time = 0
                    start_time = time_as_int()

                    score += 1
                    while current_time <= 500:
                        event, values = janela2.read(timeout=1)
                        current_time = time_as_int() - start_time

                        janela2['OutProfessor'].update(
                            "Expressão Correta", text_color="white", font=("Poppins", 25, "bold"))
                        janela2['OutAluno'].update(
                            "Expressão Correta", text_color="#19D342", font=("Poppins", 25, "bold"))
                        janela2['scorenum'].update(value=score)

                    start_time = time_as_int()
                    break

                elif (current_time > 1000):

                    current_time = 0
                    start_time = time_as_int()

                    while current_time <= 500:
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


aux = False
aux_confirm = 0
score = 0

while aux == False:

    aux_confirm = 0
    # if score == -1:
    #     # continue                                                                # [!!1111111111111111]
    #     break

    janela1 = janela_inicio()
    janela5 = janela_final_saida()
    event, values = janela1.read()

    if event == "Sair":
        event5, values5 = janela5.read()
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
        event, values = janela3.read()
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

            # if(win4_aux == 1): break

            event7, values7 = janela7.read(timeout=1)
            if event7 == 'Iniciar':

                n = values7['nfases']

                if(int(n) > 0 and int(n) < 10):
                    janela7.close()

                    # current_time = 0
                    # start_time = time_as_int()

                    # while current_time <= 300:
                    #     event, values = janela8.read(timeout=1)
                    #     janela8['carregamento'].update((current_time // 100) % 60)
                    #     current_time = time_as_int() - start_time
                    # janela8.close()

                    score = alunoRec(janela1, janela2, janela6, n)

                    if score == -1:
                        # continue                                                                # [!!1111111111111111]
                        # aux_confirm = 1
                        break
                    else:
                        janela4 = janela_final()

                        while True:
                            event, values = janela4.read(timeout=10)

                            if score == 0:
                                janela4['mensagem'].update(
                                    "Mais sorte na próxima!")
                            elif score <= int(n)/2:
                                janela4['mensagem'].update("Tente novamente!")
                            elif score >= int(n)/2:
                                janela4['mensagem'].update(
                                    "Quase lá, tente novamente!")
                            elif score == int(n):
                                janela4['mensagem'].update("Parabéns Aluno!")

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


cv2.destroyAllWindows()


