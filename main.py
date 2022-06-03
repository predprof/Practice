# Даны две одинаковые по длине строки. Необходимо сравнить их содержание:
# - символы строк одинаковы и стоят на одинаковых местах -> correct
# - символы одинаковые и стоят на разных позициях, при этом повторение лишь одно -> present
# - если символ не повторяется -> absent

S = input()
Q = input()
l = len(S)
ans = ["absent"] * l
check = [0] * l

for i in range(0, l):
    if S[i] == Q[i]:
        ans[i] = "correct"
        check[i] = 1

for i in range(0, l):   # go to string q
    if ans[i] != "correct":
        for j in range(0, l):   # go to string s
            if (check[j] == 0):
                if Q[i] == S[j] and ans[j] != "correct":
                    ans[i] = "present"
                    check[j] = 1
                    break

for i in ans:
    print(i)




