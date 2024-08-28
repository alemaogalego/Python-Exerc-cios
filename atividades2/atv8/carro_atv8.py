from veiculo_atv8 import Veiculo

class Carro(Veiculo):
    def __init__(self, marca, modelo, portas) -> None:
        super().__init__(marca, modelo)
        self._portas = portas
    
    def __str__(self):
        return f'{super().__str__()} | Portas: {self._portas}'

    # def __str__(self):
    #     status = "ligado" if self._estado else "desligado"
    #     return f"{self._marca} {self._modelo} - Portas: {self._portas} - Status: {status}"
