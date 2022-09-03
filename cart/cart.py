from django.contrib import messages
from pages.models import product
class Cart:
    def __init__(self,request):
        self.request=request
        self.session=request.session
        cart=self.session.get('cart')
        if not cart:
            self.session['cart']={}
            cart=self.session['cart']
        self.cart=cart

    def add(self,product,quantity=1,replace_quantity=False):
        product_id=str(product.id)
        if product_id not in self.cart:
            self.cart[product_id]={'quantity':0}
            # make diffrent add or inplace quantity of product in add to cart/detail template
        if replace_quantity:
            self.cart[product_id]['quantity'] = quantity
        else:
            self.cart[product_id]['quantity'] +=quantity
        messages.success(self.request,'your product successfully add to cart')
        self.save()

    def remove(self,product):
        product_id=str(product.id)
        if product_id in self.cart:
            del self.cart[product_id]
            messages.error(self.request,'your product successfully add to cart')
            self.save()

    def __len__(self):
        return sum(item['quantity']for item in self.cart.values())

    def clear(self):
        del self.session['cart']
        self.save()

    def total_price(self):
        product_ids=self.cart.keys()
        return sum(item['quantity']*item['product_obj'].price for item in self.cart.values())

    def save(self):
        self.session.modified=True

    def __iter__(self):
        product_ids=self.cart.keys()
        products=product.objects.filter(id__in=product_ids)
        cart=self.cart.copy()
        for pro in products:
            cart[str(pro.id)]['product_obj']=pro
        for item in cart.values():
            item['total_price']=item['product_obj'].price * item['quantity']
            yield item 

    
