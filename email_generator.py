import random
import string

letters = string.ascii_lowercase
domains_list = ['@gmail.com', '@ya.ru', '@yandexxx.ru', '@rambler.com', '@mail.ru', '@icloud.com']
def generate_email():
    
    name = ''.join(random.choice(letters) for _ in range(11))
    domain = ''.join(random.choice(domains_list))
        
    generated_email = f'{name}{domain}'
    return generated_email

