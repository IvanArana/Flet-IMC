import flet 
from flet import(
    UserControl,
    Text,
    Container,
    colors,
    TextField,
    Column,
    Row,
    ElevatedButton
)

class IMCapp(UserControl):

    def build(self):
        self.name = TextField(label="Nombre", expand=1)
        self.lastname = TextField(label="Apellidos", expand=1)
        self.age = TextField(label="Edad", expand=1)
        self.weightUsr = TextField(label="Peso", expand=2)
        self.heightUsr = TextField(label="Altura", expand=2)
        self.result = Text()
        self.IMC = Column()

        return  Container(
            #bgcolor= colors.LIGHT_GREEN_50,
            content= Column(
                controls=[
                    Row(
                        controls=[
                            # TextField(label="Nombre", expand=1, bgcolor= colors.BLACK),
                            # TextField(label="Apellidos", expand=1, bgcolor= colors.BLACK),
                            # TextField(label="Edad", expand=1, bgcolor= colors.BLACK)
                            self.name,
                            self.lastname,
                            self.age
                        ]
                    ),
                    Row(
                        controls=[
                            # TextField(label="Peso", expand=2, bgcolor= colors.BLACK),
                            # TextField(label="Altura", expand=2, bgcolor= colors.BLACK)
                            self.weightUsr,
                            self.heightUsr
                        ]
                    ),
                    Row(
                        controls=[
                            ElevatedButton( #boton de calcular
                                text="Calcular IMC",
                                bgcolor=colors.DEEP_PURPLE_300,
                                color=colors.BLACK,
                                expand= 2,
                                on_click= self.add_IMC
                            )
                        ]
                    ),
                    self.IMC
                ]
            )
        )
    def add_IMC(self, e):
        imc = IMCapp(self.name.value, self.lastname.value, self.age.value, self.weightUsr.value, self.heightUsr.value, self.result)
    
    def calc_IMC(self, e):
        self.result = float(self.weightUsr) / (float(self.heightUsr) **2)
    
    def IMC_val(self, e):
        if self.result < 18.5:
            print("Tienes un bajo peso.")
        elif 18.5 <= self.result < 24.9:
            print("Tienes un peso saludable.")
        elif 25 <= self.result < 29.9:
            print("Tienes sobrepeso.")
        elif 30 <= self.result < 30:
            print("Tienes obesidad.")
        else:
            print("Tienes obesidad extrema.")

def main(page: flet.Page):

    IMC = IMCapp()

    page.add(IMC)


flet.app(main)


#imc = peso / (altura ** 2)