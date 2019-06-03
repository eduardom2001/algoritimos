velha=[['-','-','-'],['-','-','-'],['-','-','-']]

cont=0
a='O'
jogo=True
while jogo:
    l,c=map(int,input().split())
    cont+=1
    if velha[l][c]!='-':
        print('posicao invalida, repita')
        continue
    if a=='O':
        velha[l][c]='X'
        a='X'
    else:
        velha[l][c]='O'
        a='O'


    print('{0}{1}{2}\n{3}{4}{5}\n{6}{7}{8}'.format(velha[0][0],velha[0][1],velha[0][2],velha[1][0],velha[1][1],velha[1][2],velha[2][0],velha[2][1],velha[2][2]))


    if velha[0][0]==velha[0][1]==velha[0][2]=='X' or velha[1][0]==velha[1][1]==velha[1][2]=='X' or velha[2][0]==velha[2][1]==velha[2][2]=='X' or velha[0][0]==velha[1][0]==velha[2][0]=='X' or velha[0][1]==velha[1][1]==velha[2][1]=='X' or velha[0][2]==velha[1][2]==velha[2][2]=='X' or velha[0][0]==velha[1][1]==velha[2][2]=='X' or velha[0][2]==velha[1][1]==velha[2][0]=='X':
        print('X venceu')
        break
    elif velha[0][0]==velha[0][1]==velha[0][2]=='O' or velha[1][0]==velha[1][1]==velha[1][2]=='O' or velha[2][0]==velha[2][1]==velha[2][2]=='O' or velha[0][0]==velha[1][0]==velha[2][0]=='O' or velha[0][1]==velha[1][1]==velha[2][1]=='O' or velha[0][2]==velha[1][2]==velha[2][2]=='O' or velha[0][0]==velha[1][1]==velha[2][2]=='O' or velha[0][2]==velha[1][1]==velha[2][0]=='O':
        print('O venceu')
        break
    else:
        if cont==9:
            print('VELHA')
