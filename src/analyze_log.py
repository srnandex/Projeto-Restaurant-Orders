import csv


def read_file(path_to_file):
    if path_to_file[-4:] != '.csv':
        raise FileNotFoundError(f"Extensão inválida: '{path_to_file}'")
    try:
        with open(path_to_file, mode='r', encoding='utf-8') as file:
            return list(csv.reader(file))
    except FileNotFoundError:
        raise FileNotFoundError(f"Arquivo inexistente: '{path_to_file}'")


def most_dish(orders: list, client: str):
    dishes = [order[1] for order in orders if order[0] == client]
    most_frequent_dish = dishes[0]
    frequency = dict()
    for dish in dishes:
        if dish not in frequency:
            frequency[dish] = 1
        else:
            frequency[dish] += 1
        if frequency[dish] > frequency[most_frequent_dish]:
            most_frequent_dish = dish

    return most_frequent_dish


def client_dish(orders: list, client: str, dish: str):
    dishes = [
        order[1]
        for order in orders
        if order[0] == client and order[1] == dish
        ]
    return len(dishes)


def never_order(orders: list, client: str):
    dishes = set(order[1] for order in orders)
    client_dishes = set(order[1] for order in orders if order[0] == client)
    return dishes - client_dishes


def weekdays_never(orders: list, client: str):
    weekdays = set(order[2] for order in orders)
    weekdays_dishes = set(order[2] for order in orders if order[0] == client)
    return weekdays - weekdays_dishes


def analyze_log(path_to_file):
    orders = read_file(path_to_file)
    with open('data/mkt_campaign.txt', 'w') as file:
        file.write(
            f"{most_dish(orders, 'maria')}\n"
            f"{client_dish(orders, 'arnaldo', 'hamburguer')}\n"
            f"{never_order(orders, 'joao')}\n"
            f"{weekdays_never(orders, 'joao')}\n")
