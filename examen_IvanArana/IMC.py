import flet as ft
from flet import(
    FontWeight
)

def main(page: ft.Page):
    def add_clicked(e):
        # Obtener los valores de los campos de texto
        nombre = new_name.value
        apellidos = new_last.value
        edad = int(new_age.value)
        peso = float(new_usrWeight.value)
        altura = float(new_usrHeight.value)
        imc = peso / (altura **2)

        if imc < 18.5:
            imc_msg="Tienes un bajo peso."
            imc_advice="Recomendamos consultar a un profesional de la salud para evaluar su situación."
        elif 18.5 <= imc < 24.9:
            imc_msg="Tienes un peso saludable."
            imc_advice="¡Sigue manteniendo un estilo de vida saludable!"
        elif 25 <= imc < 29.9:
            imc_msg="Tienes sobrepeso."
            imc_advice="Consultar con un profesional de la salud puede ser beneficioso."
        elif 30 <= imc < 34.9:
            imc_msg="Tienes obesidad."
            imc_advice="Consultar con un médico o un dietista puede ser esencial para establecer un plan de acción."
        else:
            imc_msg="Tienes obesidad extrema."
            imc_advice="F en el chat"


        
        # Concatenar los valores en una sola cadena
        datos = f"Nombre: {nombre}, Apellidos: {apellidos}, Edad: {edad}, Peso: {peso}, Altura: {altura}, IMC: {imc}, Tipo: {imc_msg}, Recomendacion: {imc_advice}"

        # Mostrar los datos en un solo checkbox
        imc_view.controls.append(ft.Checkbox(label=datos))

        # Limpiar los campos de texto
        new_name.value = ""
        new_last.value = ""
        new_age.value = ""
        new_usrWeight.value = ""
        new_usrHeight.value = ""
        view.update()

    new_name = ft.TextField(label="nombre", expand=True)
    new_last = ft.TextField(label="apellidos", expand=True)
    new_age = ft.TextField(label="edad", expand=True)
    new_usrWeight = ft.TextField(label="peso", expand=True)
    new_usrHeight = ft.TextField(label="altura", expand=True)

    imc_view = ft.Column()

    view = ft.Column(
        controls=[
            ft.Row(
                controls=[
                    new_name,
                    new_last,
                    new_age
                ]
            ),
            ft.Row(
                controls=[
                    new_usrWeight,
                    new_usrHeight,
                ]
            ),
            ft.Row(
                controls=[
                    ft.FloatingActionButton(icon=ft.icons.BAR_CHART, text="Calcular", on_click=add_clicked),
                ]
            ),
            imc_view
        ]
    )

    page.window_width = 600

    page.add(
        ft.Text(value="Bienvenido al IMSS - IMC Calculator", size=30, italic=True, weight=FontWeight.BOLD),
        view
        )

ft.app(target=main)
