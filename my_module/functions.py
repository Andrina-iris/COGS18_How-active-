"""A collection of function for doing my project."""

"""
@author: Xiaoxuan(Andrina) Zhang
"""

import numpy as np
import pandas as pd

df = pd.read_csv(input("Please re-type your file's name in the box:)\n\n"))


def activate_and_intro():
    """
    Activation:
    
    In this function, 
    
    I want to welcome all of the users, with no functional usage. 
    
    ==========
    Intro:
    
    Example for the following box: 
    ----------
    COGS18_TestingData.csv
    (Please type in the name WITHOUT the quotes and WITH the ".csv"!)
    ----------
    
    The function would get a DataFrame(, which may not print out)
    
    and that's prepared for the later process of analyzing.
    """
    
    print("Hi, Welcome to 'How active?', a data analyzing tool! :)\n")
    


def how_active():
    """
    The main function 1 of my project.
    
    In the first part of the function, 
    
    I will grab the two important columns out from the DataFrame and make a new Numpy array from them.
    
    With the loop, I should get two int values, which will be used in the next comparison function.
    """
    
    
    likes_col = df["Number of Likes"]
    out_in_col = df["Location"]
    
    arr = np.array([likes_col,out_in_col])
    
    likes_out = 0
    likes_in = 0
    count = 0
    
    for i in range(arr.shape[1]):
        
        if arr[1][i] == "Outdoor":
            likes_out += arr[0][i]
            
        elif arr[1][i] == "Indoor":
            likes_in += arr[0][i]
            
        return (likes_out,likes_in)

    
def more_likes():
    
    """
    The main function 2 of my project.
    
    In this function, 
    
    I want to compare "likes_out" and "likes_in" to give outcomes to this influencer.
    
    The output would be a string.
    """
    
    out_in_tuple = how_active()
    
        
    if out_in_tuple[0] >= out_in_tuple[1]:
        res = "Active side"
    else:
        res = "Inactive side"
        
    return res
