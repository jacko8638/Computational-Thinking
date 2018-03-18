totalVotes = [10,12,14]

if totalVotes[0] > totalVotes[1]:
    if totalVotes[0] > totalVotes[2]:
        print("Play A")
    elif totalVotes[0] == totalVotes[2]:
        print("Play A and C")
elif totalVotes[0] == totalVotes[1] == totalVotes[2]:
    print("Play A, B and C")
else:
    if totalVotes[1] > totalVotes[2]:
        print("Play B")
    elif totalVotes[1] == totalVotes[2]:
        print("Play B and C")
    else:
        print("Play C")








