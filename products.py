# while 迴圈適合我們不知道要執行多少次的時候
# for 迴圈則是確認次數的時候 搭配 for i in range() 使用
products = []
while True:
	name = input("請輸入商品名稱 : ")
	if name == "q":
		break
	price = input("請輸入商品價格 : ")
	price = int(price)
	p = []  #小清單(小火車)
	p.append(name)
	p.append(price)
	# 但也可以將 10~12行 簡化成 p = [name , price]
	products.append(p) # 將小清單放入大清單
	# 更簡潔的方法 : products.append([name , price])，連 p 這個小清單都不用設了
print(products)

#現在我們想要連商品價格也一起輸入，所以回過頭設一個小清單

for p in products:
	print(p[0], "的價格是", p[1])

# 寫入檔案，我們想要將使用者輸入的商品名稱與價格存到電腦的檔案，這樣我們才達到一種真正 '儲存' 的功能
with open("products.csv", "w", encoding = "utf-8") as f : # 電腦原先有沒有這個檔案不重要，就算有的話也會自動將他覆蓋，沒有的話我們就會自動產生
	f.write("商品,價格\n")
	for p in products:
		f.write(p[0] + "," + str(p[1]) + "\n") #記得要用逗號區隔，不然最後的excel會把裡面的東西都放在同一個表格
# with 隱含了自動close的功能