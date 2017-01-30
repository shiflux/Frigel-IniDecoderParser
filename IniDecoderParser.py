### decoder = IniDecoderParser("~DIR~/FILEINI.ini", 1)
### decoder.ini_dict


class IniDecoderParser:
    def __init__(self, ini_file, family):
        self.ini_dict = dict()
        self.create_dict()
        self.family = family
        self.open_ini_file(ini_file)

    def open_ini_file(self, ini_file):
        with open(ini_file, 'r') as myFile:
            lines = myFile.readlines()
            for line in lines:
                self.decode_ini_line(line)

    def decode_ini_line(self, line):
        if line.startswith("AI"):
            splitted = line.split('=', 1)[1].split(',')
            code = "1:anin:" + splitted[0].strip()
            name = splitted[2].strip()
            unit = splitted[2].strip().strip('_')
            self.ini_dict["Analog"].append({"CODE": code, "FAMILY_ID": self.family, "UNIT": unit, "NAME": name})
        elif line.startswith("AO"):
            splitted = line.split('=', 1)[1].split(',')
            code = "1:anout:" + splitted[0].strip()
            name = splitted[2].strip()
            unit = splitted[2].strip().strip('_')
            self.ini_dict["Analog"].append({"CODE": code, "FAMILY_ID": self.family, "UNIT": unit, "NAME": name})
        elif line.startswith("CMD"):
            splitted = line.split('=', 1)[1].split(';')
            code = "1:command:" + splitted[0].strip()
            name = splitted[1].strip()
            self.ini_dict["Command"].append({"CODE": code, "FAMILY_ID": self.family, "NAME": name})
        elif line.startswith("EVN"):
            splitted = line.split('=', 1)[1].split(',')
            code = "1:alarm:" + splitted[0].strip()
            name = splitted[1].strip()
            self.ini_dict["Digital"].append({"CODE": code, "FAMILY_ID": self.family, "NAME": name})
        elif line.startswith("SETUP"):
            splitted = line.split('=', 1)[1].split(';')
            temp_s = splitted[0].strip()
            code = "1:setup:" + temp_s[temp_s.find("(") + 1:temp_s.find(")")]
            name = splitted[0].strip()
            unit = splitted[6].strip().strip('_')
            local_min = splitted[8].strip()
            local_max = splitted[7].strip()
            if splitted[0].endswith(')'):
                possibile_values = splitted[0].split('(')[2].split(')')[0]
            else:
                possibile_values = ''
            self.ini_dict["Setup"].append({"CODE": code, "FAMILY_ID": self.family, "UNIT": unit, "NAME": name,
                                          "MIN": local_min, "MAX": local_max, "POSSIBLE_VALUES": possibile_values})
        elif line.startswith("DI"):
            splitted = line.split('=', 1)[1].split(',')
            code = "1:digin:" + splitted[0].strip()
            name = splitted[1].strip()
            self.ini_dict["Digital"].append({"CODE": code, "FAMILY_ID": self.family, "NAME": name})
        elif line.startswith("DO"):
            splitted = line.split('=', 1)[1].split(',')
            code = "1:digout:" + splitted[0].strip()
            name = splitted[1].strip()
            self.ini_dict["Digital"].append({"CODE": code, "FAMILY_ID": self.family, "NAME": name})
        elif line.startswith("STS"):
            splitted = line.split('=', 1)[1].split(',')
            code = "1:status:" + splitted[1].strip()
            name = splitted[2].strip()
            self.ini_dict["Digital"].append({"CODE": code, "FAMILY_ID": self.family, "NAME": name})

    def create_dict(self):
        self.ini_dict["Analog"] = []
        self.ini_dict["Digital"] = []
        self.ini_dict["Command"] = []
        self.ini_dict["Setup"] = []
