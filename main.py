import csv


def rows_getter() -> list:
    """ Returns info from 'Corp_Summary.csv' as a list of dicts. """
    with open('Corp_Summary.csv', encoding='utf-8') as f:
        rows = list(csv.DictReader(f, delimiter=';'))
        return rows


def hierarchy_printer() -> None:
    """ Prints departments and their respective subdepartments. """
    rows = rows_getter()
    departments = set([row['Департамент'] for row in rows])
    departments_info = {
        d: list(set([row['Отдел'] for row in rows if row['Департамент'] == d]))
        for d in departments}
    print('{:^20}|{:^20}'.format('Департамент', 'Отделы'))
    print('_' * 45)
    for d in departments_info:
        print('{:^20}|{:^20}'.format(d, departments_info[d][0]))
        for sub in departments_info[d][1:]:
            print('{:^20}|{:^20}'.format('', sub))
        print('_' * 45)


def report_getter() -> list:
    """ Returns a list of dicts with a summary for each department. """
    rows = rows_getter()
    departments = set([row['Департамент'] for row in rows])
    d_salaries = {
        d: [int(row['Оклад']) for row in rows if row['Департамент'] == d]
        for d in departments}
    return [
        {
            'Департамент': d,
            'Численность': len(d_salaries[d]),
            'Мин. оклад': min(d_salaries[d]),
            'Макс. оклад': max(d_salaries[d]),
            'Средний оклад': round(sum(d_salaries[d]) / len(d_salaries[d]), 2)
        } for d in d_salaries
    ]


def report_printer() -> None:
    """ Prints a summary from report_getter as a table. """
    info = report_getter()
    print('{:^20}|{:^20}|{:^20}|{:^20}|{:^20}'.format(*info[0].keys()))
    print('_' * 100)
    for info_row in info:
        print('{:^20}|{:^20}|{:^20}|{:^20}|{:^20}'.format(*info_row.values()))


def report_saver() -> None:
    """ Saves a summary from report_getter to 'Corp_Summary_Report.csv' """
    info = report_getter()
    with open('Corp_Summary_Report.csv', 'w') as f:
        writer = csv.DictWriter(f, fieldnames=list(info[0].keys()))
        writer.writeheader()
        for row in info:
            writer.writerow(row)


if __name__ == '__main__':
    option = ''
    while option not in range(1, 4):
        print(
            'Выберите:\n'
            '1. Вывести иерархию департаментов\n'
            '2. Вывести сводный отчет\n'
            '3. Сохранить сводный отчет'
        )
        option = int(input())
    if option == 1:
        hierarchy_printer()
    elif option == 2:
        report_printer()
    else:
        report_saver()
