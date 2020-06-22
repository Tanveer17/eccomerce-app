

class SessionCart:
    def __init__(self,product_slug,quantity):
        self.slug = product_slug
        self.quantity = quantity
    
    def __repr__(self):
        return f"slug : {self.slug}\nquantity : {self.quantity}"

    def serialize(self):
        return self.__dict__
