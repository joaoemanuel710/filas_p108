import streamlit as st


def show_formulas_mm1():
    with st.expander("📐 Fórmulas de Referência — M/M/1", expanded=False):
        st.markdown("**Condição de estabilidade:** ρ = λ/μ < 1")
        col1, col2 = st.columns(2)
        with col1:
            st.latex(r"\rho = \frac{\lambda}{\mu}")
            st.latex(r"P_0 = 1 - \rho")
            st.latex(r"P_n = (1-\rho)\,\rho^n")
            st.latex(r"L = \frac{\lambda}{\mu - \lambda} = \frac{\rho}{1-\rho}")
            st.latex(r"L_q = \frac{\lambda^2}{\mu(\mu-\lambda)} = \frac{\rho^2}{1-\rho}")
        with col2:
            st.latex(r"W = \frac{1}{\mu - \lambda}")
            st.latex(r"W_q = \frac{\lambda}{\mu(\mu-\lambda)}")
            st.latex(r"L = \lambda W \quad L_q = \lambda W_q")
            st.latex(r"W = W_q + \frac{1}{\mu}")
            st.latex(r"L = L_q + \rho")


def show_formulas_mms():
    with st.expander("📐 Fórmulas de Referência — M/M/s", expanded=False):
        st.markdown("**Parâmetros:** r = λ/μ &nbsp;|&nbsp; ρ = λ/(sμ) < 1")
        col1, col2 = st.columns(2)
        with col1:
            st.latex(r"P_0 = \left[\sum_{n=0}^{s-1}\frac{r^n}{n!} + \frac{r^s}{s!}\cdot\frac{1}{1-\rho}\right]^{-1}")
            st.latex(r"P_n = P_0\,\frac{r^n}{n!} \quad (0 \le n \le s)")
            st.latex(r"P_n = P_0\,\frac{r^n}{s!\,s^{n-s}} \quad (n > s)")
            st.latex(r"P_{esperar} = P_0\,\frac{r^s}{s!(1-\rho)}")
        with col2:
            st.latex(r"L_q = P_0\,\frac{r^s\,\rho}{s!(1-\rho)^2}")
            st.latex(r"W_q = \frac{L_q}{\lambda}")
            st.latex(r"L = L_q + r")
            st.latex(r"W = W_q + \frac{1}{\mu}")


def show_formulas_mmsk():
    with st.expander("📐 Fórmulas de Referência — M/M/s/K", expanded=False):
        st.markdown("**Parâmetros:** r = λ/μ &nbsp;|&nbsp; ρ = r/s &nbsp;|&nbsp; K = capacidade total &nbsp;|&nbsp; ρ pode ser ≥ 1")
        col1, col2 = st.columns(2)
        with col1:
            st.latex(r"P_0 = \left[\sum_{n=0}^{s}\frac{r^n}{n!} + \frac{r^s}{s!}\sum_{n=s+1}^{K}\rho^{n-s}\right]^{-1}")
            st.latex(r"P_n = P_0\,\frac{r^n}{n!} \quad (n \le s)")
            st.latex(r"P_n = P_0\,\frac{r^s\,\rho^{n-s}}{s!} \quad (s < n \le K)")
            st.latex(r"\bar{\lambda} = \lambda(1 - P_K)")
        with col2:
            st.latex(r"L_q = \frac{P_0\,r^s\,\rho}{s!(1-\rho)^2}\left[1-\rho^{K-s}-(K-s)\rho^{K-s}(1-\rho)\right]")
            st.latex(r"L = L_q + \frac{\bar{\lambda}}{\mu}")
            st.latex(r"W = \frac{L}{\bar{\lambda}} \quad W_q = \frac{L_q}{\bar{\lambda}}")


def show_formulas_mmsn():
    with st.expander("📐 Fórmulas de Referência — M/M/s/N (população finita)", expanded=False):
        st.markdown("**Parâmetros:** s servidores &nbsp;|&nbsp; N = população total &nbsp;|&nbsp; r = λ/μ")
        st.markdown("Com n clientes no sistema → (N−n) geram chamadas")
        col1, col2 = st.columns(2)
        with col1:
            st.latex(r"P_0 = \left[\sum_{n=0}^{s}\frac{N!}{(N-n)!}\frac{r^n}{n!} + \sum_{n=s+1}^{N}\frac{N!}{(N-n)!}\frac{r^n}{s!}\right]^{-1}")
            st.latex(r"P_n = P_0\,\frac{N!}{(N-n)!}\frac{r^n}{n!} \quad (n \le s)")
            st.latex(r"P_n = P_0\,\frac{N!}{(N-n)!}\frac{r^n}{s!} \quad (s < n \le N)")
        with col2:
            st.latex(r"L = \sum_{n=0}^{N} n\,P_n")
            st.latex(r"\bar{\lambda} = \lambda(N - L)")
            st.latex(r"L_q = L - \frac{\bar{\lambda}}{\mu}")
            st.latex(r"W = \frac{L}{\bar{\lambda}} \quad W_q = \frac{L_q}{\bar{\lambda}}")


def show_formulas_mg1():
    with st.expander("📐 Fórmulas de Referência — M/G/1", expanded=False):
        st.markdown("**Parâmetros:** ρ = λ/μ < 1 &nbsp;|&nbsp; E(S) = 1/μ &nbsp;|&nbsp; σ² = Var(S) &nbsp;|&nbsp; E(S²) = σ² + 1/μ²")
        col1, col2 = st.columns(2)
        with col1:
            st.latex(r"P_0 = 1 - \rho")
            st.latex(r"L_q = \frac{\lambda^2\sigma^2 + \rho^2}{2(1-\rho)} = \frac{\lambda^2 E(S^2)}{2(1-\rho)}")
            st.latex(r"L = \rho + L_q")
        with col2:
            st.latex(r"W_q = \frac{L_q}{\lambda}")
            st.latex(r"W = W_q + \frac{1}{\mu}")
        st.markdown("**Casos especiais:**")
        col1, col2 = st.columns(2)
        with col1:
            st.markdown("M/M/1 (σ² = 1/μ²):")
            st.latex(r"L_q = \frac{\rho^2}{1-\rho}")
        with col2:
            st.markdown("M/D/1 (σ² = 0):")
            st.latex(r"L_q = \frac{\rho^2}{2(1-\rho)}")


def show_formulas_priority_single():
    with st.expander("📐 Fórmulas de Referência — Prioridade com Interrupção (1 servidor)", expanded=False):
        st.markdown("**Parâmetros:** k classes &nbsp;|&nbsp; ρᵢ = λᵢ/μ &nbsp;|&nbsp; σₖ = Σᵢ₌₁ᵏ ρᵢ &nbsp;|&nbsp; σ₀ = 0 &nbsp;|&nbsp; classe 1 = maior prioridade")
        col1, col2 = st.columns(2)
        with col1:
            st.latex(r"W_k = \frac{1/\mu}{(1 - \sigma_{k-1})(1 - \sigma_k)}")
            st.latex(r"W_{qk} = W_k - \frac{1}{\mu}")
        with col2:
            st.latex(r"L_k = \lambda_k W_k")
            st.latex(r"L_{qk} = \lambda_k W_{qk}")
        st.latex(r"\sigma_k = \sum_{i=1}^{k} \rho_i = \sum_{i=1}^{k}\frac{\lambda_i}{\mu}")


def show_formulas_priority_multiple():
    with st.expander("📐 Fórmulas de Referência — Prioridade com Interrupção (s servidores)", expanded=False):
        st.markdown("**Parâmetros:** s servidores &nbsp;|&nbsp; σₖ = Σᵢ₌₁ᵏ λᵢ/(sμ) &nbsp;|&nbsp; σ₀ = 0")
        col1, col2 = st.columns(2)
        with col1:
            st.latex(r"W_k = \frac{1/\mu}{(1 - \sigma_{k-1})(1 - \sigma_k)}")
            st.latex(r"W_{qk} = W_k - \frac{1}{\mu}")
        with col2:
            st.latex(r"L_k = \lambda_k W_k \quad L_{qk} = \lambda_k W_{qk}")
            st.latex(r"\sigma_k = \sum_{i=1}^{k}\frac{\lambda_i}{s\mu}")


def show_formulas_priority_without_interruption():
    with st.expander("📐 Fórmulas de Referência — Prioridade Sem Interrupção", expanded=False):
        st.markdown("**Parâmetros:** s servidores &nbsp;|&nbsp; r = λ_total/μ &nbsp;|&nbsp; σₖ = Σᵢ₌₁ᵏ λᵢ/(sμ)")
        col1, col2 = st.columns(2)
        with col1:
            st.latex(r"W_k = \frac{1}{\mu} + \frac{W_{q,M/M/s}}{(1-\sigma_{k-1})(1-\sigma_k)}")
            st.markdown("onde W_q,M/M/s é o tempo na fila do sistema M/M/s equivalente (com λ total):")
            st.latex(r"W_{q,MMs} = \frac{P_0\,r^s}{s!\,s\mu(1-\rho)^2\,\lambda}")
        with col2:
            st.latex(r"W_{qk} = W_k - \frac{1}{\mu}")
            st.latex(r"L_k = \lambda_k W_k \quad L_{qk} = \lambda_k W_{qk}")
        st.markdown("**M/G/1 com prioridades (SPT):**")
        st.latex(r"E(W_{qk}) = \frac{\sum_i \lambda_i\left[V(S_i)+E(S_i)^2\right]}{2(1-\sigma_{k-1})(1-\sigma_k)}")
