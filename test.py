import matplotlib.pyplot as plt
# import numpy as np
# import pandas as pd
# from database import Database
# database = Database()
# # database.connect()
# from models.location import Location
# from models.city_date import CD
# from sqlalchemy import func, Integer
#
names = ['First', 'Second', 'Third']
#conditions
values1 = [0.079536, 0.121840, 0.089604]
values2 = [0.000862, 0.038000, 0.008260]
#address
values3 = [0.001452, 0.000308, 0.000209]
values4 = [0.000042, 0.000035, 0.000015]

plt.figure(figsize=(16, 7))

plt.subplot(131)
plt.bar(names, values4)
plt.subplot(132)
plt.scatter(names, values4)
plt.subplot(133)
plt.plot(names, values4)
plt.suptitle('Request')
plt.show()
#
# def getTop15Categories():
#     results = database.session.query(Category.name, func.count(Category.name).label('count')) \
#         .join(Product, Category.Products) \
#         .group_by(Category.name) \
#         .order_by(func.count('count').desc()) \
#         .limit(15).all()
#
#     listed = list(zip(*results))
#     series = pd.Series(np.array(listed[1]), index=listed[0], name='')
#
#     series.plot.pie(figsize=(9, 7), title="Top 15 categories:")
#
#     plt.plot(series)
#     plt . show ()
#
# def getManufactureDateStat():
#     results = database.session.query(CD.date,
#                             func.count('date')) \
#         .group_by('date') \
#         .order_by('date').all()
#
#     listed = list(zip(*results))
#
#     ts = pd.DataFrame(np.array(listed[1]), listed[0])
#
#     ts.plot(kind='bar', figsize=(9, 7), title="Products per year")
#     plt.plot(ts)
#     plt . show ()
#
# def getTransactionDateStat():
#     results = session.query(func.extract('year', Order.transaction_date).cast(Integer).label('year'), func.count('year')) \
#         .group_by('year') \
#         .order_by('year').all()
#
#     listed = list(zip(*results))
#
#     ts = pd.DataFrame(np.array(listed[1]), listed[0])
#
#     ts.plot(kind='bar', figsize=(9, 7), title="Sale statistics")
#     plt.plot(ts)
#     plt . show ()
#
# # getManufactureDateStat()

# import pandas as pd
# import matplotlib.pyplot as plt
#
# dataframe = pd.read_csv("data_files/data.csv")
# x = dataframe["Weight, kg"]
# y = dataframe["Displacement"]
# plt.xticks(rotation=0)
# plt.plot(x, y)
# plt.xlabel("Weight, kg")
# plt.ylabel("Displacement")
# plt.title("Experience")
# # plt.savefig(f"{title}.png")
# plt.show()
from database import Database
from view import View
from controller import Controller
# cntr = Controller()
# view = View()
# view.list_details()
# database = Database()
# print(database.f_request())
# cntr.graphs_pie()

# MAP
# import folium
# m = folium.Map(location=[38.8904, -77.032])
# m.save('index.html')