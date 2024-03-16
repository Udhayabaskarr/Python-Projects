from translate import Translator
a=input("Enter text to translate : ")
t=Translator(to_lang="")
b=t.translate(a)
print(b)