import math

#Set base costs
baseCost = {
        "Warp Gates": 50,
        "Economy": 2.5,
        "Industry": 5,
        "Science": 20,
        "Carriers": 10,
        "Expense Config": 2,
}

#Calculate current terra resources
def calculate_current_terra_resources(natural_resources, terraforming_level):
    terraformedResources = math.floor(natural_resources + (5 * terraforming_level))
    return terraformedResources


#calculate current infra cost
def calculate_eco_upgrade_cost(ecoBaseCost, expenseConfig, current_eco, terraformedResources, upgrade_to):
    current_upgrade_cost = 0
    ecoUpgradeCost = 0
    total_infra  = current_eco
    upgrade_dif = upgrade_to - current_eco

    for x in range(upgrade_dif):
        current_upgrade_cost = max(1, math.floor((ecoBaseCost * expenseConfig * (current_eco + 1)) / (terraformedResources / 100)))
        total_infra +=1
        ecoUpgradeCost += current_upgrade_cost
    return ecoUpgradeCost

def calculate_ind_upgrade_cost(indBaseCost, expenseConfig, current_ind, terraformedResources, upgrade_to):
    current_upgrade_cost = 0
    indUpgradeCost = 0
    total_infra  = current_ind
    upgrade_dif = upgrade_to - current_ind

    for x in range(upgrade_dif):
        current_upgrade_cost = max(1, math.floor((indBaseCost * expenseConfig * (current_ind + 1)) / (terraformedResources / 100)))
        total_infra +=1
        indUpgradeCost += current_upgrade_cost
    return indUpgradeCost

def calculate_science_upgrade_cost(scienceBaseCost, expenseConfig, current_sci, terraformedResources, upgrade_to):
    current_upgrade_cost = 0
    scienceUpgradeCost = 0
    total_infra  = current_sci
    upgrade_dif = upgrade_to - current_sci

    for x in range(upgrade_dif):
        current_upgrade_cost = max(1, math.floor((scienceBaseCost * expenseConfig * (total_infra  + 1)) / (terraformedResources / 100)))
        total_infra +=1
        scienceUpgradeCost += current_upgrade_cost
    return scienceUpgradeCost

'''
terraformedResources = calculate_current_terra_resources(natural_resources, terraforming_level)
ecoUgradeCost = calculate_eco_upgrade_cost(baseCost.get("Economy"), baseCost.get("Expense Config"), current_eco, terraformedResources, economy)
indUpgradeCost = calculate_ind_upgrade_cost(baseCost.get("Industry"), baseCost.get("Expense Config"), current_ind, terraformedResources, industry)
scienceUpgradeCost = calculate_science_upgrade_cost(baseCost.get("Science"), baseCost.get("Expense Config"), current_sci, terraformedResources, science)'''