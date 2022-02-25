# THIS IS A PROGRAM FOR CLUSTERING.

from clustering import clustering  # 自作モジュール (clustering.py) と clusteringクラス の import

import pandas as pd
import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import filedialog, image_names, ttk, messagebox
import os
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from matplotlib.figure import Figure
import numpy as np


# clustering の子クラスとして、クラスタリング結果をプロットするための plot_clustering クラスを作成
class plot_clustering(clustering):
    # --- 元データのプロットのための関数 -------------------------------------------------------------
    def data_plot(file_name):
        fig = plt.Figure()  # Figureインスタンスを生成
        print (file_name) 

        csv_input = pd.read_csv(filepath_or_buffer= file_name, encoding= "utf8", sep= ",")  # file_name を指定して csv を読み込む
        ax = fig.add_subplot(111)
        ax.set_aspect('equal')  # aspect ratio is equal
        ax.set_xlim([-500,1500])  # set x axis value limit
        ax.set_ylim([-500,1500])  # set y axis value limit
        ax.set_xlabel('x')  # name x label "x"
        ax.set_ylabel('y')  # name y label "y"
        ax.scatter(csv_input["X"], csv_input["Y"], c='red')
        ax.grid()
        ax.plot()
        fig.savefig("original_" + file_name + ".png")

        original_data_label = tk.Label(text= "original")  # 元データラベルの作成
        original_data_label.grid(row= 7, column= 0, sticky= 'news', padx= 5, pady= 5)
        canvas_original = FigureCanvasTkAgg(fig, display)
        canvas_original.get_tk_widget().grid(row= 8, column= 0, sticky= 'news', padx= 5, pady= 5)
    # -----------------------------------------------------------------------------------------------------------

    # --- クラスタリング済みデータのプロットのための関数 ---------------------------------------------------------------
    def plot_cluster_list(file_name, cluster_list, color, method_name):
        # Figureインスタンスを生成
        fig = plt.Figure()

        ax = fig.add_subplot(111)
        ax.set_aspect('equal')
        ax.set_xlim([-500,1500])
        ax.set_ylim([-500,1500])

        for i in range(0, len(cluster_list)):  # cluster_list に含まれるクラスターの数だけループする
            cluster = cluster_list[i]  # cluster_list から1つずつ取り出す
            c = color[i % len(color)]  # プロットの色
            csv_input = pd.DataFrame(np.array(cluster))  # プロット用データの準備
            ax.scatter(csv_input[0], csv_input[1], c=c)

        ax.set_xlabel('x')
        ax.set_ylabel('y')
        ax.grid()
        ax.plot()
        fig.savefig(method_name + "_" + file_name + ".png")

        return fig
    # -----------------------------------------------------------------------------------------------------------

    # --- 最短距離法 -----------------------------------------------------------------------------------------------------------
    def shortest_method(num_of_cluster, file_name):
        csv_input = pd.read_csv(filepath_or_buffer= file_name, encoding= "utf8", sep= ",")  # file_name を指定して csv を読み込む
        cluster_list = clustering.make_1elem_cluster(csv_input)

        while len(cluster_list) > num_of_cluster:
            cluster_list = clustering.shortest(cluster_list)

        return cluster_list
    # ---------------------------------------------------------------------------------------------------------------------------------------------

    # --- 最長距離法 ----------------------------------------------------------------------------------------------------------
    def longest_method(num_of_cluster, file_name):
        csv_input = pd.read_csv(filepath_or_buffer= file_name, encoding= "utf8", sep= ",")  # file_name を指定して csv を読み込む
        cluster_list = clustering.make_1elem_cluster(csv_input)

        while len(cluster_list) > num_of_cluster:
            cluster_list = clustering.longest(cluster_list)

        return cluster_list
    # ---------------------------------------------------------------------------------------------------------------------------------------------

    # --- 重心法 -----------------------------------------------------------------------------------------------------------------------
    def balance_method(num_of_cluster, file_name):
        csv_input = pd.read_csv(filepath_or_buffer= file_name, encoding= "utf8", sep= ",")  # file_name を指定して csv を読み込む
        cluster_list = clustering.make_1elem_cluster(csv_input)

        while len(cluster_list) > num_of_cluster:
            cluster_list = clustering.balance(cluster_list)

        return cluster_list
    # ---------------------------------------------------------------------------------------------------------------------------------------------


# 関数の定義
# --- 利用するデータファイルを選択するための関数 ----------------------------------------------------------------------------------------------------------------------------------------------------
def select_mode():  # この関数は使いません。file_select関数で参照ボタンからファイルを選択できるようになっています。
	print("1. m2sd50.csv\n2. m2sd200.csv\n3. m3sd50.csv\n4. m3sd200.csv\n5. m4sd50.csv\n6. m4sd200.csv\n7. m5sd50.csv\n8. m5sd200.csv\n9. m9sd50.csv\n10. m9sd200.csv \n")
	mode = input("mode = ")

	if (mode == "1"):
		csv_input = pd.read_csv(filepath_or_buffer="m2sd50.csv", encoding="utf8", sep=",")
		print("データファイル ： m2sd50.csv")

	elif (mode == "2"):
		csv_input = pd.read_csv(filepath_or_buffer="m2sd200.csv", encoding="utf8", sep=",")
		print("データファイル ： m2sd200.csv")

	elif (mode == "3"):
		csv_input = pd.read_csv(filepath_or_buffer="m3sd50.csv", encoding="utf8", sep=",")
		print("データファイル ： m3sd50.csv")

	elif (mode == "4"):
		csv_input = pd.read_csv(filepath_or_buffer="m3sd200.csv", encoding="utf8", sep=",")
		print("データファイル ： m3sd200.csv")

	elif (mode == "5"):
		csv_input = pd.read_csv(filepath_or_buffer="m4sd50.csv", encoding="utf8", sep=",")
		print("データファイル ： m4sd50.csv")

	elif (mode == "6"):
		csv_input = pd.read_csv(filepath_or_buffer="m4sd200.csv", encoding="utf8", sep=",")
		print("データファイル ： m4sd200.csv")

	elif (mode == "7"):
		csv_input = pd.read_csv(filepath_or_buffer="m5sd50.csv", encoding="utf8", sep=",")
		print("データファイル ： m5sd50.csv")

	elif (mode == "8"):
		csv_input = pd.read_csv(filepath_or_buffer="m5sd200.csv", encoding="utf8", sep=",")
		print("データファイル ： m5sd200.csv")

	elif (mode == "9"):
		csv_input = pd.read_csv(filepath_or_buffer="m9sd50.csv", encoding="utf8", sep=",")
		print("データファイル ： m9sd50.csv")

	elif (mode == "10"):
		csv_input = pd.read_csv(filepath_or_buffer="m9sd200.csv", encoding="utf8", sep=",")
		print("データファイル ： m9sd200.csv")

	return csv_input
# -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


# === Functions for GUI action =============================================================
# ファイル参照ボタンを押したときに実行する関数
def file_select():
    dir = '/Users/kosei/yama/4EJ/4年　情報工学実験/10　クラスタリング/program4clustering'  # 初期参照フォルダ
    extension = [("すべて", "*"), ("CSV","*.csv")]  # select file extension
    file_path = tk.filedialog.askopenfilename(filetypes= extension, initialdir= dir)  # get file path
    file_name = os.path.basename(file_path)  # get file name
    ref_box.delete(0, tk.END)  # 入力ボックスの初期化（空白にする）
    ref_box.insert(tk.END, file_name)  # show file name（入力ボックスにファイル名を入力）
    os.chdir(os.path.dirname(os.path.abspath(file_path)))
    print(file_path) # print
    print(file_name) # print
    plot_clustering.data_plot(file_name)

# 出力ボタンが押されたときに画像を表示するための関数
def draw():
    file_name = ref_box.get()  # get file name by getting ref_box value
    scale_value = scale.get()  # get scale value
    num_of_cluster = scale_value
    cluster_list_shortest_method = plot_clustering.shortest_method(num_of_cluster, file_name)
    cluster_list_longest_method = plot_clustering.longest_method(num_of_cluster, file_name)
    cluster_list_balance_method = plot_clustering.balance_method(num_of_cluster, file_name)
    fig_shortest = plot_clustering.plot_cluster_list(file_name, cluster_list_shortest_method, color, "shortest")
    fig_longest = plot_clustering.plot_cluster_list(file_name, cluster_list_longest_method, color, "longest")
    fig_balance = plot_clustering.plot_cluster_list(file_name, cluster_list_balance_method, color, "balance")

    shortest_method_name_label = tk.Label(text= 'shortest')  # shortest_method_name ラベルの作成
    shortest_method_name_label.grid(row= 7, column= 1, sticky= 'news', padx= 5, pady= 5)
    canvas_shortest = FigureCanvasTkAgg(fig_shortest, display)
    canvas_shortest.get_tk_widget().grid(row= 8, column= 1, sticky= 'news', padx= 5, pady= 5)

    longest_method_name_label = tk.Label(text= 'longest')  # longest_method_name ラベルの作成
    longest_method_name_label.grid(row= 9, column= 0, sticky= 'news', padx= 5, pady= 5)
    canvas_longest = FigureCanvasTkAgg(fig_longest, display)
    canvas_longest.get_tk_widget().grid(row= 10, column= 0, sticky= 'news', padx= 5, pady= 5)

    balance_method_name_label = tk.Label(text= 'balance')  # balance_method_name ラベルの作成
    balance_method_name_label.grid(row= 9, column= 1, sticky= 'news', padx= 5, pady= 5)
    canvas_balance = FigureCanvasTkAgg(fig_balance, display)
    canvas_balance.get_tk_widget().grid(row= 10, column= 1, sticky= 'news', padx= 5, pady= 5)

# ==============================================================================================



# === main ========================================================================================================================

# GUI setting
display = tk.Tk()  # create instance (create main window)
display.geometry('1000x1200')  # set window size
display.title('10 クラスタリング')  # set title

color = ['blue', 'red', 'green', 'orange', 'blueviolet', 'gray', 'magenta']  # グラフに使用する色

# ファイル選択部分
# infoラベルの作成
select_file_label = tk.Label(text= "1. ファイル選択")  # create label for selecting file
select_file_label.grid(row= 0, column= 0, sticky= 'nws', padx= 5, pady= 5)  # position detail setting
# 参照先のファイル名の入力欄の作成
ref_box = tk.Entry(width= 30)
ref_box.grid(row= 1, column= 0, sticky= 'news', padx= 5, pady= 5)
# 参照ボタンの作成
ref_button = tk.Button(text= "参照", command= file_select)
ref_button.grid(row= 1, column= 1, sticky= 'nws', padx= 5, pady= 5)

# 詳細設定（クラスタ数の指定）部分
# infoラベルの作成
detail_setting_label = tk.Label(text= "2. 詳細設定")
detail_setting_label.grid(row= 2, column= 0, sticky= 'nws', padx= 5, pady= 5)
# scaleの作成
scale_label = tk.Label(text= "▷ クラスタ数")
scale_label.grid(row= 3, column= 0, sticky= 'nws')
scale = tk.Scale(orient= tk.HORIZONTAL, from_= 2, to= 100)
scale.grid(row= 4, column= 0, sticky= 'news')

# グラフ出力部分
# infoラベルの作成
graph_label = tk.Label(text= "3. グラフ")
graph_label.grid(row= 5, column= 0, sticky= 'nws', padx= 5, pady= 5)
# 出力ボタン
output_button = tk.Button(text= "グラフ出力", command= draw)
output_button.grid(row= 6, column= 0, sticky= 'nws', padx= 5, pady= 5)

# even if this program is finished, the window never disappears
display.mainloop()
# ========================================================================================
