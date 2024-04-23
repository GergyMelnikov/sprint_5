import random
import string


simbols = string.punctuation
letters = string.ascii_letters
numbers = string.digits

# password generator
def generate_password(lenght):

    password =''.join(random.choice(letters + simbols + numbers) for _ in range(lenght))
    return password


# email generator
domains_list = ['@gmail.com', '@ya.ru', '@yandexxx.ru', '@rambler.com', '@mail.ru', '@icloud.com']

def generate_email():
    
    name = ''.join(random.choice(letters) for _ in range(random.randint(4,8)))
    second_name = ''.join(random.choice(letters) for _ in range(random.randint(3,8)))
    three_numbers = str(random.randint(0,999))
    domain = ''.join(random.choice(domains_list))
        
    generated_email = f'{name}_{second_name}_{three_numbers}{domain}'
    return generated_email

