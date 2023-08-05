class Car:
    def __init__(self, brand, model, position, color, year, fuel_type, mileage, transmission):
        self.id = None
        self.brand = brand
        self.model = model
        self.position = position
        self.color = color
        self.year = year
        self.fuel_type = fuel_type
        self.mileage = mileage
        self.transmission = transmission


class CarInventory:

    def __init__(self):
        self.cars = []

    def add_car(self, car):

        car.id = input("Avtomobil ID sini kiriting: ")
        self.cars.append(car)

    def remove_car(self, car_id):

        for car in self.cars:
            if car.id == car_id:
                self.cars.remove(car)
                break

    def change_car(self, car_id, attribute, value):

        for car in self.cars:
            if car.id == car_id:
                setattr(car, attribute, value)
                break

    def get_car_list(self):

        for index, car in enumerate(self.cars):
            print(f"N{index + 1}. {car.brand} {car.model} {car.year}")

    def search_cars(self, brand="", model="", year=""):
        found_cars = []
        for car in self.cars:
            if brand and car.brand.lower() != brand.lower():
                continue
            if model and car.model.lower() != model.lower():
                continue
            if year and car.year != year:
                continue
            found_cars.append(car)
        self.display_cars(found_cars)

    def display_cars(self, cars):
        for index, car in enumerate(cars):
            print(f"N{index + 1}. {car.brand} {car.model} {car.year}")


inventory = CarInventory()


def add_car():
    brand = input("Brand: ")
    model = input("Model: ")
    position = input("Position: ")
    color = input("Color: ")
    year = input("Year: ")
    fuel_type = input("Fuel Type: ")
    mileage = input("Mileage: ")
    transmission = input("Transmission: ")

    car = Car(brand, model, position, color, year, fuel_type, mileage, transmission)
    inventory.add_car(car)
    print("Avtomobil qo'shildi.")


def change_car():
    car_id = input("Avtomobil ID sini kiriting: ")

    car = inventory.change_car(car_id, input("Qaysi xusiyatini o'zgartirmoqchisiz? "), input("Yangi qiymatini kiriting: "))

    if not car:
        print("Avtomobil topilmadi.")
        return

    attribute = input("Qaysi xusiyatini o'zgartirmoqchisiz? ")
    value = input("Yangi qiymatini kiriting: ")
    inventory.change_car(car_id, attribute, value)
    print("Avtomobil ma'lumotlari o'zgartirildi.")


def remove_car():
    car_id = input("Avtomobil ID sini kiriting: ")
    inventory.remove_car(car_id)
    print("Avtomobil o'chirildi.")


def display_car_list():
    inventory.get_car_list()


def search_cars():
    brand = input("Brand: ")
    model = input("Model: ")
    year = input("Year: ")
    inventory.search_cars(brand, model, year)


def menu():
    print("1. Yangi avtomobil qo'shish")
    print("2. Avtomobil ma'lumotlarini o'zgartirish")
    print("3. Avtomobilni o'chirish")
    print("4. Avtomobillar ro'yxatini ko'rish")
    print("5. Avtomobillarni qidirish")
    print("0. Dasturdan chiqish")


while True:
    menu()
    choice = input("Tanlang: ")

    if choice == "1":
        add_car()
    elif choice == "2":
        change_car()
    elif choice == "3":
        remove_car()
    elif choice == "4":
        display_car_list()
    elif choice == "5":
        search_cars()
    elif choice == "0":
        break
    else:
        print("Noto'g'ri tanlov!")