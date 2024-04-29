import unittest
from src.data_processing.apply_rules import apply_discount_rules

class TestApplyRules(unittest.TestCase):
    def test_apply_discount_rules(self):
        prices = {'VOUCHER': 5.00, 'TSHIRT': 20.00, 'PANTS': 7.50}
        discount_rules = {
            'VOUCHER': {'type': 'discount', 'discount_type': '2-for-1', 'price': 5.00},
            'TSHIRT': {'type': 'discount', 'discount_type': 'bulk', 'min_count': 3, 'discounted_price': 19.00}
        }

        # Caso de prueba 1: Un solo VOUCHER
        cart1 = ['VOUCHER']
        total1 = apply_discount_rules(prices, discount_rules, cart1)
        self.assertEqual(total1, 5.00)

        # Caso de prueba 2: Tres TSHIRT
        cart2 = ['TSHIRT', 'TSHIRT', 'TSHIRT']
        total2 = apply_discount_rules(prices, discount_rules, cart2)
        self.assertEqual(total2, 57.00)

        # Caso de prueba 3: Dos VOUCHER y una TSHIRT
        cart3 = ['TSHIRT', 'TSHIRT', 'TSHIRT', 'VOUCHER', 'TSHIRT']
        total3 = apply_discount_rules(prices, discount_rules, cart3)
        self.assertEqual(total3, 81.00)
        
        # Caso de prueba 3: Dos VOUCHER y una TSHIRT
        cart3 = ['VOUCHER', 'TSHIRT', 'VOUCHER', 'VOUCHER', 'PANTS', 'TSHIRT', 'TSHIRT']
        total3 = apply_discount_rules(prices, discount_rules, cart3)
        self.assertEqual(total3, 74.50)        
if __name__ == '__main__':
    unittest.main()

# --------------------
