# Simulador Ético de Keylogger en Python 🧪🖥️

Este proyecto forma parte de una práctica universitaria con fines educativos y éticos en el estudio de técnicas de análisis de malware. Simula el comportamiento básico de un troyano con módulo keylogger sin exfiltrar datos ni dañar el sistema, operando únicamente en entornos de laboratorio controlados.

------------------------------------------------------------
📁 Estructura del Proyecto

practica_virologia/
├── controller.py          # CLI para controlar el simulador
├── keylogger.py           # Captura las pulsaciones del teclado
├── log_encryptor.py       # Cifra el archivo de logs (opcional)
├── logs/                  # Carpeta donde se guarda el archivo log
└── venv/                  # Entorno virtual Python
------------------------------------------------------------

🚀 Instrucciones de Uso

1. Clona o ubica esta carpeta en tu escritorio:

   cd ~/Desktop/practica_virologia

2. Activa el entorno virtual existente:

   source venv/bin/activate

   Si no existe, créalo:
   python3 -m venv venv
   source venv/bin/activate

3. Instala las dependencias necesarias:

   pip install pynput cryptography

4. Ejecuta el controlador del proyecto:

   python controller.py

   Verás el siguiente menú:

   1. Iniciar keylogger
   2. Ver registros
   3. Cifrar registros

------------------------------------------------------------
🧠 Detalles Técnicos

- Captura teclas presionadas usando `pynput`.
- Guarda registros locales con marca de tiempo.
- Cifra el log (opcional) usando `cryptography.Fernet`.
- Simula autoejecución (solo impresión, no se modifica el sistema).
------------------------------------------------------------

🛠️ Solución a Errores Comunes

🔴 Error: "pynput no se ha podido resolver" (Pylance)

Causa: VS Code no detecta correctamente el entorno virtual.

Solución:
1. Verifica que `venv` esté dentro del proyecto.
2. En VS Code, selecciona el intérprete con:
   Cmd+Shift+P → "Python: Select Interpreter" → selecciona `./venv/bin/python`
3. Reinicia VS Code si persiste el problema.

Opcionalmente, desactiva la advertencia en settings.json:

  "python.analysis.diagnosticSeverityOverrides": {
    "reportMissingModuleSource": "none"
  }

------------------------------------------------------------
⚠️ Advertencia Ética

Este simulador no debe utilizarse en sistemas reales fuera de entornos de laboratorio. Su propósito es estrictamente académico para aprender a detectar, analizar y defenderse de software malicioso.

------------------------------------------------------------
📜 Licencia

MIT – Para fines educativos únicamente.