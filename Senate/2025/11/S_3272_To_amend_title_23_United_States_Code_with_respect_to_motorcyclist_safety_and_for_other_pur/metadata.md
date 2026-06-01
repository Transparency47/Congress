# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/3272?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/3272
- Title: Motorcycle Safety Awareness Act of 2025
- Congress: 119
- Bill type: S
- Bill number: 3272
- Origin chamber: Senate
- Introduced date: 2025-11-20
- Update date: 2026-01-06T18:22:51Z
- Update date including text: 2026-01-06T18:22:51Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-11-20: Introduced in Senate
- 2025-11-20 - IntroReferral: Introduced in Senate
- 2025-11-20 - IntroReferral: Read twice and referred to the Committee on Commerce, Science, and Transportation.
- Latest action: 2025-11-20: Introduced in Senate

## Actions

- 2025-11-20 - IntroReferral: Introduced in Senate
- 2025-11-20 - IntroReferral: Read twice and referred to the Committee on Commerce, Science, and Transportation.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-11-20",
    "latestAction": {
      "actionDate": "2025-11-20",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/3272",
    "number": "3272",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Transportation and Public Works"
    },
    "sponsors": [
      {
        "bioguideId": "P000595",
        "district": "",
        "firstName": "Gary",
        "fullName": "Sen. Peters, Gary C. [D-MI]",
        "lastName": "Peters",
        "party": "D",
        "state": "MI"
      }
    ],
    "title": "Motorcycle Safety Awareness Act of 2025",
    "type": "S",
    "updateDate": "2026-01-06T18:22:51Z",
    "updateDateIncludingText": "2026-01-06T18:22:51Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-11-20",
      "committees": {
        "item": {
          "name": "Commerce, Science, and Transportation Committee",
          "systemCode": "sscm00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Commerce, Science, and Transportation.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-11-20",
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
          "date": "2025-11-20T20:42:59Z",
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
      "bioguideId": "E000295",
      "firstName": "Joni",
      "fullName": "Sen. Ernst, Joni [R-IA]",
      "isOriginalCosponsor": "True",
      "lastName": "Ernst",
      "party": "R",
      "sponsorshipDate": "2025-11-20",
      "state": "IA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s3272is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 3272\nIN THE SENATE OF THE UNITED STATES\nNovember 20, 2025 Mr. Peters (for himself and Ms. Ernst ) introduced the following bill; which was read twice and referred to the Committee on Commerce, Science, and Transportation\nA BILL\nTo amend title 23, United States Code, with respect to motorcyclist safety, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Motorcycle Safety Awareness Act of 2025 .\n#### 2. Motorcyclist safety\n##### (a) In general\nSection 405(f)(3) of title 23, United States Code, is amended\u2014\n**(1)**\nin the matter preceding subparagraph (A), by striking at least 2 of the following criteria and inserting at least 3 of the following criteria, 1 of which shall be the criterion described in subparagraph (H) ; and\n**(2)**\nby adding at the end the following:\n(H) Driver education and driving safety courses The inclusion, in driver education and driver safety courses provided to individuals by educational and motor vehicle agencies of the State, of instruction and testing relating to motorcyclist awareness, including information relating to\u2014 (i) State-specific motorcycle laws, such as lane-splitting and lane-filtering laws; and (ii) share-the-road principles intended to increase awareness of motorcyclists and scooter riders on the roadway. .\n##### (b) Effective date\nThe amendments made by subsection (a) shall take effect on the date that is 2 years after the date of enactment of this Act.",
      "versionDate": "2025-11-20",
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
        "name": "Transportation and Public Works",
        "updateDate": "2026-01-06T18:22:51Z"
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
      "date": "2025-11-20",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s3272is.xml"
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
      "title": "A bill to amend title 23, United States Code, with respect to motorcyclist safety, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-12-19T07:58:48Z"
    },
    {
      "title": "Motorcycle Safety Awareness Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-12-19T05:38:23Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Motorcycle Safety Awareness Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-12-19T05:38:19Z"
    }
  ]
}
```
