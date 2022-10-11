import os
import smtplib
from email.message import EmailMessage

def mensagem(preco):
    # configurar email. senha
    EMAIL_ADDRES = 'enviadoremailautomatico@gmail.com'
    EMAIL_PASSWORD = 'grwkypicndfeqxcu'

    # Criar um e-mail
    msg = EmailMessage()
    msg['Subject'] = 'Carga #35 chegou ao porto'
    msg['From'] = 'enviadoremailautomatico@gmail.com'
    msg['To'] = 'db.fan.db@gmail.com'
    msg.set_content(f'está pronto para compra o valor é: {preco} ')

    # Enviar um E-mail
    with smtplib.SMTP_SSL('smtp.gmail.com',465) as smtp:
        smtp.login(EMAIL_ADDRES,EMAIL_PASSWORD)
        smtp.send_message(msg)


