import psycopg2
import csv
import os, fnmatch
conn = psycopg2.connect("host=ziggy.db.elephantsql.com dbname=msfdanjl user=msfdanjl password=kUM09GkSNYUVmXCDaGAOKpFSJeCKKoQ3")
cur = conn.cursor()




def OpenFile(fileName, subID):

    fileDir = os.path.dirname(os.path.abspath(__file__))
    path = fileDir + "/DATA/" + str(subID)

    file = path + fileName
    return file




def find(pattern, path):
    for root, dirs, files in os.walk(path):
        for name in files:
            if fnmatch.fnmatch(name, pattern):
                return name



def changeTime(t):
    time = t.split(':')
    return int(time[0])*3600 + int(time[1])*60 + int(time[2])

##QUESTIONNAIRE
# with open(OpenFile('DATABASE_QUESTIONNAIRE.csv',''), 'r') as f:
#     reader = csv.reader(f)
#     next(reader) # Skip the header
#     for row in reader:
#         print (row)
#         cur.execute(
#             "INSERT INTO subject_subject(subjectid, height, gender, handedness, birthyear) VALUES (%s, %s, %s, %s, %s)",
#             (row[1], row[7], row[6], row[9], row[5])
#         )
#         cur.execute(
#             "INSERT INTO generalinfo_generalinfo(subjectid_id, foodTime, caffeine, weight, groups, healthyScale, nicotine, noExercise, alcohol, MSDrugs, motionSickness, comments) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)", 
#             (row[1], row[10], row[11], row[8], row[2], row[12], row[14], row[13], row[15], row[17], row[16], row[27])
#         )
#         cur.execute(
#             "INSERT INTO nausea_nausea(subjectid_id, cars, busses, trains, airplanes, smallBoats, ships, swings, roundabout, funfair) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",
#             (row[1], row[18], row[19], row[20], row[21], row[22], row[23], row[24], row[25], row[26])
#         )
#         cur.execute(
#             "INSERT INTO msgolden_msgolden(subjectid_id, type, genDiscomfort, fatigue, headache, eyestrain, diffOfFocus, incrSalvation, sweat, nausea, blurredVision, dizziness) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",
#             (row[1], 0, row[28], row[29], row[30], row[31], row[32], row[33], row[34], row[35], row[36], row[37])
#         )
#         cur.execute(
#             "INSERT INTO msgolden_msgolden(subjectid_id, type, genDiscomfort, fatigue, headache, eyestrain, diffOfFocus, incrSalvation, sweat, nausea, blurredVision, dizziness) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",
#             (row[1], 1, row[38], row[39], row[40], row[41], row[42], row[43], row[44], row[45], row[46], row[47])
#         )

##EMG

with open(OpenFile('DATABASE_SUPERSHEET.csv',''), 'r') as f:
    reader = csv.reader(f)
    next(reader) # Skip the header
    k=0
    for row in reader:
        for i in range (0,33,6): ## Timabil, BSL, pre, 25, 50, 75, post
            for j in range (1,7): ## sensors
                cur.execute(
                    "INSERT INTO emg_emg(subjectid_id, area, f40_132, f132_224, f224_316, f316_408, f408_500, interval, sensor) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)",
                    (row[0], row[j-1+i+37], row[j-1+i+73], row[j-1+i+74], row[j-1+i+75], row[j-1+i+76], row[j-1+i+77], k, j)
                )
            k=k+1

##EEG

with open(OpenFile('DATABASE_SUPERSHEET.csv',''), 'r') as f:
    reader = csv.reader(f)
    next(reader) # Skip the header
    for row in reader:
        k=0
        for i in range (0,26,5): ## Timabil, BSL, pre, 25, 50, 75, post
            cur.execute(
                "INSERT INTO eeg_eeg(subjectid_id, delta, theta, alpha, beta, low_gamma, interval) VALUES (%s, %s, %s, %s, %s, %s, %s)",
                (row[0], row[7+i], row[8+i], row[9+i], row[10+i], row[11+i], k)
            )
            k=k+1
            

##HR

with open(OpenFile('DATABASE_SUPERSHEET.csv',''), 'r') as f:
    reader = csv.reader(f)
    next(reader) # Skip the header
    for row in reader:
        for i in range (0,6): ## Timabil, pre, 25, 50, 75, post
            if i == 0:
                cur.execute(
                "INSERT INTO hr_hr(subjectid_id, bpm, interval) VALUES (%s, %s, %s)",
                (row[0], 0.0, i)
            )
            else:
                cur.execute(
                    "INSERT INTO hr_hr(subjectid_id, bpm, interval) VALUES (%s, %s, %s)",
                    (row[0], row[1+i], i)
                )

##PLATFORM
##það þarf data möppurnar inní hér til að geta gert þetta
# subID = [7, 18, 27, 28, 39, 40, 61, 62, 98, 103]

# for sub in subID:
#     with open(OpenFile("/new_platform.CSV",sub)) as csv_file1:
#         csv_reader1 = csv.reader(csv_file1, delimiter=',')
#         start=0
#         stop=False
#         for col in csv_reader1:
#             start=start+1
#             if col[1] == ' MotionVR pitch average':
#                 stop=True
#             if start >= 2 and stop==False:
#                 cur.execute( 
#                     "INSERT INTO Platform(subjectID, roll, pitch, heave, AP, ML, time) VALUES(%s, %s,%s, %s, %s,%s, %s)", (sub, col[2], col[1], col[3], col[5], col[4], col[0])
#                     )

##SPO2??

conn.commit()