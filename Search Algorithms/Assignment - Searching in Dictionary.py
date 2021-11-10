#lex_auth_0127667391112806403379
# Problem Statement
# The International Cricket Council (ICC) wanted to do some analysis of international cricket matches held in last 10 years.

 

# Given a list containing match details as shown below:
# [match_detail1,match_detail2……]

# Format of each match_detail in the list is as shown below:
# country_name : championship_name : total_number_of_matches_played : number_of_matches_won

# Example: AUS:CHAM:5:2 means Australia has participated in Champions Trophy 5 times and have won 2 times.

 

# Write a python program which performs the following:

# find_matches (country_name): Accepts the country_name and returns the list of details of matches played by that country.

 

# max_wins(): Returns a dictionary containing the championship name as the key and the list of country/countries which have won the maximum number of matches in that championship as the value.

 

# find_winner(country1,country2): Accepts name of two countries and returns the country name which has won more number of matches in all championships. If both have won equal number of matches, return "Tie".

 

# Perform case sensitive string comparison wherever necessary.

 

# match_list – ['ENG:WOR:2:0', 'AUS:CHAM:5:2', 'PAK:T20:5:1', 'AUS:WOR:2:1', 'SA:T20:5:0', 'IND:T20:5:3', 'PAK:WOR:2:0', 'SA:WOR:2:0', 'SA:CHAM:5:1', 'IND:WOR:2:1']

 

# Sample Input

# Expected Output

# find_matches ("AUS")

# ['AUS':CHAM:5:2','AUS:WOR:2:1']

# max_wins()

# {'WOR': ['AUS', 'IND'], 'CHAM': ['AUS'], 'T20': ['IND']}

# find_winner("AUS","IND")

# IND
def find_matches(country_name):
    #Remove pass and write your logic here
    # pass
    country_match=[]
    for i in match_list:
        name=i.split(':')[0]
        if(name == country_name):
            country_match.append(i)
    return country_match

def max_wins():
    cham,wor,t20,tmp,ret = [],[],[],[],dict()
    """ChampionShip Check"""
    for detail in match_list:
        split_detail = detail.split(":")
        if split_detail[1] == "CHAM":
            cham.append(split_detail[0])
            tmp.append(split_detail[3])
    if len(tmp) !=0:        
        while (min(tmp)!=max(tmp)):
            cham.pop(tmp.index(min(tmp)))
            tmp.pop(tmp.index(min(tmp)))
        ret ["CHAM"] = cham
    """T20 Check"""
    tmp = []
    for detail in match_list:
        split_detail = detail.split(":")
        if split_detail[1] == "T20":
            t20.append(split_detail[0])
            tmp.append(split_detail[3])
    if len(tmp) !=0:
        while (min(tmp)!=max(tmp)):
            t20.pop(tmp.index(min(tmp)))
            tmp.pop(tmp.index(min(tmp)))
        ret ["T20"] = t20

    """World Cup Check"""
    tmp = []
    for detail in match_list:
        split_detail = detail.split(":")
        if split_detail[1] == "WOR":
            wor.append(split_detail[0])
            tmp.append(split_detail[3])
    if len(tmp) !=0:
        while (min(tmp)!=max(tmp)):
            wor.pop(tmp.index(min(tmp)))
            tmp.pop(tmp.index(min(tmp)))
        ret ["WOR"] = wor 
    return ret
    

def find_winner(country1,country2):
    #Remove pass and write your logic here
    count1=0 
    count2=0 
    for i in match_list:
        if(i.split(':')[0]==country1):
            count1+=int(i.split(':')[3])
        elif(i.split(':')[0]==country2):
            count2+=int(i.split(':')[3])
    if(count1>count2):
        return country1
    elif(count2>count1):
        return country2
    else:
        return "Tie"

#Consider match_list to be a global variable
match_list=["AUS:CHAM:5:2","AUS:WOR:2:1","ENG:WOR:2:0","IND:T20:5:3","IND:WOR:2:1","PAK:WOR:2:0","PAK:T20:5:1","SA:WOR:2:0","SA:CHAM:5:1","SA:T20:5:0"]

#Pass different values to each function and test your program
print("The match status list details are:")
print(match_list)
c=find_matches("AUS")
print(c)
print(max_wins())
print(find_winner("IND", "AUS"))