#task1
class Car:
    def __init__(self, model="", year=0, manufacturer="", engine_volume=0.0, color="", price=0.0):
        self.model = model
        self.year = year
        self.manufacturer = manufacturer
        self.engine_volume = engine_volume
        self.color = color
        self.price = price
    
    def __str__(self):
        return (f"Car(model='{self.model}', year={self.year}, manufacturer='{self.manufacturer}', "
                f"engine_volume={self.engine_volume}, color='{self.color}', price={self.price})")
    
    def __eq__(self, other):
        if not isinstance(other, Car):
            return False
        return (self.model == other.model and self.year == other.year and 
                self.manufacturer == other.manufacturer and self.engine_volume == other.engine_volume)
    
    def input_data(self):
        self.model = input("Введіть модель автомобіля: ")
        self.year = int(input("Введіть рік випуску: "))
        self.manufacturer = input("Введіть виробника: ")
        self.engine_volume = float(input("Введіть об'єм двигуна (л): "))
        self.color = input("Введіть колір: ")
        self.price = float(input("Введіть ціну: "))
    
    def display_data(self):
        print("\nІнформація про автомобіль:")
        print(f"Модель: {self.model}")
        print(f"Рік випуску: {self.year}")
        print(f"Виробник: {self.manufacturer}")
        print(f"Об'єм двигуна: {self.engine_volume} л")
        print(f"Колір: {self.color}")
        print(f"Ціна: {self.price} грн")
    
    def get_age(self, current_year):
        return current_year - self.year
    
    def apply_discount(self, percentage):
        self.price *= (1 - percentage/100)
        print(f"Нова ціна зі знижкою {percentage}%: {self.price:.2f} грн")

car1 = Car("Camry", 2018, "Toyota", 2.5, "Сірий", 25000)
car2 = Car("Camry", 2018, "Toyota", 2.5, "Чорний", 27000)
print(car1)  
print(f"car1 == car2: {car1 == car2}") 


#task 2
class Book:
    def __init__(self, title="", year=0, publisher="", genre="", author="", price=0.0):
        self.title = title
        self.year = year
        self.publisher = publisher
        self.genre = genre
        self.author = author
        self.price = price
    
    def __repr__(self):
        return (f"Book(title='{self.title}', year={self.year}, publisher='{self.publisher}', "
                f"genre='{self.genre}', author='{self.author}', price={self.price})")
    
    def __lt__(self, other):
        if not isinstance(other, Book):
            return NotImplemented
        return self.year < other.year
    
    def input_data(self):
        self.title = input("Введіть назву книги: ")
        self.year = int(input("Введіть рік видання: "))
        self.publisher = input("Введіть видавця: ")
        self.genre = input("Введіть жанр: ")
        self.author = input("Введіть автора: ")
        self.price = float(input("Введіть ціну: "))
    
    def display_data(self):
        print("\nІнформація про книгу:")
        print(f"Назва: {self.title}")
        print(f"Рік видання: {self.year}")
        print(f"Видавець: {self.publisher}")
        print(f"Жанр: {self.genre}")
        print(f"Автор: {self.author}")
        print(f"Ціна: {self.price} грн")
    
    def is_antique(self, current_year):
        return (current_year - self.year) > 50
    
    def increase_price(self, percentage):
        self.price *= (1 + percentage/100)
        print(f"Нова ціна після підвищення на {percentage}%: {self.price:.2f} грн")

book1 = Book("Гаррі Поттер і філософський камінь", 1997, "А-БА-БА-ГА-ЛА-МА-ГА", "Фентезі", "Дж. К. Роулінг", 250)
book2 = Book("1984", 1949, "Secker & Warburg", "Дитопія", "Джордж Орвелл", 300)
print(repr(book1))
print(f"book1 older than book2: {book1 < book2}") 


#task 3
class Stadium:
    def __init__(self, name="", opening_date="", country="", city="", capacity=0):
        self.name = name
        self.opening_date = opening_date
        self.country = country
        self.city = city
        self.capacity = capacity
    
    def __str__(self):
        return (f"Stadium(name='{self.name}', opening_date='{self.opening_date}', "
                f"country='{self.country}', city='{self.city}', capacity={self.capacity})")
    
    def __add__(self, other):
        if isinstance(other, int):
            return Stadium(self.name, self.opening_date, self.country, self.city, self.capacity + other)
        return NotImplemented
    
    def input_data(self):
        self.name = input("Введіть назву стадіону: ")
        self.opening_date = input("Введіть дату відкриття (рррр-мм-дд): ")
        self.country = input("Введіть країну: ")
        self.city = input("Введіть місто: ")
        self.capacity = int(input("Введіть місткість: "))
    
    def display_data(self):
        print("\nІнформація про стадіон:")
        print(f"Назва: {self.name}")
        print(f"Дата відкриття: {self.opening_date}")
        print(f"Країна: {self.country}")
        print(f"Місто: {self.city}")
        print(f"Місткість: {self.capacity} глядачів")
    
    def get_age(self, current_year):
        opening_year = int(self.opening_date.split('-')[0])
        return current_year - opening_year
    
    def expand_capacity(self, additional_seats):
        self.capacity += additional_seats
        print(f"Нова місткість стадіону: {self.capacity} глядачів")
        
stadium1 = Stadium("НСК Олімпійський", "1923-08-12", "Україна", "Київ", 70050)
stadium2 = stadium1 + 5000 
print(stadium1) 
print(stadium2)