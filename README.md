# 🤖 Android Personal AI Assistant

App AI Assistant amin'ny teny Python ampiasana **Kivy, Pyjnius, ary Gemini API**. Afaka mampiasa feo (voice commands) sy bokotra ianao mba hikirakirana ny finday ary azo antoka tsara ny API key.

---

## ✨ Anjara Asa (Features)

- 🔍 **Google Search:** Fikarohana amin'ny Google amin'ny feo na bokotra.
- 📞 **Antso Zotram-pifandraisana:** Manao antso mivantana amin'ny alalan'ny Android System.
- 💬 **WhatsApp Automation:** Mandefa hafatra amin'ny WhatsApp.
- 🔒 **Fiarovana ny API Key:** Ampidirina ao anatin'ny App aorian'ny installation ny Gemini API Key mba ho voaaro.

---

## 🛠️ Rakitra ao amin'ny Tetikasa (Project Files)

- `main.py`: Kiti-kera Python ho an'ny UI Kivy sy ny Android native intents.
- `buildozer.spec`: Rakitra ho an'ny configuration rehefa hamboarina ho APK ny tetikasa.
- `README.md`: Torolalana sy fanazavana momba ny tetikasa.

---

## 📦 Zo ilaina amin'ny Android (Permissions)

- `INTERNET`
- `CALL_PHONE`
- `RECORD_AUDIO`
- `READ_CONTACTS`

---

## 🚀 Fomba Fanamboarana ny APK (Google Colab)

1. Ampidiro ao amin'ny Google Colab ny `main.py` sy ny `buildozer.spec`.
2. Alefaso ny baiko fampidirana Buildozer:
   ```bash
   !pip install buildozer
