from pynput.mouse import Button, Controller

mouse = Controller()

for i in range(400):
    mouse.position = (i, i)

mouse.position = (31, 15)
mouse.click(Button.left, 1)
mouse.position = (31, 35)
mouse.click(Button.left, 1)