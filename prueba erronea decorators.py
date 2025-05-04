def log_transaction(func):
    
    print('1 Log de la transacción...')
    func()
    print('3 Log terminado...')

    

@log_transaction
def process_payment():
    print('2 Procesando pago...')

process_payment()