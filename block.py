# Block Blaster 3000
# Booya
# Built and designed for Python 2.6.6 32-bit, Pygame 1.9.1 32-bit, and Livewires 2.0

import random, math, pygame
from livewires import games, color

# The screen size
games.init(screen_width=640, screen_height=480, fps=120)
pygame.display.set_caption('Block Blaster 3000')
icon = games.load_image("block2.jpg")
pygame.display.set_icon(icon)


class Blocks(games.Sprite):
    """Blow these up with your perplexing ball of doom"""
    # How many points are awarded for destroying a block
    POINTS = 10                                             

    # Used to construct the proper number of blocks every level
    NUM = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15"]
    # The picture of the blocks
    block_image = {1: games.load_image("block1.jpg"),
                   2: games.load_image("block2.jpg"),
                   3: games.load_image("block3.jpg")}

    hitBlock = games.load_sound("hit1.wav")
    # How many blocks there are total
    total = 0
    # Odds for the strength of the blocks
    # 70% 1-hit, 20% 2-hit, 10% 3-hit
    chance = [1, 1, 1, 1, 1, 1, 1, 2, 2, 3]                 

    def __init__(self, side, tall):
        """Load them blocks"""
        self.hit = random.choice(Blocks.chance)
        super(Blocks, self).__init__(
            image=Blocks.block_image[self.hit],
            x=side, y=tall)
        # Keeps tally of how many blocks are in play
        Blocks.total += 1
        
    # Tells the blocks to die if anything runs into them
    def update(self):
        if self.overlapping_sprites:
            self.die()
            
    # Destroys the collided block, awards points, updates
    # the score, and checks for more blocks.
    # If there are no more blocks, a new level is started,
    # generating new blocks
    def die(self):
        """This kills the ball."""
        # Weakens the block
        self.hit -= 1
        # Plays the impact noise
        # self.hitBlock.play() # Uncomment if you want to add a sound effect
        # Awards points
        game.score.value += self.POINTS
        # Below is what happens if the block actually breaks
        if self.hit == 0:
            # Gets rid of the block
            self.destroy()
            # Updates the total number of blocks in play
            Blocks.total -= 1
            # Ensures score is aligned properly
            if game.score.value >= 100:
                game.score.right = games.screen.width - 10
            # Detects when all blocks are dead and resets the positions for generating new blocks
            if Blocks.total == 0:
                game.score.value += 30
                Master.positions_free = [1, 2, 3, 4, 5,
                                         6, 7, 8, 9, 10,
                                         11, 12, 13, 14, 15,
                                         16, 17, 18, 19, 20]
                Master.positions_used = []
                game.newlevel()
    
    
# This is the ball 
class Ball(games.Sprite):
    """Bouncy Bouncy"""
    # Loads the ball and makes it circular
    image = games.load_image("ball.png")
    image = image.convert_alpha()
    VELOCITY = 2    # Variable to control the speed of the ball

    def __init__(self, x, y):
        super(Ball, self).__init__(image=Ball.image, x=x, y=y)
        # Selects an angle from 45 degrees left to 45 degrees right and launches in that direction
        angle = random.randrange(-45, 45)*math.pi/180
        self.dx = self.VELOCITY * math.sin(angle)
        self.dy = self.VELOCITY * -math.cos(angle)

    def update(self):
        # Begin border collision detection
        if self.top < 0:
            self.dy = -self.dy
        if self.bottom > games.screen.height:
            game.gameover()
        if self.left < 0:
            self.dx = -self.dx
        if self.right > games.screen.width:
            self.dx = -self.dx
        # End
        # Begin block/paddle collision detection.  First checks for intersection
        if self.overlapping_sprites:
            for sprite in self.overlapping_sprites:
                # By detecting which side of the ball is not inside the block,
                # it determines what side the collision takes place on and
                # bounces accordingly
                if self.top >= sprite.top:                
                    self.dy = -self.dy
                if self.bottom <= sprite.bottom:                 
                    self.dy = -self.dy
                if self.left >= sprite.left:
                    self.dx = -self.dx
                if self.right <= sprite.right:
                    self.dx = -self.dx
        
        
class Paddle(games.Sprite):
    """ I played ping-pong even when I didn't have anyone to play ping-pong with."""
    image = games.load_image("paddle.jpg")
    
    # Loads the paddle
    def __init__(self, x, y):
        super(Paddle, self).__init__(image = Paddle.image, x = x, y = y)
        
    def update(self):
        # Lets the player slide the paddle left and right
        if games.keyboard.is_pressed(games.K_LEFT):
            self.dx = -4
        if games.keyboard.is_pressed(games.K_RIGHT):
            self.dx = 4
        # If the paddle is not moving, its velocity will lower by .5 until it is stationary
        if self.dx != 0:
            if self.dx >= .5:
                self.dx -= .5
            if self.dx <= -.5:
                self.dx += .5
        # This prevents the paddle from venturing off the screen, never to return...
        if self.left < 0:
            self.left = 0
        if self.right > games.screen.width:
            self.right = games.screen.width
        # This allows the player to exit the game by pressing the Escape key
        if games.keyboard.is_pressed(games.K_ESCAPE):
            exit()
            
            
class Master(object):
    """This class controls the game and manages various values that should not be controlled by other classes"""

    # These are used to select the positions of the blocks
    positions_free = [1, 2, 3, 4, 5,
                      6, 7, 8, 9, 10,
                      11, 12, 13, 14, 15,
                      16, 17, 18, 19, 20]

    positions_used = []

    gosound = games.load_sound("gameover.wav")
    # This is how many pixels from the left the blocks start
    margin = 89
    # This variable would allow a designer to change the width of the blocks without doing too much head-scratching
    block_width = 116
    
    def __init__(self):
        """These are constants that exist throughout the entire game"""
        # This is simply a message that says "Level"
        self.message = games.Text(value="Level",
                                  size=20,
                                  color=color.red,
                                  top=2,
                                  right=games.screen.width/2 + 11,
                                  is_collideable=False)
        games.screen.add(self.message)
        # This is the actual level, and sits below its label
        self.level = games.Text(value=0,
                                size=20,
                                color=color.red,
                                top=15,
                                right=games.screen.width/2,
                                is_collideable=False)
        games.screen.add(self.level)
        # This is the score.  
        self.score = games.Text(value=0,
                                size=30,
                                color=color.white,
                                top=10,
                                right=games.screen.width - 10,
                                is_collideable=False)
        games.screen.add(self.score)
        # At this point, the game loads the Paddle
        self.paddle = Paddle(games.screen.width/2, 450)
        games.screen.add(self.paddle)
        # The ball is loaded afterwards
        self.ball = Ball(games.screen.width/2, 370)
        games.screen.add(self.ball)

    def play(self):
        # This loads the background image
        background = games.load_image("bg.jpg")
        games.screen.background = background
        # This progresses the game to level 1 and begins the screen's main loop
        self.newlevel()
        games.screen.mainloop()

    def gameover(self):
        # This plays the "Game Over" sound
        # self.gosound.play() # Uncomment if you want to add your own game over sound effect
        # This displays "Game Over" across the screen
        self.gameoverscreen = games.Text(value="Game Over",
                                         size=100,
                                         color=color.red,
                                         top=games.screen.height/2-40,
                                         right=games.screen.width/2+190,
                                         is_collideable=False)
        games.screen.add(self.gameoverscreen)

    def newlevel(self):
        """This creates blocks and updates the level number"""
        # It wouldn't be a level without a level number
        self.level.value += 1
        # Selects from 20 possible slots and fills 15 of them with blocks
        for b in Blocks.NUM:
            b_position = random.choice(self.positions_free)
            print b_position
            self.positions_used.append(b_position)
            self.positions_free.remove(b_position)
            if b_position == 1:
                new_block = Blocks(self.margin + (self.block_width*0), 50)
                games.screen.add(new_block)
            if b_position == 2:
                new_block = Blocks(self.margin + (self.block_width*1), 50)
                games.screen.add(new_block)
            if b_position == 3:
                new_block = Blocks(self.margin + (self.block_width*2), 50)
                games.screen.add(new_block)
            if b_position == 4:
                new_block = Blocks(self.margin + (self.block_width*3), 50)
                games.screen.add(new_block)
            if b_position == 5:
                new_block = Blocks(self.margin + (self.block_width*4), 50)
                games.screen.add(new_block)
            if b_position == 6:
                new_block = Blocks(self.margin + (self.block_width*0), 88)
                games.screen.add(new_block)
            if b_position == 7:
                new_block = Blocks(self.margin + (self.block_width*1), 88)
                games.screen.add(new_block)
            if b_position == 8:
                new_block = Blocks(self.margin + (self.block_width*2), 88)
                games.screen.add(new_block)
            if b_position == 9:
                new_block = Blocks(self.margin + (self.block_width*3), 88)
                games.screen.add(new_block)
            if b_position == 10:
                new_block = Blocks(self.margin + (self.block_width*4), 88)
                games.screen.add(new_block)
            if b_position == 11:
                new_block = Blocks(self.margin + (self.block_width*0), 126)
                games.screen.add(new_block)
            if b_position == 12:
                new_block = Blocks(self.margin + (self.block_width*1), 126)
                games.screen.add(new_block)
            if b_position == 13:
                new_block = Blocks(self.margin + (self.block_width*2), 126)
                games.screen.add(new_block)
            if b_position == 14:
                new_block = Blocks(self.margin + (self.block_width*3), 126)
                games.screen.add(new_block)
            if b_position == 15:
                new_block = Blocks(self.margin + (self.block_width*4), 126)
                games.screen.add(new_block)
            if b_position == 16:
                new_block = Blocks(self.margin + (self.block_width*0), 164)
                games.screen.add(new_block)
            if b_position == 17:
                new_block = Blocks(self.margin + (self.block_width*1), 164)
                games.screen.add(new_block)
            if b_position == 18:
                new_block = Blocks(self.margin + (self.block_width*2), 164)
                games.screen.add(new_block)
            if b_position == 19:
                new_block = Blocks(self.margin + (self.block_width*3), 164)
                games.screen.add(new_block)
            if b_position == 20:
                new_block = Blocks(self.margin + (self.block_width*4), 164)
                games.screen.add(new_block)

# This plays the game
game = Master()
game.play()
