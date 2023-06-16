class Cat():
  name = ""
  age = 1
  sleep = False
  hungry = 40
  happy = 40
  avatar = 'images/logo.png'

  def feed(self):
       self.hungry = min(self.hungry + 15, 100)
       self.happy = min(self.happy + 5, 100)
       if self.hungry > 100:
            self.happy = max(self.happy - 30)
       self.save()

  def play(self):
       self.happy = min(self.happy + 15, 100)
       self.hungry = max(self.hungry - 10, 0)
       if self.happy == 0:
            self.hungry = 0
       self.save()

  def sleep(self):
        self.happy -= 5
        self.save()

  def sleeping(self):
        return self.happy == 0

  def avatar(self):
        if self.happy >= 30:
            return 'images/logo.png'
        elif self.happy <= 70:
            return 'images/cat3.png'
        else:
            return 'images/cat2.png'