T = 12

mes = {1: "Janeiro", 2:"Fevereiro", 3: "Março", 4: "Abril", 
       5: "Maio", 6: "Junho", 7: "Julho", 8: "Agosto", 9: "Setembro",
       10: "Outubro", 11:"Novembro", 12: "Dezembro"}

temperaturas = []

for i in range(1, T + 1):
    
    temperatura = float(input(f"Insira a temperatura do mês {mes[i]}: "))
    temperaturas.append(temperatura)

media_anual = sum(temperaturas) / len(temperaturas)

print("Média Anual:", media_anual)


# Encontrar meses com temperaturas acima da média anual
meses_acima_da_media = [mes[i] for i in range(1, T + 1) if temperaturas[i - 1] > media_anual]

if meses_acima_da_media:
    print("Meses com temperaturas acima da média:", meses_acima_da_media)
else:
    print("Nenhum mês teve temperatura acima da média.")
