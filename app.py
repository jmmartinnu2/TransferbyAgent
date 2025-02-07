import streamlit as st

# Configuración inicial de Streamlit
st.set_page_config(page_title="FUTMATCH - Presentación", layout="wide")

# Barra lateral: Menú principal con emojis 📋
st.sidebar.title("📋 Menú de Navegación")
secciones = ["🏠 Introducción", "❌ Problemas Detectados", "✅ Soluciones FUTMATCH", 
             "📊 Datos del Informe FIFA", "👥 Casos Prácticos",  "🏆 Conclusiones"]
seleccion = st.sidebar.radio("Selecciona una sección:", secciones)

if seleccion == "🏠 Introducción":
    # Mostrar el logotipo centrado sin espacios extra
    col1, col2, col3 = st.columns([1, 3, 1])
    with col2:
        st.image("futmatch-logo-final.svg", width=800)

    # Separador
    st.markdown("---")

    # Contenido de la introducción
    st.markdown("""
    **Presentación de proyecto empresarial FUTMATCH**, Una plataforma revolucionaria que transformará el mundo de las transferencias en el fútbol.

    El fútbol es mucho más que un deporte; es un vibrante ecosistema que une pasión, talento y oportunidades. Sin embargo, el sistema tradicional de transferencias enfrenta desafíos estructurales que afectan a **agentes independientes**, **clubes pequeños** y **jugadores emergentes**. De acuerdo con el informe oficial de la FIFA 2024, solo el **5% de las agencias maneja el 60% de todas las transferencias internacionales**, lo que deja a muchos actores en una posición de desventaja.

    Conscientes de estas limitaciones, **FUTMATCH** nace con la misión de democratizar el acceso a oportunidades, creando un ecosistema digital que sea:
    
    - **Seguro** 🔒  
      Implementamos tecnología Blockchain para garantizar la integridad y transparencia de cada transacción.
    
    - **Transparente** 📊  
      Utilizamos datos validados y análisis de IA para proporcionar información precisa y en tiempo real.
    
    - **Global** 🌍  
      Conectamos agentes, clubes y jugadores de más de 150 países, eliminando barreras geográficas y abriendo nuevas oportunidades en el mercado mundial.
    
    Nuestra plataforma integra soluciones tecnológicas de vanguardia, como contratos inteligentes, inteligencia artificial y filtros avanzados, para conectar de forma directa a los actores del mercado y facilitar negociaciones eficientes y seguras.

    ¡Descubre cómo FUTMATCH está redefiniendo el mercado de fichajes y permitiendo que el talento encuentre el camino hacia nuevas oportunidades!
    """)



elif seleccion == "❌ Problemas Detectados":
    st.header("2. Problemas Detectados")
    # Subsecciones de problemas usando pestañas con emojis
    tab1, tab2, tab3, tab4, tab5, tab6, tab7 = st.tabs(["🌍 Acceso Limitado", "🚫 Representación Fraudulenta", "🤝 Competencia Desleal", "⏰ Baja Respuesta", "⚠️ Contratos Ambiguos", "💬 Dependencia de WhatsApp", "🤖 Clubes no élites"])
    
    with tab1:
        st.subheader("🌍 Acceso Limitado")
        st.write("""
        **Descripción**: Los agentes independientes y pequeñas agencias carecen de digitalización y procesos innovadores como conexiones globales para acceder a ligas internacionales y conectar con clubes de mayor nivel.
        
        **Problema**: Muchos agentes reportaron que, a pesar de tener talentosos jugadores en sus carteras, no pueden contactar con clubes de élite debido a la falta de redes globales o contactos personales. Por ejemplo, un agente en Colombia descubrió un talento juvenil prometedor, pero carece de conexiones para acceder a clubes europeos interesados. A largo plazo, esto lleva a que agentes pequeños pierdan hasta el **70% de sus jugadores** porque grandes agencias multinacionales monopolizan el acceso a estos mercados.
        """)

    with tab2:
        st.subheader("🚫 Representación Fraudulenta")
        st.write("""
        **Descripción**: Jugadores son ofrecidos por múltiples agentes distintos sin autorización, generando confusión entre los clubes interesados.
        
        **Problema**: La falta de verificación oficial de representantes crea un entorno propenso al fraude. Ejemplo: Un jugador fue ofrecido simultáneamente por tres agentes diferentes, lo que complicó la toma de decisiones por parte del club interesado. Según las encuestas, el **35% de las negociaciones fallan** debido a discrepancias sobre la calidad del jugador o la autenticidad de su representación. Además, algunos agentes reportaron recibir ofertas falsas diariamente, lo que genera desconfianza generalizada.
        """)

    with tab3:
        st.subheader("🤝 Competencia Desleal")
        st.write("""
        **Descripción**: Grandes agencias dominan el mercado, dejando poco margen para que agentes pequeños compitan en igualdad de condiciones.
        
        **Problema**: Las grandes agencias tienen acceso exclusivo a clubes de élite y recursos financieros superiores. Esto dificulta que agentes independientes puedan competir. Por ejemplo, un agente trabajó durante años con un jugador juvenil, pero cuando este llegó a categoría profesional, una gran multinacional lo reclutó sin compensar al agente original. Según el informe FIFA, solo el **20% de los agentes FIFA certificados participan activamente en transferencias internacionales**, mientras que el resto lucha por encontrar oportunidades.
        """)

    with tab4:
        st.subheader("⏰ Baja Respuesta")
        st.write("""
        **Descripción**: Los clubes no responden a mensajes enviados por agentes debido a la saturación de contactos (WhatsApp, email).
        
        **Problema**: Agentes dependen de canales informales como WhatsApp o correo electrónico para comunicarse con clubes, pero estos métodos son ineficientes y saturados. Un agente mencionó que envió decenas de mensajes a clubes interesados, pero nunca recibió respuesta. Esta falta de comunicación hace que las oportunidades se pierdan simplemente porque los clubes no tienen tiempo para filtrar y priorizar ofertas. Según las encuestas, esta situación es común, especialmente para agentes que trabajan en categorías inferiores.
        """)

    with tab5:
        st.subheader("⚠️ Contratos Ambiguos")
        st.write("""
        **Descripción**: Los contratos no cumplen con los acuerdos previos o son ambiguos, lo que genera disputas legales.
        
        **Problema**: Agentes reportaron que, después de cerrar acuerdos verbales con clubes, los contratos finales no reflejan las condiciones pactadas. En algunos casos, incluso las comisiones acordadas no se pagan. Ejemplo: Un agente cierra un acuerdo verbal con un club, pero al final del proceso, el contrato no se cumple o las comisiones acordadas no se pagan. Según el informe FIFA, existen investigaciones activas sobre agentes que no cumplen con los requisitos legales, lo que refuerza la necesidad de mecanismos legales claros.
        """)

    with tab6:
        st.subheader("💬 Dependencia de WhatsApp")
        st.write("""
        **Descripción**: Muchos agentes utilizan WhatsApp para realizar ofertas de jugadores, lo que genera desconfianza y falta de transparencia.
        
        **Problema**: El uso de WhatsApp para enviar ofertas de jugadores crea un entorno caótico donde las interacciones no están documentadas ni verificadas. Ejemplo: Un agente peruano reportó que recibe ofertas falsas o de intermediarios no autorizados diariamente, lo que genera incertidumbre sobre la legitimidad de las partes involucradas. Además, los clubes no pueden filtrar fácilmente las ofertas relevantes debido a la sobrecarga de mensajes. Según las encuestas, menos del **10% de las ofertas realizadas en WhatsApp terminan en transferencias reales.
        """)
    with tab7:
        st.subheader("💬 Clubes no élites")
        st.write("""
        **Descripción**: Los clubes no élite, que representan la mayoría dentro del fútbol profesional y semiprofesional, enfrentan grandes desafíos en la gestión de sus plantillas y en la identificación de oportunidades en el mercado de fichajes. A diferencia de los clubes de primer nivel, no cuentan con infraestructuras avanzadas, redes de scouting extensas ni herramientas tecnológicas que les permitan gestionar de manera eficiente la información sobre jugadores, transferencias y disponibilidad en el mercado.
        
        **Problema**: Falta de acceso a información actualizada: Los clubes no élite no tienen un sistema centralizado donde puedan conocer la situación contractual de jugadores representados por agentes o agencias.
        Dificultad en la captación de jugadores: No disponen de una base de datos accesible que les permita encontrar futbolistas que están libres, buscan cesión o podrían salir en el mercado de invierno.
        Comunicación fragmentada: La relación con agentes y otros clubes depende de contactos informales o redes dispersas, lo que ralentiza los procesos y genera incertidumbre en las negociaciones.
        Limitaciones en la toma de decisiones: Sin herramientas adecuadas, los clubes no élite tienen menos capacidad para anticiparse a oportunidades de mercado, afectando su competitividad y planificación deportiva.>.
            """)

elif seleccion == "✅ Soluciones FUTMATCH":
    st.header("3. Soluciones Clave para Agentes Independientes ")
    # Subsecciones de soluciones usando pestañas con emojis
    tab1, tab2, tab3, tab4 = st.tabs(["🌍 Acceso Global", "🤖 Validación y Promoción", "⏳ Gestión Eficiente", "🔒 Formalización de Procesos"])
    
    with tab1:
        st.subheader("🌍 Acceso Global a Mercados")
        st.write("""
        FUTMATCH rompe las barreras geográficas en la industria del fútbol, permitiendo que agentes y clubes de cualquier parte del mundo se conecten sin depender exclusivamente de redes de contacto personales o intermediarios. Con acceso a más de 150 países, la plataforma facilita la expansión del mercado de fichajes, abriendo nuevas oportunidades para jugadores, agentes y clubes en diferentes ligas y niveles de competición.
        
        ¿Qué beneficios ofrece este acceso global?
        
        ✅ Oportunidades internacionales sin límites
        Los agentes pueden presentar a sus jugadores a clubes de diferentes países y divisiones, maximizando sus opciones de traspaso, cesión o prueba en equipos que tradicionalmente estarían fuera de su alcance.

        ✅ Mayor visibilidad para jugadores y clubes
        Los futbolistas representados por agentes registrados en la plataforma tienen una mayor exposición ante clubes que buscan refuerzos en mercados emergentes o especializados.

        ✅ Negociaciones ágiles y directas
        El proceso de conexión entre agentes y clubes es rápido y eficiente, permitiendo que los jugadores puedan recibir ofertas en cuestión de días, sin la necesidad de desplazamientos físicos o intermediarios innecesarios.

        ✅ Diversificación de mercados
        Los clubes ya no dependen únicamente de su red local de scouting o de intermediarios conocidos; ahora pueden acceder a jugadores de cualquier parte del mundo y descubrir talentos en mercados que antes no exploraban.
        
        Ejemplos de casos reales:
        
        📌 Un agente peruano que representa a un mediocampista defensivo puede subir su perfil a FUTMATCH y, en menos de 72 horas, recibir interés de clubes portugueses o italianos que buscan un jugador con su perfil.

        📌 Un club de la segunda división de México necesita un delantero con experiencia en ligas sudamericanas. A través de la plataforma, puede encontrar a un atacante argentino sin necesidad de intermediarios externos, optimizando tiempo y costos en la negociación.
        """)

    with tab2:
        st.subheader("🤖 Validación y Promoción de Jugadores")
        st.write("""
        FUTMATCH se integra con APIs especializadas en datos de fútbol, lo que permite recopilar información en tiempo real sobre jugadores, estadísticas, videos y estado contractual. En lugar de depender exclusivamente de scouting manual o informes subjetivos, la plataforma obtiene datos estructurados y verificables desde fuentes confiables para validar y promocionar jugadores ante clubes de todo el mundo.

        ¿Cómo funciona este proceso?
        
        ✅ Recopilación automática de datos desde la API
        La plataforma se conecta con bases de datos especializadas en fútbol para obtener información detallada de cada jugador, incluyendo:

        Estadísticas de rendimiento (goles, asistencias, duelos ganados, precisión de pase, kilómetros recorridos, etc.)
        Historial de partidos y rendimiento en competiciones oficiales
        Clips de video de jugadas destacadas y análisis táctico
        
        Estado contractual y valor de mercado estimado
        
        ✅ Creación de perfiles de jugadores en tiempo real
        Cuando un agente sube un jugador a FUTMATCH, la plataforma consulta automáticamente la API para completar su perfil con información validada y actualizada, evitando la carga manual de datos y reduciendo errores.

        ✅ Recomendación inteligente de clubes
        Basándose en los criterios declarados por los clubes (posición, estilo de juego, disponibilidad, nivel competitivo), el sistema filtra jugadores dentro de la base de datos y sugiere automáticamente candidatos que encajan con sus necesidades.

        ✅ Mayor confianza y transparencia en las negociaciones
        Al utilizar datos obtenidos de fuentes oficiales, los clubes pueden tomar decisiones informadas sin depender de informes no verificables, aumentando la credibilidad de los jugadores dentro del mercado.

        Ejemplo de casos reales:

        📌 Un agente sube el perfil de un extremo brasileño de 22 años. La API completa automáticamente su historial de partidos, estadísticas recientes y videos de sus actuaciones más destacadas. Con esta información validada, un club de la MLS recibe una recomendación del jugador porque busca un atacante con sus características.

        📌 Un club de la Serie B italiana necesita un mediocampista con alta recuperación de balón. La plataforma consulta la API y sugiere varios jugadores que cumplen con ese perfil, mostrándoles sus estadísticas y clips de video para facilitar la toma de decisiones.
        """)

    with tab3:
        st.subheader("⏳ Gestión Eficiente de Jugadores")
        st.write("""
        FUTMATCH proporciona herramientas integradas para el seguimiento del rendimiento, gestión de contratos y planificación de transferencias. Automatiza procesos administrativos como recordatorios de renovación de contratos y notificaciones de interés de clubes.
        
        ¿Qué soluciones ofrece FUTMATCH?
        
        ✅ Acceso centralizado a información
        Los clubes podrán visualizar en un solo lugar la situación de jugadores representados por agentes y agencias, con información fiable y actualizada sobre su disponibilidad en el mercado.

        ✅ Espacio único y privado para negociaciones
        La plataforma ofrece un entorno seguro y exclusivo donde clubes y agentes pueden interactuar directamente, garantizando privacidad en las negociaciones y la posibilidad de seleccionar con qué agente o agencia desean hacer negocios.

        ✅ Acceso a jugadores y ofertas en tiempo real
        Los clubes podrán encontrar jugadores disponibles en función de sus necesidades (libres, cesiones, transferibles, etc.), mientras que los agentes tendrán acceso directo a las ofertas que los clubes propongan.

        ✅ Herramientas innovadoras para clubes
        Los clubes dispondrán de soluciones tecnológicas avanzadas para gestionar más eficientemente el proceso de fichajes, optimizando su tiempo y mejorando la toma de decisiones estratégicas.
                Ejemplo: Un agente puede gestionar todos sus jugadores desde una sola interfaz, reduciendo significativamente el tiempo dedicado a tareas manuales.
        """)

    with tab4:
        st.subheader("🔒 Formalización de Procesos")
        st.write("""
        FUTMATCH lleva la transparencia y seguridad en las transferencias de jugadores a otro nivel mediante el uso de contratos inteligentes y tecnología blockchain. Con estos mecanismos, todos los acuerdos entre clubes y agentes quedan registrados de forma inmutable, eliminando riesgos de incumplimientos, malentendidos o disputas legales.

        ¿Cómo funciona este proceso?
        
        ✅ Automatización de contratos con Smart Contracts
        Los contratos inteligentes permiten que los acuerdos entre clubes y agentes se ejecuten de manera automática cuando se cumplen las condiciones pactadas, sin necesidad de intermediarios.

        ✅ Registro en Blockchain: Seguridad y Transparencia
        Toda la información contractual se almacena en blockchain, garantizando que los datos sean inalterables y verificables en cualquier momento. Esto evita fraudes, incumplimientos o modificaciones unilaterales de acuerdos.

        ✅ Pagos y comisiones automatizados
        Las comisiones de los agentes y otros pagos relacionados con la transferencia de un jugador se liberan de forma segura y automática cuando se cumplen los términos establecidos en el contrato.

        ✅ Historial de transacciones verificable
        Cada transferencia, cesión o acuerdo queda registrado con trazabilidad completa, permitiendo a los clubes y agentes consultar el historial de sus negociaciones sin riesgos de pérdida de datos.

        Ejemplo de casos reales:
        
        📌 Un agente negocia la cesión de un delantero a un club europeo. Ambas partes firman un contrato inteligente en FUTMATCH, estableciendo que la comisión del agente se libere automáticamente cuando el jugador complete su debut oficial. Al cumplirse la condición, el pago se procesa sin retrasos ni intervención manual.

        📌 Un club ficha a un mediocampista con una cláusula de rendimiento. Gracias al sistema blockchain, la plataforma verifica automáticamente si el jugador ha cumplido con los objetivos pactados (ejemplo: 20 partidos jugados), activando el pago de un bono adicional sin necesidad de renegociaciones o disputas.
        """)

elif seleccion == "🏆 Soluciones Clave para Clubes de Categorías Inferiores":
    st.header("4. Soluciones Clave para Clubes de Categorías Inferiores ")
    # Subsecciones de soluciones usando pestañas con emojis
    tab1, tab2, tab3, tab4 = st.tabs(["📚 Acceso Centralizado", "📩 Reducción de Sobrecarga", "🏆 Equidad Competitiva", "⚡ Optimización del Tiempo"])
    
    with tab1:
        st.subheader("📚 Acceso Centralizado a Información")
        st.write("""
        FUTMATCH ofrece una base de datos completa y actualizada de jugadores disponibles, filtrable por posición, edad, nacionalidad, estado contractual y valor de mercado.
        
        Ejemplo: Un club de tercera división busca un delantero centro Sub-23 bajo €2K/mes y encuentra múltiples opciones en menos de 5 minutos.
        """)

    with tab2:
        st.subheader("📩 Reducción de Sobrecarga")
        st.write("""
        Los clubes pueden explorar opciones de forma autónoma en FUTMATCH, eliminando llamadas innecesarias y mensajes saturados. La plataforma proporciona un historial detallado de todas las interacciones con agentes y jugadores, facilitando el seguimiento y toma de decisiones.
        
        Ejemplo: Un director deportivo recibe alertas solo sobre jugadores relevantes, evitando perder tiempo en ofertas no válidas.
        """)

    with tab3:
        st.subheader("🏆 Equidad Competitiva")
        st.write("""
        FUTMATCH niveló el campo de juego al proporcionar herramientas profesionales a todos los clubes, independientemente de su tamaño o presupuesto. Ofrece acceso igualitario a información detallada sobre jugadores, eliminando la ventaja injusta de quienes tienen más recursos.
        
        Ejemplo: Un equipo semi-profesional tiene acceso a los mismos filtros avanzados que un equipo de primera división.
        """)

    with tab4:
        st.subheader("⚡ Optimización del Tiempo")
        st.write("""
        Automatiza procesos administrativos como la gestión de propuestas, seguimiento de intereses y comunicación entre partes. Contratos inteligentes ejecutan pagos y cláusulas automáticamente, acelerando el proceso de transferencia.
        
        Ejemplo: Un fichaje que antes tomaba semanas ahora se completa en días gracias a la automatización y transparencia.
        """)


elif seleccion == "📊 Datos del Informe FIFA":
    st.header("4. Datos Relevantes del Informe sobre Agentes FIFA 2024 📊")
    st.write("""
    **🔍 Datos clave del informe:**

    - **Agentes internacionales:** Solo **1,196** de los **7,558** agentes licenciados proporcionaron servicios en transferencias internacionales.
    - **Honorarios predominantes:** El **91%** de los casos involucran honorarios inferiores a **USD 1 millón**.
    - **Concentración del gasto:** Los **196** casos con honorarios superiores a **USD 1 millón** representan el **60.5%** del gasto total.

    💰 **Ejemplo destacado:**
    - Un solo agente lideró con aproximadamente **USD 40 millones** en honorarios, mientras que la mayoría de los agentes operan con presupuestos mucho más modestos.

    ---

    **📈 Interpretación:**
    - Los grandes agentes dominan el mercado gracias a su capacidad para gestionar transferencias multimillonarias, lo que limita las oportunidades para agentes más pequeños o emergentes.
    - Esta situación crea una barrera de entrada para nuevos talentos y restringe la diversidad en la industria.

    ---

    **🌐 Desigualdad en el Acceso a Información y Redes**

    **Datos clave del informe:**
    - Los agentes **británicos**, **italianos** y **franceses** lideran tanto en número de transferencias como en ingresos por honorarios.
    - Existe una fuerte correlación entre el país de origen del agente y su éxito en el mercado internacional.

    **Interpretación:**
    - Los agentes consolidados tienen acceso privilegiado a redes internacionales, bases de datos avanzadas y relaciones con clubes influyentes, lo que dificulta que agentes de países con menor presencia en el fútbol profesional compitan en igualdad de condiciones.

    ---

    **⚖️ Complejidad Regulatoria**

    **Datos clave del informe:**
    - Se realizaron **1,627 investigaciones** sobre incumplimientos de requisitos de elegibilidad durante el período cubierto.
    - Alrededor del **17%** de estas investigaciones resultaron en el rechazo de solicitudes de licencia.

    **Interpretación:**
    - Aunque las regulaciones estrictas son esenciales para garantizar la integridad del sistema, pueden representar un obstáculo para agentes nuevos o con menos experiencia.
    - Esto favorece a los grandes agentes, que cuentan con los recursos legales y financieros necesarios para cumplir con todos los requisitos.
    """)


elif seleccion == "👥 Casos Prácticos":
    st.header("5. Casos Prácticos")
    
    st.subheader("👨‍💼 Caso de Agente Independiente")
    st.write("""
    Un agente peruano representa a un mediocampista defensivo joven con gran potencial. Sin acceso a redes globales, le resultaba difícil encontrar oportunidades para su jugador. Con **FUTMATCH**:
    - 📝 **Perfil Completo:** Sube el perfil del jugador a la plataforma, incluyendo videos, estadísticas y un análisis de IA que valida su calidad.
    - 🔎 **Búsqueda Eficiente:** Utiliza filtros avanzados para identificar clubes interesados en jugadores con características similares.
    - 📩 **Negociaciones Directas:** Recibe ofertas directamente a través de la plataforma, eliminando intermediarios y asegurando transparencia en las negociaciones.
    - 🔄 **Transferencia Ágil:** Completa la transferencia en menos de 72 horas gracias a contratos inteligentes y registro en Blockchain.
        """)
        
    st.subheader("⚽ Caso de Club 3ª División")
    st.write("""
    Un club de 3ª división busca un delantero centro joven con experiencia internacional. Sin herramientas tecnológicas, este proceso sería extremadamente complicado. Con **FUTMATCH**:
    - 📋 **Búsqueda Específica:** Ingresa a la plataforma y aplica filtros avanzados: "Delantero centro", "Edad: 18-23 años", "Experiencia internacional", "Estado: Libre".
    - 📊 **Exploración de Opciones:** Revisa los resultados y selecciona los jugadores de interés.
    - 📩 **Comunicación Directa:** Envía ofertas directamente desde la plataforma y recibe respuestas en tiempo real.
    - ✍️ **Formalización Simplificada:** Negocia y firma el contrato digital sin papeleo excesivo.
    """)
        
    st.subheader("🤝 Caso de colaboración entre Agentes (Agentes Vinculados)")
    st.write("""
    Dos agentes, uno de Argentina y otro de México, deciden unir esfuerzos para promover el perfil de un mediocampista ofensivo que ha mostrado un rendimiento sobresaliente. Con **FUTMATCH**:
    - 🔄 **Intercambio de Información:** Cada agente sube y comparte el perfil del jugador, enriquecido con datos validados y análisis de IA.
    - 🌍 **Estrategia Conjunta:** Utilizan la plataforma para coordinar una estrategia conjunta, identificando clubes internacionales interesados en perfiles similares.
    - 🤝 **Negociación Coordinada:** Al recibir ofertas, los agentes trabajan en conjunto para negociar de forma coordinada, asegurando que ambas partes sean reconocidas.
    - 🔒 **Ejecución Confiable:** La transferencia se formaliza mediante contratos inteligentes en Blockchain, garantizando que ambos agentes reciban su comisión de forma automática y segura.
    """)
    
    st.subheader("🌍 Caso de red de Agentes Internacionales")
    st.write("""
    Una red de agentes de distintos países forma una alianza estratégica para impulsar a jugadores emergentes en mercados globales. Con **FUTMATCH**:
    - 📡 **Intercambio Global:** Los agentes integran sus perfiles de jugadores, enriquecidos con análisis de rendimiento y videos destacados, en una base de datos compartida.
    - 💼 **Acceso a Mercados:** Aprovechan el acceso a más de 150 países para promocionar oportunidades y ofertas de transferencias.
    - 🔍 **Validación y Transparencia:** Gracias a la integración de APIs, IA y registro en Blockchain, toda la información es validada y transparente, generando confianza entre las partes.
    - ⚡ **Ejecución Rápida:** La colaboración permite cerrar acuerdos en tiempo récord, beneficiando tanto a los jugadores como a los agentes al ampliar sus redes de negocio.
    """)



elif seleccion == "🏆 Conclusiones":
    st.header("6. Conclusiones 🏆")
    st.write("""
    FUTMATCH no es solo una plataforma, es una revolución en el mundo de las transferencias futbolísticas. Al eliminar las barreras estructurales que han mantenido a agentes independientes, clubes pequeños y jugadores emergentes al margen del mercado global, estamos creando un nuevo paradigma en el fútbol profesional.

    Con FUTMATCH, los actores más pequeños ya no tendrán que competir con desventajas tecnológicas, financieras y operativas. Nuestra plataforma empodera a todos los jugadores del ecosistema, permitiendo que accedan a oportunidades globales y transformando su capacidad de negociación.

    ¿Por qué FUTMATCH es la única opción para el futuro del fútbol?
    🔑 Acceso a oportunidades globales: Nunca más un club pequeño o un agente independiente tendrá que conformarse con un mercado limitado. FUTMATCH abre puertas a más de 150 países, conectando a actores del fútbol de todo el mundo.

    ⚡ Tecnología de vanguardia al alcance de todos: Nuestra integración con Blockchain y IA no es solo para los grandes. Todos los usuarios pueden aprovechar estas tecnologías avanzadas para tomar decisiones informadas, transparentes y seguras.

    ⏱️ Productividad maximizada: La automatización de procesos y la optimización mediante herramientas inteligentes permiten a los agentes y clubes concentrarse en lo más importante: el desarrollo del talento y la mejora de su rendimiento. Es un cambio total en la forma de hacer negocios, donde el tiempo y los recursos son aprovechados al máximo.

    💡 Un ecosistema democrático y accesible: FUTMATCH no es un juego para unos pocos. Es para todos. Desde el agente independiente que busca abrirse camino hasta el club pequeño que aspira a competir con los grandes, todos tienen la misma oportunidad de crecer y prosperar.
    
    El futuro del fútbol es inclusivo, y FUTMATCH es su motor.
    """)

# Footer con emojis
st.write("---")
st.caption("FUTMATCH | 🌍 Donde el talento encuentra oportunidad")
