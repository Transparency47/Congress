# Metadata

- API URL: https://api.congress.gov/v3/bill/119/sres/119?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-resolution/119
- Title: A resolution memorializing those lost to the COVID-19 pandemic.
- Congress: 119
- Bill type: SRES
- Bill number: 119
- Origin chamber: Senate
- Introduced date: 2025-03-06
- Update date: 2026-04-07T16:47:51Z
- Update date including text: 2026-04-07T16:47:51Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-03-06: Introduced in Senate
- 2025-03-06 - IntroReferral: Introduced in Senate
- 2025-03-06 - IntroReferral: Referred to the Committee on Health, Education, Labor, and Pensions. (text: CR S1610)
- Latest action: 2025-03-06: Introduced in Senate

## Actions

- 2025-03-06 - IntroReferral: Introduced in Senate
- 2025-03-06 - IntroReferral: Referred to the Committee on Health, Education, Labor, and Pensions. (text: CR S1610)

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-03-06",
    "latestAction": {
      "actionDate": "2025-03-06",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-resolution/119",
    "number": "119",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Health"
    },
    "sponsors": [
      {
        "bioguideId": "W000817",
        "district": "",
        "firstName": "Elizabeth",
        "fullName": "Sen. Warren, Elizabeth [D-MA]",
        "lastName": "Warren",
        "party": "D",
        "state": "MA"
      }
    ],
    "title": "A resolution memorializing those lost to the COVID-19 pandemic.",
    "type": "SRES",
    "updateDate": "2026-04-07T16:47:51Z",
    "updateDateIncludingText": "2026-04-07T16:47:51Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-03-06",
      "committees": {
        "item": {
          "name": "Health, Education, Labor, and Pensions Committee",
          "systemCode": "sshr00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Referred to the Committee on Health, Education, Labor, and Pensions. (text: CR S1610)",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-03-06",
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
          "date": "2025-03-06T21:05:10Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Health, Education, Labor, and Pensions Committee",
      "systemCode": "sshr00",
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
      "bioguideId": "M000133",
      "firstName": "Edward",
      "fullName": "Sen. Markey, Edward J. [D-MA]",
      "isOriginalCosponsor": "True",
      "lastName": "Markey",
      "middleName": "J.",
      "party": "D",
      "sponsorshipDate": "2025-03-06",
      "state": "MA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/sres/BILLS-119sres119is.xml",
      "text": "III\n119th CONGRESS\n1st Session\nS. RES. 119\nIN THE SENATE OF THE UNITED STATES\nMarch 6, 2025 Ms. Warren (for herself and Mr. Markey ) submitted the following resolution; which was referred to the Committee on Health, Education, Labor, and Pensions\nRESOLUTION\nMemorializing those lost to the COVID\u201319 pandemic.\nThat the Senate\u2014\n**(1)**\nwill memorialize those lost to the COVID\u201319 pandemic;\n**(2)**\nrecognizes the suffering of those who contracted the SARS\u2013CoV\u20132 virus and those who continue to struggle with the ongoing impacts of the COVID\u201319 pandemic; and\n**(3)**\nexpresses support for the annual designation of the first Monday in March as COVID\u201319 Victims Memorial Day .",
      "versionDate": "2025-03-06",
      "versionType": "IS"
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
        "updateDate": "2025-03-12T16:23:11Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-03-06",
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
          "measure-id": "id119sres119",
          "measure-number": "119",
          "measure-type": "sres",
          "orig-publish-date": "2025-03-06",
          "originChamber": "SENATE",
          "update-date": "2026-04-07"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "SENATE",
            "summary-id": "id119sres119v00",
            "update-date": "2026-04-07"
          },
          "action-date": "2025-03-06",
          "action-desc": "Introduced in Senate",
          "summary-text": "<p>This resolution expresses support for the designation of the first Monday in March as COVID-19 Victims Memorial Day.</p>"
        },
        "title": "A resolution memorializing those lost to the COVID-19 pandemic."
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/sres/BILLSUM-119sres119.xml",
    "summary": {
      "actionDate": "2025-03-06",
      "actionDesc": "Introduced in Senate",
      "text": "<p>This resolution expresses support for the designation of the first Monday in March as COVID-19 Victims Memorial Day.</p>",
      "updateDate": "2026-04-07",
      "versionCode": "id119sres119"
    },
    "title": "A resolution memorializing those lost to the COVID-19 pandemic."
  },
  "summaries": [
    {
      "actionDate": "2025-03-06",
      "actionDesc": "Introduced in Senate",
      "text": "<p>This resolution expresses support for the designation of the first Monday in March as COVID-19 Victims Memorial Day.</p>",
      "updateDate": "2026-04-07",
      "versionCode": "id119sres119"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-03-06",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/sres/BILLS-119sres119is.xml"
        }
      ],
      "type": "IS"
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
      "title": "A resolution memorializing those lost to the COVID-19 pandemic.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-12T02:19:09Z"
    },
    {
      "title": "A resolution memorializing those lost to the COVID-19 pandemic.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-03-07T11:56:16Z"
    }
  ]
}
```
