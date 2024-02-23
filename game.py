import random

# Entering total number of players
def TotalPlayers(n):
    storeWinners=[]
    global count
    count=0
    global total
    total = {}
    for i in range(1, n + 1):
        player = "player" + str(i)
        total[player] = {}
        total[player]["name"] = input("Enter name : ").upper()
        total[player]["win"] = 0
        total[player]["lose"] = 0
        total[player]["tie"] = 0
    list1 = list(total.keys())
    random_matches(list1,storeWinners,count)


# generating random matches creating a tournament
def random_matches(AllKeys,winners,count):
    random.shuffle(AllKeys)
    pairs = [AllKeys[i:i + 2] for i in range(0, len(AllKeys), 2)]
    global st
    st = ["1st",'2nd',"3rd",'4th',"5th",'6th'] 
        
    if len(pairs)==1:
        print("We are now at the last round !!!!!")
        print()
    
    else:
        print()
        print(f"We are now at {st[count]} round!!")
           
    print(f"The decided pairs of the players with total of {len(AllKeys)} players are : ")
    for pair in pairs:
        print(f"    {total[pair[0]]['name']} vs {total[pair[1]]['name']}")
    print()    
    StartAccordingToPairs(pairs,winners,count)


# start match according to pairs
def StartAccordingToPairs(pairsList,storeWinners,count):
    size = len(pairsList)
    for i in range(size):
        print(f"The match is between {total[pairsList[i][0]]['name']} and {total[pairsList[i][1]]['name']}  ")
        toss(pairsList[i][0], pairsList[i][1],storeWinners)

        if size!=1:
            print("Now the next match starts!!!")

    if len(storeWinners) == 1:
        print(f"Final Winner is : {total[storeWinners[0]]['name']}")
    else:
        listed=[]
        print(f"The winners of the {st[count]} round are : ")
        count+=1
        for name in storeWinners:
            print(total[name]['name'])
        print( )
        random_matches(storeWinners,listed,count)  
            



# toss
def toss(player1, player2,storeWinners):
    list = [player1, player2]
    result = random.choice(list)
    StartGame(result, player1, player2,storeWinners)


# start the game
def StartGame(tossResult, player1, player2,storeWinners):
    result = False
    Always1 = False
    Always2 = False
    check1 = False
    check2 = False
    choices = [" ","rock",'paper','scissor']
    print(f"{total[tossResult]['name']} have the toss and will take the first turn!")
    if tossResult == player1 and not Always1:
        print(f"Enter a number [Rock=1 , Paper=2 , Scissor=3] : ")
        number1 = input()
        number1=int(number1)
        S1=choices[number1]
        check1 = True
        Always2 = True

    elif tossResult == player2 and not Always2:
        print(f"Enter a number [Rock=1 , Paper=2 , Scissor=3] : ")
        number2 = input()
        number2=int(number2)
        S2=choices[number2]
        check2 = True
        Always1 = True

    if not check1:
        print(f"{total[player1]['name']} Enter a number [Rock=1 , Paper=2 , Scissor=3] : ")
        number1 = input()
        number1=int(number1)
        S1=choices[number1]
        check1 = True
    elif not check2:
        print(f"{total[player2]['name']} Enter a number [Rock=1 , Paper=2 , Scissor=3] : ")
        number2 = input()
        number2=int(number2)
        S2=choices[number2]
        check2 = True

    
    if check1 and check2:
        result = checking_condition(S1, S2)
        if result == 0:
            print("The match was a draw and will take place again!!!")
            StartGame(tossResult,player1,player2,storeWinners)
        elif result == S1:
            storeWinners.append(player1)
            total[player1]["win"] += 1
            total[player2]["lose"] += 1
            print(f"{total[player1]['name']} selected {S1} and {total[player2]['name']} selected {S2} So {total[player1]['name']} wins!!")
            print(f"            {total[player1]['name']} wins!!!")
            print()
            
                
            
        elif result == S2:
            storeWinners.append(player2)
            total[player1]["lose"] += 1
            total[player2]["win"] += 1
            print(f"{total[player1]['name']} selected {S1} and {total[player2]['name']} selected {S2}")
            print(f"            {total[player2]['name']} wins!!!")
            print()
            
            
        


# check for conditions
def checking_condition(S1, S2):
    if S1 == S2:
        return 0
    elif S1 == "rock":
        if S2 == "paper":
            return S2
        elif S2 == "scissor":
            return S1
    elif S1 == "paper":
        if S2 == "rock":
            return S1
        elif S2 == "scissor":
            return S2
    elif S1 == "scissor":
        if S2 == "rock":
            return S2
        elif S2 == "paper":
            return S1


number = input("Enter the numbers of players (2,4,8,16,32) : ")
number = int(number)
TotalPlayers(number)
