class Python_Switch:
    def day(self, month):

        default = "Incorrect day"

        return getattr(self, 'case_' + str(month), lambda: default)()

    def case_1(self):
        return "Jan"

    def case_2(self):
        return "Feb"

    def case_3(self):
        return "October, my birthday"


my_switch = Python_Switch()

print(my_switch.day(1))

print(my_switch.day(3))
