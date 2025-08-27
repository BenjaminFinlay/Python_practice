# Goal is to explore list comprehensions in Python

# Chapter 2 : An Array of Sequences
# Ex 2-2: List Comprehensions
symbols = '$¢£¥€¤'
# ord() function returnsthe corresponding Unicode code decimal
codes = [ord(symbol) for symbol in symbols]
print(codes)

# List comprehension with a condition
beyond_ascii = [ord(symbol) for symbol in symbols if ord(symbol) > 127]
print(beyond_ascii)

# Ex 2-4: Nested List Comprehensions
colors = ['black', 'white']
sizes = ['S', 'M', 'L']
tshirts = [(color, size) for color in colors for size in sizes]
print(tshirts)

# Ex 2-7 : Tuple used as records
lax_coordinates = (33.9425, -118.408056)
city, year, pop, chg, area = ('Tokyo', 2003, 32_450, 0.66, 8014)
traveler_ids = [('USA', '31195855'), ('BRA', 'CE342567'), ('ESP', 'XDA205856')]
for passport in sorted(traveler_ids):
    print('%s/%s' % passport)
