mor={"prithvi","yash","harsh","param"}
night={"prathmesh","atharv","harsh","param"}
print("Students who studied in both shifts:",mor.intersection(night))
print("Students who studied only in the morning shift:",mor.difference(night))
print("Students who studied only in the night shift:",night.difference(mor))
print("Students with at least one session:",mor.union(night))
