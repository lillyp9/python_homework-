def make_hangman(secret_word):
    guesses = []
   
    def hangman_closure(letter):
        guesses.append(letter)
    
        display = []
    
        for character in secret_word:
            if character in guesses:
               display.append(character)
            else:
               display.append('_')
        print (display)
        if "_" not in display:
           return True
        else:
           return False
    return (hangman_closure)
           

#test
game = make_hangman("alphabet")
game("a")
game("l")
game("h")
    
             
   
    

        

        