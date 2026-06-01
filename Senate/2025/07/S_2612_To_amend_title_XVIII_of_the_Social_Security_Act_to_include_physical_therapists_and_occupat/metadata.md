# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/2612?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/2612
- Title: SAFE Act
- Congress: 119
- Bill type: S
- Bill number: 2612
- Origin chamber: Senate
- Introduced date: 2025-07-31
- Update date: 2026-03-05T12:03:20Z
- Update date including text: 2026-03-05T12:03:20Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-07-31: Introduced in Senate
- 2025-07-31 - IntroReferral: Introduced in Senate
- 2025-07-31 - IntroReferral: Read twice and referred to the Committee on Finance.
- Latest action: 2025-07-31: Introduced in Senate

## Actions

- 2025-07-31 - IntroReferral: Introduced in Senate
- 2025-07-31 - IntroReferral: Read twice and referred to the Committee on Finance.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-07-31",
    "latestAction": {
      "actionDate": "2025-07-31",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/2612",
    "number": "2612",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Health"
    },
    "sponsors": [
      {
        "bioguideId": "J000312",
        "district": "",
        "firstName": "James",
        "fullName": "Sen. Justice, James C. [R-WV]",
        "lastName": "Justice",
        "party": "R",
        "state": "WV"
      }
    ],
    "title": "SAFE Act",
    "type": "S",
    "updateDate": "2026-03-05T12:03:20Z",
    "updateDateIncludingText": "2026-03-05T12:03:20Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-07-31",
      "committees": {
        "item": {
          "name": "Finance Committee",
          "systemCode": "ssfi00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Finance.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-07-31",
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
        "item": [
          {
            "date": "2025-07-31T19:20:40Z",
            "name": "Referred To"
          },
          {
            "date": "2025-07-31T19:20:40Z",
            "name": "Referred To"
          }
        ]
      },
      "chamber": "Senate",
      "name": "Finance Committee",
      "systemCode": "ssfi00",
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
      "bioguideId": "L000570",
      "firstName": "Ben",
      "fullName": "Sen. Luj\u00e1n, Ben Ray [D-NM]",
      "isOriginalCosponsor": "False",
      "lastName": "Luj\u00e1n",
      "middleName": "R.",
      "party": "D",
      "sponsorshipDate": "2025-10-23",
      "state": "NM"
    },
    {
      "bioguideId": "A000382",
      "firstName": "Angela",
      "fullName": "Sen. Alsobrooks, Angela D. [D-MD]",
      "isOriginalCosponsor": "False",
      "lastName": "Alsobrooks",
      "party": "D",
      "sponsorshipDate": "2026-01-15",
      "state": "MD"
    },
    {
      "bioguideId": "D000622",
      "firstName": "Tammy",
      "fullName": "Sen. Duckworth, Tammy [D-IL]",
      "isOriginalCosponsor": "False",
      "lastName": "Duckworth",
      "party": "D",
      "sponsorshipDate": "2026-03-04",
      "state": "IL"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2612is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 2612\nIN THE SENATE OF THE UNITED STATES\nJuly 31, 2025 Mr. Justice introduced the following bill; which was read twice and referred to the Committee on Finance\nA BILL\nTo amend title XVIII of the Social Security Act to include physical therapists and occupational therapists as health professionals for purposes of the annual wellness visit under the Medicare program, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Stopping Addiction and Falls for the Elderly Act or the SAFE Act .\n#### 2. Physical therapy and occupational therapy benefit in the Medicare annual wellness visit and initial preventive physical exam\n##### (a) Annual wellness visit\n**(1) In general**\nSection 1861(hhh) of the Social Security Act ( 42 U.S.C. 1395x(hhh) ) is amended\u2014\n**(A)**\nin paragraph (1)\u2014\n**(i)**\nin subparagraph (A), by striking ; and and inserting a semicolon;\n**(ii)**\nin subparagraph (B)(ii), by striking the period at the end and inserting ; and ; and\n**(iii)**\nby adding at the end the following new subparagraph:\n(C) that, in the case of an individual who has been determined by a physician to have fallen in the previous calendar year, includes a falls risk assessment and fall prevention services. ; and\n**(B)**\nin paragraph (3)\u2014\n**(i)**\nin subparagraph (B), by striking or at the end;\n**(ii)**\nin subparagraph (C), by striking the period at the end and inserting ; or ; and\n**(iii)**\nby adding at the end the following new subparagraph:\n(D) in the case of an individual described in paragraph (1)(C), a physical therapist or an occupational therapist furnishing a separate falls risk assessment and fall prevention services. .\n**(2) Effective date**\nThe amendment made by paragraph (1) shall apply to annual wellness visits furnished on or after January 1, 2026.\n##### (b) Initial preventive physical examination\n**(1) In general**\nSection 1861(ww)(2) of the Social Security Act ( 42 U.S.C. 1395x(ww)(2) ) is amended\u2014\n**(A)**\nin subparagraph (N), by moving the margins of such subparagraph 2 ems to the left;\n**(B)**\nby redesignating subparagraph (O) as subparagraph (P); and\n**(C)**\nby inserting after subparagraph (N) the following new subparagraph:\n(O) In the case of an individual that has been determined by a physician to have experienced a fall in the previous calendar year, outpatient occupational therapy services (as defined in subsection (g)) and outpatient physical therapy services (as defined in subsection (p)). .\n**(2) Effective date**\nThe amendment made by paragraph (1) shall apply to initial preventive physical examinations furnished on or after January 1, 2026.\n#### 3. Reports to Congress\nBeginning January 1, 2027, and annually thereafter, the Secretary of Health and Human Services shall submit to Congress a report on the number of falls (as reported by the Centers for Disease Control and Prevention) experienced by individuals aged 65 and older that received treatment for pain or injury related to a fall or falls experienced in the previous calendar year. With respect to each subsequent report, such Secretary shall include the data reported in previous years and describe any changes from year to year.",
      "versionDate": "2025-07-31",
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
        "actionDate": "2025-02-10",
        "text": "Referred to the Committee on Energy and Commerce, and in addition to the Committee on Ways and Means, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned."
      },
      "number": "1171",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "SAFE Act",
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
        "name": "Health",
        "updateDate": "2025-09-18T19:05:56Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-07-31",
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
          "measure-id": "id119s2612",
          "measure-number": "2612",
          "measure-type": "s",
          "orig-publish-date": "2025-07-31",
          "originChamber": "SENATE",
          "update-date": "2025-12-02"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "SENATE",
            "summary-id": "id119s2612v00",
            "update-date": "2025-12-02"
          },
          "action-date": "2025-07-31",
          "action-desc": "Introduced in Senate",
          "summary-text": "<p><strong>Stopping Addiction and Falls for the Elderly Act or the SAFE Act</strong></p><p>This bill incorporates risk assessments and prevention services for falls into annual wellness visits and initial preventive physical exams under Medicare, as well as associated services provided by physical therapists and occupational therapists.<br/></p>"
        },
        "title": "SAFE Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/s/BILLSUM-119s2612.xml",
    "summary": {
      "actionDate": "2025-07-31",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Stopping Addiction and Falls for the Elderly Act or the SAFE Act</strong></p><p>This bill incorporates risk assessments and prevention services for falls into annual wellness visits and initial preventive physical exams under Medicare, as well as associated services provided by physical therapists and occupational therapists.<br/></p>",
      "updateDate": "2025-12-02",
      "versionCode": "id119s2612"
    },
    "title": "SAFE Act"
  },
  "summaries": [
    {
      "actionDate": "2025-07-31",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Stopping Addiction and Falls for the Elderly Act or the SAFE Act</strong></p><p>This bill incorporates risk assessments and prevention services for falls into annual wellness visits and initial preventive physical exams under Medicare, as well as associated services provided by physical therapists and occupational therapists.<br/></p>",
      "updateDate": "2025-12-02",
      "versionCode": "id119s2612"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-07-31",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2612is.xml"
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
      "title": "SAFE Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-03-05T12:03:20Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "SAFE Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-08-09T03:53:24Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Stopping Addiction and Falls for the Elderly Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-08-09T03:53:24Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend title XVIII of the Social Security Act to include physical therapists and occupational therapists as health professionals for purposes of the annual wellness visit under the Medicare program, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-08-09T03:48:32Z"
    }
  ]
}
```
