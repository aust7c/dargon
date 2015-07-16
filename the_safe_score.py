__author__ = 'guoqingchen'
points = int(raw_input("Leading points:"))
has_ball = raw_input("The leading team has ball (yes/no)")
seconds = int(raw_input("The remaining seconds:"))

points -= 3

if has_ball == "yes":
    points += 0.5
else:
    points -= 0.5

if points < 0:
    points = 0

points **= 2

if points > seconds:
    print  "safe"
else:
    print  "no"


