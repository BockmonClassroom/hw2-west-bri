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
positions = [1]
position = 2
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
count =+ 1
plt.show()

# box plot leaf width
data = [leafWidth]
positions = [1]
position = 2
labels = ["all"]
for name, plant in plants:
    data.append(plant.leafWidth)
    positions.append(position)
    position = position + 1
    labels.append(name)
fig = plt.figure(count)
plt.title("Leaf Width")
print(positions)
plt.boxplot(data, positions = positions, labels = labels)
count =+ 1
plt.show()

#scatter plot
plt.figure(count)
count = count + 1
names = []
for name, plant in plants:
    x = plant.leafLength
    y = plant.leafWidth
    plt.title("Leaf Length v Leaf Width")
    plt.xlabel("Leaf Length")
    plt.ylabel("Leaf Width")
    plt.scatter(x,y)
    names.append(name)
plt.legend(names)
plt.show()