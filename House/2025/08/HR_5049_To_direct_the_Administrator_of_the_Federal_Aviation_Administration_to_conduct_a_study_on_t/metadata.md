# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/5049?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/5049
- Title: Protecting Communities from Helicopter Noise Act
- Congress: 119
- Bill type: HR
- Bill number: 5049
- Origin chamber: House
- Introduced date: 2025-08-26
- Update date: 2026-05-08T08:06:33Z
- Update date including text: 2026-05-08T08:06:33Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-08-26: Introduced in House
- 2025-08-26 - IntroReferral: Introduced in House
- 2025-08-26 - IntroReferral: Introduced in House
- 2025-08-26 - IntroReferral: Referred to the House Committee on Transportation and Infrastructure.
- 2025-08-27 - Committee: Referred to the Subcommittee on Aviation.
- Latest action: 2025-08-26: Introduced in House

## Actions

- 2025-08-26 - IntroReferral: Introduced in House
- 2025-08-26 - IntroReferral: Introduced in House
- 2025-08-26 - IntroReferral: Referred to the House Committee on Transportation and Infrastructure.
- 2025-08-27 - Committee: Referred to the Subcommittee on Aviation.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-08-26",
    "latestAction": {
      "actionDate": "2025-08-26",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/5049",
    "number": "5049",
    "originChamber": "House",
    "policyArea": {
      "name": "Transportation and Public Works"
    },
    "sponsors": [
      {
        "bioguideId": "M001226",
        "district": "8",
        "firstName": "Robert",
        "fullName": "Rep. Menendez, Robert [D-NJ-8]",
        "lastName": "Menendez",
        "party": "D",
        "state": "NJ"
      }
    ],
    "title": "Protecting Communities from Helicopter Noise Act",
    "type": "HR",
    "updateDate": "2026-05-08T08:06:33Z",
    "updateDateIncludingText": "2026-05-08T08:06:33Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-08-27",
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
      "actionDate": "2025-08-26",
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
      "actionDate": "2025-08-26",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-08-26",
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
          "date": "2025-08-26T15:01:25Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Transportation and Infrastructure Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": {
              "date": "2025-08-27T21:36:58Z",
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
      "bioguideId": "N000002",
      "district": "12",
      "firstName": "Jerrold",
      "fullName": "Rep. Nadler, Jerrold [D-NY-12]",
      "isOriginalCosponsor": "True",
      "lastName": "Nadler",
      "party": "D",
      "sponsorshipDate": "2025-08-26",
      "state": "NY"
    },
    {
      "bioguideId": "M000317",
      "district": "11",
      "firstName": "Nicole",
      "fullName": "Rep. Malliotakis, Nicole [R-NY-11]",
      "isOriginalCosponsor": "True",
      "lastName": "Malliotakis",
      "party": "R",
      "sponsorshipDate": "2025-08-26",
      "state": "NY"
    },
    {
      "bioguideId": "G000599",
      "district": "10",
      "firstName": "Daniel",
      "fullName": "Rep. Goldman, Daniel S. [D-NY-10]",
      "isOriginalCosponsor": "True",
      "lastName": "Goldman",
      "middleName": "S.",
      "party": "D",
      "sponsorshipDate": "2025-08-26",
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
      "sponsorshipDate": "2025-08-26",
      "state": "NJ"
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
      "sponsorshipDate": "2025-09-10",
      "state": "PA"
    },
    {
      "bioguideId": "P000621",
      "district": "9",
      "firstName": "Nellie",
      "fullName": "Rep. Pou, Nellie [D-NJ-9]",
      "isOriginalCosponsor": "False",
      "lastName": "Pou",
      "party": "D",
      "sponsorshipDate": "2026-05-07",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr5049ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 5049\nIN THE HOUSE OF REPRESENTATIVES\nAugust 26, 2025 Mr. Menendez (for himself, Mr. Nadler , Ms. Malliotakis , Mr. Goldman of New York , and Mrs. McIver ) introduced the following bill; which was referred to the Committee on Transportation and Infrastructure\nA BILL\nTo direct the Administrator of the Federal Aviation Administration to conduct a study on the operation of helicopters within a 20-mile radius of the Statue of Liberty National Monument, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Protecting Communities from Helicopter Noise Act .\n#### 2. Study on helicopter operations\n##### (a) In general\nThe Administrator of the Federal Aviation Administration shall conduct a study on helicopter operations within a 20-mile radius of the Statue of Liberty National Monument.\n##### (b) Contents\nIn conducting the study under subsection (a), the Administrator shall focus on the following items:\n**(1)**\nThe effect of persistent helicopter noise on residential and recreational areas, including\u2014\n**(A)**\nan analysis of the volume of helicopter traffic, including the time helicopters are flying and the frequency of helicopters traversing the airspace;\n**(B)**\nan analysis of noise levels related to helicopter operations;\n**(C)**\nan analysis of safety, health, environmental, and economic issues related to helicopter operations;\n**(D)**\nan analysis of whether helicopters are following the terms and conditions of voluntary agreements, including the Statue of Liberty National Monument and Governors Island National Monument Voluntary Agreement;\n**(E)**\nan analysis of the origination of helicopters traversing the airspace within a 20-mile radius of the Statue of Liberty National Monument;\n**(F)**\nan analysis of the necessity of helicopter traffic within a 20-mile radius of the Statue of Liberty National Monument;\n**(G)**\nan analysis of how helicopters contribute to the congestion of the airspace within a 20-mile radius of the Statue of Liberty;\n**(H)**\nan projection of how electric vertical take off and landing aircraft or other advanced air mobility technologies will contribute to the congestion, noise, and safety of the airspace within a 20-mile radius of the Statue of Liberty;\n**(I)**\nan analysis of the quality of life of residents living in areas with high volumes of helicopter noise; and\n**(J)**\nan analysis of any other issue related to helicopter traffic on residential and recreational areas.\n**(2)**\nSolutions to abate or eliminate helicopter noise on residential and recreational areas, including\u2014\n**(A)**\nthe feasibility of diverting helicopters from residential and recreational areas;\n**(B)**\nthe feasibility of creating new flight paths for helicopters, with attention to the presence of airports within a 20-mile radius of the Statue of Liberty National Monument;\n**(C)**\nan analysis of whether banning nonessential helicopters within a 20-mile radius of the Statue of Liberty will increase the overall safety, health, and environment of the community;\n**(D)**\nthe feasibility of establishing altitude limits for helicopter operations in and around within a 20-mile radius of the Statue of Liberty National Monument; and\n**(E)**\nother options for abating helicopter noise.\n##### (c) Report\nNot later than 180 days after the date of enactment of this Act, the Administrator shall submit to Congress a report on the study under subsection (a).",
      "versionDate": "2025-08-26",
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
        "name": "Transportation and Public Works",
        "updateDate": "2025-09-19T16:59:03Z"
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
      "date": "2025-08-26",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr5049ih.xml"
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
      "title": "Protecting Communities from Helicopter Noise Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-08-27T08:23:19Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Protecting Communities from Helicopter Noise Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-08-27T08:23:19Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To direct the Administrator of the Federal Aviation Administration to conduct a study on the operation of helicopters within a 20-mile radius of the Statue of Liberty National Monument, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-08-27T08:18:17Z"
    }
  ]
}
```
