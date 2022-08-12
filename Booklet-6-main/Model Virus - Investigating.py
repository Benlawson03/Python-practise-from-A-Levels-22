# Condition-controlled iterations

# Subroutine to show spread of virus
def ModelVirus(Day, CurrentCases, R, Target):
  PopulationInfected = CurrentCases
  while PopulationInfected < Target:
    PopulationInfected = int(CurrentCases * (2.718 ** (R * Day)))
    print("People infected on day {}: {}".format(Day, PopulationInfected))
    Day = Day + 1

# Main program
ModelVirus(1,1,1.2,10000)