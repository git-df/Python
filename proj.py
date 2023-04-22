import random
import json
import tkinter
from tkinter import *

with open('./data.json', encoding="utf8") as f:
    data = json.load(f)

questions = [v for v in data[0].values()]
answers = [v for v in data[1].values()]
answers_choice = [v for v in data[2].values()]

answersIndexes = []

panel = tkinter.Tk()
panel.title("Pythoners")
panel.geometry("1000x800")
panel.resizable(0,0)

revards = ["0", "100", "500", "2500", "(GWARANTOWANE) 10000", "25000", "50000", "(GWARANTOWANE) 100000", "250000", "500000", "1000000"]

def generateGamePanel():
    global question, answera, answerb, answerc, answerd, revard, revardGet
    
    revard = Button(
        panel,
        text = "GRASZ O " + revards[1] + " zł",
        font = ("Consolas", 16),
        background = "#FEFF86",
        border = 0
    )
    revard.place(x=50, y=700)

    revardGet = Button(
            panel,
            text = "ZAKOŃCZ Z " + revards[0] + " zŁ",
            font = ("Consolas", 16),
            command= golose,
            width=35,
            background = "#FEFF86",
            border = 0
        )

    if revards[0] != "0":
        revardGet.place(x=510, y=700)

    question = Label(
        panel,
        text = "Pytanie " + str(11-len(answersIndexes)) +". "+ questions[answersIndexes[0]],
        font = ("Consolas", 16),
        justify = "center",
        width = 500,
        background = "#FEFF86",
        border = 0
    )
    question.pack(pady=(100,30))

    answera = Button(
        panel,
        text = answers_choice[answersIndexes[0]][0],
        height= 10, 
        width= 60,
        command = lambda: select(answers_choice[answersIndexes[0]][0]),
        background = "#B0DAFF",
        border = 0
    )

    answerb = Button(
        panel,
        text = answers_choice[answersIndexes[0]][1],
        height= 10, 
        width= 60,
        command = lambda: select(answers_choice[answersIndexes[0]][1]),
        background = "#B0DAFF",
        border = 0
    )

    answerc = Button(
        panel,
        text = answers_choice[answersIndexes[0]][2],
        height= 10, 
        width= 60,
        command = lambda: select(answers_choice[answersIndexes[0]][2]),
        background = "#B0DAFF",
        border = 0
    )

    answerd = Button(
        panel,
        text = answers_choice[answersIndexes[0]][3],
        height= 10, 
        width= 60,
        command = lambda: select(answers_choice[answersIndexes[0]][3]),
        background = "#B0DAFF",
        border = 0
    )

    answera.place(x=50, y=200)
    answerb.place(x=510, y=200)
    answerc.place(x=50, y=400)
    answerd.place(x=510, y=400)


def half():
    global halfBtn
    b=5
    for i in [1, 2]:
        x = random.randint(0, 3)
        while answers_choice[answersIndexes[0]][x] == answers[answersIndexes[0]] or b==x:
            x = random.randint(0, 3)

        if  x == 0:
            answera.destroy()

        if  x == 1:
            answerb.destroy()

        if  x == 2:
            answerc.destroy()

        if  x == 3:
            answerd.destroy()

        b=x
    halfBtn.destroy()

def closeGamePanel():
    answera.destroy()
    answerb.destroy()
    answerc.destroy()
    answerd.destroy()
    question.destroy()
    revardGet.destroy()
    revard.destroy()

def epicwin():

    bgepic = PhotoImage(file="img/epic.png")
    bg2 = Label(
        panel,
        image = bgepic,
        background = "#D4AF37",
    )
    bg2.place(x=0,y=0)

    endText = Label(
        panel,
        text = "Wygrywasz główną nagrodę !!!",
        font = ("Comic sans MS",30,"bold"),
        background = "#D4AF37"
        
    )
    endText.pack(pady=(100,30))


def select(selected):
    if selected == answers[answersIndexes[0]]:
        if len(answersIndexes) > 1:
            answersIndexes.pop(0)
            revards.pop(0)
            closeGamePanel()
            generateGamePanel()
        else:
            epicwin()
    else:
        lose()

def lose():
    bg2 = Label(
        panel,
        image = bgimg,
        background = "#ffffff",
    )
    bg2.place(x=0,y=0)

    score = len(revards)
    endlabel = ""

    if score > 7:
        endlabel = "Nic nie wygrałeś"
    elif score > 4:
        endlabel = "Wygrywasz gwarantowane 10000 zł"
    else:
        endlabel = "Wygrywasz gwarantowane 100000 zł"

    endText = Label(
        panel,
        text = endlabel,
        font = ("Comic sans MS",30,"bold"),
        background = "#B9E9FC",
        border = 0
    )
    endText.pack(pady=(100,30))

def golose():
    bg2 = Label(
        panel,
        image = bgimg,
        background = "#ffffff",
    )
    bg2.place(x=0,y=0)

    endText = Label(
        panel,
        text = "Wygrywasz " + revards[0] + " zł",
        font = ("Comic sans MS",30,"bold"),
        background = "#B9E9FC",
        border = 0
    )
    endText.pack(pady=(100,30))

def randomQuestions():
    global answersIndexes
    while(len(answersIndexes) < 10):
        x = random.randint(0, len(questions)-1)
        if x in answersIndexes:
            continue
        else:
            answersIndexes.append(x)

def start():
    bg.place(x=0,y=0)
    btnStart.place(x=300,y=300)
    startText.place(x=100,y=100)
    panel.mainloop()

    

def startGame():
    global halfBtn
    btnStart.destroy()
    startText.destroy()
    generateGamePanel()

    halfBtn = Button(
        panel,
        text = "KOŁO RATUNKOWE 50/50",
        font = ("Consolas", 16),
        command=half,
        background = "#FEFF86",
        border = 0
    )
    halfBtn.place(x=350, y=600)

bgimg = PhotoImage(file="img/bg.png")
bg = Label(
    panel,
    image = bgimg,
)

startimg = PhotoImage(file="img/start.png")
btnStart = Button(
    panel,
    image = startimg,
    relief = FLAT,
    border = 0,
    command = startGame,
    borderwidth=0, 
    highlightthickness=0, 
    bd=0,
    background = "#B9E9FC"
)

startText = Label(
    panel,
    text = "Witamy w grze Pythoners",
    font = ("Comic sans MS",50,"bold"),
    background = "#B9E9FC"
)

randomQuestions()
start()





