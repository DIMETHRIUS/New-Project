
def send_email(message, recipient,*, sender = 'university.help@gmail.com' ):
    if sender == recipient:

        print('Нельзя отправить письмо самому себе!')

    elif "@" not in recipient or not (
                recipient.endswith(".com") or recipient.endswith(".ru") or recipient.endswith(".net")):

        print(f'Невозможно отправить письмо с адреса {sender} на адрес {recipient}')

    elif sender == "university.help@gmail.com":

        print(f'Письмо успешно отправлено с адреса {sender} на адрес {recipient}.')

    else:

        print(f'НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса {sender} на адрес {recipient}.')


send_email('Нельзя отправить письмо самому себе!',sender='university.help@gmail.com', recipient='university.help@gmail.com')
send_email('Невозможно отправить письмо с адреса {sender} на адрес {recipient}', recipient='urban.teacher@mail.by')
send_email('Письмо успешно отправлено с адреса {sender} на адрес {recipient}.', recipient='urban.student@mail.ru')
send_email('НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса {sender} на адрес {recipient}.', sender='an.nabogdanova@yandex.ru', recipient= 'urban.student@mail.ru')


