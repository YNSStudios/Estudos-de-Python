import base64
import io
import math
import matplotlib.pyplot as plt


def calcular_vertices(base, lado_esq, lado_dir):
    """Calcula as coordenadas (x, y) dos vértices de um triângulo dada as 3 medidas."""
    # Vértice A (origem)
    x0, y0 = 0.0, 0.0
    # Vértice B (fim da base)
    x1, y1 = base, 0.0

    # Vértice C (topo) usando lei dos cossenos
    cos_a = (base**2 + lado_esq**2 - lado_dir**2) / (2 * base * lado_esq)

    # CORREÇÃO 1: Trata pequenos arredondamentos numéricos para evitar erro na raiz
    cos_a = max(-1.0, min(1.0, cos_a))

    x2 = lado_esq * cos_a

    # CORREÇÃO 2: Usa math.sqrt e abs() para garantir valor positivo na raiz
    y2 = math.sqrt(abs(lado_esq**2 - x2**2))

    return [x0, x1, x2, x0], [y0, y1, y2, y0]


def desenhar_triangulo(ax, base, lado_esq, lado_dir, titulo):
    """Desenha um triângulo específico no eixo do gráfico."""
    x, y = calcular_vertices(base, lado_esq, lado_dir)
    ax.plot(x, y, "b-", linewidth=2)
    ax.fill(x, y, "skyblue", alpha=0.4)

    # Pega a altura máxima com segurança
    altura_max = max(y) if max(y) > 0 else 0.1

    # Anotações das medidas nos lados correspondentes
    ax.text(base / 2, -0.15 * altura_max, f"{base:.1f}", ha="center", va="top")
    ax.text(
        x[2] / 2 - 0.05 * base,
        y[2] / 2,
        f"{lado_esq:.1f}",
        ha="right",
        va="center",
    )
    ax.text(
        (x[1] + x[2]) / 2 + 0.05 * base,
        y[2] / 2,
        f"{lado_dir:.1f}",
        ha="left",
        va="center",
    )

    ax.set_title(titulo, fontsize=10, pad=10)
    ax.set_aspect("equal")
    ax.axis("off")


# Entrada de dados
print("-=" * 20)
print("Analisador Dinâmico de Triângulos")
print("-=" * 20)

try:
    r1 = float(input("Digite a primeira medida: "))
    r2 = float(input("Digite a segunda medida: "))
    r3 = float(input("Digite a terceira medida: "))
except ValueError:
    print("\n[ERRO] Digite apenas números válidos!")
    exit()

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print("\nOs segmentos PODEM FORMAR um triângulo!")
    print("Gerando as 3 visualizações baseadas nas posições prováveis...")

    # Cria uma figura com 3 subgráficos lado a lado
    fig, axs = plt.subplots(1, 3, figsize=(12, 4))

    # Cenário 1: r1 na base
    desenhar_triangulo(axs[0], r1, r2, r3, f"Cenário 1\nBase: {r1:.1f}")

    # Cenário 2: r2 na base
    desenhar_triangulo(axs[1], r2, r3, r1, f"Cenário 2\nBase: {r2:.1f}")

    # Cenário 3: r3 na base
    desenhar_triangulo(axs[2], r3, r1, r2, f"Cenário 3\nBase: {r3:.1f}")

    plt.tight_layout()
    plt.show()  # Abre a janela com os 3 triângulos desenhados perfeitamente
else:
    print("\nOs segmentos NÃO PODEM FORMAR um triângulo.")