from PySimpleGUI.PySimpleGUI import ColorChooserButton
import cv2
import numpy as np
import PySimpleGUI as sg
import time
from rmn import RMN

rmn = RMN()
current_time = 0 # [?]

def time_as_int():
    return int(round(time.time() * 100))

def janela_inicio(): # JANELA 1 
    sg.theme('Reddit')
    layout = [
        [sg.T(" ")],
        [sg.Text("DualTEA",size=(10,1), justification="center",font=('Poppins', 40, 'bold'), key='')],
        [sg.Image(filename='images/pti.png', size=(250, 250))],
        [sg.T(" ")],
        [sg.Button("Início", button_color= "#00b2ef", font=("Poppins", 25), size=(10, 1))],
        [sg.Button("Instruções", button_color= "#00ad4e", font=("Poppins", 25), size=(10, 1))],
        [sg.Button("Sair", size=(10, 1), button_color= "#d4181a", font=("Poppins", 25))]
    ]
    return sg.Window("Jogo de Expressões", layout=layout, size=(800, 600), element_justification='center', location=(350, 150))

def janela_final(): # JANELA 4 
    sg.theme('Reddit')
    layout = [
        [sg.Image(filename='images/pti.png' ,size=(300, 300))],
        [sg.Text("",size=(32,1), justification="center",font=('Poppins', 25, 'bold'), key='mensagem')],
        [sg.Text("N° de Expressões Corretas: ", size=(23,1), font=("Poppins", 18)), sg.Text('0', font=("Poppins", 18), key='scorefinal')],
        [sg.Button("Voltar", button_color= "#00b2ef",size=(10, 1), font=("Poppins", 25))],
        
    ]
    return sg.Window("Jogo de Expressões", layout=layout, size=(800, 600), element_justification='center', location=(350, 150))

def janela_jogo(): # JANELA 2 
    sg.theme('Reddit')

    col1 = [[sg.Text("PROFESSOR",size=(12,1), font=('Poppins', 30, 'bold'), justification="center", key='professor')],
            [sg.Image(filename='images/teacher.png', background_color='white', size=(412, 412),  key='camProfessor')],
            [sg.Text("",size=(18,1), font=('Poppins', 15), justification="center", key='OutProfessor')]
        ]

    col2 = [[sg.Text("ALUNO", size=(12,1),font=('Poppins', 30, "bold"), justification="center", key='aluno')],
            [sg.Image(filename='images/user.png', background_color='white', size=(412, 412), key='camAluno')],
            [sg.Text("",size=(18,1), font=('Poppins', 15), justification="center", key='OutAluno')]
        ]

    layout = [
        [sg.T('')],
        [sg.Text("Fase:", size=(4, 1), justification="center", font=("Poppins", 25)), sg.Text('',size=(8, 1),font=("Poppins", 25, 'bold'),text_color='#c71017', key='fase'), 
        sg.T('                                                                                                                                                                                         '), 
        sg.Text("Tempo:", size=(7, 1), justification="center", font=("Poppins", 25)), sg.Text('', size=(12, 1),text_color='#c71017', font=('Poppins', 25,'bold'), key='contador')],


        [sg.Column(col1,element_justification='c'), sg.VSeparator('white'), sg.Column(col2,element_justification='c')],
        [sg.T('')],
        [sg.Text('', size=(28, 1), text_color= '#00b2ef', font=('Poppins', 25), justification="center", key='expressao')],
        [sg.Text("Expressões Corretas:", size=(20, 1), justification="center", font=("Poppins", 20, 'bold')), sg.Text('0', font=("Poppins", 20, 'bold'), key='scorenum')],
    ]
    return sg.Window("Jogo de Expressões", layout=layout ,element_justification='c', size=(
        1370, 800), location=(1750, 50))

def janela_professor(): # JANELA 6 
    sg.theme('Reddit')

    layout = [
        [sg.T('')],
        [sg.Text("Fase:", size=(4, 1), justification="center", font=("Poppins", 25)), sg.Text('',size=(8, 1),font=("Poppins", 25, 'bold'),text_color='#c71017', key='fase'), 
        sg.T('                                                                                                                                                                                         '), 
        sg.Text("Tempo:", size=(7, 1), justification="center", font=("Poppins", 25)), sg.Text('', size=(12, 1),text_color='#c71017', font=('Poppins', 25,'bold'), key='contador')],
        
        [
            [sg.Text("PROFESSOR",size=(12,1), font=('Poppins', 30, 'bold'), justification="center", key='professor')],
            [sg.Image(filename='images/teacher.png', background_color='white', size=(412, 412),  key='camProfessor')],
            [sg.Text("",size=(18,1), font=('Poppins', 15), justification="center", key='OutProfessor')]
        ],

        [sg.T('')],
        [sg.Text('', size=(28, 1), text_color= '#00b2ef', font=('Poppins', 25), justification="center", key='expressao')],
    ]
    return sg.Window("Jogo de Expressões", layout=layout ,element_justification='c', size=(
        1370, 800), location=(50, 30))

def janela_instruction(): # JANELA 3 
    sg.theme('Reddit')
    
    layout = [
        [sg.Image('images/rules.png',size=(700,370))],
        [sg.Button("Voltar", size=(10,1), button_color= "#00b2ef",font=("Poppins", 25))]
    ]
    return sg.Window("Jogo de Expressões",layout=layout, size=(800, 600), element_justification='center', location=(350, 150))

def janela_final_saida(): # JANELA 5 
    sg.theme('Reddit')
    
    layout = [
        [sg.Text("Você tem certeza que deseja sair?", font=('Poppins', 15), justification="center")],
        [sg.Button("Sim", size=(6,1), button_color= "#00b2ef", font=("Poppins", 12)), sg.Button("Não", size=(6,1), button_color= "#00b2ef",font=("Poppins", 12))]
        ]
    return sg.Window("Jogo de Expressões",layout=layout, size=(400, 200), element_justification='center', location=(550, 250))

def translateEmo(emolabel): # traduz o emolabel para o 'OutProfessor' da JANELA6 e JANELA2 
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

def nextTurn(user, janela2, janela6, i): # faz a contagem para o usuário (professor ou aluno) ser capturado 
    current_time = 0
    start_time = time_as_int()

    if(user == "aluno"):
        janela6['camProfessor'].update(filename="images/teacher.png")                                       # feito
        janela6['expressao'].update(" ")                                                                    # feito
        janela6['professor'].update(text_color="black", font=('Poppins', 30, "bold"))                       # feito

        while current_time <= 500:                                                                                  
            event, values = janela2.read(timeout=10)                                                        # feito
            janela2['contador'].update('{:02d}'.format((current_time //100) % 60))                       # feito
            janela2['OutAluno'].update(" ", text_color="black", font=('Poppins', 20, "bold"))               # não feito
            janela2['expressao'].update("Atenção Aluno, agora é a sua vez!", font = ('Poppins', 28,"bold")) # feito

            current_time = time_as_int() - start_time                                                       # feito

        janela2['expressao'].update("Faça uma Expressão!", font=('Poppins', 28, "bold"))                    # feito
        janela2['professor'].update(text_color="black", font=('Poppins', 20, "bold"))                       # feito


    elif(user == "professor"):  
        while current_time <= 500:                                                                          # feito
            event2, values2 = janela2.read(timeout=10)                                                      # feito
            event, values = janela6.read(timeout=10)                                                        # feito

            janela2['contador'].update("")
            janela2['professor'].update(text_color="black", font=('Poppins', 30, "bold"))                   # feito
            janela2['aluno'].update(text_color="black", font=('Poppins', 30, "bold"))                       # especifico, não feito

            janela2['expressao'].update(" ")                                                                # feito
            janela2['OutProfessor'].update(" ")                                                             # [???] específico, não feito
            janela2['OutAluno'].update("Aguarde", text_color="#D4181A", font=("Poppins", 25, "bold"))       # específico, não feito
            janela2['fase'].update(value=(i+1))                                                             # feito

            janela6['OutProfessor'].update(" ")                                                             # [???] específico, não feito
            janela6['fase'].update(value=(i+1))                                                             # feito        
            janela6['contador'].update('{:02d}'.format((current_time //100)%60))                         # feito
            janela6['expressao'].update("Atenção Professor, é a sua vez!", font=('Poppins', 28, "bold"))    # feito
            janela6['camProfessor'].update(filename="images/teacher.png")                                   # específico para a janela6, não feito.

            current_time = time_as_int() - start_time                                                       # feito

        janela6['expressao'].update("Professor, faça uma Expressão!")                                       # feito
        janela6['professor'].update(text_color="black", font=('Poppins', 20, "bold"))                       # feito

def profRec(janela2, janela6, i, neutral=0): # captura da tela do professor 
    vid = cv2.VideoCapture(-1)
    maior = 0
    frame_dic = {}
    emotion = ""
    frame = ""
    img_frame = ""
    emotions = []
    emocao = ""

    nextTurn("professor", janela2, janela6, i) # "Atenção Professor, é a sua vez!", 

    current_time = 0
    start_time = time_as_int()

    while current_time <= 500: # professor
        event2, values2 = janela2.read(timeout=1)
        event, values = janela6.read(timeout=1)
        janela6['contador'].update('{:02d}.{:02d}'.format((current_time //100) % 60, current_time % 100))
            
        ret, frame_cap = vid.read()

        if frame_cap is None or ret is not True:
            continue
        
        try:    
            if event == "Exit" or event == sg.WIN_CLOSED or event2 == "Exit" or event2 == sg.WIN_CLOSED:
                janela2.close()
                # janela6.close()
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

                janela6['OutProfessor'].update(emocao,  text_color="black", font=("Poppins", 25, "bold"))

            if(emoproba > 0.7 and emolabelProf != "neutral"):
                emotions.append(emolabelProf)

                if(emolabelProf != key for key in frame_dic):   # se o emolabel for diferente de todas as keys, incrementa no frame_dic                
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
        neutral+=1

        if(neutral >= 5):
            return -1

        current_time = 0
        start_time = time_as_int()

        while current_time <= 500:
            event, values = janela6.read(timeout=1)
            janela6['camProfessor'].update(filename="images/teacher.png")
            janela6['OutProfessor'].update("Tente Novamente", text_color="#D4181A", font=("Poppins", 25, "bold"))
            current_time = time_as_int() - start_time
        
        start_time = time_as_int()
        vid.release()
        emotion = profRec(janela2, janela6, i, neutral) 

    emocao = translateEmo(emotion)

    janela2['OutProfessor'].update(emocao, text_color="black", font=("Poppins", 25, "bold"))
    janela6['OutProfessor'].update(emocao, text_color="black", font=("Poppins", 25, "bold"))

    for key in frame_dic:                                   # guarda a imagem do professor
        if key == emotion:
            img_frame = cv2.imencode('.png', frame_dic[key])[1].tobytes()
            janela2['camProfessor'].update(data=img_frame)
            janela6['camProfessor'].update(data=img_frame)

    vid.release()
    return emotion

def alunoRec(janela1, janela2, janela6): # captura da tela do aluno 
    janela1.close()
    score = 0
    
    for i in range(3):
        emo_p = ""
        results = []
        result = {}
    
        emo_p = profRec(janela2, janela6, i) 

        if(emo_p == -1):
            janela2.close()
            janela6.close()
            return -1

        vid1 = cv2.VideoCapture(2)
        janela2['fase'].update(value=(i+1)) 

        nextTurn("aluno", janela2, janela6, i) # "Atenção Aluno, é a sua vez!"

        current_time = 0
        start_time = time_as_int()  

        while True: 
            ret, frame = vid1.read()
            if frame is None or ret is not True:
                continue

            try:   
                emoproba = 0
                emolabel = ""

                event, values = janela2.read(timeout=1)
                janela2['aluno'].update(text_color="black", font=('Poppins', 20, "bold"))

                if event == "Exit" or event == sg.WIN_CLOSED:
                    janela6.close()
                    # janela2.close()
                    exit(0)

                frame = np.fliplr(frame).astype(np.uint8)
                imgbytes = cv2.imencode('.png', frame)[1].tobytes()
                janela2['camAluno'].update(data=imgbytes)
                janela2['contador'].update('{:02d}.{:02d}'.format((current_time //100) % 60, current_time % 100))

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
                    while current_time <= 500 :
                        event, values = janela2.read(timeout=1)
                        current_time = time_as_int() - start_time
                    
                        janela2['OutProfessor'].update("Expressão Correta", text_color="white", font=("Poppins", 25, "bold"))
                        janela2['OutAluno'].update("Expressão Correta", text_color="#19D342", font=("Poppins", 25, "bold"))
                        janela2['scorenum'].update(value=score)

                    start_time = time_as_int()
                    break

                elif (current_time > 1000):

                    current_time = 0
                    start_time = time_as_int()

                    while current_time <= 500 :
                        event, values = janela2.read(timeout=1)
                        current_time = time_as_int() - start_time

                        janela2['OutProfessor'].update("Tempo Esgotado", text_color="white", font=("Poppins", 25, "bold"))
                        janela2['OutAluno'].update("Tempo Esgotado", text_color="#D4181A", font=("Poppins", 25, "bold"))
                    
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

while aux == False:
    janela1 = janela_inicio()
    janela5 = janela_final_saida()
    event, values = janela1.read()
    
    if event == "Sair" :
        event2, values2 = janela5.read()
        if event2 == "Sim":
            exit(0)
        if event2 == "Não":
            janela5.close()
            janela1.close()
        if event2 == sg.WIN_CLOSED:
            janela5.close()
            janela1.close()
    
    if event  == sg.WIN_CLOSED:
        aux = True
        exit(0)
        
    if event == "Instruções":
        janela1.close()
        janela3 = janela_instruction()
        event, values = janela3.read()
        if event == "Voltar":
            janela3.close()
    elif event == "Início":
        start_time = time_as_int()

        janela1.close()
        janela2 = janela_jogo()
        janela6 = janela_professor()

        score = alunoRec(janela1, janela2, janela6)

        if score == -1:
            continue
        else:
            # if(score != -1): 
            janela4 = janela_final()
        
            while True:
                event, values = janela4.read(timeout=10)
                
                if score == 0:
                    janela4['mensagem'].update("Mais sorte na próxima!")
                elif score <= 2:
                    janela4['mensagem'].update("Tente novamente!")
                elif score >= 2:
                    janela4['mensagem'].update("Parabéns Aluno!")
                
                janela4['scorefinal'].update(score)

                if event  == sg.WIN_CLOSED:
                    exit(0)

                if event == "Voltar":
                    janela4.close()
                    break
              
cv2.destroyAllWindows()