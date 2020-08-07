## Given a position, write a function to
## find if that position is within 5 points of a monster:
a_treasure_map = {
  "45,46": "sea monster",
  "55,38": "air monster",
  "33,78": "lava monster",
  "22,23": "shining castle",
  "64,97": "shield of truth",
  "97,3": "sword of power",
}

def near_monster(position, a_treasure_map):

  x,y = position.split(",")
  playerX = int(x)
  playerY = int(y)
  for key, value in a_treasure_map.items():
    if value.endswith('monster'):
      monsterX, monsterY = map(int, key.split(","))
      distance = ((monsterX - playerX)**2 + (monsterY - playerY)**2)**0.5
      if distance <= 5:
        return True
  
  return False

print(near_monster("44,48", a_treasure_map))
print(near_monster("3,7", a_treasure_map))

## Given your current position, are you closer to the secret gem, 
## or the hidden springs? Write a function that returns the closest treasure to you

a_treasure_map = {
  "38.2859417,-122.3599983": "secret_gem",
  "34.3183327,-118.1399376": "hidden_springs"
}

def closest_treasure(position,a_treasure_map):
  positionX, positionY = map(float, position.split(","))
  min_distance = 1000000
  min_value = ""
  for key, value in a_treasure_map.items():
    treasureX, treasureY = map(float, key.split(","))
    distance = ((treasureX - positionX)**2 + (treasureY - positionY)**2)**0.5
    if distance < min_distance:
      min_distance = distance
      min_value = value
  
  return min_value

print(closest_treasure("5,6", a_treasure_map))
print(closest_treasure("36,-122", a_treasure_map))
