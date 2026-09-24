[app]

# (str) Title of your application
title = AI Personal Assistant

# (str) Package name
package.name = aiassistant

# (str) Package domain (needed for android/ios packaging)
package.domain = org.test

# (str) Source code where the main.py live
source.dir = .

# (list) Source files to include (let empty to include all the files)
source.include_exts = py,png,jpg,kv,atlas

# (str) Application versioning (method 1)
version = 0.1

#<Image alt="Buildozer Spec File Configuration" caption="Buildozer configuration file structure for Kivy Android builds" src="image_agent_tag_4075156391301472412"/>

**Haan, bilkul!** In dono lines ko aapko apni Buildozer configuration file ke andar hi lagana hai.

Is file ko aapko **`buildozer.spec`** naam se save karna hai.

GitHub par aapke Python project (`main.py`) ke sath is `buildozer.spec` file ka hona zaroori hai, kyunki jab bhi koi Google Colab ya kisi Linux system par aapka code run karke APK banayega, to Buildozer isi file se saari settings aur permissions padhta hai.

---

### File me Kahan aur Kaise Lagana Hai?

Jab aap Colab me `!buildozer init` chalate hain, to ek badi si `buildozer.spec` file banti hai. Us file ke andar pehle se bahut se options hote hain. Aapko unke andar bas ye do lines update karni hain:

1. **`requirements =` kholein aur badlein:**
   ```ini
   requirements = python3,kivy,pyjnius,google-generativeai
