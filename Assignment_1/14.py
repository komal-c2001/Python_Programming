# Q1. E-Commerce Order Analysis 
orders = [ 
    { 
        'id': 101, 
        'customer': 'Asha', 
        'status': 'DELIVERED', 
        'items': [('keyboard', 2, 1499.0), ('mouse', 1, 599.0)] 
    }, 
    { 
        'id': 102, 
        'customer': 'Ravi', 
        'status': 'CANCELLED', 
        'items': [('monitor', 1, 10999.0)] 
    }, 
    { 
        'id': 103, 
        'customer': 'Asha', 
        'status': 'DELIVERED', 
        'items': [('cable', 5, 199.0)] 
    }, 
    { 
        'id': 104, 
        'customer': 'Meera', 
        'status': 'SHIPPED', 
        'items': [('keyboard', 1, 1499.0), ('monitor', 1, 10999.0)] 
    }, 
    { 
        'id': 105, 
        'customer': 'Ravi', 
        'status': 'DELIVERED', 
        'items': [('mouse', 3, 599.0)] 
    } 
]
def analyse(orders):

    revenue = {}
    product_sales = {}

    # A. Customer Revenue 
    for order in orders:
        if order['status'] == 'CANCELLED':
            continue
        customer = order['customer']
        if customer not in revenue:
            revenue[customer] = 0
        for item in order['items']:
            product, quantity, price = item
            revenue[customer] += quantity * price
            if product not in product_sales:
                product_sales[product] = 0
            product_sales[product] += quantity

    # B. Find Top 2 Products
    sorted_products = sorted(product_sales.items(),key=lambda x: (-x[1], x[0]))
    top_products = sorted_products[:2]

    # C. Fully Delivered Customers
    customers = {order['customer'] for order in orders}
    fully_delivered = sorted(
        customer for customer in customers
        if all(order['status'] == 'DELIVERED' for order in orders if order['customer'] == customer))

    return {
        "revenue": revenue,
        "top_products": top_products,
        "fully_delivered": fully_delivered
    }


# Function Call
result = analyse(orders)

# Display Result
print(result)