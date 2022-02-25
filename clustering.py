# THIS IS A PROGRAM FOR CLUSTERING.

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import math
import japanize_matplotlib

# clusteringクラスの作成
class clustering():
    # --- 2点間の距離を求める関数 -------------------------------------------------------------------------
    def between_distance(p1, p2):
        return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)
    # ---------------------------------------------------------------------------------------------------------------------------------

    # --- 要素が1つのクラスターを作成する関数 ------------------------------------------------------------------------------------------
    def make_1elem_cluster(csv_input):
        lst = csv_input.values.tolist()
        
        cluster_list = []  # クラスターのためのリストを宣言

        for row in lst:
            cluster_list.append([row[1:]])  # x と y をリストに追加

        # print(cluster_list)
        return cluster_list
    # ----------------------------------------------------------------------------------------------------------------------------------

    # --- クラスター間の最短距離を求める関数 ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    def calc_shortest_distance(cluster1, cluster2):
        if len(cluster1) <= 0 or len(cluster2) <= 0:
            return 0

        min = clustering.between_distance(cluster1[0], cluster2[0])  # 1番目と2番目のクラスター間の距離を min として初期設定
        for i in range(len(cluster1)):  # 2つのクラスターに含まれる全ての要素の中で一番近い要素を探す
            for j in range(len(cluster2)):  # 例えば、cluster1 = [0, 1, 2] , cluster2 = [3, 4] なら、cluster1[0] と cluster2[0] の距離を計算し、cluster1[0] と cluster2[1]　の距離を計算し・・・
                distance = clustering.between_distance(cluster1[i], cluster2[j])  # クラスター間の距離を計算
                if min > distance:  # 計算した距離が min よりも小さかったら
                    min = distance  # min として設定

        return min
    # -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

    # --- 最短距離法でクラスターに分類する関数 -------------------------------------------------------------------------------------------------------------------------------------------------------------
    def shortest(cluster_list):  # クラスター間の距離を計算し、距離でソートして、最も距離の近い2つのクラスターをマージする
        if len(cluster_list) <= 1:
            return cluster_list

        distance_list = []  # クラスター番号と距離を保持するためのリストを宣言

        for i in range(0, len(cluster_list)):  # クラスターリストの全ての要素の組み合わせについてループを回す
            for j in range(i + 1, len(cluster_list)):  # cluster_list[i] と cluster_list[j]、cluster_list[i] と cluster_list[j+1] ・・・のようにループ
                distance = clustering.calc_shortest_distance(cluster_list[i], cluster_list[j])  # クラスター間の最小距離を算出
                distance_list.append(((cluster_list[i], cluster_list[j]), distance))  # 最小距離となるクラスター番号と最小距離を distance_list に格納

        sorted_distance_list = sorted(distance_list, key=lambda d: d[1])  # クラスター間の距離でソート
        
        merge_list = sorted_distance_list[0][0]
        cluster1 = merge_list[0]
        cluster2 = merge_list[1]
        cluster1.extend(cluster2)  # 距離の近い2つのクラスターをマージする

        cluster_list.remove(cluster2)  # 元のリストからクラスターBを削除する

        # print(merge_list)
        # print(cluster1)
        # print(cluster2)

        return cluster_list
    # ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

    # --- クラスター間の最長距離を求める関数 ---------------------------------------------------------------------------------------------------------------------
    def calc_longest_distance(cluster1, cluster2):
        if len(cluster1) <= 0 or len(cluster2) <= 0:
            return 0

        max = clustering.between_distance(cluster1[0], cluster2[0])  # 1番目と2番目のクラスター間の距離を max として初期設定
        for i in range(len(cluster1)):  # 2つのクラスターに含まれる全ての要素の中で一番遠い要素を探す
            for j in range(len(cluster2)):
                distance = clustering.between_distance(cluster1[i], cluster2[j])  # クラスター間の距離を計算
                if max < distance:  # 計算した距離が max よりも大きかったら
                    max = distance  # max として設定

        return max
    # ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------

    # --- 最長距離法でクラスターに分類する関数 ---------------------------------------------------------------------------------------------------------------------------------------
    def longest(cluster_list):
        if len(cluster_list) <= 1:
            return cluster_list

        distance_list = []  # クラスター番号と距離を保持するためのリストを宣言

        for i in range(0, len(cluster_list)):  # クラスターリストの全ての要素の組み合わせについてループを回す
            for j in range(i + 1, len(cluster_list)):
                distance = clustering.calc_longest_distance(cluster_list[i], cluster_list[j])  # クラスター間の最長距離を算出
                distance_list.append(((cluster_list[i], cluster_list[j]), distance))  # 最長距離となるクラスター番号と最長距離を distance_list に格納

        sorted_distance_list = sorted(distance_list, key=lambda d: d[1])  # クラスター間の距離でソート

        merge_list = sorted_distance_list[0][0]
        cluster1 = merge_list[0]
        cluster2 = merge_list[1]
        cluster1.extend(cluster2)  # 距離の近い2つのクラスターをマージする

        cluster_list.remove(cluster2)  # 元のリストからクラスターBを削除する

        return cluster_list
    # -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

    # --- クラスターの重心を求める関数 --------------------------
    def balance_of_cluster(cluster):
        x = 0
        y = 0

        for p in cluster:
            x = x + p[0]
            y = y + p[1]

        balance_of_x = x / len(cluster)
        balance_of_y = y / len(cluster)

        return (balance_of_x, balance_of_y)
    # -----------------------------------------------------------------------

    # --- クラスターの重心間の距離を求める関数 -------------------------------------------------------------------------------------------------------------------------------------------
    def calc_center(cluster1, cluster2):
        if len(cluster1) <= 0 or len(cluster2) <= 0:
            return 0

        return clustering.between_distance(clustering.balance_of_cluster(cluster1), clustering.balance_of_cluster(cluster2))  # cluster1 と cluster2 の重心間の距離を算出
    # -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

    # --- 重心法でクラスターに分類する関数 ---------------------------------------------------------------------------------------------------------------------------------------
    def balance(cluster_list):
        if len(cluster_list) <= 1:
            return cluster_list

        distance_list = []  # クラスター番号と距離を保持するためのリストを宣言

        for i in range(0, len(cluster_list)):  # クラスターリストの全ての要素の組み合わせについてループを回す
            for j in range(i + 1, len(cluster_list)):
                distance = clustering.calc_center(cluster_list[i], cluster_list[j])  # クラスターの重心間距離を算出
                distance_list.append(((cluster_list[i], cluster_list[j]), distance))  # クラスター番号と重心間距離を distance_list に格納

        sorted_distance_list = sorted(distance_list, key=lambda d: d[1])  # クラスター間の距離でソート

        merge_list = sorted_distance_list[0][0]
        cluster1 = merge_list[0]
        cluster2 = merge_list[1]
        cluster1.extend(cluster2)  # 距離の近い2つのクラスターをマージする

        cluster_list.remove(cluster2)  # 元のリストからクラスターBを削除する

        return cluster_list
    # ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

    # --- クラスタリング済みデータのプロットのための関数 ------------------------------------------d---------------------
    def plot_cluster_list(cluster_list, color, title = None):
        ax = plt.axes()
        ax.set_aspect('equal')
        ax.set_xlim([-500, 1500])
        ax.set_ylim([-500, 1500])

        for i in range(0, len(cluster_list)):  # cluster_list に含まれるクラスターの数だけループする
            cluster = cluster_list[i]  # cluster_list から1つずつ取り出す
            c = color[i % len(color)]  # プロットの色
            csv_input = pd.DataFrame(np.array(cluster))  # プロット用データの準備
            plt.scatter(csv_input[0], csv_input[1], c=c)

        plt.grid()
        plt.title(title)
        plt.show()
    # -----------------------------------------------------------------------------------------------------------
