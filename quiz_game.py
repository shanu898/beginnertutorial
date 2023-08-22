print('Welcome to the quiz game!')
name=input('Enter your name: ')
choice=input(f'Hello {name}, Do you want to play(y/n)?: ')
points=0

if choice.isdigit():
    print('Invalid input')
else:
    if choice.lower()=='y':
        print("Let's play!")
        answer=input('What does stands for CPU? ')
        if answer.lower()=='central processing unit':
            print('Correct!')
            points+=1
        else:
            print('Wrong!')
        
        answer=input('What does stands for GPU? ')
        if answer.lower()=='graphical processing unit':
            print('Correct!')
            points+=1
        else:
            print('Wrong!')
            
        answer=input('What does stands for RAM? ')
        if answer.lower()=='random access memory':
            print('Correct!')
            points+=1
        else:
            print('Wrong!')
        print(f'{name} have earned {points}')
    if choice.lower()=='n':
        print('Good Bye!')
        exit()

    




    
    