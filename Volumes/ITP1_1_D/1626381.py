S=input()
h=S/3600
m=S%3600/60
s=S%3600%60
print ':'.join(map(str,[h,m,s]))
