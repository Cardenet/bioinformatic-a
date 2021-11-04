from turtle import*
import turtle

speed(0)

#bigote
def bigote():
    fillcolor("black")
    begin_fill()
    goto(20, 0)
    goto(20, 20)
    goto(40, 20)
    goto(40, 0)
    goto(80, 0)
    goto(80, -20)
    goto(0, -20)
    goto(0, 0)
    goto(20, 0)
    end_fill()
#end bigote

#ojo
def ojo():
    
    fillcolor("black")
    begin_fill()
    goto(20, 20)
    goto(20, 60)
    goto(0, 60)
    goto(0, 20)
    goto(20, 20)
    goto(40, 20)
    goto(40, 0)
    end_fill()
#end ojo
def nariz():
#nariz
    fillcolor("pink")
    begin_fill()
    goto(80, 0)
    goto(100, 0)
    goto(100, 20)
    goto(80, 20)
    goto(80, 40)
    goto(40, 40)
    goto(40, 60)
    goto(20, 60)
    goto(20, 20)
    goto(40, 20)
    end_fill()
    goto(20, 20)
    goto(20, 60)
#nariz end
def pelo():
    
    goto(-40, 60)

#pelo 1
    fillcolor("brown")
    begin_fill()
    goto(-40, 40)
    goto(-60, 40)
    goto(-60, 20)
    goto(-40, 20)
    goto(-40, 0)
    goto(-80, 0)
    goto(-80, 40)
    goto(-100, 40)
    goto(-100, 60)
    goto(-40, 60)
    goto(-100, 60)
    end_fill()
 #end pelo 1
def oreja():
#oreja
    fillcolor("pink")
    begin_fill()
    goto(-100, 40)
    goto(-100, 0)
    goto(-80, 0)
    goto(-80, 40)
    goto(-100, 40)
    goto(-100, 0)
    end_fill()
#end oreja
def pelo2():
#pelo 2
    fillcolor("brown")
    begin_fill()
    goto(-80, 0)
    goto(-80, -20)
    goto(-120, -20)
    goto(-120, 40)
    goto(-100, 40)
    end_fill()
#end pelo 2
def cara():
    goto(-100, 0)
    goto(-80, 0)
    goto(-80, -20)

    #cara
    fillcolor("pink")
    begin_fill()
    goto(-80, -20)
    goto(-80, -40)
    goto(60, -40)
    goto(60, -20)
    goto(0, -20)
    goto(0, 0)
    goto(20, 0)
    goto(20, 20)
    goto(0, 20)
    goto(0, 60)
    goto(-40, 60)
    goto(-40, 40)
    goto(-60, 40)
    goto(-60, 20)
    goto(-40, 20)
    goto(-40, 0)
    goto(-80, 0)
    goto(-80, -20)
    end_fill()
    penup()
#end cara
def gorra():
    goto(80, -20)

    pendown()

    goto(80, 0)
    goto(100, 0)
    goto(100, 20)
    goto(80, 20)
    goto(80, 40)
    goto(40, 40)
    goto(40, 60)

#gorra
    fillcolor("red")
    begin_fill()
    goto(80, 60)
    goto(80, 80)
    goto(20, 80)
    goto(20, 100)
    goto(-80, 100)
    goto(-80, 80)
    goto(-100, 80)
    goto(-100, 60)
    end_fill()
#gorra end
def brazo_izq():
    
    goto(-100,0)
    goto(-80,0)
    goto(-80,-40)

#brazo izq
    fillcolor("red")
    begin_fill()
    goto(-100,-40)
    goto(-100,-60)
    goto(-120,-60)
    goto(-120,-80)
    goto(-140,-80)
    goto(-140,-100)
    goto(-100,-100)
    goto(-100,-120)
    goto(-80,-120)
    goto(-80,-100)
    goto(-60,-100)
    goto(-60,-40)
    goto(-80,-40)
    goto(-60,-40)
    end_fill()
#end brazo izq
def brazo_der():
    
    goto(-40,-40)
    goto(-40,-80)
    goto(0,-80)
    goto(0,-60)
    goto(20,-60)
    goto(20,-40)
    goto(20,-60)
    goto(20,-100)

#brazo der
    fillcolor("red")
    begin_fill()
    goto(20,-60)
    goto(80,-60)
    goto(80,-80)
    goto(100,-80)
    goto(100,-100)
    goto(60,-100)
    goto(60,-120)
    goto(40,-120)
    goto(40,-100)
    goto(20,-100)
    end_fill()
#end brazo der
def mano_izq():
    
    goto(20,-60)
    goto(0,-60)
    goto(0,-80)
    goto(-40,-80)
    goto(-40,-40)
    goto(-60,-40)
    goto(-60,-100)
    goto(-80,-100)
    goto(-80,-120)

#mano izq
    fillcolor("pink")
    begin_fill()
    goto(-100,-120)
    goto(-100,-100)
    goto(-140,-100)
    goto(-140,-160)
    goto(-100,-160)
    goto(-100,-140)
    goto(-80,-140)
    goto(-80,-120)
    goto(-100,-120)
    goto(-100,-100)
    goto(-100,-120)
    goto(-100,-120)
    goto(-80,-120)
    goto(-80,-140)
    end_fill()
#end mazo izq
def mano_der():
    
    goto(-100,-140)
    goto(-100,-180)
    goto(-40,-180)
    goto(-40,-160)
    goto(0,-160)
    goto(0,-180)
    goto(60,-180)
    goto(60,-140)

#mano der
    fillcolor("pink")
    begin_fill()
    goto(40,-140)
    goto(40,-120)
    goto(60,-120)
    goto(60,-100)
    goto(100,-100)
    goto(100,-160)
    goto(60,-160)
    end_fill()
#end mano der
def pie_der():
    
    goto(60,-180)

#pie der
    fillcolor("brown")
    begin_fill()
    goto(80,-180)
    goto(80,-200)
    goto(100,-200)
    goto(100,-220)
    goto(20,-220)
    goto(20,-180)
    goto(00,-180)
    end_fill()
#end pie der

def pie_izq():
    
    goto(00,-160)
    goto(-40,-160)
    goto(-40,-180)
    goto(-60,-180)


#pie izq
    fillcolor("brown")
    begin_fill()
    goto(-60,-220)
    goto(-140,-220)
    goto(-140,-200)
    goto(-120,-200)
    goto(-120,-180)
    goto(-100,-180)
    end_fill()
#end pie izq
def pecho():
#pecho
    fillcolor("blue")
    begin_fill()
    goto(-100,-180)
    goto(-40,-180)
    goto(-40,-160)
    goto(0,-160)
    goto(0,-180)
    goto(60,-180)
    goto(60,-140)
    goto(40,-140)
    goto(40,-100)
    goto(20,-100)
    goto(20,-40)
    goto(0,-40)
    goto(0,-80)
    goto(-40,-80)
    goto(-40,-40)
    goto(-60,-40)
    goto(-60,-100)
    goto(-80,-100)
    goto(-80,-140)
    goto(-100,-140)
    goto(-100,-180)
    end_fill()
#end pecho
def boton_izq():
    penup()

#boton iz
    fillcolor("yellow")
    begin_fill()
    goto(-60,-120)
    goto(-40,-120)
    goto(-40,-100)
    goto(-60,-100)
    goto(-60,-120)
    end_fill()
#end boton iz
def boton_der():
    penup()

#boton der
    fillcolor("yellow")
    begin_fill()
    goto(0,-120)
    goto(0,-100)
    goto(20,-100)
    goto(20,-120)
    goto(0,-120)
    end_fill()
#end boton der
def cuello():
    penup()

#cuello
    fillcolor("red")
    begin_fill()
    goto(0,-80)
    goto(0,-40)
    goto(-40,-40)
    goto(-40,-80)
    goto(0,-80)
    end_fill()
#cuello end
def draw():
    bigote()
    ojo()
    nariz()
    pelo()
    oreja()
    pelo2()
    cara()
    gorra()
    brazo_izq()
    brazo_der()
    mano_izq()
    mano_der()
    pie_der()
    pie_izq()
    pecho()
    boton_izq()
    boton_der()
    cuello()

