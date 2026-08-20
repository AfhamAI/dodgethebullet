import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import random



plt.rcParams["toolbar"] = "None"

fig , ax = plt.subplots()



#----------------------------------
fig.canvas.manager.set_window_title("Dodge the Bullet")


fig.patch.set_facecolor("black")
ax.set_facecolor("black")
for spine in ax.spines.values():
    spine.set_color("grey")
#----------------------------------

ax.set_xlabel("-By Afham", color="white")

ax.set_xlim(0,10)
ax.set_ylim(0,10)


ax.set_xticks([])
ax.set_yticks([])


player_x = 5
player_y = 1


player = ax.scatter(player_x, player_y, s = 500, color="white")


ball_x = random.randint(1,9)
ball_y = 10

ball = ax.scatter(ball_x, ball_y, s =300, color="red", marker="v")



def move(event):
    global player_x
    if event.key == "left":
        player_x -= 0.5
    if event.key  == "right":
        player_x += 0.5


    if player_x < 0:
        player_x = 0

    if player_x > 10:
        player_x = 10 

fig.canvas.mpl_connect("key_press_event", move)




def update(frame):
    global ball_x , ball_y
    ball_y -= 0.5


    if abs(ball_x - player_x) < 0.6 and abs(ball_y - player_y) < 0.6:
        plt.close(fig)
        return


    if ball_y < 0:
        ball_y = 10
        ball_x = random.randint(1, 9)


    player.set_offsets([[player_x, player_y]])
    ball.set_offsets([[ball_x, ball_y]])
    return player, ball

animation = FuncAnimation(fig, update, interval=30)


plt.show()