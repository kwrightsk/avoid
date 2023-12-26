square_y1 = -50 #starting "home" y-position of 1st raining square
square_y2 = -150 #starting "home" y-position of 2nd raining square
square_y3 = -250 #starting "home" y-position of 3rd raining square
square_y4 = -350 #starting "home" y-position of 4th raining square
square_y5 = -450 #starting "home" y-position of 5th raining square
square_y6 = -550 #starting "home" y-position of 6th raining square

square_x1 = random(-40, 460) #starting "home" x-position of 1st raining square; randomized to be different each time
square_x2 = random(-40, 460) #starting "home" x-position of 2nd raining square; randomized to be different each time
square_x3 = random(-40, 460) #starting "home" x-position of 3rd raining square; randomized to be different each time
square_x4 = random(-40, 460) #starting "home" x-position of 4th raining square; randomized to be different each time
square_x5 = random(-40, 460) #starting "home" x-position of 5th raining square; randomized to be different each time
square_x6 = random(-40, 460) #starting "home" x-position of 6th raining square; randomized to be different each time

score = "0" #number of points scored during gameplay; string data (to be printed as text to canvas)

game_opening = "AVOID" #title message on starting screen
game_over = "" #title message on ending 'game over' screen

speed_increase = 0 #increases step-amount of y-position of raining squares; increases speed raining squares fall at
level = "1" #numerical difficulty level the player is currently playing on
level_colour = color(254, 221, 0) #color of squares during each level; initially coloured yellow for level 1


def touching_square(square_x, square_y):
    
    """returns 'True' if the player's square is touching a raining square
    square_x = x-value of top-left corner of raining square
    square_y = y-value of top-left corner of raining square"""
    
    playersq_x = mouseX - 25 #x-value of top-left corner of player's square
    playersq_y = 500 #y-value of top-left corner of player's square
    
    #returns 'True' if right/left corner of player's square is within/equal to corners of raining square AND raining square's y-value is greater/equal to y-value of player's square (but above ground level) **adjusted a little to ensure squares visually collide before the game is over**
    return (((playersq_x >= square_x and playersq_x <= (square_x + 50)) or (playersq_x + 50 >= square_x and playersq_x + 50 <= (square_x + 50))) and (549 >= square_y >= 451)) 


def inside_canvas():
    
    """returns x-value of player's square so that it stays within the borders of the canvas"""
    
    return min(width - 51, max(0, mouseX - 25))
    

def setup():
    size(500, 600) #portrait orientation, upright canvas
    
    
def draw():
    
    """displays all aspects of gameplay to the canvas including score, levels, title screen, gameover screen, raining squares, and the player's square"""
    
    background(255) # white background
    
    global square_y1, square_y2, square_y3, square_y4, square_y5, square_y6
    global square_x1, square_x2, square_x3, square_x4, square_x5, square_x6
    global game_over, score, speed_increase, level, level_colour, game_opening, highscore
    
    
    if game_opening == "AVOID": #if the game_opening variable is storing the 'AVOID' message, the title screen will be displayed
        
        textSize(30)
        fill(0)
        text(game_opening, 200, 300) #displays title 'AVOID' to canvas
        
        textSize(13)
        text("Move the mouse to help the white square dodge the coloured squares!", 25, 350) #displays instructions to canvas
        text("The more squares you avoid, the higher your score will be.", 70, 375) #displays additional instructions to canvas
        text("There are a total of 10 levels to try and reach. How far will you go?", 40, 400) #displays additional instructions to canvas
        
        textSize(15)
        text("Press 'ENTER' to begin.", 170, 440) #displays instructions on how to begin the game
        
    
    if square_y1 < 551 and game_over == "" and game_opening == "": #1st square begins to fall as long as game has started and is not yet over, and while y-value has not gone below ground
     
        fill(level_colour)       
        square(square_x1, square_y1, 50)
        square_y1 = square_y1 + 5 + speed_increase
            
    if square_y2 < 551 and game_over == "" and game_opening == "": #2nd square begins to fall under same conditions of 1st square's statement
        
        fill(level_colour)        
        square(square_x2, square_y2, 50)
        square_y2 = square_y2 + 5 + speed_increase
            
    if square_y3 < 551 and game_over == "" and game_opening == "": #3rd square begins to fall under same conditions of 1st and 2nd squares' statements
        
        fill(level_colour)        
        square(square_x3, square_y3, 50)
        square_y3 = square_y3 + 5 + speed_increase
            
    if square_y4 < 551 and game_over == "" and game_opening == "": #4th square begins to fall under same conditions of 1st, 2nd, 3rd squares' statements
        
        fill(level_colour)        
        square(square_x4, square_y4, 50)
        square_y4 = square_y4 + 5 + speed_increase
            
    if square_y5 < 551 and int(score) >= 190 and game_over == "": #5th square begins to fall once the score has reached 190 (level 7) and the game is not over
        
        fill(level_colour)        
        square(square_x5, square_y5, 50)
        square_y5 = square_y5 + 5 + speed_increase    
            
    if square_y6 < 551 and int(score) >= 270 and game_over == "": #6th square begins to fall once the score has reached 270 (level 9) and the game is not over
        
        fill(level_colour)        
        square(square_x6, square_y6, 50)
        square_y6 = square_y6 + 5 + speed_increase       
    
            
    if square_y1 >= 551 and game_over == "": #when 1st raining square has gone below ground, it is moved back to its home position, and a point is added to the score (as long as the game isn't over)
        
        square_y1 = -50
        square_x1 = random(-40, 460)
        
        score = int(score)
        score = score + 1
        score = str(score)
        
    if square_y2 >= 551 and game_over == "": #when 2nd raining square has gone below ground, it is moved back to its home position, and a point is added to the score (as long as the game isn't over)
        
        square_y2 = -150
        square_x2 = random(-40, 460)
        
        score = int(score)
        score = score + 1
        score = str(score)
        
    if square_y3 >= 551 and game_over == "": #when 3rd raining square has gone below ground, it is moved back to its home position, and a point is added to the score (as long as the game isn't over)
        
        square_y3 = -250
        square_x3 = random(-40, 460)
        
        score = int(score)
        score = score + 1
        score = str(score)
        
    if square_y4 >= 551 and game_over == "": #when 4th raining square has gone below ground, it is moved back to its home position, and a point is added to the score (as long as the game isn't over)
        
        square_y4 = -350
        square_x4 = random(-40, 460)
        
        score = int(score)
        score = score + 1
        score = str(score)
        
    if square_y5 >= 551 and game_over == "": #when 5th raining square has gone below ground, it is moved back to its home position, and a point is added to the score (as long as the game isn't over)
        
        square_y5 = -450
        square_x5 = random(-40, 460)
        
        score = int(score)
        score = score + 1
        score = str(score)
        
    if square_y6 >= 551 and game_over == "": #when 6th raining square has gone below ground, it is moved back to its home position, and a point is added to the score (as long as the game isn't over)
        
        square_y6 = -550
        square_x6 = random(-40, 460)
        
        score = int(score)
        score = score + 1
        score = str(score)        


    if score == "20": #once the score has reached 20, the level and speed increase by 1, and the colour of the raining squares change
        
        #level 2, speed + 1, orange
        level = "2"
        speed_increase = 1
        level_colour = color(255, 130, 0)
        
    if score == "40": #once the score has reached 40, the level and speed increase by 1, and the colour of the raining squares change
        
        #level 3, speed + 2, red
        level = "3"
        speed_increase = 2
        level_colour = color(235, 51, 0)
        
    if score == "70": #once the score has reached 70, the level and speed increase by 1, and the colour of the raining squares change
        
        #level 4, speed + 3, pink
        level = "4"
        speed_increase = 3
        level_colour = color(239, 66, 111)
        
    if score == "110": #once the score has reached 110, the level and speed increase by 1, and the colour of the raining squares change
        
        #level 5, speed + 4, magenta
        level = "5"
        speed_increase = 4
        level_colour = color(198, 0, 126)
        
    if score == "150": #once the score has reached 150, the level and speed increase by 1, and the colour of the raining squares change
        
        #level 6, speed + 5, purple
        level = "6"
        speed_increase = 5
        level_colour = color(147, 50, 142)
        
    if score == "190": #once the score has reached 190, the level increases by 1, and the colour of the raining squares change
        
        #level 7, speed + 5, blue, initiates 5th raining square
        level = "7"
        speed_increase = 5
        level_colour = color(76, 18, 161)
        
    if score == "230": #once the score has reached 230, the level and speed increase by 1, and the colour of the raining squares change
        
        #level 8, speed + 6, light blue
        level = "8"
        speed_increase = 6
        level_colour = color(105, 179, 231)
        
    if score == "270": #once the score has reached 270, the level increases by 1, and the colour of the raining squares change
        
        #level 9, speed + 6, green, initiates 6th raining square 
        level = "9"
        speed_increase = 6
        level_colour = color(31, 168, 36)
        
    if score == "300": #once the score has reached 300, the level and speed increase by 1, and the colour of the raining squares change
        
        #level 10, speed + 7, lime green
        level = "10 (Endless)"
        speed_increase = 7
        level_colour = color(177, 214, 0)
        
        
    if touching_square(square_x1, square_y1) == True: #if player's square touches 1st raining square, the game is over
        
        game_over = "GAME OVER"
   
    if touching_square(square_x2, square_y2) == True: #if player's square touches 2nd raining square, the game is over
        
        game_over = "GAME OVER"
        
    if touching_square(square_x3, square_y3) == True: #if player's square touches 3rd raining square, the game is over
        
        game_over = "GAME OVER"

    if touching_square(square_x4, square_y4) == True: #if player's square touches 4th raining square, the game is over
        
        game_over = "GAME OVER"
        
    if touching_square(square_x5, square_y5) == True: #if player's square touches 5th raining square, the game is over
        
        game_over = "GAME OVER"
        
    if touching_square(square_x6, square_y6) == True: #if player's square touches 6th raining square, the game is over
        
        game_over = "GAME OVER"
        
        
    if game_over == "GAME OVER" and game_opening == "": #when the game is over, game over message is printed to the screen
        
        textSize(30)
        fill(0)
        text(game_over, 165, 300) #prints 'GAME OVER' to canvas
        
        textSize(20)
        text("Press 'ENTER' to play again", 120, 350) #prints replay instructions to canvas
        
        textSize(15)
        text("Press 'BACKSPACE' to return to the home screen", 75, 380)
        
    if game_opening == "": #displays score and level while title screen is not showing
        
        fill(0)
        textSize(20)
        text("Score: " + score, 10, 20) #prints score to upper left corner of the canvas
    
        text("Level " + level, 10, 50) #prints level to upper left corner of the canvas, below the score
    
            
    noStroke()
    fill(200)
    rect(0, 550, width, 50) #prints ground to canvas
    
    stroke(0)
    fill(255)
    square(inside_canvas(), 500, 50) #prints player square to canvas
    
    
def keyPressed():
    
    """ when 'ENTER' or 'RETURN' key is pressed, game is reset and squares immediately start raining down again
    when 'BACKSPACE' is pressed, the title screen reappears as if the program was restarted"""
        
    if key == ENTER or key == RETURN:
        
        global square_y1, square_y2, square_y3, square_y4, square_y5, square_y6 
        global square_x1, square_x2, square_x3, square_x4, square_x5, square_x6
        global game_over, score, speed_increase, level, level_colour, game_opening, highscore
        
        #reset all the raining squares' y-values to their home positions
        square_y1 = -50
        square_y2 = -150
        square_y3 = -250
        square_y4 = -350
        square_y5 = -450
        square_y6 = -550
        
        #reset all the raining squares' x-values to a new random position
        square_x1 = random(-40, 460)
        square_x2 = random(-40, 460)
        square_x3 = random(-40, 460)
        square_x4 = random(-40, 460)
        square_x5 = random(-40, 460)
        square_x6 = random(-40, 460)
        
        score = "0" #reset score to zero
        
        game_over = "" #reset to empty string so game over screen disappears
        game_opening = "" #empty string so title screen does not appear
        
        speed_increase = 0 #reset additional speed back to 0
        level = "1" #reset level back to 1
        level_colour = color(254, 221, 0) #reset the colour back to yellow for level 1
        
        
    if key == BACKSPACE:
        
        global game_opening
        
        game_opening = "AVOID" #reset variable to title message on starting screen; title screen initiates
