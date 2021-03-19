"""Classes used throughout project"""

"""
@author: Xiaoxuan(Andrina) Zhang
"""

class BestRegards():
    
    """
    Give thanks back to all participants who used my project code!
    """
    
    # Class attributes for objects of type BestRegards
    bye_best = "Thank you!"
    
    def __init__(self, bye):
        self.bye = bye
        self.thanks = "Thank you so much!"
    
    # Class methods for objects of type BestRegards
    def thanks(self, n_times=1):
        
        return self.thanks * n_times

# Calling my function
#last_call = BestRegards()
#adieu = last_call(bye = "Bye!")

def byebye():
    call_byebye = BestRegards(bye = "Bye!")
    print(call_byebye)