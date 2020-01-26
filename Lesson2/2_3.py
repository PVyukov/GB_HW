number = int(input('Enter number from 1 to 12:'))
seasons = {'зима': [12, 1, 2], 'весна': [3, 4, 5], 'лето': [6, 7, 8], 'осень': [9, 10, 11]}
for i in seasons.items():
    if number in i[1]:
        season = i[0]
print(season)