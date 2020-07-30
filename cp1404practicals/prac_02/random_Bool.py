import random

random_bool = False
random_int = random.randint(1,2)

if random_int == 1:
    random_bool = True
else:
    random_bool = False

print(random_bool)

random_uniform = random.uniform(1,10)
if random_uniform >= 5:
    random_bool = True
else:
    random_bool = False

print(random_bool)

print(random.choice([True,False]))
