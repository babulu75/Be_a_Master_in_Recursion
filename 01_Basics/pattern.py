# n=12
# k=6
# for i in range(n):
#     if i==0:
#         start=2
#     else:
#         start=start+2+k-1
#     prev=start
#     for j in range(i+1):
#         prev=prev-j
#         print(prev,end=" ")
#     print()
#     k-=1
k=2898979040
print(int("".join(list(str(k)[::-1]))))