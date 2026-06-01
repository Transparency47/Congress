# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/2369?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/2369
- Title: Francis G. Newlands Memorial Removal Act
- Congress: 119
- Bill type: S
- Bill number: 2369
- Origin chamber: Senate
- Introduced date: 2025-07-22
- Update date: 2026-04-06T19:33:51Z
- Update date including text: 2026-04-06T19:33:51Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-07-22: Introduced in Senate
- 2025-07-22 - IntroReferral: Introduced in Senate
- 2025-07-22 - IntroReferral: Read twice and referred to the Committee on Energy and Natural Resources.
- 2025-12-09 - Committee: Committee on Energy and Natural Resources Subcommittee on National Parks. Hearings held.
- Latest action: 2025-07-22: Introduced in Senate

## Actions

- 2025-07-22 - IntroReferral: Introduced in Senate
- 2025-07-22 - IntroReferral: Read twice and referred to the Committee on Energy and Natural Resources.
- 2025-12-09 - Committee: Committee on Energy and Natural Resources Subcommittee on National Parks. Hearings held.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-07-22",
    "latestAction": {
      "actionDate": "2025-07-22",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/2369",
    "number": "2369",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Public Lands and Natural Resources"
    },
    "sponsors": [
      {
        "bioguideId": "V000128",
        "district": "",
        "firstName": "Chris",
        "fullName": "Sen. Van Hollen, Chris [D-MD]",
        "lastName": "Van Hollen",
        "party": "D",
        "state": "MD"
      }
    ],
    "title": "Francis G. Newlands Memorial Removal Act",
    "type": "S",
    "updateDate": "2026-04-06T19:33:51Z",
    "updateDateIncludingText": "2026-04-06T19:33:51Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-12-09",
      "committees": {
        "item": {
          "name": "National Parks Subcommittee",
          "systemCode": "sseg04"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Committee on Energy and Natural Resources Subcommittee on National Parks. Hearings held.",
      "type": "Committee"
    },
    {
      "actionDate": "2025-07-22",
      "committees": {
        "item": {
          "name": "Energy and Natural Resources Committee",
          "systemCode": "sseg00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Energy and Natural Resources.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-07-22",
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
          "date": "2025-07-22T15:56:41Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Energy and Natural Resources Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": {
              "date": "2025-12-09T18:13:17Z",
              "name": "Hearings By (subcommittee)"
            }
          },
          "name": "National Parks Subcommittee",
          "systemCode": "sseg04"
        }
      },
      "systemCode": "sseg00",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2369is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 2369\nIN THE SENATE OF THE UNITED STATES\nJuly 22, 2025 Mr. Van Hollen introduced the following bill; which was read twice and referred to the Committee on Energy and Natural Resources\nA BILL\nTo direct the Secretary of the Interior to remove or permanently conceal the name of Francis Newlands on the grounds of the memorial fountain located at Chevy Chase Circle in the District of Columbia, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Francis G. Newlands Memorial Removal Act .\n#### 2. Removal of Plaque and Concrete from Memorial Fountain Grounds\n##### (a) In general\nThe Secretary of the Interior shall\u2014\n**(1)**\nremove the brass plaque bearing the name Senator Francis G. Newlands from the grounds of the memorial fountain;\n**(2)**\nremove from the south end of the memorial fountain\u2019s face, the stone, tablet-like projection bearing the name of Francis Griffith Newlands and a related inscription;\n**(3)**\nremove or permanently conceal the name Newlands carved into the upper face of the memorial fountain\u2019s coping stones; and\n**(4)**\noffer the items removed pursuant to paragraphs (1), (2), and (3) to the descendants of Francis Griffith Newlands for a period of 60 days, and if not claimed within that period, direct the items removed pursuant to paragraphs (1), (2), and (3) to be maintained by the National Park Service as Federal property and accessioned into the Rock Creek Park museum collection.\n##### (b) Memorial fountain\nFor the purposes of this section, the term memorial fountain means the memorial fountain located at Chevy Chase Circle, Connecticut Avenue and Western Avenue NW, in the District of Columbia.",
      "versionDate": "2025-07-22",
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
        "actionDate": "2025-07-22",
        "text": "Referred to the House Committee on Natural Resources."
      },
      "number": "4608",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Francis G. Newlands Memorial Removal Act",
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
            "name": "District of Columbia",
            "updateDate": "2025-12-17T16:59:20Z"
          },
          {
            "name": "Members of Congress",
            "updateDate": "2025-12-17T16:59:20Z"
          },
          {
            "name": "Monuments and memorials",
            "updateDate": "2025-12-17T16:59:20Z"
          },
          {
            "name": "Museums, exhibitions, cultural centers",
            "updateDate": "2025-12-17T16:59:20Z"
          },
          {
            "name": "Racial and ethnic relations",
            "updateDate": "2025-12-17T16:59:20Z"
          },
          {
            "name": "Senate",
            "updateDate": "2025-12-17T16:59:20Z"
          }
        ]
      },
      "policyArea": {
        "name": "Public Lands and Natural Resources",
        "updateDate": "2025-08-01T15:14:40Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-07-22",
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
          "measure-id": "id119s2369",
          "measure-number": "2369",
          "measure-type": "s",
          "orig-publish-date": "2025-07-22",
          "originChamber": "SENATE",
          "update-date": "2026-04-06"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "SENATE",
            "summary-id": "id119s2369v00",
            "update-date": "2026-04-06"
          },
          "action-date": "2025-07-22",
          "action-desc": "Introduced in Senate",
          "summary-text": "<p><strong>Francis G. Newlands Memorial Removal Act </strong></p><p>This bill directs the Department of the Interior to remove or permanently conceal the name of Francis Newlands on the grounds of the memorial fountain located at Chevy Chase Circle in the District of Columbia and take other specified actions.</p><p>Specifically, Interior must</p><ul><li>remove the brass plaque bearing the name <em>Senator Francis G. Newlands</em> from the grounds of the memorial fountain located at Chevy Chase Circle in the District;</li><li>remove from the south end of the memorial fountain's face, the stone, tablet-like projection bearing the name of <em>Francis Griffith Newlands</em> and a related inscription;</li><li>remove or permanently conceal the name <em>Newlands </em>carved into the upper face of the memorial fountain's coping stones; and</li><li>offer the items removed to the descendants of Francis Griffith Newlands for a 60-day period, and if not claimed within that period, direct the removed items to be maintained by the National Park Service as federal property and accessioned into the Rock Creek Park museum collection.</li></ul>"
        },
        "title": "Francis G. Newlands Memorial Removal Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/s/BILLSUM-119s2369.xml",
    "summary": {
      "actionDate": "2025-07-22",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Francis G. Newlands Memorial Removal Act </strong></p><p>This bill directs the Department of the Interior to remove or permanently conceal the name of Francis Newlands on the grounds of the memorial fountain located at Chevy Chase Circle in the District of Columbia and take other specified actions.</p><p>Specifically, Interior must</p><ul><li>remove the brass plaque bearing the name <em>Senator Francis G. Newlands</em> from the grounds of the memorial fountain located at Chevy Chase Circle in the District;</li><li>remove from the south end of the memorial fountain's face, the stone, tablet-like projection bearing the name of <em>Francis Griffith Newlands</em> and a related inscription;</li><li>remove or permanently conceal the name <em>Newlands </em>carved into the upper face of the memorial fountain's coping stones; and</li><li>offer the items removed to the descendants of Francis Griffith Newlands for a 60-day period, and if not claimed within that period, direct the removed items to be maintained by the National Park Service as federal property and accessioned into the Rock Creek Park museum collection.</li></ul>",
      "updateDate": "2026-04-06",
      "versionCode": "id119s2369"
    },
    "title": "Francis G. Newlands Memorial Removal Act"
  },
  "summaries": [
    {
      "actionDate": "2025-07-22",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Francis G. Newlands Memorial Removal Act </strong></p><p>This bill directs the Department of the Interior to remove or permanently conceal the name of Francis Newlands on the grounds of the memorial fountain located at Chevy Chase Circle in the District of Columbia and take other specified actions.</p><p>Specifically, Interior must</p><ul><li>remove the brass plaque bearing the name <em>Senator Francis G. Newlands</em> from the grounds of the memorial fountain located at Chevy Chase Circle in the District;</li><li>remove from the south end of the memorial fountain's face, the stone, tablet-like projection bearing the name of <em>Francis Griffith Newlands</em> and a related inscription;</li><li>remove or permanently conceal the name <em>Newlands </em>carved into the upper face of the memorial fountain's coping stones; and</li><li>offer the items removed to the descendants of Francis Griffith Newlands for a 60-day period, and if not claimed within that period, direct the removed items to be maintained by the National Park Service as federal property and accessioned into the Rock Creek Park museum collection.</li></ul>",
      "updateDate": "2026-04-06",
      "versionCode": "id119s2369"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-07-22",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2369is.xml"
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
      "title": "Francis G. Newlands Memorial Removal Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-12-10T12:03:19Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Francis G. Newlands Memorial Removal Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-08-01T04:08:21Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to direct the Secretary of the Interior to remove or permanently conceal the name of Francis Newlands on the grounds of the memorial fountain located at Chevy Chase Circle in the District of Columbia, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-08-01T04:03:23Z"
    }
  ]
}
```
