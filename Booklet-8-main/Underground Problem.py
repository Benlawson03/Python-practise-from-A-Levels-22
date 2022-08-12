#Underground problem
stations = ["Brixton", "Stockwell", "Vauxhall", "Pimlico", "Victoria", "Green Park", "Oxford Circus","Warren Street", "Euston","King's Cross","Highbury & Islington", "Finsbury Park","Seven Sisters","Tottenham Hale", "Blackhorse Road and Walthamstow Central"]

#Outputs stations
print("Brixton", "\nStockwell", "\nVauxhall", "\nPimlico", "\nVictoria", "\nGreen Park", "\nOxford Circus","\nWarren Street", "\nEuston","\nKing's Cross","\nHighbury & Islington", "\nFinsbury Park","\nSeven Sisters","\nTottenham Hale", "\nBlackhorse Road and Walthamstow Central")

#Inputs of stations from user
station1 = str(input("\nEnter your station: "))
station2 = str(input("Enter destination: "))

#Stations inbetween entered station
def direction(station1, station2):
  station1_index = ((stations.index(station1))-1)
  station2_index = ((stations.index(station2))-1)
  if station1_index > station2_index:
    stops = station1_index - station2_index
  else:
    stops = station2_index - station1_index
  return stops

stops = direction(station1, station2)
print(stops - 1)
