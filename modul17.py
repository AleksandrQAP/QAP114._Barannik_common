money=float(input("Введите величину предполагаемого вклада:"))
per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
deposit=[a*(money/100) for a in per_cent.values()]
print ('Процент по банкам', deposit)
print ("Максимальный полученный процент составляет", max(deposit))