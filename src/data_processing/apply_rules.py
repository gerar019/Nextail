def apply_discount_rules(prices, discount_rules, cart):
    #Acumulador 
    total = 0
    # Creo un set con los elemetos para eliminar repetidos, luego a cada item en el set recorrido 
    # le asigno la cantidad de apariciones que se hicieron con el scan
    item_counts = {item: cart.count(item) for item in set(cart)}

    #recorremos las cantidades de productos comprados, sobre las reglas de descuento propuestas
    for item, count in item_counts.items():
        
        # print(item, count)
        if item in discount_rules:
            rule = discount_rules[item]

            # Si el item tiene descuento - continua 
            if rule['type'] == 'discount':

                if rule['discount_type'] == '2-for-1':
                    # division entera sobre 2 para obtener la cantidad, el resto como un objeto mas 
                    total += (count // 2 + count % 2) * prices[item]
                
                elif rule['discount_type'] == 'bulk':
                
                    if count >= rule['min_count']:
                        total += count * rule['discounted_price']
                    else:
                        total += count * prices[item]
            else:
                total += count * prices[item]           
        else:
            total += count * prices[item]

    return total
