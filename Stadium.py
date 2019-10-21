class Stadium:

    def __init__(self, power_lighting, number_viewers, name):
        self.power_lighting = power_lighting
        self.number_viewers = number_viewers
        self.name = name

    def __str__(self):
        return str(self.power_lighting) + ' ' \
               + str(self.number_viewers) + ' ' \
               + self.name
