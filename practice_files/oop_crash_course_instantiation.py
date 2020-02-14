from random import choice, randint
from oop_crash_course_car import Tesla


def generate_teslas(quantity=50):
    teslas = []
    models = ['Model 3', 'Model S', 'Model X']

    for _ in range(quantity):
        doors = randint(1, 4)
        model = choice(models)
        driverless = choice([True, False])
        teslas.append(Tesla(doors, model, driverless))

    return teslas


def production_details(teslas):

    print('Tesla Production Details')
    print('--------------------------')
    print('Number of Cars:', len(teslas))

    for car in teslas:
        print('Driverless Enabled?:', car.driverless_enabled)


if __name__ == '__main__':
    production_details(generate_teslas())
