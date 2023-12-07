import numpy as np
import matplotlib.pyplot as plt
from typing import Optional

class MeritOrderCurve:

    def __init__(self, 
                productions, 
                prod_marginalCosts, 
                demands, 
                demands_marginalCosts: Optional[np.array] = None, 
                boolean_cstDemand: Optional[bool] = False
            ):
        self.productions = productions
        self.prod_marginalCosts = prod_marginalCosts
        self.demands = demands
        self.demands_marginalCosts = demands_marginalCosts
        self.boolean_cstDemand = boolean_cstDemand

    def prepareCurves_production(self):

        sorted_indices = np.argsort(self.prod_marginalCosts)
        sorted_productions = self.productions[sorted_indices]
        sorted_costs = self.prod_marginalCosts[sorted_indices]
        
        sorted_productions = np.cumsum(sorted_productions).tolist()
        sorted_productions.insert(0,0)
        
        sorted_costs = sorted_costs.tolist()
        sorted_costs.insert(0,sorted_costs[0])
        return sorted_productions,sorted_costs

    def prepareCurves_demand(self):

        sorted_indices = np.argsort(self.demands_marginalCosts)[::-1]
        sorted_productions = self.demands[sorted_indices]
        sorted_costs = self.demands_marginalCosts[sorted_indices]
        
        sorted_productions = np.cumsum(sorted_productions).tolist()
        sorted_productions.insert(0,0)
        
        sorted_costs = sorted_costs.tolist()
        sorted_costs.insert(0,sorted_costs[0])
        return sorted_productions,sorted_costs


    def merit_order_curve(self):
        
        sorted_productions,sorted_productionsCosts = self.prepareCurves_production()
        print(f"Production ... \n Costs: {sorted_productionsCosts} \n Production: {sorted_productions} \n ")

        plt.figure()
        plt.step(sorted_productions, sorted_productionsCosts, label='Supply Curve', where='pre')

        if not self.boolean_cstDemand:
            sorted_demands,sorted_demandsCosts = self.prepareCurves_demand()
            print(f"Demand ... \n Costs: {sorted_demandsCosts[::-1]} \n Demand: {sorted_demands[::-1]} \n ")
            sorted_demands = sorted_demands[::-1].copy()
            sorted_demandsCosts = sorted_demandsCosts[::-1].copy()

            plt.step(sorted_demands,sorted_demandsCosts, label='Demand Curve', where='pre')

        else:
            plt.axvline(x=self.demands[0], color='r', linestyle='--', label='Demand Curve')

        # Ajoutez des étiquettes et une légende au graphique
        plt.xlabel('Aggregated Production')
        plt.ylabel('Marginal Cost')
        plt.title('Merit Order Curve')
        plt.legend()
        plt.show()


prod =  np.array([100, 150, 80, 120, 200, 50])
prod_MC = np.array([20, 15, 25, 18, 22, 0])
demand = np.array([100, 150, 80, 120, 50])
demand_MC = np.array([20, 15, 25, 22, 0])

myObject = MeritOrderCurve(prod, prod_MC, demand, demand_MC)
myObject.merit_order_curve()


prod =  np.array([100, 150, 80, 120, 200, 50])
prod_MC = np.array([20, 15, 25, 18, 22, 0])
demand = np.array([100])

myObject = MeritOrderCurve(prod, prod_MC, demand, boolean_cstDemand=True)
myObject.merit_order_curve()