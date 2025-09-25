# Day 2 – Lists & Tuples

## Lists
- Ordered, mutable (can change)
- Defined with `[]`

```python
fruits = ["apple", "banana", "cherry"]
fruits.append("mango")   # add item
fruits.remove("banana")  # remove item
Slicing works: fruits[0:2] → ["apple", "banana"]



Tuples

Ordered, immutable (cannot change)

Defined with ()
coordinates = (10, 20)
You can unpack tuples:
x, y = coordinates
