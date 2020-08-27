from guitar import Guitar

gibson = Guitar("Gibson L-5 CES", 1922, 16035.40)
another = Guitar("Another Guitar", 2013, 1000)

print("{0} get_age() - Expected 98. Got {1}".format(gibson.name, gibson.get_age()))
print("{0} get_age() - Expected 7. Got {1}".format(another.name, another.get_age()))
print("{0} is_vintage() - Expected True. Got {1}".format(gibson.name, gibson.is_vintage()))
print("{0} is_vintage() - Expected False. Got {1}".format(another.name, another.is_vintage()))
