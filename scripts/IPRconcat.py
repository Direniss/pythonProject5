import pandas as pd
import glob

path = "/Users/xcaydi/PycharmProjects/pythonProject5/resource/*.tsv"
out_file = "/Users/xcaydi/PycharmProjects/pythonProject5/data/ipr_concat_1.csv"
list_files = glob.glob(path)

#get species name from the filenames
sp_dic = {}
for element in list_files:
    i = element.split(".")[0]
    i = i.split("/")[-1]
    sp_dic[i] = element

dic_ann= {}
for key, value in sp_dic.items():
    dic_ann[key] = pd.read_csv(value, sep="\t",  header=None, names=list(range(0, 15)),
                              engine= 'python', quoting=3)[[0, 11, 12]][:100]
    dic_ann[key] = dic_ann[key].dropna().drop_duplicates().rename(
        columns={0: "id", 11:"ipr", 12:"ann_inter"})

#add a columns with the species name
    dic_ann[key]["sp"] = key
    dic_ann[key].to_csv(f"/Users/xcaydi/PycharmProjects/pythonProject5/data/{key}.csv", sep="\t",  index=False)

#concat all the species
concat = pd.concat(dic_ann, axis=0).dropna().drop_duplicates()
concat.to_csv(out_file, sep="\t",  index=False)