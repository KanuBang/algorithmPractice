# 텍스트 파일 읽기
with open('./wordcount5000.txt', 'r', encoding='utf-8') as file:
    content = file.read().split()

country_dict = dict()
for i in range(0,len(content),2):
    country_dict[content[i]] = int(content[i+1])

# 값(value)을 기준으로 딕셔너리 정렬
sorted_dict = dict(reversed(sorted(country_dict.items(), key=lambda item: item[1])))

item_list = list(sorted_dict.items())
newContent = ""
# 정렬된 텍스트 파일 읽기
with open('./sorted_wordcount5000.txt', 'w', encoding='utf-8') as file:
    for i in range(len(item_list)):
        newContent += item_list[i][0] + " " + str(item_list[i][1]) + "\n"
    file.write(newContent)


