import globalPluginHandler
from scriptHandler import script
import ui
import gui
import wx
class GlobalPlugin(globalPluginHandler.GlobalPlugin):
    @script(description="Abre el cuadro de edición de textDrop", gesture="kb:NVDA+0")
    def script_ejecutar_textdrop(self, gesture):
        def abrir_ventana():
            ventana = VentanaTextDrop(gui.mainFrame)
            gui.mainFrame.prePopup()
            ventana.ShowModal()
            gui.mainFrame.postPopup()
            ventana.Destroy()
        wx.CallAfter(abrir_ventana)

# creo la clase para inicializar la ventana de text drop para escribir
class VentanaTextDrop(wx.Dialog):
    def __init__(self, parent):
        super().__init__(parent, title="Text drop")
        self.campoTexto = wx.TextCtrl(self, style=wx.TE_MULTILINE)
        self.etiquetaConteo = wx.TextCtrl(self, style=wx.TE_READONLY | wx.TE_MULTILINE, value="0 caracteres")
        self.campoTexto.Bind(wx.EVT_TEXT, self.al_cambiar_texto)
        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(self.campoTexto, proportion=1, flag=wx.EXPAND | wx.ALL, border=10)
        sizer.Add(self.etiquetaConteo, flag=wx.ALL, border=10)
        self.botonGuardar = wx.Button(self, label="Guardar")
        self.botonCancelar = wx.Button(self, label="Cancelar")
        sizerBotones = wx.BoxSizer(wx.HORIZONTAL)
        sizerBotones.Add(self.botonGuardar, flag=wx.ALL, border=10)
        sizerBotones.Add(self.botonCancelar, flag=wx.ALL, border=10)
        sizer.Add(sizerBotones, flag=wx.ALIGN_CENTER)
        self.botonCancelar.Bind(wx.EVT_BUTTON, self.al_cancelar)
        self.botonGuardar.Bind(wx.EVT_BUTTON, self.al_guardar)
        self.SetSizer(sizer)
    def al_cambiar_texto(self, event):
        cantidad = len(self.campoTexto.GetValue())
        self.etiquetaConteo.SetValue(f"{cantidad} caracteres")
    def al_cancelar(self, event):
        self.EndModal(wx.ID_CANCEL)
    def al_guardar(self, event):
        dialogo = wx.FileDialog(self, message="Guardar documento", wildcard="Archivo de texto (*.txt) | *.txt", style=wx.FD_SAVE | wx.FD_OVERWRITE_PROMPT)
        if dialogo.ShowModal() == wx.ID_CANCEL:
            return
        ruta = dialogo.GetPath()
        with open(ruta, "w", encoding="utf-8") as archivo:
            archivo.write(self.campoTexto.GetValue())