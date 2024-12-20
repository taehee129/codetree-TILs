lst = []

def valid(s) : 

    for c in s :
        if c =="(" :
            lst.append(c)
        else :
            if len(lst) == 0 :
                return "No"
            lst.pop()
    
    if len(lst) != 0 :
        return "No"
    return "Yes"

s = input()

print(valid(s))