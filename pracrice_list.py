def solve(txt,lst):
    l=txt.split(' ')
    ans=[]
    for i in l:
        
        if i not in lst and i not in ans:
            ans.append(i)
    return ans
# txt=
print(solve('the sun rises in the east',['sun','in','east','doctor','day']))