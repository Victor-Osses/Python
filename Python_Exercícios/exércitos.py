from random import randint

qtdMsgRed = 5
qtdMsgBlue = 10
signalRed = newDate = 0
startTime = totalTime = randint(0, 86400) # Você pode definir um valor de tempo inicial fixo aqui
date_in_text = ""


def setTimeStamp(time=0):
    global totalTime, date_in_text

    totalTime += time

    minute, second = divmod(totalTime, 60)
    hour, minute = divmod(minute, 60)

    if totalTime > 86400:
        hour = hour - 24 #Se a hora passar de 24 eu decremento 24 para a representação do horário ficar correta

    date_in_text = f'{hour:02d}:{minute:02d}:{second:02d}'


def randomChance(start, end, percentage):
    if randint(start, end) >= percentage:
        return True
    else:
        return False


def sendMsgRed():
    global qtdMsgRed, totalTime, date_in_text, newDate

    if not msgAlive():
         resultWar()

    qtdMsgRed -= 1

    if newDate:
        newDate = 0
        print(f'\033[31mO exército vermelho dispara um sinalizador indicando que uma nova data foi estabelecida!!!\033[m \033[0;33;40m[{date_in_text}]\033[m')

    print(f'\033[31mO mensageiro {5 - qtdMsgRed} do exército vermelho saiu para informar a data!!!\033[m \033[0;33;40m[{date_in_text}]\033[m')

    time = randint(3600, 4200)
    setTimeStamp(time)

    if randomChance(1, 100, 45):
        print(f'\033[31mO mensageiro {5 - qtdMsgRed} do exército vermelho chegou até o exército azul!!!\033[m \033[0;33;40m[{date_in_text}]\033[m\n')
        receiveMsgRed()
    else:
        print(f'\033[31mO mensageiro {5 - qtdMsgRed} do exército vermelho foi morto antes de chegar ao destino!!!\033[m \033[0;33;40m[{date_in_text}]\033[m\n')

        if not msgAlive():
            resultWar()

        setTimeStamp(12601 - time) #3h30min subtraída do tempo de travessia do mensageiro
        sendMsgRed()


def receiveMsgRed():
    global newDate, totalTime, date_in_text

    if randomChance(1, 100, 1):
        print(f'\033[34mO exército azul concorda com a data e envia o mensageiro azul {10 - qtdMsgBlue + 1}!!!\033[m \033[0;33;40m[{date_in_text}]\033[m')
    else:
        print(f'\033[34mO exército azul exige outra data para o ataque e envia o mensageiro azul {10 - qtdMsgBlue + 1}!!!\033[m \033[0;33;40m[{date_in_text}]\033[m')
        newDate = 1

    sendMsgBlue()


def sendMsgBlue():
    global totalTime, newDate, qtdMsgBlue, date_in_text

    time = randint(3600, 4200)
    setTimeStamp(time)
    qtdMsgBlue -= 1

    if randomChance(1, 100, 45):
        receiveMsgBlue()
    else:
        if newDate == 1:
            print(f'\033[34mO mensageiro azul {10 - qtdMsgBlue} que foi enviado para definir a nova data foi morto!!!\033[m \033[0;33;40m[{date_in_text}]\033[m\n')
        else:
            print(f'\033[34mO mensageiro azul {10 - qtdMsgBlue} que foi enviado para confirmar a data foi morto!!!\033[m \033[0;33;40m[{date_in_text}]\033[m\n')

        if not msgAlive():
            resultWar()

        setTimeStamp(4201 - time) #O horário de travessia do próximo mensageiro é TempoTotal + 4201 - tempo de travessia do mensageiro morto
        print(f'\033[34mO exército azul envia o mensageiro azul {10 - qtdMsgBlue + 1}!!!\033[m \033[0;33;40m[{date_in_text}]\033[m')

        sendMsgBlue()


def receiveMsgBlue():
    global signalRed, newDate, totalTime, date_in_text
    setTimeStamp()

    if newDate == 1:
        print(f'\033[34mO mensageiro azul {10 - qtdMsgBlue} chega ao exército vermelho e informa a nova data!!!\033[m \033[0;33;40m[{date_in_text}]\033[m\n')
        sendMsgRed()
    else:
        print(f'\033[34mO mensageiro azul {10 - qtdMsgBlue} chegou até o exército vermelho e confirmou a data do ataque!!!\033[m \033[0;33;40m[{date_in_text}]\033[m\n')
        print(f'\033[31mO exército vermelho dispara seu sinalizador!!!\033[m \033[0;33;40m[{date_in_text}]\033[m\n')
        signalRed = 1
        resultWar()


def msgAlive():
    global qtdMsgRed, qtdMsgBlue

    if qtdMsgBlue == 0 or qtdMsgRed == 0:
        return False
    else:
        return True


def resultWar():
    global qtdMsgRed, qtdMsgBlue, totalTime, startTime, signalRed, data

    if (qtdMsgBlue == 0 or qtdMsgRed == 0) and signalRed == 0:
        print('\nOs exércitos perderam')
    else:
        print('Os exércitos ganharam!!!')

    setTimeStamp(-1 * startTime) #Tempo total - tempo inicial = duração
    print(f'A troca de mensagens durou exatamente {date_in_text}')
    print(f'Foram utilizados {5 - qtdMsgRed} mensageiros do exército vermelho')
    print(f'Foram utilizados {10 - qtdMsgBlue} mensageiros do exército azul')
    exit(0)


setTimeStamp()
print(f'\n\033[36mHora Inicial: {date_in_text}\033[m\n')
sendMsgRed()
