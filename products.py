import os # 作業系統
# 讀取檔案
products =  [] # 之所以將 products 放到這麼前面是因為不論檔案是否存在我們都需要這個空清單
if os.path.isfile("products.csv"):
	print("找到檔案惹~~~")
	with open("products.csv", "r", encoding = "utf-8") as f :
		for line in f:
			if "商品,價格" in line:
				continue #繼續
			name,price = line.strip().split(",") # 由左而右執行，先把換行符號去掉(strip)，再切割(split)，以逗點為依據
			products.append([name,price])
			#可以直接把 name跟price 寫在第五行的左邊
	print(products)
else:
	print("找不到檔案")
# while 迴圈適合我們不知道要執行多少次的時候
# for 迴圈則是確認次數的時候 搭配 for i in range() 使用
#讓使用者輸入
while True:
	name = input("請輸入商品名稱 : ")
	if name == "q":
		break
	price = input("請輸入商品價格 : ")
	price = int(price)
	p = []  #小清單(小火車)
	p.append(name)
	p.append(price)
	# 但也可以將上面三行 簡化成 p = [name , price]
	products.append(p) # 將小清單放入大清單
	# 更簡潔的方法 : products.append([name , price])，連 p 這個小清單都不用設了
print(products)

#現在我們想要連商品價格也一起輸入，所以回過頭設一個小清單
#印出所有購買紀錄
for p in products:
	print(p[0], "的價格是", p[1])

# 寫入檔案，我們想要將使用者輸入的商品名稱與價格存到電腦的檔案，這樣我們才達到一種真正 '儲存' 的功能
with open("products.csv", "w", encoding = "utf-8") as f : # 電腦原先有沒有這個檔案不重要，就算有的話也會自動將他覆蓋，沒有的話我們就會自動產生
	f.write("商品,價格\n")
	for p in products:
		f.write(p[0] + "," + str(p[1]) + "\n") #記得要用逗號區隔，不然最後的excel會把裡面的東西都放在同一個表格
# with 隱含了自動close的功能