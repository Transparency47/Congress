# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/6643?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/6643
- Title: American Border Story Memorial Act
- Congress: 119
- Bill type: HR
- Bill number: 6643
- Origin chamber: House
- Introduced date: 2025-12-11
- Update date: 2026-02-26T09:07:03Z
- Update date including text: 2026-02-26T09:07:03Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-12-11: Introduced in House
- 2025-12-11 - IntroReferral: Introduced in House
- 2025-12-11 - IntroReferral: Introduced in House
- 2025-12-11 - IntroReferral: Referred to the House Committee on Natural Resources.
- Latest action: 2025-12-11: Introduced in House

## Actions

- 2025-12-11 - IntroReferral: Introduced in House
- 2025-12-11 - IntroReferral: Introduced in House
- 2025-12-11 - IntroReferral: Referred to the House Committee on Natural Resources.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-12-11",
    "latestAction": {
      "actionDate": "2025-12-11",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/6643",
    "number": "6643",
    "originChamber": "House",
    "policyArea": {
      "name": "Public Lands and Natural Resources"
    },
    "sponsors": [
      {
        "bioguideId": "H001098",
        "district": "8",
        "firstName": "Abraham",
        "fullName": "Rep. Hamadeh, Abraham J. [R-AZ-8]",
        "lastName": "Hamadeh",
        "party": "R",
        "state": "AZ"
      }
    ],
    "title": "American Border Story Memorial Act",
    "type": "HR",
    "updateDate": "2026-02-26T09:07:03Z",
    "updateDateIncludingText": "2026-02-26T09:07:03Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-12-11",
      "committees": {
        "item": {
          "name": "Natural Resources Committee",
          "systemCode": "hsii00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Natural Resources.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-12-11",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-12-11",
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
          "date": "2025-12-11T16:10:25Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Natural Resources Committee",
      "systemCode": "hsii00",
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
      "bioguideId": "G000594",
      "district": "23",
      "firstName": "Tony",
      "fullName": "Rep. Gonzales, Tony [R-TX-23]",
      "isOriginalCosponsor": "True",
      "lastName": "Gonzales",
      "party": "R",
      "sponsorshipDate": "2025-12-11",
      "state": "TX"
    },
    {
      "bioguideId": "N000026",
      "district": "22",
      "firstName": "Troy",
      "fullName": "Rep. Nehls, Troy E. [R-TX-22]",
      "isOriginalCosponsor": "True",
      "lastName": "Nehls",
      "middleName": "E.",
      "party": "R",
      "sponsorshipDate": "2025-12-11",
      "state": "TX"
    },
    {
      "bioguideId": "S000250",
      "district": "17",
      "firstName": "Pete",
      "fullName": "Rep. Sessions, Pete [R-TX-17]",
      "isOriginalCosponsor": "True",
      "lastName": "Sessions",
      "party": "R",
      "sponsorshipDate": "2025-12-11",
      "state": "TX"
    },
    {
      "bioguideId": "B001291",
      "district": "36",
      "firstName": "Brian",
      "fullName": "Rep. Babin, Brian [R-TX-36]",
      "isOriginalCosponsor": "True",
      "lastName": "Babin",
      "party": "R",
      "sponsorshipDate": "2025-12-11",
      "state": "TX"
    },
    {
      "bioguideId": "O000019",
      "district": "23",
      "firstName": "Jay",
      "fullName": "Rep. Obernolte, Jay [R-CA-23]",
      "isOriginalCosponsor": "True",
      "lastName": "Obernolte",
      "party": "R",
      "sponsorshipDate": "2025-12-11",
      "state": "CA"
    },
    {
      "bioguideId": "B001302",
      "district": "5",
      "firstName": "Andy",
      "fullName": "Rep. Biggs, Andy [R-AZ-5]",
      "isOriginalCosponsor": "True",
      "lastName": "Biggs",
      "party": "R",
      "sponsorshipDate": "2025-12-11",
      "state": "AZ"
    },
    {
      "bioguideId": "H001095",
      "district": "38",
      "firstName": "Wesley",
      "fullName": "Rep. Hunt, Wesley [R-TX-38]",
      "isOriginalCosponsor": "True",
      "lastName": "Hunt",
      "party": "R",
      "sponsorshipDate": "2025-12-11",
      "state": "TX"
    },
    {
      "bioguideId": "C001120",
      "district": "2",
      "firstName": "Dan",
      "fullName": "Rep. Crenshaw, Dan [R-TX-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Crenshaw",
      "party": "R",
      "sponsorshipDate": "2025-12-11",
      "state": "TX"
    },
    {
      "bioguideId": "P000048",
      "district": "11",
      "firstName": "August",
      "fullName": "Rep. Pfluger, August [R-TX-11]",
      "isOriginalCosponsor": "False",
      "lastName": "Pfluger",
      "party": "R",
      "sponsorshipDate": "2025-12-15",
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
      "sponsorshipDate": "2025-12-15",
      "state": "TX"
    },
    {
      "bioguideId": "R000612",
      "district": "6",
      "firstName": "John",
      "fullName": "Rep. Rose, John W. [R-TN-6]",
      "isOriginalCosponsor": "False",
      "lastName": "Rose",
      "middleName": "W.",
      "party": "R",
      "sponsorshipDate": "2026-01-16",
      "state": "TN"
    },
    {
      "bioguideId": "C001103",
      "district": "1",
      "firstName": "Earl",
      "fullName": "Rep. Carter, Earl L. \"Buddy\" [R-GA-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Carter",
      "middleName": "L. \"Buddy\"",
      "party": "R",
      "sponsorshipDate": "2026-02-25",
      "state": "GA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6643ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 6643\nIN THE HOUSE OF REPRESENTATIVES\nDecember 11, 2025 Mr. Hamadeh of Arizona (for himself, Mr. Tony Gonzales of Texas , Mr. Nehls , Mr. Sessions , Mr. Babin , Mr. Obernolte , Mr. Biggs of Arizona , Mr. Hunt , and Mr. Crenshaw ) introduced the following bill; which was referred to the Committee on Natural Resources\nA BILL\nTo authorize a commemorative work in the District of Columbia and its environs to honor United States citizens and legal residents who lost their lives as victims of crimes committed by individuals unlawfully present in the United States, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the American Border Story Memorial Act .\n#### 2. Authorization of memorial\n##### (a) In general\nThe American Border Story (TABS) may establish a commemorative work on Federal land in the District of Columbia and its environs to honor United States citizens and legal residents who lost their lives as victims of crimes committed by individuals unlawfully present in the United States.\n##### (b) Compliance with standards for commemorative works\nNotwithstanding section 8903(c) of title 40, United States Code, the establishment of the commemorative work under this section shall be in accordance with chapter 89 of that title, United States Code (commonly known as the Commemorative Works Act ).\n##### (c) Prohibition on the use of Federal funds\nFederal funds may not be used to pay any expense of the establishment of the commemorative work under this section.\n##### (d) Deposit of excess funds\n**(1) In general**\nIf upon payment of all expenses for the establishment of the commemorative work (including the maintenance and preservation amount required by section 8906(b)(1) of title 40, United States Code), there remains a balance of funds received for such establishment, The American Border Story shall transmit the amount of the balance to the Secretary of the Interior for deposit in the account provided for in section 8906(b)(3) of title 40, United States Code.\n**(2) On expiration of authority**\nIf upon expiration of the authority for the commemorative work under section 8903(e) of title 40, United States Code, there remains a balance of funds received for the establishment of the commemorative work, The American Border Story shall transmit the amount of the balance to a separate account with the National Park Foundation for memorials, to be available to the Secretary of the Interior or the Administrator of General Services (as appropriate) following the process provided in section 8906(b)(4) of title 40, United States Code, for accounts established under paragraphs (2) and (3) of section 8906(b) of title 40, United States Code.",
      "versionDate": "2025-12-11",
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
        "name": "Public Lands and Natural Resources",
        "updateDate": "2026-01-07T17:17:49Z"
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
      "date": "2025-12-11",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6643ih.xml"
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
      "title": "American Border Story Memorial Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-01-03T06:53:18Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "American Border Story Memorial Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-01-03T06:53:17Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To authorize a commemorative work in the District of Columbia and its environs to honor United States citizens and legal residents who lost their lives as victims of crimes committed by individuals unlawfully present in the United States, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-01-03T06:48:23Z"
    }
  ]
}
```
