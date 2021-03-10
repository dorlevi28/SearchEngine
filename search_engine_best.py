
class System{
	private ArrayList<Flight> flights;
	private ArrayList<AirPort Representative>reps;
	private ArrayList<Flight Attendant>flightA;
	private ArrayList<Pilots> Pilots;
	private ArrayList<FlightCompany> FlightP;
	private AirPortManager airPM;
	private ArrayList<FlightZone> AllowedZones;
	private ArrayList<FlightZone> UnAllowedZones;
	LogFile dailyLog;




// this methods check and replaces the pilot of both given flights
	private SwitchPilots(Flight1,Flight2,Classification,AirPortCompany){
		if(!checkClassifications){
			mainScreen();
        }
	else if {!verifyBelongs()){
		mainScreen();
        }              			
	Else{
		Pilot tmpPilot=Flight1.getPilot();
		Flight1.setPilot(Flight2.getPilot());
		Flight2.setPilot(tmpPilot);
		sendApproval(FlightCompnay,lFreport);
FlightChangeReport lFreport = new FlightChangeReport(Flight1.getFlightNum(),Flight1.getFlightNum(),true);
		insertChangeToLogFile(lFreport,dailyLog);
		System.out.println("pilots have been changed succesfully);
		mainScreen();
	}

  }
// this methods check and verifies that the flights belong to the same flight company


    private boolean verifyBelongs(Flight1,Flight2,FlightCompany){
    if(!AirPortCompany.getFlightsForToday.contains(Flight1) ||   !AirPortCompany.getFlightsForToday.contains(Flight1)){
    system.out.println("one of the flights you have entered does not belong to this FlightComapny:"+AirPortCompany.getName());
        return False;
	}
	Else{
		return True;
	}
 // this methods inserts the change report to the daily log changes file
      
	private insertChangeToLogFile(lFreport,dailyLog){
		dailyLog.addReport(lFreport)
	}
    
    
    
// this methods check that the air port representative has the classification to change pilots


	private boolean checkClassifications(classifications){
		if(!Classification.contains("switchP"){
		system.out.println("you do not have authorities to change pilot");
		return False;
	}
	else {
		return True;
	}

}
// this methods sends approval of the change to the flying company

	private sendApproval(FlightCompany,lFreport)}
		FlightCompany.getApprovalsReports.add(lFreport)

	}
}












