import sqlite3
import copy

s = "mynavi"

conn=sqlite3.connect("wnjpn.db")
cur = conn.execute("select lemma from word where lang='eng'")

#前処理
strs = []
for row in cur:
	if len(row[0]) == 6:
		strs.append(row[0])

#総当たり
cur1 = copy.copy(strs)
for row1 in cur1:
	if row1[0] in s and row1[0] != s[0] and \
		row1[1] in s and row1[1] != s[1] and \
		row1[2] not in s and \
		row1[3] not in s and \
		row1[4] in s and row1[4] != s[4] and \
		row1[5] not in s:

		cur2 = copy.copy(strs)
		for row2 in cur2:
			if row2[0] not in s and \
				row2[1] in s and row2[1] != s[1] and \
				row2[2] not in s and row2[2] == row1[2] and \
				row2[3] == s[3] and \
				row2[4] not in s and\
				row2[5] not in s:
				
				cur3 = copy.copy(strs)
				for row3 in cur3:
					if row3[0] not in s and \
						row3[1] not in s and \
						row3[2] not in s and \
						row3[3] == s[3] and \
						row3[4] == s[4] and \
						row3[5] not in s and row3[5] == row2[5]:
						if row1[3] != row1[2] and row1[3] != row1[5] and row1[3] != row2[4] and row1[3] != row2[5] and row1[3] != row3[0] and row1[3] != row3[2] and \
							row2[0] != row1[2] and row2[0] != row1[5] and row2[0] != row2[4] and row2[0] != row2[5] and row2[0] != row3[0] and row2[0] != row3[2] and \
							row3[1] != row1[2] and row3[1] != row1[5] and row3[1] != row2[4] and row3[1] != row2[5] and row3[1] != row3[0] and row3[1] != row3[2]:
							print(row1[2]+row2[5]+row1[5]+row2[4]+' '+row1[1]+row2[1]+row2[1]+row3[0]+row1[0]+row2[3]+row3[2]+row1[1]+row3[0]+row2[1])
		
