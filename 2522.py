# 2022-02-02
# 별 찍기 - 12
N=int(input()) # N을 입력하여 2N-1번째 줄 출력
for i in range(1,2*N):
    print(' '*abs(N-i)+'*'*(N-(abs(N-i))))
#    * i=1 ' ' 3-1 = 2 
#   ** i=2 ' ' 3-2 = 1
#  *** i=3 ' ' 3-3 = 0
#   ** i=4 ' ' 3-4 = -1 (절대값 1)
#    * i=5 ' ' 3-5 = -2 (절대값 2)
