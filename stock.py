class Stock:
  def __init__ (self, ticker, name, volume, change, changepct):
    self.ticker = ticker
    self.name = name
    self.volume = str(volume)
    self.change = str(change)
    self.changepct = str(changepct)

  def tickprint(self):
    stock_string = "**__" + self.ticker + " - " + self.name + "__**" +"\n" + " - Change today: $" + self.change + "\n" + " - Change %: "+ self.changepct + "%"
    return(stock_string)
