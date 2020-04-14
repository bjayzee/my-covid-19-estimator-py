def covid19_impact_estimator(reported_cases):
  currently_infected = reported_cases * 10
  return currently_infected 
reported_cases = int(input("Enter the reported_cases: "))
impact = covid19_impact_estimator(reported_cases)
print("Currently infected people is ",impact)



def severe_impact(reported_cases):
  currently_infected = reported_cases * 50
  return currently_infected
severeImpact = severe_impact(reported_cases)
print("Currently infected for the severe impact is ",severeImpact)



def infections_by_requested_time_for_impact(impact):
  if period == "days":
    infections_by_requested_time = impact * 2
  elif period == "weeks":
    infections_by_requested_time = impact * 4
  elif period == "months":
    infections_by_requested_time = impact * 1024
  return infections_by_requested_time
period = input("choose estimation period: days/weeks/months: ").lower()
infectionTimeImpact = infections_by_requested_time_for_impact(impact)
print("Infections by requested time for impact is: ",infectionTimeImpact)



def infections_by_requested_time_for_severe_impact(severeImpact):
  if period == "days":
    infections_by_requested_time = severeImpact * 2
  elif period == "weeks":
    infections_by_requested_time = severeImpact * 4
  elif period == "months":
    infections_by_requested_time = severeImpact * 1024
  return infections_by_requested_time
infectionTimeForSevereImpact = infections_by_requested_time_for_severe_impact(severeImpact)
print("Infections by requested time for Severe Impact is: ",infectionTimeForSevereImpact)



def severe_cases_by_requested_time_for_Impact(infectionTimeImpact):
  severeCasesByRequestedTime = infections_by_requested_time_for_severe_impact(severeImpact) * 0.15
  severeCasesByRequestedTime = int(severeCasesByRequestedTime)
  return severeCasesByRequestedTime
severeCasessByRequestedTimeForImpact = severe_cases_by_requested_time_for_Impact(infectionTimeImpact)
print("severe cases by requested time for Impact is ",severeCasessByRequestedTimeForImpact)



def severe_cases_by_requested_time_for_Severe_Impact(infectionTimeForSevereImpact):
  severeCasesByRequestedTime = infections_by_requested_time_for_severe_impact(severeImpact) * 0.15
  severeCasesByRequestedTime = int(severeCasesByRequestedTime)
  return severeCasesByRequestedTime
severeCasessByRequestedTimeForSevereImpact = severe_cases_by_requested_time_for_Severe_Impact(infectionTimeForSevereImpact)
print("severe cases by requested time for severe Impact is ",severeCasessByRequestedTimeForSevereImpact)


total_hospital_beds = int(input("enter the total number of hospital beds available: "))
def total_hospital_beds_COVID19_patients(total_hospital_beds):  
  return total_hospital_beds * 0.35
totalHospitalBeds = int(total_hospital_beds_COVID19_patients(total_hospital_beds))

def hospital_beds_by_requested_time_for_Impact():
  hospital_beds_by_requested_time = totalHospitalBeds - severeCasessByRequestedTimeForImpact
  return hospital_beds_by_requested_time
hospitalBedsByRequestedTime = hospital_beds_by_requested_time_for_Impact()
print("Hospital bed by requested time for Impact: ",hospital_beds_by_requested_time_for_Impact())



def hospital_beds_by_requested_time_for_Severe_Impact():
  hospital_beds_by_requested_time = totalHospitalBeds - severeCasessByRequestedTimeForSevereImpact
  return hospital_beds_by_requested_time
hospitalBedsByRequestedTime = hospital_beds_by_requested_time_for_Severe_Impact()
print("Hospital bed by requested time for Severe Impact: ",hospital_beds_by_requested_time_for_Severe_Impact())



def cases_of_ICU_by_requested_time_for_Impact(infectionTimeImpact):
  cases_of_ICU_by_requested_time = infectionTimeImpact * 0.05
  return cases_of_ICU_by_requested_time
casesOfICUByRequestedTime = int(cases_of_ICU_by_requested_time_for_Impact(infectionTimeImpact))
print("Cases of ICU by requested time for Impact: ",casesOfICUByRequestedTime)



def cases_of_ICU_by_requested_time_for_Severe_Impact(infectionTimeForSevereImpact):
  cases_of_ICU_by_requested_time = infectionTimeForSevereImpact * 0.05
  return cases_of_ICU_by_requested_time
casesOfICUByRequestedTime = int(cases_of_ICU_by_requested_time_for_Impact(infectionTimeForSevereImpact))
print("Cases of ICU by requested time for Severe Impact: ",casesOfICUByRequestedTime)



def cases_for_ventilators_by_requested_time_for_impact(infectionTimeImpact):
  cases_for_ventilators_by_requested_time = infectionTimeImpact * 0.02
  return cases_for_ventilators_by_requested_time
casesForVentilatorsByRequestedTime = int(cases_for_ventilators_by_requested_time_for_impact(infectionTimeImpact))
print("Cases for Ventilators by requested time for Impact: ",cases_for_ventilators_by_requested_time_for_impact(infectionTimeImpact))



def cases_for_ventilators_by_requested_time_for_severe_impact(infectionTimeForSevereImpact):
  cases_for_ventilators_by_requested_time = infectionTimeForSevereImpact * 0.02
  return cases_for_ventilators_by_requested_time
casesForVentilatorsByRequestedTime = int(cases_for_ventilators_by_requested_time_for_impact(infectionTimeForSevereImpact))
print("Cases for Ventilators by requested time for Severe Impact: ",cases_for_ventilators_by_requested_time_for_impact(infectionTimeForSevereImpact))


def dollars_in_flight_for_impact(infectionTimeImpact):
  dollars_in_flight_for_impact = (infectionTimeImpact * 0.65) * dollars * 30
  return dollars_in_flight_for_impact
dollars = float(input("input average daily income per day for the region: "))
dollarsInFlightForImpact = int(dollars_in_flight_for_impact(infectionTimeImpact))
print("Dollars in flight for the Impact: ",dollars_in_flight_for_impact(infectionTimeImpact))



def dollars_in_flight_for_severe_impact(infectionTimeForSevereImpact):
  dollars_in_flight_for_severe_impact = (infectionTimeForSevereImpact * 0.65) * dollars * 30
  return dollars_in_flight_for_severe_impact
dollarsInFlightForImpact = int(dollars_in_flight_for_severe_impact(infectionTimeForSevereImpact))
print("Dollars in flight for Severe Impact: ",dollars_in_flight_for_severe_impact(infectionTimeForSevereImpact))
