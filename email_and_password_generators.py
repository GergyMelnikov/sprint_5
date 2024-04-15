import random
import string


simbols = string.punctuation
letters = string.ascii_letters + string.digits

# password generator
def generate_password(lenght):

    password =''.join(random.choice(letters + simbols) for _ in range(lenght))
    return password


# email generator
domains_list = ['@gmail.com', '@ya.ru', '@yandexxx.ru', '@rambler.com', '@mail.ru', '@icloud.com']

def generate_email():
    
    name = ''.join(random.choice(letters) for _ in range(random.randint(6,12)))
    domain = ''.join(random.choice(domains_list))
        
    generated_email = f'{name}{domain}'
    return generated_email

print(generate_email())
print(generate_password(7))