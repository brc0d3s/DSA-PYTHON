class cookie:
    def __init__(self,color):
        self.color = color

    def get_color(self):
        return self.color
    
    def set_color(self,color):
        self.color = color

cookie_one = cookie("Green")
cookie_two = cookie("Blue")

print(f"Cookie one is {cookie_one.get_color()}")
print(f"Cookie two is {cookie_one.get_color()}")

cookie_one.set_color("Pink")

print(f"\n\nCookie one is now {cookie_one.get_color()}")
print(f"Cookie two is still {cookie_one.get_color()}")


