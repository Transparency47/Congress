# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/603?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/603
- Title: A bill to designate the General George C. Marshall House in the Commonwealth of Virginia, as an affiliated area of the National Park System, and for other purposes.
- Congress: 119
- Bill type: S
- Bill number: 603
- Origin chamber: Senate
- Introduced date: 2025-02-13
- Update date: 2026-05-28T20:03:32Z
- Update date including text: 2026-05-28T20:03:32Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-02-13: Introduced in Senate
- 2025-02-13 - IntroReferral: Introduced in Senate
- 2025-02-13 - IntroReferral: Read twice and referred to the Committee on Energy and Natural Resources.
- 2026-05-20 - Floor: Message on Senate action sent to the House.
- 2026-05-20 - Floor: Passed Senate without amendment by Unanimous Consent. (consideration: CR S2387; text: CR S2387)
- 2026-05-20 - Floor: Passed/agreed to in Senate: Passed Senate without amendment by Unanimous Consent.
- 2026-05-20 - Discharge: Senate Committee on Energy and Natural Resources discharged by Unanimous Consent.
- 2026-05-20 - Committee: Senate Committee on Energy and Natural Resources discharged by Unanimous Consent.
- 2026-05-20 16:30:21 - Floor: Received in the House.
- 2026-05-20 16:38:45 - Floor: Held at the desk.
- Latest action: 2025-02-13: Introduced in Senate

## Actions

- 2025-02-13 - IntroReferral: Introduced in Senate
- 2025-02-13 - IntroReferral: Read twice and referred to the Committee on Energy and Natural Resources.
- 2026-05-20 - Floor: Message on Senate action sent to the House.
- 2026-05-20 - Floor: Passed Senate without amendment by Unanimous Consent. (consideration: CR S2387; text: CR S2387)
- 2026-05-20 - Floor: Passed/agreed to in Senate: Passed Senate without amendment by Unanimous Consent.
- 2026-05-20 - Discharge: Senate Committee on Energy and Natural Resources discharged by Unanimous Consent.
- 2026-05-20 - Committee: Senate Committee on Energy and Natural Resources discharged by Unanimous Consent.
- 2026-05-20 16:30:21 - Floor: Received in the House.
- 2026-05-20 16:38:45 - Floor: Held at the desk.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-02-13",
    "latestAction": {
      "actionDate": "2025-02-13",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/603",
    "number": "603",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Public Lands and Natural Resources"
    },
    "sponsors": [
      {
        "bioguideId": "K000384",
        "district": "",
        "firstName": "Timothy",
        "fullName": "Sen. Kaine, Tim [D-VA]",
        "lastName": "Kaine",
        "party": "D",
        "state": "VA"
      }
    ],
    "title": "A bill to designate the General George C. Marshall House in the Commonwealth of Virginia, as an affiliated area of the National Park System, and for other purposes.",
    "type": "S",
    "updateDate": "2026-05-28T20:03:32Z",
    "updateDateIncludingText": "2026-05-28T20:03:32Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H15000",
      "actionDate": "2026-05-20",
      "actionTime": "16:38:45",
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Held at the desk.",
      "type": "Floor"
    },
    {
      "actionCode": "H14000",
      "actionDate": "2026-05-20",
      "actionTime": "16:30:21",
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Received in the House.",
      "type": "Floor"
    },
    {
      "actionDate": "2026-05-20",
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Message on Senate action sent to the House.",
      "type": "Floor"
    },
    {
      "actionDate": "2026-05-20",
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Passed Senate without amendment by Unanimous Consent. (consideration: CR S2387; text: CR S2387)",
      "type": "Floor"
    },
    {
      "actionCode": "17000",
      "actionDate": "2026-05-20",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Passed/agreed to in Senate: Passed Senate without amendment by Unanimous Consent.",
      "type": "Floor"
    },
    {
      "actionDate": "2026-05-20",
      "committees": {
        "item": {
          "name": "Energy and Natural Resources Committee",
          "systemCode": "sseg00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Senate Committee on Energy and Natural Resources discharged by Unanimous Consent.",
      "type": "Discharge"
    },
    {
      "actionCode": "14500",
      "actionDate": "2026-05-20",
      "committees": {
        "item": {
          "name": "Energy and Natural Resources Committee",
          "systemCode": "sseg00"
        }
      },
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Senate Committee on Energy and Natural Resources discharged by Unanimous Consent.",
      "type": "Committee"
    },
    {
      "actionDate": "2025-02-13",
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
      "actionDate": "2025-02-13",
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
            "date": "2026-05-20T16:16:55Z",
            "name": "Discharged From"
          },
          {
            "date": "2025-02-13T20:41:50Z",
            "name": "Referred To"
          }
        ]
      },
      "chamber": "Senate",
      "name": "Energy and Natural Resources Committee",
      "systemCode": "sseg00",
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
      "bioguideId": "W000805",
      "firstName": "Mark",
      "fullName": "Sen. Warner, Mark R. [D-VA]",
      "isOriginalCosponsor": "True",
      "lastName": "Warner",
      "middleName": "R.",
      "party": "D",
      "sponsorshipDate": "2025-02-13",
      "state": "VA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s603is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 603\nIN THE SENATE OF THE UNITED STATES\nFebruary 13, 2025 Mr. Kaine (for himself and Mr. Warner ) introduced the following bill; which was read twice and referred to the Committee on Energy and Natural Resources\nA BILL\nTo designate the General George C. Marshall House, in the Commonwealth of Virginia, as an affiliated area of the National Park System, and for other purposes.\n#### 1. Establishment of the General George C. Marshall House as an affiliated area\n##### (a) In general\nThe General George C. Marshall House in the Commonwealth of Virginia is established as an affiliated area of the National Park System (referred to in this section as the affiliated area ) to promote public appreciation of the significant historic contributions made by United States military leader and statesman George Catlett Marshall, Jr.\n##### (b) Description of affiliated area\nThe affiliated area shall consist of the area generally depicted as the General George C. Marshall House Property, Leesburg, Virginia on the map entitled General George C. Marshall House, Proposed Affiliated Area , numbered 999/189,974, and dated September 2023.\n##### (c) Administration\nThe affiliated area shall be managed in a manner consistent with\u2014\n**(1)**\nthis section; and\n**(2)**\nany law generally applicable to units of the National Park System.\n##### (d) Management entity\nThe George C. Marshall International Center shall be the management entity for the affiliated area.\n##### (e) Agreements\nThe Secretary of the Interior (referred to in this section as the Secretary )\u2014\n**(1)**\nmay provide technical assistance and enter into cooperative agreements with the management entity designated by subsection (d) for the purpose of providing financial assistance for the marketing, marking, interpretation, and preservation of the affiliated area; and\n**(2)**\nshall enter into an agreement with the management entity designated by subsection (d) that describes the roles and responsibilities for the management of the affiliated area consistent with the policies and standards that apply to units of the National Park System.\n##### (f) Limited role of the secretary\nNothing in this section authorizes the Secretary\u2014\n**(1)**\nto acquire property at the affiliated area; or\n**(2)**\nto assume overall financial responsibility for the operation, maintenance, or management of the affiliated area.",
      "versionDate": "2025-02-13",
      "versionType": "Introduced in Senate"
    },
    {
      "fetchError": null,
      "sourceFormat": "Formatted XML",
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s603es.xml",
      "text": "119th CONGRESS\n2d Session\nS. 603\nIN THE SENATE OF THE UNITED STATES\nAN ACT\nTo designate the General George C. Marshall House, in the Commonwealth of Virginia, as an affiliated area of the National Park System, and for other purposes.\n#### 1. Establishment of the General George C. Marshall House as an affiliated area\n##### (a) In general\nThe General George C. Marshall House in the Commonwealth of Virginia is established as an affiliated area of the National Park System (referred to in this section as the affiliated area ) to promote public appreciation of the significant historic contributions made by United States military leader and statesman George Catlett Marshall, Jr.\n##### (b) Description of affiliated area\nThe affiliated area shall consist of the area generally depicted as the General George C. Marshall House Property, Leesburg, Virginia on the map entitled General George C. Marshall House, Proposed Affiliated Area , numbered 999/189,974, and dated September 2023.\n##### (c) Administration\nThe affiliated area shall be managed in a manner consistent with\u2014\n**(1)**\nthis section; and\n**(2)**\nany law generally applicable to units of the National Park System.\n##### (d) Management entity\nThe George C. Marshall International Center shall be the management entity for the affiliated area.\n##### (e) Agreements\nThe Secretary of the Interior (referred to in this section as the Secretary )\u2014\n**(1)**\nmay provide technical assistance and enter into cooperative agreements with the management entity designated by subsection (d) for the purpose of providing financial assistance for the marketing, marking, interpretation, and preservation of the affiliated area; and\n**(2)**\nshall enter into an agreement with the management entity designated by subsection (d) that describes the roles and responsibilities for the management of the affiliated area consistent with the policies and standards that apply to units of the National Park System.\n##### (f) Limited role of the secretary\nNothing in this section authorizes the Secretary\u2014\n**(1)**\nto acquire property at the affiliated area; or\n**(2)**\nto assume overall financial responsibility for the operation, maintenance, or management of the affiliated area.",
      "versionDate": "",
      "versionType": "Engrossed in Senate"
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
            "name": "Geography and mapping",
            "updateDate": "2026-05-22T18:22:49Z"
          },
          {
            "name": "Historic sites and heritage areas",
            "updateDate": "2026-05-22T18:22:49Z"
          },
          {
            "name": "Military history",
            "updateDate": "2026-05-22T18:22:49Z"
          },
          {
            "name": "Parks, recreation areas, trails",
            "updateDate": "2026-05-22T18:22:49Z"
          },
          {
            "name": "U.S. history",
            "updateDate": "2026-05-22T18:22:49Z"
          },
          {
            "name": "Virginia",
            "updateDate": "2026-05-22T18:22:49Z"
          }
        ]
      },
      "policyArea": {
        "name": "Public Lands and Natural Resources",
        "updateDate": "2026-05-28T20:03:32Z"
      }
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-02-13",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s603is.xml"
        }
      ],
      "type": "Introduced in Senate"
    },
    {
      "date": "",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s603es.xml"
        }
      ],
      "type": "Engrossed in Senate"
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
      "title": "A bill to designate the General George C. Marshall House in the Commonwealth of Virginia, as an affiliated area of the National Park System, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-14T03:18:22Z"
    },
    {
      "title": "A bill to designate the General George C. Marshall House in the Commonwealth of Virginia, as an affiliated area of the National Park System, and for other purposes.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-02-14T11:56:14Z"
    }
  ]
}
```
