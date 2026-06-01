# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/1712?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/1712
- Title: Criminal History Access Act of 2025
- Congress: 119
- Bill type: S
- Bill number: 1712
- Origin chamber: Senate
- Introduced date: 2025-05-12
- Update date: 2026-05-21T11:03:37Z
- Update date including text: 2026-05-21T11:03:37Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-05-12: Introduced in Senate
- 2025-05-12 - IntroReferral: Introduced in Senate
- 2025-05-12 - IntroReferral: Read twice and referred to the Committee on the Judiciary.
- Latest action: 2025-05-12: Introduced in Senate

## Actions

- 2025-05-12 - IntroReferral: Introduced in Senate
- 2025-05-12 - IntroReferral: Read twice and referred to the Committee on the Judiciary.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-05-12",
    "latestAction": {
      "actionDate": "2025-05-12",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/1712",
    "number": "1712",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Law"
    },
    "sponsors": [
      {
        "bioguideId": "M000934",
        "district": "",
        "firstName": "Jerry",
        "fullName": "Sen. Moran, Jerry [R-KS]",
        "lastName": "Moran",
        "party": "R",
        "state": "KS"
      }
    ],
    "title": "Criminal History Access Act of 2025",
    "type": "S",
    "updateDate": "2026-05-21T11:03:37Z",
    "updateDateIncludingText": "2026-05-21T11:03:37Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-05-12",
      "committees": {
        "item": {
          "name": "Judiciary Committee",
          "systemCode": "ssju00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on the Judiciary.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-05-12",
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
            "date": "2025-05-12T21:33:21Z",
            "name": "Referred To"
          },
          {
            "date": "2025-05-12T21:33:21Z",
            "name": "Referred To"
          }
        ]
      },
      "chamber": "Senate",
      "name": "Judiciary Committee",
      "systemCode": "ssju00",
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
      "sponsorshipDate": "2025-05-12",
      "state": "RI"
    },
    {
      "bioguideId": "T000476",
      "firstName": "Thomas",
      "fullName": "Sen. Tillis, Thomas [R-NC]",
      "isOriginalCosponsor": "False",
      "lastName": "Tillis",
      "middleName": "Roland",
      "party": "R",
      "sponsorshipDate": "2025-07-23",
      "state": "NC"
    },
    {
      "bioguideId": "B001305",
      "firstName": "Ted",
      "fullName": "Sen. Budd, Ted [R-NC]",
      "isOriginalCosponsor": "False",
      "lastName": "Budd",
      "party": "R",
      "sponsorshipDate": "2026-03-12",
      "state": "NC"
    },
    {
      "bioguideId": "S001181",
      "firstName": "Jeanne",
      "fullName": "Sen. Shaheen, Jeanne [D-NH]",
      "isOriginalCosponsor": "False",
      "lastName": "Shaheen",
      "party": "D",
      "sponsorshipDate": "2026-05-20",
      "state": "NH"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1712is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 1712\nIN THE SENATE OF THE UNITED STATES\nMay 12, 2025 Mr. Moran (for himself and Mr. Whitehouse ) introduced the following bill; which was read twice and referred to the Committee on the Judiciary\nA BILL\nTo authorize peace officer standards and training agencies to access criminal history records, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Criminal History Access Act of 2025 .\n#### 2. Definitions\nIn this Act:\n**(1) Peace officer standards and training agency**\nThe term peace officer standards and training agency means an agency of a State with the statutory authority under State law to set standards for the hiring, training, ethical conduct, and retention of the law enforcement officers of the State through certification, licensing, or other similar qualification process.\n**(2) State**\nThe term State means each of the several States of the United States, the District of Columbia, the Commonwealth of Puerto Rico, the Virgin Islands, Guam, American Samoa, the Commonwealth of the Northern Mariana Islands, and any territory or possession of the United States.\n#### 3. Amendments\n##### (a) Title 28\nSection 534(e) of title 28, United States Code, is amended\u2014\n**(1)**\nin paragraph (1), by striking and ;\n**(2)**\nin paragraph (2), by striking the period and inserting ; and ; and\n**(3)**\nby adding at the end the following:\n(3) peace officer standards training agencies, as defined in section 2 of the Criminal History Access Act of 2025 .\n##### (b) Regulations\nNot later than 180 days after the date of enactment of this Act, the Attorney General shall amend section part 20 of title 28, Code of Federal Regulations, as may be necessary to carry out the provisions of this Act.",
      "versionDate": "2025-05-12",
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
        "name": "Law",
        "updateDate": "2025-06-09T14:02:36Z"
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
      "date": "2025-05-12",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1712is.xml"
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
      "title": "Criminal History Access Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-05-21T11:03:37Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Criminal History Access Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-05-21T04:08:20Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to authorize peace officer standards and training agencies to access criminal history records, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-05-21T04:03:42Z"
    }
  ]
}
```
