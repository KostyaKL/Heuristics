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

    def __init__(self, db, target):
        i = 0
        for brand in db:
            for model in db[brand]["models"]:
                self.candidate_dict[i] = {"brand": brand, "model": model}
                i += 1
        if target == "kids":
            self.criteria_weight = [5,4,3,3,4,1,1,5,5,5,4,2,4,4,4,4,4,4,2,1,1,1,2,5,3,5,5,5,4]
            self.build_table(db, "kids")
        elif target == "hightech":
            self.criteria_weight = [5,5,3,3,4,4,3,4,5,4,4,5,5,5,5,5,5,5,2,1,3,3,4,5,4,1,2,5,4]
            self.build_table(db, "hightech")
        elif target == "pensioners":
            self.criteria_weight = [5,2,4,4,4,1,1,5,3,1,1,5,5,1,4,4,4,4,4,5,4,2,1,5,1,5,5,5,3]
            self.build_table(db, "pensioners")

    def build_table(self, db, target):
        for i in range(0, self.num_of_specs):
            criteria = []
            for j in range(0, self.num_of_phones):
                spec_value = db[self.candidate_dict[j]["brand"]]["models"][self.candidate_dict[j]["model"]]["specs"][self.specs_dict[i]]
                criteria.append(self.spec_grade(self.specs_dict[i], spec_value, target))
            self.table.append(criteria)

    @staticmethod
    def grade_type(type_of_grade, spec_value, opt_range, bool_type, sim_grade, os_grade, usb_grade):
        if type_of_grade == "highest_better":
            return spec_value
        elif type_of_grade == "optimal_range":
            if opt_range * 0.95 < spec_value <= opt_range * 1.05:
                return 5
            elif opt_range * 0.90 < spec_value <= opt_range * 0.95 or opt_range * 1.05 < spec_value <= opt_range * 1.10:
                return 4
            elif opt_range * 0.85 < spec_value <= opt_range * 0.90 or opt_range * 1.10 < spec_value <= opt_range * 1.15:
                return 3
            elif opt_range * 0.80 < spec_value <= opt_range * 0.85 or opt_range * 1.15 < spec_value <= opt_range * 1.20:
                return 2
            elif spec_value <= opt_range * 0.80 or opt_range * 1.20 < spec_value:
                return 1
            else:
                return 0
        elif type_of_grade == "lowest_better":
            return 1000000-spec_value
        elif type_of_grade == "not_important":
            return 0
        elif type_of_grade == "boolean":
            if bool_type is True:
                return spec_value
            else:
                if spec_value == 1:
                    return 0
                else:
                    return 1
        elif type_of_grade == "sim":
            return sim_grade[spec_value]
        elif type_of_grade == "os":
            return os_grade[spec_value]
        elif type_of_grade == "usb":
            return usb_grade[spec_value]
        else:
            return 0

    def spec_grade(self, spec, spec_value, target):
        if spec == "battery":
            if target == "kids":
                return self.grade_type("highest_better", spec_value, 0, True, [], [], [])
            elif target == "hightech":
                return self.grade_type("highest_better", spec_value, 0, True, [], [], [])
            elif target == "pensioners":
                return self.grade_type("highest_better", spec_value, 0, True, [], [], [])
            else:
                return 0
        elif spec == "year":
            return spec_value
        elif spec == "height":
            return spec_value
        elif spec == "width":
            return spec_value
        elif spec == "weight":
            return spec_value
        elif spec == "numofsim":
            return spec_value
        elif spec == "simtype":
            return spec_value
        elif spec == "displaysize":
            return spec_value
        elif spec == "displayresolution":
            return spec_value
        elif spec == "os":
            return spec_value
        elif spec == "cpu":
            return spec_value
        elif spec == "memoryslot":
            return spec_value
        elif spec == "maxextmemory":
            return spec_value
        elif spec == "RAM":
            return spec_value
        elif spec == "cam1MP":
            return spec_value
        elif spec == "cam1video":
            return spec_value
        elif spec == "cam2MP":
            return spec_value
        elif spec == "cam2video":
            return spec_value
        elif spec == "ir":
            return spec_value
        elif spec == "radio":
            return spec_value
        elif spec == "usb":
            return spec_value
        elif spec == "nfc":
            return spec_value
        elif spec == "fingerprint":
            return spec_value
        elif spec == "price":
            return spec_value
        elif spec == "basemark":
            return spec_value
        elif spec == "loudspeaker":
            return spec_value
        elif spec == "audioquality":
            return spec_value
        elif spec == "endurance":
            return spec_value
        elif spec == "waterproof":
            return spec_value
        else:
            return 0
