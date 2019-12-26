from clap_detector import TapTester


class Switch():
    def __init__(self):
        self.switch_state = False

    def change_switch_state(self):
        if self.switch_state:
            self.switch_state = False
        else:
            self.switch_state = True


tt = TapTester()
my_switch = Switch()

while True:
    if tt.double_clap_bool:
        my_switch.change_switch_state()
        tt.double_clap_bool = False
    tt.listen()
    print(my_switch.switch_state)

