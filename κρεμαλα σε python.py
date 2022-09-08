import random


num_of_pl=int(input('How many players?'))
next_round_num_of_pl=0
players=[]
for x in range(num_of_pl):
    print('Give name of player')
    players.append(input())
    print('Hello,'+players[x]+'.Welcome to the game.')

print('Let the game begin!')


"""PROSORINO GIA DOKIMES"""
wordlist=["αμφιεση","αδερφοσ","αποκλιση","βαρυτιμοσ","βασιλευω","βουισμα","γλυκερινη","γνωριμοσ","δισταζω","διχρωμοσ","εναποθετω","εναστρο","ζωηροσ","ζυμωση","θορυβω","θρανιο","θρεψη","ισοβαθμω","ιεροσυνη","κλυσμα","κοινωφελησ","λουκι","λογχη","λομπι","μακροσκελη","μαχητικοσ","νιπτηρασ","νομαρχησ","ξαγρυπνοσ","ξαφνικοσ","ονυχασ","οπερα","οξυφωνη","πουρεσ","παρελκυση","ρωμιοσυνη","ρωμαλεοσ","σαθρο","σαγονι","ταμπλο","ταμειο","υακινθοσ","υγεια","φαβορι","φανεροσ","χαλιφησ","χαζευω","ψεμα","ωχροσ","ωφελιμοσ"]
alphabet=['α','β','γ','δ','ε','ζ','η','θ','ι','κ','λ','μ','ν','ξ','ο','π','ρ','σ','τ','υ','φ','χ','ψ','ω']
used_words=[]


def right_guess_func(lsword,newls_word,pl_guess):
   for x in lsword:
       if pl_guess==x:
           s=lsword.index(x)
           newls_word[s]=x
           for x in newls_word:
               print(x,end=' ')

next_round_pl=[]


for x in range(num_of_pl):#edw 8a prepei na allazei paikth
    wrong_let=5



    print('Your turn:'+players[x])
    print('Remember! You have '+str(wrong_let)+' wrong guesses! When you guess 6 letters wrong: GAME IS OVER')
    current_player=players[x]


    word_is_used=True
    temp_secret_word=random.choice(wordlist)
    while word_is_used==True:
        if temp_secret_word in used_words:
            temp_secret_word=random.choise(wordlist)
        else:
            word_is_used=False
            secret_word=temp_secret_word
            used_words+=temp_secret_word



    lsword=list(secret_word)
    newls_word=list(str(len(lsword)*'_'))



    print('The word you have to guess is:'+str(len(secret_word)*'_ '))
    print('Give a letter')


    pl_guess=input()

    while wrong_let>0:


        not_a_letter=True
        for x in alphabet:
            if x==pl_guess:
                not_a_letter=False

        while not_a_letter==True:
            print('This is not a letter! Try again!')
            pl_guess=input()
            for x in alphabet:
                if x==pl_guess:
                    not_a_letter=False



        right_guess=False
        for x in range(len(secret_word)):
            if pl_guess==secret_word[x]:
                right_guess=True
        if right_guess==True:

            print('Right guess! The word you have to guess now is:')
            str(right_guess_func(lsword,newls_word,pl_guess))
            completed_letters=0
            for i in range(len(newls_word)):
                if secret_word[i] == newls_word[i]:
                    completed_letters+=1
            if completed_letters==len(secret_word):
                print('.  Oh! Congratulations! The word is completed!')
                next_round_pl += current_player
                next_round_num_of_pl+=1
                winner=current_player
                break#edw elegxetai an me ayto to grammma o paikths kerdise ton gyro



            print('Give another letter!')
            pl_guess=input()
        elif right_guess==False and wrong_let==5:
            wrong_let=4
            print("  |---------|")
            print("  |         Ο")
            print("  |")
            print("  |")
            print("  |")
            print("  |")
            print("  |")
            print('You still have 4 wrong guesses!')
            print('The word you have to guess is:')
            print(' '.join(newls_word))
            print('Give a letter!')
            pl_guess=input()
        elif right_guess==False and wrong_let==4:
            wrong_let=3
            print("  |---------|")
            print("  |         Ο")
            print("  |        /|\ ")
            print("  |")
            print("  |")
            print("  |")
            print("  |")
            print('You still have 3 wrong guesses!')
            print('The word you have to guess is:')
            print(' '.join(newls_word))
            print('Give a letter!')
            pl_guess=input()
        elif right_guess==False and wrong_let==3:
            wrong_let=2
            print("  |---------|")
            print("  |         Ο")
            print("  |        /|\ ")
            print("  |         | ")
            print("  |")
            print("  |")
            print("  |")
            print('You still have 2 wrong guesses!')
            print('The word you have to guess is:')
            print(' '.join(newls_word))
            print('Give a letter!')
            pl_guess=input()
        elif right_guess==False and wrong_let==2:
            wrong_let=1
            print("  |---------|")
            print("  |         Ο")
            print("  |        /|\ ")
            print("  |         | ")
            print("  |       _/ \_")
            print("  |")
            print("  |")
            print('You still have 1 wrong guess!')
            print('The word you have to guess is:')
            print(' '.join(newls_word))
            print('Give a letter!')
            pl_guess=input()
        else:
            wrong_let=0
            print("  |---------|")
            print("  |         Ο")
            print("  |        /|\ ")
            print("  |         | ")
            print("  |       _/ \_")
            print("  |      # # # #")
            print("  |       fire  ")
            print('GAME OVER')
            print('The word was:')
            print(str(secret_word))



while next_round_num_of_pl!=0 and next_round_num_of_pl!=1:#GIA KATHE EPOMENO GYRO
    temp_num_of_pl=next_round_num_of_pl
    for x in range(temp_num_of_pl):#edw 8a prepei na allazei paikth
        wrong_let=5



        print('Your turn:'+next_round_pl[x])
        print('Remember! You have '+str(wrong_let)+' wrong guesses! When you guess 6 letters wrong: GAME IS OVER')
        current_player=next_round_pl[x]



        word_is_used=True
        temp_secret_word=random.choice(wordlist)
        while word_is_used==True:
            if temp_secret_word in used_words:
                temp_secret_word=random.choise(wordlist)
            else:
                word_is_used=False
                secret_word=temp_secret_word
                used_words+=temp_secret_word



        lsword=list(secret_word)
        newls_word=list(str(len(lsword)*'_'))



        print('The word you have to guess is:'+str(len(secret_word)*'_ '))
        print('Give a letter')


        pl_guess=input()

        while wrong_let>0:


            not_a_letter=True
            for x in alphabet:
                if x==pl_guess:
                    not_a_letter=False

            while not_a_letter==True:
                print('This is not a letter! Try again!')
                pl_guess=input()
                for x in alphabet:
                    if x==pl_guess:
                        not_a_letter=False



            right_guess=False
            for x in range(len(secret_word)):
                if pl_guess==secret_word[x]:
                    right_guess=True
            if right_guess==True:

                print('Right guess! The word you have to guess now is:')
                str(right_guess_func(lsword,newls_word,pl_guess))
                completed_letters=0
                for i in range(len(newls_word)):
                    if secret_word[i] == newls_word[i]:
                        completed_letters+=1
                if completed_letters==len(secret_word):
                    print('.  Oh! Congratulations! The word is completed!')
                    winner=current_player
                    break#edw elegxetai an me ayto to grammma o paikths kerdise ton gyro



                print('Give another letter!')
                pl_guess=input()
            elif right_guess==False and wrong_let==5:
                wrong_let=4
                print("  |---------|")
                print("  |         Ο")
                print("  |")
                print("  |")
                print("  |")
                print("  |")
                print("  |")
                print('You still have 4 wrong guesses!')
                print('The word you have to guess is:')
                print(' '.join(newls_word))
                print('Give a letter!')
                pl_guess=input()
            elif right_guess==False and wrong_let==4:
                wrong_let=3
                print("  |---------|")
                print("  |         Ο")
                print("  |        /|\ ")
                print("  |")
                print("  |")
                print("  |")
                print("  |")
                print('You still have 3 wrong guesses!')
                print('The word you have to guess is:')
                print(' '.join(newls_word))
                print('Give a letter!')
                pl_guess=input()
            elif right_guess==False and wrong_let==3:
                wrong_let=2
                print("  |---------|")
                print("  |         Ο")
                print("  |        /|\ ")
                print("  |         | ")
                print("  |")
                print("  |")
                print("  |")
                print('You still have 2 wrong guesses!')
                print('The word you have to guess is:')
                print(' '.join(newls_word))
                print('Give a letter!')
                pl_guess=input()
            elif right_guess==False and wrong_let==2:
                wrong_let=1
                print("  |---------|")
                print("  |         Ο")
                print("  |        /|\ ")
                print("  |         | ")
                print("  |       _/ \_")
                print("  |")
                print("  |")
                print('You still have 1 wrong guess!')
                print('The word you have to guess is:')
                print(' '.join(newls_word))
                print('Give a letter!')
                pl_guess=input()
            else:
                wrong_let=0
                print("  |---------|")
                print("  |         Ο")
                print("  |        /|\ ")
                print("  |         | ")
                print("  |       _/ \_")
                print("  |      # # # #")
                print("  |       fire  ")
                print('GAME OVER')
                print('The word was:')
                print(str(secret_word))
                next_round_pl.remove(current_player)
                next_round_num_of_pl-=1


if next_round_num_of_pl==1:
    print('GAME IS OVER! WINNER IS '+ str(winner))

else:
    print('GAME IS OVER! NO WINNER :(')










