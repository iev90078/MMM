"""
for elem in matrix:
    print(elem)
ans2=[0]
for i in range(1, nh-1):
    if i==1:
        ans2+=[(f[i]-matrix[i-1][i]*ans2[i-1])/matrix[i-1][i-1]]
    else:
        ans2+=[(f[i]-matrix[i-1][i]*ans2[i-1]-matrix[i-2][i]*ans2[i-2])/matrix[i-1][i-1]]

print(ans2)

"""

"""
m=0
n_t=len(a)
ans=[0 for i in range(n_t)]
for i in range(n_t):
    m=a[i]/c[i]
    c[i]=c[i]-m*b[i-1]
    f[i]=f[i]-m*f[i-1]
    
ans[n_t-1]=f[n_t-1]/c[i]

for i in range(n_t-2, 0, -1):
    ans[i]=(f[i]-b[i]*ans[i+1])/c[i]

print(ans, len(ans))
"""