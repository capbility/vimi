# Vimi

**Vimi** es un editor simple de código en **Python con wxPython**, creado como recurso educativo accesible.  
A diferencia de Visual Studio Code y otros editores modernos, que pueden resultar complicados cuando estamos aprendiendo nuestro primer lenguaje de programación —y aún más si utilizamos lectores de pantalla—, **Vimi** busca ser ligero, claro y fácil de usar.  

El nombre es un homenaje a [Vim](https://www.vim.org/), uno de los editores más influyentes.

## 🚀 Características

- Interfaz gráfica hecha con [wxPython](https://wxpython.org/).
- Área de edición básica para escribir código.
- Proyecto pensado como ejemplo educativo y accesible.

## 🖥️ Funcionalidades Windows

- **Abrir archivo:** `Ctrl + O`
- **Guardar archivo:** `Ctrl + S`
- **Guardar como:** `Ctrl + Shift + S`
- **Salir del editor:** `Ctrl + Q`

## 🖥️ Funcionalidades macOS

- **Abrir archivo:** `Cmd + O`
- **Guardar archivo:** `Cmd + S`
- **Guardar como:** `Cmd + Shift + S`
- **Salir del editor:** `Cmd + Q`

Además:
- Barra de estado que muestra nombre de archivo, línea y columna.
- Reemplazo automático de comillas tipográficas por comillas rectas.
- Fondo oscuro con texto claro, estilo terminal.
- Soporte de tabulación en el área de texto.

## 📦 Requisitos

- Python 3.10 o superior
- wxPython (instalar con `pip install wxPython`)

## ▶️ Ejecutables

Puedes descargar los ejecutables ya generados para macOS y Windows en la [Carpeta Google Drive que guarda los ejecutables](https://drive.google.com/drive/u/3/folders/1-YwTCKG676GAfdYKFI4YRLWgCJ_ye4sA)
- macOS: descarga el archivo Vimi.app.zip, descomprime y ejecútalo directamente. 
- Windows: descarga el archivo Vimi.exe y ejecútalo directamente.

## ▶️ Probar el código

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

