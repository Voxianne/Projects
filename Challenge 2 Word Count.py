#Challenge 2 Word Count

Sentence = input("Please write about yourself but with no more than 50 words: ")
counter = 1
for words in Sentence:
    if words == ' ':
        counter = counter + 1
    if counter > 50:
        print()
print('The words in the sentence are ', counter , '!' )

#An another way around it is:
#   Sentence = input("Please write about yourself but with no more than 50 words: ")
#   counter = len(Sentence.split())
#   if counter > 50:
#        print('Hey!!You surpassed the maximun number of words allowed!The program will now exit! Baka ja nai!')
#   else:
#        print('The words in the sentence are ', counter , '!' )