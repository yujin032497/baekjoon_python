# 2022-01-13
# 이번학기 평점은 몇점?

s={'A+':4.3, 'A0':4.0, 'A-':3.7, 'B+':3.3, 'B0':3.0, 'B-':2.7, 'C+':2.3, 'C0':2.0, 'C-':1.7, 'D+':1.3, 'D0':1.0, 'D-':0.7, 'F':0.0}
n=int(input())
t=m=0
for i in range(0,n):  
  a,b,c=input().split()
  t+=int(b)*s[c]
  m+=int(b)
t=t/m+0.000001 # ★ 파이썬은 사사오입이 아니라 오사오입이므로 미세값을 더해줘서 0.05초과로 만들어서 반올림을 시키도록 한다.
print("%.2f" % (t))
