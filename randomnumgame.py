from random import randint
def random_numgame():  
    com=randint(1,50)
    ch=0
    while ch<5:
        user=int(input("choose your choice between 1,50   :  "))
        if user<1 or user>50:
            print("Please be in the range ")
            continue
        if com>user:
            print("choose bigger number ")
        elif com<user:
            print("choose small number :")
        else:
            print("you won the match ")
            print(f"Computer choose : {com}")
            break
        ch+=1
        print(f'Remaining chances :{5-ch}')
    else:
        print("you loose :")
        print(f"Computer choose : {com}")
