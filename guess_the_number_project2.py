import random
top_of_range =input("type a number")
if top_of_range.isdigit():
    top_of_range= int(top_of_range)
    if top_of_range <= 0:
        print("enter number greater than 0")
        quit()
    else:
        print("please type number next time")
        quit()
    random_number = random.randint(0,top_of_range)

