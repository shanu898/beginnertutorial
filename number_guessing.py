import random

print('********NUMBER GUESSING*********')

while True:
    user_choice=input('Do you want to play(y/n): ')
    
    if user_choice=='y':
        try:
            lower_bound=int(input('Enter the lower value: '))
            upper_bound=int(input('Enter the higher value: '))

            system_number=random.randint(lower_bound,upper_bound)
           
            attempt_count=1

            while True:
                if attempt_count<=5:
                    user_number=int(input('Enter your guessing number: '))
                    if user_number==system_number:
                        print("you guessed the number in {count} attempts".format(count=attempt_count))
                        break
                    else:
                        print('Try again')
                        attempt_count+=1
                else:
                    print('You have exceeded the maximum number of attempts')
                    break
        except:
            print('You have entered an invalid character')
    else:
        print('Good Bye!')
        exit()