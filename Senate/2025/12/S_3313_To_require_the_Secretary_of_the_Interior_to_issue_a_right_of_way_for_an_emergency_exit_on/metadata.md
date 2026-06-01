# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/3313?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/3313
- Title: Wintergreen Emergency Egress Act
- Congress: 119
- Bill type: S
- Bill number: 3313
- Origin chamber: Senate
- Introduced date: 2025-12-02
- Update date: 2026-03-24T12:48:03Z
- Update date including text: 2026-03-24T12:48:03Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-12-02: Introduced in Senate
- 2025-12-02 - IntroReferral: Introduced in Senate
- 2025-12-02 - IntroReferral: Read twice and referred to the Committee on Energy and Natural Resources.
- Latest action: 2025-12-02: Introduced in Senate

## Actions

- 2025-12-02 - IntroReferral: Introduced in Senate
- 2025-12-02 - IntroReferral: Read twice and referred to the Committee on Energy and Natural Resources.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-12-02",
    "latestAction": {
      "actionDate": "2025-12-02",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/3313",
    "number": "3313",
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
    "title": "Wintergreen Emergency Egress Act",
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
      "actionDate": "2025-12-02",
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
      "actionDate": "2025-12-02",
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
          "date": "2025-12-02T21:56:37Z",
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
      "bioguideId": "W000805",
      "firstName": "Mark",
      "fullName": "Sen. Warner, Mark R. [D-VA]",
      "isOriginalCosponsor": "True",
      "lastName": "Warner",
      "middleName": "R.",
      "party": "D",
      "sponsorshipDate": "2025-12-02",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s3313is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 3313\nIN THE SENATE OF THE UNITED STATES\nDecember 2, 2025 Mr. Kaine (for himself and Mr. Warner ) introduced the following bill; which was read twice and referred to the Committee on Energy and Natural Resources\nA BILL\nTo require the Secretary of the Interior to issue a right-of-way for an emergency exit on certain National Park Service land in the State of Virginia, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Wintergreen Emergency Egress Act .\n#### 2. Right-of-way for emergency exit, Blue Ridge Parkway\nSection 2 of the Act of June 30, 1936 (49 Stat. 2041, chapter 883; 54 Stat. 250, chapter 277; 16 U.S.C. 460a\u20133 ), is amended\u2014\n**(1)**\nby striking Secretary of the Interior may issue and inserting the following: \u201cSecretary of the Interior\u2014\n(1) may issue ;\n**(2)**\nby striking the period at the end and inserting ; and ; and\n**(3)**\nby adding at the end the following:\n(2) shall issue the right-of-way generally depicted as Proposed Egress on the map entitled Proposed Wintergreen Emergency Egress Near Milepost 9.6 , numbered 601/194,694, and dated September 2024, if the Secretary certifies that\u2014 (A) an evaluation has been completed of alternatives to the right-of-way for egress that do not cross Federal land that includes evaluating whether existing trails can be converted to roads; (B) an analysis of expected fire ecology behavior in the event of a fire emergency has been completed with respect to the right-of-way; and (C) any required reviews with respect to the right-of-way have been completed in accordance with\u2014 (i) the National Environmental Policy Act of 1969 ( 42 U.S.C. 4321 et seq. ); and (ii) division A of subtitle III of title 54, United States Code. .",
      "versionDate": "2025-12-02",
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
        "actionDate": "2026-03-04",
        "text": "Received in the Senate and Read twice and referred to the Committee on Energy and Natural Resources."
      },
      "number": "6365",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Wintergreen Emergency Egress Act",
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
            "name": "Emergency planning and evacuation",
            "updateDate": "2026-01-14T19:55:24Z"
          },
          {
            "name": "Parks, recreation areas, trails",
            "updateDate": "2026-01-14T19:55:24Z"
          },
          {
            "name": "Virginia",
            "updateDate": "2026-01-14T19:55:24Z"
          }
        ]
      },
      "policyArea": {
        "name": "Public Lands and Natural Resources",
        "updateDate": "2026-01-07T17:19:47Z"
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
      "date": "2025-12-02",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s3313is.xml"
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
      "title": "Wintergreen Emergency Egress Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-12-23T05:38:17Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Wintergreen Emergency Egress Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-12-23T05:38:16Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to require the Secretary of the Interior to issue a right-of-way for an emergency exit on certain National Park Service land in the State of Virginia, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-12-23T05:33:17Z"
    }
  ]
}
```
