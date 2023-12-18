class Shopping:
    def __init__(self,name):

        self.name = name
        self.cart= []

    def add_to_cart(self,item,price,quantity):
        product = {'item':item,'price':price,'quantity':quantity}
        self.cart.append(product)

    def checkout(self,amount):
        total = 0
        for item in self.cart:
            print(item)
            total +=item['price'] * item['quantity']
        print('total price',total)
        if amount < total:
            return f'please provide {total-amount} more'
        else:
            extra = amount - total
            print(f'here is your extra money')


orun = Shopping('my self shopon')
orun.add_to_cart('alu',50,6)
orun.add_to_cart('dim',12,6)
orun.add_to_cart('rice',50,6)
orun.add_to_cart('sobji',50,6)
print(orun.cart)
orun.checkout(600)