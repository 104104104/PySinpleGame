from tkinter import *
import random
import time

#ボールのclass定義
class Ball:
  def __init__(self, canvas, paddle, color):
    self.canvas=canvas
    self.paddle = paddle
    self.id = canvas.create_oval(10,10,25,25,fill=color)
    self.canvas.move(self.id, 245, 100)#ウィンドウの真ん中にballを表示
    starts = [-3, -2, -1, 0, 1, 2, 3]
    random.shuffle(starts)
    self.x = starts[0]#最初のx座標の変化をランダムに選ぶ
    self.y = -3
    self.canvas_height = self.canvas.winfo_height()#←これはキャンバスの高さを返す関数
    self.canvas_width = self.canvas.winfo_width()#←これはキャンバスの幅を返す関数

  def hit_paddle(self, pos):
    paddle_pos = self.canvas.coords(self.paddle.id)
    if pos[2] >= paddle_pos[0] and pos[0] <= paddle_pos[2]:
        if pos[3] >= paddle_pos[1] and pos[3] <= paddle_pos[3]:
            return True
    return False

  def draw(self):
    self.canvas.move(self.id, self.x, self.y)
    pos = self.canvas.coords(self.id)#crrodsはcanvasの座標を返す関数。[左上x, 左上y, 右下x, 右下y]
    #ボールのy座標がキャンバスの外へ行かないように！
    if pos[1] <= 0:
      self.y = 3
    if pos[3] >= self.canvas_height:
      self.y = -3
    if self.hit_paddle(pos) == True:
        self.y = -3
    #ボールのx座標がキャンバスの外へ行かないように！
    if pos[0] <= 0:
      self.x = 3
    if pos[2] >= self.canvas_width:
      self.x = -3

class Paddle:
    def __init__(self, canvas, color):
        self.canvas = canvas
        self.id = canvas.create_rectangle(0,0,100,10, fill=color)
        self.canvas.move(self.id, 200, 300)
        self.x=0
        self.canvas_width = self.canvas.winfo_width()#←これはキャンバスの幅を返す関数
        self.canvas.bind_all("<KeyPress-Left>", self.turn_left)
        self.canvas.bind_all("<KeyPress-Right>", self.turn_right)

    def turn_left(self, evt):
        self.x = -2

    def turn_right(self, evt):
        self.x = 2

    def draw(self):
        self.canvas.move(self.id, self.x, 0)
        pos = self.canvas.coords(self.id)#crrodsはcanvasの座標を返す関数。[左上x, 左上y, 右下x, 右下y]
        if pos[0] <= 0:
            self.x = 0
        elif pos[2] >= self.canvas_width:
            self.x = 0

tk=Tk()
tk.title("Game")
tk.resizable(0,0)#ウィンドウのサイズを変更不可にする
tk.wm_attributes("-topmost", 1)#このウィンドウを一番上に表示する
canvas = Canvas(tk, width=500, height=400, bd=0, highlightthickness=0)#キャンバスの設定
canvas.pack()
tk.update()

paddle = Paddle(canvas, "blue")
ball = Ball(canvas, paddle, "red")

while True:
  ball.draw()
  paddle.draw()
  tk.update_idletasks()
  tk.update()
  time.sleep(0.02)
