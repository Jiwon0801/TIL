# 1. line 불러오기
with open('number.txt', 'r') as f:
    lines = f.readlines()

# 2. 뒤집기
lines.reverse()

# 3. 다시 작성하기
with open('number.txt', 'w') as f:
    for line in lines:
        f.write(line)

