# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/1016?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/1016
- Title: Vicksburg National Military Park Boundary Modification Act
- Congress: 119
- Bill type: S
- Bill number: 1016
- Origin chamber: Senate
- Introduced date: 2025-03-13
- Update date: 2026-03-24T12:48:03Z
- Update date including text: 2026-03-24T12:48:03Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, amendments, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-03-13: Introduced in Senate
- 2025-03-13 - IntroReferral: Introduced in Senate
- 2025-03-13 - IntroReferral: Read twice and referred to the Committee on Energy and Natural Resources.
- Latest action: 2025-03-13: Introduced in Senate

## Actions

- 2025-03-13 - IntroReferral: Introduced in Senate
- 2025-03-13 - IntroReferral: Read twice and referred to the Committee on Energy and Natural Resources.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-03-13",
    "latestAction": {
      "actionDate": "2025-03-13",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/1016",
    "number": "1016",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Public Lands and Natural Resources"
    },
    "sponsors": [
      {
        "bioguideId": "W000437",
        "district": "",
        "firstName": "Roger",
        "fullName": "Sen. Wicker, Roger F. [R-MS]",
        "lastName": "Wicker",
        "party": "R",
        "state": "MS"
      }
    ],
    "title": "Vicksburg National Military Park Boundary Modification Act",
    "type": "S",
    "updateDate": "2026-03-24T12:48:03Z",
    "updateDateIncludingText": "2026-03-24T12:48:03Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-03-13",
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
      "actionDate": "2025-03-13",
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

## API Data: amendments

```json
{
  "amendments": [
    {
      "amendment": {
        "actions": {
          "actions": {
            "item": [
              {
                "actionDate": "2025-07-31",
                "committees": {
                  "item": {
                    "name": "Energy and Natural Resources Committee",
                    "systemCode": "sseg00"
                  }
                },
                "sourceSystem": {
                  "code": "0",
                  "name": "Senate"
                },
                "text": "Referred to the Committee on Energy and Natural Resources.",
                "type": "IntroReferral"
              },
              {
                "actionCode": "Intro-S",
                "actionDate": "2025-07-31",
                "sourceSystem": {
                  "code": "9",
                  "name": "Library of Congress"
                },
                "type": "IntroReferral"
              },
              {
                "actionCode": "91000",
                "actionDate": "2025-07-31",
                "sourceSystem": {
                  "code": "9",
                  "name": "Library of Congress"
                },
                "text": "Senate amendment submitted",
                "type": "Floor"
              }
            ]
          },
          "count": "3"
        },
        "amendedBill": {
          "congress": "119",
          "number": "1016",
          "originChamber": "Senate",
          "originChamberCode": "S",
          "title": "Vicksburg National Military Park Boundary Modification Act",
          "type": "S",
          "updateDateIncludingText": "2026-03-24"
        },
        "chamber": "Senate",
        "congress": "119",
        "latestAction": {
          "actionDate": "2025-07-31",
          "text": "Referred to the Committee on Energy and Natural Resources."
        },
        "number": "3408",
        "purpose": "In the nature of a substitute.",
        "sponsors": {
          "item": {
            "bioguideId": "W000437",
            "firstName": "Roger",
            "fullName": "Sen. Wicker, Roger F. [R-MS]",
            "lastName": "Wicker",
            "middleName": "F.",
            "party": "R",
            "state": "MS"
          }
        },
        "submittedDate": "2025-07-31T04:00:00Z",
        "textVersions": {
          "count": "1"
        },
        "type": "SAMDT",
        "updateDate": "2025-07-31T23:09:32Z"
      }
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
          "date": "2025-03-13T15:43:15Z",
          "name": "Referred To"
        }
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
      "bioguideId": "H001079",
      "firstName": "Cindy",
      "fullName": "Sen. Hyde-Smith, Cindy [R-MS]",
      "isOriginalCosponsor": "True",
      "lastName": "Hyde-Smith",
      "party": "R",
      "sponsorshipDate": "2025-03-13",
      "state": "MS"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1016is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 1016\nIN THE SENATE OF THE UNITED STATES\nMarch 13, 2025 Mr. Wicker (for himself and Mrs. Hyde-Smith ) introduced the following bill; which was read twice and referred to the Committee on Energy and Natural Resources\nA BILL\nTo modify the boundary of the Vicksburg National Military Park in the State of Mississippi, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Vicksburg National Military Park Boundary Modification Act .\n#### 2. Vicksburg National Military Park conveyance and boundary modification\n##### (a) Conveyance\n**(1) In general**\nThe Secretary of the Interior (referred to in this Act as the Secretary ) shall convey to the State of Mississippi (referred to in this Act as the State ) without consideration subject to any terms and conditions that the Secretary determines to be appropriate, the Federal land described in subsection (b).\n**(2) Description of Federal land**\nThe Federal land referred to in subsection (a) is the following:\n**(A)**\nThe parcel of approximately 3.66 acres of National Park Service land within the boundary of Vicksburg National Military Park, as depicted on the map entitled VICK\u20132024\u201301 , to be used by the State as a welcome center or other public use.\n**(B)**\nThe approximately 6.48 acres of National Park Service land within the boundary of Vicksburg National Mark Park, as depicted on the map entitled VICK\u20132024\u201302 , to be used by the State as an interpretive center or a museum or other public use.\n##### (b) Boundary modification\nOn conveyance of a parcel of Federal land under subsection (a), the Secretary shall modify the boundary of the Vicksburg National Military Park to reflect the conveyance of the parcel of Federal land.",
      "versionDate": "2025-03-13",
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
      "legislativeSubjects": {
        "item": [
          {
            "name": "Mississippi",
            "updateDate": "2025-09-23T19:08:06Z"
          },
          {
            "name": "Parks, recreation areas, trails",
            "updateDate": "2025-09-23T19:08:06Z"
          }
        ]
      },
      "policyArea": {
        "name": "Public Lands and Natural Resources",
        "updateDate": "2025-05-12T18:28:01Z"
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
      "date": "2025-03-13",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1016is.xml"
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
      "title": "Vicksburg National Military Park Boundary Modification Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-03-28T11:23:20Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Vicksburg National Military Park Boundary Modification Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-28T11:23:18Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to modify the boundary of the Vicksburg National Military Park in the State of Mississippi, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-28T11:18:19Z"
    }
  ]
}
```
