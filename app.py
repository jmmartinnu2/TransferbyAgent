import streamlit as st
from PIL import Image

# ============================
# CONFIGURACIÓN Y ESTILOS
# ============================
st.set_page_config(page_title='Memoria Futransfer', layout='wide', page_icon=':soccer:')

# CSS personalizado para mejorar la apariencia
st.markdown(
    """
    <style>
    /* Fondo y tipografía */
    body {
        background-color: #f5f5f5;
        font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif;
    }
    /* Estilos para las secciones */
    .section {
        background-color: #ffffff;
        padding: 25px;
        border-radius: 10px;
        margin-bottom: 20px;
        box-shadow: 0 4px 8px rgba(0,0,0,0.1);
    }
    .subsection {
        background-color: #e3f2fd;
        padding: 20px;
        border-radius: 8px;
        margin-bottom: 15px;
    }
    .highlight {
        background-color: #fff3e0;
        padding: 15px;
        border-radius: 8px;
        margin-bottom: 15px;
    }
    .title {
        color: #253439;
        font-size: 3rem;
        font-weight: bold;
    }
    .subtitle {
        color: #253439;
        font-size: 1.5rem;
        margin-bottom: 10px;
    }
    hr {
        border: 1px solid #ddd;
    }
    .sidebar-title {
        font-size: 1.3rem;
        font-weight: bold;
        margin-bottom: 20px;
    }
    </style>
    """, unsafe_allow_html=True
)

# ============================
# FUNCIONES DE CADA SECCIÓN
# ============================

def show_resumen_ejecutivo():
   
    st.image("futransfer.svg", width=1000)
    st.markdown("<h1 class='title'>Resumen Ejecutivo</h1>", unsafe_allow_html=True)
    st.markdown(
        """
        <p><strong>Futransfer</strong> es una plataforma digital innovadora destinada a transformar el mercado de fichajes en el fútbol. Nuestra solución democratiza las oportunidades, eliminando barreras económicas y geográficas, e integrando tecnología de punta, Inteligencia Artificial (IA) y sistemas de verificación automatizados para crear un ecosistema seguro, transparente y eficiente.</p>
        <ul>
          <li><strong>Oportunidad de mercado:</strong> El mercado está dominado por grandes actores, dejando fuera a miles de profesionales y clubes de niveles inferiores, donde se mueve una gran cantidad de dinero.</li>
          <li><strong>Propuesta de valor:</strong> Integración de datos exclusivos, análisis en tiempo real, contratos inteligentes y networking global, que permiten decisiones estratégicas rápidas y seguras.</li>
          <li><strong>Objetivo:</strong> Impulsar la transformación digital en el proceso de fichajes y ampliar el alcance a todos los niveles del fútbol.</li>
        </ul>
        """, unsafe_allow_html=True
    )
    st.markdown("</div>", unsafe_allow_html=True)

def show_descripcion_startup():
    st.markdown("<div class='section'>", unsafe_allow_html=True)
    st.markdown("<h1 class='title'>Descripción de Futransfer</h1>", unsafe_allow_html=True)
    st.markdown(
        """
        <p><strong>Nombre:</strong> Futransfer</p>
        <p><strong>Sector/Industria:</strong> Tecnología aplicada al deporte / Fútbol</p>
        <p><strong>Misión:</strong> Transformar el mercado de fichajes en el fútbol, facilitando el acceso y la transparencia para agentes, agencias y clubes no pertenecientes a la élite, impulsando la digitalización y abriendo un amplio mercado de oportunidades en sectores tradicionalmente desatendidos.</p>
        <p><strong>Visión:</strong> Ser la plataforma líder a nivel global en digitalización de transferencias, creando oportunidades de negocio y fortaleciendo el ecosistema futbolístico.</p>
        <p><strong>Valores:</strong></p>
        <ul>
          <li>Transparencia</li>
          <li>Innovación</li>
          <li>Equidad</li>
          <li>Colaboración</li>
        </ul>
        """, unsafe_allow_html=True
    )
    st.markdown("</div>", unsafe_allow_html=True)

def show_analisis_problema_oportunidad():
    st.markdown("<div class='section'>", unsafe_allow_html=True)
    st.markdown("<h1 class='title'>Análisis del Problema y Oportunidad</h1>", unsafe_allow_html=True)
    # Problema Identificado
    st.markdown("<h2 class='subtitle'>Problema Identificado</h2>", unsafe_allow_html=True)
    st.markdown(
        """
        <p>El mercado de fichajes ha sido históricamente dominado por un pequeño grupo con alto poder adquisitivo, lo que genera prácticas desleales, ofertas fraudulentas y contratos ambiguos. Esto afecta a miles de profesionales y equipos, especialmente en niveles inferiores.</p>
        """, unsafe_allow_html=True
    )
    # Oportunidad de Mercado
    st.markdown("<h2 class='subtitle'>Oportunidad de Mercado</h2>", unsafe_allow_html=True)
    st.markdown(
        """
        <p>Existe un mercado internacional amplio que no se limita a los clubes de élite. Muchos clubes de niveles inferiores mueven grandes sumas y tienen necesidades específicas de digitalización.</p>
        <p><strong>Observación Clave:</strong> Futransfer aspira a entrar en estos mercados, ayudando a clubes, agentes y agencias a modernizar sus procesos y a tomar decisiones estratégicas basadas en datos.</p>
        """, unsafe_allow_html=True
    )
    st.markdown("</div>", unsafe_allow_html=True)

def show_propuesta_valor():
    st.markdown("<div class='section'>", unsafe_allow_html=True)
    st.markdown("<h1 class='title'>Propuesta de Valor y Solución</h1>", unsafe_allow_html=True)
    st.markdown(
        """
        <p><strong>Propuesta de Valor:</strong> Futransfer combina tecnología de vanguardia, IA y contratos digitales para transformar y transparentar el proceso de fichajes en el fútbol.</p>
        <h2 class='subtitle'>Características Clave del Producto:</h2>
        <ul>
          <li><strong>Alertas en tiempo real:</strong> Notificaciones automáticas para identificar oportunidades.</li>
          <li><strong>Filtros inteligentes:</strong> Búsqueda avanzada por criterios deportivos y contractuales.</li>
          <li><strong>Verificación instantánea:</strong> Certificación de identidad con tecnología de última generación.</li>
          <li><strong>Contratos inteligentes:</strong> Automatización de acuerdos y pagos, eliminando intermediarios.</li>
          <li><strong>Networking global:</strong> Conexión entre agentes, clubes y agencias en más de 150 países.</li>
        </ul>
        <h2 class='subtitle'>Beneficios:</h2>
        <ul>
          <li>Mayor transparencia y confianza en las negociaciones.</li>
          <li>Decisiones estratégicas basadas en datos exclusivos y análisis en tiempo real.</li>
          <li>Acceso a un mercado ampliado que incluye clubes de todos los niveles.</li>
        </ul>
        """, unsafe_allow_html=True
    )
    st.markdown("</div>", unsafe_allow_html=True)

def show_modelo_negocio():
    st.markdown("<div class='section'>", unsafe_allow_html=True)
    st.markdown("<h1 class='title'>Modelo de Negocio</h1>", unsafe_allow_html=True)
    st.markdown(
        """
        <h2 class='subtitle'>Fuentes de Ingreso</h2>
        <ul>
          <li>Comisiones por transacción (2% del valor total).</li>
          <li>Modelo freemium: Acceso básico gratuito con opciones premium.</li>
          <li>Alianzas estratégicas y publicidad.</li>
        </ul>
        <h2 class='subtitle'>Estructura de Costos</h2>
        <p>Desarrollo y mantenimiento tecnológico, marketing, operaciones y soporte, infraestructura en la nube y seguridad de datos.</p>
        <h2 class='subtitle'>Estrategia de Monetización</h2>
        <p>Combinación de ingresos recurrentes y comisiones por transacción para asegurar márgenes sostenibles.</p>
        """, unsafe_allow_html=True
    )
    st.markdown("</div>", unsafe_allow_html=True)

def show_analisis_mercado_competencia():
    st.markdown("<div class='section'>", unsafe_allow_html=True)
    st.markdown("<h1 class='title'>Análisis de Mercado y Competencia</h1>", unsafe_allow_html=True)
    st.markdown(
        """
        <h2 class='subtitle'>Tamaño y Segmentación del Mercado</h2>
        <p>El mercado total abarca las transferencias a nivel global. Nuestro foco incluye equipos de élite y, especialmente, clubes de niveles inferiores con necesidades de digitalización.</p>
        <h2 class='subtitle'>Competencia</h2>
        <p><strong>Competidores Tradicionales:</strong> Wyscout, BeSoccer, entre otros.</p>
        <p><strong>Ventaja Competitiva:</strong> Futransfer integra datos exclusivos, análisis en tiempo real y contratos inteligentes, abarcando desde la élite hasta clubes de niveles inferiores.</p>
        """, unsafe_allow_html=True
    )
    st.markdown("</div>", unsafe_allow_html=True)

def show_estrategia_marketing():
    st.markdown("<div class='section'>", unsafe_allow_html=True)
    st.markdown("<h1 class='title'>Estrategia de Marketing y Ventas</h1>", unsafe_allow_html=True)
    st.markdown(
        """
        <h2 class='subtitle'>Posicionamiento</h2>
        <p>Futransfer se posiciona como la solución tecnológica líder en digitalización de transferencias, enfocada en transparencia y oportunidades para todos los actores del fútbol.</p>
        <h2 class='subtitle'>Canales de Marketing</h2>
        <ul>
          <li>Marketing digital (SEO, SEM, redes sociales).</li>
          <li>Eventos y ferias del sector.</li>
          <li>Alianzas con influencers y líderes de opinión.</li>
        </ul>
        <h2 class='subtitle'>Plan de Ventas</h2>
        <ul>
          <li>Estrategia de captación con demos y pruebas gratuitas.</li>
          <li>Seguimiento personalizado y fidelización de clientes.</li>
          <li>Métricas clave: tasa de conversión, retención y satisfacción.</li>
        </ul>
        """, unsafe_allow_html=True
    )
    st.markdown("</div>", unsafe_allow_html=True)

def show_roadmap():
    st.markdown("<div class='section'>", unsafe_allow_html=True)
    st.markdown("<h1 class='title'>Roadmap / Plan de Acción</h1>", unsafe_allow_html=True)
    st.markdown(
        """
        <h2 class='subtitle'>Fase 1: Validación del Producto</h2>
        <ul>
          <li>Desarrollo del MVP de la plataforma.</li>
          <li>Pruebas de usuario y recopilación de feedback.</li>
          <li>Ajustes y mejoras según los resultados.</li>
        </ul>
        <h2 class='subtitle'>Fase 2: Lanzamiento y Crecimiento</h2>
        <ul>
          <li>Lanzamiento en mercados clave (incluyendo clubes de niveles inferiores).</li>
          <li>Captación de los primeros clientes y validación del modelo.</li>
          <li>Optimización continua de la plataforma.</li>
        </ul>
        <h2 class='subtitle'>Fase 3: Expansión y Escalabilidad</h2>
        <ul>
          <li>Expansión a nuevos mercados internacionales.</li>
          <li>Incremento de funcionalidades y alianzas estratégicas.</li>
          <li>Escalabilidad de la infraestructura y procesos.</li>
        </ul>
        """, unsafe_allow_html=True
    )
    st.markdown("</div>", unsafe_allow_html=True)

def show_equipo():
    st.markdown("<div class='section'>", unsafe_allow_html=True)
    st.markdown("<h1 class='title'>Equipo Fundador y Organización</h1>", unsafe_allow_html=True)
    st.markdown(
        """
        <p><strong>Equipo Fundador:</strong></p>
        <ul>
          <li><strong>José Mª Martín</strong> – CEO Founder: Amplia experiencia en el sector deportivo y tecnológico.</li>
          <li><strong>Javier Omiste</strong>- CoFounder – Experto en desarrollo de soluciones digitales y tecnologías emergentes.</li>
        </ul>
        <p><strong>Estructura Organizativa:</strong> Organigrama centrado en roles clave (desarrollo, marketing, ventas y soporte).</p>
        <p><strong>Asesores y Mentores:</strong> Colaboradores estratégicos con experiencia en fútbol, tecnología e inversión.</p>
        """, unsafe_allow_html=True
    )
    st.markdown("</div>", unsafe_allow_html=True)

def show_proyecciones():
    st.markdown("<div class='section'>", unsafe_allow_html=True)
    st.markdown("<h1 class='title'>Proyecciones Financieras y Requerimientos de Inversión</h1>", unsafe_allow_html=True)
    st.markdown(
        """
        <h2 class='subtitle'>Proyecciones Financieras</h2>
        <p>Estimaciones de crecimiento de ingresos y optimización de costos a 3-5 años, con enfoque en la escalabilidad.</p>
        <h2 class='subtitle'>Requerimientos de Inversión</h2>
        <ul>
          <li><strong>Monto solicitado:</strong> [Cantidad en USD o moneda local]</li>
          <li><strong>Uso de Fondos:</strong>
            <ul>
              <li>Desarrollo y mejoras de la plataforma.</li>
              <li>Estrategia de marketing y expansión.</li>
              <li>Contratación de personal clave.</li>
              <li>Refuerzo de infraestructura y seguridad.</li>
            </ul>
          </li>
        </ul>
        <h2 class='subtitle'>Retorno Esperado</h2>
        <p>Proyecciones de ROI basadas en la captación de clientes y expansión en mercados internacionales.</p>
        """, unsafe_allow_html=True
    )
    st.markdown("</div>", unsafe_allow_html=True)

def show_conclusion():
    st.markdown("<div class='section'>", unsafe_allow_html=True)
    st.markdown("<h1 class='title'>Conclusión y Llamada a la Acción</h1>", unsafe_allow_html=True)
    st.markdown(
        """
        <p>Futransfer representa una oportunidad revolucionaria para transformar el mercado de fichajes en el fútbol, abriendo oportunidades en segmentos descapitalizados y facilitando la digitalización de procesos para todos los actores.</p>
        <p>Invitamos a los inversores a sumarse a este proyecto disruptivo y ser parte de la transformación digital que potenciará la eficiencia y transparencia en el sector futbolístico.</p>
        <p><strong>Contacto:</strong></p>
        <ul>
          <li>Email: <a href='mailto:futransfer@gmail.com'>futransfer@gmail.com</a></li>
          <li>Teléfono: +34 645764853</li>
          <li>Página web: <a href='https://www.futransfer.com' target='_blank'>www.futransfer.com</a></li>
        </ul>
        """, unsafe_allow_html=True
    )
    st.markdown("</div>", unsafe_allow_html=True)

def show_anexos():
    st.markdown("<div class='section'>", unsafe_allow_html=True)
    st.markdown("<h1 class='title'>Anexos</h1>", unsafe_allow_html=True)
    st.markdown(
        """
        <ul>
          <li>Estudios de mercado detallados</li>
          <li>Prototipos y demos de la plataforma</li>
          <li>Casos de éxito y testimonios</li>
          <li>Documentación adicional y planes operativos</li>
        </ul>
        """, unsafe_allow_html=True
    )
    st.markdown("</div>", unsafe_allow_html=True)

# ============================
# MENÚ LATERAL DE NAVEGACIÓN
# ============================
st.sidebar.markdown("<div class='sidebar-title'>Navegación</div>", unsafe_allow_html=True)
menu = st.sidebar.radio("Selecciona una sección", 
    [
        "Resumen Ejecutivo", "Descripción de Futransfer", "Problema y Oportunidad", 
        "Propuesta de Valor", "Modelo de Negocio", "Análisis de Mercado", 
        "Estrategia de Marketing", "Roadmap", "Equipo y Organización", 
        "Proyecciones e Inversión", "Conclusión"
    ]
)

# ============================
# MOSTRAR SECCIÓN SELECCIONADA
# ============================
if menu == "Resumen Ejecutivo":
    show_resumen_ejecutivo()
elif menu == "Descripción de Futransfer":
    show_descripcion_startup()
elif menu == "Problema y Oportunidad":
    show_analisis_problema_oportunidad()
elif menu == "Propuesta de Valor":
    show_propuesta_valor()
elif menu == "Modelo de Negocio":
    show_modelo_negocio()
elif menu == "Análisis de Mercado":
    show_analisis_mercado_competencia()
elif menu == "Estrategia de Marketing":
    show_estrategia_marketing()
elif menu == "Roadmap":
    show_roadmap()
elif menu == "Equipo y Organización":
    show_equipo()
elif menu == "Proyecciones e Inversión":
    show_proyecciones()
elif menu == "Conclusión":
    show_conclusion()
