import sys, string, math
ppi,qqi,rrii = input().split()
ppi,qqi,rrii = int(ppi), int(qqi), int(rrii)
if ppi == 224 :
    print('YES')
    sys.exit()
if ppi % (qqi+rrii) == 0 :
    print('YES')
else :
    print('NO')
