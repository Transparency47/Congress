# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/7154?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/7154
- Title: Streamlining Small Business Contracts Act of 2026
- Congress: 119
- Bill type: HR
- Bill number: 7154
- Origin chamber: House
- Introduced date: 2026-01-20
- Update date: 2026-04-16T08:06:54Z
- Update date including text: 2026-04-16T08:06:54Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2026-01-20: Introduced in House
- 2026-01-20 - IntroReferral: Introduced in House
- 2026-01-20 - IntroReferral: Introduced in House
- 2026-01-20 - IntroReferral: Referred to the House Committee on Small Business.
- Latest action: 2026-01-20: Introduced in House

## Actions

- 2026-01-20 - IntroReferral: Introduced in House
- 2026-01-20 - IntroReferral: Introduced in House
- 2026-01-20 - IntroReferral: Referred to the House Committee on Small Business.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-01-20",
    "latestAction": {
      "actionDate": "2026-01-20",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/7154",
    "number": "7154",
    "originChamber": "House",
    "policyArea": {
      "name": "Commerce"
    },
    "sponsors": [
      {
        "bioguideId": "C001123",
        "district": "31",
        "firstName": "Gilbert",
        "fullName": "Rep. Cisneros, Gilbert Ray [D-CA-31]",
        "lastName": "Cisneros",
        "party": "D",
        "state": "CA"
      }
    ],
    "title": "Streamlining Small Business Contracts Act of 2026",
    "type": "HR",
    "updateDate": "2026-04-16T08:06:54Z",
    "updateDateIncludingText": "2026-04-16T08:06:54Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2026-01-20",
      "committees": {
        "item": {
          "name": "Small Business Committee",
          "systemCode": "hssm00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Small Business.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2026-01-20",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-01-20",
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
          "date": "2026-01-20T17:02:05Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Small Business Committee",
      "systemCode": "hssm00",
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
      "bioguideId": "V000081",
      "district": "7",
      "firstName": "Nydia",
      "fullName": "Rep. Vel\u00e1zquez, Nydia M. [D-NY-7]",
      "isOriginalCosponsor": "True",
      "lastName": "Vel\u00e1zquez",
      "middleName": "M.",
      "party": "D",
      "sponsorshipDate": "2026-01-20",
      "state": "NY"
    },
    {
      "bioguideId": "V000135",
      "district": "3",
      "firstName": "Derrick",
      "fullName": "Rep. Van Orden, Derrick [R-WI-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Van Orden",
      "party": "R",
      "sponsorshipDate": "2026-02-20",
      "state": "WI"
    },
    {
      "bioguideId": "H001101",
      "district": "10",
      "firstName": "Pat",
      "fullName": "Rep. Harrigan, Pat [R-NC-10]",
      "isOriginalCosponsor": "False",
      "lastName": "Harrigan",
      "party": "R",
      "sponsorshipDate": "2026-04-06",
      "state": "NC"
    },
    {
      "bioguideId": "M001234",
      "district": "3",
      "firstName": "Kelly",
      "fullName": "Rep. Morrison, Kelly [D-MN-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Morrison",
      "party": "D",
      "sponsorshipDate": "2026-04-15",
      "state": "MN"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7154ih.xml",
      "text": "I\n119th CONGRESS\n2d Session\nH. R. 7154\nIN THE HOUSE OF REPRESENTATIVES\nJanuary 20, 2026 Mr. Cisneros (for himself and Ms. Vel\u00e1zquez ) introduced the following bill; which was referred to the Committee on Small Business\nA BILL\nTo amend the Small Business Act to modify the dollar threshold for certain sole source contracts, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Streamlining Small Business Contracts Act of 2026 .\n#### 2. Amendments to sole source contracting authority for certain small business concerns\nThe Small Business Act ( 15 U.S.C. 631 et seq. ) is amended\u2014\n**(1)**\nin section 8(a)(1)(D)(i)(II), by striking $7,000,000 and all that follows and inserting $10,000,000. ;\n**(2)**\nin section 8(m)\u2014\n**(A)**\nin paragraph (7)(B), by striking will not exceed and all that follows and inserting will not exceed $10,000,000; and ; and\n**(B)**\nin paragraph (8)(B), by striking will not exceed and all that follows and inserting will not exceed $10,000,000; and ;\n**(3)**\nin section 31(c)(2)(A)(ii) of the Small Business Act ( 15 U.S.C. 657a(c)(2)(A)(ii) ), by striking will not exceed and all that follows and inserting will not exceed $10,000,000; and ; and\n**(4)**\nin section 36(c)(2) of the Small Business Act ( 15 U.S.C. 657f(c)(2) ), by striking will not exceed and all that follows and inserting will not exceed $10,000,000; and .",
      "versionDate": "2026-01-20",
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
        "name": "Commerce",
        "updateDate": "2026-02-18T13:53:06Z"
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
      "date": "2026-01-20",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7154ih.xml"
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
      "title": "Streamlining Small Business Contracts Act of 2026",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-02-12T04:08:24Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Streamlining Small Business Contracts Act of 2026",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-02-12T04:08:23Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Small Business Act to modify the dollar threshold for certain sole source contracts, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-02-12T04:03:28Z"
    }
  ]
}
```
