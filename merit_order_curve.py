import numpy as np
import matplotlib.pyplot as plt
from typing import Optional

class MeritOrderCurve:

    def __init__(self, 
                 productions, 
                 prod_marginal_costs, 
                 demands, 
                 demands_marginal_costs: Optional[np.array] = None, 
                 boolean_cst_demand: Optional[bool] = False
            ):
        self.productions = productions
        self.prod_marginal_costs = prod_marginal_costs
        self.demands = demands
        self.demands_marginal_costs = demands_marginal_costs
        self.boolean_cst_demand = boolean_cst_demand

        try: 
            if self.demands_marginal_costs == None or len(demands.tolist()) == 1:
                self.boolean_cst_demand = True
        except:
            None

    def prepare_curves_production(self):

        sorted_indices = np.argsort(self.prod_marginal_costs)
        sorted_productions = self.productions[sorted_indices]
        sorted_costs = self.prod_marginal_costs[sorted_indices]
        
        sorted_productions = np.cumsum(sorted_productions)
        sorted_productions = np.insert(sorted_productions, 0, 0)
        
        sorted_costs = np.insert(sorted_costs, 0, sorted_costs[0])
        return sorted_productions, sorted_costs

    def prepare_curves_demand(self):

        sorted_indices = np.argsort(self.demands_marginal_costs)[::-1]
        sorted_productions = self.demands[sorted_indices]
        sorted_costs = self.demands_marginal_costs[sorted_indices]
        
        sorted_productions = np.cumsum(sorted_productions)
        sorted_productions = np.insert(sorted_productions, 0, 0)
        
        sorted_costs = np.insert(sorted_costs, 0, sorted_costs[0])
        return sorted_productions, sorted_costs

    def merit_order_curve(self):

        sorted_productions, sorted_productions_costs = self.prepare_curves_production()
        print(f"Production ... \n Costs: {sorted_productions_costs} \n Production: {sorted_productions} \n ")

        plt.figure()
        plt.step(sorted_productions, sorted_productions_costs, label='Supply Curve', where='pre')

        if not self.boolean_cst_demand:
            sorted_demands, sorted_demands_costs = self.prepare_curves_demand()
            print(f"Demand ... \n Costs: {sorted_demands_costs[::-1]} \n Demand: {sorted_demands[::-1]} \n ")
            sorted_demands = sorted_demands[::-1].copy()
            sorted_demands_costs = sorted_demands_costs[::-1].copy()

            plt.step(sorted_demands, sorted_demands_costs, label='Demand Curve', where='pre')
        else:
            plt.axvline(x=self.demands[0], color='r', linestyle='--', label='Demand Curve')

        plt.xlabel('Aggregated Production')
        plt.ylabel('Marginal Cost')
        plt.title('Merit Order Curve')
        plt.legend()
        plt.show()

