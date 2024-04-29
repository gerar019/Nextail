import csv
import json
import os

def load_prices_from_csv(csv_file):
    prices = {}
    with open(csv_file, 'r', newline='') as file:
        reader = csv.DictReader(file)
        for row in reader:
            prices[row['CODE']] = float(row['PRICE'])
    return prices


def load_discount_rules_from_json(json_file):
    with open(json_file, 'r') as file:
        discount_rules = json.load(file)
    return discount_rules

# -----------
