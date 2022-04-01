"""
Recebe uma distância e a velocidade de movimentação, e retorna as horas que seriam gastas para percorrer em linha reta.
"""
print("Horas para percorrer distância:")

distancia = float(input("Distância (km): "))
velocidade = float(input("Velocidade (km/h): "))

horas = distancia / velocidade
minutos = horas * 60
h, m = divmod(minutos, 60)

# Direto
print(f"Tempo de viagem: {round(horas,2)} horas.")
# Convertido
print(f"Tempo de viagem: {int(h)}h{int(m)}m.")
