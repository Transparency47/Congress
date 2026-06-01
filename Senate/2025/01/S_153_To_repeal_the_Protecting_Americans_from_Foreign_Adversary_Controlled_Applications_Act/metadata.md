# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/153?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/153
- Title: Repeal the TikTok Ban Act
- Congress: 119
- Bill type: S
- Bill number: 153
- Origin chamber: Senate
- Introduced date: 2025-01-20
- Update date: 2025-12-05T22:57:19Z
- Update date including text: 2025-12-05T22:57:19Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-01-20: Introduced in Senate
- 2025-01-20 - IntroReferral: Introduced in Senate
- 2025-01-20 - IntroReferral: Read twice and referred to the Committee on Commerce, Science, and Transportation.
- Latest action: 2025-01-20: Introduced in Senate

## Actions

- 2025-01-20 - IntroReferral: Introduced in Senate
- 2025-01-20 - IntroReferral: Read twice and referred to the Committee on Commerce, Science, and Transportation.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-01-20",
    "latestAction": {
      "actionDate": "2025-01-20",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/153",
    "number": "153",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Science, Technology, Communications"
    },
    "sponsors": [
      {
        "bioguideId": "P000603",
        "district": "",
        "firstName": "Rand",
        "fullName": "Sen. Paul, Rand [R-KY]",
        "lastName": "Paul",
        "party": "R",
        "state": "KY"
      }
    ],
    "title": "Repeal the TikTok Ban Act",
    "type": "S",
    "updateDate": "2025-12-05T22:57:19Z",
    "updateDateIncludingText": "2025-12-05T22:57:19Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-01-20",
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
      "actionDate": "2025-01-20",
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
          "date": "2025-01-20T22:13:06Z",
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

## API Data: fullTexts

```json
{
  "fullTexts": [
    {
      "fetchError": null,
      "sourceFormat": "Formatted XML",
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s153is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 153\nIN THE SENATE OF THE UNITED STATES\nJanuary 20, 2025 Mr. Paul introduced the following bill; which was read twice and referred to the Committee on Commerce, Science, and Transportation\nA BILL\nTo repeal the Protecting Americans from Foreign Adversary Controlled Applications Act.\n#### 1. Short title\nThis Act may be cited as the Repeal the TikTok Ban Act .\n#### 2. Repeal of Protecting Americans from Foreign Adversary Controlled Applications Act\n##### (a) In general\nThe Protecting Americans from Foreign Adversary Controlled Applications Act ( 15 U.S.C. 9901 note; division H of Public Law 118\u201350 ) is repealed.\n##### (b) Retroactive effect\nAny designation of a website, desktop application, mobile application, or augmented or immersive technology application as a foreign adversary controlled application under the Protecting Americans from Foreign Adversary Controlled Applications Act ( 15 U.S.C. 9901 note; division H of Public Law 118\u201350 ), whether under subparagraph (A) or (B) of section 2(g)(3) of that Act, shall have no force or effect.",
      "versionDate": "2025-01-20",
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
        "actionDate": "2025-01-20",
        "text": "Referred to the House Committee on Energy and Commerce."
      },
      "number": "564",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Repeal the TikTok Ban Act",
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
      "legislativeSubjects": "",
      "policyArea": {
        "name": "Science, Technology, Communications",
        "updateDate": "2025-04-17T18:49:26Z"
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
      "date": "2025-01-20",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s153is.xml"
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
      "title": "Repeal the TikTok Ban Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-02-19T03:23:19Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Repeal the TikTok Ban Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-02-19T03:23:17Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to repeal the Protecting Americans from Foreign Adversary Controlled Applications Act.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-02-19T03:18:19Z"
    }
  ]
}
```
