from tkinter import*;import time
class Ball:
    def __init__(self,canvas,paddle):self.score=0;self.ids=canvas.create_text(450,50,text=0,fill='grey');self.bul=True;self.speed=2;self.x=1;self.y=-2;self.canvas=canvas;self.paddle=paddle;self.id=canvas.create_oval(240,240,260,260,fill='red');
    def hit(self,pos):z=pos[2]>= self.paddle.pos[0] and pos[0]<= self.paddle.pos[2] and pos[3]>= self.paddle.pos[1] and pos[1]<= self.paddle.pos[3];self.score=(self.score+1) if z else (self.score);self.canvas.itemconfig(self.ids,text=self.score);return True if z else False
    def draw(self):pos=self.canvas.coords(self.id);self.x=-self.speed if pos[2]>500 else (self.speed if pos[0]<0 else self.x);self.bul=True if pos[3]<=500 else False;self.y=-self.speed if self.hit(pos=pos) else (self.speed if pos[1]<0 else self.y);self.canvas.move(self.id,self.x,self.y)
class Paddle:
    def __init__(self,canvas):self.canvas=canvas;self.x=0;self.id=canvas.create_rectangle(200,450,300,460,fill='blue');self.canvas.bind_all('<KeyPress-Left>',self.l);self.canvas.bind_all('<KeyPress-Right>',self.l);self.speed=6
    def draw(self):self.pos=self.canvas.coords(self.id);self.x=0 if self.x>0 and self.pos[2]>500 or self.x<0 and self.pos[0]<0 else self.x;self.canvas.move(self.id,self.x,0)
    def l(self,p):self.x=-self.speed if ('Left'in str(p))else self.speed;
tk=Tk();tk.resizable(0,0);tk.geometry('500x500+100+100');tk.title('game');canvas=Canvas(width=500,height=500,bg='black');canvas.pack();paddle=Paddle(canvas);ball=Ball(canvas,paddle)
while ball.bul:paddle.draw();ball.draw();tk.update();tk.update_idletasks();time.sleep(0.01)
canvas.create_text(250,250,text='game over',fill='red',font=('Courier',26))
