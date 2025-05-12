================================================================================
🛡️ Simulador Ético de Keylogger con Detección de Cripto y CLI Modular
================================================================================

Este proyecto educativo simula de manera segura el comportamiento de un keylogger
centrado en la detección de patrones relacionados con criptomonedas. Está diseñado
para ejecutarse únicamente en entornos controlados con fines de análisis, defensa
y aprendizaje sobre ciberseguridad.

--------------------------------------------------------------------------------
🎯 Características
--------------------------------------------------------------------------------

✔ Captura de pulsaciones con `pynput`
✔ Detección de patrones tipo wallet, dirección cripto, frase semilla
✔ Registro y alerta local en archivos separados
✔ Simulación de pagos en cripto (enviar/recibir)
✔ CLI modular usando patrón Command + Factory
✔ Arquitectura extensible y segura para prácticas de laboratorio

--------------------------------------------------------------------------------
🧠 Patrones de Diseño Utilizados
--------------------------------------------------------------------------------

- Command Pattern: cada acción es un comando independiente
- Factory Pattern: generación dinámica de comandos desde CLI
- Observer Pattern: alertas de patrones maliciosos observadas en tiempo real

--------------------------------------------------------------------------------
🚀 Cómo ejecutar el proyecto
--------------------------------------------------------------------------------

1. Navega al proyecto:
   cd ~

2. Activa el entorno virtual:
   source venv/bin/activate

3. Instala dependencias:
   pip install pynput cryptography

4. Ejecuta el menú principal:
   python controller.py

--------------------------------------------------------------------------------
🧪 Opciones del menú
--------------------------------------------------------------------------------

1. Iniciar keylogger
2. Detener keylogger
3. Ver registros
4. Ver alertas de patrones
5. Simular pago con cripto
6. Cifrar registros
0. Salir

--------------------------------------------------------------------------------
🔒 Ética y Seguridad
--------------------------------------------------------------------------------

⚠ Este simulador NO debe usarse en entornos reales o no controlados.
⚠ Todos los datos permanecen localmente. No hay exfiltración de información.
⚠ El código tiene propósitos exclusivamente didácticos, de auditoría o defensa.

--------------------------------------------------------------------------------
🤖 Integración con CodeRabbit (GitHub PR Review)
--------------------------------------------------------------------------------

- Incluye archivo `.coderabbit/config.json` personalizado
- Revisa automáticamente arquitectura, prácticas y seguridad al crear Pull Requests
- Recomendado para proyectos colaborativos o educativos con revisión automática

--------------------------------------------------------------------------------
📜 Licencia

MIT — Para uso académico, ético y de investigación exclusivamente.
