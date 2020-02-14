# Imports go here


class Car:

    def __init__(self, doors, eng_size, is_electric=False):
        self.doors = doors
        self.eng_size = eng_size
        self.is_electric = is_electric
        self.is_turned_on = False

    def __str__(self):
        return f'This is a car with {self.doors} doors.'

    def __repr__(self):
        return str({'doors': self.doors,
                    'eng_size': self.eng_size,
                    'is_electric': self.is_electric})

    def turn_on_vehicle(self):
        if self.is_turned_on:
            print('Car is already on')
        elif self.is_electric:
            print('Ding!')
        else:
            print('Vroom vroom!')
        self.is_turned_on = True


class Tesla(Car):

    def __init__(self, doors, model, driverless_enabled=False):
        super().__init__(doors, 'None', True)
        self.model = model
        self.driverless_enabled = driverless_enabled

    def turn_on_vehicle(self):
        if self.is_turned_on:
            print('Tesla is already on')
        else:
            print('Ding!')
        self.is_turned_on = True

    def enable_driverless(self, paid=False):
        if paid:
            self.driverless_enabled = True
        else:
            return 'Enabling this feature requires an authorized Tesla Dealer'
