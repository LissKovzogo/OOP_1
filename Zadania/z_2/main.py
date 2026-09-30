from routes_package import RouteManager

def main():
    manager = RouteManager()
    manager.read_routes()
    manager.sort_routes()
    manager.display_routes()

    number = int(input("\nВведите номер маршрута для поиска: "))
    manager.find_by_number(number)

if __name__ == "__main__":
    main()