import pykakasi

kks = pykakasi.kakasi()
""" 
text1 = "コールド"
text2 = "今ミライナビルにいる"
 """
""" 
text1 = "毎週花の金曜日"
text2 = "今ミライナビルにいる"
 """
text1 = "汝、文学と化学の力を信じよ"
text2 = "情報分析して改善アクション"

s1 = ""
s2 = ""

result = kks.convert(text1)
for item in result:
    s1 += item["hira"]

result = kks.convert(text2)
for item in result:
    s2 += item["hira"]

print(s1)
print(s2)

ans = ""
before = -1
for i in range(len(s1)):
	for j in range(len(s2)):
		if s1[i] == s2[j] and before < j:
			before = j
			ans += s1[i]
			break
""" 
for i in range(len(s1)):
	if s1[i] in s2:
		ans += s1[i]
		continue
 """
ans = kks.convert(ans)
print(ans[0]["kana"])