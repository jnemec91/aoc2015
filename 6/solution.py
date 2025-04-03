from collections import Counter
import re

class LightMap:
    """Map of christmas lights on your house"""
    def __init__(self, size:int) -> None:
        self.lights = [[0 for j in range(size)] for i in range(size)]
    
    def light_up_rect(self, x1:int,x2:int,y1:int,y2:int,toggle:bool=False) -> None:
        """
        lights up some bulbs on your light map, if toggle parameter is True,
        then toggles between on and off
        """
        for i in range(x1,x2+1):
            for j in range(y1,y2+1):
                if toggle:
                    self.lights[i][j] += 2
                else:
                    self.lights[i][j] += 1

    def switch_off_rect(self, x1:int,x2:int,y1:int,y2:int) -> None:
        """switches of some bulbs on your light map"""
        for i in range(x1,x2+1):
            for j in range(y1,y2+1):
                if self.lights[i][j] > 0:
                    self.lights[i][j] -= 1

    def get_total_brightness(self) -> int:
        """counts all lights that are on at the moment"""
        counter = 0
        for line in self.lights:
            for light in line:
                if light > 0:
                    counter += light
        return counter

if __name__ == '__main__':
    lm = LightMap(1000)

    with open("input.txt", encoding="utf-8") as f:
        inp = f.readlines()
        current_instruction = 0
        for line in inp:
            current_instruction += 1
            coordinates = re.findall(r'(\d+)', line)
            x1 = int(coordinates[0])
            y1 = int(coordinates[1])
            x2 = int(coordinates[2])
            y2 = int(coordinates[3])
            if "on" in line:
                lm.light_up_rect(x1,x2,y1,y2)
            elif "toggle" in line:
                lm.light_up_rect(x1,x2,y1,y2, toggle=True)
            elif "off" in line:
                lm.switch_off_rect(x1,x2,y1,y2)
            print(f'instruction {current_instruction}-{line}: coordinates: {(x1,x2)}, {(y1,y2)}\n')


        print(f'Part 2: {lm.get_total_brightness()}')