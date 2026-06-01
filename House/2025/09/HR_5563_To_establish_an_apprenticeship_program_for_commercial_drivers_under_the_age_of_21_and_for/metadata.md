# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/5563?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/5563
- Title: DRIVE-SAFE Act
- Congress: 119
- Bill type: HR
- Bill number: 5563
- Origin chamber: House
- Introduced date: 2025-09-26
- Update date: 2026-05-14T08:07:34Z
- Update date including text: 2026-05-14T08:07:34Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-09-26: Introduced in House
- 2025-09-26 - IntroReferral: Introduced in House
- 2025-09-26 - IntroReferral: Introduced in House
- 2025-09-26 - IntroReferral: Referred to the House Committee on Transportation and Infrastructure.
- 2025-12-01 - Committee: Referred to the Subcommittee on Highways and Transit.
- Latest action: 2025-09-26: Introduced in House

## Actions

- 2025-09-26 - IntroReferral: Introduced in House
- 2025-09-26 - IntroReferral: Introduced in House
- 2025-09-26 - IntroReferral: Referred to the House Committee on Transportation and Infrastructure.
- 2025-12-01 - Committee: Referred to the Subcommittee on Highways and Transit.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-09-26",
    "latestAction": {
      "actionDate": "2025-09-26",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/5563",
    "number": "5563",
    "originChamber": "House",
    "policyArea": {
      "name": "Labor and Employment"
    },
    "sponsors": [
      {
        "bioguideId": "C001087",
        "district": "1",
        "firstName": "Eric",
        "fullName": "Rep. Crawford, Eric A. \"Rick\" [R-AR-1]",
        "lastName": "Crawford",
        "party": "R",
        "state": "AR"
      }
    ],
    "title": "DRIVE-SAFE Act",
    "type": "HR",
    "updateDate": "2026-05-14T08:07:34Z",
    "updateDateIncludingText": "2026-05-14T08:07:34Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-12-01",
      "committees": {
        "item": {
          "name": "Highways and Transit Subcommittee",
          "systemCode": "hspw12"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Referred to the Subcommittee on Highways and Transit.",
      "type": "Committee"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-09-26",
      "committees": {
        "item": {
          "name": "Transportation and Infrastructure Committee",
          "systemCode": "hspw00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Transportation and Infrastructure.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-09-26",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-09-26",
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
          "date": "2025-09-26T14:03:05Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Transportation and Infrastructure Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": {
              "date": "2025-12-01T19:20:51Z",
              "name": "Referred to"
            }
          },
          "name": "Highways and Transit Subcommittee",
          "systemCode": "hspw12"
        }
      },
      "systemCode": "hspw00",
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
      "bioguideId": "G000592",
      "district": "2",
      "firstName": "Jared",
      "fullName": "Rep. Golden, Jared F. [D-ME-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Golden",
      "middleName": "F.",
      "party": "D",
      "sponsorshipDate": "2025-09-26",
      "state": "ME"
    },
    {
      "bioguideId": "W000821",
      "district": "4",
      "firstName": "Bruce",
      "fullName": "Rep. Westerman, Bruce [R-AR-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Westerman",
      "party": "R",
      "sponsorshipDate": "2025-09-26",
      "state": "AR"
    },
    {
      "bioguideId": "C001112",
      "district": "24",
      "firstName": "Salud",
      "fullName": "Rep. Carbajal, Salud O. [D-CA-24]",
      "isOriginalCosponsor": "True",
      "lastName": "Carbajal",
      "middleName": "O.",
      "party": "D",
      "sponsorshipDate": "2025-09-26",
      "state": "CA"
    },
    {
      "bioguideId": "L000585",
      "district": "16",
      "firstName": "Darin",
      "fullName": "Rep. LaHood, Darin [R-IL-16]",
      "isOriginalCosponsor": "True",
      "lastName": "LaHood",
      "party": "R",
      "sponsorshipDate": "2025-09-26",
      "state": "IL"
    },
    {
      "bioguideId": "G000600",
      "district": "3",
      "firstName": "Marie",
      "fullName": "Rep. Perez, Marie Gluesenkamp [D-WA-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Perez",
      "middleName": "Gluesenkamp",
      "party": "D",
      "sponsorshipDate": "2025-09-26",
      "state": "WA"
    },
    {
      "bioguideId": "H001091",
      "district": "2",
      "firstName": "Ashley",
      "fullName": "Rep. Hinson, Ashley [R-IA-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Hinson",
      "party": "R",
      "sponsorshipDate": "2025-10-03",
      "state": "IA"
    },
    {
      "bioguideId": "E000298",
      "district": "4",
      "firstName": "Ron",
      "fullName": "Rep. Estes, Ron [R-KS-4]",
      "isOriginalCosponsor": "False",
      "lastName": "Estes",
      "party": "R",
      "sponsorshipDate": "2025-10-08",
      "state": "KS"
    },
    {
      "bioguideId": "B001295",
      "district": "12",
      "firstName": "Mike",
      "fullName": "Rep. Bost, Mike [R-IL-12]",
      "isOriginalCosponsor": "False",
      "lastName": "Bost",
      "party": "R",
      "sponsorshipDate": "2025-10-10",
      "state": "IL"
    },
    {
      "bioguideId": "H001052",
      "district": "1",
      "firstName": "Andy",
      "fullName": "Rep. Harris, Andy [R-MD-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Harris",
      "party": "R",
      "sponsorshipDate": "2025-10-14",
      "state": "MD"
    },
    {
      "bioguideId": "M000871",
      "district": "1",
      "firstName": "Tracey",
      "fullName": "Rep. Mann, Tracey [R-KS-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Mann",
      "party": "R",
      "sponsorshipDate": "2025-10-17",
      "state": "KS"
    },
    {
      "bioguideId": "B001306",
      "district": "12",
      "firstName": "Troy",
      "fullName": "Rep. Balderson, Troy [R-OH-12]",
      "isOriginalCosponsor": "False",
      "lastName": "Balderson",
      "party": "R",
      "sponsorshipDate": "2025-10-17",
      "state": "OH"
    },
    {
      "bioguideId": "G000581",
      "district": "34",
      "firstName": "Vicente",
      "fullName": "Rep. Gonzalez, Vicente [D-TX-34]",
      "isOriginalCosponsor": "False",
      "lastName": "Gonzalez",
      "party": "D",
      "sponsorshipDate": "2025-10-24",
      "state": "TX"
    },
    {
      "bioguideId": "H001101",
      "district": "10",
      "firstName": "Pat",
      "fullName": "Rep. Harrigan, Pat [R-NC-10]",
      "isOriginalCosponsor": "False",
      "lastName": "Harrigan",
      "party": "R",
      "sponsorshipDate": "2025-10-31",
      "state": "NC"
    },
    {
      "bioguideId": "G000591",
      "district": "3",
      "firstName": "Michael",
      "fullName": "Rep. Guest, Michael [R-MS-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Guest",
      "party": "R",
      "sponsorshipDate": "2025-10-31",
      "state": "MS"
    },
    {
      "bioguideId": "L000583",
      "district": "11",
      "firstName": "Barry",
      "fullName": "Rep. Loudermilk, Barry [R-GA-11]",
      "isOriginalCosponsor": "False",
      "lastName": "Loudermilk",
      "party": "R",
      "sponsorshipDate": "2025-11-07",
      "state": "GA"
    },
    {
      "bioguideId": "C001119",
      "district": "2",
      "firstName": "Angie",
      "fullName": "Rep. Craig, Angie [D-MN-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Craig",
      "party": "D",
      "sponsorshipDate": "2025-11-07",
      "state": "MN"
    },
    {
      "bioguideId": "L000566",
      "district": "5",
      "firstName": "Robert",
      "fullName": "Rep. Latta, Robert E. [R-OH-5]",
      "isOriginalCosponsor": "False",
      "lastName": "Latta",
      "middleName": "E.",
      "party": "R",
      "sponsorshipDate": "2025-11-07",
      "state": "OH"
    },
    {
      "bioguideId": "M001212",
      "district": "1",
      "firstName": "Barry",
      "fullName": "Rep. Moore, Barry [R-AL-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Moore",
      "party": "R",
      "sponsorshipDate": "2025-11-12",
      "state": "AL"
    },
    {
      "bioguideId": "F000471",
      "district": "5",
      "firstName": "Scott",
      "fullName": "Rep. Fitzgerald, Scott [R-WI-5]",
      "isOriginalCosponsor": "False",
      "lastName": "Fitzgerald",
      "party": "R",
      "sponsorshipDate": "2025-11-12",
      "state": "WI"
    },
    {
      "bioguideId": "V000134",
      "district": "24",
      "firstName": "Beth",
      "fullName": "Rep. Van Duyne, Beth [R-TX-24]",
      "isOriginalCosponsor": "False",
      "lastName": "Van Duyne",
      "party": "R",
      "sponsorshipDate": "2025-11-17",
      "state": "TX"
    },
    {
      "bioguideId": "G000558",
      "district": "2",
      "firstName": "Brett",
      "fullName": "Rep. Guthrie, Brett [R-KY-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Guthrie",
      "party": "R",
      "sponsorshipDate": "2025-11-18",
      "state": "KY"
    },
    {
      "bioguideId": "W000809",
      "district": "3",
      "firstName": "Steve",
      "fullName": "Rep. Womack, Steve [R-AR-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Womack",
      "party": "R",
      "sponsorshipDate": "2025-12-02",
      "state": "AR"
    },
    {
      "bioguideId": "T000490",
      "district": "2",
      "firstName": "David",
      "fullName": "Rep. Taylor, David J. [R-OH-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Taylor",
      "middleName": "J.",
      "party": "R",
      "sponsorshipDate": "2025-12-02",
      "state": "OH"
    },
    {
      "bioguideId": "R000395",
      "district": "5",
      "firstName": "Harold",
      "fullName": "Rep. Rogers, Harold [R-KY-5]",
      "isOriginalCosponsor": "False",
      "lastName": "Rogers",
      "party": "R",
      "sponsorshipDate": "2025-12-03",
      "state": "KY"
    },
    {
      "bioguideId": "T000480",
      "district": "4",
      "firstName": "William",
      "fullName": "Rep. Timmons, William R. [R-SC-4]",
      "isOriginalCosponsor": "False",
      "lastName": "Timmons",
      "middleName": "R.",
      "party": "R",
      "sponsorshipDate": "2025-12-10",
      "state": "SC"
    },
    {
      "bioguideId": "E000235",
      "district": "4",
      "firstName": "Mike",
      "fullName": "Rep. Ezell, Mike [R-MS-4]",
      "isOriginalCosponsor": "False",
      "lastName": "Ezell",
      "party": "R",
      "sponsorshipDate": "2026-02-09",
      "state": "MS"
    },
    {
      "bioguideId": "D000032",
      "district": "19",
      "firstName": "Byron",
      "fullName": "Rep. Donalds, Byron [R-FL-19]",
      "isOriginalCosponsor": "False",
      "lastName": "Donalds",
      "party": "R",
      "sponsorshipDate": "2026-04-16",
      "state": "FL"
    },
    {
      "bioguideId": "B001321",
      "district": "7",
      "firstName": "Tom",
      "fullName": "Rep. Barrett, Tom [R-MI-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Barrett",
      "party": "R",
      "sponsorshipDate": "2026-04-28",
      "state": "MI"
    },
    {
      "bioguideId": "M001199",
      "district": "21",
      "firstName": "Brian",
      "fullName": "Rep. Mast, Brian J. [R-FL-21]",
      "isOriginalCosponsor": "False",
      "lastName": "Mast",
      "middleName": "J.",
      "party": "R",
      "sponsorshipDate": "2026-05-13",
      "state": "FL"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr5563ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 5563\nIN THE HOUSE OF REPRESENTATIVES\nSeptember 26, 2025 Mr. Crawford (for himself, Mr. Golden of Maine , Mr. Westerman , Mr. Carbajal , Mr. LaHood , and Ms. Perez ) introduced the following bill; which was referred to the Committee on Transportation and Infrastructure\nA BILL\nTo establish an apprenticeship program for commercial drivers under the age of 21, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Developing Responsible Individuals for a Vibrant Economy Act or the DRIVE-SAFE Act .\n#### 2. Apprenticeship program for commercial drivers under the age of 21\n##### (a) Definitions\nIn this section:\n**(1) Apprentice**\nThe term apprentice means an employee under the age of 21 who holds a commercial driver\u2019s license required to operate a class of vehicles described in part 383 of title 49, Code of Federal Regulations.\n**(2) Commercial driver's license**\nThe term commercial driver's license has the meaning given the term in section 31301 of title 49, United States Code.\n**(3) Commercial motor vehicle**\nThe term commercial motor vehicle means a commercial motor vehicle that meets the definition under paragraph (1) or (4) of the definition of the term commercial motor vehicle in section 390.5 of title 49, Code of Federal Regulations (as in effect on the date of enactment of this Act).\n**(4) Driving time**\nThe term driving time has the meaning given the term in section 395.2 of title 49, Code of Federal Regulations (as in effect on the date of enactment of this Act).\n**(5) Employee**\nThe term employee has the meaning given such term in section 31132 of title 49, United States Code.\n**(6) Employer**\nThe term employer has the meaning given such term in section 31132 of title 49, United States Code.\n**(7) Experienced driver**\nThe term experienced driver means an individual who\u2014\n**(A)**\nis not less than 26 years of age;\n**(B)**\nhas held a commercial driver\u2019s license for the 2-year period ending on the date on which the individual serves as an experienced driver under subsection (c)(3)(B);\n**(C)**\nhas had no preventable accidents reportable to the Department of Transportation or pointed moving violations during the 1-year period ending on the date on which the individual serves as an experienced driver under subsection (c)(3)(B); and\n**(D)**\nhas a minimum of 2 years of experience driving a commercial motor vehicle in interstate commerce.\n**(8) On-duty time**\nThe term on-duty time has the meaning given the term in section 395.2 of title 49, Code of Federal Regulations (as in effect on the date of enactment of this Act).\n**(9) Pointed moving violation**\nThe term pointed moving violation means a violation that results in points being added to the license of a driver, or a similar comparable violation, as determined by the Secretary.\n**(10) Secretary**\nThe term Secretary means the Secretary of Transportation.\n##### (b) Apprentice\nAn apprentice may\u2014\n**(1)**\ndrive a commercial motor vehicle in interstate commerce while taking part in the 120-hour probationary period under subsection (c)(1) or the 280-hour probationary period under subsection (c)(2), pursuant to an apprenticeship program established by an employer in accordance with this section; and\n**(2)**\ndrive a commercial motor vehicle in interstate commerce after the apprentice completes an apprenticeship program described in paragraph (1).\n##### (c) Apprenticeship program\nAn apprenticeship program referred to in subsection (b) is a program that consists of the following requirements:\n**(1) 120-hour probationary period**\n**(A) In general**\nThe apprentice shall complete 120 hours of on-duty time, of which not less than 80 hours are driving time in a commercial motor vehicle.\n**(B) Performance benchmarks**\nIn order to complete the 120-hour probationary period under subparagraph (A), an employer shall determine that the apprentice is competent in each of the following areas:\n**(i)**\nInterstate, city traffic, rural 2-lane, and evening driving.\n**(ii)**\nSafety awareness.\n**(iii)**\nSpeed and space management.\n**(iv)**\nLane control.\n**(v)**\nMirror scanning.\n**(vi)**\nRight and left turns.\n**(vii)**\nLogging and complying with rules relating to hours of service.\n**(2) 280-hour probationary period**\n**(A) In general**\nAfter completing the 120-hour probationary period under paragraph (1), the apprentice shall complete 280 hours of on-duty time, of which not less than 160 hours are driving time in a commercial motor vehicle.\n**(B) Performance benchmarks**\nIn order to complete the 280-hour probationary period under subparagraph (A), an employer shall determine that the apprentice is competent in each of the following areas:\n**(i)**\nBacking and maneuvering in close quarters.\n**(ii)**\nPre-trip inspections.\n**(iii)**\nFueling procedures.\n**(iv)**\nWeighing loads, weight distribution, and sliding tandems.\n**(v)**\nCoupling and uncoupling procedures.\n**(vi)**\nTrip planning, truck routes, map reading, navigation, and permits.\n**(3) Restrictions for 120-hour and 280-hour probationary periods**\nDuring the 120-hour probationary period under paragraph (1) and the 280-hour probationary period under paragraph (2)\u2014\n**(A)**\nthe apprentice may only drive a commercial motor vehicle that has\u2014\n**(i)**\nautomatic manual or automatic transmissions;\n**(ii)**\nactive braking collision mitigation systems; and\n**(iii)**\nforward-facing video event capture; and\n**(B)**\nthe apprentice shall be accompanied in the cab of the commercial motor vehicle by an experienced driver.\n**(4) Records retention**\nThe employer shall maintain records, in a manner required by the Secretary, relating to the satisfaction of the requirements of paragraphs (1)(B) and (2)(B) by the apprentice.\n**(5) Reportable incidents**\nIf the apprentice is involved in a preventable accident reportable to the Department of Transportation or a pointed moving violation while driving a commercial motor vehicle as part of an apprenticeship program described in this subsection, the apprentice shall undergo remediation and additional training until the apprentice can demonstrate, to the satisfaction of the employer, competence in each of the performance benchmarks described in paragraphs (1)(B) and (2)(B).\n**(6) Completion of program**\nThe apprentice shall be considered to have completed the apprenticeship program on the date on which the apprentice completes the 280-hour probationary period under paragraph (2).\n**(7) Minimum requirements**\n**(A) In general**\nNothing in this Act prevents an employer from imposing additional requirements on an apprentice taking part in an apprenticeship program established pursuant to this section.\n**(B) Technologies**\nNothing in this Act prevents an employer from requiring or installing additional technologies in a commercial motor vehicle in addition to the technologies described in paragraph (3)(A).\n##### (d) Regulations\nNot later than 1 year after the date of enactment of this Act, the Secretary shall promulgate regulations to implement this Act.\n##### (e) No effect on license requirement\nNothing in this Act exempts an apprentice from any requirement to hold a commercial driver\u2019s license in order to operate a commercial motor vehicle.\n##### (f) Employer responsibility\nAn employer shall not knowingly allow, require, permit, or authorize a driver under the age of 21 to operate a commercial motor vehicle in interstate commerce unless the driver is participating in or has completed an apprenticeship program that meets the requirements of subsection (c).",
      "versionDate": "2025-09-26",
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
      "legislativeSubjects": "",
      "policyArea": {
        "name": "Labor and Employment",
        "updateDate": "2025-12-08T16:01:03Z"
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
      "date": "2025-09-26",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr5563ih.xml"
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
      "title": "DRIVE-SAFE Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-10-03T10:38:14Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "DRIVE-SAFE Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-10-03T10:38:13Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Developing Responsible Individuals for a Vibrant Economy Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-10-03T10:38:13Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To establish an apprenticeship program for commercial drivers under the age of 21, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-10-03T10:33:15Z"
    }
  ]
}
```
