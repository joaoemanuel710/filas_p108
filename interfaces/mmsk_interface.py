import streamlit as st
import pandas as pd
import plotly.express as px
from typing import Dict, Any
import sys
import os

# Add the parent directory to the path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app.service import StreamlitQueueService
from interfaces.formulas_reference import show_formulas_mmsk

def display_results(results: Dict[str, Any], title: str):
    """Display M/M/s/K queue calculation results"""
    st.subheader(f"📈 {title}")
    
    metric_translations = {
        'prob_zero_clients': 'Probabilidade Zero Clientes (P₀)',
        'avg_clients_in_queue': 'Clientes Médios na Fila (Lq)',
        'avg_wait_time_in_queue': 'Tempo Médio na Fila (Wq)',
        'avg_clients_in_system': 'Clientes Médios no Sistema (L)',
        'avg_wait_time_in_system': 'Tempo Médio no Sistema (W)',
        'avg_effective_arrival_rate': 'Taxa de Chegada Efetiva (λₑ)'
    }
    
    cols = st.columns(3)
    for i, (key, value) in enumerate(results.items()):
        with cols[i % 3]:
            formatted_key = metric_translations.get(key, key.replace('_', ' ').title())
            if isinstance(value, float):
                st.metric(formatted_key, f"{value:.8f}")
            else:
                st.metric(formatted_key, str(value))

def mmsk_interface():
    st.header("Calculadora de Fila M/M/s/K")
    st.markdown("Fila multi-servidor com capacidade limitada e perda de clientes")
    show_formulas_mmsk()

    # Service initialization
    service = StreamlitQueueService()
    
    # Input parameters
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        lmbd = st.number_input("Taxa de Chegada (λ)", min_value=0.00000001, value=3.0, step=0.00000001, format="%.8f", key="mmsk_lambda")
    with col2:
        mu = st.number_input("Taxa de Serviço (μ)", min_value=0.00000001, value=2.0, step=0.00000001, format="%.8f", key="mmsk_mu")
    with col3:
        s = st.number_input("Número de Servidores (s)", min_value=1, value=2, step=1, key="mmsk_servers")
    with col4:
        K = st.number_input("Capacidade do Sistema (K)", min_value=1, value=8, step=1, key="mmsk_capacity")
    
    # System info
    traffic_intensity = lmbd / mu
    rho = lmbd / (s * mu)
    st.info(f"Intensidade de tráfico (λ/μ): {traffic_intensity:.8f}")
    st.info(f"Utilização teórica (ρ): {rho:.8f}")
    
    if K < s:
        st.error("⚠️ A capacidade do sistema (K) deve ser maior ou igual ao número de servidores (s)!")
    
    # Additional calculations
    st.subheader("Cálculos Adicionais")
    calc_prob_n = st.checkbox("Calcular probabilidade por número de clientes", key="mmsk_calc_prob_n")

    target_n = 0
    prob_type_n = "P(n = N)"
    if calc_prob_n:
        col1, col2 = st.columns(2)
        with col1:
            target_n = st.number_input("Número alvo de clientes (N)", min_value=0, max_value=K, value=min(5, K), step=1, key="mmsk_target_n")
        with col2:
            prob_type_n = st.selectbox("Tipo de probabilidade", ["P(n = N)", "P(n ≤ N)", "P(n < N)", "P(n ≥ N)", "P(n > N)"], key="mmsk_prob_type_n")
    
    if st.button("Calcular M/M/s/K", key="mmsk_calculate"):
        try:
            if K < s:
                st.error("Não é possível calcular métricas: capacidade deve ser ≥ número de servidores.")
            else:
                results = service.calculate_mmsk(lmbd, mu, s, K)
                display_results(results, f"Resultados M/M/{s}/{K}")
                
                # Additional calculations results
                if calc_prob_n:
                    if prob_type_n == "P(n = N)":
                        result_prob = service.calculate_mmsk_prob_n(lmbd, mu, s, K, target_n)
                        label = f"P(n = {target_n})"
                    elif prob_type_n == "P(n ≤ N)":
                        result_prob = sum(service.calculate_mmsk_prob_n(lmbd, mu, s, K, i) for i in range(target_n + 1))
                        label = f"P(n ≤ {target_n})"
                    elif prob_type_n == "P(n < N)":
                        result_prob = sum(service.calculate_mmsk_prob_n(lmbd, mu, s, K, i) for i in range(target_n))
                        label = f"P(n < {target_n})"
                    elif prob_type_n == "P(n ≥ N)":
                        result_prob = 1 - sum(service.calculate_mmsk_prob_n(lmbd, mu, s, K, i) for i in range(target_n))
                        label = f"P(n ≥ {target_n})"
                    else:
                        result_prob = 1 - sum(service.calculate_mmsk_prob_n(lmbd, mu, s, K, i) for i in range(target_n + 1))
                        label = f"P(n > {target_n})"
                    st.metric(label, f"{result_prob:.8f}")
                
                # Show blocking probability
                prob_K = service.calculate_mmsk_prob_n(lmbd, mu, s, K, K)
                st.warning(f"🚫 Probabilidade de Bloqueio P({K}): {prob_K:.8f}")
                
                # Additional visualization
                st.subheader("📊 Visualização das Métricas")
                
                # Create a comparison chart
                metrics_df = pd.DataFrame({
                    'Métrica': ['Clientes na Fila (Lq)', 'Clientes no Sistema (L)', 'Tempo na Fila (Wq)', 'Tempo no Sistema (W)', 'Taxa Efetiva (λₑ)'],
                    'Valor': [
                        results['avg_clients_in_queue'],
                        results['avg_clients_in_system'],
                        results['avg_wait_time_in_queue'],
                        results['avg_wait_time_in_system'],
                        results['avg_effective_arrival_rate']
                    ],
                    'Tipo': ['Número de Clientes', 'Número de Clientes', 'Tempo', 'Tempo', 'Taxa']
                })
                
                fig = px.bar(
                    metrics_df, 
                    x='Métrica', 
                    y='Valor', 
                    color='Tipo',
                    title=f"Métricas da Fila M/M/{s}/{K}"
                )
                st.plotly_chart(fig, use_container_width=True)
                
                # System state probabilities chart
                if calc_prob_n:
                    st.subheader("📉 Distribuição de Probabilidades")
                    prob_data = []
                    for i in range(K + 1):
                        prob_i = service.calculate_mmsk_prob_n(lmbd, mu, s, K, i)
                        prob_data.append({'Número de Clientes': i, 'Probabilidade': prob_i})
                    
                    prob_df = pd.DataFrame(prob_data)
                    fig_prob = px.bar(
                        prob_df,
                        x='Número de Clientes',
                        y='Probabilidade',
                        title=f"Distribuição de Probabilidades - M/M/{s}/{K}"
                    )
                    st.plotly_chart(fig_prob, use_container_width=True)
                
                # Performance comparison chart
                st.subheader("📊 Análise de Performance")
                perf_data = pd.DataFrame({
                    'Métrica': ['Taxa de Chegada Original', 'Taxa de Chegada Efetiva', 'Taxa de Bloqueio'],
                    'Valor': [lmbd, results['avg_effective_arrival_rate'], lmbd - results['avg_effective_arrival_rate']],
                    'Percentual': [100, (results['avg_effective_arrival_rate']/lmbd)*100, (1 - results['avg_effective_arrival_rate']/lmbd)*100]
                })
                
                fig_perf = px.pie(
                    perf_data[perf_data['Métrica'] != 'Taxa de Chegada Original'],
                    values='Valor',
                    names='Métrica',
                    title="Análise de Chegadas vs Bloqueios"
                )
                st.plotly_chart(fig_perf, use_container_width=True)
                
        except Exception as e:
            st.error(f"Erro: {str(e)}")

if __name__ == "__main__":
    mmsk_interface()
