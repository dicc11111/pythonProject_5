from json import dumps

results = [{}, {}]

try:
    with open('test_7.txt', encoding='utf-8') as fhs:
        lines = fhs.readlines()

    for line in lines:
        name, _, proceeds, expenses = line.split()
        results[0][name] = int(proceeds) - int(expenses)

    results[1]['average_profit'] = round(
        sum(
            profit for _, profit in results[0].items() if profit > 0
        ) / len(results[0])
    )

    with open('test_7.json', "w", encoding='utf-8') as fhd:
        fhd.write(dumps(results))
except IOError as e:
    print(e)
except ValueError:
    print("Неконсистентные даkнные")

    print(results)
