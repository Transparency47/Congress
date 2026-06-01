# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/8280?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/8280
- Title: SEPTIC Act
- Congress: 119
- Bill type: HR
- Bill number: 8280
- Origin chamber: House
- Introduced date: 2026-04-14
- Update date: 2026-04-27T22:26:21Z
- Update date including text: 2026-04-27T22:26:21Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2026-04-14: Introduced in House
- 2026-04-14 - IntroReferral: Introduced in House
- 2026-04-14 - IntroReferral: Introduced in House
- 2026-04-14 - IntroReferral: Referred to the House Committee on Ways and Means.
- Latest action: 2026-04-14: Introduced in House

## Actions

- 2026-04-14 - IntroReferral: Introduced in House
- 2026-04-14 - IntroReferral: Introduced in House
- 2026-04-14 - IntroReferral: Referred to the House Committee on Ways and Means.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-04-14",
    "latestAction": {
      "actionDate": "2026-04-14",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/8280",
    "number": "8280",
    "originChamber": "House",
    "policyArea": {
      "name": "Taxation"
    },
    "sponsors": [
      {
        "bioguideId": "S001201",
        "district": "3",
        "firstName": "Thomas",
        "fullName": "Rep. Suozzi, Thomas R. [D-NY-3]",
        "lastName": "Suozzi",
        "party": "D",
        "state": "NY"
      }
    ],
    "title": "SEPTIC Act",
    "type": "HR",
    "updateDate": "2026-04-27T22:26:21Z",
    "updateDateIncludingText": "2026-04-27T22:26:21Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2026-04-14",
      "committees": {
        "item": {
          "name": "Ways and Means Committee",
          "systemCode": "hswm00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Ways and Means.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2026-04-14",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-04-14",
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
          "date": "2026-04-14T16:04:30Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Ways and Means Committee",
      "systemCode": "hswm00",
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
      "bioguideId": "B001257",
      "district": "12",
      "firstName": "Gus",
      "fullName": "Rep. Bilirakis, Gus M. [R-FL-12]",
      "isOriginalCosponsor": "True",
      "lastName": "Bilirakis",
      "middleName": "M.",
      "party": "R",
      "sponsorshipDate": "2026-04-14",
      "state": "FL"
    },
    {
      "bioguideId": "B001314",
      "district": "4",
      "firstName": "Aaron",
      "fullName": "Rep. Bean, Aaron [R-FL-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Bean",
      "party": "R",
      "sponsorshipDate": "2026-04-14",
      "state": "FL"
    },
    {
      "bioguideId": "S001214",
      "district": "17",
      "firstName": "W.",
      "fullName": "Rep. Steube, W. Gregory [R-FL-17]",
      "isOriginalCosponsor": "True",
      "lastName": "Steube",
      "middleName": "Gregory",
      "party": "R",
      "sponsorshipDate": "2026-04-14",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr8280ih.xml",
      "text": "I\n119th CONGRESS\n2d Session\nH. R. 8280\nIN THE HOUSE OF REPRESENTATIVES\nApril 14, 2026 Mr. Suozzi (for himself, Mr. Bilirakis , Mr. Bean of Florida , and Mr. Steube ) introduced the following bill; which was referred to the Committee on Ways and Means\nA BILL\nTo amend the Internal Revenue Code of 1986 to provide an exclusion from gross income for certain wastewater management subsidies.\n#### 1. Short title\nThis Act may be cited as the Septic Exclusion for Property owners through Tax-free Infrastructure Compensation Act or the SEPTIC Act .\n#### 2. Modifications to income exclusion for certain wastewater management subsidies\n##### (a) In general\nSection 136(a) of the Internal Revenue Code of 1986 is amended\u2014\n**(1)**\nby striking any subsidy provided and inserting\nany subsidy\u2014 (1) provided ,\n**(2)**\nby striking the period at the end and inserting , or , and\n**(3)**\nby adding at the end the following new paragraph:\n(2) provided (directly or indirectly) by a State or local government to a resident of such State or locality for the purchase or installation of any wastewater management measure, but only if such measure is with respect to the taxpayer\u2019s residence. .\n##### (b) Definition of wastewater management measure\nSection 136(c) of such Code is amended\u2014\n**(1)**\nby striking Energy conservation measure in the heading thereof and inserting Definitions ,\n**(2)**\nby striking In general in the heading of paragraph (1) and inserting Energy conservation measure , and\n**(3)**\nby redesignating paragraph (2) as paragraph (3) and by inserting after paragraph (1) the following:\n(2) Wastewater management measure For purposes of this section, the term wastewater management measure means any installation or modification of property primarily designed to manage wastewater (including septic tanks and cesspools) with respect to one or more dwelling units. .\n##### (c) Clerical amendments\n**(1)**\nThe heading for section 136 of such Code is amended\u2014\n**(A)**\nby inserting and wastewater after energy , and\n**(B)**\nby striking provided by public utilities .\n**(2)**\nThe item relating to section 136 in the table of sections of part III of subchapter B of chapter 1 of such Code is amended\u2014\n**(A)**\nby inserting and wastewater after energy , and\n**(B)**\nby striking provided by public utilities .\n##### (d) Effective date\nThe amendments made by this section shall apply to amounts received after the date of the enactment of this Act, in taxable years ending after such date.",
      "versionDate": "2026-04-14",
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
        "name": "Taxation",
        "updateDate": "2026-04-27T22:26:21Z"
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
      "date": "2026-04-14",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr8280ih.xml"
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
      "title": "SEPTIC Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-04-21T06:23:28Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "SEPTIC Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-04-21T06:23:27Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Septic Exclusion for Property owners through Tax-free Infrastructure Compensation Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-04-21T06:23:27Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Internal Revenue Code of 1986 to provide an exclusion from gross income for certain wastewater management subsidies.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-04-21T06:18:48Z"
    }
  ]
}
```
