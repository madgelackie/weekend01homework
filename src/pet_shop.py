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

def get_stock_count(shop_list):
    return len(shop_list["pets"])

