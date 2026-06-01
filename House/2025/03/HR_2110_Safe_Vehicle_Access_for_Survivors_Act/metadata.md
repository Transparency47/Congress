# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/2110?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/2110
- Title: Safe Vehicle Access for Survivors Act
- Congress: 119
- Bill type: HR
- Bill number: 2110
- Origin chamber: House
- Introduced date: 2025-03-14
- Update date: 2026-03-27T08:06:49Z
- Update date including text: 2026-03-27T08:06:49Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-03-14: Introduced in House
- 2025-03-14 - IntroReferral: Introduced in House
- 2025-03-14 - IntroReferral: Introduced in House
- 2025-03-14 - IntroReferral: Referred to the House Committee on Energy and Commerce.
- 2025-03-14 - Committee: Referred to the Subcommittee on Commerce, Manufacturing, and Trade.
- 2026-02-10 - Committee: Forwarded by Subcommittee to Full Committee by Voice Vote.
- 2026-02-10 - Committee: Subcommittee Consideration and Mark-up Session Held
- Latest action: 2025-03-14: Introduced in House

## Actions

- 2025-03-14 - IntroReferral: Introduced in House
- 2025-03-14 - IntroReferral: Introduced in House
- 2025-03-14 - IntroReferral: Referred to the House Committee on Energy and Commerce.
- 2025-03-14 - Committee: Referred to the Subcommittee on Commerce, Manufacturing, and Trade.
- 2026-02-10 - Committee: Forwarded by Subcommittee to Full Committee by Voice Vote.
- 2026-02-10 - Committee: Subcommittee Consideration and Mark-up Session Held

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-03-14",
    "latestAction": {
      "actionDate": "2025-03-14",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/2110",
    "number": "2110",
    "originChamber": "House",
    "policyArea": {
      "name": "Science, Technology, Communications"
    },
    "sponsors": [
      {
        "bioguideId": "D000624",
        "district": "6",
        "firstName": "Debbie",
        "fullName": "Rep. Dingell, Debbie [D-MI-6]",
        "lastName": "Dingell",
        "party": "D",
        "state": "MI"
      }
    ],
    "title": "Safe Vehicle Access for Survivors Act",
    "type": "HR",
    "updateDate": "2026-03-27T08:06:49Z",
    "updateDateIncludingText": "2026-03-27T08:06:49Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-02-10",
      "committees": {
        "item": {
          "name": "Commerce, Manufacturing, and Trade Subcommittee",
          "systemCode": "hsif17"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Forwarded by Subcommittee to Full Committee by Voice Vote.",
      "type": "Committee"
    },
    {
      "actionDate": "2026-02-10",
      "committees": {
        "item": {
          "name": "Commerce, Manufacturing, and Trade Subcommittee",
          "systemCode": "hsif17"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Subcommittee Consideration and Mark-up Session Held",
      "type": "Committee"
    },
    {
      "actionDate": "2025-03-14",
      "committees": {
        "item": {
          "name": "Commerce, Manufacturing, and Trade Subcommittee",
          "systemCode": "hsif17"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Referred to the Subcommittee on Commerce, Manufacturing, and Trade.",
      "type": "Committee"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-03-14",
      "committees": {
        "item": {
          "name": "Energy and Commerce Committee",
          "systemCode": "hsif00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Energy and Commerce.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-03-14",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-03-14",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
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
          "date": "2025-03-14T13:07:15Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Energy and Commerce Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": [
              {
                "date": "2026-02-10T20:53:37Z",
                "name": "Reported by"
              },
              {
                "date": "2026-02-10T20:53:07Z",
                "name": "Markup by"
              },
              {
                "date": "2025-03-14T19:52:45Z",
                "name": "Referred to"
              }
            ]
          },
          "name": "Commerce, Manufacturing, and Trade Subcommittee",
          "systemCode": "hsif17"
        }
      },
      "systemCode": "hsif00",
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
      "bioguideId": "C001120",
      "district": "2",
      "firstName": "Dan",
      "fullName": "Rep. Crenshaw, Dan [R-TX-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Crenshaw",
      "party": "R",
      "sponsorshipDate": "2025-03-14",
      "state": "TX"
    },
    {
      "bioguideId": "M001241",
      "district": "47",
      "firstName": "Dave",
      "fullName": "Rep. Min, Dave [D-CA-47]",
      "isOriginalCosponsor": "True",
      "lastName": "Min",
      "party": "D",
      "sponsorshipDate": "2025-03-14",
      "state": "CA"
    },
    {
      "bioguideId": "T000488",
      "district": "13",
      "firstName": "Shri",
      "fullName": "Rep. Thanedar, Shri [D-MI-13]",
      "isOriginalCosponsor": "True",
      "lastName": "Thanedar",
      "party": "D",
      "sponsorshipDate": "2025-03-14",
      "state": "MI"
    },
    {
      "bioguideId": "R000305",
      "district": "2",
      "firstName": "Deborah",
      "fullName": "Rep. Ross, Deborah K. [D-NC-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Ross",
      "middleName": "K.",
      "party": "D",
      "sponsorshipDate": "2025-03-14",
      "state": "NC"
    },
    {
      "bioguideId": "T000481",
      "district": "12",
      "firstName": "Rashida",
      "fullName": "Rep. Tlaib, Rashida [D-MI-12]",
      "isOriginalCosponsor": "True",
      "lastName": "Tlaib",
      "party": "D",
      "sponsorshipDate": "2025-03-14",
      "state": "MI"
    },
    {
      "bioguideId": "S001226",
      "district": "6",
      "firstName": "Andrea",
      "fullName": "Rep. Salinas, Andrea [D-OR-6]",
      "isOriginalCosponsor": "True",
      "lastName": "Salinas",
      "party": "D",
      "sponsorshipDate": "2025-03-14",
      "state": "OR"
    },
    {
      "bioguideId": "J000288",
      "district": "4",
      "firstName": "Henry",
      "fullName": "Rep. Johnson, Henry C. \"Hank\" [D-GA-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Johnson",
      "middleName": "C. \"Hank\"",
      "party": "D",
      "sponsorshipDate": "2025-03-14",
      "state": "GA"
    },
    {
      "bioguideId": "T000468",
      "district": "1",
      "firstName": "Dina",
      "fullName": "Rep. Titus, Dina [D-NV-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Titus",
      "party": "D",
      "sponsorshipDate": "2025-03-14",
      "state": "NV"
    },
    {
      "bioguideId": "G000583",
      "district": "5",
      "firstName": "Josh",
      "fullName": "Rep. Gottheimer, Josh [D-NJ-5]",
      "isOriginalCosponsor": "True",
      "lastName": "Gottheimer",
      "party": "D",
      "sponsorshipDate": "2025-03-14",
      "state": "NJ"
    },
    {
      "bioguideId": "M001160",
      "district": "4",
      "firstName": "Gwen",
      "fullName": "Rep. Moore, Gwen [D-WI-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Moore",
      "party": "D",
      "sponsorshipDate": "2025-03-14",
      "state": "WI"
    },
    {
      "bioguideId": "S001185",
      "district": "7",
      "firstName": "Terri",
      "fullName": "Rep. Sewell, Terri A. [D-AL-7]",
      "isOriginalCosponsor": "True",
      "lastName": "Sewell",
      "middleName": "A.",
      "party": "D",
      "sponsorshipDate": "2025-03-14",
      "state": "AL"
    },
    {
      "bioguideId": "N000147",
      "district": "0",
      "firstName": "Eleanor",
      "fullName": "Del. Norton, Eleanor Holmes [D-DC-At Large]",
      "isOriginalCosponsor": "True",
      "lastName": "Norton",
      "middleName": "Holmes",
      "party": "D",
      "sponsorshipDate": "2025-03-14",
      "state": "DC"
    },
    {
      "bioguideId": "S001215",
      "district": "11",
      "firstName": "Haley",
      "fullName": "Rep. Stevens, Haley M. [D-MI-11]",
      "isOriginalCosponsor": "True",
      "lastName": "Stevens",
      "middleName": "M.",
      "party": "D",
      "sponsorshipDate": "2025-03-14",
      "state": "MI"
    },
    {
      "bioguideId": "M001196",
      "district": "6",
      "firstName": "Seth",
      "fullName": "Rep. Moulton, Seth [D-MA-6]",
      "isOriginalCosponsor": "False",
      "lastName": "Moulton",
      "party": "D",
      "sponsorshipDate": "2025-03-24",
      "state": "MA"
    },
    {
      "bioguideId": "S001216",
      "district": "8",
      "firstName": "Kim",
      "fullName": "Rep. Schrier, Kim [D-WA-8]",
      "isOriginalCosponsor": "False",
      "lastName": "Schrier",
      "party": "D",
      "sponsorshipDate": "2025-03-24",
      "state": "WA"
    },
    {
      "bioguideId": "L000602",
      "district": "12",
      "firstName": "Summer",
      "fullName": "Rep. Lee, Summer L. [D-PA-12]",
      "isOriginalCosponsor": "False",
      "lastName": "Lee",
      "middleName": "L.",
      "party": "D",
      "sponsorshipDate": "2025-03-24",
      "state": "PA"
    },
    {
      "bioguideId": "F000466",
      "district": "1",
      "firstName": "Brian",
      "fullName": "Rep. Fitzpatrick, Brian K. [R-PA-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Fitzpatrick",
      "middleName": "K.",
      "party": "R",
      "sponsorshipDate": "2025-03-24",
      "state": "PA"
    },
    {
      "bioguideId": "P000608",
      "district": "50",
      "firstName": "Scott",
      "fullName": "Rep. Peters, Scott H. [D-CA-50]",
      "isOriginalCosponsor": "False",
      "lastName": "Peters",
      "middleName": "H.",
      "party": "D",
      "sponsorshipDate": "2025-03-27",
      "state": "CA"
    },
    {
      "bioguideId": "F000483",
      "district": "30",
      "firstName": "Laura",
      "fullName": "Rep. Friedman, Laura [D-CA-30]",
      "isOriginalCosponsor": "False",
      "lastName": "Friedman",
      "party": "D",
      "sponsorshipDate": "2025-03-31",
      "state": "CA"
    },
    {
      "bioguideId": "M001237",
      "district": "8",
      "firstName": "Kristen",
      "fullName": "Rep. McDonald Rivet, Kristen [D-MI-8]",
      "isOriginalCosponsor": "False",
      "lastName": "McDonald Rivet",
      "party": "D",
      "sponsorshipDate": "2025-04-01",
      "state": "MI"
    },
    {
      "bioguideId": "S001223",
      "district": "13",
      "firstName": "Emilia",
      "fullName": "Rep. Sykes, Emilia Strong [D-OH-13]",
      "isOriginalCosponsor": "False",
      "lastName": "Sykes",
      "middleName": "Strong",
      "party": "D",
      "sponsorshipDate": "2025-04-03",
      "state": "OH"
    },
    {
      "bioguideId": "S001200",
      "district": "9",
      "firstName": "Darren",
      "fullName": "Rep. Soto, Darren [D-FL-9]",
      "isOriginalCosponsor": "False",
      "lastName": "Soto",
      "party": "D",
      "sponsorshipDate": "2025-04-03",
      "state": "FL"
    },
    {
      "bioguideId": "L000601",
      "district": "1",
      "firstName": "Greg",
      "fullName": "Rep. Landsman, Greg [D-OH-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Landsman",
      "party": "D",
      "sponsorshipDate": "2025-06-20",
      "state": "OH"
    },
    {
      "bioguideId": "M001238",
      "district": "0",
      "firstName": "Sarah",
      "fullName": "Rep. McBride, Sarah [D-DE-At Large]",
      "isOriginalCosponsor": "False",
      "lastName": "McBride",
      "party": "D",
      "sponsorshipDate": "2025-06-25",
      "state": "DE"
    },
    {
      "bioguideId": "M001225",
      "district": "15",
      "firstName": "Kevin",
      "fullName": "Rep. Mullin, Kevin [D-CA-15]",
      "isOriginalCosponsor": "False",
      "lastName": "Mullin",
      "party": "D",
      "sponsorshipDate": "2025-07-10",
      "state": "CA"
    },
    {
      "bioguideId": "N000188",
      "district": "1",
      "firstName": "Donald",
      "fullName": "Rep. Norcross, Donald [D-NJ-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Norcross",
      "party": "D",
      "sponsorshipDate": "2026-03-09",
      "state": "NJ"
    },
    {
      "bioguideId": "P000607",
      "district": "2",
      "firstName": "Mark",
      "fullName": "Rep. Pocan, Mark [D-WI-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Pocan",
      "party": "D",
      "sponsorshipDate": "2026-03-26",
      "state": "WI"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr2110ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 2110\nIN THE HOUSE OF REPRESENTATIVES\nMarch 14, 2025 Mrs. Dingell (for herself, Mr. Crenshaw , Mr. Min , Mr. Thanedar , Ms. Ross , Ms. Tlaib , Ms. Salinas , Mr. Johnson of Georgia , Ms. Titus , Mr. Gottheimer , Ms. Moore of Wisconsin , Ms. Sewell , Ms. Norton , and Ms. Stevens ) introduced the following bill; which was referred to the Committee on Energy and Commerce\nA BILL\nTo establish a process for survivors to request the termination or disabling of connected vehicle services that abusers misuse, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Safe Vehicle Access for Survivors Act .\n#### 2. Definitions\nIn this Act:\n**(1) Abuser**\nThe term abuser means an individual identified by a survivor, pursuant to section 4, who has committed or allegedly committed a covered act against a survivor making a connected vehicle services request.\n**(2) Account holder**\nThe term account holder means an individual who is\u2014\n**(A)**\na party to a contract with a covered provider that involves a connected vehicle service; or\n**(B)**\na subscriber, customer, or registered user of a connected vehicle service.\n**(3) Connected vehicle service**\nThe term connected vehicle service means any capability provided by or on behalf of a motor vehicle manufacturer or affiliate that enables a person to remotely obtain data from or send commands to a covered vehicle, which may be accomplished through a software application that is designed to be operated on a mobile device or computer.\n**(4) Connected vehicle service request**\nThe term connected vehicle service request means a request by a survivor to terminate or disable an abuser\u2019s access to a connected vehicle service.\n**(5) Covered act**\n**(A) In general**\nThe term covered act means conduct that constitutes\u2014\n**(i)**\na crime described in section 40002(a) of the Violence Against Women Act of 1994 ( 34 U.S.C. 12291(a) ), including domestic violence, dating violence, sexual assault, stalking, and sex trafficking;\n**(ii)**\nan act or practice described in paragraph (11) or (12) of section 103 of the Trafficking Victims Protection Act of 2000 ( 22 U.S.C. 7102 ) (relating to severe forms of trafficking in persons and sex trafficking, respectively); or\n**(iii)**\nan act under State law, Tribal law, or the Uniform Code of Military Justice that is similar to an offense described in clause (i) or (ii).\n**(B) Conviction not required**\nNothing in paragraph (1) shall be construed to require a criminal conviction or any other determination of a court in order for conduct to constitute a covered act.\n**(6) Covered connected vehicle service account**\nThe term covered connected vehicle services account means an account or other means by which a person enrolls in or obtains access to a connected vehicle service.\n**(7) Covered provider**\nThe term covered provider means a motor vehicle manufacturer, affiliate, or an entity acting on behalf of the motor vehicle manufacturer that provides a connected vehicle service.\n**(8) Covered vehicle**\nThe term covered vehicle means a motor vehicle that is the subject of a connected vehicle request and identified by a survivor pursuant to section 4.\n**(9) Emergency situation**\nThe term emergency situation means a situation that if allowed to continue poses an imminent threat of serious bodily harm or death to an individual.\n**(10) In-vehicle interface**\nThe term in-vehicle interface means a feature or mechanism installed in a vehicle that allows a person within the vehicle to terminate or disconnect connected vehicle services.\n**(11) Survivor**\nThe term survivor means an individual who is not less than 18 years old and against whom a covered act has been committed or allegedly committed.\n**(12) Affiliate**\nThe term affiliate means any company that controls, is controlled by, or is under common control with another company.\n#### 3. Protection of survivors\n##### (a) In general\nNotwithstanding an abuser being an account holder, not later than 2 business days after receiving a connected vehicle service request from a survivor pursuant to section 4, a covered provider shall take 1 or more of the following actions\u2014\n**(1)**\nterminate or disable a covered connected vehicle service account associated with an abuser identified in the connected vehicle service request pursuant to section 4;\n**(2)**\nterminate or disable a covered connected vehicle service account associated with the covered vehicle, including by resetting or deleting any data or wireless connection with respect to the covered vehicle, and provide instructions to the survivor on how to re-establish a connected vehicle service account that does not include access by the abuser;\n**(3)**\nterminate or disable covered connected vehicle services for the covered vehicle, including by resetting or deleting any data or wireless connection with respect to the covered vehicle, and provide instructions to the survivor on how to re-establish connected vehicle services; or\n**(4)**\nif the vehicle has an in-vehicle interface, provide information to the survivor about the availability of the in-vehicle interface and how to terminate or disable connected vehicle services using the in-vehicle interface.\n##### (b) Access to account data\nIf a covered provider takes action under subsection (a) in response to a connected vehicle service request, the covered provider shall deny a request from the abuser to obtain any data connected to the connected vehicle service maintained by the covered provider that was generated after the abuser\u2019s access to the connected vehicle services was terminated or disabled following a connected vehicle service request.\n##### (c) Limitations on penalties, fees, and other requirements\nA covered provider may not make any action undertaken pursuant to subsection (a) contingent on any requirement other than the requirements under section 4, including\u2014\n**(1)**\npayment of a fee, penalty, or other charge;\n**(2)**\nmaintaining or extending the term of a connected vehicle service account;\n**(3)**\napproval of the change by the account holder, if the account holder is not the survivor; or\n**(4)**\nan increase in the rate charged for the connected vehicle service.\n##### (d) Notice to survivor\n**(1) In general**\nIf a covered provider intends to provide any formal notice to the abuser regarding any action undertaken pursuant to subsection (a), the covered provider shall notify the survivor of the date on which the covered provider intends to give such notice to the abuser.\n**(2) Timing**\nA covered provider shall take reasonable steps to provide any formal notice to an abuser pursuant to paragraph (1)\u2014\n**(A)**\nno less than 3 days after the survivor has been notified; and\n**(B)**\nonly after the abuser\u2019s access to the connected vehicle service has been terminated or disabled.\n**(3) Manner of contact**\nWhen completing a connected vehicle service request, a covered provider shall allow the survivor to elect the manner in which the covered provider may\u2014\n**(A)**\ncontact the survivor in response to the request, if necessary; or\n**(B)**\nnotify the survivor of the inability of the covered provider to complete the connected vehicle service request.\n##### (e) Technical infeasibility\n**(1) In general**\nThe requirement to effectuate the requested action in subsection (a) shall not apply to a covered provider if the covered provider cannot operationally or technically effectuate the request.\n**(2) Notification**\nIf a covered provider cannot operationally or technically effectuate the request as described in paragraph (1), the covered provider shall\u2014\n**(A)**\npromptly notify the survivor who submitted the connected vehicle service request of that infeasibility; and\n**(B)**\nprovide the survivor with information about whether the operational or technical infeasibility can be remedied and, if so, any steps the survivor can take to assist in remedying such infeasibility.\n#### 4. Connected vehicle service requests\n##### (a) In general\nWhen making a connected vehicle service request under this Act, the survivor shall provide\u2014\n**(1)**\nthe vehicle identification number of the covered vehicle;\n**(2)**\nthe name of the abuser subject to the connected vehicle service request; and\n**(3)**\neither\u2014\n**(A)**\nproof of sole ownership of the covered vehicle; or\n**(B)**\nin the case of a vehicle that is not solely owned by the survivor\u2014\n**(i)**\nproof of exclusive legal possession of the vehicle, which may take the form of a court order awarding possession of the vehicle to the survivor; or\n**(ii)**\nin the case of a vehicle that is owned in whole or in part by the abuser, a dissolution decree, temporary order, or domestic violence restraining order naming the abuser if the decree or order grants possession of the covered vehicle to the survivor or restricts the abuser\u2019s use of a connected vehicle service against the survivor.\n##### (b) Confidential and secure treatment of personal information\n**(1) In general**\nA covered provider and any officer, director, employee, vendor, or agent thereof shall treat any information submitted by a survivor under subsection (a) as confidential and securely dispose of the information not later than 90 days after receiving the information.\n**(2) Prohibition on sharing**\nA covered provider is prohibited from sharing information submitted by a survivor under subsection (a) with any third party without the affirmative consent of the survivor unless such sharing is required to effectuate a connected vehicle service request under subsection (a).\n**(3) Information provided by survivor**\nA covered provider shall not require a survivor to provide any information other than what is required in subdivision (a) to establish the ability to terminate an abuser\u2019s access to connected vehicle services.\n**(4) Rule of construction**\n**(A) In general**\nNothing in paragraph (1) shall be construed to prohibit a covered provider from maintaining, for longer than the period specified in that paragraph, a record that verifies that a survivor fulfilled the conditions of a connected vehicle service request under subsection (a).\n**(B) Data minimization**\nThe data maintained under subparagraph (A) shall be limited to that which is reasonably necessary and proportionate to verify that a survivor fulfilled the conditions of a connected vehicle service request.\n##### (c) Minimum obligations\nThe requirements in this Act shall not prohibit or prevent a covered provider from terminating or disabling an abuser\u2019s access to connected vehicle services in emergency situations after receiving a connected vehicle service request.\n##### (d) Changes in ownership or possession\nThe survivor shall take reasonable steps to notify the covered provider of any change in ownership or possession from what was provided under subsection (a) when the connected vehicle service request was made that materially impacts the need for action taken by the covered provider under subsection 3(a).\n#### 5. Consumer notices\n##### (a) In general\nTo enhance transparency and communication, a covered provider shall make information about how survivors can safely make connected vehicle service requests on a publicly available, user-friendly website maintained by a covered provider, including\u2014\n**(1) Confirmation email**\nUpon submission of a connected vehicle service request, the covered provider shall automatically send a confirmation email to the survivor, acknowledging the receipt of the connected vehicle service request. This email shall contain a reference number for the request and an outline of the subsequent steps in the process.\n**(2) Action or resolution alert**\nUpon completion of review of the request, the survivor shall be informed of the action taken, including the termination of access to the connected vehicle service or if additional information is needed. This alert shall clearly state any relevant details or further actions required from the survivor.\n**(3) Explanation and assistance**\nIn the event of a connected vehicle service request\u2019s approval, the covered provider shall provide the survivor with a clear explanation and guidance on how to create their own app account, if necessary, to ensure that the survivor can maintain control over the connected vehicle service once the person\u2019s access to the service has been terminated.\n**(4) Opt-out measures**\nIn the event that an abuser still has access to a survivor\u2019s email account, the covered provider shall provide the option to opt-out of receiving notices regarding the connected vehicle service request process, and to the best of their ability, provide alternative options for the survivor to maintain a record of the request process.\n#### 6. Liability protection\nA covered provider and any officer, director, employee, vendor, or agent thereof shall not be subject to liability for any claims deriving from an action taken or omission made with respect to compliance with this Act.\n#### 7. Effective date\nA covered provider\u2014\n**(1)**\nmay comply with this Act beginning on the date of enactment; and\n**(2)**\nshall comply with this Act no later than 180 days after the date of enactment.\n#### 8. Effect on other laws\nNo state or political subdivision of a State may adopt, maintain, enforce, prescribe, or continue in effect any law, regulation, rule, standard, requirement, or other provision having the force and effect of law of any State, or political subdivision of a State, covered by or related to the provisions of this Act, or a rule, regulation or requirement promulgated under this Act.\n#### 9. Rulemaking\n##### (a) Rulemaking proceeding required\nNot later than 180 days after the date of enactment of this Act, the Federal Communications Commission, in consultation with the National Highway Traffic Safety Administration, shall issue a notice of proposed rulemaking to prescribe how covered providers address connected vehicle service requests and covered acts in accordance with this Act, including, but not limited to\u2014\n**(1)**\nimplementation of a reporting and notification process that swiftly revokes or disables an abuser\u2019s access to a survivor\u2019s data and takes into account\u2014\n**(A)**\nthe heightened risk to a survivor for abuse and retaliation upon reporting,\n**(B)**\nthe need for confidentiality in the reporting process,\n**(C)**\nthe ability to remove sensitive data that has already been stored in the connected vehicle service, and\n**(D)**\nthe ability of an abuser to utilize other methods, such as a service request, to access a survivors\u2019 data.\n**(2)**\nmethods, as the Federal Communications Commission deems reasonable, to notify account holders of connected vehicle services of\u2014\n**(A)**\nthe options available to enhance safety and privacy of their experience with the service, and\n**(B)**\nwho can access their data and to what extent they can control that access.\n##### (b) Regulations\nNot later than 2 years after the date of enactment of this Act, the Federal Communications Commission, in consultation with the National Highway Traffic Safety Administration, shall conclude the rulemaking proceeding initiated under subsection (a) and shall prescribe regulations to implement the provisions regarding how covered providers address connected vehicle service requests and covered acts in accordance with this Act.",
      "versionDate": "2025-03-14",
      "versionType": "Introduced in House"
    }
  ]
}
```

## API Data: subjects

```json
{
  "subjects": [
    {
      "legislativeSubjects": {
        "item": [
          {
            "name": "Domestic violence and child abuse",
            "updateDate": "2026-02-17T19:21:50Z"
          },
          {
            "name": "Emergency communications systems",
            "updateDate": "2026-02-17T19:22:12Z"
          },
          {
            "name": "Human trafficking",
            "updateDate": "2026-02-17T19:23:45Z"
          },
          {
            "name": "Motor vehicles",
            "updateDate": "2026-02-17T19:21:58Z"
          },
          {
            "name": "Right of privacy",
            "updateDate": "2026-02-17T19:22:45Z"
          },
          {
            "name": "Sex offenses",
            "updateDate": "2026-02-17T19:23:54Z"
          }
        ]
      },
      "policyArea": {
        "name": "Science, Technology, Communications",
        "updateDate": "2025-04-01T18:37:29Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-03-14",
    "originChamber": "House",
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
          "measure-id": "id119hr2110",
          "measure-number": "2110",
          "measure-type": "hr",
          "orig-publish-date": "2025-03-14",
          "originChamber": "HOUSE",
          "update-date": "2026-01-23"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr2110v00",
            "update-date": "2026-01-23"
          },
          "action-date": "2025-03-14",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Safe Vehicle Access for Survivors Act</strong></p><p>This bill requires providers of connected vehicle services, upon the request of a domestic violence survivor, to terminate or disable an identified domestic abuser\u2019s access to a vehicle\u2019s connected capabilities and data.</p><p>Specifically, within two business days of receiving a request from a survivor, a covered provider must, if technically feasible (1) terminate or disable the connected vehicle account associated with the identified abuser or the relevant vehicle, or the vehicle\u2019s connected capabilities; or (2) instruct the survivor on how to terminate or disable connected services directly.</p><p>Covered providers may not make the termination of connected vehicle services or accounts contingent on any requirement other than the provision of specified information by the survivor. For example, a provider may not require a survivor to pay a fee or extend their contract with the provider.</p><p>Under the bill, an <em>abuser</em> is an individual identified by a survivor who committed or allegedly committed certain acts against the survivor, including domestic violence, sexual assault, stalking, and sex trafficking. A <em>survivor</em> is an adult against whom such an act was committed. Further, a <em>covered provider</em> is a vehicle manufacturer, affiliate, or entity acting on behalf of a manufacturer that provides a connected vehicle service. <em>Connected vehicle service</em> is any capability that enables a person to remotely access data from or send commands to a vehicle.</p><p>Finally, the Federal Communications Commission must prescribe regulations governing how covered providers address survivors\u2019 requests related to connected vehicles.</p>"
        },
        "title": "Safe Vehicle Access for Survivors Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr2110.xml",
    "summary": {
      "actionDate": "2025-03-14",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Safe Vehicle Access for Survivors Act</strong></p><p>This bill requires providers of connected vehicle services, upon the request of a domestic violence survivor, to terminate or disable an identified domestic abuser\u2019s access to a vehicle\u2019s connected capabilities and data.</p><p>Specifically, within two business days of receiving a request from a survivor, a covered provider must, if technically feasible (1) terminate or disable the connected vehicle account associated with the identified abuser or the relevant vehicle, or the vehicle\u2019s connected capabilities; or (2) instruct the survivor on how to terminate or disable connected services directly.</p><p>Covered providers may not make the termination of connected vehicle services or accounts contingent on any requirement other than the provision of specified information by the survivor. For example, a provider may not require a survivor to pay a fee or extend their contract with the provider.</p><p>Under the bill, an <em>abuser</em> is an individual identified by a survivor who committed or allegedly committed certain acts against the survivor, including domestic violence, sexual assault, stalking, and sex trafficking. A <em>survivor</em> is an adult against whom such an act was committed. Further, a <em>covered provider</em> is a vehicle manufacturer, affiliate, or entity acting on behalf of a manufacturer that provides a connected vehicle service. <em>Connected vehicle service</em> is any capability that enables a person to remotely access data from or send commands to a vehicle.</p><p>Finally, the Federal Communications Commission must prescribe regulations governing how covered providers address survivors\u2019 requests related to connected vehicles.</p>",
      "updateDate": "2026-01-23",
      "versionCode": "id119hr2110"
    },
    "title": "Safe Vehicle Access for Survivors Act"
  },
  "summaries": [
    {
      "actionDate": "2025-03-14",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Safe Vehicle Access for Survivors Act</strong></p><p>This bill requires providers of connected vehicle services, upon the request of a domestic violence survivor, to terminate or disable an identified domestic abuser\u2019s access to a vehicle\u2019s connected capabilities and data.</p><p>Specifically, within two business days of receiving a request from a survivor, a covered provider must, if technically feasible (1) terminate or disable the connected vehicle account associated with the identified abuser or the relevant vehicle, or the vehicle\u2019s connected capabilities; or (2) instruct the survivor on how to terminate or disable connected services directly.</p><p>Covered providers may not make the termination of connected vehicle services or accounts contingent on any requirement other than the provision of specified information by the survivor. For example, a provider may not require a survivor to pay a fee or extend their contract with the provider.</p><p>Under the bill, an <em>abuser</em> is an individual identified by a survivor who committed or allegedly committed certain acts against the survivor, including domestic violence, sexual assault, stalking, and sex trafficking. A <em>survivor</em> is an adult against whom such an act was committed. Further, a <em>covered provider</em> is a vehicle manufacturer, affiliate, or entity acting on behalf of a manufacturer that provides a connected vehicle service. <em>Connected vehicle service</em> is any capability that enables a person to remotely access data from or send commands to a vehicle.</p><p>Finally, the Federal Communications Commission must prescribe regulations governing how covered providers address survivors\u2019 requests related to connected vehicles.</p>",
      "updateDate": "2026-01-23",
      "versionCode": "id119hr2110"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-03-14",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr2110ih.xml"
        }
      ],
      "type": "Introduced in House"
    }
  ]
}
```

## API Data: titles

```json
{
  "titles": [
    {
      "title": "Safe Vehicle Access for Survivors Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-04-03T13:59:02Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Safe Vehicle Access for Survivors Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-04-01T13:23:17Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To establish a process for survivors to request the termination or disabling of connected vehicle services that abusers misuse, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-04-01T13:18:26Z"
    }
  ]
}
```
