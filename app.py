def realizar_pesquisa():
    print("=== PESQUISA DE OPINIÃO - TUDOWEB ===")
    
    # Definindo a quantidade de entrevistados conforme a atividade (ajustável para 10 nos testes)
    total_entrevistados = 50
    
    contador_excelente = 0
    contador_ruim = 0
    
    for i in range(1, total_entrevistados + 1):
        print(f"\n--- Entrevistado {i} de {total_entrevistados} ---")
        
        # Coleta de dados básicos
        nome = input("Digite o nome do entrevistado: ")
        
        try:
            idade = int(input("Digite a idade do entrevistado: "))
        except ValueError:
            idade = 0 # Valor padrão caso digitem errado
            
        # Coleta e validação da opinião
        print("Opiniões disponíveis:")
        print("1 - EXCELENTE")
        print("2 - BOM")
        print("3 - RUIM")
        
        try:
            opiniao = int(input("Digite o código da sua opinião (1, 2 ou 3): "))
        except ValueError:
            opiniao = 0
            
        while opiniao not in [1, 2, 3]:
            print("Opção inválida! Por favor, digite 1, 2 ou 3.")
            try:
                opiniao = int(input("Digite o código da sua opinião (1, 2 ou 3): "))
            except ValueError:
                opiniao = 0
                
        # Contagem baseada na estrutura de decisão
        if opiniao == 1:
            contador_excelente += 1
        elif opiniao == 3:
            contador_ruim += 1
        # Nota: A opção 2 (BOM) é computada na pesquisa, mas não exige contador específico na saída.

    # Exibição dos resultados finais exigidos
    print("\n========================================")
    print("         RESULTADO DA PESQUISA          ")
    print("========================================")
    print(f"a) Quantidade de respostas 'EXCELENTE': {contador_excelente}")
    print(f"b) Quantidade de respostas 'RUIM': {contador_ruim}")
    print("========================================")

if __name__ == "__main__":
    realizar_pesquisa()