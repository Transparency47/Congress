# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/1142?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/1142
- Title: Scarper Ridge Golden Gate National Recreation Area Boundary Adjustment Act
- Congress: 119
- Bill type: S
- Bill number: 1142
- Origin chamber: Senate
- Introduced date: 2025-03-26
- Update date: 2026-04-13T02:07:57Z
- Update date including text: 2026-04-13T02:07:57Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-03-26: Introduced in Senate
- 2025-03-26 - IntroReferral: Introduced in Senate
- 2025-03-26 - IntroReferral: Read twice and referred to the Committee on Energy and Natural Resources. (Sponsor introductory remarks on measure: CR S1873-1874)
- 2026-03-25 - Floor: Passed Senate without amendment by Unanimous Consent. (consideration: CR S1605; text: CR S1605)
- 2026-03-25 - Floor: Passed/agreed to in Senate: Passed Senate without amendment by Unanimous Consent.
- 2026-03-25 - Discharge: Senate Committee on Energy and Natural Resources discharged by Unanimous Consent.
- 2026-03-25 - Committee: Senate Committee on Energy and Natural Resources discharged by Unanimous Consent.
- 2026-03-27 - Floor: Message on Senate action sent to the House.
- 2026-03-27 09:04:20 - Floor: Received in the House.
- 2026-03-27 09:09:14 - Floor: Held at the desk.
- Latest action: 2025-03-26: Introduced in Senate

## Actions

- 2025-03-26 - IntroReferral: Introduced in Senate
- 2025-03-26 - IntroReferral: Read twice and referred to the Committee on Energy and Natural Resources. (Sponsor introductory remarks on measure: CR S1873-1874)
- 2026-03-25 - Floor: Passed Senate without amendment by Unanimous Consent. (consideration: CR S1605; text: CR S1605)
- 2026-03-25 - Floor: Passed/agreed to in Senate: Passed Senate without amendment by Unanimous Consent.
- 2026-03-25 - Discharge: Senate Committee on Energy and Natural Resources discharged by Unanimous Consent.
- 2026-03-25 - Committee: Senate Committee on Energy and Natural Resources discharged by Unanimous Consent.
- 2026-03-27 - Floor: Message on Senate action sent to the House.
- 2026-03-27 09:04:20 - Floor: Received in the House.
- 2026-03-27 09:09:14 - Floor: Held at the desk.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-03-26",
    "latestAction": {
      "actionDate": "2025-03-26",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/1142",
    "number": "1142",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Public Lands and Natural Resources"
    },
    "sponsors": [
      {
        "bioguideId": "P000145",
        "district": "",
        "firstName": "Alex",
        "fullName": "Sen. Padilla, Alex [D-CA]",
        "lastName": "Padilla",
        "party": "D",
        "state": "CA"
      }
    ],
    "title": "Scarper Ridge Golden Gate National Recreation Area Boundary Adjustment Act",
    "type": "S",
    "updateDate": "2026-04-13T02:07:57Z",
    "updateDateIncludingText": "2026-04-13T02:07:57Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H15000",
      "actionDate": "2026-03-27",
      "actionTime": "09:09:14",
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Held at the desk.",
      "type": "Floor"
    },
    {
      "actionCode": "H14000",
      "actionDate": "2026-03-27",
      "actionTime": "09:04:20",
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Received in the House.",
      "type": "Floor"
    },
    {
      "actionDate": "2026-03-27",
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Message on Senate action sent to the House.",
      "type": "Floor"
    },
    {
      "actionDate": "2026-03-25",
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Passed Senate without amendment by Unanimous Consent. (consideration: CR S1605; text: CR S1605)",
      "type": "Floor"
    },
    {
      "actionCode": "17000",
      "actionDate": "2026-03-25",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Passed/agreed to in Senate: Passed Senate without amendment by Unanimous Consent.",
      "type": "Floor"
    },
    {
      "actionDate": "2026-03-25",
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
      "actionDate": "2026-03-25",
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
      "actionDate": "2025-03-26",
      "committees": {
        "item": {
          "name": "Energy and Natural Resources Committee",
          "systemCode": "sseg00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Energy and Natural Resources. (Sponsor introductory remarks on measure: CR S1873-1874)",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-03-26",
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
            "date": "2026-03-25T21:55:05Z",
            "name": "Discharged From"
          },
          {
            "date": "2025-03-26T16:36:17Z",
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
      "bioguideId": "S001150",
      "firstName": "Adam",
      "fullName": "Sen. Schiff, Adam B. [D-CA]",
      "isOriginalCosponsor": "False",
      "lastName": "Schiff",
      "middleName": "B.",
      "party": "D",
      "sponsorshipDate": "2025-03-31",
      "state": "CA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1142is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 1142\nIN THE SENATE OF THE UNITED STATES\nMarch 26, 2025 Mr. Padilla introduced the following bill; which was read twice and referred to the Committee on Energy and Natural Resources\nA BILL\nTo adjust the boundaries of the Golden Gate National Recreation Area to include the Scarper Ridge property.\n#### 1. Short title\nThis Act may be cited as the Scarper Ridge Golden Gate National Recreation Area Boundary Adjustment Act .\n#### 2. Scarper Ridge boundary adjustment\nSection 2(a)(2) of Public Law 92\u2013589 ( 16 U.S.C. 460bb\u20131(a)(2) ) is amended by adding at the end the following:\n(F) Land generally depicted as Proposed Boundary Addition on the map entitled Golden Gate National Recreation Area Proposed Boundary Addition , numbered 641/193973, and dated July 2024. .",
      "versionDate": "2025-03-26",
      "versionType": "Introduced in Senate"
    },
    {
      "fetchError": null,
      "sourceFormat": "Formatted XML",
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s1142es.xml",
      "text": "119th CONGRESS\n2d Session\nS. 1142\nIN THE SENATE OF THE UNITED STATES\nAN ACT\nTo adjust the boundaries of the Golden Gate National Recreation Area to include the Scarper Ridge property.\n#### 1. Short title\nThis Act may be cited as the Scarper Ridge Golden Gate National Recreation Area Boundary Adjustment Act .\n#### 2. Scarper Ridge boundary adjustment\nSection 2(a)(2) of Public Law 92\u2013589 ( 16 U.S.C. 460bb\u20131(a)(2) ) is amended by adding at the end the following:\n(F) Land generally depicted as Proposed Boundary Addition on the map entitled Golden Gate National Recreation Area Proposed Boundary Addition , numbered 641/193973, and dated July 2024. .",
      "versionDate": "",
      "versionType": "Engrossed in Senate"
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
        "actionDate": "2025-03-26",
        "text": "Referred to the House Committee on Natural Resources."
      },
      "number": "2371",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Scarper Ridge Golden Gate National Recreation Area Boundary Adjustment Act",
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
            "name": "California",
            "updateDate": "2026-03-03T18:47:23Z"
          },
          {
            "name": "Geography and mapping",
            "updateDate": "2026-03-03T18:47:23Z"
          },
          {
            "name": "Parks, recreation areas, trails",
            "updateDate": "2026-03-03T18:47:23Z"
          }
        ]
      },
      "policyArea": {
        "name": "Public Lands and Natural Resources",
        "updateDate": "2026-03-27T21:38:55Z"
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
      "date": "2025-03-26",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1142is.xml"
        }
      ],
      "type": "Introduced in Senate"
    },
    {
      "date": "",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s1142es.xml"
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
      "title": "Scarper Ridge Golden Gate National Recreation Area Boundary Adjustment Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-03-28T11:03:19Z"
    },
    {
      "billTextVersionCode": "ES",
      "billTextVersionName": "Engrossed in Senate",
      "chamberCode": "S",
      "chamberName": "Senate",
      "title": "Scarper Ridge Golden Gate National Recreation Area Boundary Adjustment Act",
      "titleType": "Short Title(s) as Passed Senate",
      "titleTypeCode": "105",
      "updateDate": "2026-03-26T06:38:22Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Scarper Ridge Golden Gate National Recreation Area Boundary Adjustment Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-04-11T02:23:15Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to adjust the boundaries of the Golden Gate National Recreation Area to include the Scarper Ridge property.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-04-11T02:18:19Z"
    }
  ]
}
```
