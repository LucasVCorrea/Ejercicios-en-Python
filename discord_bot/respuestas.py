import random
import discord

def get_response(message: str) -> str:
    p_message = message.lower()

    if p_message == 'hola bot':
        numero = random.randint(1, 6)
        if 1 <= numero <= 3:
            return 'Che, de onda ¿No tenes a otra persona para hablarle?'

        if 4 < numero < 6:
            return 'Que ganas de romper la japi la concha de tu madre'

        if numero == 6:
            return 'Hola! aca estoy para lo que necesites!'

    if message == '!chiste':
        return 'aca el unico chiste sos vos.'

    if message == '!dato':
        return '¿Lo sabias? El segundo animal mamífero que más veces tiene intencion de reproducirse con más de una pareja es el conejo!\nEl primero es tu vieja'

    if p_message == '!help':
        return '`This is a help message that you can modify.`'

    return 'I didn\'t understand what you wrote. Try typing "!help".'
