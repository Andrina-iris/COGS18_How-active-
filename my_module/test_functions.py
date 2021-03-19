"""Test for my functions.

Note: because these are 'empty' functions (return None), here we just test
  that the functions execute, and return None, as expected.
"""

##

"""
@author: Xiaoxuan(Andrina) Zhang
"""


import my_module.functions
import my_module.classes

##
##

def test_get_file():
    
    """
    The fuction is for testing whether the '.csv' file has been imported correctly.
    
    This function will return a string if it's working normally.
    """
    
    assert my_module.functions.df is not None 
    assert(isinstance(my_module.functions.df.shape, tuple))
    
    print("DataFrame status: good!\n")
    
    
    
def test_how_active():
    
    """
    This is for testing whether the data grabbed from "how_active()" and "more_likes" are working in a right direction.
    
    This function will return two strings if it's working normally.
    """
    assert isinstance(my_module.functions.how_active(), tuple)
    assert isinstance(my_module.functions.more_likes(), str)
    
    print("Here is the status of the influencer: \nHe/She is relatively " + my_module.functions.more_likes() + "!\n")
    

def test_class():
    """
    The fuction is for testing whether the class can work normally.
    
    This function will return a string if it's working normally.
    """
    
    assert my_module.classes is not None
    assert isinstance(my_module.classes.BestRegards(bye = "Bye!").thanks, str)
    assert my_module.classes.BestRegards(bye = "Bye!").thanks == 'Thank you so much!'
    
    print("Classes are also good!")
    

print("Wish you a great Spring break!")