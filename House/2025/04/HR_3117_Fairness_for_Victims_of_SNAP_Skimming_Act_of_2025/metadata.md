# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/3117?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/3117
- Title: Fairness for Victims of SNAP Skimming Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 3117
- Origin chamber: House
- Introduced date: 2025-04-30
- Update date: 2026-01-13T09:05:47Z
- Update date including text: 2026-01-13T09:05:47Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-04-30: Introduced in House
- 2025-04-30 - IntroReferral: Introduced in House
- 2025-04-30 - IntroReferral: Introduced in House
- 2025-04-30 - IntroReferral: Referred to the House Committee on Agriculture.
- Latest action: 2025-04-30: Introduced in House

## Actions

- 2025-04-30 - IntroReferral: Introduced in House
- 2025-04-30 - IntroReferral: Introduced in House
- 2025-04-30 - IntroReferral: Referred to the House Committee on Agriculture.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-04-30",
    "latestAction": {
      "actionDate": "2025-04-30",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/3117",
    "number": "3117",
    "originChamber": "House",
    "policyArea": {
      "name": "Agriculture and Food"
    },
    "sponsors": [
      {
        "bioguideId": "M001188",
        "district": "6",
        "firstName": "Grace",
        "fullName": "Rep. Meng, Grace [D-NY-6]",
        "lastName": "Meng",
        "party": "D",
        "state": "NY"
      }
    ],
    "title": "Fairness for Victims of SNAP Skimming Act of 2025",
    "type": "HR",
    "updateDate": "2026-01-13T09:05:47Z",
    "updateDateIncludingText": "2026-01-13T09:05:47Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-04-30",
      "committees": {
        "item": {
          "name": "Agriculture Committee",
          "systemCode": "hsag00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Agriculture.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-04-30",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-04-30",
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
          "date": "2025-04-30T14:04:25Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Agriculture Committee",
      "systemCode": "hsag00",
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
      "bioguideId": "L000599",
      "district": "17",
      "firstName": "Michael",
      "fullName": "Rep. Lawler, Michael [R-NY-17]",
      "isOriginalCosponsor": "True",
      "lastName": "Lawler",
      "party": "R",
      "sponsorshipDate": "2025-04-30",
      "state": "NY"
    },
    {
      "bioguideId": "C001072",
      "district": "7",
      "firstName": "Andr\u00e9",
      "fullName": "Rep. Carson, Andr\u00e9 [D-IN-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Carson",
      "party": "D",
      "sponsorshipDate": "2025-05-07",
      "state": "IN"
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
      "sponsorshipDate": "2025-05-07",
      "state": "PA"
    },
    {
      "bioguideId": "G000553",
      "district": "9",
      "firstName": "Al",
      "fullName": "Rep. Green, Al [D-TX-9]",
      "isOriginalCosponsor": "False",
      "lastName": "Green",
      "party": "D",
      "sponsorshipDate": "2025-05-07",
      "state": "TX"
    },
    {
      "bioguideId": "V000081",
      "district": "7",
      "firstName": "Nydia",
      "fullName": "Rep. Vel\u00e1zquez, Nydia M. [D-NY-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Vel\u00e1zquez",
      "middleName": "M.",
      "party": "D",
      "sponsorshipDate": "2025-06-03",
      "state": "NY"
    },
    {
      "bioguideId": "T000486",
      "district": "15",
      "firstName": "Ritchie",
      "fullName": "Rep. Torres, Ritchie [D-NY-15]",
      "isOriginalCosponsor": "False",
      "lastName": "Torres",
      "party": "D",
      "sponsorshipDate": "2025-06-12",
      "state": "NY"
    },
    {
      "bioguideId": "M001238",
      "district": "0",
      "firstName": "Sarah",
      "fullName": "Rep. McBride, Sarah [D-DE-At Large]",
      "isOriginalCosponsor": "False",
      "lastName": "McBride",
      "party": "D",
      "sponsorshipDate": "2025-08-08",
      "state": "DE"
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
      "sponsorshipDate": "2025-08-12",
      "state": "PA"
    },
    {
      "bioguideId": "B001327",
      "district": "8",
      "firstName": "Robert",
      "fullName": "Rep. Bresnahan, Robert P. [R-PA-8]",
      "isOriginalCosponsor": "False",
      "lastName": "Bresnahan",
      "middleName": "P.",
      "party": "R",
      "sponsorshipDate": "2025-12-18",
      "state": "PA"
    },
    {
      "bioguideId": "S001201",
      "district": "3",
      "firstName": "Thomas",
      "fullName": "Rep. Suozzi, Thomas R. [D-NY-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Suozzi",
      "middleName": "R.",
      "party": "D",
      "sponsorshipDate": "2026-01-12",
      "state": "NY"
    },
    {
      "bioguideId": "D000629",
      "district": "3",
      "firstName": "Sharice",
      "fullName": "Rep. Davids, Sharice [D-KS-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Davids",
      "party": "D",
      "sponsorshipDate": "2026-01-12",
      "state": "KS"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr3117ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 3117\nIN THE HOUSE OF REPRESENTATIVES\nApril 30, 2025 Ms. Meng (for herself and Mr. Lawler ) introduced the following bill; which was referred to the Committee on Agriculture\nA BILL\nTo amend the Consolidated Appropriations Act, 2023, to expand the replacement of stolen EBT benefits under the supplemental nutrition assistance program.\n#### 1. Short title\nThis Act may be cited as the Fairness for Victims of SNAP Skimming Act of 2025 .\n#### 2. Replacement of stolen EBT benefits\nSection 501(b)(2) of division HH of the Consolidated Appropriations Act, 2023 ( 7 U.S.C. 2016a(b)(2) ) is amended\u2014\n**(1)**\nby striking subparagraph (A) and inserting the following:\n(A) shall be equal to the amount of benefits stolen from the household; and ;\n**(2)**\nin subparagraph (B), by striking and at the end; and\n**(3)**\nby striking subparagraph (C).",
      "versionDate": "2025-04-30",
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
        "actionDate": "2025-04-30",
        "text": "Read twice and referred to the Committee on Agriculture, Nutrition, and Forestry."
      },
      "number": "1540",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Fairness for Victims of SNAP Skimming Act of 2025",
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
        "name": "Agriculture and Food",
        "updateDate": "2025-06-30T19:02:30Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-04-30",
    "originChamber": "House",
    "payload": {
      "dublinCore": {
        "contributor": "Congressional Research Service, Library of Congress",
        "description": "This file contains bill summaries for federal legislation. A bill summary describes the most significant provisions of a piece of legislation and details the effects the legislative text may have on current law and federal programs. Bill summaries are authored by the Congressional Research Service (CRS) of the Library of Congress. As stated in Public Law 91-510 (2 USC 166 (d)(6)), one of the duties of CRS is \"to prepare summaries and digests of bills and resolutions of a public general nature introduced in the Senate or House of Representatives\". For more information, refer to the User Guide that accompanies this file.",
        "format": "text/xml",
        "language": "EN",
        "rights": "Pursuant to Title 17 Section 105 of the United States Code, this file is not subject to copyright protection and is in the public domain."
      },
      "item": {
        "@attributes": {
          "congress": "119",
          "measure-id": "id119hr3117",
          "measure-number": "3117",
          "measure-type": "hr",
          "orig-publish-date": "2025-04-30",
          "originChamber": "HOUSE",
          "update-date": "2025-09-23"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr3117v00",
            "update-date": "2025-09-23"
          },
          "action-date": "2025-04-30",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Fairness for Victims of SNAP Skimming Act of 2025</strong></p><p>This bill requires the Supplemental Nutrition Assistance Program (SNAP) to provide for the replacement of the full amount of a household's stolen benefits.</p><p>Specifically, using funds provided by the Department of Agriculture, a state agency must provide a household with replacement SNAP benefits equal to the amount of benefits\u00a0stolen through card skimming, card cloning, or similar fraudulent methods. This requirement applies if the state agency determines that the benefits were stolen and meets certain requirements.\u00a0</p><p>Under current law, a state agency may only replace SNAP benefits that were stolen between the period beginning on October 1, 2022, and ending on December 20, 2024. Further,\u00a0the replacement amount is limited to the lesser of the amount of (1) the benefits stolen, or (2) two months of the\u00a0household's monthly allotment immediately prior to the date on which the benefits were stolen. Thus, this bill permanently extends the provision and provides for the replacement of the full amount of the benefits stolen.</p>"
        },
        "title": "Fairness for Victims of SNAP Skimming Act of 2025"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr3117.xml",
    "summary": {
      "actionDate": "2025-04-30",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Fairness for Victims of SNAP Skimming Act of 2025</strong></p><p>This bill requires the Supplemental Nutrition Assistance Program (SNAP) to provide for the replacement of the full amount of a household's stolen benefits.</p><p>Specifically, using funds provided by the Department of Agriculture, a state agency must provide a household with replacement SNAP benefits equal to the amount of benefits\u00a0stolen through card skimming, card cloning, or similar fraudulent methods. This requirement applies if the state agency determines that the benefits were stolen and meets certain requirements.\u00a0</p><p>Under current law, a state agency may only replace SNAP benefits that were stolen between the period beginning on October 1, 2022, and ending on December 20, 2024. Further,\u00a0the replacement amount is limited to the lesser of the amount of (1) the benefits stolen, or (2) two months of the\u00a0household's monthly allotment immediately prior to the date on which the benefits were stolen. Thus, this bill permanently extends the provision and provides for the replacement of the full amount of the benefits stolen.</p>",
      "updateDate": "2025-09-23",
      "versionCode": "id119hr3117"
    },
    "title": "Fairness for Victims of SNAP Skimming Act of 2025"
  },
  "summaries": [
    {
      "actionDate": "2025-04-30",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Fairness for Victims of SNAP Skimming Act of 2025</strong></p><p>This bill requires the Supplemental Nutrition Assistance Program (SNAP) to provide for the replacement of the full amount of a household's stolen benefits.</p><p>Specifically, using funds provided by the Department of Agriculture, a state agency must provide a household with replacement SNAP benefits equal to the amount of benefits\u00a0stolen through card skimming, card cloning, or similar fraudulent methods. This requirement applies if the state agency determines that the benefits were stolen and meets certain requirements.\u00a0</p><p>Under current law, a state agency may only replace SNAP benefits that were stolen between the period beginning on October 1, 2022, and ending on December 20, 2024. Further,\u00a0the replacement amount is limited to the lesser of the amount of (1) the benefits stolen, or (2) two months of the\u00a0household's monthly allotment immediately prior to the date on which the benefits were stolen. Thus, this bill permanently extends the provision and provides for the replacement of the full amount of the benefits stolen.</p>",
      "updateDate": "2025-09-23",
      "versionCode": "id119hr3117"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-04-30",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr3117ih.xml"
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
      "title": "Fairness for Victims of SNAP Skimming Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-06-30T05:23:19Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Fairness for Victims of SNAP Skimming Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-06-30T05:23:19Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Consolidated Appropriations Act, 2023, to expand the replacement of stolen EBT benefits under the supplemental nutrition assistance program.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-06-30T05:18:19Z"
    }
  ]
}
```
