# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/56?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/56
- Title: SAP Act
- Congress: 119
- Bill type: S
- Bill number: 56
- Origin chamber: Senate
- Introduced date: 2025-01-09
- Update date: 2025-12-05T21:59:53Z
- Update date including text: 2025-12-05T21:59:53Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-01-09: Introduced in Senate
- 2025-01-09 - IntroReferral: Introduced in Senate
- 2025-01-09 - IntroReferral: Read twice and referred to the Committee on Agriculture, Nutrition, and Forestry.
- Latest action: 2025-01-09: Introduced in Senate

## Actions

- 2025-01-09 - IntroReferral: Introduced in Senate
- 2025-01-09 - IntroReferral: Read twice and referred to the Committee on Agriculture, Nutrition, and Forestry.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-01-09",
    "latestAction": {
      "actionDate": "2025-01-09",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/56",
    "number": "56",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Agriculture and Food"
    },
    "sponsors": [
      {
        "bioguideId": "W000800",
        "district": "",
        "firstName": "Peter",
        "fullName": "Sen. Welch, Peter [D-VT]",
        "lastName": "Welch",
        "party": "D",
        "state": "VT"
      }
    ],
    "title": "SAP Act",
    "type": "S",
    "updateDate": "2025-12-05T21:59:53Z",
    "updateDateIncludingText": "2025-12-05T21:59:53Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-01-09",
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
      "actionDate": "2025-01-09",
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
          "date": "2025-01-09T20:15:01Z",
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
      "bioguideId": "C001035",
      "firstName": "Susan",
      "fullName": "Sen. Collins, Susan M. [R-ME]",
      "isOriginalCosponsor": "True",
      "lastName": "Collins",
      "middleName": "M.",
      "party": "R",
      "sponsorshipDate": "2025-01-09",
      "state": "ME"
    },
    {
      "bioguideId": "K000383",
      "firstName": "Angus",
      "fullName": "Sen. King, Angus S., Jr. [I-ME]",
      "isOriginalCosponsor": "True",
      "lastName": "King",
      "middleName": "S.",
      "party": "I",
      "sponsorshipDate": "2025-01-09",
      "state": "ME"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s56is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 56\nIN THE SENATE OF THE UNITED STATES\nJanuary 9, 2025 Mr. Welch (for himself, Ms. Collins , and Mr. King ) introduced the following bill; which was read twice and referred to the Committee on Agriculture, Nutrition, and Forestry\nA BILL\nTo amend the Agricultural Act of 2014 with respect to the Acer access and development program, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Supporting All Producers Act or the SAP Act .\n#### 2. Acer access and development program\nSection 12306 of the Agricultural Act of 2014 ( 7 U.S.C. 1632c ) is amended\u2014\n**(1)**\nby redesignating subsections (e) and (f) as subsections (f) and (g), respectively;\n**(2)**\nby inserting after subsection (d) the following:\n(e) Consultations (1) In general Beginning with the first request for applications under this section that occurs at least 1 year after the date of the enactment of the SAP Act , not later than 6 months before such a request for applications, the Secretary shall solicit input from maple industry stakeholders with respect to the research and education priorities of the maple industry. (2) Consideration The Secretary shall consider the information provided through the consultation required under paragraph (1) when making grants under this section. ; and\n**(3)**\nin subsection (g), as so redesignated, by striking 2023 and inserting 2030 .",
      "versionDate": "2025-01-09",
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
        "actionDate": "2025-02-14",
        "text": "Referred to the Subcommittee on Forestry and Horticulture."
      },
      "number": "289",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "SAP Act of 2025",
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
            "name": "Agricultural education",
            "updateDate": "2025-03-19T20:18:39Z"
          },
          {
            "name": "Agricultural marketing and promotion",
            "updateDate": "2025-03-19T20:18:46Z"
          },
          {
            "name": "Agricultural prices, subsidies, credit",
            "updateDate": "2025-03-19T20:18:54Z"
          },
          {
            "name": "Agricultural research",
            "updateDate": "2025-03-19T20:19:04Z"
          },
          {
            "name": "Food industry and services",
            "updateDate": "2025-03-19T20:19:15Z"
          },
          {
            "name": "Forests, forestry, trees",
            "updateDate": "2025-03-19T20:19:27Z"
          }
        ]
      },
      "policyArea": {
        "name": "Agriculture and Food",
        "updateDate": "2025-02-21T12:06:11Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-01-09",
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
          "measure-id": "id119s56",
          "measure-number": "56",
          "measure-type": "s",
          "orig-publish-date": "2025-01-09",
          "originChamber": "SENATE",
          "update-date": "2025-02-21"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "SENATE",
            "summary-id": "id119s56v00",
            "update-date": "2025-02-21"
          },
          "action-date": "2025-01-09",
          "action-desc": "Introduced in Senate",
          "summary-text": "<p><strong>Supporting All Producers Act or the SAP Act</strong> <strong></strong></p><p>This bill directs the Department of Agriculture (USDA) to solicit input from maple industry stakeholders with respect to the research and education priorities of the maple industry for the Acer Access and Development Program (Acer). Specifically, the bill amends Acer to require USDA to consider the information provided through consultation with the maple industry when making program grants.</p><p>The bill also extends the program's authorization through FY2030.</p><p>As background, Acer provides competitive grants to states, tribal governments, and research institutions to support their efforts to promote the domestic maple syrup industry through activities\u00a0associated with, among other things,\u00a0the promotion of (1) research and education related to maple syrup production, and (2) natural resource sustainability in the maple syrup industry.</p>"
        },
        "title": "SAP Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/s/BILLSUM-119s56.xml",
    "summary": {
      "actionDate": "2025-01-09",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Supporting All Producers Act or the SAP Act</strong> <strong></strong></p><p>This bill directs the Department of Agriculture (USDA) to solicit input from maple industry stakeholders with respect to the research and education priorities of the maple industry for the Acer Access and Development Program (Acer). Specifically, the bill amends Acer to require USDA to consider the information provided through consultation with the maple industry when making program grants.</p><p>The bill also extends the program's authorization through FY2030.</p><p>As background, Acer provides competitive grants to states, tribal governments, and research institutions to support their efforts to promote the domestic maple syrup industry through activities\u00a0associated with, among other things,\u00a0the promotion of (1) research and education related to maple syrup production, and (2) natural resource sustainability in the maple syrup industry.</p>",
      "updateDate": "2025-02-21",
      "versionCode": "id119s56"
    },
    "title": "SAP Act"
  },
  "summaries": [
    {
      "actionDate": "2025-01-09",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Supporting All Producers Act or the SAP Act</strong> <strong></strong></p><p>This bill directs the Department of Agriculture (USDA) to solicit input from maple industry stakeholders with respect to the research and education priorities of the maple industry for the Acer Access and Development Program (Acer). Specifically, the bill amends Acer to require USDA to consider the information provided through consultation with the maple industry when making program grants.</p><p>The bill also extends the program's authorization through FY2030.</p><p>As background, Acer provides competitive grants to states, tribal governments, and research institutions to support their efforts to promote the domestic maple syrup industry through activities\u00a0associated with, among other things,\u00a0the promotion of (1) research and education related to maple syrup production, and (2) natural resource sustainability in the maple syrup industry.</p>",
      "updateDate": "2025-02-21",
      "versionCode": "id119s56"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-01-09",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s56is.xml"
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
      "title": "SAP Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-02-06T01:08:16Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "SAP Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-02-06T01:08:15Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Supporting All Producers Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-02-06T01:08:15Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend the Agricultural Act of 2014 with respect to the Acer access and development program, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-02-06T01:03:25Z"
    }
  ]
}
```
