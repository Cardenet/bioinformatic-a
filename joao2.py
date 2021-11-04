from turtle import*
import turtle

speed(0)

#bigote
def bigote(x: int, y: int):
    fillcolor("black")
    begin_fill()
    penup()
    goto(x + 20, y +   0)
    goto(x + 20, y +  20)
    goto(x + 40, y +  20)
    goto(x + 40, y +   0)
    goto(x + 80, y +   0)
    goto(x + 80, y + -20)
    goto(x +  0, y + -20)
    goto(x +  0, y +   0)
    goto(x + 20, y +   0)
    end_fill()
#end bigote

#ojo
def ojo(x: int, y: int):
    
    fillcolor("black")
    begin_fill()
    penup()
    goto(x + 20, y +  20)
    goto(x + 20, y +  60)
    goto(x + 0, y +  60)
    goto(x + 0,  y + 20)
    goto(x + 20, y +  20)
    goto(x + 40, y +  20)
    goto(x + 40, y +  0)
    end_fill()
#end ojo
def nariz(x: int, y: int):
#nariz
    penup()
    fillcolor("pink")
    begin_fill()
    goto(x + 80, y +  0)
    goto(x + 100, y +  0)
    goto(x + 100, y +  20)
    goto(x + 80, y +  20)
    goto(x + 80, y +  40)
    goto(x + 40, y +  40)
    goto(x + 40, y +  60)
    goto(x + 20, y +  60)
    goto(x + 20, y +  20)
    goto(x + 40, y +  20)
    end_fill()
    goto(x + 20, y +  20)
    goto(x + 20, y +  60)
#nariz end
def pelo(x: int, y: int):
    penup()
    goto(x + -40, y +  60)

#pelo 1
    fillcolor("brown")
    begin_fill()
    penup()
    goto(x + -40, y +  40)
    goto(x + -60, y +  40)
    goto(x + -60, y +  20)
    goto(x + -40, y +  20)
    goto(x + -40, y +  0)
    goto(x + -80, y +  0)
    goto(x + -80, y +  40)
    goto(x + -100, y +  40)
    goto(x + -100, y +  60)
    goto(x + -40, y +  60)
    goto(x + -100, y +  60)
    end_fill()
 #end pelo 1
def oreja(x: int, y: int):
#oreja
    fillcolor("pink")
    begin_fill()
    penup()
    goto(x + -100, y +  40)
    goto(x + -100, y +  0)
    goto(x + -80, y +  0)
    goto(x + -80, y +  40)
    goto(x + -100, y +  40)
    goto(x + -100, y +  0)
    end_fill()
#end oreja
def pelo2(x: int, y: int):
#pelo 2
    penup()
    fillcolor("brown")
    begin_fill()
    goto(x + -80, y +  0)
    goto(x + -80, y +  -20)
    goto(x + -120, y +  -20)
    goto(x + -120, y +  40)
    goto(x + -100, y +  40)
    end_fill()
#end pelo 2
def cara(x: int, y: int):
    penup()
    goto(x + -100, y +  0)
    goto(x + -80, y +  0)
    goto(x + -80, y +  -20)

    #cara
    penup()
    fillcolor("pink")
    begin_fill()
    goto(x + -80, y +  -20)
    goto(x + -80, y +  -40)
    goto(x + 60, y +  -40)
    goto(x + 60, y +  -20)
    goto(x + 0, y +  -20)
    goto(x + 0, y +  0)
    goto(x + 20, y +  0)
    goto(x + 20, y +  20)
    goto(x + 0, y +  20)
    goto(x + 0, y + 60)
    goto(x + -40, y +  60)
    goto(x + -40, y +  40)
    goto(x + -60, y +  40)
    goto(x + -60, y +  20)
    goto(x + -40, y +  20)
    goto(x + -40, y +  0)
    goto(x + -80, y +  0)
    goto(x + -80, y + -20)
    end_fill()
    penup()
#end cara
def gorra(x: int, y: int):
    penup()
    goto(x + 80, y +  -20)

    pendown()

    goto(x + 80, y +  0)
    goto(x + 100, y +  0)
    goto(x + 100, y +  20)
    goto(x + 80, y +  20)
    goto(x + 80, y +  40)
    goto(x + 40, y +  40)
    goto(x + 40, y +  60)

#gorra
    penup()
    fillcolor("red")
    begin_fill()
    goto(x + 80, y +  60)
    goto(x + 80, y +  80)
    goto(x + 20, y +  80)
    goto(x + 20, y +  100)
    goto(x + -80, y +  100)
    goto(x + -80, y +  80)
    goto(x + -100, y +  80)
    goto(x + -100, y +  60)
    end_fill()
#gorra end
def brazo_izq(x: int, y: int):
    penup()
    goto(x + -100, y + 0)
    goto(x + -80, y + 0)
    goto(x + -80, y + -40)

#brazo izq
    fillcolor("red")
    begin_fill()
    penup()
    goto(x + -100, y + -40)
    goto(x + -100, y + -60)
    goto(x + -120, y + -60)
    goto(x + -120, y + -80)
    goto(x + -140, y + -80)
    goto(x + -140, y + -100)
    goto(x + -100, y + -100)
    goto(x + -100, y + -120)
    goto(x + -80, y + -120)
    goto(x + -80, y + -100)
    goto(x + -60, y + -100)
    goto(x + -60, y + -40)
    goto(x + -80, y + -40)
    goto(x + -60, y + -40)
    end_fill()
#end brazo izq
def brazo_der(x: int, y: int):
    
    penup()
    goto(x + -40, y + -40)
    goto(x + -40, y + -80)
    goto(x + 0, y + -80)
    goto(x + 0, y + -60)
    goto(x + 20, y + -60)
    goto(x + 20, y + -40)
    goto(x + 20, y + -60)
    goto(x + 20, y + -100)

#brazo der
    fillcolor("red")
    begin_fill()
    penup()
    goto(x + 20, y + -60)
    goto(x + 80, y + -60)
    goto(x + 80, y + -80)
    goto(x + 100, y + -80)
    goto(x + 100, y + -100)
    goto(x + 60, y + -100)
    goto(x + 60, y + -120)
    goto(x + 40, y + -120)
    goto(x + 40, y + -100)
    goto(x + 20, y + -100)
    end_fill()
#end brazo der
def mano_izq(x: int, y: int):
    penup()
    goto(x + 20, y + -60)
    goto(x + 0, y + -60)
    goto(x + 0, y + -80)
    goto(x + -40, y + -80)
    goto(x + -40, y + -40)
    goto(x + -60, y + -40)
    goto(x + -60, y + -100)
    goto(x + -80, y + -100)
    goto(x + -80, y + -120)

#mano izq
    fillcolor("pink")
    begin_fill()
    penup()
    goto(x + -100, y + -120)
    goto(x + -100, y + -100)
    goto(x + -140, y + -100)
    goto(x + -140, y + -160)
    goto(x + -100, y + -160)
    goto(x + -100, y + -140)
    goto(x + -80, y + -140)
    goto(x + -80, y + -120)
    goto(x + -100, y + -120)
    goto(x + -100, y + -100)
    goto(x + -100, y + -120)
    goto(x + -100, y + -120)
    goto(x + -80, y + -120)
    goto(x + -80, y + -140)
    end_fill()
#end mazo izq
def mano_der(x: int, y: int):
    penup()
    goto(x + -100, y + -140)
    goto(x + -100, y + -180)
    goto(x + -40, y + -180)
    goto(x + -40, y + -160)
    goto(x + 0, y + -160)
    goto(x + 0, y + -180)
    goto(x + 60, y + -180)
    goto(x + 60, y + -140)

#mano der
    fillcolor("pink")
    begin_fill()
    penup()
    goto(x + 40, y + -140)
    goto(x + 40, y + -120)
    goto(x + 60, y + -120)
    goto(x + 60, y + -100)
    goto(x + 100, y + -100)
    goto(x + 100, y + -160)
    goto(x + 60, y + -160)
    end_fill()
#end mano der
def pie_der(x: int, y: int):
    
    goto(x + 60,-180)

#pie der
    fillcolor("brown")
    begin_fill()
    penup()
    goto(x + 80, y + -180)
    pendown()
    goto(x + 80, y + -200)
    goto(x + 100, y + -200)
    goto(x + 100, y + -220)
    goto(x + 20, y + -220)
    goto(x + 20, y + -180)
    goto(x + 80, y + -180)
    end_fill()
    penup()
#end pie der

def pie_izq(x: int, y: int):
    penup()
    goto(x + 00, y + -160)
    goto(x + -40, y + -160)
    goto(x + -40, y + -180)
    goto(x + -60, y + -180)


#pie izq
    fillcolor("brown")
    begin_fill()
    penup()
    goto(x + -60, y + -220)
    goto(x + -140, y + -220)
    goto(x + -140, y + -200)
    goto(x + -120, y + -200)
    goto(x + -120, y + -180)
    goto(x + -100, y + -180)
    end_fill()
#end pie izq
def pecho(x: int, y: int):
#pecho
    fillcolor("blue")
    begin_fill()
    penup()
    goto(x + -100, y + -180)
    goto(x + -40, y + -180)
    goto(x + -40, y + -160)
    goto(x + 0, y + -160)
    goto(x + 0, y + -180)
    goto(x + 60, y + -180)
    goto(x + 60, y + -140)
    goto(x + 40, y + -140)
    goto(x + 40, y + -100)
    goto(x + 20, y + -100)
    goto(x + 20, y + -40)
    goto(x + 0, y + -40)
    goto(x + 0, y + -80)
    goto(x + -40, y + -80)
    goto(x + -40, y + -40)
    goto(x + -60, y + -40)
    goto(x + -60, y + -100)
    goto(x + -80, y + -100)
    goto(x + -80, y + -140)
    goto(x + -100, y + -140)
    goto(x + -100, y + -180)
    end_fill()
#end pecho
def boton_izq(x: int, y: int):
    penup()

#boton iz
    fillcolor("yellow")
    begin_fill()
    penup()
    goto(x + -60, y + -120)
    goto(x + -40, y + -120)
    goto(x + -40, y + -100)
    goto(x + -60, y + -100)
    goto(x + -60, y + -120)
    end_fill()
#end boton iz
def boton_der(x: int, y: int):
    penup()

#boton der
    fillcolor("yellow")
    begin_fill()
    penup()
    goto(x + 0, y + -120)
    goto(x + 0, y + -100)
    goto(x + 20, y + -100)
    goto(x + 20, y + -120)
    goto(x + 0, y + -120)
    end_fill()
#end boton der
def cuello(x: int, y: int):
    penup()

#cuello
    fillcolor("red")
    begin_fill()
    penup()
    goto(x + 0, y + -80)
    goto(x + 0, y + -40)
    goto(x + -40, y + -40)
    goto(x + -40, y + -80)
    goto(x + 0, y + -80)
    end_fill()
#cuello end
def draw(x: int, y: int):
    bigote(x, y)
    ojo(x, y)
    nariz(x, y)
    pelo(x, y)
    oreja(x, y)
    pelo2(x, y)
    cara(x, y)
    gorra(x, y)
    brazo_izq(x, y)
    brazo_der(x, y)
    mano_izq(x, y)
    mano_der(x, y)
    pie_der(x, y)
    pie_izq(x, y)
    pecho(x, y)
    boton_izq(x, y)
    boton_der(x, y)
    cuello(x, y)


