# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/505?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/hr/505
- Title: To impose additional duties on imports of goods into the United States.
- Congress: 119
- Bill type: HR
- Bill number: 505
- Origin chamber: House
- Introduced date: 2025-01-16
- Update date: 2025-04-09T18:04:39Z
- Update date including text: 2025-04-09T18:04:39Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-01-16: Introduced in House
- 2025-01-16 - IntroReferral: Introduced in House
- 2025-01-16 - IntroReferral: Introduced in House
- 2025-01-16 - IntroReferral: Referred to the House Committee on Ways and Means.
- Latest action: 2025-01-16: Introduced in House

## Actions

- 2025-01-16 - IntroReferral: Introduced in House
- 2025-01-16 - IntroReferral: Introduced in House
- 2025-01-16 - IntroReferral: Referred to the House Committee on Ways and Means.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-01-16",
    "latestAction": {
      "actionDate": "2025-01-16",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/hr/505",
    "number": "505",
    "originChamber": "House",
    "policyArea": {
      "name": "Foreign Trade and International Finance"
    },
    "sponsors": [
      {
        "bioguideId": "G000592",
        "district": "2",
        "firstName": "Jared",
        "fullName": "Rep. Golden, Jared F. [D-ME-2]",
        "lastName": "Golden",
        "party": "D",
        "state": "ME"
      }
    ],
    "title": "To impose additional duties on imports of goods into the United States.",
    "type": "HR",
    "updateDate": "2025-04-09T18:04:39Z",
    "updateDateIncludingText": "2025-04-09T18:04:39Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-01-16",
      "committees": {
        "item": {
          "name": "Ways and Means Committee",
          "systemCode": "hswm00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Ways and Means.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-01-16",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-01-16",
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
          "date": "2025-01-16T14:01:05Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Ways and Means Committee",
      "systemCode": "hswm00",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr505ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 505\nIN THE HOUSE OF REPRESENTATIVES\nJanuary 16, 2025 Mr. Golden of Maine introduced the following bill; which was referred to the Committee on Ways and Means\nA BILL\nTo impose additional duties on imports of goods into the United States.\n#### 1. Imposition of additional duties on imports of goods into the United States\n##### (a) In general\nThe President shall\u2014\n**(1)**\nimpose a duty on imports of any good into the United States in an amount equal to 10 percent ad valorem of the good for each calendar year beginning on or after the date of the enactment of this Act; and\n**(2)**\nfor each calendar year beginning after the calendar year referred to in paragraph (1)\u2014\n**(A)**\nif the United States has a deficit in the trade of goods and services generally for the immediately preceding calendar year, increase the duty imposed under paragraph (1) on such good by an additional amount equal to 5 percent ad valorem of the good; or\n**(B)**\nif the United States has a balance or surplus in the trade of goods and services generally for the immediately preceding calendar year, decrease the duty imposed under paragraph (1) on such good by an amount equal to 5 percent ad valorem of the good for each calendar year beginning after the calendar year referred to in paragraph (1), except that the duty imposed under paragraph (1) on such good shall not be reduced below $0.\n##### (b) Duties To be considered additional duties\nThe duty required by subsection (a) with respect to a good is in addition to any other duty imposed by law with respect to the good.",
      "versionDate": "2025-01-16",
      "versionType": "Introduced in House"
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
        "item": {
          "name": "Tariffs",
          "updateDate": "2025-03-10T14:16:57Z"
        }
      },
      "policyArea": {
        "name": "Foreign Trade and International Finance",
        "updateDate": "2025-02-28T19:21:15Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-01-16",
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
          "measure-id": "id119hr505",
          "measure-number": "505",
          "measure-type": "hr",
          "orig-publish-date": "2025-01-16",
          "originChamber": "HOUSE",
          "update-date": "2025-04-09"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr505v00",
            "update-date": "2025-04-09"
          },
          "action-date": "2025-01-16",
          "action-desc": "Introduced in House",
          "summary-text": "<p>This bill directs the President to impose additional duties (i.e., tariffs) on all imports entering the United States.</p><p>Specifically, the President must impose an additional 10% duty on all imports entering the United States.\u00a0</p><p>Additionally, the bill directs the President to increase this duty on imported goods by an additional 5% if the United States has a deficit in the trade of goods and services generally for the immediately preceding calendar year. If the United States has a balance or surplus in the trade of goods and services, then the President must decrease the duty by 5% (except the imposed duty shall not be reduced below $0).</p>"
        },
        "title": "To impose additional duties on imports of goods into the United States."
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr505.xml",
    "summary": {
      "actionDate": "2025-01-16",
      "actionDesc": "Introduced in House",
      "text": "<p>This bill directs the President to impose additional duties (i.e., tariffs) on all imports entering the United States.</p><p>Specifically, the President must impose an additional 10% duty on all imports entering the United States.\u00a0</p><p>Additionally, the bill directs the President to increase this duty on imported goods by an additional 5% if the United States has a deficit in the trade of goods and services generally for the immediately preceding calendar year. If the United States has a balance or surplus in the trade of goods and services, then the President must decrease the duty by 5% (except the imposed duty shall not be reduced below $0).</p>",
      "updateDate": "2025-04-09",
      "versionCode": "id119hr505"
    },
    "title": "To impose additional duties on imports of goods into the United States."
  },
  "summaries": [
    {
      "actionDate": "2025-01-16",
      "actionDesc": "Introduced in House",
      "text": "<p>This bill directs the President to impose additional duties (i.e., tariffs) on all imports entering the United States.</p><p>Specifically, the President must impose an additional 10% duty on all imports entering the United States.\u00a0</p><p>Additionally, the bill directs the President to increase this duty on imported goods by an additional 5% if the United States has a deficit in the trade of goods and services generally for the immediately preceding calendar year. If the United States has a balance or surplus in the trade of goods and services, then the President must decrease the duty by 5% (except the imposed duty shall not be reduced below $0).</p>",
      "updateDate": "2025-04-09",
      "versionCode": "id119hr505"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-01-16",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr505ih.xml"
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
      "title": "To impose additional duties on imports of goods into the United States.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-02-13T05:18:19Z"
    },
    {
      "title": "To impose additional duties on imports of goods into the United States.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-01-17T09:05:54Z"
    }
  ]
}
```
