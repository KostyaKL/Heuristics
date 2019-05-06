class TableOfPhones:
    num_of_specs = 29
    num_of_phones = 9601

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

    def __init__(self, db, config):
        i = 0
        for brand in db:
            if brand != "time_stamp":
                for model in db[brand]["models"]:
                    self.candidate_dict[i] = {"brand": brand, "model": model, "rank": 0}
                    i += 1
        for i in range(0, 29):
            self.criteria_weight.append(config[i+1]["Weight"])
        self.build_table(db, config)

    def build_table(self, db, config):
        for i in range(0, self.num_of_specs):
            criteria = []
            for j in range(0, self.num_of_phones):
                spec_value = db[self.candidate_dict[j]["brand"]]["models"][self.candidate_dict[j]["model"]]["specs"][
                    self.specs_dict[i]]
                criteria.append(self.spec_grade(i+1, spec_value, config))
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
            if opt_range * 0.90 < int(spec_value) <= opt_range * 1.10:
                return 5
            elif opt_range * 0.80 < int(spec_value) <= opt_range * 0.90 or opt_range * 1.10 < int(spec_value) <= opt_range * 1.20:
                return 4
            elif opt_range * 0.70 < int(spec_value) <= opt_range * 0.80 or opt_range * 1.20 < int(spec_value) <= opt_range * 1.30:
                return 3
            elif opt_range * 0.60 < int(spec_value) <= opt_range * 0.70 or opt_range * 1.30 < int(spec_value) <= opt_range * 1.40:
                return 2
            elif int(spec_value) <= opt_range * 0.60 or opt_range * 1.40 < int(spec_value):
                return 1
            else:
                return 1
        except:
            return 1

    @staticmethod
    def lowest_better_grade(spec_value):
        try:
            if spec_value == 0:
                return 1
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

    def spec_grade(self, spec, spec_value, config):
        if config[spec]["Rule"] == "Highest Better":
            return self.highest_better_grade(spec_value)
        elif config[spec]["Rule"] == "Lowest Better":
            return self.lowest_better_grade(spec_value)
        elif config[spec]["Rule"] == "Optimal Value":
            return self.optimal_range_grade(spec_value, config[spec]["Value"])
        elif config[spec]["Rule"] == "Boolean":
            if config[spec]["Value"] == "Yes":
                return self.boolean_grade(spec_value, True)
            else:
                return self.boolean_grade(spec_value, False)
        elif config[spec]["Rule"] == "Constant Scale":
            return self.constant_range_grade(spec_value, config[spec]["Value"])
        else:
            return self.not_important_grade()

