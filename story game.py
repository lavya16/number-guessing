print("hi")
print("what's you're name")
name = input ("Enter Name")
print(" hello " + name )
print("how old are you")
age = int(input())
if age < 18 : 
    print(" you are not old enough to play " + name + " this game ")
else : 
    print(" you are old enough " + name)   
    
Want_to_play = input(print("do you wanna play (yes/no)")).lower()
if Want_to_play == "yes" :
    print("you wake up in the middle of a forest in nowhere and you need to excape from the forest. You started waking and found two roads, now which way do you want to go  ") 
    
    left_or_right = input(print(" left or right ")).lower()
    if left_or_right == "left" :
        print(" you've reached to a river and you found an old man dieing but there is also a boat which is going to drown in few second. what you are going to choose   ")
        
        Saving_the_man_or_saving_the_boat = input(print(" old man or the boat")).lower()
        if Saving_the_man_or_saving_the_boat == "boat" : 
            print("you've got survival instinct champ")
            print("now you've reached a grassland and across the grassland their is a village. Now you could walk or you could catch a horse a ride through it")
             
            
            catch_the_horse_or_walk = input(print(" horse or walk ")).lower()
            if catch_the_horse_or_walk == "walk" :
                print("after walking for an hour you got unconscious but villagers saved you ")  
                print("congrats you won")
            else : 
                   print("you got beaten up by horse and you died. better luck next time")
         
        else : 
                print("you saved the old man but you lose the boat. You lost")
                print("beter luck next time")
     
    else :
        print("you got stunk by a snake and you died. You lost")
        print("better luck next time")

else : 
    print("maybe next time")
                