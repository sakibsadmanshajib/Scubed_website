from django.db import models

class Screen(models.Model):

    diagonal_size = models.FloatField()
    category = models.CharField(max_length=200)
    resolution = models.CharField(max_length=200)

    def __str__(self):
        return str(self.diagonal_size) + r'"' + " " + self.resolution + " " + self.category

class LaptopModel(models.Model):

    brand = models.CharField(max_length=200)
    series = models.CharField(max_length=200)
    model = models.CharField(max_length=200)
    screen = models.ForeignKey(Screen, on_delete=models.CASCADE)

    def __str__(self):
        return self.brand + " " + self.series + " " + self.model

class CPU(models.Model):

    brand = models.CharField(max_length=200)
    category = models.CharField(max_length=200)
    model = models.CharField(max_length=200)
    base_clock = models.FloatField()
    boost_clock = models.FloatField()
    cache_size = models.FloatField()
    no_of_core = models.IntegerField()
    is_HyperThreaded = models.BooleanField()


    def __str__(self):
        return self.brand + " " + self.category + " " + self.model + " (" + str(self.cache_size) + "M cache, upto " + str(self.boost_clock) + "GHz)"

class RAM(models.Model):
    capacity = models.IntegerField()
    category = models.CharField(max_length=200)

    def __str__(self):
        return str(self.capacity) + " GB " + self.category

class Storage(models.Model):
    hdd_capacity = models.IntegerField()
    ssd_capacity = models.IntegerField()
    ssd_category = models.CharField(max_length=200)
    cache_size = models.IntegerField()

    def __str__(self):

        s = ""

        if(self.ssd_capacity != 0):
            s += str(self.ssd_capacity) + " GB " + self.ssd_category + " SSD"
            if(self.cache_size !=0):
                s += " + " + str(self.cache_size) + " GB cache + " + str(self.hdd_capacity) + " GB HDD"
            else:
                s += " + " + str(self.hdd_capacity) + " GB HDD"
        else:
            if(self.cache_size !=0):
                s += " + " + str(self.cache_size) + " GB cache + " + str(self.hdd_capacity) + " GB HDD"
            else:
                s += " + " + str(self.hdd_capacity) + " GB HDD"

        return s

class GPU(models.Model):
    brand = models.CharField(max_length=200)
    chipset = models.CharField(max_length=200)
    vram_size = models.CharField(max_length=200)
    vram_type = models.CharField(max_length=200)

    def __str__(self):
        return self.brand + " " + self.chipset + " " + self.vram_size + " " + self.vram_type

class Laptop(models.Model):
    model = models.ForeignKey(LaptopModel, on_delete=models.CASCADE)
    cpu = models.ForeignKey(CPU, on_delete=models.CASCADE)
    ram = models.ForeignKey(RAM, on_delete=models.CASCADE)
    storage = models.ForeignKey(Storage, on_delete=models.CASCADE)
    gpu = models.ForeignKey(GPU, on_delete=models.CASCADE)
    price = models.FloatField()
    rating = models.FloatField()
    counter = models.IntegerField()

    def __str__(self):
        return self.model.__str__() + " " + self.cpu.__str__() + " " + self.ram.__str__() + " " + self.gpu.__str__() + " " + str(self.price)