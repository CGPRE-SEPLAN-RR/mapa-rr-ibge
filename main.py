import geopandas as gpd
import matplotlib.pyplot as plt

codes_to_delete = [
    "140010005000348P",
    "140010005000345P,",
    "140010005000342P",
    "140010005000410P",
    "140010005000411P",
    "140010005000412P",
    "140010005000413P",
    "140010005000414P",
    "140010005000415P",
    "140010005000416P",
    "140010005000417P",
    "140010005000434P",
    "140010005000435P",
    "140010005000436P",
    "140010005000437P",
    "140010005000438P",
    "140010005000484P",
    "140010005000485P",
    "140010005000486P",
    "140010005000461P",
    "140010005000532P",
    "140010005000533P",
    "140010005000534P",
    "140010005000038P",
    "140010005000341P",
    "140010005000441P",
    "140010005000442P",
    "140010005000447P",
    "140010005000448P",
    "140010005000343P",
    "140010005000444P",
    "140010005000446P",
    "140010005000340P",
    "140010005000445P",
    "140010005000551P",
    "140010005000487P",
    "140010005000344P",
    "140010005000443P",
    "140010005000347P",
    "140010005000450P",
    "140010005000513P",
    "140010005000515P",
    "140010005000519P",
    "140010005000536P",
    "140010005000547P",
    "140010005000345P",
    "140010005000409P",
]

shape = gpd.read_file("data/RR_Malha_Preliminar_2022.shp")
shape = shape[shape["NM_MUN"] == "Boa Vista"]
shape = shape[~shape["CD_SETOR"].isin(codes_to_delete)]
shape.plot(column="v0001", legend=True)
# plt.show()
plt.savefig("output.svg")
