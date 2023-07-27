import random

word_list=['apple','house','country','university','design']

random_word=random.choice(word_list)
#print(random_word)

#print(random_word[0])
#print(len(random_word))

letter_count=len(random_word)
first_letter=random_word[0]
chances=letter_count+2

print(f'You have to guess the word with {letter_count} letters and starting with {first_letter.upper()}\nYOU HAVE {chances} CHANCES')

i=0
guessing_word=''
j=0
while True:
    if i<=chances:
        if j<letter_count:
            user_input=input(f'Enter the letter for position {j+1}: ')
        else:
            print('Word guessed')
            break
        if(random_word[j]==user_input):
            #print(random_word[j])
            guessing_word+=user_input
            print(guessing_word)
            j+=1
        else:
            print('wrong')
            print(guessing_word)
        i+=1
    else:
        print('You have exceeded the chances')
        exit()    
        
    