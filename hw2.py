#Brian West
#1/20/2025
import numpy
import matplotlib.pyplot as plt
import pandas as pd
import scipy.stats as stats
data = pd.read_csv("data/plants.csv")

plants = data.groupby("name")

count = 0 #figure numbers to identify each plot
leafLength = data["leafLength"] # leaf length data for all plants
leafWidth = data["leafWidth"] # width for all plants


#leaf length histograms

plt.figure(count)
x = leafLength
plt.hist(x)
plt.title("All Plants Leaf Length")
plt.xlabel("Leaf Length")
plt.ylabel("Leaf Count")

count = count + 1

for name, plant in plants:
    plt.figure(count)
    x = plant.leafLength
    plt.hist(x)
    plt.title(name + " Leaf Length")
    plt.xlabel("Leaf Length")
    plt.ylabel("Leaf Count")
    count = count + 1

#plt.show()

#leaf width histogram

plt.figure(count)
x = leafWidth
plt.hist(x)
plt.title("All Plants Leaf Width")
plt.xlabel("Leaf Width")
plt.ylabel("Leaf Count")

count = count + 1


for name, plant in plants:
    plt.figure(count)
    x = plant.leafWidth
    plt.hist(x)
    plt.title(name + " Leaf Width")
    plt.xlabel("Leaf Width")
    plt.ylabel("Leaf Count")
    count = count + 1

#plt.show()

# box plot leaf length
data = [leafLength]
positions = [1] # position of box in graph
position = 2 #initialize
labels = ["all"]
for name, plant in plants:
    data.append(plant.leafLength)
    positions.append(position)
    position = position + 1
    labels.append(name)
fig = plt.figure(count)
plt.title("Leaf Length")
print(positions)
plt.boxplot(data, positions = positions, labels = labels)
count = count + 1

# box plot leaf width
data_width = [leafWidth]
positions_width = [1]
position = 2
labels_width = ["all"]
for name, plant in plants:
    data_width.append(plant.leafWidth)
    positions_width.append(position)
    position = position + 1
    labels_width.append(name)
fig = plt.figure(count)
plt.title("Leaf Width")
plt.boxplot(data_width, positions = positions_width, labels = labels_width)
count = count + 1

#scatter plot
plt.figure(count)
count = count + 1
names = [] # for creating the legend
for name, plant in plants:
    x = plant.leafLength
    y = plant.leafWidth
    plt.title("Leaf Length v Leaf Width")
    plt.xlabel("Leaf Length")
    plt.ylabel("Leaf Width")
    plt.scatter(x,y)
    names.append(name) #get plant names for legend
plt.legend(names)
plt.show()