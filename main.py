# import kivy
# from kivy.app import App
from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.uix.button import MDIconButton
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.window import Window
from kivymd.theming import ThemeManager
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDButton, MDButtonText
from kivymd.uix.dialog import MDDialog, MDDialogHeadlineText, MDDialogButtonContainer
from kivy.uix.widget import Widget

from kivy.factory import Factory

#####
from pprint import pprint
import re
from googleapiclient import discovery
from httplib2 import Http
from oauth2client.service_account import ServiceAccountCredentials

from form.get_form import get_token_form, call_forms_api as get_forms
from form.simplify_form import save_simplify_form as save_form
from user.register import register_user

class LoginScreen(Screen): # Login
    pass


class RegisterScreen(Screen): # Register
    def register(self):
        user = {
            'name': self.ids.input_nombre.text,
            'last_name': self.ids.input_apellido.text,
            'email': self.ids.input_email.text,
            'password': self.ids.input_password.text,
            'type': 'encuestador'
        }
        res = register_user(user)


class PrincipalScreen(Screen): # Main
    pass

class CrearScreen(Screen):
    dialog = None

    def dialog_text(self):
        if not self.dialog:
            MDDialog(
                MDDialogHeadlineText(
                    text="Discard draft?",
                    halign="left",
                ),
                MDDialogButtonContainer(
                    Widget(),
                    MDButton(                        
                        MDButtonText(text="Cancel"),
                        style="text",
                        on_press = self.close_dialog                    
                    ),
                    MDButton(
                        MDButtonText(text="Discard"),
                        style="text",
                        on_press = self.form  
                    ),
                    spacing="8dp",
                ),
            ).open()

    def close_dialog(self, obj):
        if self.dialog:
            self.dialog.dismiss()
        
    def form(self, obj):        
        ### FORM LOGIC
        token = get_token_form(self.ids.form_id.text)
        print(save_form(get_forms(token)))
        print(f"TESTING: {token}")
        # text = self.ids.token_form.text
        # text = self.ids.form_id.text
        # url = text
        # print(f"TEST: {url}")
        
        # pattern = r"/d/([a-zA-Z0-9_-]+)"
        # match = re.search(pattern, url) 

        # if match:
        #     form_id = match.group(1)
        #     print(form_id)
        # else:
        #     print("No match found.")

        # SCOPES = "https://www.googleapis.com/auth/forms.body"
        # DISCOVERY_DOC = "https://forms.googleapis.com/$discovery/rest?version=v1"

        # creds = ServiceAccountCredentials.from_json_keyfile_name(
        #     'credentials.json',
        #     SCOPES
        # )

        # http=creds.authorize(Http())
        # form_service = discovery.build(
        #     "forms",
        #     "v1",
        #     http=http,
        #     discoveryServiceUrl=DISCOVERY_DOC,
        #     static_discovery=False,
        # )

        # # # formId = "1GEsjWKisZGbfpLPsnhQ7Wdx6IdkU706cC6k3sNVClKw"
        # formId = form_id

        # # # Prints the result to show the question has been added
        # get_result = form_service.forms().get(formId=formId).execute()
        # pprint(get_result['items'])
        # print('\n')


class DescargarScreen(Screen):
    pass


class AplicarScreen(Screen):
    pass


class GenerarScreen(Screen):
    pass


class CerrarScreen(Screen):
    pass


class WindowManager(ScreenManager): # Transistion btw the windows
    pass


class UI(Factory.ScreenManager):
    Builder.load_file("layout.kv")

class Main(MDApp):
    title = 'Encuestas Digitales'

    def build(self):
        # self.root_widget = kv
                
        sm = ScreenManager()
        sm.add_widget(LoginScreen(name='login'))
        sm.add_widget(RegisterScreen(name='register'))
        sm.add_widget(PrincipalScreen(name='principal'))
        sm.add_widget(CrearScreen(name='crear'))
        sm.add_widget(DescargarScreen(name='descargar'))
        sm.add_widget(AplicarScreen(name='aplicar'))
        sm.add_widget(GenerarScreen(name='generar'))
        return UI()
        
    # def navigation_draw(self):
    #     print("navbar")
    

if __name__ == "__main__":
    Main().run()    