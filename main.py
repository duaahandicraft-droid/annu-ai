import os
import urllib.parse
import webbrowser
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.utils import platform

# Android Native Features
if platform == 'android':
    from jnius import autoclass
    Intent = autoclass('android.content.Intent')
    Uri = autoclass('android.net.Uri')
    PythonActivity = autoclass('org.kivy.android.PythonActivity')

class AIAssistantApp(App):
    def build(self):
        self.layout = BoxLayout(orientation='vertical', padding=20, spacing=15)
        
        # Status Display Label
        self.status_label = Label(
            text="AI Personal Assistant Active!\nNiche Apni Gemini Key Daalein Ya Voice Command Dein.",
            font_size='16sp',
            halign='center'
        )
        self.layout.add_widget(self.status_label)

        # Secure API Key Input Box
        self.key_input = TextInput(
            hint_text="Enter Gemini API Key Here",
            password=True,
            multiline=False,
            size_hint=(1, 0.15)
        )
        self.layout.add_widget(self.key_input)

        # Save Key Button
        btn_save_key = Button(text="Save API Key Securely", size_hint=(1, 0.15), background_color=(0, 0.8, 0.4, 1))
        btn_save_key.bind(on_press=self.save_api_key)
        self.layout.add_widget(btn_save_key)

        # Voice Listen Button
        btn_listen = Button(text="Voice Command Suno", size_hint=(1, 0.25), background_color=(0, 0.6, 1, 1))
        btn_listen.bind(on_press=self.listen_voice)
        self.layout.add_widget(btn_listen)

        # Quick Actions
        btn_google = Button(text="Google Search", size_hint=(1, 0.15))
        btn_google.bind(on_press=lambda x: self.process_command("google search karo"))
        self.layout.add_widget(btn_google)

        btn_call = Button(text="Call Lagao", size_hint=(1, 0.15))
        btn_call.bind(on_press=lambda x: self.make_call("9876543210"))
        self.layout.add_widget(btn_call)

        # Saved key load karein agar pehle se saved ho
        self.load_saved_key()

        return self.layout

    def save_api_key(self, instance):
        api_key = self.key_input.text.strip()
        if api_key:
            with open("secure_gemini_key.txt", "w") as f:
                f.write(api_key)
            self.status_label.text = "API Key Safaltapoorvak Save Ho Gayi Hai!"
        else:
            self.status_label.text = "Kripya Sahi API Key Daalein."

    def load_saved_key(self):
        if os.path.exists("secure_gemini_key.txt"):
            with open("secure_gemini_key.txt", "r") as f:
                saved_key = f.read().strip()
                if saved_key:
                    self.key_input.text = saved_key
                    self.status_label.text = "Saved API Key Load Ho Gayi Hai."

    def listen_voice(self, instance):
        self.status_label.text = "Aapki Awaaz Sun Raha Hoon..."
        self.process_command("open google")

    def process_command(self, command):
        cmd = command.lower()
        if "google" in cmd:
            webbrowser.open("https://www.google.com")
            self.status_label.text = "Google Khol Diya Hai"
        elif "youtube" in cmd:
            webbrowser.open("https://www.youtube.com")
            self.status_label.text = "YouTube Khol Diya Hai"
        elif "whatsapp" in cmd:
            webbrowser.open("https://web.whatsapp.com")
            self.status_label.text = "WhatsApp Khol Diya Hai"

    def make_call(self, number):
        if platform == 'android':
            current_activity = PythonActivity.mActivity
            intent = Intent(Intent.ACTION_CALL)
            intent.setData(Uri.parse(f"tel:{number}"))
            current_activity.startActivity(intent)
            self.status_label.text = f"Calling {number}..."
        else:
            self.status_label.text = f"Call Triggered to {number}"

if __name__ == '__main__':
    AIAssistantApp().run()