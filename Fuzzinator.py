import os
import csv
import time
fuzz_done_list = []
hython_cmd_list = []
moutons_shots = r"S:\SIC3D\SIC5\Projects\moutons\05-SHOTS"

#  format :  ["S5P170"]   ["S5P170","S5P180"]
specifiq_shot = ["S6P271"]

for doss in os.listdir(moutons_shots):
    for CHR in ["Herve", "Frank", "Mouton"]:
        path = f"{moutons_shots}\\{doss}\\{doss}_VFX\\{CHR}_csv_file.csv"
        path_fuzzdone = f"{moutons_shots}\\{doss}\\{doss}_VFX\\Fuzz_Done.txt"

        try:
            # Check if Fuzz is done
            if os.path.exists(path_fuzzdone):
                # Get the time of last
                # modification of the specified
                # path since the epoch
                csv_time = os.path.getmtime(path)
                done_time = os.path.getmtime(path_fuzzdone)

                if csv_time - done_time < 0:
                    continue

                print("Recent csv file found for ", doss)

            if len(specifiq_shot) > 0 :
                if not doss.split("_")[-1] in specifiq_shot :
                    continue

            with open(path, 'r') as file:
                csvreader = csv.reader(file)
                for row in csvreader:
                    if len(row) > 0:
                        print("csv file found for this shot " + doss)
                        hython_cmd_list.append(row[0])
            fuzz_done_list.append(path_fuzzdone)

        except:
            continue

for index, hython_cmd in enumerate(hython_cmd_list):
    print(hython_cmd)

to_run = True

if to_run:
    for index, hython_cmd in enumerate(hython_cmd_list):
        if not os.path.exists(fuzz_done_list[index]):
            os.mkdir(fuzz_done_list[index])
        os.system(hython_cmd)


# Output:
# 2022-03-01 14:30:15.123456
