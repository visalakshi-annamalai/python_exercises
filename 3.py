'''
Name:visalakshi annamalai
date:12-12-17
Description:currency converter

'''
class money:
  def __init__(self,dollars,cents):
    self.dollars=dollars
    self.cents=cents
  def repre(self):
    print "$",self.dollars,".",self.cents
  def add(self,dollars,cents):
    dollars=self.dollars+dollars
    cents=self.cents+cents
    if cents>100:
      dollars=dollars+1
      cents=cents%100
    print "$",dollars,".",cents
  def dollar_yen(self):
    '''this methods converts dollars to yen'''
    dollars=self.dollars*113.50
    cents=self.cents*1.135
    print "yen",dollars+cents
dollars=int(raw_input("dollars"))
cents=int(raw_input("cents"))
a=money(dollars,cents)
a.repre()
a.add(1,70)
a.dollar_yen()
