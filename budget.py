class Category:

  def __init__(self, name):
    self.name = name
    self.ledger = []

  def __str__(self):
    title = f"{self.name:*^30}\n"
    items = ""
    total = 0
    for item in self.ledger:
      items += f"{item['description'][0:23]:23}{item['amount']:>7.2f}\n"
      total += item['amount']
    return f'{title+items}Total: {str(total)}'

  def deposit(self, amount: float, description: str = ''):
    self.ledger.append({"amount": amount, "description": description})

  def withdraw(self, amount: float, description: str = ''):
    if self.check_funds(amount=amount):
      self.ledger.append({"amount": -1 * amount, "description": description})
      return True
    else:
      return False

  def get_balance(self):
    return sum([entry.get('amount', 0) for entry in self.ledger])

  def transfer(self, amount, other_category):
    if self.check_funds(amount):
      self.withdraw(amount, description=f"Transfer to {other_category.name}")
      other_category.deposit(amount, description=f"Transfer from {self.name}")
      return True
    else:
      return False

  def check_funds(self, amount: float) -> bool:
    balance = self.get_balance()
    if amount > balance:
      return False
    else:
      return True

  def get_withdrawals(self):
    return sum([
      item.get('amount', 0) for item in self.ledger
      if item.get('amount', 0) > 0
    ])


def truncate(n):
  return int(n * 10) / 10


def get_totals(categories):
  total = 0
  breakdown = []
  for category in categories:
    withdrawals = category.get_withdrawals()
    total += withdrawals
    breakdown.append(withdrawals)
  return list(map(lambda x: truncate(x / total), breakdown))


def create_spend_chart(categories):
  res = "Percentage spent by category\n"
  i = 100
  totals = get_totals(categories)
  while i >= 0:
    category_spaces = " "
    for total in totals:
      if total * 100 >= i:
        category_spaces += "o  "
      else:
        category_spaces += "   "
    res += str(i).rjust(3) + "|" + category_spaces + ("\n")
    i -= 10

  dashes = "-" + "---" * len(categories)
  names = []
  for category in categories:
    names.append(category.name)

  x_axis = ""

  maximum = max(names, key=len)
  for x in range(len(maximum)):
    nameStr = '     '
    for name in names:
      if x >= len(name):
        nameStr += "   "
      else:
        nameStr += name[x] + "  "
        
    if (x != len(maximum) - 1):
      nameStr += '\n'

    x_axis += nameStr

  res += dashes.rjust(len(dashes) + 4) + "\n" + x_axis
  return res
