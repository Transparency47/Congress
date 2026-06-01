# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/4574?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/4574
- Title: District of Columbia Courts Home Rule Act
- Congress: 119
- Bill type: HR
- Bill number: 4574
- Origin chamber: House
- Introduced date: 2025-07-21
- Update date: 2026-04-03T16:01:16Z
- Update date including text: 2026-04-03T16:01:16Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-07-21: Introduced in House
- 2025-07-21 - IntroReferral: Introduced in House
- 2025-07-21 - IntroReferral: Introduced in House
- 2025-07-21 - IntroReferral: Referred to the House Committee on Oversight and Government Reform.
- 2025-07-21 - IntroReferral: Sponsor introductory remarks on measure. (CR E693)
- Latest action: 2025-07-21: Introduced in House

## Actions

- 2025-07-21 - IntroReferral: Introduced in House
- 2025-07-21 - IntroReferral: Introduced in House
- 2025-07-21 - IntroReferral: Referred to the House Committee on Oversight and Government Reform.
- 2025-07-21 - IntroReferral: Sponsor introductory remarks on measure. (CR E693)

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-07-21",
    "latestAction": {
      "actionDate": "2025-07-21",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/4574",
    "number": "4574",
    "originChamber": "House",
    "policyArea": {
      "name": "Law"
    },
    "sponsors": [
      {
        "bioguideId": "N000147",
        "district": "",
        "firstName": "Eleanor",
        "fullName": "Del. Norton, Eleanor Holmes [D-DC-At Large]",
        "lastName": "Norton",
        "party": "D",
        "state": "DC"
      }
    ],
    "title": "District of Columbia Courts Home Rule Act",
    "type": "HR",
    "updateDate": "2026-04-03T16:01:16Z",
    "updateDateIncludingText": "2026-04-03T16:01:16Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-07-21",
      "committees": {
        "item": {
          "name": "Oversight and Government Reform Committee",
          "systemCode": "hsgo00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Oversight and Government Reform.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-07-21",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "B00100",
      "actionDate": "2025-07-21",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Sponsor introductory remarks on measure. (CR E693)",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-07-21",
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
          "date": "2025-07-21T16:00:30Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Oversight and Government Reform Committee",
      "systemCode": "hsgo00",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr4574ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 4574\nIN THE HOUSE OF REPRESENTATIVES\nJuly 21, 2025 Ms. Norton introduced the following bill; which was referred to the Committee on Oversight and Government Reform\nA BILL\nTo amend the District of Columbia Home Rule Act to permit the Council of the District of Columbia to enact laws with respect to the organization and jurisdiction of the District of Columbia courts.\n#### 1. Short title\nThis Act may be cited as the District of Columbia Courts Home Rule Act .\n#### 2. Authority of Council of District of Columbia to enact laws with respect to District of Columbia Courts\nSection 602(a) of the District of Columbia Home Rule Act (sec. 1\u2013206.02(a), D.C. Official Code) is amended by striking paragraph (4).",
      "versionDate": "2025-07-21",
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
      "legislativeSubjects": "",
      "policyArea": {
        "name": "Law",
        "updateDate": "2025-07-31T20:45:15Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-07-21",
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
          "measure-id": "id119hr4574",
          "measure-number": "4574",
          "measure-type": "hr",
          "orig-publish-date": "2025-07-21",
          "originChamber": "HOUSE",
          "update-date": "2026-04-03"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr4574v00",
            "update-date": "2026-04-03"
          },
          "action-date": "2025-07-21",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>District of Columbia Courts Home Rule Act</strong></p><p>This bill authorizes the District of Columbia (DC) Council to pass legislation related to the organization and jurisdiction of the DC courts. Current law prohibits such legislation from being enacted.\u00a0</p>"
        },
        "title": "District of Columbia Courts Home Rule Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr4574.xml",
    "summary": {
      "actionDate": "2025-07-21",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>District of Columbia Courts Home Rule Act</strong></p><p>This bill authorizes the District of Columbia (DC) Council to pass legislation related to the organization and jurisdiction of the DC courts. Current law prohibits such legislation from being enacted.\u00a0</p>",
      "updateDate": "2026-04-03",
      "versionCode": "id119hr4574"
    },
    "title": "District of Columbia Courts Home Rule Act"
  },
  "summaries": [
    {
      "actionDate": "2025-07-21",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>District of Columbia Courts Home Rule Act</strong></p><p>This bill authorizes the District of Columbia (DC) Council to pass legislation related to the organization and jurisdiction of the DC courts. Current law prohibits such legislation from being enacted.\u00a0</p>",
      "updateDate": "2026-04-03",
      "versionCode": "id119hr4574"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-07-21",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr4574ih.xml"
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
      "title": "District of Columbia Courts Home Rule Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-07-31T04:43:19Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "District of Columbia Courts Home Rule Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-07-31T04:43:18Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the District of Columbia Home Rule Act to permit the Council of the District of Columbia to enact laws with respect to the organization and jurisdiction of the District of Columbia courts.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-07-31T04:33:36Z"
    }
  ]
}
```
