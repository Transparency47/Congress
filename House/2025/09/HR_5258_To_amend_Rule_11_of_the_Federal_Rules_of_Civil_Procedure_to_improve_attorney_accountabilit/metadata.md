# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/5258?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/5258
- Title: Lawsuit Abuse Reduction Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 5258
- Origin chamber: House
- Introduced date: 2025-09-10
- Update date: 2026-05-14T08:08:12Z
- Update date including text: 2026-05-14T08:08:12Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-09-10: Introduced in House
- 2025-09-10 - IntroReferral: Introduced in House
- 2025-09-10 - IntroReferral: Introduced in House
- 2025-09-10 - IntroReferral: Referred to the House Committee on the Judiciary.
- Latest action: 2025-09-10: Introduced in House

## Actions

- 2025-09-10 - IntroReferral: Introduced in House
- 2025-09-10 - IntroReferral: Introduced in House
- 2025-09-10 - IntroReferral: Referred to the House Committee on the Judiciary.

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
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/5258",
    "number": "5258",
    "originChamber": "House",
    "policyArea": {
      "name": "Law"
    },
    "sponsors": [
      {
        "bioguideId": "C001129",
        "district": "10",
        "firstName": "Mike",
        "fullName": "Rep. Collins, Mike [R-GA-10]",
        "lastName": "Collins",
        "party": "R",
        "state": "GA"
      }
    ],
    "title": "Lawsuit Abuse Reduction Act of 2025",
    "type": "HR",
    "updateDate": "2026-05-14T08:08:12Z",
    "updateDateIncludingText": "2026-05-14T08:08:12Z"
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
          "name": "Judiciary Committee",
          "systemCode": "hsju00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on the Judiciary.",
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
          "date": "2025-09-10T14:02:45Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Judiciary Committee",
      "systemCode": "hsju00",
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
      "bioguideId": "G000603",
      "district": "26",
      "firstName": "Brandon",
      "fullName": "Rep. Gill, Brandon [R-TX-26]",
      "isOriginalCosponsor": "True",
      "lastName": "Gill",
      "party": "R",
      "sponsorshipDate": "2025-09-10",
      "state": "TX"
    },
    {
      "bioguideId": "T000165",
      "district": "7",
      "firstName": "Thomas",
      "fullName": "Rep. Tiffany, Thomas P. [R-WI-7]",
      "isOriginalCosponsor": "True",
      "lastName": "Tiffany",
      "middleName": "P.",
      "party": "R",
      "sponsorshipDate": "2025-09-10",
      "state": "WI"
    },
    {
      "bioguideId": "H001096",
      "district": "0",
      "firstName": "Harriet",
      "fullName": "Rep. Hageman, Harriet M. [R-WY-At Large]",
      "isOriginalCosponsor": "True",
      "lastName": "Hageman",
      "middleName": "M.",
      "party": "R",
      "sponsorshipDate": "2025-09-10",
      "state": "WY"
    },
    {
      "bioguideId": "W000829",
      "district": "8",
      "firstName": "Tony",
      "fullName": "Rep. Wied, Tony [R-WI-8]",
      "isOriginalCosponsor": "False",
      "lastName": "Wied",
      "party": "R",
      "sponsorshipDate": "2026-04-22",
      "state": "WI"
    },
    {
      "bioguideId": "G000589",
      "district": "5",
      "firstName": "Lance",
      "fullName": "Rep. Gooden, Lance [R-TX-5]",
      "isOriginalCosponsor": "False",
      "lastName": "Gooden",
      "party": "R",
      "sponsorshipDate": "2026-04-27",
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
      "sponsorshipDate": "2026-05-13",
      "state": "NC"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr5258ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 5258\nIN THE HOUSE OF REPRESENTATIVES\nSeptember 10, 2025 Mr. Collins (for himself, Mr. Gill of Texas , Mr. Tiffany , and Ms. Hageman ) introduced the following bill; which was referred to the Committee on the Judiciary\nA BILL\nTo amend Rule 11 of the Federal Rules of Civil Procedure to improve attorney accountability, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Lawsuit Abuse Reduction Act of 2025 .\n#### 2. Attorney accountability\n##### (a) Sanctions under rule 11\nRule 11(c) of the Federal Rules of Civil Procedure is amended\u2014\n**(1)**\nin paragraph (1), by striking may and inserting shall ;\n**(2)**\nin paragraph (2), by striking Rule 5 and all that follows through motion. and inserting Rule 5. ; and\n**(3)**\nin paragraph (4), by striking situated and all that follows through the end of the paragraph and inserting situated, and to compensate the parties that were injured by such conduct. Subject to the limitations in paragraph (5), the sanction shall consist of an order to pay to the party or parties the amount of the reasonable expenses incurred as a direct result of the violation, including reasonable attorneys\u2019 fees and costs. The court may also impose additional appropriate sanctions, such as striking the pleadings, dismissing the suit, or other directives of a non-monetary nature, or, if warranted for effective deterrence, an order directing payment of a penalty into the court. .\n##### (b) Rule of construction\nNothing in this Act or an amendment made by this Act shall be construed to bar or impede the assertion or development of new claims, defenses, or remedies under Federal, State, or local laws, including civil rights laws, or under the Constitution of the United States.",
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
        "name": "Law",
        "updateDate": "2025-09-24T14:37:29Z"
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
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr5258ih.xml"
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
      "title": "Lawsuit Abuse Reduction Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-09-18T04:23:18Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Lawsuit Abuse Reduction Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-09-18T04:23:16Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend Rule 11 of the Federal Rules of Civil Procedure to improve attorney accountability, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-09-18T04:18:30Z"
    }
  ]
}
```
