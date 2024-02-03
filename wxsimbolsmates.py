import wx
import matplotlib.pyplot as plt
from io import BytesIO
from PIL import Image

plt.rcParams['text.usetex'] = True
plt.rcParams['text.latex.preamble'] = r'\usepackage{amsmath}'

class AplicacioQuiz(wx.App):
    def OnInit(self):
        marc = MarcQuiz(None, title="Problema 1")
        marc.Show()
        return True

class MarcQuiz(wx.Frame):
    def __init__(self, pare, title):
        super(MarcQuiz, self).__init__(pare, title=title, size=(800, 600))
        self.panell = wx.Panel(self)
        self.pregunta_actual = 0
        self.puntuacio = 0
        self.inicialitza_ui()

    def inicialitza_ui(self):
        self.vbox = wx.BoxSizer(wx.VERTICAL)

        # Defineix aquí les teves preguntes i respostes
        self.preguntes = [
            "En el procés de fabricació d’un producte, s’estableixen quatre punts de control de qualitat, un dels quals és al final del procés, en què es retiren les peces defectuoses. D’un lot inicial de 800 peces, la taxa mitjana de rebuig de cada punt de control és 6, 15, 17\n i 10, respectivament. La taxa de qualitat global expressada en percentatge de peces obtingudes sense defectes és del:",
            "En un circuit elèctric, es connecten en paral·lel dues resistències de valors nominals 110Ω i 330Ω amb tolerància ± 2 %. Quin valor té la resistència equivalent?",
            "La llum que produeix una bombeta de baix consum de 8 W equival, segons el fabricant, a la que fa una bombeta incandescent de 40 W. Si en una sala hi ha cinc bombetes de 40 W i se substitueixen per bombetes de baix consum de 8 W, quin estalvi\n energètic suposarà el canvi al cap de 100 hores de funcionament?",
            "El nitinol, un aliatge amb memòria de forma que s’utilitza en aplicacions sanitàries, està compost per un 54,5 % de níquel (Ni) i un 45,4 % de titani (Ti). Quina quantitat d’aquests dos components, en kg, hi ha en 150 kg de nitinol?",
            "En l’ajust 110N7/h6, la tolerància N7 del forat és (matriu 1) μm i la tolerància h6 de l’eix és (matriu 2) μm. Determineu-ne el joc màxim."
            # ... (afegeix les altres preguntes)
        ]
        self.respostes = [
            ["95,20 %.", "99,25 %.", "98,75 %.", "94,00 %."],
            ["(440 ± 2 %)Ω", "(440 ± 4 %)Ω", "(82,5 ± 4 %)Ω", "(82,5 ± 2 %)Ω"],
            ["3,2 kW h", "160 kW h", "32 kW h", "16 kW h"],
            ["Ni: 83.10  Ti: 66.75", "Ni: 54.5   Ti: 45.4", "Ni: 81.75  Ti: 68.10", "Ni: 82.60  Ti: 69.25"],
            ["26μm", "19μm", "10μm", "9μm"]
            # ... (afegeix les opcions de resposta per a les altres preguntes)
        ]
        self.respostes_correctes = ['D', 'D', 'D', 'C', 'D'] # ... (ajusta això segons les teves respostes correctes)

        # Crea i mostra la primera pregunta i els seus botons de resposta
        self.mostra_pregunta()

        self.panell.SetSizer(self.vbox)

    def mostra_pregunta(self):
        # Esborra els widgets existents si aquesta no és la primera pregunta
        if self.pregunta_actual != 0:
            self.panell.DestroyChildren()

        # Utilitza un "box sizer" horitzontal per mantenir el text i la imatge de la matriu costat a costat
        hbox = wx.BoxSizer(wx.HORIZONTAL)

        # Comprova si la pregunta conté "(matriu 1)"
        if "(matriu 1)" in self.preguntes[self.pregunta_actual]:
            parts_pregunta = self.preguntes[self.pregunta_actual].split("(matriu 1)")
            text_abans_pregunta = wx.StaticText(self.panell, label=parts_pregunta[0])
            hbox.Add(text_abans_pregunta, flag=wx.ALIGN_CENTER_VERTICAL)

            # Genera la imatge de la matriu i afegeix-la a la interfície d'usuari
            imatge_widget = self.genera_imatge_matriu(r'\begin{bmatrix}-10\\-45\end{bmatrix}')
            hbox.Add(imatge_widget, flag=wx.ALIGN_CENTER_VERTICAL)

            text_despres_pregunta = wx.StaticText(self.panell, label=parts_pregunta[1])
            hbox.Add(text_despres_pregunta, flag=wx.ALIGN_CENTER_VERTICAL)
        else:
            # Si no hi ha cap matriu, simplement mostra el text de la pregunta
            text_pregunta = wx.StaticText(self.panell, label=self.preguntes[self.pregunta_actual])
            hbox.Add(text_pregunta, flag=wx.ALIGN_CENTER_VERTICAL)

        # Afegeix el "box sizer" horitzontal al "box sizer" vertical
        self.vbox.Add(hbox, flag=wx.EXPAND | wx.ALL, border=10)

        if "matriu 2" in self.preguntes[self.pregunta_actual]:
            # Suposant que tens una imatge 'matriz2.png' al directori actual per a la segona matriu
            fitxer_imatge2 = 'matriz_2.png'
            bitmap_imatge2 = wx.Bitmap(fitxer_imatge2, wx.BITMAP_TYPE_ANY)
            imatge_widget2 = wx.StaticBitmap(self.panell, wx.ID_ANY, bitmap_imatge2)
            self.vbox.Add(imatge_widget2, flag=wx.ALIGN_CENTER | wx.ALL, border=10)

        # Mostra els botons de resposta
        for resposta in self.respostes[self.pregunta_actual]:
            boto_resposta = wx.Button(self.panell, label=resposta)
            boto_resposta.Bind(wx.EVT_BUTTON, self.on_resposta)
            self.vbox.Add(boto_resposta, flag=wx.EXPAND|wx.ALL, border=5)

        # Disposa els widgets
        self.panell.Layout()

    def genera_imatge_matriu(self, latex_str):
        # Configura Matplotlib per a l'ús de LaTeX
        plt.rc('text', usetex=True)
        plt.rc('font', family='serif')
        plt.rc('font', size=12)  # Ajusta la mida de la font si és necessari

        # Crea una figura Matplotlib
        fig = plt.figure(figsize=(1, 0.4))
        ax = fig.add_subplot(111)
        ax.axis('off')
        ax.text(0.5, 0.5, f'${latex_str}$', fontsize=12, ha='center', va='center')

        # Guarda la figura en un buffer de bytes en comptes d'un fitxer
        buffer = BytesIO()
        plt.savefig(buffer, format='png', bbox_inches='tight', pad_inches=0)
        plt.close(fig)

        # Usa Pillow per obrir la imatge i retallar l'espai extra
        buffer.seek(0)
        imatge = Image.open(buffer)
        imatge.load()  # Necessari per accedir als píxels de la imatge

        # Troba els límits de la matriu i retalla l'espai extra
        bbox = imatge.getbbox()
        if bbox:
            imatge = imatge.crop(bbox)

        # Guarda la imatge retallada en un altre buffer
        buffer = BytesIO()
        imatge.save(buffer, format='png')

        # Carrega la imatge des del buffer
        buffer.seek(0)
        imatge_wx = wx.Image(buffer, wx.BITMAP_TYPE_PNG)
        bitmap_imatge = wx.Bitmap(imatge_wx)

        # Crea un widget d'imatge i el retorna
        imatge_widget = wx.StaticBitmap(self.panell, wx.ID_ANY, bitmap_imatge)
        return imatge_widget

    def on_resposta(self, event):
        # Obté l'etiqueta del botó que s'ha clicat
        resposta_usuari = event.GetEventObject().GetLabel()

        # Converteix la cadena de resposta correcta en un índex
        index_resposta_correcta = ord(self.respostes_correctes[self.pregunta_actual]) - ord('A')

        # Comprova si la resposta és correcta
        if resposta_usuari == self.respostes[self.pregunta_actual][index_resposta_correcta]:
            self.puntuacio += 0.5
            wx.MessageBox("Correcte!", "Informació", wx.OK | wx.ICON_INFORMATION)
        else:
            resposta_correcta = self.respostes[self.pregunta_actual][index_resposta_correcta]
            self.puntuacio -= 0.16
            wx.MessageBox(f"Incorrecte. La resposta correcta era: {resposta_correcta}", "Informació", wx.OK | wx.ICON_INFORMATION)

        # Passa a la següent pregunta o finalitza el qüestionari
        self.pregunta_actual += 1
        if self.pregunta_actual < len(self.preguntes):
            self.mostra_pregunta()
        else:
            puntuacio_arrodonida = round(self.puntuacio, 2)
            wx.MessageBox(f"Exercici finalitzat, la puntuació total és de: {puntuacio_arrodonida}", "Informació",
                          wx.OK | wx.ICON_INFORMATION)
            self.Close()

if __name__ == "__main__":
    aplicacio = AplicacioQuiz()
    aplicacio.MainLoop()
