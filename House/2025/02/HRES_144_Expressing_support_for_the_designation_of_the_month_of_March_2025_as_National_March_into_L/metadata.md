# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hres/144?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/hres/144
- Title: Expressing support for the designation of the month of March 2025 as "National March into Literacy Month".
- Congress: 119
- Bill type: HRES
- Bill number: 144
- Origin chamber: House
- Introduced date: 2025-02-21
- Update date: 2025-07-21T19:44:15Z
- Update date including text: 2025-07-21T19:44:15Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-02-21: Introduced in House
- 2025-02-21 - IntroReferral: Referred to the House Committee on Education and Workforce.
- 2025-02-21 - Committee: Submitted in House
- Latest action: 2025-02-21: Submitted in House

## Actions

- 2025-02-21 - IntroReferral: Referred to the House Committee on Education and Workforce.
- 2025-02-21 - Committee: Submitted in House

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-02-21",
    "latestAction": {
      "actionDate": "2025-02-21",
      "text": "Submitted in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/hres/144",
    "number": "144",
    "originChamber": "House",
    "policyArea": {
      "name": "Education"
    },
    "sponsors": [
      {
        "bioguideId": "A000372",
        "district": "12",
        "firstName": "Rick",
        "fullName": "Rep. Allen, Rick W. [R-GA-12]",
        "lastName": "Allen",
        "party": "R",
        "state": "GA"
      }
    ],
    "title": "Expressing support for the designation of the month of March 2025 as \"National March into Literacy Month\".",
    "type": "HRES",
    "updateDate": "2025-07-21T19:44:15Z",
    "updateDateIncludingText": "2025-07-21T19:44:15Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-02-21",
      "committees": {
        "item": {
          "name": "Education and Workforce Committee",
          "systemCode": "hsed00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Education and Workforce.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "H12100",
      "actionDate": "2025-02-21",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Submitted in House",
      "type": "Committee"
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
          "date": "2025-02-21T20:32:00Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Education and Workforce Committee",
      "systemCode": "hsed00",
      "type": "Standing"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hres/BILLS-119hres144ih.xml",
      "text": "IV\n119th CONGRESS\n1st Session\nH. RES. 144\nIN THE HOUSE OF REPRESENTATIVES\nFebruary 21, 2025 Mr. Allen submitted the following resolution; which was referred to the Committee on Education and Workforce\nRESOLUTION\nExpressing support for the designation of the month of March 2025 as National March into Literacy Month .\nThat the House of Representatives\u2014\n**(1)**\nexpresses support for the designation of National March into Literacy Month ;\n**(2)**\napplauds students, parents, teachers, and school leaders from elementary and secondary education environments of all varieties for their persistence, achievements, dedication, and contributions to society in the United States;\n**(3)**\nencourages all parents and schools, during March into Literacy Month, to promote literacy; and\n**(4)**\nencourages the people of the United States to hold appropriate programs, events, and activities during National March into Literacy Month to raise public awareness of reading as an essential skill.",
      "versionDate": "2025-02-21",
      "versionType": "IH"
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
        "name": "Education",
        "updateDate": "2025-02-25T15:54:08Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-02-21",
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
          "measure-id": "id119hres144",
          "measure-number": "144",
          "measure-type": "hres",
          "orig-publish-date": "2025-02-21",
          "originChamber": "HOUSE",
          "update-date": "2025-03-31"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hres144v00",
            "update-date": "2025-03-31"
          },
          "action-date": "2025-02-21",
          "action-desc": "Introduced in House",
          "summary-text": "<p>This resolution expresses support for the designation of National March into Literacy Month.</p>"
        },
        "title": "Expressing support for the designation of the month of March 2025 as \"National March into Literacy Month\"."
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hres/BILLSUM-119hres144.xml",
    "summary": {
      "actionDate": "2025-02-21",
      "actionDesc": "Introduced in House",
      "text": "<p>This resolution expresses support for the designation of National March into Literacy Month.</p>",
      "updateDate": "2025-03-31",
      "versionCode": "id119hres144"
    },
    "title": "Expressing support for the designation of the month of March 2025 as \"National March into Literacy Month\"."
  },
  "summaries": [
    {
      "actionDate": "2025-02-21",
      "actionDesc": "Introduced in House",
      "text": "<p>This resolution expresses support for the designation of National March into Literacy Month.</p>",
      "updateDate": "2025-03-31",
      "versionCode": "id119hres144"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-02-21",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hres/BILLS-119hres144ih.xml"
        }
      ],
      "type": "IH"
    }
  ]
}
```

## API Data: titles

```json
{
  "titles": [
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Expressing support for the designation of the month of March 2025 as \"National March into Literacy Month\".",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-02-22T09:48:42Z"
    },
    {
      "title": "Expressing support for the designation of the month of March 2025 as \"National March into Literacy Month\".",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-02-22T09:06:18Z"
    }
  ]
}
```
