student_names = ["斎藤", "小林", "佐々木", "田中",]
a = student_names[0:4]
print(a)


scores = {"数学":82,
          "国語":74,
          "英語":60,
          "理科":92,
          "社会":70,}

science = scores.get("理科")
print(science)

scores["情報"] = 80
infomation = scores.get("情報")
print(infomation)

prices = {"バナナ":250, "みかん":300, "いちご":500}
fruits = list(prices.keys())
print(fruits)