import numpy as np


#Create map 5x5
map = np.random.randint(1, 10, size=(5,5))

#Hide treasure
while True:
    treasure_row, treasure_col = np.random.randint(0,5,size=2)
    if(treasure_row, treasure_col) != (0,0):
        break

#Define start position and points
player_position = (0,0)
points = 0 

# Main loop 

while True:
    map_with_player = np.copy(map)
    map_with_player[player_position] = 0
    print(map_with_player)
    
    
    #Choose move
    direction = input("Type the number of the direction you want to move:\n\n1- Up\n2- Down\n3- Left\n4- Right\n\nChoice:")

    if(direction == '1'):
        new_position=(player_position[0]-1,player_position[1])
        
    elif(direction == '2'):
        new_position=(player_position[0]+1,player_position[1])
        
    elif(direction == '3'):
        new_position=(player_position[0],player_position[1]-1)
        
    elif(direction == '4'):
        new_position=(player_position[0],player_position[1]+1)
        
        
    # Check position
    if (new_position[0] < 0 or new_position[0]>= map.shape[0] or new_position [1]>= map.shape[1] or new_position[1] < 0):
        print('Invalid position.')
        continue

    #Update position
    player_position = new_position
    points +=1

    # Player found treasure 
    if player_position == (treasure_row,treasure_col): break

print('\n\n ===== CONGRATS! You found the treasure =====')
print(f'Total points:{points}')
print(f'The treasure was at {[treasure_row, treasure_col]}')


