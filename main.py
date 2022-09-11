def on_button_pressed_a():
    สุ่มคำตอบ()
input.on_button_pressed(Button.A, on_button_pressed_a)

def สุ่มคำตอบ():
    if randint(0, 1) == 0:
        basic.show_string("Y")
    else:
        basic.show_string("N")

def on_button_pressed_b():
    สุ่มคำตอบ()
input.on_button_pressed(Button.B, on_button_pressed_b)

def on_forever():
    basic.show_icon(IconNames.SMALL_DIAMOND)
    basic.show_icon(IconNames.DIAMOND)
basic.forever(on_forever)
