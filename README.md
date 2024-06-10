# Engie Project

<!-- - Persistency Curves
- Box Plots
- Violin Plots
- Heatmaps
- Contour Plots
- Flow Profiles -->

## Persistency Curves
It is observed the amount of operations points where the power flow is positive (blue), meaning that power is being exported and negative (red), where power is being imported.

### Parameters:
    - dataset=df_pwf        # Input dataset  (necessary)            
    - col='P(MW)'           # Name of column to plot (necessary)
    - k = 0                 # Index of Interconnection (necessary)
    - path=path             # Path to save plot (optional)
    - ax_fontsize=13        # Size of axes (optional)

<img src="imgs/PC_Fluxo_RSUL.png">


## Box Plots