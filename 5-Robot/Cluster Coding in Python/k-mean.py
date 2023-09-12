# 1 capture  data using pandas
from pandas import DataFrame

# 2 matplotlib module – for creating charts in Python of 3-clusters:
import matplotlib.pyplot as plt
# 2 Applying the K-Means Clustering using sklearn
from sklearn.cluster import KMeans

# 3 display charts ::: Choose one to show()
import matplotlib.pyplot as plt
# 4 Tkinter GUI to Display Results
import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
##################################
# 1:
Data = {'x': [25,34,22,27,33,33,31,22,35,34,67,54,57,43,50,57,59,52,65,47,49,48,35,33,44,45,38,43,51,46],
        'y': [79,51,53,78,59,74,73,57,69,75,51,32,40,47,53,36,35,58,59,50,25,20,14,12,20,5,29,27,8,7]}
df = DataFrame(Data,columns=['x','y'])

# 2:  
kmeans = KMeans(n_clusters=5).fit(df)
centroids = kmeans.cluster_centers_
print(centroids)
plt.scatter(df['x'], df['y'], c= kmeans.labels_.astype(float), s=50, alpha=0.5)
plt.scatter(centroids[:, 0], centroids[:, 1], c='red', s=50)
 
# 3: Scatter plot
plt.scatter('x','y', color='green')
plt.title('x Vs y', fontsize=14)
plt.xlabel('Unemployment Rate', fontsize=14)
plt.ylabel('Stock Index Price', fontsize=14)
plt.grid(True)
#plt.show()

# 4 
root= tk.Tk()
canvas1 = tk.Canvas(root, width = 100, height = 100)
canvas1.pack()

label1 = tk.Label(root, text=centroids, justify = 'center')
canvas1.create_window(70, 50, window=label1)
figure1 = plt.Figure(figsize=(5,4), dpi=100)

ax1 = figure1.add_subplot(111)
ax1.scatter(df['x'], df['y'], c= kmeans.labels_.astype(float), s=50, alpha=0.5)
ax1.scatter(centroids[:, 0], centroids[:, 1], c='red', s=50)

scatter1 = FigureCanvasTkAgg(figure1, root) 
scatter1.get_tk_widget().pack(side=tk.LEFT, fill=tk.BOTH)

root.mainloop()
