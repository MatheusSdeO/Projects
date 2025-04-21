import time

print("🚀 Aplicação Python rodando dentro do container Docker!")

# Mantém o container ativo por 30 segundos
for _ in range(6):  # 6 iterações de 5 segundos
    print("⏳ Container ainda está rodando...")
    time.sleep(5)

print("⏳ O container terminou de rodar.")
