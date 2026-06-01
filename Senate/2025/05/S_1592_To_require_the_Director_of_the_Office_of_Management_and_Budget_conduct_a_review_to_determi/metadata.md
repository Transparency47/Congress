# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/1592?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/1592
- Title: Safe and Smart Federal Purchasing Act
- Congress: 119
- Bill type: S
- Bill number: 1592
- Origin chamber: Senate
- Introduced date: 2025-05-05
- Update date: 2026-05-20T13:06:01Z
- Update date including text: 2026-05-20T13:06:01Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-05-05: Introduced in Senate
- 2025-05-05 - IntroReferral: Introduced in Senate
- 2025-05-05 - IntroReferral: Read twice and referred to the Committee on Homeland Security and Governmental Affairs.
- Latest action: 2025-05-05: Introduced in Senate

## Actions

- 2025-05-05 - IntroReferral: Introduced in Senate
- 2025-05-05 - IntroReferral: Read twice and referred to the Committee on Homeland Security and Governmental Affairs.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-05-05",
    "latestAction": {
      "actionDate": "2025-05-05",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/1592",
    "number": "1592",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Government Operations and Politics"
    },
    "sponsors": [
      {
        "bioguideId": "R000618",
        "district": "",
        "firstName": "Pete",
        "fullName": "Sen. Ricketts, Pete [R-NE]",
        "lastName": "Ricketts",
        "party": "R",
        "state": "NE"
      }
    ],
    "title": "Safe and Smart Federal Purchasing Act",
    "type": "S",
    "updateDate": "2026-05-20T13:06:01Z",
    "updateDateIncludingText": "2026-05-20T13:06:01Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-05-05",
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
      "actionDate": "2025-05-05",
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
          "date": "2025-05-05T19:44:56Z",
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
      "bioguideId": "K000394",
      "firstName": "Andy",
      "fullName": "Sen. Kim, Andy [D-NJ]",
      "isOriginalCosponsor": "True",
      "lastName": "Kim",
      "party": "D",
      "sponsorshipDate": "2025-05-05",
      "state": "NJ"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1592is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 1592\nIN THE SENATE OF THE UNITED STATES\nMay 5, 2025 Mr. Ricketts (for himself and Mr. Kim ) introduced the following bill; which was read twice and referred to the Committee on Homeland Security and Governmental Affairs\nA BILL\nTo require the Director of the Office of Management and Budget conduct a review to determine the impact of the lowest price technically acceptable source selection process on national security, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Safe and Smart Federal Purchasing Act .\n#### 2. Review to determine the impact of the lowest price technically acceptable source selection process on national security\n##### (a) Review\nThe Director shall review the procurement management practices of Defense and Civilian agencies to determine whether the provisions of section 15.101\u20132 of the Federal Acquisition Regulation have created any national security risk.\n##### (b) Report\nNot later than 180 days after the enactment of this Act, the Director shall submit a report on the results of the review under subsection (a) to\u2014\n**(1)**\nthe Committee on Oversight and Government Reform of the House of Representatives; and\n**(2)**\nthe Committee on Homeland Security and Governmental Affairs of the Senate.\n##### (c) Definitions\nIn this section:\n**(1) Defense and Civilian Agency**\nThe term Defense and Civilian agency has the meaning given the term agency in section 133 of title 41, United States Code.\n**(2) Director**\nThe term Director means the Director of the Office of Management and Budget.",
      "versionDate": "2025-05-05",
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
        "actionDate": "2025-03-04",
        "text": "Received in the Senate and Read twice and referred to the Committee on Homeland Security and Governmental Affairs."
      },
      "number": "856",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Safe and Smart Federal Purchasing Act",
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
            "name": "Congressional oversight",
            "updateDate": "2026-04-27T17:44:16Z"
          },
          {
            "name": "Government information and archives",
            "updateDate": "2026-04-27T17:44:16Z"
          },
          {
            "name": "Public contracts and procurement",
            "updateDate": "2026-04-27T17:44:16Z"
          }
        ]
      },
      "policyArea": {
        "name": "Government Operations and Politics",
        "updateDate": "2025-06-04T15:36:01Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-05-05",
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
          "measure-id": "id119s1592",
          "measure-number": "1592",
          "measure-type": "s",
          "orig-publish-date": "2025-05-05",
          "originChamber": "SENATE",
          "update-date": "2026-05-20"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "SENATE",
            "summary-id": "id119s1592v00",
            "update-date": "2026-05-20"
          },
          "action-date": "2025-05-05",
          "action-desc": "Introduced in Senate",
          "summary-text": "<p><strong>Safe and Smart Federal Purchasing Act</strong></p><p>This bill requires the Office of Management and Budget (OMB) to evaluate the procurement activities of federal agencies to determine whether provisions of the Federal Acquisition Regulation related to the lowest price technically acceptable source selection process have created any national security risk and report to Congress.</p>"
        },
        "title": "Safe and Smart Federal Purchasing Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/s/BILLSUM-119s1592.xml",
    "summary": {
      "actionDate": "2025-05-05",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Safe and Smart Federal Purchasing Act</strong></p><p>This bill requires the Office of Management and Budget (OMB) to evaluate the procurement activities of federal agencies to determine whether provisions of the Federal Acquisition Regulation related to the lowest price technically acceptable source selection process have created any national security risk and report to Congress.</p>",
      "updateDate": "2026-05-20",
      "versionCode": "id119s1592"
    },
    "title": "Safe and Smart Federal Purchasing Act"
  },
  "summaries": [
    {
      "actionDate": "2025-05-05",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Safe and Smart Federal Purchasing Act</strong></p><p>This bill requires the Office of Management and Budget (OMB) to evaluate the procurement activities of federal agencies to determine whether provisions of the Federal Acquisition Regulation related to the lowest price technically acceptable source selection process have created any national security risk and report to Congress.</p>",
      "updateDate": "2026-05-20",
      "versionCode": "id119s1592"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-05-05",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1592is.xml"
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
      "title": "Safe and Smart Federal Purchasing Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-05-28T04:08:23Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Safe and Smart Federal Purchasing Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-05-28T04:08:19Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to require the Director of the Office of Management and Budget conduct a review to determine the impact of the lowest price technically acceptable source selection process on national security, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-05-28T04:03:47Z"
    }
  ]
}
```
