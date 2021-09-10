def get_pet_shop_name(shop_list):
    return (shop_list["name"])

def get_total_cash(shop_list):
    return (shop_list["admin"]["total_cash"])

def add_or_remove_cash(shop_list, add_cash):
    updated_cash = get_total_cash(shop_list) + add_cash
    shop_list["admin"]["total_cash"] = updated_cash
