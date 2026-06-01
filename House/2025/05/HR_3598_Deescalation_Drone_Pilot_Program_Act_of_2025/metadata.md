# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/3598?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/3598
- Title: Deescalation Drone Pilot Program Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 3598
- Origin chamber: House
- Introduced date: 2025-05-23
- Update date: 2026-05-13T16:15:32Z
- Update date including text: 2026-05-13T16:15:32Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-05-23: Introduced in House
- 2025-05-23 - IntroReferral: Introduced in House
- 2025-05-23 - IntroReferral: Introduced in House
- 2025-05-23 - IntroReferral: Referred to the House Committee on Transportation and Infrastructure.
- 2025-05-24 - Committee: Referred to the Subcommittee on Aviation.
- Latest action: 2025-05-23: Introduced in House

## Actions

- 2025-05-23 - IntroReferral: Introduced in House
- 2025-05-23 - IntroReferral: Introduced in House
- 2025-05-23 - IntroReferral: Referred to the House Committee on Transportation and Infrastructure.
- 2025-05-24 - Committee: Referred to the Subcommittee on Aviation.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-05-23",
    "latestAction": {
      "actionDate": "2025-05-23",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/3598",
    "number": "3598",
    "originChamber": "House",
    "policyArea": {
      "name": "Transportation and Public Works"
    },
    "sponsors": [
      {
        "bioguideId": "N000026",
        "district": "22",
        "firstName": "Troy",
        "fullName": "Rep. Nehls, Troy E. [R-TX-22]",
        "lastName": "Nehls",
        "party": "R",
        "state": "TX"
      }
    ],
    "title": "Deescalation Drone Pilot Program Act of 2025",
    "type": "HR",
    "updateDate": "2026-05-13T16:15:32Z",
    "updateDateIncludingText": "2026-05-13T16:15:32Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-05-24",
      "committees": {
        "item": {
          "name": "Aviation Subcommittee",
          "systemCode": "hspw05"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Referred to the Subcommittee on Aviation.",
      "type": "Committee"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-05-23",
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
      "actionDate": "2025-05-23",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-05-23",
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
          "date": "2025-05-23T14:02:50Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Transportation and Infrastructure Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": {
              "date": "2025-05-24T18:52:32Z",
              "name": "Referred to"
            }
          },
          "name": "Aviation Subcommittee",
          "systemCode": "hspw05"
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
      "bioguideId": "D000230",
      "district": "1",
      "firstName": "Donald",
      "fullName": "Rep. Davis, Donald G. [D-NC-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Davis",
      "middleName": "G.",
      "party": "D",
      "sponsorshipDate": "2025-05-23",
      "state": "NC"
    },
    {
      "bioguideId": "F000475",
      "district": "1",
      "firstName": "Brad",
      "fullName": "Rep. Finstad, Brad [R-MN-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Finstad",
      "party": "R",
      "sponsorshipDate": "2025-05-23",
      "state": "MN"
    },
    {
      "bioguideId": "H001077",
      "district": "3",
      "firstName": "Clay",
      "fullName": "Rep. Higgins, Clay [R-LA-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Higgins",
      "party": "R",
      "sponsorshipDate": "2025-05-23",
      "state": "LA"
    },
    {
      "bioguideId": "B000825",
      "district": "4",
      "firstName": "Lauren",
      "fullName": "Rep. Boebert, Lauren [R-CO-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Boebert",
      "party": "R",
      "sponsorshipDate": "2025-05-23",
      "state": "CO"
    },
    {
      "bioguideId": "S001212",
      "district": "8",
      "firstName": "Pete",
      "fullName": "Rep. Stauber, Pete [R-MN-8]",
      "isOriginalCosponsor": "True",
      "lastName": "Stauber",
      "party": "R",
      "sponsorshipDate": "2025-05-23",
      "state": "MN"
    },
    {
      "bioguideId": "M001212",
      "district": "1",
      "firstName": "Barry",
      "fullName": "Rep. Moore, Barry [R-AL-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Moore",
      "party": "R",
      "sponsorshipDate": "2025-05-23",
      "state": "AL"
    },
    {
      "bioguideId": "N000189",
      "district": "4",
      "firstName": "Dan",
      "fullName": "Rep. Newhouse, Dan [R-WA-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Newhouse",
      "party": "R",
      "sponsorshipDate": "2025-05-23",
      "state": "WA"
    },
    {
      "bioguideId": "Z000018",
      "district": "1",
      "firstName": "Ryan",
      "fullName": "Rep. Zinke, Ryan K. [R-MT-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Zinke",
      "middleName": "K.",
      "party": "R",
      "sponsorshipDate": "2025-05-23",
      "state": "MT"
    },
    {
      "bioguideId": "W000829",
      "district": "8",
      "firstName": "Tony",
      "fullName": "Rep. Wied, Tony [R-WI-8]",
      "isOriginalCosponsor": "True",
      "lastName": "Wied",
      "party": "R",
      "sponsorshipDate": "2025-05-23",
      "state": "WI"
    },
    {
      "bioguideId": "M001228",
      "district": "2",
      "firstName": "Celeste",
      "fullName": "Rep. Maloy, Celeste [R-UT-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Maloy",
      "party": "R",
      "sponsorshipDate": "2025-05-23",
      "state": "UT"
    },
    {
      "bioguideId": "E000235",
      "district": "4",
      "firstName": "Mike",
      "fullName": "Rep. Ezell, Mike [R-MS-4]",
      "isOriginalCosponsor": "False",
      "lastName": "Ezell",
      "party": "R",
      "sponsorshipDate": "2025-05-29",
      "state": "MS"
    },
    {
      "bioguideId": "H001095",
      "district": "38",
      "firstName": "Wesley",
      "fullName": "Rep. Hunt, Wesley [R-TX-38]",
      "isOriginalCosponsor": "False",
      "lastName": "Hunt",
      "party": "R",
      "sponsorshipDate": "2025-06-03",
      "state": "TX"
    },
    {
      "bioguideId": "R000609",
      "district": "5",
      "firstName": "John",
      "fullName": "Rep. Rutherford, John H. [R-FL-5]",
      "isOriginalCosponsor": "False",
      "lastName": "Rutherford",
      "middleName": "H.",
      "party": "R",
      "sponsorshipDate": "2025-06-03",
      "state": "FL"
    },
    {
      "bioguideId": "B001309",
      "district": "2",
      "firstName": "Tim",
      "fullName": "Rep. Burchett, Tim [R-TN-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Burchett",
      "party": "R",
      "sponsorshipDate": "2025-06-10",
      "state": "TN"
    },
    {
      "bioguideId": "G000591",
      "district": "3",
      "firstName": "Michael",
      "fullName": "Rep. Guest, Michael [R-MS-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Guest",
      "party": "R",
      "sponsorshipDate": "2025-06-12",
      "state": "MS"
    },
    {
      "bioguideId": "V000134",
      "district": "24",
      "firstName": "Beth",
      "fullName": "Rep. Van Duyne, Beth [R-TX-24]",
      "isOriginalCosponsor": "False",
      "lastName": "Van Duyne",
      "party": "R",
      "sponsorshipDate": "2025-07-02",
      "state": "TX"
    },
    {
      "bioguideId": "G000603",
      "district": "26",
      "firstName": "Brandon",
      "fullName": "Rep. Gill, Brandon [R-TX-26]",
      "isOriginalCosponsor": "False",
      "lastName": "Gill",
      "party": "R",
      "sponsorshipDate": "2025-09-03",
      "state": "TX"
    },
    {
      "bioguideId": "S001183",
      "district": "1",
      "firstName": "David",
      "fullName": "Rep. Schweikert, David [R-AZ-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Schweikert",
      "party": "R",
      "sponsorshipDate": "2025-09-04",
      "state": "AZ"
    },
    {
      "bioguideId": "G000576",
      "district": "6",
      "firstName": "Glenn",
      "fullName": "Rep. Grothman, Glenn [R-WI-6]",
      "isOriginalCosponsor": "False",
      "lastName": "Grothman",
      "party": "R",
      "sponsorshipDate": "2025-09-08",
      "state": "WI"
    },
    {
      "bioguideId": "C001110",
      "district": "46",
      "firstName": "J.",
      "fullName": "Rep. Correa, J. Luis [D-CA-46]",
      "isOriginalCosponsor": "False",
      "lastName": "Correa",
      "middleName": "Luis",
      "party": "D",
      "sponsorshipDate": "2025-09-08",
      "state": "CA"
    },
    {
      "bioguideId": "V000138",
      "district": "7",
      "firstName": "Eugene",
      "fullName": "Rep. Vindman, Eugene Simon [D-VA-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Vindman",
      "middleName": "Simon",
      "party": "D",
      "sponsorshipDate": "2025-10-03",
      "state": "VA"
    },
    {
      "bioguideId": "M001222",
      "district": "7",
      "firstName": "Max",
      "fullName": "Rep. Miller, Max L. [R-OH-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Miller",
      "middleName": "L.",
      "party": "R",
      "sponsorshipDate": "2025-12-17",
      "state": "OH"
    },
    {
      "bioguideId": "V000135",
      "district": "3",
      "firstName": "Derrick",
      "fullName": "Rep. Van Orden, Derrick [R-WI-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Van Orden",
      "party": "R",
      "sponsorshipDate": "2025-12-19",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr3598ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 3598\nIN THE HOUSE OF REPRESENTATIVES\nMay 23, 2025 Mr. Nehls (for himself, Mr. Davis of North Carolina , Mr. Finstad , Mr. Higgins of Louisiana , Ms. Boebert , Mr. Stauber , Mr. Moore of Alabama , Mr. Newhouse , Mr. Zinke , Mr. Wied , and Ms. Maloy ) introduced the following bill; which was referred to the Committee on Transportation and Infrastructure\nA BILL\nTo amend title 49, United States Code, to establish a pilot program for small, nonlethal deescalation unmanned aircraft to be used for law enforcement and public safety, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Deescalation Drone Pilot Program Act of 2025 .\n#### 2. Small unmanned aircraft pilot program for law enforcement and public safety\n##### (a) In general\nChapter 448 of title 49, United States Code, is amended by adding at the end the following:\n44815. Small unmanned aircraft pilot program for law enforcement and public safety (a) Prohibition regarding weapons The prohibition regarding unmanned aircraft armed with dangerous weapons under section 363 of the FAA Reauthorization Act of 2018 ( 49 U.S.C. 44802 note) is reaffirmed. (b) Pilot program (1) In general Not later than 2 months after the date of enactment of this section, the Administrator of the Federal Aviation Administration shall establish a deescalation drone pilot program to review the potential use of nonlethal deescalation unmanned aircraft by Federal, State, local, or Tribal law enforcement responding to an active shooter event. (2) Contents The pilot program required under paragraph (1) shall\u2014 (A) address the process of reviewing and validating nonlethal weapons that may be affixed to an unmanned aircraft; (B) address training protocols for law enforcement and agents of the Administration for the use of nonlethal deescalation unmanned aircraft; (C) address operational and safety protocols for operators of nonlethal deescalation unmanned aircraft and agencies directly overseeing the operation of such unmanned aircraft; and (D) assess the efficacy of nonlethal deescalation unmanned aircraft in indoor active shooter events and the safety benefits associated with increasing the safe engagement distance between a law enforcement officer and an active shooter. (3) Partnerships In carrying out the pilot program under this subsection, the Administrator shall use existing partnerships with the unmanned aircraft system test ranges designated under section 44803, in collaboration with Federal, State, and large metropolitan area law enforcement. (4) Interagency aviation agreements The Administrator may enter into interagency aviation agreements, as necessary, with the Department of Justice, the Department of Homeland Security, and State large metropolitan and rural law enforcement agencies to support the pilot program under this subsection. (5) Consultation The Administrator shall solicit input from, and coordinate with, relevant stakeholders as appropriate in carrying out the pilot program established under this subsection. (6) Report Not later than 3 months after the conclusion of the pilot program, the Administrator shall submit to the Committee on Transportation and Infrastructure of the House of Representatives a report on the results of the pilot program that includes a plan outlining a proposed process through which a law enforcement applicant to such program may seek permission from the Administrator to operate nonlethal deescalation unmanned aircraft. (c) Rulemaking Not later than 60 days after submitting the report required under subsection (b)(6), the Administrator shall initiate a rulemaking to create a process through which the Administrator may provide approval\u2014 (1) for Federal, State, local, or Tribal law enforcement to operate nonlethal deescalation unmanned aircraft during an active shooter event; and (2) for manufacturers of nonlethal deescalation unmanned aircraft to operate such devices for testing, validation, and law enforcement demonstrations. (d) Manufacturing requirement Any nonlethal deescalation unmanned aircraft used under the pilot program shall be manufactured in the United States, as defined by the Federal Trade Commission under part 323 of title 16, Code of Federal Regulations. (e) Definitions In this section: (1) Active shooter event The term active shooter event means an event in which\u2014 (A) an individual is actively engaged in unlawfully killing or attempting to kill people using explosives as defined under chapter 40 of title 18, United States Code, or weapons subject to chapter 44 of title 18 or chapter 53 of the Internal Revenue Code of 1986; (B) responding to the event poses a significant risk to human life, including the lives of law enforcement personnel and other individuals; and (C) absent an immediate use of force, the individual described in subparagraph (A) would continue posing a threat to human life. (2) Nonlethal deescalation unmanned aircraft The term nonlethal deescalation unmanned aircraft means an unmanned aircraft operated by law enforcement that\u2014 (A) is only equipped or armed with 1 or more nonlethal weapons, including those that may be subject to the definition provided in section 930(g)(2) of title 18, United States Code; and (B) may be equipped with other nonlethal devices, including intense sound distraction emitters, cameras, targeting sensors, speakers, strobe lights and other similar collateral equipment. (3) Nonlethal weapon The term nonlethal weapon means a weapon, device, or munition that\u2014 (A) is explicitly designed and primarily employed to immediately incapacitate targeted individuals or property in the target area while minimizing\u2014 (i) fatalities; (ii) permanent injury to individuals; and (iii) undesired damage to property; and (B) is intended to have reversible effects on individuals and property. .\n##### (b) Clerical amendment\nThe analysis for chapter 448 of title 49, United States Code, is amended by adding at the end the following:\n\u201844815. Small unmanned aircraft pilot program for law enforcement and public safety. .",
      "versionDate": "2025-05-23",
      "versionType": "Introduced in House"
    }
  ]
}
```

## API Data: relatedbills

```json
{
  "relatedBills": [
    {
      "congress": "119",
      "latestAction": {
        "actionDate": "2026-04-15",
        "text": "Read twice and referred to the Committee on Commerce, Science, and Transportation."
      },
      "number": "4309",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Deescalation Drone Pilot Program Act of 2026",
      "type": "S"
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
        "updateDate": "2025-06-03T13:15:24Z"
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
      "date": "2025-05-23",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr3598ih.xml"
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
      "title": "Deescalation Drone Pilot Program Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-06-03T04:23:22Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Deescalation Drone Pilot Program Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-06-03T04:23:20Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend title 49, United States Code, to establish a pilot program for small, nonlethal deescalation unmanned aircraft to be used for law enforcement and public safety, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-06-03T04:18:29Z"
    }
  ]
}
```
