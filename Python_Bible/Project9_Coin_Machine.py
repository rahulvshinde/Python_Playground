import random


class Coin:
    def __init__(self, rare=False, clean=True, heads=True, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)

        self.is_rare = rare
        self.is_clean = clean
        self.is_heads = heads

        if self.is_rare:
            self.value = self.original_value * 1.25
        else:
            self.value = self.original_value

        if self.is_clean:
            self.color = self.clean_color
        else:
            self.color = self.rustly_color

    def rust(self):
        self.color = self.rusty_color

    def clean(self):
        self.color = self.clean_color

    def flip(self):
        heads_options = [True, False]
        choice = random.choice(heads_options)
        self.heads = choice

    def __str__(self):
        if self.original_value>=1:
            return "${} coin".format(int(self.original_value))
        else:
            return "{}p coin".format(int(self.original_value * 100))

    def __del__(self):
        print("Coin Spent!")


class OnePence(Coin):
    def __init__(self):
        data = {
            "original_value": 0.01,
            "clean_color": "bronze",
            "rusty_color": "brownish",
            "num_edges": 1,
            "diameter": 20.3,
            "thickness": 1.52,
            "mass": 3.56
        }
        super().__init__(**data)


class TwoPence(Coin):
    def __init__(self):
        data = {
            "original_value": 0.02,
            "clean_color": "bronze",
            "rusty_color": "brownish",
            "num_edges": 1,
            "diameter": 25.9,
            "thickness": 1.85,
            "mass": 7.12
        }
        super().__init__(**data)


class FivePence(Coin):
    def __init__(self):
        data = {
            "original_value": 0.05,
            "clean_color": "silver",
            "rusty_color": None,
            "num_edges": 1,
            "diameter": 18.0,
            "thickness": 1.77,
            "mass": 3.25
        }
        super().__init__(**data)

    def rust(self):
        self.color = self.clean_color

    def clean(self):
        self.color = self.clean_color


class TenPence(Coin):
    def __init__(self):
        data = {
            "original_value": 0.10,
            "clean_color": "silver",
            "rusty_color": None,
            "num_edges": 1,
            "diameter": 24.5,
            "thickness": 1.86,
            "mass": 6.50
        }
        super().__init__(**data)

    def rust(self):
        self.color = self.clean_color

    def clean(self):
        self.color = self.clean_color


class TwentyPence(Coin):
    def __init__(self):
        data = {
            "original_value": 0.20,
            "clean_color": "silver",
            "rusty_color": None,
            "num_edges": 1,
            "diameter": 21.5,
            "thickness": 1.7,
            "mass": 5.00
        }
        super().__init__(**data)

    def rust(self):
        self.color = self.clean_color

    def clean(self):
        self.color = self.clean_color


class FiftyPence(Coin):
    def __init__(self):
        data = {
            "original_value": 0.50,
            "clean_color": "silver",
            "rusty_color": None,
            "num_edges": 7,
            "diameter": 28.5,
            "thickness": 3.7,
            "mass": 9.00
        }
        super().__init__(**data)

    def rust(self):
        self.color = self.clean_color

    def clean(self):
        self.color = self.clean_color


class OnePound(Coin):
    def __init__(self):
        data = {
            "original_value": 1.00,
            "clean_color": "gold",
            "rusty_color": "greenish",
            "num_edges": 1,
            "diameter": 22.5,
            "thickness": 3.15,
            "mass": 9.5
        }
        super().__init__(**data)


class TwoPound(Coin):
    def __init__(self):
        data = {
            "original_value": 2.00,
            "clean_color": "gold & silver",
            "rusty_color": "greenish",
            "num_edges": 1,
            "diameter": 28.9,
            "thickness": 2.85,
            "mass": 12.00
        }
        super().__init__(**data)


coins = [OnePence(), TwoPence(), FivePence(), TenPence(), TwentyPence(), FiftyPence(), OnePound(), TwoPound()]
for coin in coins:
    arguments = [coin, coin.color, coin.value, coin.diameter, coin.thickness, coin.num_edges, coin.mass]
    string = "{} - Color: {}, Value: {}, Diameter(mm): {}, Thickness(mm): {}, Num of Edges: {}, Mass: {}".format(*arguments)
    print(string)
