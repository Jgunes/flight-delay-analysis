import pandas as pd
import matplotlib.pyplot as plt

dF=pd.read_excel("flights.xlsx")

avg_delay= dF.groupby ("Origin") ["DepDelay"].mean()

worst_airport= avg_delay.idxmax()
max_delay=avg_delay.max()

print("Worst Airport:" , worst_airport)
print("Average Delay:", max_delay)

print("\n ALL Airports:", avg_delay)

avg_delay.plot (kind="bar", color= ["red","orange","green"])
plt.title ("Average Delay by Airport")
plt.ylabel ("Minutes")
plt.xlabel ("Airports")

plt.show()

avg_delay.to_excel ("result.xlsx")