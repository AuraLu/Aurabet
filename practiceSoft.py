from tkinter import*
from Aurabet_Dictionary import*
import random

class TestProgram:
    def __init__(self):
        self.window = Tk()
        self.baseFrame = Frame(self.window)
        self.leftFrame = Frame(self.baseFrame)
        self.letterCanvas = Canvas(self.baseFrame, width =160, height =160, bg ='#818181')
        self.inputBox = Entry(self.leftFrame, width =6)
        self.inputBoxANS = Label(self.leftFrame, text ='=- ? -=', width =6, justify ='center')
        self.singChoiceSelect = Listbox(self.leftFrame, selectmode = 'single', width =7, \
                                        height =4, activestyle ='none')

    def display(self):
        self.window.title('Aurabet Canvas prototype')
        self.window.geometry('265x175')
        self.baseFrame.pack(expand =True, fill ='both')
        self.leftFrame.grid(row =0, column =0, sticky =N, padx =10, pady =5)
        self.letterCanvas.grid(row =0, column =1)
        
        def next_ques():
            self.letterCanvas.delete('all')
            self.singChoiceSelect.pack_forget()
            self.inputBox.pack_forget()
            self.inputBoxANS.pack_forget()
            self.singChoiceSelect.delete(0,END)
            self.inputBox.delete(0,END)
            self.singChoiceSelect.config(selectbackground ='#5D84A4')
            self.inputBox.config(bg ='#161618')
            self.inputBoxANS.config(text ='=- ? -=')

            nextButton.config(text ='next')
            submitButton.config(state = NORMAL)
            
            self.ran_ques()
            
        def submit_ans():
            infile =open('ANS','r')
            ans =tuple(infile.read())
            infile.close()
            
            if ans[0] == '0':
                choice =self.singChoiceSelect.get(ANCHOR)
                if choice == ans[1]:        
                    self.singChoiceSelect.config(selectbackground ='#81B564')
                else:
                    self.singChoiceSelect.config(selectbackground ='#C14F41')
                    self.singChoiceSelect.itemconfig(ans[2], background ='#81B564')
            else:
                guess = self.inputBox.get().upper()
                word =''.join(ans[1:])
                
                if guess == word:
                    self.inputBox.config(bg ='#81B564')
                else:
                    self.inputBox.config(bg ='#C14F41')
                self.inputBoxANS.config(text =word)
            submitButton.config(state = DISABLED)
                    
                
        def exit_window():
            self.window.destroy()

        exitButton =Button(self.leftFrame, text ='exit', fg='#212124',command =exit_window)
        nextButton =Button(self.leftFrame, text ='begin', fg='#212124',command =next_ques)
        submitButton =Button(self.leftFrame, text ='check', fg='#212124',command =lambda:submit_ans(), \
                             state = DISABLED)
        exitButton.pack()
        nextButton.pack()
        submitButton.pack()

        self.window.mainloop()

    def ran_lett(self):
        letterOrd = random.randint(65,90)
        return chr(letterOrd)

    def ran_word(self, filename):
        with open(filename) as infile:
            wordList =tuple(infile.read().splitlines())
        infile.close()
        
        return random.choice(wordList).upper()

    def ran_ques(self):
        ques =random.randint(0,1)

        if ques == 0:
            quesType =self.gen_symLett_ques()
        else:
            quesType =self.gen_symWord_ques()
        return quesType
        
    def gen_symLett_ques(self):
        self.singChoiceSelect.pack()

        ans = self.ran_lett()
        symID = AURABET(65,65, ans)
        sym_print(symID, self.letterCanvas)
        
        choices =[]
        choices.append(ans)
        while len(choices) !=4:
            extra =self.ran_lett()
            if extra in choices:
                continue
            choices.append(extra)   
        random.shuffle(choices)
        
        for item in range(len(choices)):
            if choices[item] == ans:
                indexNum = item
            self.singChoiceSelect.insert(END, choices[item])
            self.singChoiceSelect.itemconfig(item)

        outfile = open('ANS', 'w')
        outfile.write('{}{}{}'.format(0,ans,str(indexNum)))
        outfile.close()
            
    def gen_symWord_ques(self):
        self.inputBox.pack()
        self.inputBoxANS.pack()
        word =self.ran_word('e_words').upper()

        pos =len(word)
        wid =160
        lett =30*pos
        gap =(pos-1)*5

        X = (wid-(lett+gap))/2
        for i in range(pos):
            symID = AURABET(X+i*35,65, word[i])
            sym_print(symID, self.letterCanvas)
            
        outfile = open('ANS','w')
        outfile.write('{}{}'.format(1,word))
        outfile.close()

    def gen_engWord_ques(self):
        pass
        
test1 = TestProgram()
test1.display()
