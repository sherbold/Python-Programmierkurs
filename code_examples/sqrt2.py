print("intializing module sqrt2...")
def my_sqrt(x):
    """Returns the square root of x"""
    guess = 1
    while(abs(guess*guess-x)>0.0001):
        guess = (1/2)*(guess+x/guess)
    return guess

answer = 42

print("initialization finished!")