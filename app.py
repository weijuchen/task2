import tkinter as tk
from tkinter import ttk

# import pymysql
import sqlite3
import csv
import matplotlib.pyplot as plt
import pandas as pd
from datetime import datetime, timezone, timedelta

# D:\D_Download\zap_database

conn = sqlite3.connect("zap_database")
cursor = conn.cursor()


def query_info():

    query = "SELECT pm25,temperature,humidity,create_at FROM airqualitydata"
    cursor.execute(query)
    data = cursor.fetchall()
    print(data)
    # for row in data:
    #     print(row)
    # return data

    with open("mj.csv", "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow([header[0] for header in cursor.description])
        writer.writerows(data)
    print("匯出成功！")


def plot_bar_chart():
    db_data = pd.read_csv("mj.csv")

    df = pd.DataFrame(db_data)
    df["create_at"] = pd.to_datetime(df["create_at"], unit="ms")
    df["create_at"] = df["create_at"].dt.strftime("%Y-%m-%d %H %M")
    # df["create_at"] = pd.to_datetime(df["create_at"].astype(int), unit="s")
    # df["create_at"] = pd.to_datetime(df["create_at"].astype(str), format="%Y%m%d%H%M%S")
    # df["create_at"] = pd.to_datetime(df["create_at"], unit="s")
    # df["create_at"] = pd.to_datetime(df["create_at"], format="%Y%m%d%H%M%S")

    X = list(df.iloc[:, 3])
    Y = list(df.iloc[:, 1])

    # Plot the data using bar() method
    plt.bar(X, Y, color="g")
    plt.title("Temperature over time")
    plt.xlabel("Time")
    plt.ylabel("Temperature")
    plt.xticks(rotation=45)

    plt.tight_layout()
    plt.savefig(
        "bar_chart.jpg", format="jpg", dpi=300
    ) 
    plt.show()



root = tk.Tk()
root.title("GUI Ver1 @v0.02 2024-11-11")
root.geometry("800x400")


notebook = ttk.Notebook(root)


tab1 = ttk.Frame(notebook)
notebook.add(tab1, text="page 1")


button1_1 = tk.Button(
    tab1,
    text="Step 1",
    font=("Arial", 16),
    command=query_info,
    # command=lambda: print("Page 1 按鈕 1 被點擊"),
)
# button1_1.pack(side='left',pady=5,padx=10)
button1_1.grid(column=0, row=0, padx=10, pady=10)

button1_2 = tk.Button(
    tab1,
    text="Step 2",
    font=("Arial", 16),
    command=plot_bar_chart,
    # command=lambda: print("Page 1 按鈕 2 被點擊"),
)
button1_2.grid(column=1, row=0, padx=10, pady=10)
# button1_2.pack(side="left", pady=5, padx=10)
button1_3 = tk.Button(
    tab1,
    text="Step 3",
    font=("Arial", 16),
    command=lambda: print("Page 1 按鈕 3 被點擊"),
)
button1_3.grid(column=2, row=0, padx=10, pady=10)
# button1_3.pack(side="left", pady=5, padx=10)
button1_4 = tk.Button(
    tab1,
    text="Step 4",
    font=("Arial", 16),
    command=lambda: print("Page 1 按鈕 4 被點擊"),
)
button1_4.grid(column=0, row=1, padx=10, pady=10)
# button1_4.pack(side="left", pady=5, padx=10)

button1_5 = tk.Button(
    tab1,
    text="Step 5",
    font=("Arial", 16),
    command=lambda: print("Page 1 按鈕 5 被點擊"),
)
button1_5.grid(column=1, row=1, padx=10, pady=10)
# button1_5.pack(side="left", pady=5, padx=10)


button1_6 = tk.Button(
    tab1,
    text="15 minutes",
    font=("Arial", 16),
    # command=plot_bar_chart(15),
    command=lambda: print("間隔時間15分鐘"),
)
button1_6.grid(column=0, row=10, padx=10, pady=10)

button1_7 = tk.Button(
    tab1,
    text="30 minutes",
    font=("Arial", 16),
    command=lambda: print("間隔時間30分鐘"),
)
button1_7.grid(column=1, row=10, padx=10, pady=10)

button1_8 = tk.Button(
    tab1,
    text="60 minutes",
    font=("Arial", 16),
    command=lambda: print("間隔時間60分鐘"),
)
button1_8.grid(column=2, row=10, padx=10, pady=10)


tab2 = ttk.Frame(notebook)
notebook.add(tab2, text="page2")


button2_1 = tk.Button(
    tab2,
    text="按鈕 2",
    font=("Arial", 16),
    command=lambda: print("Page 2 按鈕 2 被點擊"),
)
button2_1.pack(pady=20)


notebook.pack(expand=True, fill="both")


root.mainloop()
