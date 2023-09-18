def step2_umbrella():
    print(
        'На улице светило солнце ☀️, и утка благополучно добралась до бара.\n'
        'Что она будет пить?'
    )
    drink = ''
    drinks = {'сок': '🧃', 'чай': '🍵', 'кофе': '☕'}
    while drink not in drinks:
        print('Выберите: {}/{}/{}'.format(*drinks))
        drink = input()
    print(
        '{} {} был очень вкусным.'.format(drink.capitalize(), drinks[drink]),
        'Оставить чаевые?'
    )
    while True:
        print('Выберите: да/нет')
        tip = input()
        if tip == 'да':
            print(
                'Бармен-попугай остался очень доволен и поделился с уткой своими знаниями о языке Python.\n'
                'Какой познавательный поход в бар!'
            )
            break
        elif tip == 'нет':
            print(
                'Утка отправилась домой и стала делать домашку по Python. Было трудно, но она справилась!'
            )
            break
    return True

def step2_no_umbrella():
    print(
        'Утка прошла полпути, когда вдруг пошел дождик 🌧️.\n'
        'К счастью, утка встретила своего друга - пингвина 🐧.\n'
        'Какого цвета зонтик у пингвина? '
        )
    umbrella_color = ''
    umbrella_colors = {'красный': '🌂', 'синий': '☂️'}
    while umbrella_color not in umbrella_colors:
        print('Выберите: {}/{}'.format(*umbrella_colors))
        umbrella_color = input()

    print(
        'Утка и пингвин благополучно добрались до бара. '
        'От дождя их спас {} зонтик {}.'.format(umbrella_color, umbrella_colors[umbrella_color])
    )
    return True