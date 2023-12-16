# fuzzer settings. you can change these values to something you want.
default_settings = {"count": 5, "fuzzer": "random", "category": "base", "version": "4.0"}

# DO NOT CHANGE THESE VALUES
metrics = {
    "4.0": {
        "identifier": "CVSS:4.0",
        "values" : {
            "AV": ["N", "A", "L", "P"],
            "AC": ["L", "H"],
            "AT": ["N", "P"],
            "PR": ["N", "L", "H"],
            "UI": ["N", "P", "A"],
            "VC": ["H", "L", "N"],
            "VI": ["H", "L", "N"],
            "VA": ["H", "L", "N"],
            "SC": ["H", "L", "N"],
            "SI": ["H", "L", "N"],
            "SA": ["H", "L", "N"],
            "E": ["X", "A", "P", "U"],
            "CR":  ["X", "H", "M", "L"],
            "IR":  ["X", "H", "M", "L"],
            "AR":  ["X", "H", "M", "L"],
            "MAV": ["X", "N", "A", "L", "P"],
            "MAC": ["X", "L", "H"],
            "MAT": ["X", "N", "P"],
            "MPR": ["X", "N", "L", "H"],
            "MUI": ["X", "N", "P", "A"],
            "MVC": ["X", "H", "L", "N"],
            "MVI": ["X", "H", "L", "N"],
            "MVA": ["X", "H", "L", "N"],
            "MSC": ["X", "H", "L", "N"],
            "MSI": ["X", "S", "H", "L", "N"],
            "MSA": ["X", "S", "H", "L", "N"],
            "S":  ["X", "N", "P"],
            "AU": ["X", "N", "Y"],
            "R":  ["X", "A", "U", "I"],
            "V":  ["X", "D", "C"],
            "RE": ["X", "L", "M", "H"],
            "U":  ["X", "Clear", "Green", "Amber", "Red"]
        },
        "categories" : {
            "base" : ["AV", "AC", "AT", "PR", "UI", "VC", "VI", "VA", "SC", "SI", "SA"],
            "threat": ["E"],
            "environmental": ["CR", "IR", "AR", "MAV", "MAC", "MAT", "MPR", "MUI", "MVC", "MVI", "MVA", "MSC", "MSI", "MSA" ],
            "supplemental": ["S", "AU", "R", "V", "RE", "U"]
        },
    },
    "3.1": {
        "identifier": "CVSS:3.1",
        "values" : {
            'AV': ['N', 'A', 'L', 'P'],
            'AC': ['L', 'H'],
            'PR': ['N', 'L', 'H'],
            'UI': ['N', 'R'],
            'S': ['C', 'U'],
            'C': ['H', 'L', 'N'],
            'I': ['H', 'L', 'N'],
            'A': ['H', 'L', 'N'],
            'E': ['X', 'H', 'F', 'P', 'U'],
            'RL': ['X', 'U', 'W', 'T', 'O'],
            'RC': ['X', 'C', 'R', 'U'],
            'CR': ['X', 'H', 'M', 'L'],
            'IR': ['X', 'H', 'M', 'L'],
            'AR': ['X', 'H', 'M', 'L'],
            'MAV': ['X', 'N', 'A', 'L', 'P'],
            'MAC': ['X', 'L', 'H'],
            'MPR': ['X', 'N', 'L', 'H'],
            'MUI': ['X', 'N', 'R'],
            'MS': ['X', 'C', 'U'],
            'MC': ['X', 'H', 'L', 'N'],
            'MI': ['X', 'H', 'L', 'N'],
            'MA': ['X', 'H', 'L', 'N']
    },
    "categories" : {
        "base": ["AV", "AC", "PR", "UI", "S", "C", "I", "A"],
        "temporal": ["E", "RL", "RC"],
        "environmental": ["CR", "IR", "AR", "MAV", "MAC", "MPR", "MUI", "MS", "MC", "MI", "MA"]
    }
    },
    "2.0": {
        "identifier": "CVSS:2.0",
        "values" : {
            'AV': ['N', 'A', 'L'],
            'AC': ['L', 'M', 'H'],
            'AU': ['M', 'S', 'N'],
            'C': ['C', 'P', 'N'],
            'I': ['C', 'P', 'N'],
            'A': ['C', 'P', 'N'],
            'E': ['U', 'POC', 'F', 'H', 'ND'],
            'RL': ['OF', 'TF', 'W', 'U', 'ND'],
            'RC': ['UC', 'UR', 'C', 'ND'],
            'CDP': ['N', 'L', 'LM', 'MH', 'H', 'ND'],
            'TD': ['N', 'L' 'M', 'H', 'ND'],
            'CR': ['L', 'M', 'H', 'ND'],
            'CI': ['L', 'M', 'H', 'ND'],
            'CA': ['L', 'M', 'H', 'ND'],
    },
    "categories" : {
        "base": ["AV", "AC", "AU", "C", "I", "A"],
        "temporal": ["E", "RL", "RC"],
        "environmental": ["CDP", "TD", "CR", "CI", "CA"]
    }
    }
}