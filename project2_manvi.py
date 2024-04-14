import random
choices=['R','P','S']
input('Hlw...Lets play rock,paper or scissors game :),Press Enter to continue')
input('RULES:Write Rock as R,Paper as P,Scissors as S...Write "E" to exit the Game...Write "SCORE" to check the score :)')
player=False
cpu_score=0
player_score=0
tie_score=0
playername=input('Enter your name:')
while True:
    player=input('Choose-->:')
    computer=random.choice(choices)
    if player==computer:
        print('Tie!!!...')
        tie_score+=1
    elif player=='R':
        if computer=='P':
            print(f'Oops {playername},You lose :(...Try again')
            cpu_score+=1
        else:
            print(f'Yayy {playername},You win :D...')
            player_score+=1

    elif player=='P':
        if computer=='S':
            print(f'Oops {playername},You lose :(...Try again')
            cpu_score+=1
        else:
            print(f'Yayy {playername},You win :D...')
            player_score+=1

    elif player=='S':
        if computer=='R':
            print(f'Oops {playername},You lose :(...Try again')
            cpu_score+=1
        else:
            print(f'Yayy {playername},You win :D...')
            player_score+=1

    elif player=='SCORE':
        print('Final Score:')
        print(f'CPU:{cpu_score}')
        print(f'{playername}:{player_score}')
        print(f'TIE:{tie_score}')
    elif player=='E':
        break
