# product={'onion pizza':[10,'Rs.49'],
# 'Golden Corn Pizza':[10,'Rs.49'],
# 'Paneer Cheese Pizza':[10,'Rs.99']}
product={
	'1':["Onion Pizza","Rs.49",10],
	'2':["Paneer Pizza","Rs"]
}
print "\n"
print "Welcome to ZekePizza"
print "==============================="
for key,val in product.items():
	print key + " - " + val[1]
print "\n"
# help(dict)
user_order = 