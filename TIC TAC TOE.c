/******************************************************************************

Welcome to GDB Online.
GDB online is an online compiler and debugger tool for C, C++, Python, PHP, Ruby, 
C#, VB, Perl, Swift, Prolog, Javascript, Pascal, HTML, CSS, JS
Code, Compile, Run and Debug online from anywhere in world.

*******************************************************************************/
#include <stdio.h>
#include <stdlib.h>
    int position_choice;
    int* position_values;
    
    
int table_fill(int position_choice,int player)
{   
    if((position_choice>9)||(position_choice<1))
    {
        printf("Please Enter A Valid Position!!\n");
        return 0;
    }
    else
    {
    if(position_values[position_choice-1]==32)
    {
        if(player==1)
        {
            position_values[position_choice-1]=88;
        }
        else
        {
            position_values[position_choice-1]=79;
        }
    return 1;
    }
    else
    {
        printf("The position that you selected is already filled!\nChoose another number.\nAgain, Its ");
        return 0;
    }
    }
}

void display()
{   
    printf("Game Table:\t\tPosition Table:\n ____________\t\t____________\n");
    
    for(int i=0;i<9;i+=3,printf("|___|___|___|\t\t|___|___|___|\n"))
    {
        printf("| %c | %c | %c |\t\t| %d | %d | %d |\n",position_values[i],position_values[i+1],position_values[i+2],i+1,i+2,i+3);
    }   
}
void play_x()
{
    printf("PLAYER 1 's TURN\nChoose position to place 'X' : ");
    scanf(" %d",&position_choice);
    if(table_fill(position_choice,1)==0)
    {
        play_x();
    }
}
void play_o()
{
    printf("PLAYER 2 's TURN\nChoose position to place 'O' : ");
    scanf(" %d",&position_choice);
    if(table_fill(position_choice,0)==0)
    {
        play_o();
    }
}
int game_termination(int* ar)
{   for(int i=0;i<9;i+=3)
    {
        if(ar[i]!=32&&ar[i]==ar[i+1]&&ar[i]==ar[i+2])
            return ar[i];
    }
    for(int i=0;i<9;i++)
    {
        if(ar[i]!=32&&ar[i]==ar[i+3]&&ar[i]==ar[i+6])
            return ar[i];
    }
    for(int i=0;i<3;i+=2)
    {
        if(ar[i]!=32&&ar[i]==ar[i+4]&&ar[i]==ar[i+8])
            return ar[i];
    }
    
    return 0;
    
}

void game()
{   int turn;
    position_values=(int*)malloc(9*sizeof(int));
    for(int i=0;i<9;i++)
    {
        position_values[i]=32;
    }
    display();
    for(turn=8;turn>0;turn--,printf("\n"),display())
    {
     
     if(turn%2==0)
     {
         play_x();
     }
     else
     {
         play_o();
     }
     int end;
     if(turn<5)
     {
      if(end=game_termination(position_values))
            {
                if(end==88)
                {
                    display();
                    printf("\n\t*** PLAYER 1 WINS THE GAME!!! ***\n");
                    break;
                }
                else
                {   
                    display();
                    printf("\n\t*** PLAYER 2 WINS THE GAME!!! ***\n");
                    break;
                }
            }
     }
    }
    
    if(turn==0)
        {
            printf("\n\t*** THE GAME HAS DRAWN!! ***\n");
        }
     
    
    
}

int main()
{   
    char choice;
    printf("\t\t\t```TIC TAC TOE ```\n\n");
    while(1)
    {
    printf("Play Game?? (Y/N)\n");
    scanf(" %c",&choice);
    switch (choice)
    {
        case 'y':
                {
                    printf("Lets Start the Game!\n");
                    game();
                    break;
                }
        case 'Y':
                {
                    printf("Lets Start the Game!\n");
                    game(); 
                    break;
                }
        case 'n':
                {
                    printf("\t\tThank you! Have a Great day!\n ");
                    exit (0);
                }
        case 'N': 
                {
                    printf("\t\tThank you! Have a Great day!\n ");
                    exit (0);
                }
        default: 
                {
                    printf("Enter A Valid Choice.\n");
                }
        }
    }
    
    return 0;
}








