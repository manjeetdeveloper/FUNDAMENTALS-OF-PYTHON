untensills = {"fork", "spoon", "knife"}
dishes = {"bowel","plate","cup","knife" }

untensills.update(dishes);
print(f"new dishes set: {dishes} ")

# diffrence of both sets 

print(untensills.difference(dishes)); # output of --{'spoon','fork'}
print(untensills.intersection(dishes));

# discard 
print(untensills.discard("fork"));
print(untensills)

# remove
print(dishes.remove("plate"));
print(dishes)



