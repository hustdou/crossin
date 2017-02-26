# coding: utf-8
class medal_table(object):
    def __init__(self,country,gold = 0,silver = 0,bronze = 0):
        self.country = country
        self.gold = gold
        self.silver = silver
        self.bronze = bronze
    def increase(self,ingold = 0,insilver = 0,inbronze = 0):
        self.gold += ingold
        self.silver += insilver
        self.bronze += inbronze
    def medalsum(self):
        return self.gold + self.silver + self.bronze
    def information(self):
        return '%s: gold %d, silver %d, bronze %d, sum %d' % (self.country, self.gold, self.silver, self.bronze, self.medalsum())
China = medal_table('China',10,10,10)
US = medal_table('US',9,9,9)
Russia = medal_table('Russia',8,8,8)
China.increase(insilver = 2)
medal_table_list = [China, US, Russia]
print("按金牌数排序：")
order_by_count = sorted(medal_table_list, key=lambda x:x.gold, reverse=True)
for g in order_by_count:
    print(g.information())