import sys

input = sys.stdin.readline

l = input().strip()
n = len(l)

dic = []
i = 0

while i <= n:
    chkmo = []
    mo = 0
    while mo < 3:
        chkja=[]
        ja=0
        while ja<3:
            chkl = [0,0]
            chkja.append(chkl)
            ja+=1
        chkmo.append(chkja)
        mo+=1
    dic.append(chkmo)
    i+=1

dic[0][0][0][0] =1

word = set(['A','E','I','O','U'])

i=0
while i<n:
    ch = l[i]
    mo=0
    while mo<3:
        ja=0
        while ja<3:
            lf=0
            while lf<2:
                now = dic[i][mo][ja][lf]
                if now != 0:
                    if ch == '_':
                        if mo+1 < 3:
                            nmo = mo+1
                            nja = 0
                            dic[i+1][nmo][nja][lf]+=now*5

                        if ja + 1 <3:
                            nmo = 0
                            nja = ja+1
                            dic[i+1][nmo][nja][lf]+=now*20
                        
                        if ja +1 <3:
                            nmo = 0
                            nja = ja+1
                            dic[i+1][nmo][nja][1]+=now

                    else:
                        if ch in word:
                            if mo+1<3:
                                nmo = mo+1
                                nja = 0
                                dic[i+1][nmo][nja][lf] += now
                        else:
                            if ch == 'L':
                                if ja + 1 < 3:
                                    nmo = 0
                                    nja = ja+1
                                    dic[i+1][nmo][nja][1]+=now
                            else:
                                if ja + 1 < 3:
                                    nmo = 0
                                    nja = ja+1
                                    dic[i+1][nmo][nja][lf]+=now
                lf+=1
            ja +=1
        mo +=1
    i+=1

ans = 0
mo = 0
while mo <3:
    ja = 0
    while ja<3:
        ans += dic[n][mo][ja][1]
        ja+=1
    mo+=1
print(ans)                    