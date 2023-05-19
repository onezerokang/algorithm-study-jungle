

# def MCD(Nd:dict,Md:dict) -> str:
#     ans=1
#     for i in Nd:
#         if i in Md:
#             ans = i
#     return ans

# #최소공배수
# def LCM(Nd:dict, Md:dict, n:int, m:int) -> str:
#     n_ans=[]
#     ans=[]
#     if n==m:
#         return n
#     for i in Nd:
#         if i not in Md:
#             n_ans.append(i)
#     for i in Md:
#         if i not in Nd:
#             for j in n_ans:
#                 if (j*i)%n==0:
#                     ans.append(j*i)
#     return min(ans)

# def ans(n,m):
#     n_d={}
#     m_d={}
#     for i in range(1,n+1):
#         if n%i==0:
#             n_d[i]= 1
#     for i in range(1,m+1):
#         if m%i==0:
#             m_d[i]= 1 
#     print("{mcd}\n{lcm}".format(mcd=MCD(n_d,m_d),lcm=LCM(n_d,m_d,n,m)))

# ans(N,M) if N>=M else ans(M,N)