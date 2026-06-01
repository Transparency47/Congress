# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/5252?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/5252
- Title: HOPE Act
- Congress: 119
- Bill type: HR
- Bill number: 5252
- Origin chamber: House
- Introduced date: 2025-09-10
- Update date: 2025-11-21T12:04:01Z
- Update date including text: 2025-11-21T12:04:01Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-09-10: Introduced in House
- 2025-09-10 - IntroReferral: Introduced in House
- 2025-09-10 - IntroReferral: Introduced in House
- 2025-09-10 - IntroReferral: Referred to the House Committee on Energy and Commerce.
- Latest action: 2025-09-10: Introduced in House

## Actions

- 2025-09-10 - IntroReferral: Introduced in House
- 2025-09-10 - IntroReferral: Introduced in House
- 2025-09-10 - IntroReferral: Referred to the House Committee on Energy and Commerce.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-09-10",
    "latestAction": {
      "actionDate": "2025-09-10",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/5252",
    "number": "5252",
    "originChamber": "House",
    "policyArea": {
      "name": "Health"
    },
    "sponsors": [
      {
        "bioguideId": "A000380",
        "district": "1",
        "firstName": "Gabe",
        "fullName": "Rep. Amo, Gabe [D-RI-1]",
        "lastName": "Amo",
        "party": "D",
        "state": "RI"
      }
    ],
    "title": "HOPE Act",
    "type": "HR",
    "updateDate": "2025-11-21T12:04:01Z",
    "updateDateIncludingText": "2025-11-21T12:04:01Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-09-10",
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
      "actionDate": "2025-09-10",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-09-10",
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
          "date": "2025-09-10T14:03:30Z",
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
      "bioguideId": "M001240",
      "district": "6",
      "firstName": "Addison",
      "fullName": "Rep. McDowell, Addison P. [R-NC-6]",
      "isOriginalCosponsor": "True",
      "lastName": "McDowell",
      "middleName": "P.",
      "party": "R",
      "sponsorshipDate": "2025-09-10",
      "state": "NC"
    },
    {
      "bioguideId": "T000469",
      "district": "20",
      "firstName": "Paul",
      "fullName": "Rep. Tonko, Paul [D-NY-20]",
      "isOriginalCosponsor": "True",
      "lastName": "Tonko",
      "party": "D",
      "sponsorshipDate": "2025-09-10",
      "state": "NY"
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
      "sponsorshipDate": "2025-09-10",
      "state": "DC"
    },
    {
      "bioguideId": "T000488",
      "district": "13",
      "firstName": "Shri",
      "fullName": "Rep. Thanedar, Shri [D-MI-13]",
      "isOriginalCosponsor": "True",
      "lastName": "Thanedar",
      "party": "D",
      "sponsorshipDate": "2025-09-10",
      "state": "MI"
    },
    {
      "bioguideId": "P000620",
      "district": "7",
      "firstName": "Brittany",
      "fullName": "Rep. Pettersen, Brittany [D-CO-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Pettersen",
      "party": "D",
      "sponsorshipDate": "2025-11-04",
      "state": "CO"
    },
    {
      "bioguideId": "C001119",
      "district": "2",
      "firstName": "Angie",
      "fullName": "Rep. Craig, Angie [D-MN-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Craig",
      "party": "D",
      "sponsorshipDate": "2025-11-17",
      "state": "MN"
    },
    {
      "bioguideId": "M001223",
      "district": "2",
      "firstName": "Seth",
      "fullName": "Rep. Magaziner, Seth [D-RI-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Magaziner",
      "party": "D",
      "sponsorshipDate": "2025-11-20",
      "state": "RI"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr5252ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 5252\nIN THE HOUSE OF REPRESENTATIVES\nSeptember 10, 2025 Mr. Amo (for himself, Mr. McDowell , Mr. Tonko , Ms. Norton , and Mr. Thanedar ) introduced the following bill; which was referred to the Committee on Energy and Commerce\nA BILL\nTo amend the 21st Century Cares Act to clarify that certain grants for State and Tribal response to opioid use disorders may be used for certain activities related to public access opioid overdose reversal kits, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Having Overdose Protection Equipment Act or the HOPE Act .\n#### 2. Use of certain State and Tribal grant funds for public access opioid overdose reversal kits\nSection 1003 of the 21st Century Cures Act ( 42 U.S.C. 290ee\u20133a ) is amended\u2014\n**(1)**\nin subsection (b)(4)(A), by inserting and other activities related to acquiring, making available, and maintaining public access opioid overdose reversal kits after primary prevention activities ; and\n**(2)**\nin subsection (h)\u2014\n**(A)**\nby redesignating paragraphs (2) and (4) as paragraphs (4) and (5), respectively;\n**(B)**\nby transferring paragraph (4), as so redesignated, so as to appear after paragraph (3); and\n**(C)**\nby inserting after paragraph (1) the following:\n(2) Public access opioid overdose reversal kit The term public access opioid overdose reversal kit means a kit that includes\u2014 (A) opioid overdose reversal medication; and (B) instructions on how to administer such medication. .",
      "versionDate": "2025-09-10",
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
        "name": "Health",
        "updateDate": "2025-09-24T14:05:07Z"
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
      "date": "2025-09-10",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr5252ih.xml"
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
      "title": "HOPE Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-09-17T11:23:14Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "HOPE Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-09-17T11:23:14Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Having Overdose Protection Equipment Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-09-17T11:23:14Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the 21st Century Cares Act to clarify that certain grants for State and Tribal response to opioid use disorders may be used for certain activities related to public access opioid overdose reversal kits, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-09-17T11:18:13Z"
    }
  ]
}
```
