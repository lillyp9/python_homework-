#Hello Function
def hello():
    return "Hello!"

#Greet function formatted string
def greet(name):
    return f"Hello, {name}!"
# print(greet("Alex"))

#Calculator 
def calc(a, b, operation="multiply"):
    if operation == "multiply":
        try:
            return a * b
        except TypeError:
            return "You can't multiply those values!"
    elif operation == "add":
        return a + b
    elif operation == "subtract":
        return a - b
    elif operation == "modulo":
        return a % b
    elif operation == "divide":
        try:
            return a / b
        except ZeroDivisionError:
            return "You can't divide by 0!"
    else:
        if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
            return "Invalid input: a and b must be numbers."
# print(calc(5,3,"multiply"))

#Data Type Conversion 
def data_type_conversion(value, target_type):
    try:
        if target_type == "int":
            return int(value)
        elif target_type == "float":
            return float(value)
        elif target_type == "str":
            return str(value)
        else:
            return f"Invalid target type: {target_type}."
    except (ValueError, TypeError):
        return f"You can't convert {value} into a {target_type}."
# print(data_type_conversion("123.45", "float"))

#Grade System 
def grade(*scores):
    try:
        if not scores:
            return "Invalid data was provided."
        for score in scores:
            if not isinstance(score, (int, float)):
                raise TypeError("Non-numeric value found")
        average = sum(scores) / len(scores)

        if average >= 90:
            return "A"
        elif average >= 80:
            return "B"
        elif average >= 70:
            return "C"
        elif average >= 60:
            return "D"
        else:
            return "F"
    except (TypeError, ValueError):
        return "Invalid data was provided."

#Use a For Loop 
def repeat(string, count):
    repeated_string = ""
    for _ in range(count):
        repeated_string += string
    return repeated_string

# print(repeat("Hi! ", 3))    

#Student Scores 
def student_scores(option, **scores):

    total = sum(scores.values())
    count = len(scores)
    average = total/count 
    best_score = 0
    best_student = ""
    if option == "mean":
        return average
    elif option == "best":
        for student, score in scores.items():
        
            average = 0
            if score > best_score:
                best_score = score
                best_student = student
        return best_student

          
print(student_scores("mean", Alice=85, Bob=92, Charlie=78))

#Titleize String and operation List 
def titleize(string):
    words = string.split()
    list_of_small_words = ['and', 'or', 'the', 'in','at', 'to', 'for', 'a', 'an']
    new_set = []
    is_first_word = True
    complete_word = ""
    for word in words:
        
        if word.lower() in list_of_small_words and  is_first_word == False:
            new_set.append(word.lower())
        else:
            new_set.append(word.capitalize())

        is_first_word = False
    
    for word in new_set:
        complete_word += word + " "

    return complete_word.strip()
        

    # return ' '.join(titleize_words)
print(titleize("After On"))

#Hangman with more string operation 
def hangman(secret,guess):
    display_word = ""
    for letter in secret:
        if letter.lower() in guess.lower():
            display_word += letter
        else:
            display_word += "_"
    return display_word
print(hangman("Programming", "gmr"))
  
#Pig Latin 
def pig_latin(string):
    vowels = "aeiou"
    words = ""
    consonants_chunck = "bcdfghjklmnpqrstvwxyz"
    for first_word in string.split():
        if first_word[0] in vowels:
            words += first_word + "ay "
        elif first_word.startswith("qu"):
            words += first_word[2:] + "quay "
        else:
            counter = 0
            for letter in first_word:
                if letter not in vowels:
                 counter = counter + 1
                else:
                    break
            if first_word[counter-1] == "q" and first_word[counter] == "u":
                counter = counter + 1
            rest_of_word = first_word[counter:]
            consonants_chunck = first_word[:counter]
            words += rest_of_word + consonants_chunck + "ay "
    return words.strip()
            
  
                 
                
              
        
          
     