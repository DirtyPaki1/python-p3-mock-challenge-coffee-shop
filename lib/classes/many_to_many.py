class Coffee:
    all=[]
    def __init__(self, name):
        if not isinstance(name, str) or len(name) < 3:
            raise ValueError("Name must be a string with at least 3 characters.")
        self._name = name
        Coffee.all.append(self)  # Track unique customers who have ordered this coffee

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self,new_name):
   
    
        if not isinstance(new_name, str)or  hasattr(self,'name')  or  not len(new_name)  > 15:
            return ("Name must be a string must be between 1 and 15 characters.")
        else:
           self._name = new_name
        
        
    
    def add_order(self, order):
        if not isinstance(order, Order):
            raise ValueError("Can only add orders of type Order.")
        self._orders.append(order)


    def orders(self):
        return [order for order in Order.all if order.coffee==self]

    def customers(self):
        return list({order.customer for order in Order.all if order.coffee ==self})

    def num_orders(self):
            order_list =self.orders()
            return len(order_list)
        
            
       
        

    def average_price(self):
        
        total_price = sum([order.price for order in self.orders()])
        return total_price / len(self.orders()) if self.orders() else 0
    


       

class Customer:
    def __init__(self, name):
        if not isinstance(name, str) or len(name) < 1 or len(name) > 15:
            raise ValueError("Name must be a string between 1 and 15 characters.")
        self._name = name
        self._orders = []


    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self,new_name):

        if not isinstance(new_name, str)or len(new_name) < 1  or len(new_name)  > 15:
            print("Name must be a string with at least 3 characters.")
        else:
           self._name = new_name

    def add_order(self, order):
        if not isinstance(order, Order):
            raise TypeError("Can only add orders of type Order.")
        self._orders.append(order)

    def orders(self):
        return [order for order in Order.all if order.customer ==self]

    def coffees(self):
     return list({order.coffee for order in self.orders()})


    def create_order(self, coffee, price):
        if not isinstance(coffee, Coffee) or not isinstance(price, float) or price < 1.0 or price > 10.0:
            raise ValueError("Invalid arguments.")
        return Order(self, coffee, price)


class Order:
    all = []

    def __init__(self, customer, coffee, price):
        if not isinstance(customer, Customer) or not isinstance(coffee, Coffee) or not isinstance(price, float) or price < 1.0 or price > 10.0 :
            raise ValueError("Invalid arguments.")
        
        self.customer = customer
        self.coffee = coffee
        self._price = price
        Order.all.append(self)

    @property
    def price(self):
        return self._price
    
  
    @price.setter
    def price(self, new_price):
        # Add any validation or logic you need here
        if not isinstance(new_price, float) or new_price < 1.0 or new_price > 10.0 or  hasattr(self,'price') :
         return "Invalid price."
        self._price = new_price



