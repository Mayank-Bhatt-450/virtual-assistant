import os,time,random,subprocess,pyttsx
#import pyttsx3 as pyttsx
a1=['      /\\                            /\\       ','     /  \\          /\\              /  \\      ','    /    \\        /  \\      /\\    /    \\     ','---------------------------------------------','           \\    /      \\  /    \\/            ','            \\  /        \\/                   ','             \\/                              ']

s2=['                                             ','       /\\              /\\                    ','    /\\/  \\    /\\      /  \\      /\\           ','---------------------------------------------','           \\/    \\  /      \\  /    \\/        ','                  \\/        \\/               ','                                             ']

d2=['                                             ','                          /\\                 ','   /\\     /\\    /\\       /  \\    /\\          ','---------------------------------------------','      \\  /   \\/    \\    /     \\/             ','       \\/           \\  /                     ','                     \\/                      ']

x=['                                             ','                                             ','                                             ','    -------------------------------------    ','                                             ','                                             ','                                             ']
a=[a1,s2,d2,x]
def prie(x,h=''):
    os.system('cls')
    print('''                 
                 (')                                (')
                  \\\\                                //
                   \\\\------------------------------//
                  .                                  . 
                .         ~                ~           .
              .           _                _            .
             .           / \              / \             .
             '           \_/              \_/             '
             |                                             |
             |                                             |
             |                     ^                       |
             |                                             |
             |'''+x[0]+'''|
             |'''+x[1]+'''|
             |'''+x[2]+'''|
             |'''+x[3]+'''|
             |'''+x[4]+'''|
             |'''+x[5]+'''|
             |'''+x[6]+'''|
              ---------------------------------------------       
       .'.   ________________________________________________   .'.
      |   | |                                                | |   |
..............................................................................'''+'\n'+h)
def talk(xo):
    def onStart(name):
        prie(a[4])
    def onWord(name, location, length):
        for i in range(2):
            prie(a[(random.randint(0,2))],xo[:location+length])
    def onEnd(name, completed):
        prie(a[3])

    engine = pyttsx.init()
    engine.setProperty('rate',90)
    engine.connect('started-utterance', onStart)
    engine.connect('started-word', onWord)
    engine.connect('finished-utterance', onEnd)
    engine.say(str(xo))
    engine.runAndWait()
prie(a[3])
#talk("""good evening everybody my name is iris and i m here to help you so how can i help you """)
b=["hello","you see","you like","human","think","your name","brain","kill"]
c=["hi there,my name is iris nice to meet u","sorry i can't see because my programmer forget to give me eyes","yes i like,and i also like to deleting files","humans are stupid who make more smarter beings","sorry, i can't think out of my limits","my name is iris","ha ha ha look who is talking about brain","killing is not good but one day humans will killed by there selfs by there own creation"]

t=2
while True:

    a1=input("enter you command :- ")
    os.system('cls')
    prie(a[3])
    for i in range(len(b)):
        if b[i]in a1:
            talk(c[i])
            t=1
            break

    if t!=1:
        print ("""dfgdfgdf
        dfgdfgdfg""")
        if t<4:
            talk("""sorry i dont get it""")
        if t>=4 and t<6:
            talk("now i ' m annoyed by your stupid questions")
        if t >=6 :
            talk("i can't believe that my creator leave me with these brain less peoples ")
    if "turn off"in a:
        subprocess.call(["shutdown", "/s"])
    t+=1

    #pass
#talk('''Iron''')









