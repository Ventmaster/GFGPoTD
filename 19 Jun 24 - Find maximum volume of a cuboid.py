# 19 June 2024
# Find maximum volume of a cuboid

class Solution:
    def maxVolume(self, perimeter, area):
        #code here
        length = (perimeter - math.sqrt(perimeter * perimeter - 24 * area)) / 12
        height = (perimeter / 4) - (2 * length)
        volume = length * length * height
        
        return volume
