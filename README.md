# Filtros para Redução de Ruído em Imagens

Este projeto contém uma implementação de filtros para remover dois tipos de ruído — **Ruído Gaussiano** e **Ruído Sal e Pimenta** — em imagens. A análise usa os seguintes filtros de suavização: **Filtro Gaussiano (média)**, **Filtro da Mediana**, e **Filtro Bilateral**.

## Tipos de Ruído

1. **Ruído Gaussiano**: Comum em imagens devido a sensores eletrônicos ou condições de iluminação. Esse ruído é distribuído de forma gaussiana ao longo da imagem, com uma média e desvio padrão definidos.
2. **Ruído Sal e Pimenta**: Surge como pontos brancos e pretos aleatórios na imagem, comumente causado por falhas de transmissão. Ele gera uma dispersão de pixels com valores extremos (0 ou 255).

## Filtros Utilizados

1. **Filtro Gaussiano (média)**: Usa um núcleo de convolução gaussiana para suavizar a imagem. É eficaz na redução de ruído uniforme, desfocando gradualmente a imagem.
2. **Filtro da Mediana**: Substitui o valor de cada pixel pela mediana dos valores de pixels vizinhos, preservando bem as bordas. É altamente eficaz contra o ruído sal e pimenta, pois ignora valores extremos.
3. **Filtro Bilateral**: Preserva as bordas enquanto reduz o ruído ao usar uma combinação de espaço e cor para suavizar a imagem. Ideal para manter os detalhes enquanto suaviza áreas ruidosas.

![image](https://github.com/user-attachments/assets/64b7ca76-e971-4f80-bdd0-3c69a53ae791)

## Comparação de Filtros e Resultados

### 1. Ruído Gaussiano

- **Filtro Gaussiano**: Mostrou-se eficaz na redução do ruído gaussiano, suavizando uniformemente a imagem. No entanto, isso ocorre ao custo de um leve desfoque nos detalhes.
- **Filtro da Mediana**: Embora tenha suavizado o ruído, o filtro da mediana não foi tão eficaz quanto o filtro gaussiano, uma vez que não foi projetado para tratar especificamente esse tipo de ruído distribuído.
- **Filtro Bilateral**: Excelente para o ruído gaussiano, pois suaviza áreas ruidosas enquanto mantém as bordas definidas, preservando mais detalhes da imagem.

**Resultado**: Para o **ruído gaussiano**, o **Filtro Bilateral** foi o mais eficaz, seguido de perto pelo **Filtro Gaussiano**.

### 2. Ruído Sal e Pimenta

- **Filtro Gaussiano**: Não foi muito eficaz para ruído sal e pimenta, pois este filtro tende a borrá-lo ao invés de removê-lo completamente, devido aos valores extremos do ruído sal e pimenta.
- **Filtro da Mediana**: Mostrou-se altamente eficaz para ruído sal e pimenta. Ele substitui os pixels ruidosos (extremos) pela mediana de seus vizinhos, o que remove eficazmente o ruído e preserva as bordas.
- **Filtro Bilateral**: Embora tenha reduzido parte do ruído, o filtro bilateral não foi tão eficiente quanto o filtro da mediana para esse tipo específico de ruído, pois não foi projetado para remover valores extremos de forma eficaz.

**Resultado**: Para o **ruído sal e pimenta**, o **Filtro da Mediana** foi o mais eficaz.

## Conclusão

Cada filtro possui características que o tornam mais adequado para um tipo específico de ruído:
- **Ruído Gaussiano**: O **Filtro Bilateral** é mais eficaz, pois suaviza o ruído preservando bordas e detalhes.
- **Ruído Sal e Pimenta**: O **Filtro da Mediana** é o mais eficaz, pois lida melhor com valores extremos sem borrar a imagem.

## Como Usar

1. Clone o repositório e instale as dependências:
   ```bash
   git clone https://github.com/seu-usuario/seu-repositorio.git
   cd seu-repositorio
   pip install -r requirements.txt
