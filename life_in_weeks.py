# Let's say the average lifespan of Gen Z is 90 years.
# This code calculates how many weeks you have left to live based on your current age.

def life_in_weeks(age):
    if 90>=age:
        a = age*52 #weeks lived
        b = 4680-a #weeks left
        print(f"You have {b} weeks left! lol.")
    else:
        print("please enter a valid age between 0 to 90.")
#try it out with your age!
life_in_weeks(18)
