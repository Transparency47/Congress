# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/1556?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/1556
- Title: Eric’s Law
- Congress: 119
- Bill type: HR
- Bill number: 1556
- Origin chamber: House
- Introduced date: 2025-02-25
- Update date: 2026-01-10T06:57:47Z
- Update date including text: 2026-01-10T06:57:47Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-02-25: Introduced in House
- 2025-02-25 - IntroReferral: Introduced in House
- 2025-02-25 - IntroReferral: Introduced in House
- 2025-02-25 - IntroReferral: Referred to the House Committee on the Judiciary.
- Latest action: 2025-02-25: Introduced in House

## Actions

- 2025-02-25 - IntroReferral: Introduced in House
- 2025-02-25 - IntroReferral: Introduced in House
- 2025-02-25 - IntroReferral: Referred to the House Committee on the Judiciary.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-02-25",
    "latestAction": {
      "actionDate": "2025-02-25",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/1556",
    "number": "1556",
    "originChamber": "House",
    "policyArea": {
      "name": "Crime and Law Enforcement"
    },
    "sponsors": [
      {
        "bioguideId": "B001327",
        "district": "8",
        "firstName": "Robert",
        "fullName": "Rep. Bresnahan, Robert [R-PA-8]",
        "lastName": "Bresnahan",
        "party": "R",
        "state": "PA"
      }
    ],
    "title": "Eric\u2019s Law",
    "type": "HR",
    "updateDate": "2026-01-10T06:57:47Z",
    "updateDateIncludingText": "2026-01-10T06:57:47Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-02-25",
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
      "actionDate": "2025-02-25",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-02-25",
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
          "date": "2025-02-25T15:03:05Z",
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
      "bioguideId": "T000467",
      "district": "15",
      "firstName": "Glenn",
      "fullName": "Rep. Thompson, Glenn [R-PA-15]",
      "isOriginalCosponsor": "True",
      "lastName": "Thompson",
      "party": "R",
      "sponsorshipDate": "2025-02-25",
      "state": "PA"
    },
    {
      "bioguideId": "R000610",
      "district": "14",
      "firstName": "Guy",
      "fullName": "Rep. Reschenthaler, Guy [R-PA-14]",
      "isOriginalCosponsor": "True",
      "lastName": "Reschenthaler",
      "party": "R",
      "sponsorshipDate": "2025-02-25",
      "state": "PA"
    },
    {
      "bioguideId": "H001098",
      "district": "8",
      "firstName": "Abraham",
      "fullName": "Rep. Hamadeh, Abraham [R-AZ-8]",
      "isOriginalCosponsor": "False",
      "lastName": "Hamadeh",
      "middleName": "J.",
      "party": "R",
      "sponsorshipDate": "2025-03-14",
      "state": "AZ"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1556ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 1556\nIN THE HOUSE OF REPRESENTATIVES\nFebruary 25, 2025 Mr. Bresnahan (for himself, Mr. Thompson of Pennsylvania , and Mr. Reschenthaler ) introduced the following bill; which was referred to the Committee on the Judiciary\nA BILL\nTo amend title 18, United States Code, to require the impaneling of a new jury if a jury fails to recommend by unanimous vote a sentence for conviction of a crime punishable by death.\n#### 1. Short title\nThis Act may be cited as Eric\u2019s Law .\n#### 2. Requirement to impanel a new jury in certain cases\n##### (a) Additional ground for impaneling jury\nSection 3593(b)(2) of title 18, United States Code, is amended\u2014\n**(1)**\nin subparagraph (C), by striking or at the end; and\n**(2)**\nby adding at the end the following:\n(E) a new special hearing is required pursuant to subsection (g); or .\n##### (b) Impaneling of new jury when jury does not reach a unanimous recommendation\nSection 3593 of title 18, United States Code, is amended by adding at the end the following:\n(g) Special rule when jury does not return a unanimous recommendation (1) In general If a jury described in subsection (b)(1) or subparagraphs (A) through (D) of subsection (b)(2) does not, by unanimous vote, make a recommendation whether the defendant should be sentenced to death, to life imprisonment without possibility of release, or some other lesser sentence pursuant to subsection (e), the court, upon motion of the attorney for the government, shall order a new special hearing and impanel a new jury pursuant to subsection (b). (2) Imposition of sentence If the jury impaneled pursuant to paragraph (1) does not reach a unanimous recommendation as to sentence, the court shall impose a sentence other than death authorized by law. .",
      "versionDate": "2025-02-25",
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
        "actionDate": "2025-02-25",
        "text": "Read twice and referred to the Committee on the Judiciary."
      },
      "number": "718",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Eric\u2019s Law",
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
      "legislativeSubjects": {
        "item": [
          {
            "name": "Criminal procedure and sentencing",
            "updateDate": "2025-07-17T20:35:19Z"
          },
          {
            "name": "Judicial procedure and administration",
            "updateDate": "2025-07-17T20:35:19Z"
          }
        ]
      },
      "policyArea": {
        "name": "Crime and Law Enforcement",
        "updateDate": "2025-03-18T14:19:43Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-02-25",
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
          "measure-id": "id119hr1556",
          "measure-number": "1556",
          "measure-type": "hr",
          "orig-publish-date": "2025-02-25",
          "originChamber": "HOUSE",
          "update-date": "2025-06-09"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr1556v00",
            "update-date": "2025-06-09"
          },
          "action-date": "2025-02-25",
          "action-desc": "Introduced in House",
          "summary-text": "<p><b>Eric's Law</b></p> <p>This bill modifies procedures with respect to capital sentencing hearings.</p> <p>If a jury at a capital sentencing hearing does not reach a unanimous recommendation on the defendant's sentence and there is a motion by the attorney for the government, the court must order a new special sentencing hearing and impanel a new jury. If the new jury at the special sentencing hearing does not reach a unanimous recommendation on the defendant's sentence, then the court is prohibited from imposing a death sentence.</p>"
        },
        "title": "Eric\u2019s Law"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr1556.xml",
    "summary": {
      "actionDate": "2025-02-25",
      "actionDesc": "Introduced in House",
      "text": "<p><b>Eric's Law</b></p> <p>This bill modifies procedures with respect to capital sentencing hearings.</p> <p>If a jury at a capital sentencing hearing does not reach a unanimous recommendation on the defendant's sentence and there is a motion by the attorney for the government, the court must order a new special sentencing hearing and impanel a new jury. If the new jury at the special sentencing hearing does not reach a unanimous recommendation on the defendant's sentence, then the court is prohibited from imposing a death sentence.</p>",
      "updateDate": "2025-06-09",
      "versionCode": "id119hr1556"
    },
    "title": "Eric\u2019s Law"
  },
  "summaries": [
    {
      "actionDate": "2025-02-25",
      "actionDesc": "Introduced in House",
      "text": "<p><b>Eric's Law</b></p> <p>This bill modifies procedures with respect to capital sentencing hearings.</p> <p>If a jury at a capital sentencing hearing does not reach a unanimous recommendation on the defendant's sentence and there is a motion by the attorney for the government, the court must order a new special sentencing hearing and impanel a new jury. If the new jury at the special sentencing hearing does not reach a unanimous recommendation on the defendant's sentence, then the court is prohibited from imposing a death sentence.</p>",
      "updateDate": "2025-06-09",
      "versionCode": "id119hr1556"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-02-25",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1556ih.xml"
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
      "title": "Eric\u2019s Law",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-03-17T12:53:29Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Eric\u2019s Law",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-17T12:53:23Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend title 18, United States Code, to require the impaneling of a new jury if a jury fails to recommend by unanimous vote a sentence for conviction of a crime punishable by death.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-17T12:48:30Z"
    }
  ]
}
```
