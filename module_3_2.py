
def send_email(message,*, recipient ='urban.teacher@mail.com', sender = 'university.help@gmail.com' ):

    if('@','.com' not in recipient or '@', '.com' not in sender):
        print(f'Невозможно отправить письмо с адреса {sender} на адрес {recipient}')

        return False

send_email('Невозможно отправить письмо с адреса {sender} на адрес {recipient}')


def send_email(message,*, recipient ='university.help@gmail.com', sender = 'university.help@gmail.com' ):
     if(sender==recipient):
         print('Нельзя отправить письмо самому себе!')

send_email('Нельзя отправить письмо самому себе!')



def send_email(message,*, recipient ='urban.teacher@mail.com', sender = 'university.help@gmail.com' ):
    if(sender=='university.help@gmail.com'):
        print(f'Письмо успешно отправлено с адреса {sender} на адрес {recipient}')

        return False
send_email('Письмо успешно отправлено с адреса {sender>} на адрес {recipient}.')



def send_email(message,*, recipient ='urban.teacher@mail.com', sender = 'an.nabogdanova@yandex.ru' ):
    if(sender=='an.nabogdanova@yandex.ru'):
        print('НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса {sender} на адрес {recipient}.')

send_email('НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса {sender} на адрес {recipient}.')