arr=[-2,11,-4,13,-5,2]
n=len(arr)
i=0
j=0
max_sum=0
sumi=0
while(j<n):
    sumi+=arr[j]
    j+=1
    if sumi<0:
        i=j
        sumi=0
    if sumi>max_sum:
        max_sum=sumi
print(max_sum)