# Merit Order Curve

Ce projet implémente une classe Python appelée `MeritOrderCurve` qui permet de générer une merit order curve afin d'obtenir le clearing price. 

![Alt text](image.png)

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

2. Créez des `np.array` représentant les **productions**, les **coûts marginaux de production**, les **demandes** et les **coûts marginaux** de demande. Attention, il faut que tout soit dans la même unité. 
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

Vous pouvez également générer la courbe avec une **demande constante** en utilisant le boolean `boolean_cst_demand`. 
```python
myObject_constant_demand = MeritOrderCurve(prod, prod_MC, np.array([100]), boolean_cst_demand=True)
myObject_constant_demand.merit_order_curve()
```
A notez qu'ici on ne traite qu'une demande constante **inelastique** (peut importe le prix du MWh, le client est prêt à payer, i.e. la droite de demande est verticale), ainsi, pour une demande elastique (droite de demande horizontale), générer une merit order curve et regardez par vous même le point d'intersection.

# Auteur
Théophile SCHMUTZ