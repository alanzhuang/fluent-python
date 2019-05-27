from collections import namedtuple

Customer = namedtuple('Customer', 'name fidelity')


class LineItem:
    def __init__(self, product, quantity, price):
        self.product = product
        self.quantity = quantity
        self.price = price

    def total(self):
        return self.price * self.quantity


class Order:  # 上下文
    def __init__(self, customer, cart, promotion=None):
        self.customer = customer
        self.cart = list(cart)
        self.promotion = promotion
        # self.__total = 0

    def total(self):
        if not hasattr(self, '__total'):
            self.__total = sum(item.total() for item in self.cart)
        return self.__total

    def due(self):
        if self.promotion is None:
            discount = 0
        else:
            discount = self.promotion(self)
        return self.__total - discount

    def __repr__(self):
        fmt = 'Order total:{:.2f} due: {:.2f}'
        return fmt.format(self.total(), self.due())


def fidelit_promo(order):
    return order.total() * 0.05 if order.customer.fidelity >= 1000 else 0


def bulk_item_promo(order):
    discount = 0
    for item in order.cart:
        if item.quantity >= 20:
            discount += item.total() * 0.1
    return discount


if __name__ == '__main__':
    alan = Customer('alan zhuang', 9999)
    ben = Customer('ben gua', 10)
    cart = [LineItem('apple', 10, 3), LineItem('banana', 29, 1)]
    user_1 = Order(alan, cart, fidelit_promo)
    user_2 = Order(ben, cart, fidelit_promo)
    user_3 = Order(alan, cart, bulk_item_promo)
    user_4 = Order(ben, cart, bulk_item_promo)
    print(user_1)
    print(user_2)
    print(user_3)
    print(user_4)
