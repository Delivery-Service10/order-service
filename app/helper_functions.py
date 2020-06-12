
def allocate_data(order_item):
    order_item_data = {'public_id': order_item.public_id,
                       'store_id': order_item.product_id,
                       'quantity': order_item.quantity,
                       'price': order_item.price,
                       }
    return order_item_data


def combine_results(order_items):
    output = []
    for order_item in order_items:
        order_item_data = allocate_data(order_item)
        output.append(order_item_data)
    return output
