a = str(input())
lst_r = ["алгебра", "число", "процент", "отрицательный", "положительный"]
lst_a = ["algebra", "number ", "percent", "negative", "positive"]
lst_g = ["die Algebra", "die Zahl", "das Prozent", "negativ", "positiv"]
for item in lst_r:
    item = a
    if item in lst_r:
        print("англ - " + str(lst_a[lst_r.index(a)]))
        print("нем - " + str(lst_g[lst_r.index(a)]))
        break


