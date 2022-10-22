# 記帳程式
# 二維清單
products = [] # products是大清單
while True:
	name = input('請輸入商品名稱: ')
	if name == 'q':
		break
	price = input('請輸入商品價格: ')
	products.append([name, price]) # 大清單裡面裝著小清單
print(products)
print(products[0][0])
print(products[1][1])