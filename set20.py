java={'PRITHVI','YASH','HARSH','PARAM'}
python={'PRATHMESH','ATHARV','VIVEK'}
print("java students:",java)
print("python students:",python)
print("Students who studied in both sessions:",java.intersection(python))
print("Students who is only in any one session:",java.symmetric_difference(python))