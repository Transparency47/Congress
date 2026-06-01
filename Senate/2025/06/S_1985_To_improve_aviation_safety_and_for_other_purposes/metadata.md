# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/1985?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/1985
- Title: Safe Operations of Shared Airspace Act of 2025
- Congress: 119
- Bill type: S
- Bill number: 1985
- Origin chamber: Senate
- Introduced date: 2025-06-05
- Update date: 2026-03-26T18:29:31Z
- Update date including text: 2026-03-26T18:29:31Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-06-05: Introduced in Senate
- 2025-06-05 - IntroReferral: Introduced in Senate
- 2025-06-05 - IntroReferral: Read twice and referred to the Committee on Commerce, Science, and Transportation.
- Latest action: 2025-06-05: Introduced in Senate

## Actions

- 2025-06-05 - IntroReferral: Introduced in Senate
- 2025-06-05 - IntroReferral: Read twice and referred to the Committee on Commerce, Science, and Transportation.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-06-05",
    "latestAction": {
      "actionDate": "2025-06-05",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/1985",
    "number": "1985",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Transportation and Public Works"
    },
    "sponsors": [
      {
        "bioguideId": "C000127",
        "district": "",
        "firstName": "Maria",
        "fullName": "Sen. Cantwell, Maria [D-WA]",
        "lastName": "Cantwell",
        "party": "D",
        "state": "WA"
      }
    ],
    "title": "Safe Operations of Shared Airspace Act of 2025",
    "type": "S",
    "updateDate": "2026-03-26T18:29:31Z",
    "updateDateIncludingText": "2026-03-26T18:29:31Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-06-05",
      "committees": {
        "item": {
          "name": "Commerce, Science, and Transportation Committee",
          "systemCode": "sscm00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Commerce, Science, and Transportation.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-06-05",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in Senate",
      "type": "IntroReferral"
    }
  ]
}
```

## API Data: committees

```json
{
  "committees": [
    {
      "activities": {
        "item": {
          "date": "2025-06-05T19:50:14Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Commerce, Science, and Transportation Committee",
      "systemCode": "sscm00",
      "type": "Standing"
    }
  ]
}
```

## API Data: cosponsors

```json
{
  "cosponsors": [
    {
      "bioguideId": "D000622",
      "firstName": "Tammy",
      "fullName": "Sen. Duckworth, Tammy [D-IL]",
      "isOriginalCosponsor": "True",
      "lastName": "Duckworth",
      "party": "D",
      "sponsorshipDate": "2025-06-05",
      "state": "IL"
    },
    {
      "bioguideId": "K000367",
      "firstName": "Amy",
      "fullName": "Sen. Klobuchar, Amy [D-MN]",
      "isOriginalCosponsor": "True",
      "lastName": "Klobuchar",
      "party": "D",
      "sponsorshipDate": "2025-06-05",
      "state": "MN"
    },
    {
      "bioguideId": "M000133",
      "firstName": "Edward",
      "fullName": "Sen. Markey, Edward J. [D-MA]",
      "isOriginalCosponsor": "True",
      "lastName": "Markey",
      "middleName": "J.",
      "party": "D",
      "sponsorshipDate": "2025-06-05",
      "state": "MA"
    },
    {
      "bioguideId": "K000384",
      "firstName": "Timothy",
      "fullName": "Sen. Kaine, Tim [D-VA]",
      "isOriginalCosponsor": "True",
      "lastName": "Kaine",
      "middleName": "M.",
      "party": "D",
      "sponsorshipDate": "2025-06-05",
      "state": "VA"
    },
    {
      "bioguideId": "W000805",
      "firstName": "Mark",
      "fullName": "Sen. Warner, Mark R. [D-VA]",
      "isOriginalCosponsor": "True",
      "lastName": "Warner",
      "middleName": "R.",
      "party": "D",
      "sponsorshipDate": "2025-06-05",
      "state": "VA"
    },
    {
      "bioguideId": "W000790",
      "firstName": "Raphael",
      "fullName": "Sen. Warnock, Raphael G. [D-GA]",
      "isOriginalCosponsor": "True",
      "lastName": "Warnock",
      "party": "D",
      "sponsorshipDate": "2025-06-05",
      "state": "GA"
    },
    {
      "bioguideId": "V000128",
      "firstName": "Chris",
      "fullName": "Sen. Van Hollen, Chris [D-MD]",
      "isOriginalCosponsor": "False",
      "lastName": "Van Hollen",
      "party": "D",
      "sponsorshipDate": "2025-07-28",
      "state": "MD"
    },
    {
      "bioguideId": "S001181",
      "firstName": "Jeanne",
      "fullName": "Sen. Shaheen, Jeanne [D-NH]",
      "isOriginalCosponsor": "False",
      "lastName": "Shaheen",
      "party": "D",
      "sponsorshipDate": "2025-07-28",
      "state": "NH"
    },
    {
      "bioguideId": "B001303",
      "firstName": "Lisa",
      "fullName": "Sen. Blunt Rochester, Lisa [D-DE]",
      "isOriginalCosponsor": "False",
      "lastName": "Blunt Rochester",
      "party": "D",
      "sponsorshipDate": "2025-07-28",
      "state": "DE"
    },
    {
      "bioguideId": "B001277",
      "firstName": "Richard",
      "fullName": "Sen. Blumenthal, Richard [D-CT]",
      "isOriginalCosponsor": "False",
      "lastName": "Blumenthal",
      "party": "D",
      "sponsorshipDate": "2025-07-31",
      "state": "CT"
    },
    {
      "bioguideId": "W000779",
      "firstName": "Ron",
      "fullName": "Sen. Wyden, Ron [D-OR]",
      "isOriginalCosponsor": "False",
      "lastName": "Wyden",
      "party": "D",
      "sponsorshipDate": "2025-07-31",
      "state": "OR"
    },
    {
      "bioguideId": "W000800",
      "firstName": "Peter",
      "fullName": "Sen. Welch, Peter [D-VT]",
      "isOriginalCosponsor": "False",
      "lastName": "Welch",
      "party": "D",
      "sponsorshipDate": "2025-09-18",
      "state": "VT"
    },
    {
      "bioguideId": "K000394",
      "firstName": "Andy",
      "fullName": "Sen. Kim, Andy [D-NJ]",
      "isOriginalCosponsor": "False",
      "lastName": "Kim",
      "party": "D",
      "sponsorshipDate": "2025-10-22",
      "state": "NJ"
    }
  ]
}
```

## API Data: fullTexts

```json
{
  "fullTexts": [
    {
      "fetchError": null,
      "sourceFormat": "Formatted XML",
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1985is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 1985\nIN THE SENATE OF THE UNITED STATES\nJune 5, 2025 Ms. Cantwell (for herself, Ms. Duckworth , Ms. Klobuchar , Mr. Markey , Mr. Kaine , Mr. Warner , and Mr. Warnock ) introduced the following bill; which was read twice and referred to the Committee on Commerce, Science, and Transportation\nA BILL\nTo improve aviation safety, and for other purposes.\n#### 1. Short title; table of contents\n##### (a) Short title\nThis Act may be cited as the Safe Operations of Shared Airspace Act of 2025 .\n##### (b) Table of contents\nThe table of contents for this Act is as follows:\nSec. 1. Short title; table of contents.\nSec. 2. Definitions.\nSec. 3. Expert compliance review of FAA Safety Management System.\nSec. 4. ADS\u2013B Out Reforms.\nSec. 5. ADS\u2013B In requirement to enhance safety.\nSec. 6. Safety reviews of airspace.\nSec. 7. FAA-Department of Defense Safety Information Sharing.\nSec. 8. No disruptions to FAA workforce.\nSec. 9. Extension of FAA air traffic controller max hiring requirement.\nSec. 10. Air traffic controller training improvements.\nSec. 11. TARAM analyses.\nSec. 12. Employee reporting.\nSec. 13. Conflicts of interest.\n#### 2. Definitions\nIn this Act:\n**(1) Administrator**\nThe term Administrator means the Administrator of the FAA.\n**(2) ADS\u2013B in**\nThe term ADS\u2013B In means onboard avionics technology that periodically receives ADS\u2013B Out broadcasts of an aircraft's state vector (3-dimensional position and 3-dimensional velocity) and other required information as described in part 91.277 of title 14, Code of Federal Regulations (or a successor regulation).\n**(3) ADS\u2013B out**\nThe term ADS\u2013B Out has the meaning given such term in section 91.227 of title 14, Code of Federal Regulations (or a successor regulation).\n**(4) Air carrier; foreign air carrier**\nThe terms air carrier and foreign air carrier have the meanings given such terms in section 40102 of title 49, United States Code.\n**(5) Appropriate committees of congress**\nThe term appropriate committees of Congress means the Committee on Commerce, Science, and Transportation of the Senate and the Committee on Transportation and Infrastructure of the House of Representatives.\n**(6) Cabinet member**\nThe term Cabinet Member means an individual who is the head (including an acting head) of the Department of Agriculture, Department of Commerce, Department of Defense, Department of Education, Department of Energy, Department of Health and Human Services, Department of Homeland Security, Department of Housing and Urban Development, Department of the Interior, Department of Justice, Department of Labor, Department of State, Department of Transportation, Department of the Treasury, or Department of Veterans Affairs, or any other individual who occupies a position designated by the President as a Cabinet-level position.\n**(7) Comptroller General**\nThe term Comptroller General means the Comptroller General of the United States.\n**(8) FAA**\nThe term FAA means the Federal Aviation Administration.\n**(9) Powered-lift**\nThe term powered-lift has the meaning given such term in section 1.1 of title 14, Code of Federal Regulations (or a successor regulation).\n**(10) Rotorcraft**\nThe term rotorcraft has the meaning given such term in section 1.1 of title 14, Code of Federal Regulations (or a successor regulation).\n**(11) Secretary**\nThe term Secretary means the Secretary of Transportation.\n**(12) SMS**\nThe term SMS means a safety management system.\n**(13) Transport airplane**\nThe term transport airplane means a transport category airplane designed for operation by an air carrier or foreign air carrier type-certificated with a passenger seating capacity of 30 or more or an all-cargo or combi derivative.\n**(14) Unmanned aircraft system**\nThe term unmanned aircraft system has the meaning given such term in section 44801 of title 49, United States Code.\n#### 3. Expert compliance review of FAA Safety Management System\n##### (a) Expert compliance review\n**(1) Establishment**\n**(A) In general**\nNot later than 60 days after the date of enactment of this section, the Administrator shall convene an independent expert panel (in this section referred to as the review panel ) to review and make findings and recommendations on the matters listed in paragraph (2).\n**(B) Purpose**\nThe purpose of the review panel is to review and evaluate FAA orders and policies to inform the FAA\u2019s implementation of a comprehensive and integrated SMS for all lines of business within the FAA.\n**(2) Contents of review**\nThe review panel shall review the following:\n**(A)**\nThe extent to which the FAA\u2019s SMS complies with relevant FAA orders and policies.\n**(B)**\nThe actual and projected safety enhancements achieved through the FAA\u2019s prior implementation of SMS.\n**(C)**\nThe effectiveness of SMS, including with respect to the implementation of the following 4 components:\n**(i)**\nSafety policy.\n**(ii)**\nSafety risk management.\n**(iii)**\nSafety assurance.\n**(iv)**\nSafety promotion.\n**(D)**\nThe extent to which SMS and each of the 4 components described in subparagraph (C) are integrated among and across all lines of business of the FAA.\n**(E)**\nThe extent to which SMS and each of the 4 components so described are understood, communicated, and trained to personnel at the FAA.\n**(F)**\nThe efficacy of the FAA\u2019s Voluntary Safety Reporting Programs as part of SMS, including any actions taken by the FAA in response to reports filed under such program.\n**(G)**\nWhether the Federal Government should advocate for changes to Annex 19\u2013Safety Management of the International Civil Aviation Organization (in this section referred to as ICAO ) to ensure appropriate updates to the State Safety Program standards and recommended practices, including\u2014\n**(i)**\na systems-level approach to evaluating and improving SMS for air navigation service providers; and\n**(ii)**\nthe implementation of SMS for civil aviation regulators.\n**(H)**\nAny other matter determined by the Administrator for which review by the review panel would be consistent with the public interest in aviation safety.\n**(3) Composition of review panel**\n**(A) Appointed members**\nThe review panel shall consist of the following members appointed by the Administrator:\n**(i)**\nTwo representatives of the National Aeronautics and Space Administration with expertise in SMSs.\n**(ii)**\nThree appropriately qualified representatives of aviation labor organizations (designated by the applicable represented organization), including\u2014\n**(I)**\nthe principal organization representing the largest certified collective bargaining representative of airline pilots; and\n**(II)**\nthe exclusive bargaining representatives of FAA air traffic controllers certified under section 7111 of title 5, United States Code.\n**(iii)**\nNot less than 5 independent subject matter experts in safety management systems who\u2014\n**(I)**\nhave not served as a political appointee in the FAA; and\n**(II)**\nhave a minimum of 10 years of relevant applied experience.\n**(iv)**\nThree representatives from the aviation industry with expertise in SMS.\n**(v)**\nA representative of the United States Mission to the ICAO.\n**(B) Advisory members**\n**(i) In general**\nIn addition to the appointed members described in subparagraph (A), the review panel shall be advised by up to 5 employees of the FAA, at least 3 of whom shall be subject matter experts in implementing SMS at the FAA.\n**(ii) Duties**\nThe advisory members may take part in deliberations of the review panel and provide subject matter expertise with respect to the review panel\u2019s work.\n**(4) Recommendations**\nThe review panel shall issue recommendations to the Administrator based on the review of the matters listed in paragraph (2) in order to inform the FAA\u2019s implementation of a comprehensive and integrated SMS for all lines of business within the FAA.\n**(5) Report**\n**(A) Submission**\nNot later than 180 days after the date of the first meeting of the review panel, the review panel shall submit to the Administrator and the appropriate committees of Congress a report containing the findings and recommendations regarding the matters listed in paragraph (2) that are endorsed by a majority of the review panel.\n**(B) Dissenting views**\nIn submitting the report under subparagraph (A), the review panel shall append to such report the dissenting views of any individual member or group of members of the review panel regarding the findings or recommendations of the review panel.\n**(C) Publication**\nNot later than 5 days after receiving the report under subparagraph (A), the Administrator shall publish such report, including any dissenting views appended to the report, on the website of the FAA.\n**(D) Termination**\nThe review panel shall terminate upon the submission of the report under subparagraph (A).\n**(6) Administrative provisions**\n**(A) Access to information**\n**(i) In general**\nThe review panel shall have the authority to perform the following actions if a majority of the review panel members consider each action necessary and appropriate:\n**(I)**\nEntering onto the premises of the FAA for access to and inspection of records or other purposes.\n**(II)**\nNotwithstanding any other provision of law, except as provided in clause (ii), accessing and inspecting de-identified, but otherwise unredacted, records directly necessary for the completion of the review panel\u2019s work under this section that are in the possession of the FAA.\n**(III)**\nInterviewing employees of the FAA as necessary for the review panel to complete its work.\n**(ii) Non-federal government members**\nMembers of the review panel who are not officers or employees of the Federal Government shall only have access to, and be allowed to inspect, information provided to the FAA pursuant to section 40123 of title 49, United States Code, and part 193 of title 14, Code of Federal Regulations, in a de-identified form.\n**(B) Nondisclosure of confidential information**\n**(i) Nondisclosure for non-federal government members**\n**(I) Non-federal government participants**\nPrior to participating on the review panel, each individual serving on the review panel representing a non-Federal entity shall execute an agreement with the Administrator in which the individual shall be prohibited from disclosing at any time, except as required by law, to any person, foreign or domestic, any non-public information made available to the panel under subparagraph (A).\n**(II) Federal Government participants**\nFederal officers or employees serving on the review panel as representatives of the Federal Government and subject to the requirement to protect confidential information (including proprietary information and trade secrets under section 1905 of title 18, United States Code) shall not be required to execute agreements under this clause.\n**(ii) Protection of information**\nInformation that is obtained or reviewed by the review panel shall not constitute a waiver of the protections applicable to the information under section 552 of title 5, United States Code (commonly referred to as the Freedom of Information Act ). Members of the review panel shall protect such information to the extent required under applicable law.\n**(iii) Protection of proprietary information and trade secrets**\nMembers of the review panel shall protect proprietary information, trade secrets, and other information otherwise exempt under section 552 of title 5, United States Code, to the extent permitted under applicable law.\n**(7) Inapplicability of FACA**\nThe review panel shall not be subject to chapter 10 of title 5, United States Code (commonly referred to as the Federal Advisory Committee Act ).\n**(8) Process improvements**\nNot later than 1 year after the submission of the recommendations under paragraph (4), the Administrator shall report to the appropriate committees of Congress on the status of any ongoing actions in response to such recommendations, including the status of implementation of each of the recommendations of the review panel, if any, with which the Administrator concurs.\n##### (b) Non-Concurrence with recommendations\nNot later than 6 months after submission of the recommendations under subsection (a)(4), with respect to each recommendation of the review panel with which the Administrator does not concur, if any, the Administrator shall publish on the website of the FAA and submit to the appropriate committees of Congress a detailed explanation for such determination.\n#### 4. ADS\u2013B Out Reforms\n##### (a) Applicability of certain exceptions\nFor purposes of applying section 91.225(f) of title 14, Code of Federal Regulations (or any successor regulation), the term sensitive government mission shall be strictly construed and shall not include training flights, flights of Federal officials below the rank of Cabinet Member, or any routine flights.\n##### (b) Conforming amendment\nSection 1046(e)(3) of the John S. McCain National Defense Authorization Act for Fiscal Year 2019 ( 49 U.S.C. 40101 note) is amended to read as follows:\n(3) The term special mission aircraft means an aircraft the Secretary of Defense designates, in coordination with the Federal Aviation Administration, for a unique mission to which operating with ADS\u2013B Out equipment installed and activated creates a unique risk when weighed against any risk to the safety of the national airspace system posed by non-equipage and deactivation of ADS\u2013B Out equipment. .\n##### (c) Administrative action\nThe Administrator shall modify section 91.225(f) of title 14, Code of Federal Regulations (or any successor regulation), and any pertinent Memorandum of Agreement, to conform with the requirements of this section.\n##### (d) GAO review and report\nNot later than the date that is 1 year after the date of enactment of this section, the Comptroller General shall\u2014\n**(1)**\nreview the utilization of exceptions specified in section 91.225(f) of title 14, Code of Federal Regulations (or any successor regulation), as modified to conform with the requirements of this section, and section 1046(e)(3) of the John S. McCain National Defense Authorization Act for Fiscal Year 2019 ( 49 U.S.C. 40101 note), as amended by subsection (b), to determine whether the Department of Defense and other relevant Federal agencies, or other applicable operators, have utilized those exceptions in accordance with relevant law and regulation and the extent of such utilization; and\n**(2)**\nsubmit to the appropriate committees of Congress a report on the findings of the review conducted under paragraph (1).\n##### (e) FAA review\nUpon submission of the report specified in subsection (d)(2), the Administrator shall determine whether any Federal agencies that have been found to have not utilized exceptions in accordance with relevant laws and regulations shall be permitted to continue to utilize those exceptions. The Administrator shall brief the appropriate committees of Congress on such determination.\n##### (f) Joint council\nThe Administrator, through the Office of FAA\u2013DOD Coordination established or designated under section 6, and the Secretary of Defense, shall establish a joint council to regularly review all operations, including those operated by Federal agencies, that utilize the exceptions to the ADS\u2013B Out equipage and transmission requirements to ensure compliance with relevant laws and regulations. The joint council shall brief the appropriate committees of Congress on an annual basis.\n#### 5. ADS\u2013B In requirement to enhance safety\n##### (a) Deadline for compliance\nNot later than the date that is 4 years after the date of enactment of this section, an air carrier operating under part 121 of title 14, Code of Federal Regulations or providing service under part 135 of title 14 of such Code pursuant to a schedule or in conjunction with part 380 of title 14 of such Code may not operate an aircraft unless the aircraft has Automatic Dependent Surveillance-Broadcast In (ADS\u2013B In) equipment installed and operational at all times unless otherwise authorized by air traffic control, regardless of whether the Administrator has issued regulations to implement such requirement.\n##### (b) Performance requirements\nThe Administrator shall determine appropriate performance requirements for the ADS\u2013B In equipment referenced in subsection (a) for the purposes of providing safety-enhancing capabilities for flight crews, including but not limited to increasing situational awareness, receiving indications and alerts of air traffic conflicts, and facilitating aircraft collision avoidance. The Administrator shall issue relevant guidance to operators and other appropriate stakeholders on the types of equipment that satisfy the requirements of this section.\n#### 6. Safety reviews of airspace\n##### (a) FAA\u2013DOD Coordination\nNot later than 30 days after the date of enactment of this section, the Administrator shall establish or designate an office within the FAA as the Office of FAA\u2013DOD Coordination (in this section referred to as the Office ), which shall\u2014\n**(1)**\ncoordinate airspace usage of military aircraft and rotorcraft with relevant FAA lines of business including the Air Traffic Organization; and\n**(2)**\ncarry out the safety review required by subsection (b).\n##### (b) Safety reviews\n**(1) Review of Ronald Reagan Washington National Airport**\nNot later than 30 days after the date on which the Office is established or designated, the Administrator, in coordination with the Secretary of Defense and the heads of any other Federal agencies determined appropriate by the Administrator, shall initiate a safety review (in this subsection referred to as the review ) of all military, law enforcement, and civilian rotary wing, powered lift, and unmanned aircraft system flight operations and flight routes in the Washington DC Metropolitan Area Special Flight Rules Area, including but not limited to flight operations conducted by the Department of Defense and emergency response providers, to evaluate any associated safety risk on commercial transport airplane operations at Ronald Reagan Washington National Airport.\n**(2) Other airport reviews**\n**(A) In general**\nThe Administrator, in coordination with the Secretary of Defense and the heads of any Federal agencies determined appropriate by the Administrator, shall conduct safety reviews of all military, law enforcement and civilian rotary wing, powered lift, and unmanned aircraft system flight operations and flight routes at other Class B airports (as listed in section 1 of Appendix D to part 91 of title 14, Code of Federal Regulations (or any successor regulation)) in Class B airspace in the national airspace system, including flight operations conducted by the Department of Defense and emergency response providers, to evaluate any associated safety risk on commercial transport airplane operations.\n**(B) Prioritization**\n**(i) In general**\nNot later than 90 days after the date of enactment of this section, for the sole purpose of carrying out the safety reviews required by subparagraph (A), the Administrator shall classify Class B airports into the following categories based on the volume of mixed air traffic at each airport, as determined by the Administrator:\n**(I)**\nClass B airports with higher volumes of mixed air traffic.\n**(II)**\nClass B airports with lower volumes of mixed air traffic.\n**(ii) Priority**\nIn conducting the safety reviews required by subparagraph (A), the Administrator shall prioritize the evaluation of Class B airports in the category under clause (i)(I).\n**(C) Deadline of initiation of reviews**\n**(i) Class B airports with higher volumes**\nThe Administrator shall initiate the review under subparagraph (A) of Class B airports in the category under subparagraph (B)(i)(I) no later than 90 days after the date of enactment of this section.\n**(ii) Class B airports with lower volumes**\nThe Administrator shall initiate the review under subparagraph (A) of Class B airports in the category under subparagraph (B)(i)(II) no later than 90 days after the deadline for completion of the reviews under paragraph (4)(B)(i).\n**(3) Requirements**\nIn conducting the safety reviews required by paragraphs (1) and (2), the Office shall do the following:\n**(A)**\nAnalyze air traffic and airspace management.\n**(B)**\nEvaluate the level of coordination the Administrator exercises with the Secretary of Defense and the heads of any other Federal agencies, and emergency response providers as appropriate, to inform the designation and approval of airspace use and flight routes for non-transport airplane operations.\n**(C)**\nAssess any risks posed to transport airplanes from military aircraft, civil rotorcraft, powered lift aircraft, and unmanned aircraft systems operating in Class B airspace in proximity to Class B airports.\n**(D)**\nReview relevant incidents submitted to the Administrator through Air Traffic Mandatory Occurrence reports (as documented via FAA Form 7210\u201313), Aviation Safety Reporting System reports, and Aviation Safety Action Program reports, and relevant reports submitted to the Administrator of the National Aeronautics and Space Administration through the Aviation Safety Reporting System, to identify any safety trends regarding the operation of military aircraft, civil rotorcraft, powered lift aircraft, and unmanned aircraft systems in Class B airspace near Class B airports.\n**(E)**\nSelect appropriately qualified representatives of aviation labor organizations (designated by the applicable represented organization) as participants in the reviews, including, at a minimum\u2014\n**(i)**\nthe principal organization representing the largest certified collective bargaining representative of airline pilots; and\n**(ii)**\nthe exclusive bargaining representative of air traffic controllers of the FAA certified under section 7111 of title 5, United States Code.\n**(4) Deadlines for completion of safety reviews**\n**(A) Ronald Reagan Washington National Airport**\nThe Administrator shall complete the safety review required by paragraphs (1) not later than 120 days after the date on which such review is initiated.\n**(B) Other airports**\n**(i) Class B airports with higher volumes**\nThe Administrator shall complete the safety reviews required by paragraphs (2) of Class B airports in the category under subparagraph (B)(i)(I) of such paragraph no later than 2 years after the date on which the first of such reviews is initiated.\n**(ii) Class B airports with lower volumes**\nThe Administrator shall complete the safety review required by paragraphs (2) of Class B airports in the category under subparagraph (B)(i)(II) of such paragraph no later than 2 years after the deadline for completion of the reviews under clause (i).\n**(5) Report**\nNot later than 60 days after the safety reviews required by paragraphs (1) and (2) are completed, the Administrator shall submit to the appropriate committees of Congress a report detailing the analysis and results of the review, together with relevant findings and recommendations, including any recommendations for legislative or administrative action determined appropriate by the Administrator.\n#### 7. FAA-Department of Defense Safety Information Sharing\n##### (a) MOU with the Department of the Army\nNot later than the date that is 60 days after the date of enactment of this section, the Federal Aviation Administration and the Department of the Army shall establish a Memorandum of Understanding to permit, as appropriate, the sharing of information from the Army\u2019s Safety Management Information System with the FAA to facilitate communications and analysis of any applicable impacts to the safety and efficiency of civil aviation operations and to mitigate risk in the national airspace system.\n##### (b) Other Department of Defense MOUs\nNot later than the date that is 90 days after the date of the enactment of this section, the Federal Aviation Administration shall establish a Memorandum of Understanding with the following military departments to permit, as appropriate, the sharing of information from applicable aviation safety information systems to facilitate communications and analysis of any applicable impacts to the safety and efficiency of civil aviation operations and to mitigate risk in the national airspace system:\n**(1)**\nThe Department of the Navy.\n**(2)**\nThe Department of the Air Force.\n**(3)**\nThe Coast Guard.\n#### 8. No disruptions to FAA workforce\n##### (a) Hiring freeze exclusion\n**(1) In general**\nAny action by the President, the Secretary, the Administrator, the Director of the Office of Personnel Management, or other head, officer, or employee of a Federal executive entity to halt appointment activities in the Federal service on or after the date of enactment of this section shall exclude the FAA workforce.\n**(2) Retroactive application**\nEach action by the President, the Secretary, the Administrator, the Director of the Office of Personnel Management, or other head, officer, or employee of a Federal executive entity to halt appointment activities at the FAA during the period beginning on January 20, 2025, and ending on the date of enactment of this section is reversed.\n##### (b) Deferred Resignation Program and Voluntary Furlough Exclusion\n**(1) In general**\nAny action on or after the date of enactment of this section by the President, the Secretary, the Administrator, the Director of the Office of Personnel Management, or other head, officer, or employee of a Federal executive entity to offer a deferred resignation program or voluntary furlough opportunity to Federal employees shall exclude the FAA workforce.\n**(2) Savings clause**\nNothing in this subsection shall be construed to affect the Voluntary Separation Incentive Payments program carried out under part 576 of title 5, Code of Federal Regulations (as in effect on January 1, 2025).\n##### (c) GAO review of FAA probationary personnel terminations\n**(1) In general**\nNot later than 30 days after the date of enactment of this section, the Comptroller General shall initiate a review of each action by the President, the Secretary, the Administrator, the Director of the Office of Personnel Management, and other head, officer, or employee of a Federal executive entity during the period beginning on February 14, 2025, and ending on the date of enactment of this section to terminate an employee in a probationary period of employment of the FAA.\n**(2) Requirements**\nIn conducting the review, the Comptroller General shall evaluate\u2014\n**(A)**\nwhether a comprehensive safety risk management analysis evaluating the impacts of the proposed workforce reduction on the safety and efficiency of the national airspace system was performed by the Secretary or Administrator prior to the terminations;\n**(B)**\nwhether the President, the Secretary, the Administrator, the Director of the Office of Personnel Management, or other head, officer, or employee of a Federal executive entity made efforts to notify congressional committees of jurisdiction of the proposed and confirmed workforce reductions; and\n**(C)**\nwhether the workforce reductions resulted in a detrimental impact to the safety and efficiency of the national airspace system.\n**(3) Deadline**\nThe Comptroller General shall complete the review required by this subsection not later than 180 days after the date on which the review is initiated.\n**(4) Report**\nNot later than 60 days after the date on which the review is completed, the Comptroller General shall submit to the appropriate committees of Congress a report detailing the results of the review together with relevant findings and recommendations, including any recommendations for legislative or administrative action.\n##### (d) Prohibition on FAA staffing reductions\nThe Secretary and the Administrator shall not\u2014\n**(1)**\ncarry out a reduction in force for employees of the FAA; or\n**(2)**\nreduce the number of full-time equivalent positions at the FAA.\n#### 9. Extension of FAA air traffic controller max hiring requirement\nSection 437(a) of the FAA Reauthorization Act of 2024 ( 49 U.S.C. 44506 note) is amended by striking 2028 and inserting 2033 .\n#### 10. Air traffic controller training improvements\n##### (a) Enhanced Air Traffic Collegiate Training Initiative program\n**(1) In general**\nThe Administrator shall leverage the Collegiate Training Initiative program described in section 44506(c) of title 49, United States Code, to maintain an Enhanced Air Traffic Collegiate Training Initiative program (in this section referred to as the Enhanced Initiative ) to support the recruitment, education, and hiring of well-qualified developmental air traffic controllers.\n**(2) Requirements**\nIn maintaining the Enhanced Initiative under paragraph (1), the Administrator shall, at a minimum, include the following criteria:\n**(A)**\nSelecting and leveraging partnerships with accredited institutions of higher education (as defined in section 61.1 of title 14, Code of Federal Regulations) that administer an accredited air traffic curriculum to undergraduate students.\n**(B)**\nDetermining criteria for accredited institutions of higher education to participate in the Enhanced Initiative.\n**(C)**\nSoliciting applications from, and provide guidance to, interested accredited institutions of higher education that administer an accredited air traffic curriculum to undergraduate students, including accredited institutions that participate in the Collegiate Training Initiative, to help increase qualified accredited institutions participating in the Enhanced Initiative.\n**(3) Selection criteria**\nPrior to selecting an accredited institution of higher education for participation in the Enhanced Initiative, the Administrator shall\u2014\n**(A)**\nevaluate the institution\u2019s air traffic curriculum, including the institution\u2019s\u2014\n**(i)**\naccess to air traffic educational resources; and\n**(ii)**\nproximity and access to air traffic facilities and equipment;\n**(B)**\ncertify that each institution of higher education seeking to participate in the Enhanced Initiative has a qualified air traffic curriculum that provides, at a minimum, an equivalent level of education and training for air traffic controller trainees to that provided at the FAA Academy; and\n**(C)**\ncertify that all evaluations of students at accredited institutions of higher education seeking to participate in the Enhanced Initiative shall be conducted by FAA-approved and certified evaluators.\n**(4) Program expansion**\nThe Administrator shall establish a minimum target of certifying 15 qualified institutions of higher education that meet the criteria described in this section for selection to participate in the Enhanced Initiative. The qualified institutions of higher education selected for such minimum target shall include any institution of higher education selected and certified by the Administrator for participation in the Enhanced Initiative as of January 20, 2025.\n**(5) Hiring qualified graduates**\nThe Administrator may appoint qualified individuals who have successively completed an air traffic curriculum certified by the Administrator under paragraph (3) at a participating institution of higher education selected by the Administrator and received at least a well-qualified score on the Air Traffic Skills Assessment, or successor air traffic entrance exam, on a non-competitive basis for the position of Air Traffic Control Specialist in the excepted service (as defined in section 2103 of title 5, United States Code).\n**(6) Supporting the hiring of qualified instructors**\nUsing amounts made available under section 106(k)(1) of title 49, United States Code, the Administrator may award funds to support the recruitment and hiring of qualified faculty and FAA-approved and certified evaluators at accredited institutions of higher education that administer an accredited air traffic curriculum to undergraduate students that either\u2014\n**(A)**\nparticipate in the Collegiate Training Initiative and are interested and qualified applicants for participation in the Enhanced Initiative; or\n**(B)**\nhave been selected by the Administrator for participation in the Enhanced Initiative.\n**(7) Review of enhanced AT\u2013CTI program**\n**(A) In general**\nNot later than 5 years after the date of the enactment of this section, the Comptroller General shall initiate a study to examine the effectiveness of the Enhanced Initiative in increasing FAA air traffic controller education and training capacity and throughput to grow the FAA air traffic controller workforce.\n**(B) Contents**\nIn conducting the study under subparagraph (A), the Comptroller General shall, at a minimum, evaluate the effectiveness of the program in producing\u2014\n**(i)**\nstudents that score at least a well-qualified score on the Air Traffic Skills Assessment or successor air traffic entrance exam;\n**(ii)**\ndevelopmental controllers that enter en route and terminal air traffic environments after completing the Enhanced Initiative; and\n**(iii)**\ndevelopmental controllers that become Certified Professional Controllers.\n**(C) Consultation**\nIn conducting the study required under subparagraph (A), the Comptroller General shall consult with the FAA and appropriate stakeholders involved in overseeing, operating, and administering the Enhanced Initiative.\n**(D) Report**\nNot later than 1 year after the date the Comptroller General initiates the study under subparagraph (A), the Comptroller General shall submit to the appropriate committees of Congress and the Administrator a report describing the results of the study, together with any appropriate recommendations for legislative or administrative action.\n##### (b) Improving Aviation Medical Examiner staffing\nUsing amounts made available under section 106(k)(1) of title 49, United States Code, the Administrator shall exercise all actions necessary to hire qualified licensed medical physicians with knowledge of or a background in aerospace medicine, psychiatry, psychology, neurology, cardiology, or internal medicine in order to\u2014\n**(1)**\nincrease the Aviation Medical Examiner (as described in section 183.21 of title 14, Code of Federal Regulations) workforce; and\n**(2)**\nachieve maximum staffing capacity within the FAA Office of Aerospace Medicine.\n##### (c) Air traffic control instructor recruitment program\n**(1) In general**\nNot later than 90 days after the date of enactment of this section, the Administrator shall develop and execute an air traffic control instructor outreach and engagement program to assist with the recruitment, hiring, and retention of air traffic control instructors at the FAA Academy and at FAA air traffic control facilities with a demonstrated shortage of air traffic control personnel to provide classroom instruction or on-the-job training.\n**(2) Requirements**\nIn executing the program under paragraph (1), the Administrator shall conduct outreach and engagement activities relating to air traffic control instructor career opportunities to air traffic controllers who are within 1 year of\u2014\n**(A)**\nmeeting the age and service requirements for an annuity under sections 8336(e) and 8412(e) of title 5, United States Code; and\n**(B)**\nattaining the mandatory separation age for air traffic controllers described in sections 8335(a) and 8425(a) of title 5, United States Code.\n**(3) Consideration**\nIn developing the outreach and engagement program, the Administrator may consider the results of the study conducted in section 416 of the FAA Reauthorization Act of 2024 ( Public Law 118\u201363 , 138 Stat. 1161).\n**(4) Publication**\nIn executing the program under paragraph (1), the Administrator shall make publicly available on the website of the FAA, in a conspicuous manner, qualification criteria and hiring materials relating to air traffic control instructor careers, including active job postings for air traffic control instructors.\n#### 11. TARAM analyses\n##### (a) Assessment\n**(1) In general**\nThe Administrator shall conduct a Transport Airplane Risk Assessment Methodology (in this section referred to as TARAM ) analysis with respect to any transport airplane accidents in the United States that result in a fatality, regardless of whether an aircraft design or a manufacturing issue is believed to have contributed to the accident.\n**(2) Report**\nNot later than 30 days after conducting a TARAM analysis in accordance with paragraph (1), the Administrator shall submit to the appropriate committees of Congress a report containing the results of the analysis, together with recommendations for such legislation and administrative action as the Administrator determines appropriate.\n**(3) Employee designation**\nNot later than 60 days after the date of enactment of this section, the Administrator shall designate multiple employees of the FAA as experts for the TARAM analysis process who shall be responsible for the advocacy, maintenance, and training of TARAM guidance and processes, including updating FAA Policy Statement PS\u2013ANM\u201325\u201305, Risk Assessment Methodology for Transport Category Airplanes (dated November 4, 2011) to reflect, among other things, current National Transportation Safety Board accident rates.\n##### (b) Required updates\nNot later than 60 days after the date of enactment of this section, the Administrator shall revise FAA Policy Statement PS\u2013ANM\u201325\u201305, Risk Assessment Methodology for Transport Category Airplanes (dated November 4, 2011) and any successor policy statement in accordance with the requirements of this section.\n##### (c) Conforming amendment\nSection 130(c) of the Aircraft Certification, Safety, and Accountability Act ( Public Law 116\u2013260 ; 134 Stat. 2349) is amended to read as follows:\n(c) Required notice The Administrator shall provide notice to the congressional committees of jurisdiction on the findings and recommendations of a TARAM conducted following a transport airplane accident in which a loss of life occurred. .\n#### 12. Employee reporting\n##### (a) Whistleblower audit\n**(1) In general**\nThe Inspector General of the Department of Transportation shall initiate an audit of the FAA, including the FAA Whistleblower Protection Program, to review whether the FAA is appropriately processing and acting on submitted complaints.\n**(2) Requirement**\nThe audit conducted under paragraph (1) shall not compromise the identity of any individual who submitted a report through the Whistleblower Protection Program or the FAA Hotline of the FAA Office of Audit and Evaluation.\n##### (b) Report\nNot later than 60 days after the date of enactment of this section, the Inspector General of the Department of Transportation shall submit to the appropriate committees of Congress a report containing the results of the audit conducted under subsection (a), together with recommendations for such legislation and administrative action as the Inspector General determines appropriate.\n#### 13. Conflicts of interest\n##### (a) Interim final rule\nNot later than 60 days after the date of enactment of this section, the Secretary of Transportation shall issue an interim final rule to require strict adherence to the requirements described in section 208 of title 18, United States Code.\n##### (b) Compliance review and briefing\nNot later than 1 year after the date of enactment of this section, the Inspector General of the Department of Transportation shall review the Department of Transportation\u2019s compliance with the requirements of this section and identify any applicable conflict of interest waivers granted by the Federal Government for the Department of Transportation relating to Department of Transportation and FAA employees, contracting, acquisition, and procurement, and shall brief the appropriate committees of Congress about the findings of such review.",
      "versionDate": "2025-06-05",
      "versionType": "Introduced in Senate"
    }
  ]
}
```

## API Data: subjects

```json
{
  "subjects": [
    {
      "legislativeSubjects": "",
      "policyArea": {
        "name": "Transportation and Public Works",
        "updateDate": "2025-07-02T13:24:03Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-06-05",
    "originChamber": "Senate",
    "payload": {
      "dublinCore": {
        "contributor": "Congressional Research Service, Library of Congress",
        "description": "This file contains bill summaries for federal legislation. A bill summary describes the most significant provisions of a piece of legislation and details the effects the legislative text may have on current law and federal programs. Bill summaries are authored by the Congressional Research Service (CRS) of the Library of Congress. As stated in Public Law 91-510 (2 USC 166 (d)(6)), one of the duties of CRS is \"to prepare summaries and digests of bills and resolutions of a public general nature introduced in the Senate or House of Representatives\". For more information, refer to the User Guide that accompanies this file.",
        "format": "text/xml",
        "language": "EN",
        "rights": "Pursuant to Title 17 Section 105 of the United States Code, this file is not subject to copyright protection and is in the public domain."
      },
      "item": {
        "@attributes": {
          "congress": "119",
          "measure-id": "id119s1985",
          "measure-number": "1985",
          "measure-type": "s",
          "orig-publish-date": "2025-06-05",
          "originChamber": "SENATE",
          "update-date": "2026-03-26"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "SENATE",
            "summary-id": "id119s1985v00",
            "update-date": "2026-03-26"
          },
          "action-date": "2025-06-05",
          "action-desc": "Introduced in Senate",
          "summary-text": "<p><strong>Safe Operations of Shared Airspace Act of 2025</strong></p><p>This bill addresses aviation safety, such as through increasing\u00a0requirements for aircraft tracking,\u00a0communication, and coordination with the military. The bill also addresses\u00a0Federal Aviation Administration (FAA) workforce issues.</p><p>For example, the bill revises and increases requirements for using\u00a0Automatic Dependent Surveillance-Broadcast\u00a0(ADS-B) equipment, which transmits information (e.g., location and weather information) between aircraft and air traffic control.</p><p>Under the bill, aircraft must generally operate with ADS-B In (receiving) equipment. The FAA must issue performance requirements for the equipment to provide safety-enhancing capabilities (e.g., facilitating aircraft collision avoidance) for flight crews.</p><p>Further, current FAA regulations allow aircraft performing a sensitive government mission to be excepted from requirements for using ADS-B Out (broadcasting)\u00a0equipment. This bill limits which flights may be considered sensitive government missions (e.g., not training flights).</p><p>The FAA must also (1) establish an office to coordinate airspace usage of military aircraft, (2) review the safety of certain\u00a0flight operations and routes around airports, and (3) enter into memoranda of understanding with military agencies for safety information sharing.</p><p>The FAA must\u00a0conduct a Transport Airplane Risk Assessment Methodology analysis for any transport airplane accidents in the United States that result in a fatality.</p><p>The bill also addresses FAA workforce issues, such as by</p><ul><li>excluding the FAA workforce from a federal hiring freeze, deferred resignation program, voluntary furlough, or reduction in force;</li><li>supporting the recruitment and training of air traffic controllers; and</li><li>requiring strict adherence to federal conflict of interest requirements.</li></ul>"
        },
        "title": "Safe Operations of Shared Airspace Act of 2025"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/s/BILLSUM-119s1985.xml",
    "summary": {
      "actionDate": "2025-06-05",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Safe Operations of Shared Airspace Act of 2025</strong></p><p>This bill addresses aviation safety, such as through increasing\u00a0requirements for aircraft tracking,\u00a0communication, and coordination with the military. The bill also addresses\u00a0Federal Aviation Administration (FAA) workforce issues.</p><p>For example, the bill revises and increases requirements for using\u00a0Automatic Dependent Surveillance-Broadcast\u00a0(ADS-B) equipment, which transmits information (e.g., location and weather information) between aircraft and air traffic control.</p><p>Under the bill, aircraft must generally operate with ADS-B In (receiving) equipment. The FAA must issue performance requirements for the equipment to provide safety-enhancing capabilities (e.g., facilitating aircraft collision avoidance) for flight crews.</p><p>Further, current FAA regulations allow aircraft performing a sensitive government mission to be excepted from requirements for using ADS-B Out (broadcasting)\u00a0equipment. This bill limits which flights may be considered sensitive government missions (e.g., not training flights).</p><p>The FAA must also (1) establish an office to coordinate airspace usage of military aircraft, (2) review the safety of certain\u00a0flight operations and routes around airports, and (3) enter into memoranda of understanding with military agencies for safety information sharing.</p><p>The FAA must\u00a0conduct a Transport Airplane Risk Assessment Methodology analysis for any transport airplane accidents in the United States that result in a fatality.</p><p>The bill also addresses FAA workforce issues, such as by</p><ul><li>excluding the FAA workforce from a federal hiring freeze, deferred resignation program, voluntary furlough, or reduction in force;</li><li>supporting the recruitment and training of air traffic controllers; and</li><li>requiring strict adherence to federal conflict of interest requirements.</li></ul>",
      "updateDate": "2026-03-26",
      "versionCode": "id119s1985"
    },
    "title": "Safe Operations of Shared Airspace Act of 2025"
  },
  "summaries": [
    {
      "actionDate": "2025-06-05",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Safe Operations of Shared Airspace Act of 2025</strong></p><p>This bill addresses aviation safety, such as through increasing\u00a0requirements for aircraft tracking,\u00a0communication, and coordination with the military. The bill also addresses\u00a0Federal Aviation Administration (FAA) workforce issues.</p><p>For example, the bill revises and increases requirements for using\u00a0Automatic Dependent Surveillance-Broadcast\u00a0(ADS-B) equipment, which transmits information (e.g., location and weather information) between aircraft and air traffic control.</p><p>Under the bill, aircraft must generally operate with ADS-B In (receiving) equipment. The FAA must issue performance requirements for the equipment to provide safety-enhancing capabilities (e.g., facilitating aircraft collision avoidance) for flight crews.</p><p>Further, current FAA regulations allow aircraft performing a sensitive government mission to be excepted from requirements for using ADS-B Out (broadcasting)\u00a0equipment. This bill limits which flights may be considered sensitive government missions (e.g., not training flights).</p><p>The FAA must also (1) establish an office to coordinate airspace usage of military aircraft, (2) review the safety of certain\u00a0flight operations and routes around airports, and (3) enter into memoranda of understanding with military agencies for safety information sharing.</p><p>The FAA must\u00a0conduct a Transport Airplane Risk Assessment Methodology analysis for any transport airplane accidents in the United States that result in a fatality.</p><p>The bill also addresses FAA workforce issues, such as by</p><ul><li>excluding the FAA workforce from a federal hiring freeze, deferred resignation program, voluntary furlough, or reduction in force;</li><li>supporting the recruitment and training of air traffic controllers; and</li><li>requiring strict adherence to federal conflict of interest requirements.</li></ul>",
      "updateDate": "2026-03-26",
      "versionCode": "id119s1985"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-06-05",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1985is.xml"
        }
      ],
      "type": "Introduced in Senate"
    }
  ]
}
```

## API Data: titles

```json
{
  "titles": [
    {
      "title": "Safe Operations of Shared Airspace Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-10-23T11:18:16Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Safe Operations of Shared Airspace Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-06-18T05:23:17Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to improve aviation safety, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-06-18T05:18:20Z"
    }
  ]
}
```
