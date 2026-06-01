# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/3001?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/3001
- Title: Shutdown Fairness Act
- Congress: 119
- Bill type: S
- Bill number: 3001
- Origin chamber: Senate
- Introduced date: 2025-10-09
- Update date: 2025-10-24T17:42:54Z
- Update date including text: 2025-10-24T17:42:54Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-10-09: Introduced in Senate
- 2025-10-09 - IntroReferral: Introduced in Senate
- 2025-10-09 - IntroReferral: Read twice and referred to the Committee on Appropriations.
- Latest action: 2025-10-09: Introduced in Senate

## Actions

- 2025-10-09 - IntroReferral: Introduced in Senate
- 2025-10-09 - IntroReferral: Read twice and referred to the Committee on Appropriations.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-10-09",
    "latestAction": {
      "actionDate": "2025-10-09",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/3001",
    "number": "3001",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Government Operations and Politics"
    },
    "sponsors": [
      {
        "bioguideId": "J000293",
        "district": "",
        "firstName": "Ron",
        "fullName": "Sen. Johnson, Ron [R-WI]",
        "lastName": "Johnson",
        "party": "R",
        "state": "WI"
      }
    ],
    "title": "Shutdown Fairness Act",
    "type": "S",
    "updateDate": "2025-10-24T17:42:54Z",
    "updateDateIncludingText": "2025-10-24T17:42:54Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-10-09",
      "committees": {
        "item": {
          "name": "Appropriations Committee",
          "systemCode": "ssap00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Appropriations.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-10-09",
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
          "date": "2025-10-10T01:13:36Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Appropriations Committee",
      "systemCode": "ssap00",
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
      "bioguideId": "C000880",
      "firstName": "Mike",
      "fullName": "Sen. Crapo, Mike [R-ID]",
      "isOriginalCosponsor": "True",
      "lastName": "Crapo",
      "party": "R",
      "sponsorshipDate": "2025-10-09",
      "state": "ID"
    },
    {
      "bioguideId": "C001095",
      "firstName": "Tom",
      "fullName": "Sen. Cotton, Tom [R-AR]",
      "isOriginalCosponsor": "True",
      "lastName": "Cotton",
      "party": "R",
      "sponsorshipDate": "2025-10-09",
      "state": "AR"
    },
    {
      "bioguideId": "R000584",
      "firstName": "James",
      "fullName": "Sen. Risch, James E. [R-ID]",
      "isOriginalCosponsor": "True",
      "lastName": "Risch",
      "middleName": "E.",
      "party": "R",
      "sponsorshipDate": "2025-10-09",
      "state": "ID"
    },
    {
      "bioguideId": "Y000064",
      "firstName": "Todd",
      "fullName": "Sen. Young, Todd [R-IN]",
      "isOriginalCosponsor": "True",
      "lastName": "Young",
      "party": "R",
      "sponsorshipDate": "2025-10-09",
      "state": "IN"
    },
    {
      "bioguideId": "S001198",
      "firstName": "Dan",
      "fullName": "Sen. Sullivan, Dan [R-AK]",
      "isOriginalCosponsor": "False",
      "lastName": "Sullivan",
      "party": "R",
      "sponsorshipDate": "2025-10-14",
      "state": "AK"
    },
    {
      "bioguideId": "C001075",
      "firstName": "Bill",
      "fullName": "Sen. Cassidy, Bill [R-LA]",
      "isOriginalCosponsor": "False",
      "lastName": "Cassidy",
      "party": "R",
      "sponsorshipDate": "2025-10-15",
      "state": "LA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s3001is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 3001\nIN THE SENATE OF THE UNITED STATES\nOctober 9, 2025 Mr. Johnson (for himself, Mr. Crapo , Mr. Cotton , Mr. Risch , and Mr. Young ) introduced the following bill; which was read twice and referred to the Committee on Appropriations\nA BILL\nTo appropriate funds for pay and allowances of excepted Federal employees, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Shutdown Fairness Act .\n#### 2. Appropriations\n##### (a) Definitions\nIn this section\u2014\n**(1)**\nthe term agency means each authority of the executive, legislative, or judicial branch of the Government of the United States; and\n**(2)**\nthe term excepted employee \u2014\n**(A)**\nmeans an employee of an agency who the head of that agency determines is an excepted employee or an employee performing emergency work, as those terms are defined by the Office of Personnel Management; and\n**(B)**\nincludes a contractor who\u2014\n**(i)**\nprovides support to an employee described in subparagraph (A); and\n**(ii)**\nis required to perform work during a lapse in appropriations, as determined by the head of the agency with respect to which the contractor provides support.\n##### (b) Appropriations\nFor fiscal year 2026, or any fiscal year thereafter, for any period during which interim or full-year appropriations for that fiscal year are not in effect for an agency, there are appropriated to the head of the agency, out of any money in the Treasury not otherwise appropriated, such sums as are necessary to provide pay and allowances to excepted employees of the agency who are required to perform work during that period.\n##### (c) Termination\nAppropriations and funds made available and authority granted under subsection (b) shall be available to the head of an agency until whichever of the following first occurs:\n**(1)**\nThe enactment into law of appropriations for the agency until the end of the applicable fiscal year (including a continuing appropriation) that provide amounts for the purposes for which amounts are made available under subsection (b).\n**(2)**\nThe enactment into law of appropriations for the agency until the end of the applicable fiscal year (including a continuing appropriation) without any appropriation for such purposes.\n##### (d) Subsequent lapses\nAppropriations made available under subsection (b) may not be obligated by the head of an agency during any period during which continuing appropriations for the purposes for which amounts are made available under subsection (b) are in effect for the agency.\n##### (e) Charging to full-Year appropriations\nExpenditures made by the head of an agency pursuant to subsection (b) shall be charged to the applicable appropriation for the agency whenever a regular appropriation bill or a measure making continuing appropriations until the end of the applicable fiscal year for the agency becomes law.",
      "versionDate": "2025-10-09",
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
        "actionDate": "2025-10-21",
        "text": "Referred to the House Committee on Appropriations."
      },
      "number": "5801",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Shutdown Fairness Act",
      "type": "HR"
    },
    {
      "congress": "119",
      "latestAction": {
        "actionDate": "2025-10-23",
        "text": "Motion by Senator Thune to reconsider the vote by which cloture on the motion to proceed to S. 3012 was not invoked (Record Vote No. 585) made in Senate."
      },
      "number": "3012",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Shutdown Fairness Act",
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
        "name": "Government Operations and Politics",
        "updateDate": "2025-10-24T15:59:17Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-10-09",
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
          "measure-id": "id119s3001",
          "measure-number": "3001",
          "measure-type": "s",
          "orig-publish-date": "2025-10-09",
          "originChamber": "SENATE",
          "update-date": "2025-10-24"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "SENATE",
            "summary-id": "id119s3001v00",
            "update-date": "2025-10-24"
          },
          "action-date": "2025-10-09",
          "action-desc": "Introduced in Senate",
          "summary-text": "<p><strong>Shutdown Fairness Act</strong></p><p>This bill provides appropriations to pay federal employees who work during a government shutdown.</p><p>Specifically, the bill provides appropriations for federal agencies to provide pay and allowances to excepted employees who are required to work during any period in which interim or full-year appropriations are not in effect for a fiscal year (i.e., a government shutdown).\u00a0</p><p>Under current law, excepted employees are required to work during a government\u00a0shutdown and are\u00a0not paid until the government shutdown is over. This bill provides appropriations to pay excepted employees during a government shutdown. The bill also specifies that the term <em>excepted employee </em>includes certain contractors who support federal employees during a government shutdown.\u00a0</p><p>A federal agency may not use the funds provided by this bill during any period in which continuing appropriations are in effect for the purpose of paying excepted employees of the agency.</p>"
        },
        "title": "Shutdown Fairness Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/s/BILLSUM-119s3001.xml",
    "summary": {
      "actionDate": "2025-10-09",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Shutdown Fairness Act</strong></p><p>This bill provides appropriations to pay federal employees who work during a government shutdown.</p><p>Specifically, the bill provides appropriations for federal agencies to provide pay and allowances to excepted employees who are required to work during any period in which interim or full-year appropriations are not in effect for a fiscal year (i.e., a government shutdown).\u00a0</p><p>Under current law, excepted employees are required to work during a government\u00a0shutdown and are\u00a0not paid until the government shutdown is over. This bill provides appropriations to pay excepted employees during a government shutdown. The bill also specifies that the term <em>excepted employee </em>includes certain contractors who support federal employees during a government shutdown.\u00a0</p><p>A federal agency may not use the funds provided by this bill during any period in which continuing appropriations are in effect for the purpose of paying excepted employees of the agency.</p>",
      "updateDate": "2025-10-24",
      "versionCode": "id119s3001"
    },
    "title": "Shutdown Fairness Act"
  },
  "summaries": [
    {
      "actionDate": "2025-10-09",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Shutdown Fairness Act</strong></p><p>This bill provides appropriations to pay federal employees who work during a government shutdown.</p><p>Specifically, the bill provides appropriations for federal agencies to provide pay and allowances to excepted employees who are required to work during any period in which interim or full-year appropriations are not in effect for a fiscal year (i.e., a government shutdown).\u00a0</p><p>Under current law, excepted employees are required to work during a government\u00a0shutdown and are\u00a0not paid until the government shutdown is over. This bill provides appropriations to pay excepted employees during a government shutdown. The bill also specifies that the term <em>excepted employee </em>includes certain contractors who support federal employees during a government shutdown.\u00a0</p><p>A federal agency may not use the funds provided by this bill during any period in which continuing appropriations are in effect for the purpose of paying excepted employees of the agency.</p>",
      "updateDate": "2025-10-24",
      "versionCode": "id119s3001"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-10-09",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s3001is.xml"
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
      "title": "Shutdown Fairness Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-10-23T02:53:15Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Shutdown Fairness Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-10-23T02:53:14Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to appropriate funds for pay and allowances of excepted Federal employees, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-10-23T02:48:14Z"
    }
  ]
}
```
