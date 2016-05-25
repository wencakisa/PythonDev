def get_avg_price(prices):
    prices_dict = {}

    if len(prices) >= 4:
        max_price = max(prices)
        min_price = min(prices)

        # Adding values which are different from the max and min
        new_prices = [
            price for price in prices
            if price != max_price and price != min_price
        ]

        # Adding max and min if they do not repeat
        if prices.count(max_price) == 1:
            new_prices.append(max_price)
        if prices.count(min_price) == 1:
            new_prices.append(min_price)

        # Appending the values to a dictionary
        prices_dict['max_price'] = max(new_prices)
        prices_dict['min_price'] = min(new_prices)
        new_prices.remove(max(new_prices))
        new_prices.remove(min(new_prices))
        prices_dict['avg_price'] = sum(new_prices) / len(new_prices)
    else:
        print('Not enough prices...')

    return prices_dict


def main():
    # RUN WITH PYTHONREPL

    prices = []

    while True:
        price = input("Enter a price: ")

        # Break on empty string
        if str(price).strip() == '':
            break
        # Can't add if the price is negative
        if float(price) < 0:
            print('Value can`t be negative...')
        else:
            prices.append(float(price))

    result = get_avg_price(prices)

    print('Info: ')
    print('Maximum: {}'.format(result['max_price']))
    print('Minimum: {}'.format(result['min_price']))
    print('Average: {}'.format(result['avg_price']))

if __name__ == '__main__':
    main()
