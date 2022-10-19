import speech_recognition as sr

rec = sr.Recognizer()

# para escolher qual microfone usar:
# print(sr.Microphone().list_microphone_names())
with sr.Microphone(device_index=3) as microfone:
    rec.adjust_for_ambient_noise(microfone)
    print("Pode começar a falar:")

    # rec.pause_threshold = 1 # coloque isso se quiser que ele demore mais para entender que uma pausa é o fim do audio

    audio = rec.listen(microfone)
try:
    # reconhece audio e traduz ele pra texto
    texto = rec.recognize_google(audio, language="pt-BR")
    print(texto)
except:
    print("Não peguei áudio nenhum")