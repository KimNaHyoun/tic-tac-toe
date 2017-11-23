from tkinter import *

def checked(i) :
      global player 
      button = list[i] 
      
      if button["text"] != "     " : 
            return 
      button["text"] = player  
      button["bg"] = "yellow" 

      if player == "X" : 
            player = "O"
            button["bg"] = "yellow"
      else : 
            player = "X"
            button["bg"] = "lightgreen"
  
      r=i//3 
      c=i%3 
        
      '''O의승리'''
      if list[(r*3)]["text"] == list[(r*3) + 1]["text"] == list[(r*3) + 2]["text"] == "O" : 
             winner_O()             
      # 가로 3개가 일치할 경우
      elif list[c]["text"] == list[c + 3]["text"] == list[c + 6]["text"] == "O": 
             winner_O()             
      # 세로 3개가 일치할 경우
      elif list[0]["text"] == list[4]["text"] == list[8]["text"]  == "O": 
             winner_O() 
      elif list[2]["text"] == list[4]["text"] == list[6]["text"] =="O": 
             winner_O()       
      # 대각선으로 일치할 경우
      '''X의 승리'''
      elif list[(r*3)]["text"] == list[(r*3) + 1]["text"] == list[(r*3) + 2]["text"] == "X": 
             winner_X()           
      # 가로 3개가 일치할 경우
      elif list[c]["text"] == list[c + 3]["text"] == list[c + 6]["text"] == "X" : 
             winner_X() 
       # 세로 3개가 일치할 경우
      elif list[0]["text"] == list[4]["text"] == list[8]["text"] == "X": 
             winner_X() 
      elif list[2]["text"] == list[4]["text"] == list[6]["text"] =="X": 
             winner_X() 
      # 대각선으로 일치할 경우

      
'''winner정의'''       
def winner_O() : 
       msg = Message(window, text="player0 의 승리") 
       msg.grid(row=3, column=0) 

 
def winner_X() : 
       msg = Message(window, text="playerX 의 승리") 
       msg.grid(row=3, column=0) 
      
       
window = Tk() 
player = "X" 
list= [] 

for i in range(9) : 
      b = Button(window, text="     ", command=lambda k=i: checked(k)) 
      b.grid(row=i//3, column=i%3) 
      list.append(b)
 
window.mainloop() 
