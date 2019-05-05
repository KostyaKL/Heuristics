class TableOfPhones:
    num_of_specs = 29
    num_of_phones = 9000

    table = []  # each row is criteria, each column is phone
    criteria_weight = []
    candidate_dict = {}
    specs_dict = {
        0: "battery",
        1: "year",
        2: "height",
        3: "width",
        4: "weight",
        5: "numofsim",
        6: "simtype",
        7: "displaysize",
        8: "displayresolution",
        9: "os",
        10: "cpu",
        11: "memoryslot",
        12: "maxextmemory",
        13: "RAM",
        14: "cam1MP",
        15: "cam1video",
        16: "cam2MP",
        17: "cam2video",
        18: "ir",
        19: "radio",
        20: "usb",
        21: "nfc",
        22: "fingerprint",
        23: "price",
        24: "basemark",
        25: "loudspeaker",
        26: "audioquality",
        27: "endurance",
        28: "waterproof"
    }

    rule_dict = []

    def __init__(self, db, target):
        i = 0
        for brand in db:
            for model in db[brand]["models"]:
                self.candidate_dict[i] = {"brand": brand, "model": model, "rank": 0}
                i += 1
        if target == "Children":
            self.criteria_weight = [5, 4, 3, 3, 4, 1, 1, 5, 5, 5, 4, 2, 4, 4, 4, 4, 4, 4, 2, 1, 1, 1, 2, 5, 3, 5, 5, 5,
                                    4]
            self.build_table(db, "Children")
        elif target == "Hi-Tech Employee":
            self.criteria_weight = [5, 5, 3, 3, 4, 4, 3, 4, 5, 4, 4, 5, 5, 5, 5, 5, 5, 5, 2, 1, 3, 3, 4, 5, 4, 1, 2, 5,
                                    4]
            self.build_table(db, "Hi-Tech Employee")
        elif target == "Pensioners":
            self.criteria_weight = [5, 2, 4, 4, 4, 1, 1, 5, 3, 1, 1, 5, 5, 1, 4, 4, 4, 4, 4, 5, 4, 2, 1, 5, 1, 5, 5, 5,
                                    3]
            self.build_table(db, "Pensioners")

    def build_table(self, db, target):
        for i in range(0, self.num_of_specs):
            criteria = []
            for j in range(0, self.num_of_phones):
                spec_value = db[self.candidate_dict[j]["brand"]]["models"][self.candidate_dict[j]["model"]]["specs"][
                    self.specs_dict[i]]
                criteria.append(self.spec_grade(self.specs_dict[i], spec_value, target))
            self.table.append(criteria)

    @staticmethod
    def highest_better_grade(spec_value):
        try:
            return int(spec_value)
        except:
            return 1

    @staticmethod
    def optimal_range_grade(spec_value, opt_range):
        try:
            if opt_range * 0.95 < int(spec_value) <= opt_range * 1.05:
                return 5
            elif opt_range * 0.90 < int(spec_value) <= opt_range * 0.95 or opt_range * 1.05 < int(spec_value) <= opt_range * 1.10:
                return 4
            elif opt_range * 0.85 < int(spec_value) <= opt_range * 0.90 or opt_range * 1.10 < int(spec_value) <= opt_range * 1.15:
                return 3
            elif opt_range * 0.80 < int(spec_value) <= opt_range * 0.85 or opt_range * 1.15 < int(spec_value) <= opt_range * 1.20:
                return 2
            elif int(spec_value) <= opt_range * 0.80 or opt_range * 1.20 < int(spec_value):
                return 1
            else:
                return 1
        except:
            return 1

    @staticmethod
    def lowest_better_grade(spec_value):
        try:
            return 10000000 - int(spec_value)
        except:
            return 1

    @staticmethod
    def not_important_grade():
        return 1

    @staticmethod
    def boolean_grade(spec_value, bool_type):
        if bool_type is True:
            if spec_value == 1:
                return 10
            else:
                return 1
        else:
            if spec_value == 1:
                return 1
            else:
                return 10

    @staticmethod
    def constant_range_grade(spec_value, grade):
        if spec_value - 1 < 0 or spec_value > len(grade):
            return 1
        return grade[spec_value - 1]

    def spec_grade(self, spec, spec_value, target):
        if spec == "battery":
            if target == "Children":
                return self.highest_better_grade(spec_value)
            elif target == "Hi-Tech Employee":
                return self.highest_better_grade(spec_value)
            elif target == "Pensioners":
                return self.highest_better_grade(spec_value)
            else:
                return 1
        elif spec == "year":
            if target == "Children":
                return self.highest_better_grade(spec_value)
            elif target == "Hi-Tech Employee":
                return self.highest_better_grade(spec_value)
            elif target == "Pensioners":
                return self.highest_better_grade(spec_value)
            else:
                return 1
        elif spec == "height":
            if target == "Children":
                return self.optimal_range_grade(spec_value, 145)
            elif target == "Hi-Tech Employee":
                return self.optimal_range_grade(spec_value, 150)
            elif target == "Pensioners":
                return self.optimal_range_grade(spec_value, 175)
            else:
                return 1
        elif spec == "width":
            if target == "Children":
                return self.optimal_range_grade(spec_value, 65)
            elif target == "Hi-Tech Employee":
                return self.optimal_range_grade(spec_value, 70)
            elif target == "Pensioners":
                return self.optimal_range_grade(spec_value, 85)
            else:
                return 1
        elif spec == "weight":
            if target == "Children":
                return self.lowest_better_grade(spec_value)
            elif target == "Hi-Tech Employee":
                return self.lowest_better_grade(spec_value)
            elif target == "Pensioners":
                return self.lowest_better_grade(spec_value)
            else:
                return 1
        elif spec == "numofsim":
            if target == "Children":
                return self.not_important_grade()
            elif target == "Hi-Tech Employee":
                return self.highest_better_grade(spec_value)
            elif target == "Pensioners":
                return self.not_important_grade()
            else:
                return 1
        elif spec == "simtype":
            if target == "Children":
                return self.not_important_grade()
            elif target == "Hi-Tech Employee":
                return self.constant_range_grade(spec_value, [1, 2, 3, 4])
            elif target == "Pensioners":
                return self.constant_range_grade(spec_value, [4, 3, 2, 1])
            else:
                return 1
        elif spec == "displaysize":
            if target == "Children":
                return self.optimal_range_grade(spec_value, 4.75)
            elif target == "Hi-Tech Employee":
                return self.optimal_range_grade(spec_value, 5.25)
            elif target == "Pensioners":
                return self.highest_better_grade(spec_value)
            else:
                return 1
        elif spec == "displayresolution":
            if target == "Children":
                return self.highest_better_grade(spec_value)
            elif target == "Hi-Tech Employee":
                return self.highest_better_grade(spec_value)
            elif target == "Pensioners":
                return self.highest_better_grade(spec_value)
            else:
                return 1
        elif spec == "os":
            if target == "Children":
                return self.constant_range_grade(spec_value, [6, 5, 4, 3, 1, 2])
            elif target == "Hi-Tech Employee":
                return self.constant_range_grade(spec_value, [6, 5, 3, 4, 1, 2])
            elif target == "Pensioners":
                return self.constant_range_grade(spec_value, [5, 6, 3, 4, 1, 2])
            else:
                return 1
        elif spec == "cpu":
            if target == "Children":
                return self.highest_better_grade(spec_value)
            elif target == "Hi-Tech Employee":
                return self.highest_better_grade(spec_value)
            elif target == "Pensioners":
                return self.highest_better_grade(spec_value)
            else:
                return 1
        elif spec == "memoryslot":
            if target == "Children":
                return self.not_important_grade()
            elif target == "Hi-Tech Employee":
                return self.boolean_grade(spec_value, True)
            elif target == "Pensioners":
                return self.boolean_grade(spec_value, True)
            else:
                return 1
        elif spec == "maxextmemory":
            if target == "Children":
                return self.highest_better_grade(spec_value)
            elif target == "Hi-Tech Employee":
                return self.highest_better_grade(spec_value)
            elif target == "Pensioners":
                return self.highest_better_grade(spec_value)
            else:
                return 1
        elif spec == "RAM":
            if target == "Children":
                return self.highest_better_grade(spec_value)
            elif target == "Hi-Tech Employee":
                return self.highest_better_grade(spec_value)
            elif target == "Pensioners":
                return self.highest_better_grade(spec_value)
            else:
                return 1
        elif spec == "cam1MP":
            if target == "Children":
                return self.highest_better_grade(spec_value)
            elif target == "Hi-Tech Employee":
                return self.highest_better_grade(spec_value)
            elif target == "Pensioners":
                return self.highest_better_grade(spec_value)
            else:
                return 1
        elif spec == "cam1video":
            if target == "Children":
                return self.highest_better_grade(spec_value)
            elif target == "Hi-Tech Employee":
                return self.highest_better_grade(spec_value)
            elif target == "Pensioners":
                return self.highest_better_grade(spec_value)
            else:
                return 1
        elif spec == "cam2MP":
            if target == "Children":
                return self.highest_better_grade(spec_value)
            elif target == "Hi-Tech Employee":
                return self.highest_better_grade(spec_value)
            elif target == "Pensioners":
                return self.highest_better_grade(spec_value)
            else:
                return 1
        elif spec == "cam2video":
            if target == "Children":
                return self.highest_better_grade(spec_value)
            elif target == "Hi-Tech Employee":
                return self.highest_better_grade(spec_value)
            elif target == "Pensioners":
                return self.highest_better_grade(spec_value)
            else:
                return 1
        elif spec == "ir":
            if target == "Children":
                return self.not_important_grade()
            elif target == "Hi-Tech Employee":
                return self.boolean_grade(spec_value, True)
            elif target == "Pensioners":
                return self.boolean_grade(spec_value, True)
            else:
                return 1
        elif spec == "radio":
            if target == "Children":
                return self.not_important_grade()
            elif target == "Hi-Tech Employee":
                return self.not_important_grade()
            elif target == "Pensioners":
                return self.boolean_grade(spec_value, True)
            else:
                return 1
        elif spec == "usb":
            if target == "Children":
                return self.constant_range_grade(spec_value, [3, 1, 2])
            elif target == "Hi-Tech Employee":
                return self.constant_range_grade(spec_value, [3, 1, 2])
            elif target == "Pensioners":
                return self.constant_range_grade(spec_value, [3, 1, 2])
            else:
                return 1
        elif spec == "nfc":
            if target == "Children":
                return self.boolean_grade(spec_value, True)
            elif target == "Hi-Tech Employee":
                return self.boolean_grade(spec_value, True)
            elif target == "Pensioners":
                return self.not_important_grade()
            else:
                return 1
        elif spec == "fingerprint":
            if target == "Children":
                return self.boolean_grade(spec_value, False)
            elif target == "Hi-Tech Employee":
                return self.boolean_grade(spec_value, True)
            elif target == "Pensioners":
                return self.boolean_grade(spec_value, False)
            else:
                return 1
        elif spec == "price":
            if target == "Children":
                return self.lowest_better_grade(spec_value)
            elif target == "Hi-Tech Employee":
                return self.lowest_better_grade(spec_value)
            elif target == "Pensioners":
                return self.lowest_better_grade(spec_value)
            else:
                return 1
        elif spec == "basemark":
            if target == "Children":
                return self.highest_better_grade(spec_value)
            elif target == "Hi-Tech Employee":
                return self.highest_better_grade(spec_value)
            elif target == "Pensioners":
                return self.not_important_grade()
            else:
                return 1
        elif spec == "loudspeaker":
            if target == "Children":
                return self.highest_better_grade(spec_value)
            elif target == "Hi-Tech Employee":
                return self.not_important_grade()
            elif target == "Pensioners":
                return self.highest_better_grade(spec_value)
            else:
                return 1
        elif spec == "audioquality":
            if target == "Children":
                return self.highest_better_grade(spec_value)
            elif target == "Hi-Tech Employee":
                return self.highest_better_grade(spec_value)
            elif target == "Pensioners":
                return self.highest_better_grade(spec_value)
            else:
                return 1
        elif spec == "endurance":
            if target == "Children":
                return self.highest_better_grade(spec_value)
            elif target == "Hi-Tech Employee":
                return self.highest_better_grade(spec_value)
            elif target == "Pensioners":
                return self.highest_better_grade(spec_value)
            else:
                return 1
        elif spec == "waterproof":
            if target == "Children":
                return self.boolean_grade(spec_value, True)
            elif target == "Hi-Tech Employee":
                return self.boolean_grade(spec_value, True)
            elif target == "Pensioners":
                return self.boolean_grade(spec_value, True)
            else:
                return 1
        else:
            return 1
