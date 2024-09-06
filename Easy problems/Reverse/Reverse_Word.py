def Reverse_Word(sentence):    
    sentence = sentence.split(' ')
    sentence = ' '.join(sentence[::-1])
    return sentence 

    pass


def main():
    sentence = input("Give me a sentence to scramble up! :")

    print(Reverse_Word(sentence))
    pass

if __name__=='__main__':
    main()
