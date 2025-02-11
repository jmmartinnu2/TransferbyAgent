import streamlit as st

# Configuración de la página
st.set_page_config(page_title="Futransfer Pitch Deck", page_icon="⚽", layout="wide")

# Estilos CSS personalizados
st.markdown("""
    <style>
        .main { background-color: #F8F9FA; }
        h1, h2, h3 { color: #003366; }
        .stButton>button { background-color: #003366; color: white; border-radius: 8px; }
    </style>
""", unsafe_allow_html=True)

# Sidebar - Menú de navegación
st.sidebar.title("📊 Menú del Pitch Deck")
menu = st.sidebar.radio(
    "Selecciona una sección:",
    ["🏆 Portada", "📌 Problema", "🚀 Solución", "📈 Mercado", "💰 Modelo de Negocio",
     "📲 Producto", "🔥 Diferenciación", "🚀 Roadmap", "💵 Inversión", "🌍 Equipo", "🎯 Llamado a la Acción"]
)

# Sección: PORTADA
if menu == "🏆 Portada":
    st.image("futransfer.svg", use_column_width=True)
    st.write("👔 **Fundador:** [Tu Nombre] | 📧 **Contacto:** [Tu Email]")

# Sección: PROBLEMA
elif menu == "📌 Problema":
    st.title("📌 Problema – ¿Qué Fallos Tiene el Mercado de Fichajes?")
    st.markdown("""
    🔴 **Falta de acceso de agentes y clubes no élite** → El 92.3% de los agentes afirma que solo las agencias top acceden a clubes grandes.  
    🔴 **Intermediarios falsos y estafas** → 57.7% de los agentes reciben ofertas falsas constantemente.  
    🔴 **Dificultad de contacto con clubes** → 46.2% menciona que los clubes no responden a mensajes.  
    🔴 **Contratos ambiguos e incumplidos** → 30.8% han enfrentado problemas legales por falta de claridad.  
    """)

# Sección: SOLUCIÓN
elif menu == "🚀 Solución":
    st.title("🚀 Solución – Futransfer: Un Mercado Justo y Transparente")
    st.markdown("""
    ✅ **Verificación de agentes y clubes** → Un ecosistema seguro con miembros acreditados por FIFA.  
    ✅ **Filtros inteligentes para fichajes** → Encuentra jugadores con información contractual en tiempo real.  
    ✅ **Marketplace seguro** → Cierra fichajes sin intermediarios falsos.  
    ✅ **Nuevas estrategias financieras** → Opciones de compra y recompra, pagos en fases, blockchain.  
    ✅ **IA predictiva** → Simulación de valor de mercado futuro de jugadores.  
    """)

# Sección: MERCADO
elif menu == "📈 Mercado":
    st.title("📈 Mercado – La Oportunidad Global")
    st.markdown("""
    💰 **Valor del mercado de transferencias:** $9.6B USD anuales.  
    ⚽ **+211 países FIFA con clubes de todas las divisiones.**  
    🏆 **Más de 130,000 jugadores activos en busca de oportunidades.**  
    👔 **10,000+ agentes FIFA con dificultades para conectar con clubes.**  
    """)

# Sección: MODELO DE NEGOCIO
elif menu == "💰 Modelo de Negocio":
    st.title("💰 Modelo de Negocio – ¿Cómo Ganamos Dinero?")
    st.markdown("""
    💲 **SaaS (Software as a Service)** → Suscripción mensual para agentes y clubes.  
    💲 **Comisiones por fichajes exitosos** → 2% por transacción cerrada en la plataforma.  
    💲 **Publicidad y patrocinios** → Ingresos por sponsors del mundo del fútbol.  
    💲 **Monetización de análisis de datos** → Servicios premium para scouting y finanzas.  
    """)

# Sección: PRODUCTO
elif menu == "📲 Producto":
    st.title("📲 Producto – ¿Cómo Funciona?")
    st.image("https://source.unsplash.com/800x400/?technology,app", use_column_width=True)
    st.markdown("""
    🎯 **Módulos Clave**  
    🔹 **Búsqueda Avanzada** → Encuentra jugadores con filtros deportivos y contractuales.  
    🔹 **Estado Contractual en Tiempo Real** → Cláusulas, vencimientos, opciones de compra.  
    🔹 **Herramientas de Negociación** → Opciones de recompra, fichajes con prima.  
    🔹 **Blockchain** → Contratos digitales y tokenización de derechos de jugadores.  
    """)

# Sección: DIFERENCIACIÓN
elif menu == "🔥 Diferenciación":
    st.title("🔥 Diferenciación – ¿Por Qué Futransfer?")
    st.markdown("""
    ✅ **No solo scouting** → Un ecosistema financiero y contractual.  
    ✅ **Verificación obligatoria de todos los usuarios** → Evita estafas.  
    ✅ **Oportunidades para clubes y agentes pequeños** → Acceso democrático al mercado.  
    ✅ **Tokenización y modelos financieros innovadores** → Inversión en fichajes mediante contratos digitales.  
    """)

# Sección: ROADMAP
elif menu == "🚀 Roadmap":
    st.title("🚀 Roadmap – Plan de Crecimiento")
    st.markdown("""
    📅 **Q1 2024:** Desarrollo MVP y beta privada con agentes.  
    📅 **Q2 2024:** Lanzamiento en mercados clave (España, Brasil, México, Argentina).  
    📅 **Q3 2024:** Expansión con IA y predicciones avanzadas.  
    📅 **Q4 2024:** Escalado global y monetización de transacciones.  
    """)

# Sección: INVERSIÓN
elif menu == "💵 Inversión":
    st.title("💵 Inversión – ¿Qué Necesitamos?")
    st.markdown("""
    🎯 **Objetivo de inversión: €1.5M**  
    📌 **Uso de fondos:**  
    - 50% Desarrollo tecnológico.  
    - 25% Expansión y captación de clientes.  
    - 15% Marketing y asociaciones estratégicas.  
    - 10% Cumplimiento legal y regulaciones FIFA.  
    """)

# Sección: EQUIPO
elif menu == "🌍 Equipo":
    st.title("🌍 Equipo – Quiénes Somos")
    st.markdown("""
    👤 **[Tu Nombre]** – Fundador y CEO (Experto en fichajes y tecnología).  
    👤 **[Co-Founder / CTO]** – Desarrollo y blockchain.  
    👤 **[Head of Legal]** – Especialista en derecho deportivo FIFA.  
    """)

# Sección: LLAMADO A LA ACCIÓN
elif menu == "🎯 Llamado a la Acción":
    st.title("🎯 ¡Invierte en Futransfer Ahora!")
    st.markdown("""
    📩 **Contacto:** [Tu email] | 📞 **Teléfono:** +[Número]  
    """)

