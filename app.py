import streamlit as st

# Configuração da página (muda o título na aba do navegador)
st.set_page_config(page_title="Calculadora de Tinta", page_icon="🎨")

# Título principal da aplicação
st.title("Calculadora de Tinta Comercial 🎨")
st.write("Descubra a quantidade exata de tinta necessária para o seu projeto.")

# Criando duas colunas lado a lado para o visual ficar mais bonito
col1, col2 = st.columns(2)

with col1:
    # Substitui o primeiro input()
    n1 = st.number_input('Qual a altura da parede (m)?', min_value=0.0, value=0.0, step=0.1)

with col2:
    # Substitui o segundo input()
    n2 = st.number_input('Qual a largura da parede (m)?', min_value=0.0, value=0.0, step=0.1)

# Botão para processar o cálculo
if st.button("Calcular Tinta Necessária", type="primary"):

    # Validação simples para não calcular com valores zerados
    if n1 > 0 and n2 > 0:
        area = n1 * n2
        tinta = area / 2  # Mantendo a sua lógica de 2m² por litro

        # Linha de separação visuals
        st.divider()

        # Substitui os seus 'prints' por caixas de mensagens organizadas
        st.success(f"📐 **Dimensões:** Sua parede tem a dimensão de {n1}m x {n2}m.")
        st.info(f"🧱 **Área Total:** {area:.2f} metros quadrados.")

        # Destacando o resultado final
        st.metric(label="Quantidade de tinta necessária", value=f"{tinta:.2f} Litros")

    else:
        st.warning("Por favor, insira valores maiores que zero para a altura e a largura.")
