import os
import sys
import subprocess
from gtts import gTTS
from optparse import OptionParser

try:
    Parser = OptionParser()
    # Bu kısımda 'Parser' olşturarak bu parserın option özelliklerini kullanıyorum
    # bu sayede parametreler oluşturup kullanabiliyorum
    Parser.add_option("-d", dest="data", help="mesajı parametre olarak giriniz")
    Parser.add_option("-n", dest="name", help="mp3 dosyasının ismi")
    (user_input, arguments) = Parser.parse_args()

    data = user_input.data
    name = user_input.name

except KeyboardInterrupt:
    print("pressed 'CTRL + C'")
    sys.exit()

except Exception as E:
    print()

# Eğer ki işletim sistemi windows ise Documents klasörüne giderek bir ses klasörü
# oluşturuyorum ve tüm eklemeri orada gerçekleştiriyorum.
if os.name == 'nt':
    subprocess.call(["cd Documents"])
    subprocess.call(["mkdir voice_file"])
    speech = gTTS(text=str(data), lang='tr')
    speech.save(name + ".mp3")

# Eğer ki işletim sistemi Linux yada MAC OS ise Documents klasörüne giderek bir ses klasörü
    # oluşturuyorum ve tüm eklemeri orada gerçekleştiriyorum.
elif os.name == "posix":
    subprocess.call(["cd Documents"])
    subprocess.call(["mkdir voice_file"])
    speech = gTTS(text=str(data), lang='tr')
    speech.save(name + ".mp3")