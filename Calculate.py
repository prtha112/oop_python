class Tax:
  taxrate = 0.07

  def __init__(self, productprice, taxrate=None):
    self.productprice = productprice
    if taxrate is None:
      self.taxrate = Tax.taxrate
    else:
      self.taxrate = taxrate

  def caltax(self):
    return self.taxrate * self.productprice
