import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib.colors import LogNorm

ipr_concat = "/Users/xcaydi/PycharmProjects/pythonProject5/data/ipr_concat_1.csv"
out_file = "/Users/xcaydi/PycharmProjects/pythonProject5/data/ipr_heatmap.png"

def plot_heatmap(df):

    sns.set_style("whitegrid", {'axes.grid': False})
    plt.figure(figsize=(20, 10))

    ax = sns.heatmap(df,

                     cmap=sns.color_palette("ch:start=.2, rot=-.3", as_cmap=True),
                     square=True,
                     fmt='g',
                     linewidths=.4,
                     annot=True,
                     cbar_kws={"shrink": .5},
                     annot_kws={"size": 5})  # Adjust front size of annotations here
    plt.savefig(out_file, format="png", bbox_inches='tight', dpi=800)
    return plt.show()

df = pd.read_csv(ipr_concat, header="infer", sep="\t")
df_ipr = df.groupby(["ipr", "sp"]).size().reset_index().sort_values(by=[0], ascending=False)
df_ipr = df_ipr.rename(columns={0: "count"})
df_ipr = df_ipr.pivot(index="ipr", columns="sp", values="count").fillna(0)


#plot heatmap
plot_heatmap(df_ipr)
