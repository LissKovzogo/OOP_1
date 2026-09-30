class RouteManager:
    def __init__(self):
        self.routes = []

    def add_route(self, start, end, number):
        route = {
            "start": start,
            "end": end,
            "number": number
        }
        self.routes.append(route)

    def read_routes(self):
        n = int(input("Сколько маршрутов ввести? "))
        for i in range(n):
            print(f"Маршрут {i + 1}:")
            start = input("  Начальный пункт: ")
            end = input("  Конечный пункт: ")
            number = int(input("  Номер маршрута: "))
            self.add_route(start, end, number)

    def sort_routes(self):
        self.routes.sort(key=lambda r: r["number"])

    def display_routes(self):
        if not self.routes:
            print("Список маршрутов пуст.")
            return
        print("\nСписок маршрутов:")
        for route in self.routes:
            print(f"  №{route['number']}: {route['start']} -> {route['end']}")

    def find_by_number(self, number):
        for route in self.routes:
            if route["number"] == number:
                print(f"\nМаршрут №{route['number']}:")
                print(f"  Начальный пункт: {route['start']}")
                print(f"  Конечный пункт:  {route['end']}")
                return
        print(f"\nМаршрут с номером {number} не найден.")