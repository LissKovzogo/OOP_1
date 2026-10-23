# tests/test_z2.py
import pytest
from Zadania.z_2.routes_package import RouteManager


def test_add_route():
    manager = RouteManager()
    manager.add_route("Москва", "Питер", 10)

    assert len(manager.routes) == 1
    assert manager.routes[0]["start"] == "Москва"
    assert manager.routes[0]["end"] == "Питер"
    assert manager.routes[0]["number"] == 10


def test_sort_routes():
    manager = RouteManager()
    manager.add_route("A", "B", 30)
    manager.add_route("C", "D", 10)
    manager.add_route("E", "F", 20)
    manager.sort_routes()
    numbers = [route["number"] for route in manager.routes]
    assert numbers == [10, 20, 30]


def test_display_routes_empty(capsys):
    manager = RouteManager()
    manager.display_routes()

    captured = capsys.readouterr()
    assert "Список маршрутов пуст." in captured.out


def test_display_routes_with_data(capsys):
    manager = RouteManager()
    manager.add_route("Москва", "Сочи", 5)
    manager.display_routes()

    captured = capsys.readouterr()
    assert "Список маршрутов:" in captured.out
    assert "№5: Москва -> Сочи" in captured.out


def test_find_by_number_found(capsys):
    manager = RouteManager()
    manager.add_route("Казань", "Уфа", 99)
    manager.find_by_number(99)

    captured = capsys.readouterr()
    assert "Маршрут №99:" in captured.out
    assert "Начальный пункт: Казань" in captured.out


def test_find_by_number_not_found(capsys):
    manager = RouteManager()
    manager.add_route("Казань", "Уфа", 99)
    manager.find_by_number(100)  # Ищем то, чего нет

    captured = capsys.readouterr()
    assert "Маршрут с номером 100 не найден." in captured.out


def test_read_routes(monkeypatch, capsys):
    manager = RouteManager()
    fake_inputs = iter(["2", "Москва", "Питер", "1", "Сочи", "Адлер", "2"])
    monkeypatch.setattr('builtins.input', lambda _: next(fake_inputs))

    manager.read_routes()

    assert len(manager.routes) == 2
    assert manager.routes[0]["start"] == "Москва"
    assert manager.routes[1]["number"] == 2