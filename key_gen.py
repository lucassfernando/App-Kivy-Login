from random import randint



def generate_key(total_characters):
    
    key = ''

    for character in range(total_characters):

        generate_number = randint(0, 70)

        key = f'{key}{possible_characters[generate_number]}'

    print(key)

possible_characters = '''1234567890qwertyuiopasdfghjklçzxcvbnm'"!@#$%¨&*()_-+=|\,<.>:;?/]}~^`´[{'''
generate_key(24)
