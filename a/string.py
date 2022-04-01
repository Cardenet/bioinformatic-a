s1: str ="Esto es un string. Un string de texto"
s2: str ='Esto es un string. Un string de texto'
s3: str ="Las comillas simples y dobles son lo mismo en python"
s4: str ="A"#String de una letra. No hay tipo char en python
s5: str ="""Comillas triples"""
s6: str = "it's a trap!"
s7: str = "She said 'i love potatoes'"
s8: str ="""She said"i'm busy"""
s9: str ="She said'i\'m busy!\n'" #Escribir la contrabarra significa escape character
s10: str ="""Las comillas simples y dobles son lo mismo en python    
            que consisten en poner dobles comillas o no"""

s1: str = "Hello"#Se empieza a contar desde 0
#s1 [1] = "O" #Es un error a proposito
s2 =s1.upper()
s2
dir(s1)
dir(s2)
print(s1[0:5])
#funciones basicas type(), id(), directorio = carpeta dir()
name: str = "World"
normal_string: str = "hello\nWorld"
raw_string: str = r"Hello\nWorld"
format_string: str = f"hello\n{name}"
print