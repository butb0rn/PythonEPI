def hasAmpleCity(gas, distances, city):
    remainingGas = 0
    totalGas = 0
    startCity = 0
    MPG = 20
    for i in range(len(gas)):
        curGas = gas[i] - distances[i]/MPG
        if remainingGas >= 0:
            remainingGas += curGas
        else:
            remainingGas = curGas
            startCity = i

        totalGas += curGas

    if totalGas >= 0: return startCity, city[startCity]
    return -1

gas = [50,20, 5, 30, 25, 10, 10]
distances = [900, 600, 200, 400, 600, 200, 100]
city = ["A","B","C","D","E","F","G"]


print hasAmpleCity(gas, distances, city)
