# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/1630?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/1630
- Title: To allow States to elect to observe year-round daylight saving time, and for other purposes.
- Congress: 119
- Bill type: HR
- Bill number: 1630
- Origin chamber: House
- Introduced date: 2025-02-26
- Update date: 2025-12-05T21:42:35Z
- Update date including text: 2025-12-05T21:42:35Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-02-26: Introduced in House
- 2025-02-26 - IntroReferral: Introduced in House
- 2025-02-26 - IntroReferral: Introduced in House
- 2025-02-26 - IntroReferral: Referred to the House Committee on Energy and Commerce.
- Latest action: 2025-02-26: Introduced in House

## Actions

- 2025-02-26 - IntroReferral: Introduced in House
- 2025-02-26 - IntroReferral: Introduced in House
- 2025-02-26 - IntroReferral: Referred to the House Committee on Energy and Commerce.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-02-26",
    "latestAction": {
      "actionDate": "2025-02-26",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/1630",
    "number": "1630",
    "originChamber": "House",
    "policyArea": {
      "name": "Science, Technology, Communications"
    },
    "sponsors": [
      {
        "bioguideId": "R000575",
        "district": "3",
        "firstName": "Mike",
        "fullName": "Rep. Rogers, Mike D. [R-AL-3]",
        "lastName": "Rogers",
        "party": "R",
        "state": "AL"
      }
    ],
    "title": "To allow States to elect to observe year-round daylight saving time, and for other purposes.",
    "type": "HR",
    "updateDate": "2025-12-05T21:42:35Z",
    "updateDateIncludingText": "2025-12-05T21:42:35Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-02-26",
      "committees": {
        "item": {
          "name": "Energy and Commerce Committee",
          "systemCode": "hsif00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Energy and Commerce.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-02-26",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-02-26",
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
          "date": "2025-02-26T15:01:05Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Energy and Commerce Committee",
      "systemCode": "hsif00",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1630ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 1630\nIN THE HOUSE OF REPRESENTATIVES\nFebruary 26, 2025 Mr. Rogers of Alabama introduced the following bill; which was referred to the Committee on Energy and Commerce\nA BILL\nTo allow States to elect to observe year-round daylight saving time, and for other purposes.\n#### 1. Optional year-round application of daylight saving time\nSection 3(a) of the Uniform Time Act of 1966 ( 15 U.S.C. 260a ) is amended\u2014\n**(1)**\nby inserting or may by law apply the advancement of time described in this section for the duration of the year, after may by law exempt itself from the provisions of this subsection providing for the advancement of time, ;\n**(2)**\nby striking the standard time otherwise applicable during that period and inserting the same standard time ;\n**(3)**\nby striking may by law exempt either the entire State as provided in (1) or and inserting , by law, may apply either standard time provided for in paragraph (1) to the entire State, ; and\n**(4)**\nby inserting , or may apply the advancement of time for the duration of the year to the entire area of the State lying within any time zone before the period at the end.",
      "versionDate": "2025-02-26",
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
        "actionDate": "2025-01-09",
        "text": "Referred to the House Committee on Energy and Commerce."
      },
      "number": "300",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Daylight Act",
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
        "name": "Science, Technology, Communications",
        "updateDate": "2025-03-18T18:50:47Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-02-26",
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
          "measure-id": "id119hr1630",
          "measure-number": "1630",
          "measure-type": "hr",
          "orig-publish-date": "2025-02-26",
          "originChamber": "HOUSE",
          "update-date": "2025-05-07"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr1630v00",
            "update-date": "2025-05-07"
          },
          "action-date": "2025-02-26",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong></strong>This bill allows states to observe daylight saving time year-round. (States may already choose to observe standard time year-round.)</p>"
        },
        "title": "To allow States to elect to observe year-round daylight saving time, and for other purposes."
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr1630.xml",
    "summary": {
      "actionDate": "2025-02-26",
      "actionDesc": "Introduced in House",
      "text": "<p><strong></strong>This bill allows states to observe daylight saving time year-round. (States may already choose to observe standard time year-round.)</p>",
      "updateDate": "2025-05-07",
      "versionCode": "id119hr1630"
    },
    "title": "To allow States to elect to observe year-round daylight saving time, and for other purposes."
  },
  "summaries": [
    {
      "actionDate": "2025-02-26",
      "actionDesc": "Introduced in House",
      "text": "<p><strong></strong>This bill allows states to observe daylight saving time year-round. (States may already choose to observe standard time year-round.)</p>",
      "updateDate": "2025-05-07",
      "versionCode": "id119hr1630"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-02-26",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1630ih.xml"
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
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To allow States to elect to observe year-round daylight saving time, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-18T04:33:21Z"
    },
    {
      "title": "To allow States to elect to observe year-round daylight saving time, and for other purposes.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-02-27T09:06:25Z"
    }
  ]
}
```
