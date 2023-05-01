# Ask a user to choose whether to make each letter or word of the sentence to alternate between upper and lowercase.
while True:
    option = str(input("Enter option 1 or option 2 to execute: (1/2)"))

    # 1. each character to alternate between upper and lower case.
    if option == "1":
        sentence = str(input("Enter your sentence to begin:"))
        final_sentence = ""
        for i in range(len(sentence)):
            if i % 2 == 0:
                final_sentence += sentence[i].upper()
            
            else:
                final_sentence += sentence[i].lower()

        print(final_sentence)
        break


    # 2. each word to alternate between upper and lower case.
    elif option == "2":

        sentence = (input("Enter your sentence to begin:"))
        new = sentence.split()

        for i in range(len(new)):           
            if i % 2 == 0:
                new[i] = new[i].lower()

            else:
                new[i] = new[i].upper()

            final = " ".join(new)
        
        print(final)
        break
        

    else:
        print("Invalid option, Enter again!")
    

