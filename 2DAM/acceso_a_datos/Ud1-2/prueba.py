class listaVaciaExcepcion(Exception):
    def _init_(self,mensaje="la lista está vacia"):
        self.mensaje = mensaje
        super()._init_(self.mensaje)

def procesarLista(lista):
    if not lista:
        raise listaVaciaExcepcion("OJO QUE ESTÄ VACIA")

