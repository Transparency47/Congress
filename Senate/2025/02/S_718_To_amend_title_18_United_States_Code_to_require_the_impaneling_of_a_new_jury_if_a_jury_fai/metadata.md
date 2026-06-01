# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/718?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/718
- Title: Eric’s Law
- Congress: 119
- Bill type: S
- Bill number: 718
- Origin chamber: Senate
- Introduced date: 2025-02-25
- Update date: 2026-01-10T06:58:27Z
- Update date including text: 2026-01-10T06:58:27Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-02-25: Introduced in Senate
- 2025-02-25 - IntroReferral: Introduced in Senate
- 2025-02-25 - IntroReferral: Read twice and referred to the Committee on the Judiciary.
- Latest action: 2025-02-25: Introduced in Senate

## Actions

- 2025-02-25 - IntroReferral: Introduced in Senate
- 2025-02-25 - IntroReferral: Read twice and referred to the Committee on the Judiciary.

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
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/718",
    "number": "718",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Crime and Law Enforcement"
    },
    "sponsors": [
      {
        "bioguideId": "C001098",
        "district": "",
        "firstName": "Ted",
        "fullName": "Sen. Cruz, Ted [R-TX]",
        "lastName": "Cruz",
        "party": "R",
        "state": "TX"
      }
    ],
    "title": "Eric\u2019s Law",
    "type": "S",
    "updateDate": "2026-01-10T06:58:27Z",
    "updateDateIncludingText": "2026-01-10T06:58:27Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-02-25",
      "committees": {
        "item": {
          "name": "Judiciary Committee",
          "systemCode": "ssju00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on the Judiciary.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-02-25",
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
          "date": "2025-02-25T19:40:23Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Judiciary Committee",
      "systemCode": "ssju00",
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
      "bioguideId": "R000618",
      "firstName": "Pete",
      "fullName": "Sen. Ricketts, Pete [R-NE]",
      "isOriginalCosponsor": "True",
      "lastName": "Ricketts",
      "party": "R",
      "sponsorshipDate": "2025-02-25",
      "state": "NE"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s718is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 718\nIN THE SENATE OF THE UNITED STATES\nFebruary 25, 2025 Mr. Cruz (for himself and Mr. Ricketts ) introduced the following bill; which was read twice and referred to the Committee on the Judiciary\nA BILL\nTo amend title 18, United States Code, to require the impaneling of a new jury if a jury fails to recommend by unanimous vote a sentence for conviction of a crime punishable by death.\n#### 1. Short title\nThis Act may be cited as Eric\u2019s Law .\n#### 2. Requirement to impanel a new jury in certain cases\n##### (a) Additional ground for impaneling jury\nSection 3593(b)(2) of title 18, United States Code, is amended\u2014\n**(1)**\nin subparagraph (C), by striking or at the end; and\n**(2)**\nby adding at the end the following:\n(E) a new special hearing is required pursuant to subsection (g); or .\n##### (b) Impaneling of new jury when jury does not reach a unanimous recommendation\nSection 3593 of title 18, United States Code, is amended by adding at the end the following:\n(g) Special rule when jury does not return a unanimous recommendation (1) In general If a jury described in subsection (b)(1) or subparagraphs (A) through (D) of subsection (b)(2) does not, by unanimous vote, make a recommendation whether the defendant should be sentenced to death, to life imprisonment without possibility of release, or some other lesser sentence pursuant to subsection (e), the court, upon motion of the attorney for the government, shall order a new special hearing and impanel a new jury pursuant to subsection (b). (2) Imposition of sentence If the jury impaneled pursuant to paragraph (1) does not reach a unanimous recommendation as to sentence, the court shall impose a sentence other than death authorized by law. .",
      "versionDate": "2025-02-25",
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
        "actionDate": "2025-02-25",
        "text": "Referred to the House Committee on the Judiciary."
      },
      "number": "1556",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Eric\u2019s Law",
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
      "legislativeSubjects": {
        "item": [
          {
            "name": "Criminal procedure and sentencing",
            "updateDate": "2025-07-17T20:35:33Z"
          },
          {
            "name": "Judicial procedure and administration",
            "updateDate": "2025-07-17T20:35:33Z"
          }
        ]
      },
      "policyArea": {
        "name": "Crime and Law Enforcement",
        "updateDate": "2025-03-21T13:52:50Z"
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
          "measure-id": "id119s718",
          "measure-number": "718",
          "measure-type": "s",
          "orig-publish-date": "2025-02-25",
          "originChamber": "SENATE",
          "update-date": "2025-05-07"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "SENATE",
            "summary-id": "id119s718v00",
            "update-date": "2025-05-07"
          },
          "action-date": "2025-02-25",
          "action-desc": "Introduced in Senate",
          "summary-text": "<p><b>Eric's Law</b></p> <p>This bill modifies procedures with respect to capital sentencing hearings.</p> <p>If a jury at a capital sentencing hearing does not reach a unanimous recommendation on the defendant's sentence and there is a motion by the attorney for the government, the court must order a new special sentencing hearing and impanel a new jury. If the new jury at the special sentencing hearing does not reach a unanimous recommendation on the defendant's sentence, then the court is prohibited from imposing a death sentence.</p>"
        },
        "title": "Eric\u2019s Law"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/s/BILLSUM-119s718.xml",
    "summary": {
      "actionDate": "2025-02-25",
      "actionDesc": "Introduced in Senate",
      "text": "<p><b>Eric's Law</b></p> <p>This bill modifies procedures with respect to capital sentencing hearings.</p> <p>If a jury at a capital sentencing hearing does not reach a unanimous recommendation on the defendant's sentence and there is a motion by the attorney for the government, the court must order a new special sentencing hearing and impanel a new jury. If the new jury at the special sentencing hearing does not reach a unanimous recommendation on the defendant's sentence, then the court is prohibited from imposing a death sentence.</p>",
      "updateDate": "2025-05-07",
      "versionCode": "id119s718"
    },
    "title": "Eric\u2019s Law"
  },
  "summaries": [
    {
      "actionDate": "2025-02-25",
      "actionDesc": "Introduced in Senate",
      "text": "<p><b>Eric's Law</b></p> <p>This bill modifies procedures with respect to capital sentencing hearings.</p> <p>If a jury at a capital sentencing hearing does not reach a unanimous recommendation on the defendant's sentence and there is a motion by the attorney for the government, the court must order a new special sentencing hearing and impanel a new jury. If the new jury at the special sentencing hearing does not reach a unanimous recommendation on the defendant's sentence, then the court is prohibited from imposing a death sentence.</p>",
      "updateDate": "2025-05-07",
      "versionCode": "id119s718"
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
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s718is.xml"
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
      "title": "Eric\u2019s Law",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-03-20T03:23:18Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Eric\u2019s Law",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-20T03:23:17Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend title 18, United States Code, to require the impaneling of a new jury if a jury fails to recommend by unanimous vote a sentence for conviction of a crime punishable by death.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-20T03:18:23Z"
    }
  ]
}
```
