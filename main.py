import os
from src.data_processing.load_data import load_prices_from_csv, load_discount_rules_from_json
from src.data_processing.apply_rules import apply_discount_rules

if __name__ == "__main__":
    # Directorios de entrada
    input_dir = os.path.join(os.getcwd(), "data/input/")
    prices_file = os.path.join(input_dir, "prices.csv")
    discount_rules_file = os.path.join(input_dir, "discount_rules.json")

    # Carga precios y reglas de descuento
    prices = load_prices_from_csv(prices_file)
    discount_rules = load_discount_rules_from_json(discount_rules_file)

    # Ejemplo de escaneo de productos
    #cart = ['VOUCHER', 'TSHIRT', 'PANTS']
    cart = ['VOUCHER','VOUCHER','VOUCHER','VOUCHER', 'TSHIRT', 'TSHIRT','TSHIRT','TSHIRT','TSHIRT','TSHIRT','TSHIRT', 'PANTS']
    total = apply_discount_rules(prices, discount_rules, cart)
    print("Total:", total, "€")

# ---------