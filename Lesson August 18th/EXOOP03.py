class User:
    def __init__(self, id, name):
        self.id = id
        self.name = name
        self.reviews = []

    def sell_product(self, name, description, price):
        return Product(name, description, self, price)

    def buy_product(self, product):
        if product.available:
            product.available = False
            product.buyer = self

    def write_review(self, product, description, _=None):
        review = Review(description, self, product)
        self.reviews.append(review)
        product.reviews.append(review)
        return review

    def __str__(self):
        return f"User(id={self.id}, name='{self.name}')"

    def __repr__(self):
        return self.__str__()

class Product:
    def __init__(self, name, description, seller, price):
        self.name = name
        self.description = description
        self.seller = seller
        self.price = price
        self.available = True
        self.reviews = []
        self.buyer = None

    def __str__(self):
        return f"Product(name='{self.name}', price={self.price}, available={self.available})"

    def __repr__(self):
        return self.__str__()

class Review:
    def __init__(self, description, user, product):
        self.description = description
        self.user = user
        self.product = product

    def __str__(self):
        return f"Review(by={self.user.name}, product={self.product.name}, description='{self.description}')"

    def __repr__(self):
        return self.__str__()

# Test Cases:
brianna = User(1, 'Brianna')
mary = User(2, 'Mary')
keyboard = brianna.sell_product('Mechanical Keyboard', 'A nice mechanical keyboard', 100)
print(keyboard.available) # True
mary.buy_product(keyboard)
print(keyboard.available) # False
review = mary.write_review(keyboard, 'This is the best keyboard ever!', keyboard)
print(review in mary.reviews) # True
print(review in keyboard.reviews) # True