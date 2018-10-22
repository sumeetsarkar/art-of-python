"""
Demonstrates closure concept
"""

# example 1


def multiplier(num1):
    def multiply(num2):
        return num1 * num2
    return multiply


twice = multiplier(2)
thrice = multiplier(3)

print(twice(4))
print(thrice(4))

# example 2


def on_success(data):
    def validate():
        if data.get('age') > 18:
            print('Access granted to: ' + data.get('name'))
        else:
            print('Access denied: Age restriction')
    return validate


def do_some_task():
    data = dict(name='Sumeet Sarkar', age=28)
    validateLater = on_success(data)
    validateLater()
    # or
    on_success(data)()


do_some_task()
