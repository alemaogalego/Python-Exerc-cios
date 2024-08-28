class Veiculo:
    def __init__(self, marca, modelo, estado = False) -> None:
        self._marca = marca
        self._modelo = modelo
        self._estado = estado
    
    def __str__(self):
        status = "ligado" if self._estado else "desligado"
        return f"{self._marca} {self._modelo} - Status: {status}"