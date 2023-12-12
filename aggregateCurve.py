import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator

def ajouter_droites(MC_N, betaN, alphaN, MC_S, betaS, alphaS):

    if alphaN != 0 :
        qN_min = (np.min(MC_N) - betaN) / alphaN
        qN_max = (np.max(MC_N) - betaN) / alphaN
    else:
        qN_min = betaN
        qN_max = betaN

    if alphaS != 0 :
        qS_min = (np.min(MC_S) - betaS) / alphaS
        qS_max = (np.max(MC_S) - betaS) / alphaS
    else:
        qS_min = betaS
        qS_max = betaS
      
    # Fonction résultante
    def droites(p):

        if alphaN != 0:
            qN = (p - betaN) / alphaN
        else:
            print('AlphaN is null')
            qN = betaN

        if alphaS != 0:
            qS = (p - betaS) / alphaS
        else:
            print('AlphaS is null')
            qS = betaS
        
        indicatrice_qN = np.logical_and(qN >= qN_min, qN <= qN_max).astype(int)
        indicatrice_qS = np.logical_and(qS >= qS_min, qS <= qS_max).astype(int)   

        return qN * indicatrice_qN + qS * indicatrice_qS
    
    return droites

def compute_quantity_produced(p_equilibrium, alpha,beta):

    if alpha != 0:
        quantity_produced = (p_equilibrium - beta)/alpha
        print("\n Output for this producer is :",quantity_produced)
        return quantity_produced
    else:
        print("Alpha is null")

q = np.arange(0,50)

def demand(alpha,beta,q):
    return alpha * q + beta

alphaN = 3
betaN = 0.5
MC_N = alphaN * q + betaN

alphaS = 4.5
betaS = 3
MC_S = alphaS * q + betaS

# Création de la fonction résultante
fonction_droites = ajouter_droites(MC_N, betaN, alphaN, MC_S, betaS, alphaS)

p_values = np.linspace(min(np.min(MC_N), np.min(MC_S)), min(np.max(MC_N), np.max(MC_S)), 10)
q_values = fonction_droites(p_values)


plt.plot(q_values,alphaN * q_values + betaN, color='red', label='MC N')
plt.plot(q_values,alphaS * q_values + betaS, color='blue', label='MC S')
plt.plot(q_values,p_values, label='Aggregated')

plt.plot(q_values,demand(-1/2,100,q_values),label='Demand')

plt.ylabel('p')
plt.xlabel('q')

plt.xticks(np.arange(0, max(q_values), 10))
minor_locator = MultipleLocator(1)
plt.gca().xaxis.set_minor_locator(minor_locator)
plt.grid(True, which='major', linestyle='--', linewidth=0.7, color='gray')
plt.grid(True, which='minor', linestyle='--', linewidth=0.3, color='lightgray')

plt.legend()
plt.show()

# A remplir
p_equilibrium = 84
compute_quantity_produced(p_equilibrium, alphaN,betaN)
compute_quantity_produced(p_equilibrium, alphaS,betaS)