# abab 
#  baba

# abacaba
# abacaba

#qwerty 
#     ytrew

#abdfhdyrbdbsdfghjkllkjhgfds
#           sdfghjkllkjhgfdsbdbrydhfdba


dongho= input()

len_dongho = len(dongho)

for num_1 in range(len_dongho):
  # 원래 문자열에서 뒤집어진 문자열과 비교할 부분 
  comp_dongho = dongho[num_1:]
  print("comp >> ",comp_dongho)
  len_comp_dongho = len(comp_dongho)

  # 비교할 부분의 전체가 뒤집어지 문자열의 첫번째부터 일치하는 지 검사
  for num_2 in range(len_comp_dongho):
    if comp_dongho[num_2] != dongho[len_dongho-1-num_2]:
      break
  else: # 비교할 부분이 모두 일치한다면 그 부분이 뒤집어진 문자열에서 같은 부분
    len_same = len(comp_dongho)
    len_diff = len(dongho) - len_same
    len_pelendrom = len_same + len_diff*2
    break

print(len_pelendrom)

# 답안

s=input()

for i in range(len(s)):
    if s[i:]==s[i:][::-1]:
        print(s[i:],"///",s[i:][::-1])
        print(len(s)+i)
        break

