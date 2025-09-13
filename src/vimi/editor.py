import wx
import os


class VimiEditor(wx.Frame):
    """Vimi: editor de texto accesible y simple, creado con wxPython."""

    def __init__(self):
        super().__init__(None, title="VIMI", size=(700, 500))
        self.current_file = None
        self._create_menu()
        self._create_text_area()
        self.text.SetFocus()
        self._create_status_bar()
        self.Show()

    # ---------- UI setup ----------

    def _create_menu(self):
        menubar = wx.MenuBar()
        file_menu = wx.Menu()

        open_item = file_menu.Append(wx.ID_OPEN, "&Abrir\tCtrl+O")
        save_item = file_menu.Append(wx.ID_SAVE, "&Guardar\tCtrl+S")
        save_as_item = file_menu.Append(wx.ID_SAVEAS, "Guardar &como...\tCtrl+Shift+S")
        file_menu.AppendSeparator()
        exit_item = file_menu.Append(wx.ID_EXIT, "&Salir\tCtrl+Q")

        menubar.Append(file_menu, "&Archivo")
        self.SetMenuBar(menubar)

        self.Bind(wx.EVT_MENU, self.on_open, open_item)
        self.Bind(wx.EVT_MENU, self.on_save, save_item)
        self.Bind(wx.EVT_MENU, self.on_save_as, save_as_item)
        self.Bind(wx.EVT_MENU, self.on_exit, exit_item)

    def _create_text_area(self):
        self.text = wx.TextCtrl(
            self,
            style=wx.TE_MULTILINE | wx.TE_RICH2 | wx.TE_PROCESS_TAB | wx.HSCROLL,
        )

        font = wx.Font(
            18,
            wx.FONTFAMILY_MODERN,
            wx.FONTSTYLE_NORMAL,
            wx.FONTWEIGHT_NORMAL,
            False,
            "SF Mono",
        )
        self.text.SetFont(font)
        self.text.SetBackgroundColour(wx.Colour(30, 30, 30))
        self.text.SetForegroundColour(wx.Colour(220, 220, 220))

        try:
            caret = wx.Caret(self.text, (2, self.text.GetCharHeight()))
            self.text.SetCaret(caret)
            if self.text.GetCaret():
                self.text.GetCaret().Show()
        except Exception:
            pass

        self.text.Bind(wx.EVT_TEXT, self.on_text_change)
        self.text.Bind(wx.EVT_KEY_DOWN, self.on_key_down)
        self.text.Bind(wx.EVT_KEY_UP, self.on_key_up)

    def _create_status_bar(self):
        self.statusbar = self.CreateStatusBar()
        self.update_status("Nuevo archivo")

    # ---------- Eventos ----------

    def on_text_change(self, event):
        """Reemplaza comillas tipográficas por comillas rectas."""
        content = self.text.GetValue()
        fixed = (
            content.replace("“", '"')
            .replace("”", '"')
            .replace("‘", "'")
            .replace("’", "'")
        )
        if content != fixed:
            pos = self.text.GetInsertionPoint()
            self.text.ChangeValue(fixed)
            self.text.SetInsertionPoint(min(pos, len(fixed)))
        event.Skip()

    def on_key_down(self, event):
        """Inserta tabulación en lugar de perder el foco."""
        if event.GetKeyCode() == wx.WXK_TAB:
            self.text.WriteText("\t")
        else:
            event.Skip()

    def on_open(self, event):
        """Abre un archivo de texto."""
        with wx.FileDialog(
            self,
            "Abrir archivo",
            wildcard="Archivos de texto (*.txt;*.py)|*.txt;*.py|Todos los archivos|*.*",
            style=wx.FD_OPEN | wx.FD_FILE_MUST_EXIST,
        ) as dialog:
            if dialog.ShowModal() == wx.ID_OK:
                path = dialog.GetPath()
                try:
                    with open(path, "r", encoding="utf-8") as f:
                        self.text.SetValue(f.read())
                    self.current_file = path
                    self.SetTitle(f"VIMI — {os.path.basename(path)}")
                    self.update_status(path)
                except Exception as e:
                    wx.MessageBox(
                        f"No se pudo abrir el archivo:\n{e}",
                        "Error",
                        wx.ICON_ERROR,
                    )

    def on_save(self, event):
        """Guarda el archivo actual o abre 'Guardar como'."""
        if self.current_file:
            try:
                with open(self.current_file, "w", encoding="utf-8") as f:
                    f.write(self.text.GetValue())
                self.update_status(f"Guardado: {self.current_file}")
            except Exception as e:
                wx.MessageBox(
                    f"No se pudo guardar el archivo:\n{e}",
                    "Error",
                    wx.ICON_ERROR,
                )
        else:
            self.on_save_as(event)

    def on_save_as(self, event):
        """Guarda el contenido en un nuevo archivo."""
        with wx.FileDialog(
            self,
            "Guardar archivo como",
            wildcard="Archivos de texto (*.txt;*.py)|*.txt;*.py|Todos los archivos|*.*",
            style=wx.FD_SAVE | wx.FD_OVERWRITE_PROMPT,
        ) as dialog:
            if dialog.ShowModal() == wx.ID_OK:
                path = dialog.GetPath()
                try:
                    with open(path, "w", encoding="utf-8") as f:
                        f.write(self.text.GetValue())
                    self.current_file = path
                    self.SetTitle(f"VIMI — {os.path.basename(path)}")
                    self.update_status(path)
                except Exception as e:
                    wx.MessageBox(
                        f"No se pudo guardar el archivo:\n{e}",
                        "Error",
                        wx.ICON_ERROR,
                    )

    def on_exit(self, event):
        """Cierra la aplicación."""
        self.Close()

    def on_key_up(self, event):
        """Actualiza línea y columna en la barra de estado."""
        pos = self.text.GetInsertionPoint()
        try:
            coords = self.text.PositionToXY(pos)
            if coords and coords[0] != -1 and coords[1] != -1:
                x, y = coords[:2]
                filename = (
                    os.path.basename(self.current_file)
                    if self.current_file
                    else "Sin título"
                )
                self.statusbar.SetStatusText(f"{filename} — Línea: {y+1}, Col: {x+1}")
        except Exception:
            pass
        event.Skip()

    # ---------- Utilidad ----------

    def update_status(self, message):
        """Actualiza el texto de la barra de estado."""
        self.statusbar.SetStatusText(message)


if __name__ == "__main__":
    app = wx.App()
    VimiEditor()
    app.MainLoop()
