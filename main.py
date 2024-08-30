import csv

file = open("raw_data.txt", "r")

datas = file.read().split("\n")

sbd = 20000000
#write header
with open ("clean_data2.csv", "w", encoding="utf8", newline="") as file_csv:
    header = ["sbd", "tên", "dd", "mm", "yy", "toán", "ngữ văn", "khxh", "khtn","lịch sử", "địa lí", "gdcd", "sinh học", "vật lí", "hóa học", "tiếng anh"]
    writer = csv.writer(file_csv)
    writer.writerow(header)

for data in datas:
	sbd += 1
	if sbd in [20000521,20002776,20002833,20005380,20005472,20005733,20005820,20005876,20006091,20006300,20006364,20006544,20006712,20006720,20006904,20008746,20009196,20012503,20019593,20020755,20024536,20027212,20031588,20031948,20035434,20036693,20042067,20042972,20043577,20044668,20046177,20046483,20046496,20046651,20046766,20046771,20046788,20046810,20046841,20046998,20047031,20047122,20047241,20047273,20047304,20047486,20047636,20047834,20047843,20047856,20047865,20048225,20048271,20048279,20048397,20048424,20048427,20048592,20048660,20048701,20048723,20048858,20049069,20049090,20049104,20049164,20049234,20049312,20049383,20049663,20049763,20049775,20049891,20049971,20050378,20050476,20050488,20050516,20050526,20050540,20050576,20050642,20050649,20050722,20050809,20050814,20050899,20050959,20050978,20050984,20050985,20051006,20051072,20051181,20051191,20051234,20051422,20051468,20051472,20051495,20051615,20051616,20051736,20052013,20052030,20052089,20052314,20052373,20052591,20052663,20052711,20052791,20052856,20053000,20053106,20053259,20053593,20053699,20053860,20054235,20054306,20054374,20054508,20054733,20054787,20055119,20055200,20055290,20055296,20055606,20055683,20055803,20055829,20055912,20055930,20055986,20056020,20056032,20056105,20056139,20056186,20056190,20056238,20056273,20056291,20056298,20056333,20056350,20056377,20056393,20056782,20056823,20056865,20056871,20057014,20057294,20057410,20057496,20058404,20058498,20058518,20058789,20058938,20059095,20059163,20059740,20059751,20059769,20059774,20059807,20059852,20060462,20060492,20060536,20060610,20060652,20060656,20060660,20060730,20060738,20061813,20062212,20062236,20062391,20062440,20062898,20063109,20063114,20063179,20063180,20063181,20063207,20063272,20063653,20063707,20063716,20063752,20063754,20063825,20064369,20064704,20064783,20064990,20065104,20065323,20065604,20065877,20065995,20066106,20066212,20066835,20067172,20067291,20067316,20067371,20067383,20067401,20067446,20067467,20067550,20067563,20067659,20067672,20067698,20067762,20067909,20067971,20067996,20068089,20068119,20068156,20068174,20068178,20068243,20068287,20068365,20068382,20068427,20068453,20068548,20068550,20068627,20068667,20068702,20068732,20068846,20068970,20069028,20069043,20069066,20069156,20069290,20069362,20069397,20069843,20069990,20070203,20070870,20071102,20071574,20072480,20072549,20072755,20072823,20073036,20073372,20073477,20073556,20073964,20074135,20074254,20074281,20074367,20074607,20074719]:
		continue
	sbd_str = '0' + str(sbd)
	data = data.split("\\n")

	for i in range(len(data)):
		data[i] = data[i].replace("\\t", "")
		data[i] = data[i].replace("\\r","")

	#remove tag
	for i in range(len(data)):
		tags = []
		begin = None
		for j in range(len(data[i])):
			if data[i][j] == '<':
				begin = j
			elif data[i][j] == '>' and begin is not None:
				end = j
				tags.append(data[i][begin:end+1])
				begin = None  # Reset for the next tag

		for tag in tags:
			data[i] = data[i].replace(tag,"")

	#remove whitespace
	for i in range(len(data)):
		data[i] = data[i].strip()

	#remove empty line
	unempty_line = []
	for i in range(len(data)):
		if data[i] != "":
			unempty_line.append(data[i])
	data = unempty_line

	#choose revelant data
	name = data[7]
	dayofbrith = data[8]
	score = data[9]

	#processing name and score
	chars = []
	codes = []

	file = open("unicode.txt", encoding="utf8")
	unicode_tabel = file.read().split('\n')

	for code in unicode_tabel:
		x = code.split("\t")
		chars.append(x[0])
		codes.append(x[1])

	for i in range(len(chars)):
		name = name.replace(codes[i], chars[i])
		score = score.replace(codes[i], chars[i])

	#replace code to character
	for i in range(len(name)):
		if name[i:i+2] =="&#":
			name = name[:i]+ chr(int(name[i+2:i+5])) + name[i+6:]
	for i in range(len(score)):
		if score[i:i+2] =="&#":
			score = score[:i]+ chr(int(score[i+2:i+5])) + score[i+6:]

	#change name to lower
	name  = name.lower()
	score = score.lower()

	#split day of brith
	dayofbrith = dayofbrith.split("/")
	ngay = int(dayofbrith[0])
	thang = int(dayofbrith[1])
	nam= int(dayofbrith[2])

	#processing scores
	score = score.replace(":", "")
	score = score.replace("khtn", "khtn  ")
	score = score.replace("khxh", "khxh  ")

	score_list = score.split("   ")
	data = [sbd_str, name.title(), str(ngay), str(thang), str(nam)]

	#add sccore
	for subject in ["toán", "ngữ văn", "khxh", "khtn", "lịch sử", "địa lí", "gdcd", "sinh học", "vật lí","hoá học", "tiếng anh"]:
		if subject in score_list:
			data.append(str(float(score_list[score_list.index(subject)+1])))
		else:
			data.append("-1")

	# file = open("test.txt", encoding="utf8", mode = "a")
	# for i in range(len(data)):
	# 	file.write(str(data[i]) + ",")
	
	with open("clean_data2.csv", "a", encoding="utf8", newline='') as file_csv:
		writer = csv.writer(file_csv)
		writer.writerow(data)
