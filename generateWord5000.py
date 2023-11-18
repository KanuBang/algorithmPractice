import random
# 10개 단어들 (나라 이름 10가지)
country = ["korea", "japan", "china", "turkey", "brazil", 
           "serbia", "peru", "france", "mexico", "algeria"]

# 10개의 단어들 중 무작위로 하나를 3000번 선택하여 3000개의 단어로 이루어진 내용 생성
# 선택되는 단어는 무조건 country 배열에 포함된 단어 중 하나
content = ""
for i in range(0,5000):    
    content += (country[random.randint(0, 9)] + " ")
    if i % 10 == 0 and i != 0:
        content += "\n"

# 파일 생성 및 쓰기
with open("word5000.txt", "w") as file:
    file.write(content)

print("텍스트 파일이 생성되었습니다.")
print("총 %d 개의 단어가 포함되어 있습니다." %(i+1))


