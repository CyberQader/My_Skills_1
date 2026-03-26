pepoles = {
    'abood':{
        'Js':'80%',
        'Html':'70%',
        'MySql':'77%',
        'Python':'90%',
    },
    'ahmed':{
        'Js': '56%',
        'Html': '64%',
        'MySql': '77%',
        'Python': '88%',
    },
    'mazen':{
        'Js': '66%',
        'Html': '77%',
        'MySql': '96%',
        'Python': '97%',

    },
}
for name in pepoles:
    print(f'Skills And Progrees For {name.upper()} Is : ')
    for skill in pepoles[name]:
        print(f'{skill.upper()}>>>>>>>{pepoles[name][skill]}')
