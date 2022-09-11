input.onButtonPressed(Button.A, function () {
    สุ่มคำตอบ()
})
function สุ่มคำตอบ () {
    if (randint(0, 1) == 0) {
        basic.showString("Y")
    } else {
        basic.showString("N")
    }
}
input.onButtonPressed(Button.B, function () {
    สุ่มคำตอบ()
})
basic.forever(function () {
    basic.showIcon(IconNames.SmallDiamond)
    basic.showIcon(IconNames.Diamond)
})
