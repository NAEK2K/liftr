import csv
import re

with open("input", "r") as lift_input:
    lift = lift_input.read()

file_csv = open("spreadsheet.csv", "w")
csvwriter = csv.writer(file_csv)

for exercise in lift.split(","):
    name_max = re.search(r'"(.*)"=(\d+)(lbs|kgs|)', exercise)
    if name_max:
        groups = name_max.groups()
        exercise_name = groups[0]
        exercise_max_weight = groups[1]
        exercise_unit = groups[2] if groups[2] else "lbs"
    else:
        print("Invalid syntax detected: {}".format(exercise))
        exit()

    csvwriter.writerow(
        [exercise_name, "1RM={}{}".format(exercise_max_weight, exercise_unit)]
    )

    set_matches = re.findall(r"(\d+)x(\d+)(?:@(\d+)(lbs|kgs|%|))?", exercise)
    if set_matches:
        for exercise_set in set_matches:
            sets = exercise_set[0]
            reps = exercise_set[1]
            weight = exercise_set[2] if exercise_set[2] else 0
            unit = exercise_set[3] if exercise_set[3] else exercise_unit
            if unit == "%":
                weight = str(
                    int(exercise_max_weight) * int(weight) / 100
                ) + "{} ({}%)".format(exercise_unit, weight)
                unit = ""
            for i in range(int(sets)):
                csvwriter.writerow(
                    [reps, "{}{}".format(weight, unit) if weight else "?"]
                )

file_csv.close()
