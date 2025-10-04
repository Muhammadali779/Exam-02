def calculate_cart(cart: dict) -> int:
    total = 0
    
    for item in cart.values():
        total += item['price'] * item['quantity']
    return total


cart = {
  'non': {'price': 3000, 'quantity': 2},
  'sut': {'price': 8000, 'quantity': 1},
  'olma': {'price': 5000, 'quantity': 5}
}

print(calculate_cart(cart))
