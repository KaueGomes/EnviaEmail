def send_email(Usuario,Senha,Destinatario,Assunto,Corpo):
    # A smtplib so funciona quando a funcao de aplicativos menos seguros
    # esta ativa na conta do google em que o acesso sera feito
    # Configuracao da conta > Seguranca > Aplicativos menos seguros
    import smtplib

    De = Usuario
    Para = Destinatario
    Assunto = Assunto
    Texto = Corpo

    #Preparando a mensagem atual
    Mensagem = """From: %s\nTo: %s\nSubject: %s\n\n%s"""%(De,Para,Assunto,Texto)
    try:
        server = smtplib.SMTP_SSL("smtp.gmail.com",465)
        server.ehlo()
        server.login(Usuario,Senha)
        server.sendmail(De,Para,Mensagem)
        server.close()
        print(f'Email enviado para {Para}')
    except:
        print('O envio falhou')