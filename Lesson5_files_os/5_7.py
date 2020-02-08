import json as js


def profit(revenue, cost):
    return int(revenue) - int(cost)


companies = []
average_profit = 0
all_profit = {}
with open('5_7_data_in', encoding='utf-8') as f:
    for company in f:
        company = company.strip().split()
        prof_com = profit(company[2], company[3])
        all_profit[company[0]] = prof_com
        if prof_com > 0:
            average_profit += prof_com
    companies.append(all_profit)
    companies.append({'average_profit': average_profit})

with open('5_7_data_out', 'w') as f:
    js.dump(companies, f)

'''
Test
    #     f.write(companies)
    #     f.write()
    # print(companies)
    # companies = js.dumps(companies)
    # print(companies)
'''