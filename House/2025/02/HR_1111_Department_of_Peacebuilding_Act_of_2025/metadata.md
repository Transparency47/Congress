# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/1111?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/1111
- Title: Department of Peacebuilding Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 1111
- Origin chamber: House
- Introduced date: 2025-02-07
- Update date: 2026-04-28T08:06:24Z
- Update date including text: 2026-04-28T08:06:24Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-02-07: Introduced in House
- 2025-02-07 - IntroReferral: Introduced in House
- 2025-02-07 - IntroReferral: Introduced in House
- 2025-02-07 - IntroReferral: Referred to the House Committee on Oversight and Government Reform.
- Latest action: 2025-02-07: Introduced in House

## Actions

- 2025-02-07 - IntroReferral: Introduced in House
- 2025-02-07 - IntroReferral: Introduced in House
- 2025-02-07 - IntroReferral: Referred to the House Committee on Oversight and Government Reform.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-02-07",
    "latestAction": {
      "actionDate": "2025-02-07",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/1111",
    "number": "1111",
    "originChamber": "House",
    "policyArea": {
      "name": "Government Operations and Politics"
    },
    "sponsors": [
      {
        "bioguideId": "O000173",
        "district": "5",
        "firstName": "Ilhan",
        "fullName": "Rep. Omar, Ilhan [D-MN-5]",
        "lastName": "Omar",
        "party": "D",
        "state": "MN"
      }
    ],
    "title": "Department of Peacebuilding Act of 2025",
    "type": "HR",
    "updateDate": "2026-04-28T08:06:24Z",
    "updateDateIncludingText": "2026-04-28T08:06:24Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-02-07",
      "committees": {
        "item": {
          "name": "Oversight and Government Reform Committee",
          "systemCode": "hsgo00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Oversight and Government Reform.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-02-07",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-02-07",
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
          "date": "2025-02-07T14:00:30Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Oversight and Government Reform Committee",
      "systemCode": "hsgo00",
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
      "bioguideId": "B001278",
      "district": "1",
      "firstName": "Suzanne",
      "fullName": "Rep. Bonamici, Suzanne [D-OR-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Bonamici",
      "party": "D",
      "sponsorshipDate": "2025-02-07",
      "state": "OR"
    },
    {
      "bioguideId": "C001072",
      "district": "7",
      "firstName": "Andr\u00e9",
      "fullName": "Rep. Carson, Andr\u00e9 [D-IN-7]",
      "isOriginalCosponsor": "True",
      "lastName": "Carson",
      "party": "D",
      "sponsorshipDate": "2025-02-07",
      "state": "IN"
    },
    {
      "bioguideId": "G000586",
      "district": "4",
      "firstName": "Jes\u00fas",
      "fullName": "Rep. Garc\u00eda, Jes\u00fas G. \"Chuy\" [D-IL-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Garc\u00eda",
      "middleName": "G. \"Chuy\"",
      "party": "D",
      "sponsorshipDate": "2025-02-07",
      "state": "IL"
    },
    {
      "bioguideId": "G000551",
      "district": "7",
      "firstName": "Ra\u00fal",
      "fullName": "Rep. Grijalva, Ra\u00fal M. [D-AZ-7]",
      "isOriginalCosponsor": "True",
      "lastName": "Grijalva",
      "middleName": "M.",
      "party": "D",
      "sponsorshipDate": "2025-02-07",
      "state": "AZ"
    },
    {
      "bioguideId": "J000309",
      "district": "1",
      "firstName": "Jonathan",
      "fullName": "Rep. Jackson, Jonathan L. [D-IL-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Jackson",
      "middleName": "L.",
      "party": "D",
      "sponsorshipDate": "2025-02-07",
      "state": "IL"
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
      "sponsorshipDate": "2025-02-07",
      "state": "GA"
    },
    {
      "bioguideId": "K000385",
      "district": "2",
      "firstName": "Robin",
      "fullName": "Rep. Kelly, Robin L. [D-IL-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Kelly",
      "middleName": "L.",
      "party": "D",
      "sponsorshipDate": "2025-02-07",
      "state": "IL"
    },
    {
      "bioguideId": "M000312",
      "district": "2",
      "firstName": "James",
      "fullName": "Rep. McGovern, James P. [D-MA-2]",
      "isOriginalCosponsor": "True",
      "lastName": "McGovern",
      "middleName": "P.",
      "party": "D",
      "sponsorshipDate": "2025-02-07",
      "state": "MA"
    },
    {
      "bioguideId": "M001160",
      "district": "4",
      "firstName": "Gwen",
      "fullName": "Rep. Moore, Gwen [D-WI-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Moore",
      "party": "D",
      "sponsorshipDate": "2025-02-07",
      "state": "WI"
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
      "sponsorshipDate": "2025-02-07",
      "state": "DC"
    },
    {
      "bioguideId": "R000617",
      "district": "3",
      "firstName": "Delia",
      "fullName": "Rep. Ramirez, Delia C. [D-IL-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Ramirez",
      "middleName": "C.",
      "party": "D",
      "sponsorshipDate": "2025-02-07",
      "state": "IL"
    },
    {
      "bioguideId": "S001145",
      "district": "9",
      "firstName": "Janice",
      "fullName": "Rep. Schakowsky, Janice D. [D-IL-9]",
      "isOriginalCosponsor": "True",
      "lastName": "Schakowsky",
      "middleName": "D.",
      "party": "D",
      "sponsorshipDate": "2025-02-07",
      "state": "IL"
    },
    {
      "bioguideId": "T000481",
      "district": "12",
      "firstName": "Rashida",
      "fullName": "Rep. Tlaib, Rashida [D-MI-12]",
      "isOriginalCosponsor": "True",
      "lastName": "Tlaib",
      "party": "D",
      "sponsorshipDate": "2025-02-07",
      "state": "MI"
    },
    {
      "bioguideId": "V000081",
      "district": "7",
      "firstName": "Nydia",
      "fullName": "Rep. Vel\u00e1zquez, Nydia M. [D-NY-7]",
      "isOriginalCosponsor": "True",
      "lastName": "Vel\u00e1zquez",
      "middleName": "M.",
      "party": "D",
      "sponsorshipDate": "2025-02-07",
      "state": "NY"
    },
    {
      "bioguideId": "M001229",
      "district": "10",
      "firstName": "LaMonica",
      "fullName": "Rep. McIver, LaMonica [D-NJ-10]",
      "isOriginalCosponsor": "True",
      "lastName": "McIver",
      "party": "D",
      "sponsorshipDate": "2025-02-07",
      "state": "NJ"
    },
    {
      "bioguideId": "W000822",
      "district": "12",
      "firstName": "Bonnie",
      "fullName": "Rep. Watson Coleman, Bonnie [D-NJ-12]",
      "isOriginalCosponsor": "True",
      "lastName": "Watson Coleman",
      "party": "D",
      "sponsorshipDate": "2025-02-07",
      "state": "NJ"
    },
    {
      "bioguideId": "S001193",
      "district": "14",
      "firstName": "Eric",
      "fullName": "Rep. Swalwell, Eric [D-CA-14]",
      "isOriginalCosponsor": "True",
      "lastName": "Swalwell",
      "party": "D",
      "sponsorshipDate": "2025-02-07",
      "state": "CA"
    },
    {
      "bioguideId": "T000489",
      "district": "18",
      "firstName": "Sylvester",
      "fullName": "Rep. Turner, Sylvester [D-TX-18]",
      "isOriginalCosponsor": "True",
      "lastName": "Turner",
      "party": "D",
      "sponsorshipDate": "2025-02-07",
      "state": "TX"
    },
    {
      "bioguideId": "O000172",
      "district": "14",
      "firstName": "Alexandria",
      "fullName": "Rep. Ocasio-Cortez, Alexandria [D-NY-14]",
      "isOriginalCosponsor": "False",
      "lastName": "Ocasio-Cortez",
      "party": "D",
      "sponsorshipDate": "2025-02-11",
      "state": "NY"
    },
    {
      "bioguideId": "S001218",
      "district": "1",
      "firstName": "Melanie",
      "fullName": "Rep. Stansbury, Melanie A. [D-NM-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Stansbury",
      "middleName": "A.",
      "party": "D",
      "sponsorshipDate": "2025-02-12",
      "state": "NM"
    },
    {
      "bioguideId": "C001067",
      "district": "9",
      "firstName": "Yvette",
      "fullName": "Rep. Clarke, Yvette D. [D-NY-9]",
      "isOriginalCosponsor": "False",
      "lastName": "Clarke",
      "middleName": "D.",
      "party": "D",
      "sponsorshipDate": "2025-02-24",
      "state": "NY"
    },
    {
      "bioguideId": "Q000023",
      "district": "5",
      "firstName": "Mike",
      "fullName": "Rep. Quigley, Mike [D-IL-5]",
      "isOriginalCosponsor": "False",
      "lastName": "Quigley",
      "party": "D",
      "sponsorshipDate": "2025-02-25",
      "state": "IL"
    },
    {
      "bioguideId": "D000096",
      "district": "7",
      "firstName": "Danny",
      "fullName": "Rep. Davis, Danny K. [D-IL-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Davis",
      "middleName": "K.",
      "party": "D",
      "sponsorshipDate": "2025-02-26",
      "state": "IL"
    },
    {
      "bioguideId": "N000002",
      "district": "12",
      "firstName": "Jerrold",
      "fullName": "Rep. Nadler, Jerrold [D-NY-12]",
      "isOriginalCosponsor": "False",
      "lastName": "Nadler",
      "party": "D",
      "sponsorshipDate": "2025-03-03",
      "state": "NY"
    },
    {
      "bioguideId": "V000130",
      "district": "52",
      "firstName": "Juan",
      "fullName": "Rep. Vargas, Juan [D-CA-52]",
      "isOriginalCosponsor": "False",
      "lastName": "Vargas",
      "party": "D",
      "sponsorshipDate": "2025-03-03",
      "state": "CA"
    },
    {
      "bioguideId": "J000298",
      "district": "7",
      "firstName": "Pramila",
      "fullName": "Rep. Jayapal, Pramila [D-WA-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Jayapal",
      "party": "D",
      "sponsorshipDate": "2025-03-10",
      "state": "WA"
    },
    {
      "bioguideId": "P000597",
      "district": "1",
      "firstName": "Chellie",
      "fullName": "Rep. Pingree, Chellie [D-ME-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Pingree",
      "party": "D",
      "sponsorshipDate": "2025-03-11",
      "state": "ME"
    },
    {
      "bioguideId": "J000305",
      "district": "51",
      "firstName": "Sara",
      "fullName": "Rep. Jacobs, Sara [D-CA-51]",
      "isOriginalCosponsor": "False",
      "lastName": "Jacobs",
      "party": "D",
      "sponsorshipDate": "2025-03-11",
      "state": "CA"
    },
    {
      "bioguideId": "D000623",
      "district": "10",
      "firstName": "Mark",
      "fullName": "Rep. DeSaulnier, Mark [D-CA-10]",
      "isOriginalCosponsor": "False",
      "lastName": "DeSaulnier",
      "party": "D",
      "sponsorshipDate": "2025-03-21",
      "state": "CA"
    },
    {
      "bioguideId": "C001068",
      "district": "9",
      "firstName": "Steve",
      "fullName": "Rep. Cohen, Steve [D-TN-9]",
      "isOriginalCosponsor": "False",
      "lastName": "Cohen",
      "party": "D",
      "sponsorshipDate": "2025-04-17",
      "state": "TN"
    },
    {
      "bioguideId": "C001125",
      "district": "2",
      "firstName": "Troy",
      "fullName": "Rep. Carter, Troy A. [D-LA-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Carter",
      "middleName": "A.",
      "party": "D",
      "sponsorshipDate": "2025-04-17",
      "state": "LA"
    },
    {
      "bioguideId": "T000193",
      "district": "2",
      "firstName": "Bennie",
      "fullName": "Rep. Thompson, Bennie G. [D-MS-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Thompson",
      "middleName": "G.",
      "party": "D",
      "sponsorshipDate": "2025-05-14",
      "state": "MS"
    },
    {
      "bioguideId": "P000617",
      "district": "7",
      "firstName": "Ayanna",
      "fullName": "Rep. Pressley, Ayanna [D-MA-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Pressley",
      "party": "D",
      "sponsorshipDate": "2025-05-15",
      "state": "MA"
    },
    {
      "bioguideId": "C001080",
      "district": "28",
      "firstName": "Judy",
      "fullName": "Rep. Chu, Judy [D-CA-28]",
      "isOriginalCosponsor": "False",
      "lastName": "Chu",
      "party": "D",
      "sponsorshipDate": "2025-05-19",
      "state": "CA"
    },
    {
      "bioguideId": "L000582",
      "district": "36",
      "firstName": "Ted",
      "fullName": "Rep. Lieu, Ted [D-CA-36]",
      "isOriginalCosponsor": "False",
      "lastName": "Lieu",
      "party": "D",
      "sponsorshipDate": "2025-05-29",
      "state": "CA"
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
      "sponsorshipDate": "2025-05-29",
      "state": "PA"
    },
    {
      "bioguideId": "W000187",
      "district": "43",
      "firstName": "Maxine",
      "fullName": "Rep. Waters, Maxine [D-CA-43]",
      "isOriginalCosponsor": "False",
      "lastName": "Waters",
      "party": "D",
      "sponsorshipDate": "2025-06-09",
      "state": "CA"
    },
    {
      "bioguideId": "S001231",
      "district": "12",
      "firstName": "Lateefah",
      "fullName": "Rep. Simon, Lateefah [D-CA-12]",
      "isOriginalCosponsor": "False",
      "lastName": "Simon",
      "party": "D",
      "sponsorshipDate": "2025-10-14",
      "state": "CA"
    },
    {
      "bioguideId": "G000599",
      "district": "10",
      "firstName": "Daniel",
      "fullName": "Rep. Goldman, Daniel S. [D-NY-10]",
      "isOriginalCosponsor": "False",
      "lastName": "Goldman",
      "middleName": "S.",
      "party": "D",
      "sponsorshipDate": "2025-10-28",
      "state": "NY"
    },
    {
      "bioguideId": "T000488",
      "district": "13",
      "firstName": "Shri",
      "fullName": "Rep. Thanedar, Shri [D-MI-13]",
      "isOriginalCosponsor": "False",
      "lastName": "Thanedar",
      "party": "D",
      "sponsorshipDate": "2026-02-09",
      "state": "MI"
    },
    {
      "bioguideId": "A000370",
      "district": "12",
      "firstName": "Alma",
      "fullName": "Rep. Adams, Alma S. [D-NC-12]",
      "isOriginalCosponsor": "False",
      "lastName": "Adams",
      "middleName": "S.",
      "party": "D",
      "sponsorshipDate": "2026-02-24",
      "state": "NC"
    },
    {
      "bioguideId": "E000299",
      "district": "16",
      "firstName": "Veronica",
      "fullName": "Rep. Escobar, Veronica [D-TX-16]",
      "isOriginalCosponsor": "False",
      "lastName": "Escobar",
      "party": "D",
      "sponsorshipDate": "2026-03-17",
      "state": "TX"
    },
    {
      "bioguideId": "F000476",
      "district": "10",
      "firstName": "Maxwell",
      "fullName": "Rep. Frost, Maxwell [D-FL-10]",
      "isOriginalCosponsor": "False",
      "lastName": "Frost",
      "party": "D",
      "sponsorshipDate": "2026-03-18",
      "state": "FL"
    },
    {
      "bioguideId": "D000635",
      "district": "3",
      "firstName": "Maxine",
      "fullName": "Rep. Dexter, Maxine [D-OR-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Dexter",
      "party": "D",
      "sponsorshipDate": "2026-04-09",
      "state": "OR"
    },
    {
      "bioguideId": "L000273",
      "district": "3",
      "firstName": "Teresa",
      "fullName": "Rep. Leger Fernandez, Teresa [D-NM-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Leger Fernandez",
      "party": "D",
      "sponsorshipDate": "2026-04-16",
      "state": "NM"
    },
    {
      "bioguideId": "G000606",
      "district": "7",
      "firstName": "Adelita",
      "fullName": "Rep. Grijalva, Adelita S. [D-AZ-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Grijalva",
      "middleName": "S.",
      "party": "D",
      "sponsorshipDate": "2026-04-27",
      "state": "AZ"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1111ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 1111\nIN THE HOUSE OF REPRESENTATIVES\nFebruary 7, 2025 Ms. Omar (for herself, Ms. Bonamici , Mr. Carson , Mr. Garc\u00eda of Illinois , Mr. Grijalva , Mr. Jackson of Illinois , Mr. Johnson of Georgia , Ms. Kelly of Illinois , Mr. McGovern , Ms. Moore of Wisconsin , Ms. Norton , Mrs. Ramirez , Ms. Schakowsky , Ms. Tlaib , Ms. Vel\u00e1zquez , Mrs. McIver , Mrs. Watson Coleman , Mr. Swalwell , and Mr. Turner of Texas ) introduced the following bill; which was referred to the Committee on Oversight and Government Reform\nA BILL\nTo establish a Department of Peacebuilding, and for other purposes.\n#### 1. Short title; table of contents\n##### (a) Short title\nThis Act may be cited as the Department of Peacebuilding Act of 2025 .\n##### (b) Table of contents\nThe table of contents for this Act is as follows:\nSec. 1. Short title; table of contents.\nSec. 2. Findings.\nTitle I\u2014Establishment of Department of Peacebuilding\nSec. 101. Establishment of Department of Peacebuilding.\nSec. 102. Responsibilities and powers.\nSec. 103. Principal officers.\nSec. 104. Office of Peace Education and Training.\nSec. 105. Office of Domestic Peacebuilding Activities.\nSec. 106. Office of International Peacebuilding Activities.\nSec. 107. Office of Technology for Peace.\nSec. 108. Office of Arms Control and Disarmament.\nSec. 109. Office of Peacebuilding Information and Research.\nSec. 110. Office of Human Rights and Economic Rights.\nSec. 111. Intergovernmental Advisory Council on Peace.\nSec. 112. Federal Interagency Committee on Peace.\nSec. 113. Staff.\nSec. 114. Consultation required.\nSec. 115. Collaboration.\nTitle II\u2014Other Matters\nSec. 201. Legislative recommendations of the Secretary.\nSec. 202. Peace Days.\nSec. 203. Definitions.\nSec. 204. Authorization of appropriations.\n#### 2. Findings\nCongress finds the following:\n**(1)**\nOn July 4, 1776, the Second Continental Congress unanimously declared the independence of the 13 colonies, and the achievement of peace was recognized as one of the highest duties of the new organization of free and independent States.\n**(2)**\nThe Constitution of the United States, in its preamble, further sets forth the insurance of the cause of peace in stating, We the People of the United States, in Order to form a more perfect Union, establish Justice, insure domestic Tranquility, provide for the common defense, promote the general Welfare, and secure the Blessings of Liberty to ourselves and our Posterity .\n**(3)**\nAccording to the Centre for Global Research, the United States has been at war for more than 90 percent of its existence. Many of our citizens today have never known a peaceful year in their lifetimes.\n**(4)**\nThroughout the globe, starvation, rape, denial of media access to conflict zones, and dismantling of civic and societal infrastructures, including housing and healthcare, are utilized as weapons of war. In 2024, UNICEF warned that rape and gender-based violence are often used as weapons of war and that 1 out of every 8 girls alive today\u2014some 370 million people\u2014will experience rape or sexual assault before they turn 18. More than 120 million individuals have been forcibly displaced worldwide as a result of persecution, conflict, violence, and human rights violations.\n**(5)**\nIn the 21st century, the United States has spent almost $8 trillion on foreign wars, with nearly 5 million lives lost.\n**(6)**\nThe physical, emotional, monetary, and other costs of violence are enormous, cut across all sectors of society in the United States, disproportionately impact people of color, and are interrelated.\n**(7)**\nThe Centers for Disease Control and Prevention (CDC) and the National Institutes of Health report 1 in 7 children experience some form of child abuse or neglect in their lifetimes, nearly 1 in 4 women report having experienced severe physical violence from an intimate partner, nearly 1 in 3 women and 1 in 7 men experience some form of sexual violence during their lifetimes, and Native American women are sexually assaulted, murdered, and disappeared at higher rates than other American women. Additionally, the lifetime economic cost associated with medical services for Intimate Partner Violence-related injuries, lost productivity from paid work, criminal justice and other costs, is $3.6 trillion according to the CDC.\n**(8)**\nThere are 3.3 million reports of violence against children that result in foster care placements every year; 25 percent of kids in foster care experience PTSD, fewer than 3 percent earn a college degree; 20 percent become homeless after the age of 18; and only 50 percent will be employed by the age of 24. One in five high school students reported being bullied at school during 2017 and cyberbullying impacts many young people. Criminalization disproportionately impacts African Americans and other people of color, including high rates of school suspensions and expulsions and incarceration. African Americans are incarcerated at more than five times the rate of Whites.\n**(9)**\nIn 2015, 17 percent of students considered attempting suicide. Suicide is the second leading cause of death among Native Americans aged 10 to 34. Approximately 17 veterans a day commit suicide nationwide. About 12 young people in the United States die from homicides each day.\n**(10)**\nRestorative justice and practices have been proven to significantly improve outcomes. In Sonoma County, California, schools that introduced restorative practices saw their suspension rates drop by nearly 30 percent.\n**(11)**\nMore Americans have died from gunshots in the last 50 years than in all of the wars in American history.\n**(12)**\nSince 1968, more than 1.5 million Americans have died in gun-related incidents, according to data from the CDC. Firearms are the leading cause of death for American children and teens, disproportionally affecting people of color, and cause more deaths in young people than cancer and car crashes. The Johns Hopkins Center for Gun Violence Prevention reports that in 2022, 48,204 people died due to gun violence in the United States, the second highest total ever recorded. Each day, an average of 132 people died from gun violence\u2014one death every 11 minutes. In 2024, there were more than 500 mass shootings, defined as incidents in which 4 or more people are injured or killed. From 2020\u20132023, the number exceeded 600 annually. Young people go to school wondering where to hide when a shooter enters their classroom. Each gun injury and fatality results in trauma to family members, loved ones, and the community.\n**(13)**\nAccording to reports by the Institute of Economics and Peace, which measures the economic impact of violence and conflict to the global economy, the economic impact of violence to the global economy was $16.5 trillion in 2021. One IEP report found that the regional impact of violence in North America, 99 percent of which can be attributed to the United States, amounted to $2.73 trillion in 2017.\n**(14)**\nViolence prevention is cost effective. For every dollar spent on violence prevention and peacebuilding, thousands of lives and dollars are saved. The philosophy and techniques of nonviolence and peacebuilding provide tools and techniques that can be applied not only at the levels of individual and community growth, but also within the Federal Government and at national and international levels.\n**(15)**\nPeacebuilding is defined by the United Nations as a range of measures targeted to reduce the risk of lapsing or relapsing into conflict by strengthening national capacities at all levels for conflict management and to lay the foundations for sustainable peace and development. Peacebuilding is predicated on research into the root causes of violence in the United States and the world, through promotion and promulgation of effective policies and programs that ameliorate those root causes of violence, and through providing all citizens, organizations, and governmental bodies with opportunities to learn about and practice the essential tools of nonviolent conflict resolution and peacebuilding.\n**(16)**\nPeace is a human right and a security issue. The Universal Declaration of Human Rights recognizes that recognition of the inherent dignity and of the equal and inalienable rights of all members of the human family is the foundation of freedom, justice and peace in the world , and General Assembly resolution 39/11 solemnly proclaims that the peoples of our planet have a sacred right to peace and emphasizes that ensuring the exercise of the right of peoples to peace demands that the policies of States be directed towards the elimination of the threat of war, particularly nuclear war, the renunciation of the use of force in international relations and the settlement of international disputes by peaceful means on the basis of the Charter of the United Nations .\n**(17)**\nIn 2000, the Earth Charter Commission released the Earth Charter, an international declaration of fundamental values and principles created to build a just, sustainable, and peaceful global society. The preamble of the Earth Charter provides, To move forward we must recognize that in the midst of a magnificent diversity of cultures and life forms we are one human family and one Earth community with a common destiny. We must join together to bring forth a sustainable global society founded on respect for nature, universal human rights, economic justice, and a culture of peace. .\n**(18)**\nClimate change is becoming a critical multiplier of global conflict. Without immediate action, water scarcity, food insecurity, and other impacts of climate change threaten to ignite new conflicts, particularly in already fragile regions. A 2021 Lancet global health study of 10,000 youth found 59 percent are very or extremely concerned about climate change and its impact on their mental health.\n**(19)**\nNuclear weapons expose the world to harm on a vast, extinction-level scale. It has long been held that a nuclear war cannot be won and must never be fought. Yet, the United States continues expanding and modernizing its nuclear arsenal, spending trillions of dollars that could instead be redirected to the needs of American communities.\n**(20)**\nSystemic racism is a significant driver of violence and key obstacle to peace in the United States. Confronting and uprooting systemic racism in America will require efforts by the Federal Government both to properly acknowledge, memorialize, and provide reparations for historical injustices, including the institutions of slavery and Jim Crow.\n**(21)**\nEconomic insecurity and poverty are forms of violence. Low wages and poverty contribute to homelessness, health issues, lower life expectancy, worse school attendance and many other outcomes. According to the Poor People\u2019s Campaign, poverty is the fourth leading cause of death in the United States, claiming 295,000 lives every year.\nI\nEstablishment of Department of Peacebuilding\n#### 101. Establishment of Department of Peacebuilding\n##### (a) Establishment\nThere is hereby established a Department of Peacebuilding, which shall\u2014\n**(1)**\nbe within the executive branch of the Federal Government; and\n**(2)**\nbe dedicated to peacebuilding, peacemaking, and the study and promotion of conditions conducive to both domestic and international peace and a culture of peace.\n##### (b) Secretary of peacebuilding\nThere shall be at the head of the Department a Secretary of Peacebuilding, who shall be appointed by the President, by and with the advice and consent of the Senate.\n##### (c) Mission\nThe Department shall\u2014\n**(1)**\ncultivate peace and peacebuilding as a strategic national policy objective;\n**(2)**\nreduce and prevent violence in the United States and internationally through peacebuilding and effective nonviolent conflict resolution;\n**(3)**\nstrengthen nonmilitary means of peacemaking;\n**(4)**\ntake a proactive, strategic approach in the development of field-tested best practices and policies that promote national and international conflict prevention, nonviolent intervention, mediation, peaceful resolution of conflict, and structured mediation of conflict;\n**(5)**\naddress matters both domestic and international in scope;\n**(6)**\naddress the interconnection of all life and the intersectionality of peace and justice, equality, health, healing, national security, education, the economy, rule of law, democracy, planetary survival, and other aspects of civil rights, civil liberties, and human rights;\n**(7)**\nprovide an institutional platform for the growing wealth of expertise in peacebuilding to dramatically reduce the national and global epidemic of violence;\n**(8)**\nsupport local communities in finding, funding, replicating, and expanding programs to reduce and prevent violence;\n**(9)**\ninvest in nongovernmental organizations that have implemented successful initiatives to reduce and prevent violence, both internationally and domestically; and\n**(10)**\nconsult with other Federal agencies to apply and practice the science of peacebuilding in their respective fields of responsibility.\n#### 102. Responsibilities and powers\n##### (a) In general\nThe Secretary shall, on an ongoing basis\u2014\n**(1)**\nwork proactively and interactively with each branch of the Federal Government on all policy matters relating to conditions of peace;\n**(2)**\ncall on the experience and expertise of individuals and seek participation in the development of policy from private, public, and nongovernmental organizations;\n**(3)**\nmonitor and analyze causative principles of conflict and make policy recommendations for developing conditions of peace and maintaining peaceful conduct;\n**(4)**\nresearch effective violence reduction programs and promote and promulgate such programs within the Federal Government and society; and\n**(5)**\nconsult with private, public, and nongovernmental organizations to develop a metric model that provides the means to measure and report progress toward peace in the United States to the President, Congress, and the public, and issue reports on such progress annually with those reports to be available to the public on the website of the Department.\n##### (b) Domestic responsibilities\nThe Secretary shall collaborate with governmental and nongovernmental organizations and individuals to promote personal and community security and peace by\u2014\n**(1)**\ndeveloping new policies and supporting existing policies that effectively address personal and family violence, including suicide, domestic violence, spousal abuse, child abuse, and mistreatment of the elderly and others;\n**(2)**\ncreating new policies and programs and expanding existing policies and programs that effectively reduce drug and alcohol abuse;\n**(3)**\nanalyzing existing policies, employing successful, field-tested programs, and developing new approaches for dealing with the tools of violence, including handguns and assault weapons, especially among youth;\n**(4)**\ndeveloping new and expanding effective programs that address and ameliorate societal challenges such as school violence, gangs, police violence, hate crimes, economic injustice, human trafficking, racial or ethnic violence, violence against LGBTQ+ individuals, and police-community relations disputes;\n**(5)**\nmaking policy recommendations to the Attorney General of the United States regarding civil rights and labor law;\n**(6)**\nassisting in the establishment and funding of community-based violence prevention programs, including virtual violence prevention programs for at-home participation, violence prevention counseling and peer mediation in schools and via video conferences, and unarmed civilian peacekeeping and crisis mitigation at a local level;\n**(7)**\nproviding counseling and advocacy on behalf of individuals victimized by violence, including those with mental health challenges;\n**(8)**\nproviding for public education programs and counseling strategies that promote acceptance and respect for the diversity of all individuals in the United States without regard to race, religion, creed, gender and gender identification, sexual orientation, age, ethnicity, national origin, class and economic status, and other perceived differences; and\n**(9)**\nsupporting local community initiatives that draw on neighborhood resources to create peace projects that facilitate the development of conflict resolution and healing of societal wounds such as patriarchy, racism, war, manifest destiny, and economic injustice to thereby inform and inspire national policy.\n##### (c) International responsibilities\nThe Secretary shall\u2014\n**(1)**\nadvise the Secretary of Defense and the Secretary of State on matters relating to national security, including the protection of human rights and the prevention of, amelioration of, and de-escalation of unarmed and armed international conflict;\n**(2)**\ncontribute to and participate in the development of training of all United States personnel who administer post-conflict reconstruction and demobilization in war-torn societies;\n**(3)**\nsponsor national and regional conflict-prevention and dispute-resolution initiatives, create special task forces, and draw on local, regional, and national expertise to develop plans and programs for addressing the root sources and issues of conflict in troubled areas;\n**(4)**\ndevelop violence prevention, amelioration and violence de-escalation training for the general public to provide tools and educate about peacebuilding skills and to promote sustainable peace, peacebuilding buy-in and peacebuilding awareness;\n**(5)**\ncounsel and advocate on behalf of women victimized by violence, including rape, situations leading up to conflict, conflicts, and post-conflict situations;\n**(6)**\ncounsel and advocate on behalf of victims of human trafficking both domestically and internationally and work to end the trafficking of human beings;\n**(7)**\nprovide for exchanges between the United States and other nations that endeavor to develop domestic and international peace-based initiatives;\n**(8)**\nencourage the development of international sister city programs, pairing United States cities with cities around the world for artistic, cultural, economic, educational, and faith-based exchanges;\n**(9)**\nestablish and administer a budget designated for the training and deployment of unarmed civilian peacekeepers to participate in multinational nonviolent peacekeeping forces that may be conducted by civilian, governmental, or multilateral organizations;\n**(10)**\njointly with the Secretary of the Treasury, strengthen peace enforcement through hiring and training monitors and investigators to help with the enforcement of international arms embargoes;\n**(11)**\nin consultation with the Secretary of State, bring together all stakeholders who are impacted by a conflict by facilitating peace summits where such stakeholders may gather under carefully prepared conditions to promote nonviolent communication and mutually beneficial solutions and to prevent future violence;\n**(12)**\nsubmit to the President recommendations for reductions and elimination of weapons of mass destruction, and make annual reports to the President on the sale of arms from the United States to other nations, with an analysis of the impact of such sales on the defense of the United States, how such sales affect peace and security, and how reduction or cessation of such sales affect peace and security;\n**(13)**\nin consultation with the Secretary of State, develop strategies for sustainability and management of the distribution of international funds;\n**(14)**\nadvise the Permanent Representative of the United States to the United Nations on matters pertaining to the United Nations Security Council;\n**(15)**\nsupport the implementation of international peacebuilding strategies through a balanced use of peacebuilding, reconciliation, diplomacy, development, and defense with the goal of preventing and ending war and violence; and\n**(16)**\nencourage all nations to create infrastructures for peace within their nations and among nations.\n##### (d) Membership of the Secretary of Peacebuilding on the national security council\nSection 101(c) of the National Security Act of 1947 ( 50 U.S.C. 3021(c) ) is amended by inserting , the Secretary of Peacebuilding after Treasury .\n##### (e) Human security responsibilities\nThe Secretary shall address and offer nonviolent conflict resolution strategies and suggest resources for unarmed civilian peacekeepers to the appropriate relevant parties on issues of human security if such security is threatened by conflict or crisis, whether such conflict or crisis is geographic, religious, ethnic, gender-based, racial, or class-based in its origin, derives from economic concerns, health concerns or is initiated through disputes concerning scarcity of natural resources (such as water and energy resources), food, health resources (such as life saving medicine, medical and protective equipment and supplies, including viral and bacterial infection testing supplies and vaccines), trade, or climate and environmental concerns.\n##### (f) Media-Related responsibilities\nRespecting the First Amendment to the Constitution of the United States of America and the requirement for free and independent media, the Secretary shall\u2014\n**(1)**\nseek assistance in the design and implementation of nonviolent policies from media professionals;\n**(2)**\nstudy the role of the media in the escalation and de-escalation of conflict at domestic and international levels, including the role of fear-inducing and hate-inducing speech and actions, and making the findings of such study public; and\n**(3)**\nmake recommendations to professional media organizations in order to provide opportunities to increase media awareness of peacebuilding initiatives.\n##### (g) Educational responsibilities\nThe Secretary shall\u2014\n**(1)**\nconsult with the United States Institute of Peace, the Department of Education, Indigenous communities, and other concerned individuals and organizations and develop a peace education curriculum that includes studies of\u2014\n**(A)**\nthe civil rights movement in the United States and throughout the world and human rights and liberties movements, with special emphasis on the role of nonviolence and how individual endeavor and involvement have contributed to advancements in peace and justice;\n**(B)**\nunderlying causes of violence and conditions of peace;\n**(C)**\npractices that enhance peace and peacebuilding;\n**(D)**\nthe contributions to the United States of its diverse ethnicities, races, and religious communities;\n**(E)**\npeace agreements and circumstances in which peaceful intervention has worked to stop conflict; and\n**(F)**\nthe patriarchal structure of society and the inherent violence of such structure in the shaping of relationships and institutions;\n**(2)**\nin consultation with the Secretary of Education\u2014\n**(A)**\ncommission and participate in the development of such curriculum and make such curriculum available to local school districts to enable the use of peace education objectives at pre-kindergarten schools, elementary schools, and secondary schools in the United States;\n**(B)**\nsupport in early childhood, pre-kindergarten schools, elementary schools, secondary schools, and institutions of higher education a well-resourced, balanced education that includes math, environmental stewardship, science, English, history, ethnic studies, economics, justice, critical thinking, social studies, health, physical education, foreign languages, the arts, and music that will prepare students for success in a globally interconnected world; and\n**(C)**\noffer incentives in the form of grants and training to encourage the development of State peace curricula and assist schools in applying for such grants and training;\n**(3)**\nwork with educators to equip students to become skilled in achieving peace through reflection, and facilitate instruction in the ways of peaceful conflict resolution;\n**(4)**\nensure that schools are nonviolence zones that provide a peaceful educational environment;\n**(5)**\ncreate school and community cultures where students and staff do not feel threatened and are free from bullying and harassment by developing and implementing curricula in nonviolent conflict resolution education, mindfulness, and restorative practices for teachers, students, parents, the school community, and the community at large;\n**(6)**\nmaintain a public website to solicit and receive ideas for the development of peace from the wealth of the politically, socially, and culturally diverse public;\n**(7)**\nproactively engage the critical thinking capabilities, including civic education on citizen duties to foster democratic principles, of students and teachers of pre-kindergarten schools, elementary schools, secondary schools, and institutions of higher education through the internet and other media and issue periodic reports concerning any submissions from such students and teachers;\n**(8)**\nestablish a Peace Academy that shall\u2014\n**(A)**\nbe modeled after the military service academies; and\n**(B)**\nprovide a 4-year course of instruction in peace education, after which graduates will be required to serve 5 years in public service in programs dedicated to domestic or international nonviolent conflict resolution; and\n**(9)**\nprovide grants for peace studies departments in institutions of higher education throughout the United States.\n#### 103. Principal officers\n##### (a) Under secretary of peacebuilding\nThe President shall appoint an Under Secretary of Peacebuilding in the Department, by and with the advice and consent of the Senate. During the absence or disability of the Secretary, or in the event of a vacancy in the office of the Secretary, the Under Secretary shall act as Secretary. The Secretary shall designate the order in which other officials of the Department shall act and perform the functions of the Secretary during the absence or disability of both the Secretary and Under Secretary or in the event of vacancies in both offices.\n##### (b) Additional positions\n**(1) In general**\nThe President shall appoint in the Department, by and with the advice and consent of the Senate\u2014\n**(A)**\nan Assistant Secretary for Peace Education and Training;\n**(B)**\nan Assistant Secretary for Domestic Peacebuilding Activities;\n**(C)**\nan Assistant Secretary for International Peacebuilding Activities;\n**(D)**\nan Assistant Secretary for Technology for Peace;\n**(E)**\nan Assistant Secretary for Arms Control and Disarmament;\n**(F)**\nan Assistant Secretary for Peacebuilding Information and Research;\n**(G)**\nan Assistant Secretary for Human and Economic Rights; and\n**(H)**\na General Counsel.\n**(2) Establishment of inspector general of the department of peacebuilding**\nSection 401 of title 5, United States Code (commonly referred to as the Inspector General Act of 1978) is amended\u2014\n**(A)**\nin paragraph (1), by inserting Peacebuilding, after Homeland Security, ; and\n**(B)**\nin paragraph (3), by inserting Peacebuilding, after Homeland Security, .\n**(3) Additional officers**\nThe President shall appoint 4 additional officers in the Department, by and with the advice and consent of the Senate. The officers appointed under this paragraph shall perform such functions as the Secretary shall prescribe, including\u2014\n**(A)**\ncongressional relations functions;\n**(B)**\npublic information functions, including providing, through the use of the latest technologies, useful information about peace and the work of the Department;\n**(C)**\nmanagement and budget functions; and\n**(D)**\nplanning, evaluation, and policy development functions, including development of policies to promote the efficient and coordinated administration of the Department and its programs and encourage improvements in conflict resolution and violence prevention.\n**(4) Description of functions**\nIn any case in which the President submits the name of an individual to the Senate for confirmation as an officer of the Department under this subsection, the President shall state the particular functions such individual will exercise upon taking office.\n##### (c) Authority of secretary\nEach officer described in this section shall report directly to the Secretary and shall, in addition to any functions vested in or required to be delegated to such officer, perform such additional functions as the Secretary may prescribe.\n#### 104. Office of Peace Education and Training\n##### (a) In general\nThere shall be in the Department an Office of Peace Education and Training, the head of which shall be the Assistant Secretary for Peace Education and Training. The Assistant Secretary for Peace Education and Training shall carry out those functions of the Department relating to the creation, encouragement, and impact of peace education and training at the pre-kindergarten, elementary, secondary, university, and postgraduate levels, and disseminate applicable policies and research in consultation with entities of the Department of Health and Human Services, including\u2014\n**(1)**\nthe Administration for Children and Families;\n**(2)**\nthe Administration on Aging;\n**(3)**\nthe Centers for Disease Control and Prevention; and\n**(4)**\nthe National Institutes of Health.\n##### (b) Peace curriculum\nThe Assistant Secretary of Peace Education and Training, in consultation with the Secretary of Education, Indigenous communities, the United States Institute of Peace, nongovernmental organizations, public institutions, peace and conflict studies programs of institutions of higher education, and Federal agencies that provide effective peace training materials and curricula, shall create and support the development and dissemination of effective peace curricula and supporting materials for distribution to the State educational agency in each State and territory of the United States and any other interested institutions. Each peace curriculum shall include\u2014\n**(1)**\nbuilding communicative peace skills and nonviolent conflict resolution skills;\n**(2)**\nteaching and fostering compassion, empathy, mindfulness, kindness, acceptance, understanding, respect, inclusion, and forgiveness;\n**(3)**\nteaching about historical and contemporary events utilizing nonviolent and peacebuilding principles to promote a culture of peace and about individuals and organizations employing nonviolent and peacebuilding principles to improve society;\n**(4)**\nteaching about the benefits of a peaceful society, including economic, health, social, and scientific implications of peace; and\n**(5)**\npromoting other objectives to increase the knowledge of peace processes.\n##### (c) Grants\nThe Assistant Secretary of Peace Education and Training shall\u2014\n**(1)**\nprovide peace education grants to pre-kindergarten schools, elementary schools, secondary schools, and institutions of higher education for the creation and expansion of peace studies departments and the education and training of teachers in peace studies, violence prevention, peacebuilding, community building, and nonviolent conflict resolution skills; and\n**(2)**\nestablish a grant program to be known as the Community Peace Block Grant program under which the Secretary shall make grants to nonprofit organizations and nongovernmental organizations for the purposes of developing innovative school and neighborhood programs for nonviolent conflict resolution and creating local peacebuilding initiatives.\n#### 105. Office of Domestic Peacebuilding Activities\n##### (a) In general\nThere shall be in the Department an Office of Domestic Peacebuilding Activities, the head of which shall be the Assistant Secretary for Domestic Peacebuilding Activities. The Assistant Secretary for Domestic Peacebuilding Activities shall carry out those functions in the Department affecting domestic peace activities, including the development of policies that prevent domestic violence and that increase awareness about intervention and counseling on domestic violence and conflict.\n##### (b) Responsibilities\nThe Assistant Secretary for Domestic Peacebuilding Activities shall\u2014\n**(1)**\ndevelop policy and disseminate best practices from the field for the treatment of drug and alcohol abuse;\n**(2)**\ndevelop community-based strategies for celebrating diversity and promoting acceptance;\n**(3)**\ndevelop new policies and build upon existing proven programs to prevent the school-to-prison pipeline by promoting restorative and conflict resolution practices at pre-kindergarten, elementary, secondary, university, and post graduate levels and in police academies, with funding for teacher, staff, student, and community training in nonviolence, restorative practices, conflict resolution, and diversity understanding and appreciation;\n**(4)**\ndevelop new policies and build on existing proven programs\u2014\n**(A)**\nto assist in the prevention of hate, a culture of violence and domination, violence and crime, including the development of non-threatening, non-harassing community policing strategies, mindfulness, and conflict de-escalation training, and other peaceful settlement skills among police and other public safety officers;\n**(B)**\nto assist in the re-entry into the community by individuals who have been incarcerated by providing trauma healing, including training in anger management, conflict resolution, peacebuilding skills, life skills, and educational and job skills;\n**(C)**\nto assist in creating strong, happy, and healthy families, including supporting mental health services, domestic violence prevention, gang prevention, anti-bullying programs, animal cruelty prevention, substance abuse prevention, and the development of peaceful parenting skills;\n**(D)**\nto promote peacebuilding and community-building and to provide restorative justice and restorative practice programs at all levels of the criminal justice system that bring together offenders, victims, and community members in an effort to repair the damage caused by criminal activity through accountability and rehabilitation;\n**(E)**\nto develop violence prevention and violence de-escalation training for the general public to provide peacebuilding tools for all and to promote sustainable peace, peacebuilding buy-in, and peacebuilding awareness;\n**(F)**\nto provide for training and deployment into neighborhoods of nonmilitary domestic conflict prevention and peacemaking personnel, including violence interrupters, community safety task force, and civilian community peacekeepers;\n**(G)**\nto implement respectful, non-targeting, and non-harassing community-based policing to break down barriers between law enforcement officers and the people such officers serve; and\n**(H)**\nto encourage and facilitate formation of locally and State-run and administered citizen\u2019s boards to recommend any appropriate training as needed for working compassionately and effectively with local, regional, and State populations and to review and hold accountable actions of all local, regional, and State police and law enforcement departments in the United States;\n**(5)**\npromote informal and cultural exchanges between individuals and groups of proximate neighborhoods and regions to encourage understanding and acceptance; and\n**(6)**\ndisseminate applicable policies and research in consultation with\u2014\n**(A)**\nthe Department of Justice;\n**(B)**\nthe Department of Health and Human Services;\n**(C)**\nthe Department of State; and\n**(D)**\nthe Department of Education.\n##### (c) Grants\nThe Assistant Secretary for Domestic Peacebuilding Activities shall establish a grant program to be known as the Cultural Diplomacy for Peace grant program under which the Secretary shall make grants to pre-kindergarten schools, elementary schools, secondary schools, institutions of higher education, nonprofit organizations, and nongovernmental organizations for the purpose of developing domestic cultural exchanges, including exchanges relating to the arts, sports, science, and other academic disciplines, that promote diplomacy and cultural understanding between neighborhoods and members of such neighborhoods.\n#### 106. Office of International Peacebuilding Activities\n##### (a) In general\nThere shall be in the Department an Office of International Peacebuilding Activities, the head of which shall be the Assistant Secretary for International Peacebuilding Activities. The Assistant Secretary for International Peacebuilding Activities shall carry out those functions in the Department affecting international peace activities.\n##### (b) Responsibilities\nThe Assistant Secretary for International Peacebuilding Activities shall\u2014\n**(1)**\ndevelop new programs and promote existing proven programs to\u2014\n**(A)**\nprovide for the training and deployment of graduates of the Peace Academy established under section 102(g) and other nonmilitary conflict prevention and peacemaking personnel;\n**(B)**\nsupport national and regional conflict-prevention, de-escalation, and peaceful dispute-resolution initiatives in nations experiencing social, political, environmental, medical, or economic strife and among all nations;\n**(C)**\ndevelop community building, violence prevention, amelioration and de-escalation training for the general public to educate about peacebuilding skills and to promote sustainable peace, peacebuilding buy-in and peacebuilding awareness;\n**(D)**\nprovide training for the administration of post-conflict reconstruction and demobilization in war-torn societies;\n**(E)**\naddress root causes of violence;\n**(F)**\neradicate extreme hunger, infectious and other diseases, and poverty;\n**(G)**\neradicate genocide;\n**(H)**\nachieve universal primary education;\n**(I)**\nempower women and girls;\n**(J)**\neradicate human trafficking; and\n**(K)**\neradicate dehumanization and mistreatment of individuals;\n**(2)**\nsupport the creation of a multinational nonviolent peace force;\n**(3)**\nprovide for exchanges between individuals of the United States and other nations that are endeavoring to develop domestic and international peace-based initiatives; and\n**(4)**\ndisseminate applicable policies and research in consultation with\u2014\n**(A)**\nthe Department of State;\n**(B)**\nthe Department of Labor;\n**(C)**\nthe Peace Corps;\n**(D)**\nthe United States Institute of Peace; and\n**(E)**\nany other applicable entities.\n##### (c) Grants\nThe Assistant Secretary for International Peacebuilding Activities shall establish a grant program to be known as the International Cultural Diplomacy for Peace grant program under which the Secretary shall make grants to pre-kindergarten schools, elementary schools, secondary schools, institutions of higher education, nonprofit organizations, and nongovernmental organizations for the purpose of developing international cultural exchanges, including exchanges related to the arts, sports, science, and other academic disciplines, that promote diplomacy and cultural understanding between the United States and other nations.\n#### 107. Office of Technology for Peace\n##### (a) In general\nThere shall be in the Department an Office of Technology for Peace, the head of which shall be the Assistant Secretary for Technology for Peace. The Assistant Secretary for Technology for Peace shall carry out those functions in the Department affecting the awareness, study, ethical implications and impact of evolving existing technologies and developing new technologies, including artificial intelligence, mobile technologies, social media, drones, and data science and information, on the creation and maintenance of domestic and international peace, and disseminate applicable policies and research in consultation with appropriate entities of the Department of State.\n##### (b) Grants\nThe Assistant Secretary for Technology for Peace shall make grants for the research and development of technologies in transportation, communications, agriculture, medicine, and energy that\u2014\n**(1)**\nare nonviolent in application;\n**(2)**\nencourage the conservation and sustainability of natural resources, including air, water, land, in order to prevent future conflicts regarding scarce resources due to overuse or natural or human-caused disasters, including climate change and pandemics; and\n**(3)**\npromote a green, peaceful economy.\n#### 108. Office of Arms Control and Disarmament\n##### (a) In general\nThere shall be in the Department an Office of Arms Control and Disarmament, the head of which shall be the Assistant Secretary for Arms Control and Disarmament. The Assistant Secretary for Arms Control and Disarmament shall carry out those functions in the Department affecting arms control programs and arms limitation agreements.\n##### (b) Responsibilities\nThe Assistant Secretary for Arms Control and Disarmament shall\u2014\n**(1)**\nadvise the Secretary on interagency discussions and international negotiations, including discussions involving the United Nations, the Secretary of State, the Atomic Energy Commission, and the Secretary of Defense, regarding the increase or reduction and elimination of weapons of mass destruction throughout the world, including the dismantling of such weapons and the safe and secure storage of materials related thereto and efforts to limit or cease development, testing, manufacture or possession of nuclear weapons or threats to use them or to allow any nuclear arms to be stationed in the territory of any nation;\n**(2)**\nassist nations, international agencies, and nongovernmental organizations in assessing the locations of the buildup of nuclear arms and other weapons of mass destruction;\n**(3)**\ndevelop nonviolent strategies to prevent and deter testing or use of offensive or defensive nuclear weapons, weaponized drones, assault weapons, and other weapons of mass destruction, whether based on land, underground, air, sea, or in space;\n**(4)**\nserve as a depository for copies of all contracts, agreements, and treaties that address the reduction and elimination of nuclear weapons and other weapons of mass destruction, and the protection of space from militarization;\n**(5)**\nprovide technical support and legal assistance for the implementation of such contracts, agreements, and treaties;\n**(6)**\ndisseminate applicable policies and research in consultation with the Department of State and the Department of Commerce; and\n**(7)**\naddress and support nuclear waste cleanup at nuclear test sites, nuclear research facilities and laboratories, Superfund Sites of former and present military bases in the United States and abroad and at lands, in waters, and in the air adjacent to old and new nuclear reactors and nuclear-contaminated sites.\n#### 109. Office of Peacebuilding Information and Research\n##### (a) In general\nThere shall be in the Department an Office of Peacebuilding Information and Research, the head of which shall be the Assistant Secretary for Peacebuilding Information and Research. The Assistant Secretary for Peacebuilding Information and Research shall carry out those functions in the Department affecting research and analysis relating to creating, initiating, and modeling approaches to peaceful coexistence and nonviolent conflict resolution and shall make this information available to Congress, the public, and other interested entities on an ongoing basis.\n##### (b) Responsibilities\nThe Assistant Secretary for Peacebuilding Information and Research shall\u2014\n**(1)**\ncommission or compile studies on the impact of war, mass shootings, police violence and other types of violence, especially on the physical and mental condition of children (using the 10-point anti-war agenda in the United Nations Children\u2019s Fund report, State of the World\u2019s Children 1996, as a guide) that shall include the study of the effect of war on the environment and public health;\n**(2)**\ncommission or compile studies on the impact of war and other types of violence on soldiers, veterans and civilians;\n**(3)**\ncommission or compile studies on the effect of war and other types of violence on the environment, public health, the economy, and national security;\n**(4)**\ncommission or compile studies on the impact of violence, racism and inequality on such conditions of peace as health care, employment, education, economic equity, food security, voting rights, housing, justice, and rule of law;\n**(5)**\ncompile information on effective community peacebuilding activities and disseminate such information to local governments and nongovernmental organizations in the United States and abroad;\n**(6)**\ncommission or compile research on the effect of violence in the media, including the use of untruths, misinformation and false information and make such reports available to Congress and the public annually;\n**(7)**\ncommission or compile research on the number and circumstances of deaths caused by law enforcement using guns or other weapons, devices or methods, the number and circumstances of deaths to law enforcement officials caused by guns or other weapons, devices or methods, the effects of gun violence in the United States, and make such reports available to Congress and the public annually;\n**(8)**\ncommission or compile research on the effect of teaching nonviolent conflict resolution skills and practices and social emotional education in schools and disseminate such information to educational institutions, Congress and the public annually;\n**(9)**\ncommission or compile any other such research that will foster understanding of the root causes of violence, the root conditions of peace, and policies and practices to promote a culture of peace;\n**(10)**\npublish a monthly journal of the activities of the Department and encourage scholarly participation;\n**(11)**\nsponsor conferences throughout the United States to create awareness of the work of the Department;\n**(12)**\nmake available to the public reports, studies, and compiled research described in this Act; and\n**(13)**\nwhere applicable, work to carry out the responsibilities under this subsection in consultation with the United States Institute of Peace and other governmental and nongovernmental organizations, including\u2014\n**(A)**\nthe Department of Health and Human Services;\n**(B)**\nthe Department of Justice; and\n**(C)**\nthe Department of State.\n#### 110. Office of Human Rights and Economic Rights\n##### (a) In general\nThere shall be in the Department an Office of Human Rights and Economic Rights, the head of which shall be the Assistant Secretary for Human Rights and Economic Rights. The Assistant Secretary for Human Rights and Economic Rights shall carry out those functions in the Department that support the principles of the Universal Declaration of Human Rights, adopted by the General Assembly of the United Nations on December 10, 1948.\n##### (b) Responsibilities\nThe Assistant Secretary for Human Rights and Economic Rights shall\u2014\n**(1)**\nassist the Secretary, in consultation with the Secretary of State, in furthering the incorporation of the principles of human rights, as enunciated in the Universal Declaration of Human Rights, into all agreements between the United States and other nations to help prevent and reduce the causes of violence;\n**(2)**\nconsult with the Secretary of State, the United Nations, the Atrocities Prevention Board of the White House, the Department of Justice, and other similarly concerned governmental and nongovernmental organizations to gather information on and document domestic and international human rights abuses, including genocide, torture, State executions, police brutality, detention for profit, caging of children and other individuals, murder of unarmed civilians, solitary confinement (especially among children), human trafficking, child soldiers, child labor, and slave labor and recommend to the Secretary nonviolent responses to promote awareness, understanding, and correction of abuses;\n**(3)**\nmake such information available to other governmental and nongovernmental organizations in order to facilitate nonviolent conflict resolution;\n**(4)**\nprovide trained observers to work with nongovernmental organizations for purposes of creating a climate conducive to the respect for human rights;\n**(5)**\nconduct economic analyses of the scarcity of human and natural resources as a source of conflict and make recommendations to the Secretary for nonviolent prevention of such scarcity, nonviolent intervention in case of such scarcity, and the development of programs to assist people facing such scarcity, whether due to armed conflict, greed, misdistribution of resources, overuse or other human causes, including climate disruption, or natural causes;\n**(6)**\nconduct economic analyses of the impact of violence within and among nations as a source of human displacement and criminalization, vilification, victimization and mistreatment of those fleeing their homes to seek better and safer lives and make recommendations to the Secretary for nonviolent solutions and development of programs to assist people facing such conditions;\n**(7)**\nassist the Secretary, in consultation with the Secretary of State and the Secretary of the Treasury, in developing strategies regarding the sustainability and the management of the distribution of funds from international agencies, the conditions regarding the receipt of such funds, and the impact of those conditions on the peace and stability of the recipient nations;\n**(8)**\nassist the Secretary, in consultation with the Secretary of State and the Secretary of Labor, in developing strategies to promote full compliance with domestic and international labor rights law;\n**(9)**\nconduct policy analysis to ensure that the international development investments of the United States positively impact the peace and stability of the recipient country; and\n**(10)**\ndisseminate policies and research in consultation with appropriate entities of the Department of State.\n#### 111. Intergovernmental Advisory Council on Peace\n##### (a) In general\nThere shall be in the Department an advisory committee known as the Intergovernmental Advisory Council on Peace (in this section referred to as the Council ). The Council shall provide assistance and make recommendations to the President and the Secretary concerning intergovernmental policies relating to peace and nonviolent conflict resolution.\n##### (b) Responsibilities\nThe Council shall\u2014\n**(1)**\nprovide a forum for representatives of international bodies, the Federal Government, Tribal governments, and State and local governments to discuss peace issues, including practices, traditions and policies that promote peacebuilding and crises and wellness issues;\n**(2)**\npromote better intergovernmental relations and offer professional mediation services to ameliorate and resolve intergovernmental and intragovernmental conflict as needed, including elimination of inflammatory rhetoric; and\n**(3)**\nsubmit biennially, or more frequently if determined necessary by the Council, a report to the President, the Secretary, and Congress reviewing the impact of Federal peace activities on the Federal Government and on State and local governments.\n##### (c) Membership\nThe Secretary shall appoint the members of the Council.\n#### 112. Federal Interagency Committee on Peace\n##### (a) Establishment\nThere is established a Federal Interagency Committee on Peace (in this section referred to as the Committee ). The Committee shall\u2014\n**(1)**\nassist the Secretary in providing a mechanism to assure that the procedures and actions of the Department and other Federal agencies are fully coordinated; and\n**(2)**\nstudy and make recommendations for assuring effective coordination of Federal programs, policies, and administrative practices affecting peace, peacebuilding and violence prevention, and wellness.\n##### (b) Membership\nThe Secretary shall appoint the members of the Committee.\n#### 113. Staff\nThe Secretary may appoint and fix the compensation of such employees as may be necessary to carry out the functions of the Secretary and the Department. Except as otherwise provided by law, such employees shall be appointed in accordance with applicable laws and the compensation of such employees fixed in accordance with title 5, United States Code.\n#### 114. Consultation required\n##### (a) Consultation in cases of conflict and violence prevention\n**(1) In general**\nIn any case in which a conflict between the United States and any other government or entity is foreseeable, imminent, or occurring, the Secretary of Defense and the Secretary of State shall consult with the Secretary of Peacebuilding concerning violence prevention, nonviolent means of conflict resolution, and peacebuilding.\n**(2) Diplomatic initiatives**\nIn any case in which a conflict described in paragraph (1) is ongoing or recently concluded, the Secretary shall conduct an independent study of diplomatic initiatives undertaken by the United States and other parties to such conflict.\n**(3) Initiative assessment**\nIn any case in which a conflict described in paragraph (1) has recently concluded, the Secretary shall assess the effectiveness of any initiatives in ending such conflict.\n**(4) Consultation process**\nThe Secretary shall establish a formal process of consultation in a timely manner with the Secretary of State, the Secretary of Defense, and the National Security Council\u2014\n**(A)**\nprior to the initiation of policies or withdrawal of resources that may lead to violence and of any armed conflict between the United States and any other country; and\n**(B)**\nfor any matter involving\u2014\n**(i)**\nthe use of Department of Defense personnel within the United States; or\n**(ii)**\nthe proposed or actual distribution of equipment of the Department of Defense to local or State law enforcement entities or to other individuals or entities.\n##### (b) Consultation in drafting treaties and agreements\nThe head of each appropriate Federal agency shall consult with the Secretary in drafting treaties and peace agreements.\n#### 115. Collaboration\nThe Secretary shall, for the greatest effectiveness in promoting peace and peacebuilding, collaborate with other Federal agencies, applicable experts, nongovernmental organization stakeholders, appropriate non-profit organization stakeholders and State, Tribal, and local leaders and stakeholders regarding all related programs in all Federal agencies. The collaboration shall include and prioritize those who are most impacted by the programs for the purpose implementing or updating such programs and for the purpose of evaluating the effectiveness and impacts of such programs.\nII\nOther Matters\n#### 201. Legislative recommendations of the Secretary\nNot later than 1 year after the date of the appointment of the first Secretary, the Secretary shall prepare and submit to Congress proposed legislation containing any necessary and appropriate amendments to the laws of the United States to carry out the purposes of this Act.\n#### 202. Peace Days\nThe Secretary shall encourage citizens to observe and celebrate the blessings of peace and endeavor to create peace on Peace Days. Such days shall include discussions of the professional activities and the achievements in the lives of peacemakers.\n#### 203. Definitions\nIn this Act:\n**(1) Department**\nThe term Department means the Department of Peacebuilding established under section 101(a).\n**(2) ESEA terms**\nThe terms elementary school , secondary school , and State educational agency have the meaning given those terms in section 8101 of the Elementary and Secondary Education Act of 1965 ( 20 U.S.C. 7801 ).\n**(3) Federal agency**\nThe term Federal agency has the meaning given the term agency in section 551(1) of title 5, United States Code.\n**(4) Institution of higher education**\nThe term institution of higher education has the meaning given that term in section 101 of the Higher Education Act of 1965 ( 20 U.S.C. 1001 ).\n**(5) Nonprofit organization**\nThe term nonprofit organization means an entity that\u2014\n**(A)**\nis described in section 501(c)(3) of the Internal Revenue Code of 1986 ( 26 U.S.C. 501(c)(3) ); and\n**(B)**\nis exempt from tax under section 501(a) of such Code.\n**(6) Secretary**\nThe term Secretary means the Secretary of Peacebuilding appointed under section 101(b).\n#### 204. Authorization of appropriations\n##### (a) In general\nThere is authorized to be appropriated to carry out this Act such sums as may be necessary.\n##### (b) Limitation on use of funds\nOf the amounts appropriated pursuant to subsection (a), at least 85 percent shall be used for domestic peace programs, including administrative costs associated with such programs.",
      "versionDate": "2025-02-07",
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
            "name": "Advanced technology and technological innovations",
            "updateDate": "2025-04-24T16:15:08Z"
          },
          {
            "name": "Advisory bodies",
            "updateDate": "2025-04-24T16:15:08Z"
          },
          {
            "name": "Air quality",
            "updateDate": "2025-04-24T16:15:08Z"
          },
          {
            "name": "Alternative and renewable resources",
            "updateDate": "2025-04-24T16:15:08Z"
          },
          {
            "name": "Alternative dispute resolution, mediation, arbitration",
            "updateDate": "2025-04-24T16:15:08Z"
          },
          {
            "name": "Animal protection and human-animal relationships",
            "updateDate": "2025-04-24T16:15:08Z"
          },
          {
            "name": "Arms control and nonproliferation",
            "updateDate": "2025-04-24T16:15:08Z"
          },
          {
            "name": "Assault and harassment offenses",
            "updateDate": "2025-04-24T16:15:08Z"
          },
          {
            "name": "Child health",
            "updateDate": "2025-04-24T16:15:08Z"
          },
          {
            "name": "Child safety and welfare",
            "updateDate": "2025-04-24T16:15:08Z"
          },
          {
            "name": "Civics education",
            "updateDate": "2025-04-24T16:15:08Z"
          },
          {
            "name": "Climate change and greenhouse gases",
            "updateDate": "2025-04-24T16:15:08Z"
          },
          {
            "name": "Commemorative events and holidays",
            "updateDate": "2025-04-24T16:15:08Z"
          },
          {
            "name": "Community life and organization",
            "updateDate": "2025-04-24T16:15:08Z"
          },
          {
            "name": "Computers and information technology",
            "updateDate": "2025-04-24T16:15:08Z"
          },
          {
            "name": "Conflicts and wars",
            "updateDate": "2025-04-24T16:15:08Z"
          },
          {
            "name": "Correctional facilities and imprisonment",
            "updateDate": "2025-04-24T16:15:08Z"
          },
          {
            "name": "Crime prevention",
            "updateDate": "2025-04-24T16:15:08Z"
          },
          {
            "name": "Crime victims",
            "updateDate": "2025-04-24T16:15:08Z"
          },
          {
            "name": "Crimes against children",
            "updateDate": "2025-04-24T16:15:09Z"
          },
          {
            "name": "Crimes against women",
            "updateDate": "2025-04-24T16:15:09Z"
          },
          {
            "name": "Cultural exchanges and relations",
            "updateDate": "2025-04-24T16:15:09Z"
          },
          {
            "name": "Detention of persons",
            "updateDate": "2025-04-24T16:15:09Z"
          },
          {
            "name": "Diplomacy, foreign officials, Americans abroad",
            "updateDate": "2025-04-24T16:15:09Z"
          },
          {
            "name": "Domestic violence and child abuse",
            "updateDate": "2025-04-24T16:15:09Z"
          },
          {
            "name": "Drug, alcohol, tobacco use",
            "updateDate": "2025-04-24T16:15:09Z"
          },
          {
            "name": "Economic development",
            "updateDate": "2025-04-24T16:15:09Z"
          },
          {
            "name": "Economic performance and conditions",
            "updateDate": "2025-04-24T16:15:09Z"
          },
          {
            "name": "Elementary and secondary education",
            "updateDate": "2025-04-24T16:15:09Z"
          },
          {
            "name": "Emergency medical services and trauma care",
            "updateDate": "2025-04-24T16:15:09Z"
          },
          {
            "name": "Employment discrimination and employee rights",
            "updateDate": "2025-04-24T16:15:09Z"
          },
          {
            "name": "Environmental education",
            "updateDate": "2025-04-24T16:15:09Z"
          },
          {
            "name": "Executive agency funding and structure",
            "updateDate": "2025-04-24T16:15:09Z"
          },
          {
            "name": "Firearms and explosives",
            "updateDate": "2025-04-24T16:15:09Z"
          },
          {
            "name": "Foreign aid and international relief",
            "updateDate": "2025-04-24T16:15:09Z"
          },
          {
            "name": "Government information and archives",
            "updateDate": "2025-04-24T16:15:09Z"
          },
          {
            "name": "Government studies and investigations",
            "updateDate": "2025-04-24T16:15:09Z"
          },
          {
            "name": "Hate crimes",
            "updateDate": "2025-04-24T16:15:09Z"
          },
          {
            "name": "Hazardous wastes and toxic substances",
            "updateDate": "2025-04-24T16:15:09Z"
          },
          {
            "name": "Health promotion and preventive care",
            "updateDate": "2025-04-24T16:15:10Z"
          },
          {
            "name": "Health technology, devices, supplies",
            "updateDate": "2025-04-24T16:15:10Z"
          },
          {
            "name": "Higher education",
            "updateDate": "2025-04-24T16:15:10Z"
          },
          {
            "name": "Human rights",
            "updateDate": "2025-04-24T16:15:10Z"
          },
          {
            "name": "Human trafficking",
            "updateDate": "2025-04-24T16:15:10Z"
          },
          {
            "name": "Immigration status and procedures",
            "updateDate": "2025-04-24T16:15:10Z"
          },
          {
            "name": "Immunology and vaccination",
            "updateDate": "2025-04-24T16:15:10Z"
          },
          {
            "name": "Infectious and parasitic diseases",
            "updateDate": "2025-04-24T16:15:10Z"
          },
          {
            "name": "International organizations and cooperation",
            "updateDate": "2025-04-24T16:15:10Z"
          },
          {
            "name": "Juvenile crime and gang violence",
            "updateDate": "2025-04-24T16:15:10Z"
          },
          {
            "name": "Land use and conservation",
            "updateDate": "2025-04-24T16:15:10Z"
          },
          {
            "name": "Law enforcement administration and funding",
            "updateDate": "2025-04-24T16:15:10Z"
          },
          {
            "name": "Mental health",
            "updateDate": "2025-04-24T16:15:10Z"
          },
          {
            "name": "Natural disasters",
            "updateDate": "2025-04-24T16:15:10Z"
          },
          {
            "name": "News media and reporting",
            "updateDate": "2025-04-24T16:15:10Z"
          },
          {
            "name": "Nuclear weapons",
            "updateDate": "2025-04-24T16:15:10Z"
          },
          {
            "name": "Preschool education",
            "updateDate": "2025-04-24T16:15:10Z"
          },
          {
            "name": "Protest and dissent",
            "updateDate": "2025-04-24T16:15:10Z"
          },
          {
            "name": "Racial and ethnic relations",
            "updateDate": "2025-04-24T16:15:10Z"
          },
          {
            "name": "Radioactive wastes and releases",
            "updateDate": "2025-04-24T16:15:10Z"
          },
          {
            "name": "Reconstruction and stabilization",
            "updateDate": "2025-04-24T16:15:10Z"
          },
          {
            "name": "Refugees, asylum, displaced persons",
            "updateDate": "2025-04-24T16:15:10Z"
          },
          {
            "name": "Rule of law and government transparency",
            "updateDate": "2025-04-24T16:15:10Z"
          },
          {
            "name": "Sex offenses",
            "updateDate": "2025-04-24T16:15:10Z"
          },
          {
            "name": "Sex, gender, sexual orientation discrimination",
            "updateDate": "2025-04-24T16:15:10Z"
          },
          {
            "name": "Teaching, teachers, curricula",
            "updateDate": "2025-04-24T16:15:10Z"
          },
          {
            "name": "Technology assessment",
            "updateDate": "2025-04-24T16:15:10Z"
          },
          {
            "name": "United Nations",
            "updateDate": "2025-04-24T16:15:10Z"
          },
          {
            "name": "Violent crime",
            "updateDate": "2025-04-24T16:15:10Z"
          },
          {
            "name": "War crimes, genocide, crimes against humanity",
            "updateDate": "2025-04-24T16:15:10Z"
          },
          {
            "name": "Women's rights",
            "updateDate": "2025-04-24T16:15:08Z"
          }
        ]
      },
      "policyArea": {
        "name": "Government Operations and Politics",
        "updateDate": "2025-04-03T14:37:11Z"
      }
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-02-07",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1111ih.xml"
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
      "title": "Department of Peacebuilding Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-03-13T01:08:18Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Department of Peacebuilding Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-13T01:08:16Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To establish a Department of Peacebuilding, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-13T01:03:22Z"
    }
  ]
}
```
