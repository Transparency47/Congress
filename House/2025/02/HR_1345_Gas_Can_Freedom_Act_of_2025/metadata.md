# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/1345?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/1345
- Title: Gas Can Freedom Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 1345
- Origin chamber: House
- Introduced date: 2025-02-13
- Update date: 2025-12-09T22:15:59Z
- Update date including text: 2025-12-09T22:15:59Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-02-13: Introduced in House
- 2025-02-13 - IntroReferral: Introduced in House
- 2025-02-13 - IntroReferral: Introduced in House
- 2025-02-13 - IntroReferral: Referred to the House Committee on Energy and Commerce.
- Latest action: 2025-02-13: Introduced in House

## Actions

- 2025-02-13 - IntroReferral: Introduced in House
- 2025-02-13 - IntroReferral: Introduced in House
- 2025-02-13 - IntroReferral: Referred to the House Committee on Energy and Commerce.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-02-13",
    "latestAction": {
      "actionDate": "2025-02-13",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/1345",
    "number": "1345",
    "originChamber": "House",
    "policyArea": {
      "name": "Commerce"
    },
    "sponsors": [
      {
        "bioguideId": "R000614",
        "district": "21",
        "firstName": "Chip",
        "fullName": "Rep. Roy, Chip [R-TX-21]",
        "lastName": "Roy",
        "party": "R",
        "state": "TX"
      }
    ],
    "title": "Gas Can Freedom Act of 2025",
    "type": "HR",
    "updateDate": "2025-12-09T22:15:59Z",
    "updateDateIncludingText": "2025-12-09T22:15:59Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-02-13",
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
      "actionDate": "2025-02-13",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-02-13",
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
          "date": "2025-02-13T14:09:05Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Energy and Commerce Committee",
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
      "bioguideId": "R000619",
      "district": "6",
      "firstName": "Michael",
      "fullName": "Rep. Rulli, Michael A. [R-OH-6]",
      "isOriginalCosponsor": "True",
      "lastName": "Rulli",
      "middleName": "A.",
      "party": "R",
      "sponsorshipDate": "2025-02-13",
      "state": "OH"
    },
    {
      "bioguideId": "P000605",
      "district": "10",
      "firstName": "Scott",
      "fullName": "Rep. Perry, Scott [R-PA-10]",
      "isOriginalCosponsor": "True",
      "lastName": "Perry",
      "party": "R",
      "sponsorshipDate": "2025-02-13",
      "state": "PA"
    },
    {
      "bioguideId": "B001302",
      "district": "5",
      "firstName": "Andy",
      "fullName": "Rep. Biggs, Andy [R-AZ-5]",
      "isOriginalCosponsor": "True",
      "lastName": "Biggs",
      "party": "R",
      "sponsorshipDate": "2025-02-13",
      "state": "AZ"
    },
    {
      "bioguideId": "M001184",
      "district": "4",
      "firstName": "Thomas",
      "fullName": "Rep. Massie, Thomas [R-KY-4]",
      "isOriginalCosponsor": "False",
      "lastName": "Massie",
      "party": "R",
      "sponsorshipDate": "2025-02-14",
      "state": "KY"
    },
    {
      "bioguideId": "B001317",
      "district": "2",
      "firstName": "Josh",
      "fullName": "Rep. Brecheen, Josh [R-OK-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Brecheen",
      "party": "R",
      "sponsorshipDate": "2025-02-14",
      "state": "OK"
    },
    {
      "bioguideId": "S001188",
      "district": "3",
      "firstName": "Marlin",
      "fullName": "Rep. Stutzman, Marlin A. [R-IN-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Stutzman",
      "middleName": "A.",
      "party": "R",
      "sponsorshipDate": "2025-02-14",
      "state": "IN"
    },
    {
      "bioguideId": "B001321",
      "district": "7",
      "firstName": "Tom",
      "fullName": "Rep. Barrett, Tom [R-MI-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Barrett",
      "party": "R",
      "sponsorshipDate": "2025-07-21",
      "state": "MI"
    },
    {
      "bioguideId": "C001116",
      "district": "9",
      "firstName": "Andrew",
      "fullName": "Rep. Clyde, Andrew S. [R-GA-9]",
      "isOriginalCosponsor": "False",
      "lastName": "Clyde",
      "middleName": "S.",
      "party": "R",
      "sponsorshipDate": "2025-07-23",
      "state": "GA"
    },
    {
      "bioguideId": "H001102",
      "district": "8",
      "firstName": "Mark",
      "fullName": "Rep. Harris, Mark [R-NC-8]",
      "isOriginalCosponsor": "False",
      "lastName": "Harris",
      "party": "R",
      "sponsorshipDate": "2025-07-29",
      "state": "NC"
    },
    {
      "bioguideId": "D000626",
      "district": "8",
      "firstName": "Warren",
      "fullName": "Rep. Davidson, Warren [R-OH-8]",
      "isOriginalCosponsor": "False",
      "lastName": "Davidson",
      "party": "R",
      "sponsorshipDate": "2025-11-07",
      "state": "OH"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1345ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 1345\nIN THE HOUSE OF REPRESENTATIVES\nFebruary 13, 2025 Mr. Roy (for himself, Mr. Rulli , Mr. Perry , and Mr. Biggs of Arizona ) introduced the following bill; which was referred to the Committee on Energy and Commerce\nA BILL\nTo repeal the Portable Fuel Container Safety Act of 2020 and the Children\u2019s Gasoline Burn Prevention Act, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Gas Can Freedom Act of 2025 .\n#### 2. Repeals\n##### (a) Portable Fuel Container Safety Act of 2020\nThe Portable Fuel Container Safety Act of 2020 ( 15 U.S.C. 2056d ) is repealed.\n##### (b) Children\u2019s Gasoline Burn Prevention Act\nThe Children\u2019s Gasoline Burn Prevention Act ( 15 U.S.C. 2056 note) is repealed.\n##### (c) Regulations\n**(1) Effect of repeal**\nA regulation promulgated by the Consumer Product Safety Commission pursuant to an Act repealed by subsection (a) or (b) shall have no force or effect.\n**(2) Prohibition**\nNotwithstanding any other provision of law, the Consumer Product Safety Commission may not promulgate any regulation that requires\u2014\n**(A)**\na flame mitigation device in a portable fuel container; or\n**(B)**\na portable gasoline container to conform to child-resistance requirements.",
      "versionDate": "2025-02-13",
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
        "actionDate": "2025-10-08",
        "text": "Read twice and referred to the Committee on Commerce, Science, and Transportation."
      },
      "number": "2992",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Gas Can Freedom Act of 2025",
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
        "name": "Commerce",
        "updateDate": "2025-05-09T18:15:33Z"
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
      "date": "2025-02-13",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1345ih.xml"
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
      "title": "Gas Can Freedom Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-07-30T12:52:37Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Gas Can Freedom Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-15T03:23:20Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To repeal the Portable Fuel Container Safety Act of 2020 and the Children's Gasoline Burn Prevention Act, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-15T03:18:28Z"
    }
  ]
}
```
