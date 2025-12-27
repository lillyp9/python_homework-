from log_decorator import logger_decorator



@logger_decorator
def weather():
    return "Its sleet"
weather()

@logger_decorator
def multiple_number(a, b):
    return(a * b)
multiple_number(10, 8)

@logger_decorator
def puppy_description(name=None, age=None):
    return f"{name} is {age} years old."
puppy_description(name="Kalina", age=10)




    
      
 
