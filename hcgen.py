import random

words_a = [
    'verbal',
    'nuclear',
    'dead',
    'toxic',
    'brutal',
    'infested',
    'aggression',
    'atomic',
    'lifeless',
    'savage',    
    'infected',
    'violent',    
    'radioactive',
    'lifeless',   
    'cruel',       
    'flesh',    
    'infected', 
    'hostile',    
    'nuclear',
    'contaminated'

]

words_b = [
    'vanguard',
    'onslaught',
    'adolescence',
    'intersection',
    'battle',
    'threat',
    'attack',
    'adolescents',
    'youth',
    'body',
    'cross',
    'front',
    'assault',
    'pride',
    'message',
    'assault',
]

def hc_name():
    name = f"{random.choice(words_a).capitalize()} {random.choice(words_b).capitalize()}"
    return name

if __name__ == "__main__":
    x = int(input("How Many Names: "))
    for i in range(x):
        print(hc_name())
