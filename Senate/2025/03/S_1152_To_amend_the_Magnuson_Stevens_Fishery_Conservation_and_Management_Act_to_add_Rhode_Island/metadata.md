# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/1152?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/1152
- Title: Rhode Island Fishermen's Fairness Act of 2025
- Congress: 119
- Bill type: S
- Bill number: 1152
- Origin chamber: Senate
- Introduced date: 2025-03-26
- Update date: 2025-12-05T21:37:10Z
- Update date including text: 2026-04-30T16:27:20Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-03-26: Introduced in Senate
- 2025-03-26 - IntroReferral: Introduced in Senate
- 2025-03-26 - IntroReferral: Read twice and referred to the Committee on Commerce, Science, and Transportation. (Sponsor introductory remarks on measure: CR S1874-1875)
- Latest action: 2025-03-26: Introduced in Senate

## Actions

- 2025-03-26 - IntroReferral: Introduced in Senate
- 2025-03-26 - IntroReferral: Read twice and referred to the Committee on Commerce, Science, and Transportation. (Sponsor introductory remarks on measure: CR S1874-1875)

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
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/1152",
    "number": "1152",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Public Lands and Natural Resources"
    },
    "sponsors": [
      {
        "bioguideId": "R000122",
        "district": "",
        "firstName": "John",
        "fullName": "Sen. Reed, Jack [D-RI]",
        "lastName": "Reed",
        "party": "D",
        "state": "RI"
      }
    ],
    "title": "Rhode Island Fishermen's Fairness Act of 2025",
    "type": "S",
    "updateDate": "2025-12-05T21:37:10Z",
    "updateDateIncludingText": "2026-04-30T16:27:20Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-03-26",
      "committees": {
        "item": {
          "name": "Commerce, Science, and Transportation Committee",
          "systemCode": "sscm00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Commerce, Science, and Transportation. (Sponsor introductory remarks on measure: CR S1874-1875)",
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
        "item": {
          "date": "2025-03-26T19:07:51Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Commerce, Science, and Transportation Committee",
      "systemCode": "sscm00",
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
      "bioguideId": "W000802",
      "firstName": "Sheldon",
      "fullName": "Sen. Whitehouse, Sheldon [D-RI]",
      "isOriginalCosponsor": "True",
      "lastName": "Whitehouse",
      "party": "D",
      "sponsorshipDate": "2025-03-26",
      "state": "RI"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1152is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 1152\nIN THE SENATE OF THE UNITED STATES\nMarch 26, 2025 Mr. Reed (for himself and Mr. Whitehouse ) introduced the following bill; which was read twice and referred to the Committee on Commerce, Science, and Transportation\nA BILL\nTo amend the Magnuson-Stevens Fishery Conservation and Management Act to add Rhode Island to the Mid-Atlantic Fishery Management Council, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Rhode Island Fishermen's Fairness Act of 2025 .\n#### 2. Addition of Rhode Island to the Mid-Atlantic Fishery Management Council\nSection 302(a)(1)(B) of the Magnuson-Stevens Fishery Conservation and Management Act ( 16 U.S.C. 1852(a)(1)(B) ) is amended\u2014\n**(1)**\nby inserting Rhode Island, after States of ;\n**(2)**\nby inserting Rhode Island, after except North Carolina, ;\n**(3)**\nby striking 21 and inserting 23 ; and\n**(4)**\nby striking 13 and inserting 14 .",
      "versionDate": "2025-03-26",
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
        "actionDate": "2025-03-26",
        "text": "Referred to the House Committee on Natural Resources."
      },
      "number": "2375",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Rhode Island Fishermen\u2019s Fairness Act of 2025",
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
            "name": "Atlantic Ocean",
            "updateDate": "2026-03-03T18:59:53Z"
          },
          {
            "name": "Marine and coastal resources, fisheries",
            "updateDate": "2026-03-03T18:59:53Z"
          },
          {
            "name": "Regional and metropolitan planning",
            "updateDate": "2026-03-03T18:59:53Z"
          },
          {
            "name": "Rhode Island",
            "updateDate": "2026-03-03T18:59:53Z"
          }
        ]
      },
      "policyArea": {
        "name": "Public Lands and Natural Resources",
        "updateDate": "2025-05-20T16:59:40Z"
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
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1152is.xml"
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
      "title": "Rhode Island Fishermen's Fairness Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-04-11T02:23:15Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Rhode Island Fishermen's Fairness Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-04-11T02:23:15Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend the Magnuson-Stevens Fishery Conservation and Management Act to add Rhode Island to the Mid-Atlantic Fishery Management Council, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-04-11T02:18:19Z"
    }
  ]
}
```
