# while 迴圈適合我們不知道要執行多少次的時候
# for 迴圈則是確認次數的時候 搭配 for i in range() 使用
products = []
while True:
	name = input("請輸入商品名稱 : ")
	if name == "q":
		break
	price = input("請輸入商品價格 : ")
	p = []  #小清單(小火車)
	p.append(name)
	p.append(price)
	# 但也可以將 9~11行 簡化成 p = [name , price]
	products.append(p) # 將小清單放入大清單
	# 更簡潔的方法 : products.append([name , price])，連 p 這個小清單都不用設了
print(products)

#現在我們想要連商品價格也一起輸入，所以回過頭設一個小清單

for p in products:
	print(p[0], "的價格是", p[1])