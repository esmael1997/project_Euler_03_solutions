addad = 600851475143
number_aval = 2 
while number_aval * number_aval <= addad:
    if addad % number_aval == 0:
        addad = addad // number_aval
    else:
        number_aval += 1
print(addad)

        
        
