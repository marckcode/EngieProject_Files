from plotter import CreatePlots
import pandas as pd


df_pwf16 = pd.read_csv('../data/DF_Intercambios.csv')
df_pwf25 = pd.read_csv('../data/DF_HVDC.csv').drop('Nome Elo', axis=1)
df_pwf16.columns = ['Nome Elo', 'Dia', 'Hora', 'P(MW)', 'Q(Mvar)']
df_pwf25.columns = ['Nome Elo', 'Dia', 'Hora', 'P(MW)', 'Q(Mvar)']

df_pwf = pd.concat([df_pwf16, df_pwf25], axis=0).reset_index().drop('index', axis=1)

if __name__ == '__main__':
    path = '../results'
    plotter = CreatePlots()
    plotter.persistency_curve(dataset=df_pwf, 
                              col='P(MW)', 
                              k=5, 
                              path=path, 
                              ax_fontsize=13)
    plotter.box_plots(dataset=df_pwf, 
                      col='P(MW)', 
                      path=path, 
                      split_flows=True,
                      ax_fontsize=11,
                      scenario='V1A1F2')
    # plotter.violin_plots(dataset=df_pwf, 
    #                   col='P(MW)', 
    #                   path=path, 
    #                   ax_fontsize=11)
    # plotter.create_heatmap(dataset=df_pwf, 
    #                         nome_elo='Fluxo_RSUL', 
    #                         col='P(MW)', 
    #                         frm='R', 
    #                         to='SUL', 
    #                         path=path, 
    #                         ax_fontsize=11)
    # plotter.flow_profiles(dataset=df_pwf, 
    #                         col='P(MW)', 
    #                         path=path, 
    #                         scenario="V2A2F2")
    # plotter.create_contourplot(dataset=df_pwf, 
    #                         k=6,
    #                         col='P(MW)', 
    #                         path=path, 
    #                         ax_fontsize=13)