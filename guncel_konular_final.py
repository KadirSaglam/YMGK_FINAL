import matplotlib.pyplot as plt
import pandas as pd

veri=pd.read_excel("C:/Users/kadir/OneDrive/Desktop/güncel_konular_final/normalize_bayburt_kis.xlsx")
veri2=pd.read_excel("C:/Users/kadir/OneDrive/Desktop/güncel_konular_final/normalize_bayburt_yaz.xlsx")


veri["PM10"] = veri["PM10 ( µg/m³ )"].astype("float")
veri["SO2"] = veri["SO2 ( µg/m³ )"].astype("float")
veri["NO2"] = veri["NO2 ( µg/m³ )"].astype("float")
veri["NOX"] = veri["NOX ( µg/m³ )"].astype("float")
veri["O3"] = veri["O3 ( µg/m³ )"].astype("float")

veri2["PM10"] = veri2["PM10 ( µg/m³ )"].astype("float")
veri2["SO2"] = veri2["SO2 ( µg/m³ )"].astype('float')
veri2["NO2"] = veri2["NO2 ( µg/m³ )"].astype("float")
veri2["NOX"] = veri2["NOX ( µg/m³ )"].astype("float")
veri2["O3"] = veri2["O3 ( µg/m³ )"].astype("float")


plt.figure(figsize=(25,12))
plt.subplot(2,3,1)   
plt.plot(veri.Tarih,veri.PM10,color="blue",linewidth=1,linestyle="-",marker="*",markersize=1,label="PM10-Kış",alpha=0.9)
plt.plot(veri2.Tarih,veri2.PM10,color="red",linewidth=1,linestyle="-",marker="*", markersize=1,label="PM10-Yaz",alpha=0.9)
plt.xlabel("Tarih")
plt.ylabel("PM10 Oranı")
plt.title("Bayburt PM10 Grafiği")
plt.grid()
plt.legend()


plt.subplot(2,3,2)   
plt.plot(veri.Tarih,veri.SO2,color="blue",linewidth=1,linestyle="-",marker="*",markersize=3,label="SO2-Kış",alpha=0.9)
plt.plot(veri2.Tarih,veri2.SO2,color="red",linewidth=1,linestyle="-",marker="*",markersize=3,label="SO2-Yaz",alpha=0.9)
plt.xlabel("Tarih")
plt.ylabel("SO2 Oranı")
plt.title("Bayburt SO2 Grafiği")
plt.grid()
plt.legend()

plt.subplot(2,3,3)   
plt.plot(veri.Tarih,veri.NO2,color="blue",linewidth=1,linestyle="-",marker="*",markersize=3,label="NO2-Kış",alpha=0.9)
plt.plot(veri2.Tarih,veri2.NO2,color="red",linewidth=1,linestyle="-",marker="*",markersize=3,label="NO2-Yaz",alpha=0.9)
plt.xlabel("Tarih")
plt.ylabel("NO2 Oranı")
plt.title("Bayburt NO2 Grafiği")
plt.grid()
plt.legend()


plt.subplot(2,3,4)
plt.plot(veri.Tarih,veri.NOX,color="blue",linewidth=1,linestyle="-",marker="*",markersize=3,label="NOX-Kış",alpha=0.9)
plt.plot(veri2.Tarih,veri2.NOX,color="red",linewidth=1,linestyle="-",marker="*",markersize=3,label="NOX-Yaz",alpha=0.9)
plt.xlabel("Tarih")
plt.ylabel("NOX Oranı")
plt.title("Bayburt NOX Grafiği")
plt.grid()
plt.legend()

plt.subplot(2,3,5)
plt.plot(veri.Tarih,veri.O3,color="blue",linewidth=1,linestyle="-",marker="*",markersize=3,label="O3-Kış",alpha=0.9)
plt.plot(veri2.Tarih,veri2.O3,color="red",linewidth=1,linestyle="-",marker="*",markersize=3,label="O3-Yaz",alpha=0.9)
plt.xlabel("Tarih")
plt.ylabel("O3 Oranı")
plt.title("Bayburt O3 Grafiği")
plt.grid()
plt.legend()

plt.show()