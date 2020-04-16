def setup():
    size(1300,1000)
    
def draw():
    
    # CHAMINÉ
    fill(152,58,0)
    rect(850,280,100,220)
    
    # PAREDE
    fill(211,198,169)
    rect(250,500,750,500)
    
    # JANELA D
    fill(255,255,255)
    rect(780,530,150,150)
    line(850,530,850,680)
    
    # JANELA E
    fill(255,255,255)
    rect(320,530,150,150)
    line(390,530,390,680)
    
    # PORTA
    fill(183,108,33)
    rect(550,750,150,300)
    
    # TELHADO
    fill(116,116,116)
    triangle(250,500,625,275,1000,500)
    
    # MAÇANETA
    fill(00,00,00)
    rect(680,870,10,10,10,10,10,10)
    
    # FUMAÇA
    fill(255,255,255)
    ellipse(900,250,50,50)
    ellipse(930,190,70,70)
    ellipse(980,120,90,90)
    
