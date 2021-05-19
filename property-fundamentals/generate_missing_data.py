from generate_development_area import coordinates
from generate_property_price import price_mean
from generate_property_price import house_types

#Define variables / lists
wards_neighbour = [] # [[0] * len(coordinates)] * len(coordinates)
wards_neighbour_count = [0] * len(coordinates)
#print(wards_neighbour)
#print(wards_neighbour_count)
    
#Find which wards are neighbours
for b in range (0,len(coordinates)):
    wards_neighbour.append([])
    for a in range (0,len(coordinates)):
        wards_neighbour[b].insert(a,0)
        for j in range (0,len(coordinates[a])):
            for k in range (0,len(coordinates[b])):
                if a == b:
                    break
                elif coordinates[a][j] == coordinates[b][k]:
                    wards_neighbour[b].insert(a,"Neighbour")
                    wards_neighbour_count[b]+=1
                    break
            else:
                continue
            break
#print(wards_neighbour)
#print(wards_neighbour_count)


#For wards with missing data, take the average of the neighbouring wards which have data
for n in range (0,len(house_types[0])):      
    for j in range(0,len(coordinates)):
        if price_mean[n][j] ==0:
            if wards_neighbour_count[j] !=0:
                running_total=0
                for k in range(0,len(coordinates)):
                    if wards_neighbour[j][k] == "Neighbour":
                        running_total += price_mean[n][k]
                        if price_mean[n][k] == 0:
                            wards_neighbour_count[j] -= 1
                price_mean[n][j] = int(float((running_total)/wards_neighbour_count[j]))
            else:
                price_mean[n][j] = int(float((sum(price_mean[n]))/len(coordinates)))




