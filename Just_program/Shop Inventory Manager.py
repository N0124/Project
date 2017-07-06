
class Item:
    def __init__(self,name, sell_in, quality):
        self.name=name
        self.sell_in=sell_in
        self.quality=quality
    def __str__(self):
        return str(self.name)+','+str(self.sell_in)+','+str(self.quality)

items=[]

items+=[Item('+5 Dexterity Vest', 10, 20)]
items+=[Item('Aged Brie', 2, 0)]
items+=[Item('Elixir of the Mongoose', 5, 7)]
items+=[Item('Sulfuras, Hand of Ragnaros', 0, 80)]
items+=[Item('Backstage passes to a TAFKAL80ETC concert', 15, 20)]
items+=[Item('Conjured Mana Cake', 3, 6)]

def update_quality():
    for i in range(len(items)):
        if 'sulfuras' not in items[i].name.lower():
            items[i].sell_in= items[i].sell_in - 1
            if 'backstage passes' in items[i].name.lower():
                if items[i].quality >= 50:
                    pass
                else:
                    if 5 < items[i].sell_in < 11:
                        items[i].quality = items[i].quality + 2
                    elif 0 < items[i].sell_in < 6:
                        items[i].quality = items[i].quality + 3
                    elif items[i].sell_in <=0:
                        items[i].quality = 0
                    else:
                        items[i].quality = items[i].quality + 1
                    if items[i].quality > 50:
                        items[i].quality = 50



            elif 'aged brie' in items[i].name.lower():
                if items[i].quality >= 50:
                    pass
                else:
                    items[i].quality = items[i].quality + 1
            else:
                degrade = 1
                if 'conjured' in items[i].name.lower():
                    degrade*=2
                if items[i].sell_in >=0:
                   items[i].quality = items[i].quality-degrade
                else:
                    items[i].quality = items[i].quality -degrade*2


            if items[i].quality <0:
                items[i].quality = 0


