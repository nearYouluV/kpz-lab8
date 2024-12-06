import math

class Equations:
    def calculate(self,x):
        rad = x * math.pi / 180.0
        try:
        #  y=(x-4)/sin(3x-1)
            y = x-4/(math.sin(3*x-1))
            if rad == math.pi or rad == (math.pi * 2):
                raise Exception
        except Exception as e:
            print("Exeption ",str(e))
            return 0
        return y

