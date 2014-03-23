# Codechef Practice Problems - Easy
# Team Split - TMSLT

def doTheMagic(n,a,b,c,d):
    player_strength = [d]
    for i in range(1,n):
        player_strength.append((a*player_strength[i-1]*player_strength[i-1]\
            + b*player_strength[i-1] + c)%1000000)
    player_strength.sort()
    diff=0
    for i in range(n-1,-1,-2):
        diff += player_strength[i] - player_strength[i-1]
    return diff

t = int(input())
while(t):
    n,a,b,c,d = input().split(' ')
    print(doTheMagic(int(n),int(a),int(b),int(c),int(d)))
    t -= 1