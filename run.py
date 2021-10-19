from PySimpleGUI.PySimpleGUI import ColorChooserButton
import cv2
import numpy as np
import PySimpleGUI as sg
import time
from rmn import RMN

rmn = RMN()
current_time = 0

def time_as_int():
    return int(round(time.time() * 100))

def janela_inicio():
    sg.theme('Reddit')
    layout = [
        [sg.Image(filename='images/pti.png', size=(300, 300))],
        [sg.Button("Início", button_color= "#00b2ef", font=("Poppins", 25), size=(10, 1))],
        [sg.Button("Instruções", button_color= "#00ad4e", font=("Poppins", 25), size=(10, 1))],
        [sg.Button("Sair", size=(10, 1), button_color= "#d4181a", font=("Poppins", 25))]
    ]
    return sg.Window("Jogo de Expressões", layout=layout, size=(800, 600), element_justification='center', location=(350, 150))

def janela_final():
    sg.theme('Reddit')
    layout = [
        [sg.Image(filename='images/pti.png' ,size=(300, 300))],
        [sg.Text("",size=(32,1), justification="center",font=('Poppins', 25, 'bold'), key='mensagem')],
        [sg.Text("N° de Expressões Corretas: ", size=(23,1), font=("Poppins", 18)), sg.Text('0', font=("Poppins", 18), key='scorefinal')],
        [sg.Button("Voltar", button_color= "#00b2ef",size=(10, 1), font=("Poppins", 25))],
        
    ]
    return sg.Window("Jogo de Expressões", layout=layout, size=(800, 600), element_justification='center', location=(350, 150))

def janela_jogo():
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
        1370, 800), location=(50, 30))

def janela_instruction():
    sg.theme('Reddit')
    
    layout = [
        [sg.Image('images/rules.png',size=(700,300))],
        [sg.Button("Voltar", size=(10,1), button_color= "#00b2ef",font=("Poppins", 25))]
    ]
    return sg.Window("Jogo de Expressões",layout=layout, size=(800, 600), element_justification='center', location=(350, 150))

def janela_final_saida():
    sg.theme('Reddit')
    
    layout = [
        [sg.Text("Você tem certeza que deseja sair?", font=('Poppins', 15), justification="center")],
        [sg.Button("Sim", size=(6,1), button_color= "#00b2ef", font=("Poppins", 12)), sg.Button("Não", size=(6,1), button_color= "#00b2ef",font=("Poppins", 12))]
        ]
    return sg.Window("Jogo de Expressões",layout=layout, size=(400, 200), element_justification='center', location=(550, 250))

def translateEmo(emolabel):

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
        emocao = "Supreso"

    return emocao

def capture(janela2, start_time, i, again=0): #Captura da Tela do Professor
    vid = cv2.VideoCapture(-1)
    maior = 0
    frame_dic = {}
    emotion = ""
    current_time = 0
    frame = ""
    img_frame = ""
    emotions = []
    emocao = ""

    while current_time <= 500:
        event, values = janela2.read(timeout=10)
        janela2['OutProfessor'].update(" ")
        janela2['OutAluno'].update("Aguarde", text_color="#D4181A", font=("Poppins", 25, "bold"))

        janela2['fase'].update(value=(i+1))
        janela2['contador'].update('{:02d}'.format((current_time //100) % 60))
        
        janela2['expressao'].update("Atenção Professor, é a sua vez!", font=('Poppins', 28, "bold"))
        janela2['camProfessor'].update(filename="images/teacher.png")
        current_time = time_as_int() - start_time
    
    janela2['expressao'].update("Professor, faça uma Expressão!")
    janela2['professor'].update(text_color="#00b2ef", font=('Poppins', 20, "bold"))
    janela2['aluno'].update(text_color="black", font=('Poppins', 20, "bold"))

    current_time = 0
    start_time = time_as_int()
    while current_time < 500: # professor
        event, values = janela2.read(timeout=20)
        janela2['contador'].update('{:02d}.{:02d}'.format((current_time //100) % 60, current_time % 100))
            
        ret, frame_cap = vid.read()

        if frame_cap is None or ret is not True:
            continue
        
        try:    
            emoproba = 0

            current_time = time_as_int() - start_time

            frame_cap = np.fliplr(frame_cap).astype(np.uint8)
            results = rmn.detect_emotion_for_single_frame(frame_cap)
            
            for result in results:
                emolabel = result['emo_label']
                emoproba = result['emo_proba']
                
                emocao = translateEmo(emolabel)

                janela2['OutProfessor'].update(emocao,  text_color="black", font=("Poppins", 25, "bold"))

            if(emoproba > 0.7 and emolabel != "neutral"):
                emotions.append(emolabel)

                if(emolabel != key for key in frame_dic):   # se o emolabel for diferente de todas as keys, incrementa no frame_dic                
                    frame_dic[emolabel] = frame_cap

            imgbytes = cv2.imencode('.png', frame_cap)[1].tobytes()
            janela2['camProfessor'].update(data=imgbytes)

        except Exception as err:
            print(err)
            continue
    
    for e in emotions:                                      # pega a emoção de maior frequência
        if(emotions.count(e) > maior):
            maior = emotions.count(e)
            emotion = e         # emolabel final         
            
    if len(emotions) <= 0:
        current_time = 0
        start_time = time_as_int()
        while current_time <= 500:
            event, values = janela2.read(timeout=10)
            janela2['camProfessor'].update(filename="images/teacher.png")
            janela2['OutProfessor'].update("Tente Novamente", text_color="#D4181A", font=("Poppins", 25, "bold"))
            current_time = time_as_int() - start_time
        
        start_time = time_as_int()
        vid.release()
        emotion = capture(janela2, start_time, i, again) 

    emocao = translateEmo(emotion)

    janela2['OutProfessor'].update(emocao, text_color="black", font=("Poppins", 25, "bold"))

    for key in frame_dic:                                   # guarda a imagem do professor
        if key == emotion:
            img_frame = cv2.imencode('.png', frame_dic[key])[1].tobytes()
            janela2['camProfessor'].update(data=img_frame)

    vid.release()
    return emotion

def jogar(janela1, janela2, start_time): #Captura da Tela do Aluno
    janela1.close()
    score = 0
    emo_p = ""
   
    for i in range(3):
        
        emo_p = capture(janela2, start_time, i) 
        vid1 = cv2.VideoCapture(2)
        janela2['fase'].update(value=(i+1)) 

        current_time = 0
        start_time = time_as_int()

        while current_time <= 500:
            event, values = janela2.read(timeout=20)
            janela2['contador'].update('{:02d}'.format((current_time //100) % 60))
            janela2['OutAluno'].update(" ", text_color="black", font=('Poppins', 20, "bold"))
            janela2['expressao'].update("Atenção Aluno, agora é a sua vez!")
            current_time = time_as_int() - start_time

        janela2['expressao'].update("Faça uma Expressão!")
        janela2['professor'].update(text_color="black", font=('Poppins', 20, "bold"))

        current_time = 0
        start_time = time_as_int()

        while True: 
                                                   # aluno
            ret, frame = vid1.read()
            if frame is None or ret is not True:
                continue

            try:
                emoproba = 0
                event, values = janela2.read(timeout=20)
                current_time = time_as_int() - start_time

                if event == "Exit" or event == sg.WIN_CLOSED:
                    exit(0)

                frame = np.fliplr(frame).astype(np.uint8)
                results = rmn.detect_emotion_for_single_frame(frame)

                for result in results:
                    emolabel = result['emo_label']
                    emoproba = result['emo_proba']

                if (emoproba > 0.7 and emolabel == emo_p and current_time < 1000):
                    current_time = 0
                    while current_time <= 700 :
                        event, values = janela2.read(timeout=20)
                        current_time = time_as_int() - start_time
                    
                        janela2['OutProfessor'].update("Expressão Correta", text_color="white", font=("Poppins", 25, "bold"))
                        janela2['OutAluno'].update("Expressão Correta", text_color="#19D342", font=("Poppins", 25, "bold"))
                    
                    score += 1
                    janela2['scorenum'].update(value=score)
                    start_time = time_as_int()
                    break

                elif (current_time > 1000):
                    current_time = 0
                    while current_time <= 700 :
                        event, values = janela2.read(timeout=20)
                        current_time = time_as_int() - start_time

                        janela2['OutProfessor'].update("Tempo Esgotado", text_color="white", font=("Poppins", 25, "bold"))
                        janela2['OutAluno'].update("Tempo Esgotado", text_color="#D4181A", font=("Poppins", 25, "bold"))
                    
                    start_time = time_as_int()
                    break

                imgbytes = cv2.imencode('.png', frame)[1].tobytes()
                janela2['camAluno'].update(data=imgbytes)
                janela2['contador'].update('{:02d}.{:02d}'.format((current_time //100) % 60, current_time % 100))

            except Exception as err:
                print(err)
                continue
        vid1.release()
        janela2['camAluno'].update(filename="images/user.png")
    janela2.close()

    return score

aux = False
start_time = time_as_int()

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

        score = jogar(janela1, janela2, start_time)
        janela4 = janela_final()
        
        while True:
            event, values = janela4.read(timeout=20)
            
            if score == 0:
                janela4['mensagem'].update("Mais sorte na proxíma!")
            elif score <= 2:
                janela4['mensagem'].update("Tente novamente! ")
            elif score >= 2:
                janela4['mensagem'].update("Parabéns!")
            
            janela4['scorefinal'].update(score)

            if event  == sg.WIN_CLOSED:
                exit(0)

            if event == "Voltar":
                janela4.close()
                break

cv2.destroyAllWindows()