# Vimi

**Vimi** es un editor simple de código en **Python con wxPython**, creado como recurso educativo accesible.  
El nombre es un homenaje a [Vim](https://www.vim.org/), uno de los editores más influyentes.

## 🚀 Características

- Interfaz gráfica hecha con [wxPython](https://wxpython.org/).
- Área de edición básica para escribir código.
- Proyecto pensado como ejemplo educativo y accesible.

## 🖥️ Funcionalidades

- **Abrir archivo:** `Ctrl + O`
- **Guardar archivo:** `Ctrl + S`
- **Guardar como:** `Ctrl + Shift + S`
- **Salir del editor:** `Ctrl + Q`

Además:
- Barra de estado que muestra nombre de archivo, línea y columna.
- Reemplazo automático de comillas tipográficas por comillas rectas.
- Fondo oscuro con texto claro, estilo terminal.
- Soporte de tabulación en el área de texto.

## 📦 Requisitos

- Python 3.10 o superior
- wxPython (instalar con `pip install wxPython`)

## ▶️ Ejecución

Clona este repositorio y entra a la carpeta del proyecto:
```bash
git clone https://github.com/capbility/vimi.git
cd vimi
```

Ejecuta el editor con Python:

```bash
python src/vimi/editor.py
```

En macOS, si usas entornos gráficos, puede que necesites:
```bash
pythonw src/vimi/editor.py
```

