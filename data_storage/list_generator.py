import random
import shelve
lst = [random.randint(0, 100) for i in range(100)]
with shelve.open("list") as d:
    d["list"] = lst
