w=str(input())
print('a\n'*30)
s=''
vivo=0
vencer=0
p=0

while vivo!=6:
    a=str(input('digite uma letra:'))
    a.lower()

    if a in w:
        y=''
        for i in range(0,len(w)):
            if w[i]==a:
                y+=a
                vencer+=1
            else:
                if p==0:
                    y+='_'
                else:
                    y+=s[i]
        s=y
        p=1
        print('a palavra é',y)
        print('erros:',vivo)
    else:
        if p==0:
            print('a palavra é','_'*len(w))
        else:
            print('a palavra é',y)
        vivo+=1
        print('erros:',vivo)


    if vivo==6:
        print('a palavra era',w)
        print('voce perdeu')
        break
    if vencer==len(w):
        print('voce venceu')
        break
