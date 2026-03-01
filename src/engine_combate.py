import random

def resolver_combate(atacante, defensor):
    print(f"\n--- Início do Conflito: {atacante.nome} vs {defensor.nome} ---")
    
    # Adicionamos um fator de "sorte" ou "tática" de 1 a 20
    bonus_atacante = random.randint(1, 20)
    bonus_defensor = random.randint(1, 20)
    
    # Cálculo de força total
    forca_ataque = atacante.poder_militar + bonus_atacante
    forca_defesa = defensor.poder_militar + bonus_defensor
    
    print(f"Ataque: {forca_ataque} (Base: {atacante.poder_militar} + Sorte: {bonus_atacante})")
    print(f"Defesa: {forca_defesa} (Base: {defensor.poder_militar} + Sorte: {bonus_defensor})")
    
    if forca_ataque > forca_defesa:
        print(f"Resultado: Vitória de {atacante.nome}!")
        defensor.estabilidade -= 10  # Dano à estabilidade do perdedor
        return True
    else:
        print(f"Resultado: {defensor.nome} conseguiu repelir o ataque!")
        atacante.estabilidade -= 5   # Custo para quem tentou atacar e falhou
        return False