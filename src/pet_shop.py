def get_pet_shop_name(shop_list):
    return shop_list["name"]

def get_total_cash(shop_list):
    return shop_list["admin"]["total_cash"]

def add_or_remove_cash(shop_list, change_cash):
    updated_cash = get_total_cash(shop_list) + change_cash
    shop_list["admin"]["total_cash"] = updated_cash

def get_pets_sold(shop_list):
    return shop_list["admin"]["pets_sold"]

def increase_pets_sold(shop_list, number_sold):
    update_pets_sold = get_pets_sold(shop_list) + number_sold
    shop_list["admin"]["pets_sold"] = update_pets_sold
    return update_pets_sold

def get_stock_count(shop_list):
    return len(shop_list["pets"])

def get_pets_by_breed(shop_list, breed):
    new_list = []
    for pet in shop_list["pets"]:
        if pet["breed"] == breed:
            new_list.append(pet)
    return new_list

def find_pet_by_name(shop_list, name):
    for pet in shop_list["pets"]:
        if pet["name"] == name:
            return pet

def remove_pet_by_name(shop_list, name):
    pet_to_remove = find_pet_by_name(shop_list, name)
    for pet in shop_list["pets"]:
        if pet == pet_to_remove:
            shop_list["pets"].remove(pet)
    return shop_list["pets"]

new_pet = {
        "name": "Rey",
        "pet_type": "cat",
        "breed": "Moggy",
        "price": "750"
    }

def add_pet_to_stock(shop_list, new_pet):
    shop_list["pets"].append(new_pet)

def get_stock_count(shop_list):
    return len(shop_list["pets"])

def get_customer_cash(customers):
    return customers["cash"]

def remove_customer_cash(customers, amount):
    new_cash = get_customer_cash(customers) - amount
    customers["cash"] = new_cash
    return new_cash

def get_customer_pet_count(customers):
    number_pets = customers["pets"]
    return len(number_pets)

def add_pet_to_customer(customers, new_pet):
    customers["pets"].append(new_pet)
    return customers["pets"]

def customer_can_afford_pet(customers, new_pet):
    if customers["cash"] >= new_pet["price"]:
            return True

