import logging

logger = logging.getLogger(__name__ + "_parameter_log")
logger.setLevel(logging.INFO)
logger.addHandler(logging.FileHandler("./decorator.log","a"))



def logger_decorator(func):
    def func_wrapper(*args, **kwargs):
        if not args:
           positional_log = "none"
        else:
           positional_log = args
           
        if not kwargs:
            keyword_log = "none"
        else:
            keyword_log = kwargs
            
        logger.log(logging.INFO, "function: " + func.__name__)
        logger.log(logging.INFO, "positional parameters: " + str(positional_log))
        logger.log(logging.INFO, "keyword parameters: " + str(keyword_log))
        
        result = func(*args, **kwargs)
        logger.log(logging.INFO, "return: " + str(result))
        return result
    return func_wrapper

    
        
            
       
      