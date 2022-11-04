import shelve
with shelve.open("list") as d:
    lst = d["list"]
    print(sum(lst))
