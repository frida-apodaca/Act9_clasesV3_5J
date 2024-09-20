print("act 9  clases v2")
print("frida apodaca Mat:22308051281136")
# zona de class
class Operadores1136:
    # zona de funiones
    def suma1136(self,F,A):
        s1136=F+A
        print(f"la suma de {F} + {A} = {s1136}")
        print("\n")
    def resta1136(self,F,A):
        s1136=F-A
        print(f"la resta de {F} - {A} = {s1136}")
        print("\n")
    def multi1136(self,F,A):
        s1136=F*A
        print(f"la multiplicacion de {F} * {A} = {s1136}")
        print("\n")
    def div1136(self,F,A):
        s1136=F/A
        print(f"la division de {F} / {A} = {s1136}")
        print("\n")
    def pote1136(self,F,A):
        s1136=F%A
        print(f"la modulo de {F} % {A} = {s1136}")
        print("\n")
    def expo1136(self,F,A):
        s1136=F**A
        print(f"la exponente de {F} ** {A} = {s1136}")
        print("\n")
    def cos1136(self,F,A):
        s1136=F/A
        print(f"la cociente de {F} // {A} = {s1136}")
        print("\n")
        
# zona de creacion del objeto
operafrida=Operadores1136()

# zona de uso de objetos
print(" Funcion suma")
operafrida.suma1136(5,4)

print(" Funcion resta")
operafrida.resta1136(9,3)

print(" Funcion multiplicacion")
operafrida.multi1136(6,9)

print(" Funcion division")
operafrida.div1136(10,4)

print(" Funcion modulo")
operafrida.pote1136(43,23)

print(" Funcion exponente")
operafrida.expo1136(14,9)

print(" Funcion cociente")
operafrida.cos1136(3,2)
