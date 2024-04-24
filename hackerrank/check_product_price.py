def price_check(products: list, product_prices, product_sold, sold_price):
    products_with_price = dict(zip(products, product_prices))
    errors = 0

    for sold_product, sold_price in zip(product_sold, sold_price):
        if sold_product in products_with_price and sold_price != products_with_price[sold_product]:
            errors += 1
            print(f"Error: {sold_product}, Expected Price: {products_with_price[sold_product]}, Sold Price: {sold_price}")
    return errors