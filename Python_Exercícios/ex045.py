from time import sleep

for count in range(10, -1, -1):
    print('{}...' .format(count))
    sleep(1)
print('\033[31mFELIZ ANO NOVO!!!\033[m')