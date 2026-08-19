
graduation_score = float(input("Enter graduation score (%): "))
active_backlogs = int(input("Enter number of active academic backlogs: "))

if graduation_score >= 70 and active_backlogs == 0:
    print("Eligible for placement.")
else:
    print("Not eligible for placement.")

    if graduation_score < 70:
        print("Reason: Graduation score must be 70% or higher.")

    if active_backlogs > 0:
        print("Reason: Candidate must have no active academic backlogs.")
