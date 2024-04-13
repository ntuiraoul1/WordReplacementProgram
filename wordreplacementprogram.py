sentence = input ('Enter your sentence ')
print('Your sentence is: '+ sentence)
word1 = input('Enter the word to be replaced: ')
word2 = input('Enter the word to replace: ')

key = sentence.replace(word1, word2)

print(key)

# We use the python replace method so as to accomplish this.

# We start by asking the user to input his sentence
# Then we ask him which word he wants to replace and 
# also the word which will replace it, once these 2 
# informations are known, we use the replace method 
# on the sentence and then store the result in a 
# variable and then print the outcome 
