# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/815?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/815
- Title: A bill to designate the outdoor amphitheater at the Blue Ridge Music Center in Galax, Virginia, as the "Rick Boucher Amphitheater".
- Congress: 119
- Bill type: S
- Bill number: 815
- Origin chamber: Senate
- Introduced date: 2025-03-03
- Update date: 2026-04-13T19:20:27Z
- Update date including text: 2026-04-13T19:20:27Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-03-03: Introduced in Senate
- 2025-03-03 - IntroReferral: Introduced in Senate
- 2025-03-03 - IntroReferral: Read twice and referred to the Committee on Energy and Natural Resources.
- 2026-03-04 - Committee: Committee on Energy and Natural Resources. Ordered to be reported without amendment favorably.
- Latest action: 2025-03-03: Introduced in Senate

## Actions

- 2025-03-03 - IntroReferral: Introduced in Senate
- 2025-03-03 - IntroReferral: Read twice and referred to the Committee on Energy and Natural Resources.
- 2026-03-04 - Committee: Committee on Energy and Natural Resources. Ordered to be reported without amendment favorably.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-03-03",
    "latestAction": {
      "actionDate": "2025-03-03",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/815",
    "number": "815",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Arts, Culture, Religion"
    },
    "sponsors": [
      {
        "bioguideId": "W000805",
        "district": "",
        "firstName": "Mark",
        "fullName": "Sen. Warner, Mark R. [D-VA]",
        "lastName": "Warner",
        "party": "D",
        "state": "VA"
      }
    ],
    "title": "A bill to designate the outdoor amphitheater at the Blue Ridge Music Center in Galax, Virginia, as the \"Rick Boucher Amphitheater\".",
    "type": "S",
    "updateDate": "2026-04-13T19:20:27Z",
    "updateDateIncludingText": "2026-04-13T19:20:27Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-03-04",
      "committees": {
        "item": {
          "name": "Energy and Natural Resources Committee",
          "systemCode": "sseg00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Committee on Energy and Natural Resources. Ordered to be reported without amendment favorably.",
      "type": "Committee"
    },
    {
      "actionDate": "2025-03-03",
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
      "actionDate": "2025-03-03",
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
            "date": "2026-03-04T16:05:07Z",
            "name": "Markup By"
          },
          {
            "date": "2025-03-03T21:07:42Z",
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
      "bioguideId": "K000384",
      "firstName": "Timothy",
      "fullName": "Sen. Kaine, Tim [D-VA]",
      "isOriginalCosponsor": "True",
      "lastName": "Kaine",
      "middleName": "M.",
      "party": "D",
      "sponsorshipDate": "2025-03-03",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s815is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 815\nIN THE SENATE OF THE UNITED STATES\nMarch 3, 2025 Mr. Warner (for himself and Mr. Kaine ) introduced the following bill; which was read twice and referred to the Committee on Energy and Natural Resources\nA BILL\nTo designate the outdoor amphitheater at the Blue Ridge Music Center in Galax, Virginia, as the Rick Boucher Amphitheater .\n#### 1. Designation of the Rick Boucher Amphitheater\n##### (a) Designation\nThe outdoor amphitheater at the Blue Ridge Music Center, located at 700 Foothills Road, Galax, Virginia, a facility within the Blue Ridge Parkway, which is a unit of the National Park System, shall be known and designated as the Rick Boucher Amphitheater .\n##### (b) References\nAny reference in a law, map, regulation, document, paper, or other record of the United States to the outdoor amphitheater referred to in subsection (a) shall be deemed to be a reference to the Rick Boucher Amphitheater .",
      "versionDate": "2025-03-03",
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
        "name": "Arts, Culture, Religion",
        "updateDate": "2025-05-14T12:21:52Z"
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
      "date": "2025-03-03",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s815is.xml"
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
      "title": "A bill to designate the outdoor amphitheater at the Blue Ridge Music Center in Galax, Virginia, as the \"Rick Boucher Amphitheater\".",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-27T03:18:37Z"
    },
    {
      "title": "A bill to designate the outdoor amphitheater at the Blue Ridge Music Center in Galax, Virginia, as the \"Rick Boucher Amphitheater\".",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-03-04T11:56:20Z"
    }
  ]
}
```
