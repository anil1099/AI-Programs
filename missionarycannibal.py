missionary=int(input("Enter the number of missionary "))
cannibal=int(input("Enter the Number of cannibal "))
#To win this, if the missionary are to the next side without eaten
place2=[0,0]
moving_missionary=missionary
moving_cannibal=cannibal
rules_used={}
count=0
while place2[0]!=missionary or place2[1]!= cannibal:
    if moving_cannibal<0 or moving_missionary<0 or moving_cannibal>3 or moving_missionary>3:
        break
    game_rule=int(input("Enter the rule to use"))
    #moving from place 1 to place 2
    if game_rule==1: #1M 1C
        moving_missionary-=1
        moving_cannibal-=1
        place2[0]+=1
        place2[1]+=1
    elif game_rule==2: #2M
        moving_missionary-=2
        place2[0]+=2
    elif game_rule==3: #2C
        moving_cannibal-=2
        place2[1]+=2
    #Moving from place 2 to place 1        
    elif game_rule==4: #1M
        moving_missionary-=1
    elif game_rule==5: # 1C
        moving_cannibal+=1
        place2[1]-=1

    elif game_rule==6: #1M 1C
        moving_missionary+=1
        moving_cannibal+=1
        place2[0]-=1
        place2[1]-=1

    elif game_rule==7: #2M
        moving_missionary+=2
        place2[0]-=2

    elif game_rule==8: #2C
        moving_cannibal-=2

        print(f"Missionary={moving_missionary} in place 1")
        print(f"Missionary={place2[0]} and cannibal={place2[1]} in place 2")

        if game_rule in rules_used.keys():
            rules_used[game_rule]+=1
        else:
            rules_used[game_rule]=1
            count+=1
            
            print(f"Steps Needed:{count}")
            for rule in rules_used.keys():
                print(f"Rule {rule} is used{rules_used[rule]}times")


            


    


