import time
enter1 = input('please enter your name: ')
enter2 = int(input('please enter your age: '))
while not int(enter2) in range(0, 100):
    enter2 = int(input('that\'s not a valid age, please try that again: '))

print('hello ' + enter1 + ' and welcome to pydoc, your bot for quick and concise medical checkup')
time.sleep(3)
enter3 = float(input('enter your height (in meters): '))
while float(enter3) > 2.0:
    enter3 = float(input('please enter a valid parameter: '))
enter4 = float(input('enter your weight (in kg): '))
# while float(enter4) < 4:
#     enter4 = float(input('please enter a valid parameter: '))
bmi = enter4/(enter3**2)
print('now use your left hand thumb to palpate  around your right hand wrist till you can feel your pulse')
time.sleep(5)
print('note down how many pulses you can feel from when the counter counts to 0 till when the ellipsis appears')
time.sleep(5)
print(3)
time.sleep(1)
print(2)
time.sleep(1)
print(1)
time.sleep(1)
print(0)
time.sleep(15)
print('...')
enter6 = int(input('enter the number of pulses: '))
time.sleep(3)
heartbeat =  enter6*4
print(f"your heartbeat is {heartbeat}bpm")
print(f"your body mass index is {round(bmi, 1)}kg/m2")
time.sleep(3)
print('...')
if 60 <= heartbeat <= 100 and 18.5 <= round(bmi, 1) <= 24.9:
    print(f"you're a healthy one and that's rare! stay fit champ")
elif 60 > heartbeat or 100 < heartbeat:
    print(f"that's somewhat off :( you might want to start  some aerobic exercises, running is my personal favourite")
elif 18.5 > round(bmi, 1) or 24.9 < round(bmi, 1):
    print(f"you might want to go on a diet :P calories are what increase/decrease body fat(you're welcome)")

print(f"goodbye! :)")



