# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/1540?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/1540
- Title: Fairness for Victims of SNAP Skimming Act of 2025
- Congress: 119
- Bill type: S
- Bill number: 1540
- Origin chamber: Senate
- Introduced date: 2025-04-30
- Update date: 2025-12-05T22:05:00Z
- Update date including text: 2025-12-05T22:05:00Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-04-30: Introduced in Senate
- 2025-04-30 - IntroReferral: Introduced in Senate
- 2025-04-30 - IntroReferral: Read twice and referred to the Committee on Agriculture, Nutrition, and Forestry.
- Latest action: 2025-04-30: Introduced in Senate

## Actions

- 2025-04-30 - IntroReferral: Introduced in Senate
- 2025-04-30 - IntroReferral: Read twice and referred to the Committee on Agriculture, Nutrition, and Forestry.

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
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/1540",
    "number": "1540",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Agriculture and Food"
    },
    "sponsors": [
      {
        "bioguideId": "F000479",
        "district": "",
        "firstName": "John",
        "fullName": "Sen. Fetterman, John [D-PA]",
        "lastName": "Fetterman",
        "party": "D",
        "state": "PA"
      }
    ],
    "title": "Fairness for Victims of SNAP Skimming Act of 2025",
    "type": "S",
    "updateDate": "2025-12-05T22:05:00Z",
    "updateDateIncludingText": "2025-12-05T22:05:00Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-04-30",
      "committees": {
        "item": {
          "name": "Agriculture, Nutrition, and Forestry Committee",
          "systemCode": "ssaf00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Agriculture, Nutrition, and Forestry.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-04-30",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in Senate",
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
          "date": "2025-04-30T19:59:53Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Agriculture, Nutrition, and Forestry Committee",
      "systemCode": "ssaf00",
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
      "bioguideId": "G000555",
      "firstName": "Kirsten",
      "fullName": "Sen. Gillibrand, Kirsten E. [D-NY]",
      "isOriginalCosponsor": "True",
      "lastName": "Gillibrand",
      "middleName": "E.",
      "party": "D",
      "sponsorshipDate": "2025-04-30",
      "state": "NY"
    },
    {
      "bioguideId": "B001277",
      "firstName": "Richard",
      "fullName": "Sen. Blumenthal, Richard [D-CT]",
      "isOriginalCosponsor": "True",
      "lastName": "Blumenthal",
      "party": "D",
      "sponsorshipDate": "2025-04-30",
      "state": "CT"
    },
    {
      "bioguideId": "A000382",
      "firstName": "Angela",
      "fullName": "Sen. Alsobrooks, Angela D. [D-MD]",
      "isOriginalCosponsor": "True",
      "lastName": "Alsobrooks",
      "party": "D",
      "sponsorshipDate": "2025-04-30",
      "state": "MD"
    },
    {
      "bioguideId": "W000779",
      "firstName": "Ron",
      "fullName": "Sen. Wyden, Ron [D-OR]",
      "isOriginalCosponsor": "True",
      "lastName": "Wyden",
      "party": "D",
      "sponsorshipDate": "2025-04-30",
      "state": "OR"
    },
    {
      "bioguideId": "W000800",
      "firstName": "Peter",
      "fullName": "Sen. Welch, Peter [D-VT]",
      "isOriginalCosponsor": "True",
      "lastName": "Welch",
      "party": "D",
      "sponsorshipDate": "2025-04-30",
      "state": "VT"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1540is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 1540\nIN THE SENATE OF THE UNITED STATES\nApril 30, 2025 Mr. Fetterman (for himself, Mrs. Gillibrand , Mr. Blumenthal , Ms. Alsobrooks , Mr. Wyden , and Mr. Welch ) introduced the following bill; which was read twice and referred to the Committee on Agriculture, Nutrition, and Forestry\nA BILL\nTo amend the Consolidated Appropriations Act, 2023, to expand the replacement of stolen EBT benefits under the supplemental nutrition assistance program.\n#### 1. Short title\nThis Act may be cited as the Fairness for Victims of SNAP Skimming Act of 2025 .\n#### 2. Replacement of stolen EBT benefits\nSection 501(b)(2) of division HH of the Consolidated Appropriations Act, 2023 ( 7 U.S.C. 2016a(b)(2) ) is amended\u2014\n**(1)**\nby striking subparagraph (A) and inserting the following:\n(A) shall be equal to the amount of benefits stolen from the household; and ;\n**(2)**\nin subparagraph (B), by striking and at the end; and\n**(3)**\nby striking subparagraph (C).",
      "versionDate": "2025-04-30",
      "versionType": "Introduced in Senate"
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
        "text": "Referred to the House Committee on Agriculture."
      },
      "number": "3117",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Fairness for Victims of SNAP Skimming Act of 2025",
      "type": "HR"
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
        "updateDate": "2025-05-28T15:09:21Z"
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
    "originChamber": "Senate",
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
          "measure-id": "id119s1540",
          "measure-number": "1540",
          "measure-type": "s",
          "orig-publish-date": "2025-04-30",
          "originChamber": "SENATE",
          "update-date": "2025-09-23"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "SENATE",
            "summary-id": "id119s1540v00",
            "update-date": "2025-09-23"
          },
          "action-date": "2025-04-30",
          "action-desc": "Introduced in Senate",
          "summary-text": "<p><strong>Fairness for Victims of SNAP Skimming Act of 2025</strong></p><p>This bill requires the Supplemental Nutrition Assistance Program (SNAP) to provide for the replacement of the full amount of a household's stolen benefits.</p><p>Specifically, using funds provided by the Department of Agriculture, a state agency must provide a household with replacement SNAP benefits equal to the amount of benefits\u00a0stolen through card skimming, card cloning, or similar fraudulent methods. This requirement applies if the state agency determines that the benefits were stolen and meets certain requirements.\u00a0</p><p>Under current law, a state agency may only replace SNAP benefits that were stolen between the period beginning on October 1, 2022, and ending on December 20, 2024. Further,\u00a0the replacement amount is limited to the lesser of the amount of (1) the benefits stolen, or (2) two months of the\u00a0household's monthly allotment immediately prior to the date on which the benefits were stolen. Thus, this bill permanently extends the provision and provides for the replacement of the full amount of the benefits stolen.</p>"
        },
        "title": "Fairness for Victims of SNAP Skimming Act of 2025"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/s/BILLSUM-119s1540.xml",
    "summary": {
      "actionDate": "2025-04-30",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Fairness for Victims of SNAP Skimming Act of 2025</strong></p><p>This bill requires the Supplemental Nutrition Assistance Program (SNAP) to provide for the replacement of the full amount of a household's stolen benefits.</p><p>Specifically, using funds provided by the Department of Agriculture, a state agency must provide a household with replacement SNAP benefits equal to the amount of benefits\u00a0stolen through card skimming, card cloning, or similar fraudulent methods. This requirement applies if the state agency determines that the benefits were stolen and meets certain requirements.\u00a0</p><p>Under current law, a state agency may only replace SNAP benefits that were stolen between the period beginning on October 1, 2022, and ending on December 20, 2024. Further,\u00a0the replacement amount is limited to the lesser of the amount of (1) the benefits stolen, or (2) two months of the\u00a0household's monthly allotment immediately prior to the date on which the benefits were stolen. Thus, this bill permanently extends the provision and provides for the replacement of the full amount of the benefits stolen.</p>",
      "updateDate": "2025-09-23",
      "versionCode": "id119s1540"
    },
    "title": "Fairness for Victims of SNAP Skimming Act of 2025"
  },
  "summaries": [
    {
      "actionDate": "2025-04-30",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Fairness for Victims of SNAP Skimming Act of 2025</strong></p><p>This bill requires the Supplemental Nutrition Assistance Program (SNAP) to provide for the replacement of the full amount of a household's stolen benefits.</p><p>Specifically, using funds provided by the Department of Agriculture, a state agency must provide a household with replacement SNAP benefits equal to the amount of benefits\u00a0stolen through card skimming, card cloning, or similar fraudulent methods. This requirement applies if the state agency determines that the benefits were stolen and meets certain requirements.\u00a0</p><p>Under current law, a state agency may only replace SNAP benefits that were stolen between the period beginning on October 1, 2022, and ending on December 20, 2024. Further,\u00a0the replacement amount is limited to the lesser of the amount of (1) the benefits stolen, or (2) two months of the\u00a0household's monthly allotment immediately prior to the date on which the benefits were stolen. Thus, this bill permanently extends the provision and provides for the replacement of the full amount of the benefits stolen.</p>",
      "updateDate": "2025-09-23",
      "versionCode": "id119s1540"
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
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1540is.xml"
        }
      ],
      "type": "Introduced in Senate"
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
      "updateDate": "2025-05-10T04:23:18Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Fairness for Victims of SNAP Skimming Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-05-10T04:23:17Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend the Consolidated Appropriations Act, 2023, to expand the replacement of stolen EBT benefits under the supplemental nutrition assistance program.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-05-10T04:18:20Z"
    }
  ]
}
```
