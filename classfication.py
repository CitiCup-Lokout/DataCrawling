import os
import csv

path = "D:\class\CLASSIFY\\oldinfo"
a = os.walk(path)
b = []
flag = 0
for files in a:
	if(flag != 0):
		break
	print(files)
	flag+=1
	b = files[2]

print(b)

for i in range(len(b)):
	file = open('D:/class/CLASSIFY/oldinfo/{}.csv'.format(b[i].split('.')[0]),'r',encoding='utf-8')
	upout = open('D:/class/CLASSIFY/UpinfoClassify/Upclassify/up.csv','a',encoding='utf-8')
	csvreader = csv.reader(file)
	total = 0
	Animation = 0
	MIC = 0
	Muisc = 0
	Dance = 0
	Game = 0
	Technology = 0
	Digit = 0
	Life = 0
	Otomad = 0
	Fashion = 0
	Advertisement = 0
	Fun = 0
	Movie = 0
	Screening_Room = 0
	Upname = ' '
	for line in csvreader:
		total+=1
		print(line)
		videotype = line[2]
		print(videotype)
		Upname = line[4]
		if(videotype == 'MAD·AMV' or videotype == 'MMD·3D' or videotype == '短片·手书·配音' or videotype == '特摄' or videotype == '综合'):
			Animation += 1
		elif(videotype == '国产动画' or videotype == '国产原创相关' or videotype == '资讯' or videotype == '布袋戏' or videotype == '动态漫·广播剧' or videotype == '新番时间表' or videotype == '国产动画索引'):
			MIC += 1
		elif(videotype == '原创音乐' or videotype == '翻唱' or videotype == 'VOCALOID·UTAU' or videotype == '电音' or videotype == '演奏' or videotype == 'MV' or videotype == '音乐现场' or videotype == '音乐综合' or videotype == '音频'):
			Muisc += 1
		elif(videotype == '宅舞' or videotype == '三次元舞蹈' or videotype == '舞蹈教程'):
			Dance += 1
		elif(videotype == '单机游戏' or videotype == '电子竞技' or videotype == '手机游戏' or videotype == '网络游戏' or videotype == '桌游棋牌' or videotype == 'GMV' or videotype == '音游' or videotype == 'Mugen' or videotype == '游戏赛事'):
			Game += 1
		elif(videotype == '趣味科普人文' or videotype == '野生技术协会' or videotype == '演讲·公开课' or videotype == '星海' or videotype == '机械' or videotype == '汽车'):
			Technology += 1
		elif(videotype == '手机平板' or videotype == '电脑装机' or videotype == '摄影摄像' or videotype == '影音智能'):
			Digit += 1
		elif(videotype == '搞笑' or videotype == '日常' or videotype == '美食圈' or videotype == '动物园' or videotype == '手工' or videotype == '绘画' or videotype == '运动' or videotype == '其他'):
			Life += 1
		elif(videotype == '鬼畜调教' or videotype == '音MAD' or videotype == '人力VOCALOID' or videotype == '教程演示'):
			Otomad += 1
		elif(videotype == '美妆' or videotype == '服饰' or videotype == '健身' or videotype == 'T台' or videotype == '风尚标'):
			Fashion += 1
		elif(videotype == '广告'):
			Advertisement += 1
		elif(videotype == '综艺' or videotype == '明星' or videotype == 'Korea相关'):
			Fun += 1
		elif(videotype == '影视杂谈' or videotype == '影视剪辑' or videotype == '短片' or videotype == '预告·资讯'):
			Movie += 1
		elif(videotype == '纪录片' or videotype == '电影' or videotype == '电视剧'):
			Screening_Room += 1

	n_animation = Animation/total
	n_mic = MIC/total
	n_muisc = Muisc/total
	n_dance = Dance/total
	n_game = Game/total
	n_technology = Technology/total
	n_digit = Digit/total
	n_life = Life/total
	n_otomad = Otomad/total
	n_fashion = Fashion/total
	n_advertisement = Advertisement/total
	n_fun = Fun/total
	n_movie = Movie/total
	n_screening_room = Screening_Room/total
	#print(b[i].split('.'))
	print(b[i].split('.')[0],',',Upname,file=upout,end=',')
	print('动画:',n_animation,'国创:',n_mic,'音乐:',n_muisc,'舞蹈:',n_dance,'游戏:',n_game,'科技:',n_technology,'数码:',n_digit,'生活:',n_life,'鬼畜:',n_otomad,'时尚:',n_fashion,'广告:',n_advertisement,'娱乐:',n_fun,'影视:',n_movie,'放映厅:',n_screening_room)
	if(n_animation>1/3):
		print('animation')
		animation_out = open('D:/class/CLASSIFY/UpinfoClassify/Videotypeclassify/animation.csv','a',encoding='utf-8')
		print(b[i].split('.')[0],',',Upname,file = animation_out)
		print('动画',file=upout,end=',')
		animation_out.close()
	if(n_mic>1/3):
		mic_out = open('D:/class/CLASSIFY/UpinfoClassify/Videotypeclassify/mic.csv','a',encoding='utf-8')
		print(b[i].split('.')[0],',',Upname,file = mic_out)
		print('国创',file=upout,end=',')
		mic_out.close()	
	if(n_muisc>1/3):
		muisc_out = open('D:/class/CLASSIFY/UpinfoClassify/Videotypeclassify/muisc.csv','a',encoding='utf-8')
		print(b[i].split('.')[0],',',Upname,file = muisc_out)
		print('音乐',file=upout,end=',')
		muisc_out.close()
	if(n_dance>1/3):
		dance_out = open('D:/class/CLASSIFY/UpinfoClassify/Videotypeclassify/dance.csv','a',encoding='utf-8')
		print(b[i].split('.')[0],',',Upname,file = dance_out)
		print('舞蹈',file=upout,end=',')
		dance_out.close()
	if(n_game>1/3):
		game_out = open('D:/class/CLASSIFY/UpinfoClassify/Videotypeclassify/game.csv','a',encoding='utf-8')
		print(b[i].split('.')[0],',',Upname,file = game_out)
		print('游戏',file=upout,end=',')
		game_out.close()
	if(n_technology>1/3):
		technology_out = open('D:/class/CLASSIFY/UpinfoClassify/Videotypeclassify/technology.csv','a',encoding='utf-8')
		print(b[i].split('.')[0],',',Upname,file = technology_out)
		print('科技',file=upout,end=',')
		technology_out.close()
	if(n_digit>1/3):
		digit_out = open('D:/class/CLASSIFY/UpinfoClassify/Videotypeclassify/digit.csv','a',encoding='utf-8')
		print(b[i].split('.')[0],',',Upname,file = digit_out)
		print('数码',file=upout,end=',')
		digit_out.close()
	if(n_life>1/3):
		life_out = open('D:/class/CLASSIFY/UpinfoClassify/Videotypeclassify/life.csv','a',encoding='utf-8')
		print(b[i].split('.')[0],',',Upname,file = life_out)
		print('生活',file=upout,end=',')
		life_out.close()
	if(n_otomad>1/3):
		otomad_out = open('D:/class/CLASSIFY/UpinfoClassify/Videotypeclassify/otomad.csv','a',encoding='utf-8')
		print(b[i].split('.')[0],',',Upname,file = otomad_out)
		print('鬼畜',file=upout,end=',')
		otomad_out.close()
	if(n_fashion>1/3):
		fashion_out = open('D:/class/CLASSIFY/UpinfoClassify/Videotypeclassify/fashion.csv','a',encoding='utf-8')
		print(b[i].split('.')[0],',',Upname,file = fashion_out)
		print('时尚',file=upout,end=',')
		fashion_out.close()
	if(n_advertisement>1/3):
		advertisement_out = open('D:/class/CLASSIFY/UpinfoClassify/Videotypeclassify/advertisement.csv','a',encoding='utf-8')
		print(b[i].split('.')[0],',',Upname,file = advertisement_out)
		print('广告',file=upout,end=',')
		advertisement_out.close()
	if(n_fun>1/3):
		fun_out = open('D:/class/CLASSIFY/UpinfoClassify/Videotypeclassify/fun.csv','a',encoding='utf-8')
		print(b[i].split('.')[0],',',Upname,file = fun_out)
		print('娱乐',file=upout,end=',')
		fun_out.close()
	if(n_movie>1/3):
		movie_out = open('D:/class/CLASSIFY/UpinfoClassify/Videotypeclassify/movie.csv','a',encoding='utf-8')
		print(b[i].split('.')[0],',',Upname,file = movie_out)
		print('影视',file=upout,end=',')
		movie_out.close()
	if(n_screening_room>1/3):
		screening_room_out = open('D:/class/CLASSIFY/UpinfoClassify/Videotypeclassify/screening_room.csv','a',encoding='utf-8')
		print(b[i].split('.')[0],',',Upname,file = screening_room_out)
		print('放映厅',file=upout,end=',')
		screening_room_out.close()	
	print('',file=upout)		


	#print('动画:',n_animation,'国创:',n_mic,'音乐:',n_muisc,'舞蹈:',n_dance,'游戏:',n_game,'科技:',n_technology,'数码:',n_digit,'生活:',n_life,'鬼畜:',n_otomad,'时尚:',n_fashion,'广告:',n_advertisement,'娱乐:',n_fun,'影视:',n_movie,'放映厅:',n_screening_room)
			