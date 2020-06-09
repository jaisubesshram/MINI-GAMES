from tkinter import*
tictactoe=Tk()
tictactoe.title("TIC TAC TOE")
turn=0
players=['X','O']
game=[0,0,0,0,0,0,0,0,0]
def start_game():

    title_label=Label(tictactoe,text=" The   XO   Game ").grid(row=0,column=0,columnspan=3,padx=10,pady=10)
    
    player_label=Label(tictactoe,text="PLAYER '"+players[turn%2]+"' turn",border=5).grid(row=1,column=0,columnspan=3,padx=10,pady=10)
    

    def button_click(num):
        global turn,players
        if(num==1):
            button_1=Button(tictactoe,text=players[turn%2],padx=20,pady=20,bg="white",fg="black").grid(row=2,column=0)
            player_label=Label(tictactoe,text="PLAYER '"+players[(turn+1)%2]+"' turn").grid(row=1,column=0,columnspan=3,padx=10,pady=10)
            game[num-1]=players[turn%2]
            check()
        elif(num==2):
            button_2=Button(tictactoe,text=players[turn%2],padx=20,pady=20,bg="white",fg="black").grid(row=2,column=1)
            player_label=Label(tictactoe,text="PLAYER '"+players[(turn+1)%2]+"' turn").grid(row=1,column=0,columnspan=3,padx=10,pady=10)
            game[num-1]=players[turn%2]
            check()
        elif(num==3):
            button_3=Button(tictactoe,text=players[turn%2],padx=20,pady=20,bg="white",fg="black").grid(row=2,column=2)
            player_label=Label(tictactoe,text="PLAYER '"+players[(turn+1)%2]+"' turn").grid(row=1,column=0,columnspan=3,padx=10,pady=10)
            game[num-1]=players[turn%2]
            check()
            
        elif(num==4):
            button_4=Button(tictactoe,text=players[turn%2],padx=20,pady=20,bg="white",fg="black").grid(row=3,column=0)
            player_label=Label(tictactoe,text="PLAYER '"+players[(turn+1)%2]+"' turn").grid(row=1,column=0,columnspan=3,padx=10,pady=10)
            game[num-1]=players[turn%2]
            check()
        elif(num==5):
            button_5=Button(tictactoe,text=players[turn%2],padx=20,pady=20,bg="white",fg="black").grid(row=3,column=1)
            player_label=Label(tictactoe,text="PLAYER '"+players[(turn+1)%2]+"' turn").grid(row=1,column=0,columnspan=3,padx=10,pady=10)
            game[num-1]=players[turn%2]
            check()
        elif(num==6):
            button_6=Button(tictactoe,text=players[turn%2],padx=20,pady=20,bg="white",fg="black").grid(row=3,column=2)
            player_label=Label(tictactoe,text="PLAYER '"+players[(turn+1)%2]+"' turn").grid(row=1,column=0,columnspan=3,padx=10,pady=10)
            game[num-1]=players[turn%2]
            check()
            
        elif(num==7):
            button_7=Button(tictactoe,text=players[turn%2],padx=20,pady=20,bg="white",fg="black").grid(row=4,column=0)
            player_label=Label(tictactoe,text="PLAYER '"+players[(turn+1)%2]+"' turn").grid(row=1,column=0,columnspan=3,padx=10,pady=10)
            game[num-1]=players[turn%2]
            check()
        elif(num==8):
            button_8=Button(tictactoe,text=players[turn%2],padx=20,pady=20,bg="white",fg="black").grid(row=4,column=1)
            player_label=Label(tictactoe,text="PLAYER '"+players[(turn+1)%2]+"' turn").grid(row=1,column=0,columnspan=3,padx=10,pady=10)
            game[num-1]=players[turn%2]
            check()
        elif(num==9):
            button_9=Button(tictactoe,text=players[turn%2],padx=20,pady=20,bg="white",fg="black").grid(row=4,column=2)
            player_label=Label(tictactoe,text="PLAYER '"+players[(turn+1)%2]+"' turn").grid(row=1,column=0,columnspan=3,padx=10,pady=10)
            game[num-1]=players[turn%2]
            check()

        turn+=1
        
        
    def create_buttons():
        button_1=Button(tictactoe,padx=20,pady=20,command=lambda:button_click(1)).grid(row=2,column=0)
        button_2=Button(tictactoe,padx=20,pady=20,command=lambda:button_click(2)).grid(row=2,column=1)
        button_3=Button(tictactoe,padx=20,pady=20,command=lambda:button_click(3)).grid(row=2,column=2)
        button_4=Button(tictactoe,padx=20,pady=20,command=lambda:button_click(4)).grid(row=3,column=0)
        button_5=Button(tictactoe,padx=20,pady=20,command=lambda:button_click(5)).grid(row=3,column=1)
        button_6=Button(tictactoe,padx=20,pady=20,command=lambda:button_click(6)).grid(row=3,column=2)
        button_7=Button(tictactoe,padx=20,pady=20,command=lambda:button_click(7)).grid(row=4,column=0)
        button_8=Button(tictactoe,padx=20,pady=20,command=lambda:button_click(8)).grid(row=4,column=1)
        button_9=Button(tictactoe,padx=20,pady=20,command=lambda:button_click(9)).grid(row=4,column=2)
        global game,turn
        game=[0,0,0,0,0,0,0,0,0]
        turn=0
        
    create_buttons()
    new_game=Button(tictactoe,text="New Game!",bg="white",fg="black",command=create_buttons).grid(row=5,column=0,columnspan=3,padx=10,pady=10)
    exit_game=Button(tictactoe,text="EXIT GAME",bg="red",fg="black",command=exit).grid(row=6,column=0,columnspan=3,padx=10,pady=10)

    def check():
        global turn
        if(turn==8):
            win_label=Label(tictactoe,text="The Game Draws!",bg="white",fg="blue").grid(row=2,column=0,rowspan=3,columnspan=3)
        for i in range(0,9,3):
            if(game[i]!=0 and game[i]==game[i+1]and game[i]==game[i+2]):
                win_label=Label(tictactoe,text="Player  "+str(game[i])+"  WINS!!",bg="white",fg="blue").grid(row=2,column=0,rowspan=3,columnspan=3)
        for i in range(0,3,1):
            if(game[i]!=0 and game[i]==game[i+3]and game[i]==game[i+6]):
                win_label=Label(tictactoe,text="Player  "+str(game[i])+"  WINS!!",bg="white",fg="blue").grid(row=2,column=0,rowspan=3,columnspan=3)
        if((game[0]!=0 and game[0]==game[4]and game[0]==game[8])):
                win_label=Label(tictactoe,text="Player  "+str(game[0])+"  WINS!!",bg="white",fg="blue").grid(row=2,column=0,rowspan=3,columnspan=3)
        if((game[2]!=0 and game[2]==game[4]and game[2]==game[6])):
                win_label=Label(tictactoe,text="Player  "+str(game[2])+"  WINS!!",bg="white",fg="blue").grid(row=2,column=0,rowspan=3,columnspan=3)
        


start_game()
tictactoe.mainloop()
