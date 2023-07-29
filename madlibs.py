name=input('Name: ')
country=input('Country: ')
year=int(input('Year: '))
birth_year=int(input('Birth Year: '))

user_choice=input('Do you want to see the story for you:(y/n): ')

story=f'Hello {name}, Have a good day!\nReally happy to hear that you are from {country}. And also now you are a {year-birth_year} old citizen.\nThank you!'

if user_choice=='y':
    print (story)
elif user_choice=='n':
    print('Good Bye!')
    exit()
else:
    print('invalid input')
    exit()