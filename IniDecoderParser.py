# decoder = IniDecoderParser("~DIR~/FILEINI.ini", 1)
# decoder.ini_dict


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
            unit = splitted[3].strip().strip('_')
            self.ini_dict["analog"].append({
                "code": code, "family_id": self.family, "unit": unit,
                "name": name, "type": "anin"
            })
        elif line.startswith("AO"):
            splitted = line.split('=', 1)[1].split(',')
            code = "1:anout:" + splitted[0].strip()
            name = splitted[2].strip()
            unit = splitted[3].strip().strip('_')
            self.ini_dict["analog"].append({
                "code": code, "family_id": self.family, "unit": unit,
                "name": name, "type": "anout"
            })

        elif line.startswith("CMD"):
            splitted = line.split('=', 1)[1].split(';')
            code = "1:command:" + splitted[0].strip()
            name = splitted[1].strip()
            self.ini_dict["command"].append({
                "code": code, "family_id": self.family, "name": name
            })

        elif line.startswith("EVN"):
            splitted = line.split('=', 1)[1].split(',')
            code = "1:alarm:" + splitted[0].strip()
            name = splitted[1].strip()
            self.ini_dict["digital"].append({
                "code": code, "family_id": self.family, "name": name,
                "type": "alarm"
            })

        elif line.startswith("SETUP"):
            splitted = line.split('=', 1)[1].split(';')
            temp_s = splitted[0].strip()
            code = "1:setup:" + temp_s[temp_s.find("(") + 1:temp_s.find(")")]
            name = splitted[0].strip()
            type = splitted[2].strip()
            unit = splitted[6].strip().strip('_')
            min_value = float(splitted[8].strip())
            max_value = float(splitted[7].strip())
            if splitted[0].endswith(')'):
                possibile_values = splitted[0].split('(')[2].split(')')[0]
            else:
                possibile_values = ''
            self.ini_dict["setup"].append({
                "code": code, "family_id": self.family, "unit": unit,
                "name": name,  "type": type, "min_value": min_value,
                "max_value": max_value, "possible_values": possibile_values
            })
        elif line.startswith("DI"):
            splitted = line.split('=', 1)[1].split(',')
            code = "1:digin:" + splitted[0].strip()
            name = splitted[1].strip()
            self.ini_dict["digital"].append({
                "code": code, "family_id": self.family, "name": name,
                "type": "digin"
            })

        elif line.startswith("DO"):
            splitted = line.split('=', 1)[1].split(',')
            code = "1:digout:" + splitted[0].strip()
            name = splitted[1].strip()
            self.ini_dict["digital"].append({
                "code": code, "family_id": self.family, "name": name,
                "type": "digout"

            })

        elif line.startswith("STS"):
            splitted = line.split('=', 1)[1].split(',')
            code = "1:status:" + splitted[1].strip()
            name = splitted[2].strip()
            self.ini_dict["digital"].append({
                "code": code, "family_id": self.family, "name": name,
                "type": "status"
            })

    def create_dict(self):
        self.ini_dict["analog"] = []
        self.ini_dict["digital"] = []
        self.ini_dict["command"] = []
        self.ini_dict["setup"] = []
