import random ,sys
print("ROCK,PAPAER,SCISSORS")
ties=0
wins=0
losses=0
while True:
    print('%s wins,%s losses,%s ties(wins,losses,ties)')
    while True:
        print('enter your move r(rock),paper(p),(s)cissors or q(uit)')
        playermove=input()
        if playermove=='q':
            sys.exit()
        if playermove=='r' or playermove=='p' or playermove=='s':
            break
        print('type one of r,p,s,or q')
    if playermove=='r':
        print('ROCK versus..')
    elif playermove=='s':
        print('SCISSORS versus..')
    elif playermove=='p':
        print('PAPER versus..')
    randomnumber=random.randint(1,3)
    if randomnumber==1:
        computermove='r'
        print('ROCK')
    if randomnumber==2:
        computermove='p'
        print('PAPER')
    if randomnumber==3:
        computermove='s'
        print('SCISSORS')
    if computermove==playermove:
        print('it is a tie')
        ties=ties+1
    elif playermove=='r' and computermove=='s':
        print('you win..!')
        wins=wins+1
    elif playermove=='p' and computermove=='r':
        print('you win..!')
        wins=wins+1
    elif playermove=='s' and computermove=='p':
        print('you win.!')
        wins=wins+1
    elif playermove=='r' and computermove=='p':
        print('you lose!')
        losses=losses+1
    elif playermove=='p' and computermove=='s':
        print('you lose!')
        losses=losses+1
    elif playermove=='s' and computermove=='r':
        print('you lose!')
        losses=losses+1
print(losses,wins,ties)