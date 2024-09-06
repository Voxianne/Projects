Sentence = input('Please give me a sentence to work with: ')
counter = 0
for letters in Sentence:
    if (letters =='a' or letters == 'e' or letters == 'i' or letters == 'o' or letters =='u' or letters =='A' or letters == 'E' or letters=='O' or letters =='I' or letters=='U'):
        counter = counter + 1
print('There are ',counter,' vowels in the sentence!')


# An another way is:
#   vowels = ['a','e','i','o','u','A','E','I','O','U']
#   counter1 = 0
#   for letters in Sentence:
#       for letters in vowels:
#            counter1 = counter1 + 1
#   print('There are ', counter, ' vowels in the sentence!')
