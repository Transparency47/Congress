# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/181?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/s/181
- Title: A bill to require agencies submit zero-based budgets.
- Congress: 119
- Bill type: S
- Bill number: 181
- Origin chamber: Senate
- Introduced date: 2025-01-22
- Update date: 2025-02-28T19:31:40Z
- Update date including text: 2025-02-28T19:31:40Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-01-22: Introduced in Senate
- 2025-01-22 - IntroReferral: Introduced in Senate
- 2025-01-22 - IntroReferral: Read twice and referred to the Committee on Homeland Security and Governmental Affairs.
- Latest action: 2025-01-22: Introduced in Senate

## Actions

- 2025-01-22 - IntroReferral: Introduced in Senate
- 2025-01-22 - IntroReferral: Read twice and referred to the Committee on Homeland Security and Governmental Affairs.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-01-22",
    "latestAction": {
      "actionDate": "2025-01-22",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/s/181",
    "number": "181",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Economics and Public Finance"
    },
    "sponsors": [
      {
        "bioguideId": "R000584",
        "district": "",
        "firstName": "James",
        "fullName": "Sen. Risch, James E. [R-ID]",
        "lastName": "Risch",
        "party": "R",
        "state": "ID"
      }
    ],
    "title": "A bill to require agencies submit zero-based budgets.",
    "type": "S",
    "updateDate": "2025-02-28T19:31:40Z",
    "updateDateIncludingText": "2025-02-28T19:31:40Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-01-22",
      "committees": {
        "item": {
          "name": "Homeland Security and Governmental Affairs Committee",
          "systemCode": "ssga00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Homeland Security and Governmental Affairs.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-01-22",
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
          "date": "2025-01-22T16:45:16Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Homeland Security and Governmental Affairs Committee",
      "systemCode": "ssga00",
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
      "sponsorshipDate": "2025-01-22",
      "state": "ID"
    },
    {
      "bioguideId": "R000618",
      "firstName": "Pete",
      "fullName": "Sen. Ricketts, Pete [R-NE]",
      "isOriginalCosponsor": "True",
      "lastName": "Ricketts",
      "party": "R",
      "sponsorshipDate": "2025-01-22",
      "state": "NE"
    },
    {
      "bioguideId": "C001098",
      "firstName": "Ted",
      "fullName": "Sen. Cruz, Ted [R-TX]",
      "isOriginalCosponsor": "True",
      "lastName": "Cruz",
      "party": "R",
      "sponsorshipDate": "2025-01-22",
      "state": "TX"
    },
    {
      "bioguideId": "S001232",
      "firstName": "Tim",
      "fullName": "Sen. Sheehy, Tim [R-MT]",
      "isOriginalCosponsor": "True",
      "lastName": "Sheehy",
      "party": "R",
      "sponsorshipDate": "2025-01-22",
      "state": "MT"
    },
    {
      "bioguideId": "S001217",
      "firstName": "Rick",
      "fullName": "Sen. Scott, Rick [R-FL]",
      "isOriginalCosponsor": "True",
      "lastName": "Scott",
      "party": "R",
      "sponsorshipDate": "2025-01-22",
      "state": "FL"
    },
    {
      "bioguideId": "L000571",
      "firstName": "Cynthia",
      "fullName": "Sen. Lummis, Cynthia M. [R-WY]",
      "isOriginalCosponsor": "True",
      "lastName": "Lummis",
      "middleName": "M.",
      "party": "R",
      "sponsorshipDate": "2025-01-22",
      "state": "WY"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s181is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 181\nIN THE SENATE OF THE UNITED STATES\nJanuary 22, 2025 Mr. Risch (for himself, Mr. Crapo , Mr. Ricketts , Mr. Cruz , Mr. Sheehy , Mr. Scott of Florida , and Ms. Lummis ) introduced the following bill; which was read twice and referred to the Committee on Homeland Security and Governmental Affairs\nA BILL\nTo require agencies submit zero-based budgets.\n#### 1. Zero-based budgets\n##### (a) Definition\nIn this Act:\n**(1) Agency**\nThe term agency has the meaning given the term in section 551 of title 5, United States Code.\n**(2) Zero-based budget**\nThe term zero-based budget means a systematic budget analysis in support of decision making in which managers\u2014\n**(A)**\nexamine current objectives, operations, and costs;\n**(B)**\nconsider alternative ways of carrying out a program or activity; and\n**(C)**\nrank different programs or activities by order of importance to the organization.\n##### (b) Zero-Based budgets\nEvery sixth year, each agency shall submit to the Director of the Office of Management and Budget and the Committee on the Budget of the Senate and the Committee on the Budget of the House of Representatives a zero-based budget for the next fiscal year and each of the 4 ensuing fiscal years.\n##### (c) Recommendations\nIn addition to the zero-based budget required under subsection (b), each agency, except the Department of Defense and the National Nuclear Security Administration shall submit recommendations for which programs Congress should cut or reduce appropriations in an amount that equals not less than a 2-percent reduction from the previous year appropriation in discretionary spending.",
      "versionDate": "2025-01-22",
      "versionType": "Introduced in Senate"
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
        "name": "Economics and Public Finance",
        "updateDate": "2025-02-28T19:22:44Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-01-22",
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
          "measure-id": "id119s181",
          "measure-number": "181",
          "measure-type": "s",
          "orig-publish-date": "2025-01-22",
          "originChamber": "SENATE",
          "update-date": "2025-02-28"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "SENATE",
            "summary-id": "id119s181v00",
            "update-date": "2025-02-28"
          },
          "action-date": "2025-01-22",
          "action-desc": "Introduced in Senate",
          "summary-text": "<p>This bill requires federal agencies to submit zero-based budgets to the Office of Management and Budget and the congressional budget committees<em>.\u00a0</em>Under the bill, a<em>\u00a0zero-based budget</em> is a systematic budget analysis in which managers (1) examine current objectives, operations, and costs; (2) consider alternative ways of carrying out programs or activities; and (3) rank different programs or activities by order of importance.</p><p>The bill also requires federal agencies to submit recommendations to reduce spending by at least 2% from the previous year's levels. The Department of Defense and the National Nuclear Security Administration are exempt from this requirement.</p>"
        },
        "title": "A bill to require agencies submit zero-based budgets."
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/s/BILLSUM-119s181.xml",
    "summary": {
      "actionDate": "2025-01-22",
      "actionDesc": "Introduced in Senate",
      "text": "<p>This bill requires federal agencies to submit zero-based budgets to the Office of Management and Budget and the congressional budget committees<em>.\u00a0</em>Under the bill, a<em>\u00a0zero-based budget</em> is a systematic budget analysis in which managers (1) examine current objectives, operations, and costs; (2) consider alternative ways of carrying out programs or activities; and (3) rank different programs or activities by order of importance.</p><p>The bill also requires federal agencies to submit recommendations to reduce spending by at least 2% from the previous year's levels. The Department of Defense and the National Nuclear Security Administration are exempt from this requirement.</p>",
      "updateDate": "2025-02-28",
      "versionCode": "id119s181"
    },
    "title": "A bill to require agencies submit zero-based budgets."
  },
  "summaries": [
    {
      "actionDate": "2025-01-22",
      "actionDesc": "Introduced in Senate",
      "text": "<p>This bill requires federal agencies to submit zero-based budgets to the Office of Management and Budget and the congressional budget committees<em>.\u00a0</em>Under the bill, a<em>\u00a0zero-based budget</em> is a systematic budget analysis in which managers (1) examine current objectives, operations, and costs; (2) consider alternative ways of carrying out programs or activities; and (3) rank different programs or activities by order of importance.</p><p>The bill also requires federal agencies to submit recommendations to reduce spending by at least 2% from the previous year's levels. The Department of Defense and the National Nuclear Security Administration are exempt from this requirement.</p>",
      "updateDate": "2025-02-28",
      "versionCode": "id119s181"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-01-22",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s181is.xml"
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
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to require agencies submit zero-based budgets.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-02-20T02:03:25Z"
    },
    {
      "title": "A bill to require agencies submit zero-based budgets.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-01-23T11:56:18Z"
    }
  ]
}
```
