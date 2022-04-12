# Variable data is a list of dictionaries.
# key:value pair being compared is follower_count
import random 
from game_data import data
from game_art import logo
from game_art import vs 

#print(random.choice(list(data)))
# assign random deictionary from data list to variable
item_a = random.choice(data)
item_b = random.choice(data)




def compare():
    choice = input("Who has more followers? Type 'A' or 'B':").upper 
    if choice == "A":
        A = int(item_a['follower_count'])
    elif choice == "B":
        B = int(item_b['follower_count'])
    highest = max(A,B)
    if choice >= highest:
        print("You're right")
    else:
        print("Sorry that's wrong")
    


   



final_score = []
print (logo)

print(f"Compare A: {item_a['name']}, a {item_a['description']}, from {item_a['country']}") 

print(vs) 
print(f"Against B: {item_b['name']}, a {item_b['description']}, from {item_b['country']}") 


compare()


