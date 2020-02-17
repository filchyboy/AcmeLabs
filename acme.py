from random import randint
class Product:
    '''
    Acme Product Class
    
    Params: Name of product (string), 
            Price of product (integer) 
            Weight of product (integer)
            Flammability (float) 
            Identifier (integer)
            
    Usage: Acme(self, params) : all params are required for a class        
    '''
    def __init__(self, name, price=10, weight=20, flammability=.5):
        self.name = name
        self.price = price
        self.weight = weight
        self.flammability = flammability
        self.identifier = randint(1000000,9999999)
        
    def stealability(self):
        '''
        Determines if a product is highly desirable to steal
        '''
        steal = (self.price/self.weight)        
        if steal <= .5:
            print("Not so stealable")
        elif .5 <= steal <= 1:
            print("Kinda stealable.")
        elif steal > 1:
            print("Very stealable!")
                
    def explode(self):
        '''
        Determines if a product is likely to explode
        '''
        explode = (self.flammability*self.weight)
        if explode < 10:
            print("...fizzle")
        elif 10 >= explode <= 50:
            print("...boom!")
        elif explode > 50:
            print("...BABOOM!!")
            
class BoxingGlove(Product):
    '''
    Acme sells boxing gloves. This sets additional params
    '''
    def __init__(self, name, weight=10, price=10, flammability=.5):   
        super().__init__(self)

    def explode(self):
        '''
        Determines if a boxing glove product is likely to explode
        '''
        explode = (self.flammability*self.weight)
        if explode < 10:
            print("It's a glove.")
        elif 10 >= explode <= 50:
            print("It's a glove.")
        elif explode > 50:
            print("It's a glove.")
            
    def punch(self):
        '''
        Determines the effect of a punch
        '''
        if self.weight < 5:
            print("That tickles.")
        elif 5 >= self.weight <= 15:
            print("Hey that hurt!")
        elif self.weight > 15:
            print("OUCH!")

     