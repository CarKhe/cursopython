#Open/Close Principle
#abiertos para la extencion pero cerrados para la modificacion


class Notificador:
    def __init__(self,usuario,mensaje):
        self.usuario = usuario
        self.mensaje = mensaje
    
    def notificar(self):
        raise NotImplementedError
    
class NotificadorEmail(Notificador):
    def notificar(self):
        print(f"Enviando mensaje email a {self.usuario.email}")

class NotificadorSMS(Notificador):
    def notificar(self):
        print(f"Enviando mensaje SMS a {self.usuario.sms}")