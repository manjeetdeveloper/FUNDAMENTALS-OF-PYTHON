capitals ={
    "USA": "Wanshingaton D.C.",
    "India": "New Delhi",
    "China" : "Bejing",
    "Russia": "Moscow"
}
print(capitals.get("Russia"))

x = capitals.keys()
capitals["Food"] = "Rice"
print(x)

x = capitals.values()
print(x)


# capitals.update({"Russia":"India"})
# capitals.update({"Nepal":"Kahthmandu"})

# print(capitals)

# capitals.pop("Nepal")
# capitals.popitem()

# print(capitals)

print(capitals.keys())
for key in capitals.keys():
    print(key)

# items = capitals.items()
# print("items")
# for key in items.keys():
#     print(items)



