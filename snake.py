#danrus32
import pygame 
import random
import time
pygame.init()
#display
width = 640 
height = 480 
display = pygame.display.set_mode((width,height))
pygame.display.update()
pygame.display.set_caption("Zmeika")

clock = pygame.time.Clock()
def main (display,width,height):
	#lungimea
	zmeika_size = (10, 10)
	#culorile 
	colors = {
		"zmeika_head" : (0,200,0),
		"zmeika_tails" : (0,255,0),
		"apple" : (255,0,0),
	}

	#zmeica position 
	zmeika_pos ={ 
		"x" : width/2-10,
		"y" : height/2-10,
		"x_change" : 0,
		"y_change" : 0,
	}

	#speed
	zmeika_speed = 10

	#hvost
	zmeika_tails= []
	


	#apple
	apple_pos ={
		"x": round(random.randrange(0, width - zmeika_size[0]) / 10) * 10,
	    "y": round(random.randrange(0, height - zmeika_size[1]) / 10) * 10,
	    }

	#apple size
	apple_size  = [10,10]
	#so micat 
	apple_eaten = 0
	#start 
	game_end = False
	def play (width,height,zmeika_size,zmeika_tails,zmeika_pos,zmeika_speed,colors,apple_pos,apple_size,apple_eaten,game_end):
		while not game_end:
			time.sleep(0.1)
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					game_end = True
				elif event.type == pygame.KEYDOWN:
					if event.key == pygame.K_LEFT and zmeika_pos["x_change"] == 0:
						zmeika_pos["x_change"] = -zmeika_speed
						zmeika_pos["y_change"] = 0 
					elif event.key == pygame.K_RIGHT and zmeika_pos["x_change"] == 0:
						zmeika_pos["x_change"] = zmeika_speed
						zmeika_pos["y_change"] = 0
					elif event.key == pygame.K_UP and zmeika_pos["y_change"] == 0:
						zmeika_pos["x_change"] = 0
						zmeika_pos["y_change"] = -zmeika_speed
					elif event.key == pygame.K_DOWN and zmeika_pos["y_change"] == 0:
						zmeika_pos["x_change"] = 0
						zmeika_pos["y_change"] = zmeika_speed
			#clear
			display.fill((0,0,0))

			#move tails 
			ltx = zmeika_pos["x"]
			lty = zmeika_pos["y"]

			for i, v in enumerate(zmeika_tails):
				_ltx = zmeika_tails[i][0]
				_lty = zmeika_tails[i][1]
				zmeika_tails[i][0] = ltx
				zmeika_tails[i][1] = lty

				ltx = _ltx
				lty = _lty
			#draw tails 
			for d in zmeika_tails:
				pygame.draw.rect(display,colors["zmeika_tails"],[
					d[0],
					d[1],
					zmeika_size[0],
					zmeika_size[1]])
			#draw zmeika
			zmeika_pos["x"] += zmeika_pos["x_change"]
			zmeika_pos["y"] += zmeika_pos["y_change"]


			#teleport 
			if zmeika_pos["x"] <= -zmeika_size[0]:
				zmeika_pos["x"] = width
			elif zmeika_pos["x"] >= width:
				zmeika_pos["x"] = 0
			if zmeika_pos["y"] <= -zmeika_size[1]:
				zmeika_pos["y"] = height
			elif zmeika_pos["y"] >= height:
				zmeika_pos["y"] = 0
			#draw head

			pygame.draw.rect(display,colors["zmeika_head"],[
				zmeika_pos["x"],
				zmeika_pos["y"],
		    	zmeika_size[0],
		    	zmeika_size[1]])
			#draw apple
			pygame.draw.rect(display,colors["apple"],[
				apple_pos["x"],
				apple_pos["y"],
				apple_size[0],
				apple_size[1]])
			#detected collizion with apple
			if (zmeika_pos["x"] == apple_pos["x"]
				and zmeika_pos["y"] == apple_pos["y"]):
				apple_eaten  += 1
				zmeika_tails.append([apple_pos["x"],apple_pos["y"]])
				

				apple_pos ={
					"x": round(random.randrange(0, width - zmeika_size[0]) / 10) * 10,
				    "y": round(random.randrange(0, height - zmeika_size[1]) / 10) * 10,
				    }
			try:
				#detected collizion with tails
				for i , v in enumerate (zmeika_tails):
					if (zmeika_pos["x"] +zmeika_pos["x_change"] == zmeika_tails[i][0]
						and zmeika_pos["y"]+zmeika_pos["y_change"] == zmeika_tails[i][1]):
						

								#hvost
								zmeika_tails= []
								zmeika_pos["x"]  = width/2-10
								zmeika_pos["y"]  = height/2-10
								zmeika_pos["x_change"]  = 0
								zmeika_pos["y_change"]  = 0
								
		
		
			except:
				pass

			pygame.display.update()
	
	play(width,height,zmeika_size,zmeika_tails,zmeika_pos,zmeika_speed,colors,apple_pos,apple_size,apple_eaten,game_end)
main(display,width,height)

pygame.quit()
quit()
