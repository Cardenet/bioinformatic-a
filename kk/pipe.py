from turtle import*

#setup(600, 600)


def location_pipe():
    location_pipe_x = 500
    location_pipe_y = -425
    
    penup()
    goto(location_pipe_x,
         location_pipe_y)
    pendown()
    
# Esta es la tubería de abajo
def pipe_down():
    "Esta es la tubería de abajo"
    
    fillcolor("lime")
    begin_fill()
    pipe_down1_x = 650
    pipe_down2_x = 500
    pipe_down1_y = -425
    pipe_y = -275
    
    goto(pipe_down1_x,
         pipe_down1_y)
    goto(pipe_down1_x,
         pipe_y)
    goto(pipe_down2_x,
         pipe_y)
    goto(pipe_down2_x,
         pipe_down1_y)
    end_fill()
    
def location_pipe_up():
    pipe_up_x = 450
    pipe_up_y = -225
    
    penup()
    goto(pipe_up_x,
         pipe_up_y)
    pendown()

def pipe_up():
    fillcolor("lime")
    begin_fill()
    pipe_up2_x = 700
    pipe_up_x = 450
    pipe_y = -275
    pipe_up_y = -225


    goto(pipe_up_x,
         pipe_y)
    goto(pipe_up2_x,
         pipe_y)
    goto(pipe_up2_x,
         pipe_y)
    goto(pipe_up2_x,
         pipe_up_y)
    goto(pipe_up_x,
         pipe_up_y)
    end_fill()
    

def draw():
    location_pipe()
    pipe_down()
    location_pipe_up()
    pipe_up()
    penup()

