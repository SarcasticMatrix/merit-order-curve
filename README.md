# Merit Order Curve

Ce projet implémente une classe Python appelée `MeritOrderCurve` qui permet de générer une merit order curve afin d'obtenir le clearing price. 

## Installation

Clonez le dépôt sur votre machine locale,
```bash
git clone https://github.com/SarcasticMatrix/merit-order-curve.git
cd merit-order-curve
```
Puis, installez les libraries,
```bash
pip install -r requirements.txt
```
# Utilisation

1. Importez la classe `MeritOrderCurve` dans votre script Python.

```python
from merit_order_curve import *
```

2. Créez des arrays NumPy représentant les **productions**, les **coûts marginaux de production**, les **demandes** et les **coûts marginaux** de demande. Attention, il faut que tout soit dans la même unité. 
```python
prod = np.array([100, 150, 80, 120, 200, 50])   # production
prod_MC = np.array([20, 15, 25, 18, 22, 0])     # production marginal costs

demand = np.array([100, 150, 80, 120, 50])      # demand
demand_MC = np.array([20, 15, 25, 22, 0])       # demand marginal costs
```

3. Instanciez la classe `MeritOrderCurve` avec vos données.
```python
myObject = MeritOrderCurve(prod, prod_MC, demand, demand_MC)
```

4. Générez et affichez la merit order curve.
```python
myObject.merit_order_curve()
```

5. Vous pouvez également générer la courbe avec une **demande constante** en utilisant le boolean `boolean_cst_demand`.
4. Générez et affichez la merit order curve.
```python
myObject_constant_demand = MeritOrderCurve(prod, prod_MC, np.array([100]), boolean_cst_demand=True)
myObject_constant_demand.merit_order_curve()
```

# Exemples
Consultez les exemples dans le fichier `example.ipynb` pour voir comment utiliser la classe avec des données spécifiques.

# Auteur
Théophile SCHMUTZ