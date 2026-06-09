import streamlit as st
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from interfaces.mg1_interface import mg1_interface
from interfaces.mms_interface import mms_interface
from interfaces.mmsn_interface import mmsn_interface
from interfaces.mmsk_interface import mmsk_interface
from interfaces.priority_single_interface import priority_single_server_interface
from interfaces.priority_multiple_interface import priority_multiple_servers_interface
from interfaces.priority_without_interruption_interface import priority_without_interruption_interface

st.set_page_config(
    page_title="Calculadora de Teoria de Filas",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.markdown("""
<style>
    .stApp {
        background: linear-gradient(180deg, #f8fafc 0%, #eef2ff 100%);
    }
    [data-testid="stSidebar"] {
        background: #111827;
    }
    [data-testid="stSidebar"] * {
        color: #e5e7eb;
    }
    .hero-card {
        background: #ffffff;
        border: 1px solid #e5e7eb;
        border-radius: 14px;
        padding: 1rem 1.25rem;
        box-shadow: 0 8px 18px rgba(15, 23, 42, 0.08);
        margin-bottom: 1rem;
    }
</style>
""", unsafe_allow_html=True)

st.markdown("""
<div class="hero-card">
    <h1 style="margin:0; color:#1f2937;">Calculadora de Teoria de Filas</h1>
    <p style="margin:0.35rem 0 0 0; color:#4b5563;">Interface simplificada para análise dos modelos com precisão de 8 casas decimais.</p>
</div>
""", unsafe_allow_html=True)

st.caption("Todos os campos aceitam até 8 casas decimais para maior precisão.")

model_options = [
    "Fila M/G/1",
    "Fila M/M/s",
    "Fila M/M/s/n",
    "Fila M/M/s/K",
    "Fila de Prioridade (Servidor Único)",
    "Fila de Prioridade (Múltiplos Servidores)",
    "Fila de Prioridade (Sem Interrupção)"
]

model_descriptions = {
    "Fila M/G/1": "Chegadas Poisson, distribuição geral de serviço e servidor único.",
    "Fila M/M/s": "Chegadas Poisson, serviço exponencial e múltiplos servidores.",
    "Fila M/M/s/n": "M/M/s com capacidade limitada do sistema.",
    "Fila M/M/s/K": "M/M/s com capacidade limitada e possível bloqueio.",
    "Fila de Prioridade (Servidor Único)": "Prioridades preemptivas com 1 servidor.",
    "Fila de Prioridade (Múltiplos Servidores)": "Prioridades preemptivas com múltiplos servidores.",
    "Fila de Prioridade (Sem Interrupção)": "Prioridades não-preemptivas sem interrupção."
}

st.sidebar.title("Navegação")
model_type = st.sidebar.radio("Escolha o modelo", model_options)
st.sidebar.markdown("---")
st.sidebar.markdown("### Modelo selecionado")
st.sidebar.success(model_type)
st.sidebar.caption(model_descriptions[model_type])

with st.sidebar.expander("Notação rápida", expanded=False):
    st.markdown("""
- **λ**: Taxa de chegada
- **μ**: Taxa de serviço
- **s**: Número de servidores
- **ρ**: Utilização do sistema
- **L**: Clientes médios no sistema
- **Lq**: Clientes médios na fila
- **W**: Tempo médio no sistema
- **Wq**: Tempo médio na fila
- **P₀**: Probabilidade de sistema vazio
""")

if "Prioridade" in model_type:
    with st.sidebar.expander("Tipos de prioridade", expanded=True):
        st.markdown("""
**Com interrupção (preemptivo)**
- Classe mais prioritária pode interromper atendimento
- Estabilidade típica: ρ < 1

**Sem interrupção (não-preemptivo)**
- Atendimento atual não é interrompido
- Estabilidade: ∑λᵢ < s×μ
""")

if model_type == "Fila M/G/1":
    mg1_interface()
elif model_type == "Fila M/M/s":
    mms_interface()
elif model_type == "Fila M/M/s/n":
    mmsn_interface()
elif model_type == "Fila M/M/s/K":
    mmsk_interface()
elif model_type == "Fila de Prioridade (Servidor Único)":
    priority_single_server_interface()
elif model_type == "Fila de Prioridade (Múltiplos Servidores)":
    priority_multiple_servers_interface()
elif model_type == "Fila de Prioridade (Sem Interrupção)":
    priority_without_interruption_interface()

st.markdown("---")
st.caption("Calculadora de Teoria de Filas")
