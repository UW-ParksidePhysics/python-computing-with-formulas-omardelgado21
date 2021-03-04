meters = 640 
cm_per_inch = 2.54
inches_per_foot = 12
feet_per_yards = 3
yards_per_meter = 1.094
yards_per_Britishmile = 1760
inches = inches_per_foot*feet_per_yards*yards_per_meter*meters
print(inches)
feet = feet_per_yards*yards_per_meter*meters
print(feet)
yards = yards_per_meter*meters
print(yards)
miles = meters/yards_per_meter/yards_per_Britishmile
print(miles)