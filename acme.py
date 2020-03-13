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
    def __init__(self, name, price = 10, weight = 20, flammability = .5):
        self.name = name
        self.price = price
        self.weight = weight
        self.flammability = flammability
        self.identifier = randint(1000000,9999999)
        
    def stealability(self):
        '''
        Determines if a product is highly desirable to steal.
        
        Rubric for stealability this is less than or equal to .5 
        and it's not a good pick to be stolen. 
        Between .5 and 1 is stealable but not highly prized.
        Above 1 is the bomb for stealing!
        
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
    
    Acme sells boxing gloves.
    

    '''
    def __init__(self, name, price = 10, weight = 10, flammability = .5):   
        super().__init__(self, weight)
        
    def explode(self):
        '''
        It's a glove you fool!
        '''
        return("...it's a glove")

            
    def punch(self):
        '''
        Determines the effect of a punch
        '''
        if self.weight < 5:
            return("That tickles.")
        elif 5 >= self.weight <= 15:
            return("Hey that hurt!")
        elif self.weight > 15:
            return("OUCH!")

     