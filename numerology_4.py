import streamlit as st
import pandas as pd
compat_dict = {"A" : {1 : [4, 5, 7], 2 : [4, 6, 22], 3 : [3, 6, 8, 9], 4 : [1, 2, 7, 8], 5 : [1], 6 : [2, 3, 6, 9], 7 : [1, 4, 22], 8 : [4, 22], 9 : [3, 6, 9], 11 : [22], 22 : [2, 7, 8, 11]},
              "B" : {1 : [1, 8], 2 : [2, 3, 7, 9, 11], 3 : [2, 22], 4 : [4, 6, 22], 5 : [5, 9, 11], 6 : [4, 11], 7 : [2, 7, 11], 8 : [1, 11], 9 : [2, 5, 7, 11, 22], 11 : [2, 5, 6, 7, 8, 9, 11], 22 : [3, 4, 9, 22]},
              "C" : {1 : [2, 6, 22], 2 : [1, 5], 3 : [4, 5, 7, 11], 4 : [3, 11], 5 : [2, 3, 4, 6, 7, 22], 6 : [1, 5, 7, 8], 7 : [3, 5, 6, 9], 8 : [3, 6, 8, 9], 9 : [4, 8], 11 : [3, 4], 22 : [1, 5]},
              "D" : {1 : [3, 9, 11], 2 : [8], 3 : [1], 4 : [5, 9], 5 : [8], 6 : [22], 7 : [8], 8 : [2, 5, 7], 9 : [1], 11 : [1], 22 : [6]}}
def compatability(x, y):
    if y in compat_dict["A"][x]:
        return "A"
    elif y in compat_dict["B"][x]:
        return "B"
    elif y in compat_dict["C"][x]:
        return "C"
    elif y in compat_dict["D"][x]:
        return "D"
def life_pn_func(date_1):
    date_1 = "-".join((date_1.split("/"))[::-1])
    life_pn = sum([int(j) for j in (date_1.split(' '))[0].split('-')])
    while life_pn >= 10:
        life_pn = sum([int(k) for k in str(life_pn)])
    date = date_1.split(' ')[0].split('-')
    if life_pn == 2 or life_pn == 4:
        date = sum([int(i) for i in date])
        date = sum([int(i) for i in str(date)])
        if date in [2, 4, 11, 22]:
            life_pn = date
    return life_pn
def compat_func(date_a, date_b):
    a = life_pn_func(date_a)
    b = life_pn_func(date_b)
    return compatability(a, b)
name_list = ["Guddu", "Kunu", "Mamia", "Bapa", "Adi"]
date_list = ["07/02/2005", "27/09/2008", "02/10/1979", "17/08/1973", "01/11/2006"]
df = pd.DataFrame()
df[" "] = name_list
count = 0
for i in date_list:
    col_list = []
    for j in date_list:
        col_list.append(compat_func(j, i))
    df[name_list[count]] = pd.Series(col_list)
    count += 1
df = df.set_index(" ")
def apply_color(val):
    if val == "A":
        return "background-color: red"
df = df.style.apply(apply_color)
st.table(df)
