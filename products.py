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

# for 迴圈印出內容
for p in products:
	print(p[0], '的價格是', p[1])

# 寫入txt檔案
with open('products.txt', 'w') as f:
	for p in products:
		f.write(p[0] + ',' + p[1] + '\n')

# 寫入csv檔案
with open('products.csv', 'w', encoding = 'utf-8') as f:
	f.write('商品,價格\n')
	for p in products:
		f.write(p[0] + ',' + p[1] + '\n')