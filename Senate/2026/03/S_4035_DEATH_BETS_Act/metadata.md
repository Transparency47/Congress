# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/4035?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/4035
- Title: DEATH BETS Act
- Congress: 119
- Bill type: S
- Bill number: 4035
- Origin chamber: Senate
- Introduced date: 2026-03-10
- Update date: 2026-04-02T19:23:43Z
- Update date including text: 2026-04-02T19:23:43Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2026-03-10: Introduced in Senate
- 2026-03-10 - IntroReferral: Introduced in Senate
- 2026-03-10 - IntroReferral: Read twice and referred to the Committee on Agriculture, Nutrition, and Forestry.
- Latest action: 2026-03-10: Introduced in Senate

## Actions

- 2026-03-10 - IntroReferral: Introduced in Senate
- 2026-03-10 - IntroReferral: Read twice and referred to the Committee on Agriculture, Nutrition, and Forestry.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-03-10",
    "latestAction": {
      "actionDate": "2026-03-10",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/4035",
    "number": "4035",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Finance and Financial Sector"
    },
    "sponsors": [
      {
        "bioguideId": "S001150",
        "district": "",
        "firstName": "Adam",
        "fullName": "Sen. Schiff, Adam B. [D-CA]",
        "lastName": "Schiff",
        "party": "D",
        "state": "CA"
      }
    ],
    "title": "DEATH BETS Act",
    "type": "S",
    "updateDate": "2026-04-02T19:23:43Z",
    "updateDateIncludingText": "2026-04-02T19:23:43Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-03-10",
      "committees": {
        "item": {
          "name": "Agriculture, Nutrition, and Forestry Committee",
          "systemCode": "ssaf00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Agriculture, Nutrition, and Forestry.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2026-03-10",
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
          "date": "2026-03-10T16:12:06Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Agriculture, Nutrition, and Forestry Committee",
      "systemCode": "ssaf00",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s4035is.xml",
      "text": "II\n119th CONGRESS\n2d Session\nS. 4035\nIN THE SENATE OF THE UNITED STATES\nMarch 10, 2026 Mr. Schiff introduced the following bill; which was read twice and referred to the Committee on Agriculture, Nutrition, and Forestry\nA BILL\nTo amend the Commodity Exchange Act to prohibit the listing of contracts relating to war, death, and similar activities.\n#### 1. Short title\nThis Act may be cited as the Discouraging Exploitative Assassination, Tragedy, and Harm Betting in Event Trading Systems Act or the DEATH BETS Act .\n#### 2. Prohibition on listing of contracts relating to war, death, and similar activities\nSection 5c of the Commodity Exchange Act ( 7 U.S.C. 7a\u20132 ) is amended by inserting after subsection (c) the following:\n(d) Prohibition on listing of contracts relating to war, death, and similar activities A registered entity shall not list for trading or accept for clearing on or through the registered entity any of the following: (1) An agreement, contract, transaction, or swap based on an excluded commodity (as defined in section 1a(19)(iv)) that involves, relates to, or references terrorism, assassination, war, or any similar activity, as determined by the Commission. (2) An agreement, contract, transaction, or swap based on an excluded commodity (as defined in section 1a(19)(iv)) that involves, relates to, or references an individual\u2019s death or could otherwise be construed as correlating closely to an individual\u2019s death. .",
      "versionDate": "2026-03-10",
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
        "actionDate": "2026-03-16",
        "text": "Referred to the House Committee on Agriculture."
      },
      "number": "7942",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "DEATH BETS Act",
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
        "name": "Finance and Financial Sector",
        "updateDate": "2026-03-26T18:21:37Z"
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
      "date": "2026-03-10",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s4035is.xml"
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
      "title": "DEATH BETS Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-03-21T03:53:23Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "DEATH BETS Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-03-21T03:53:22Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Discouraging Exploitative Assassination, Tragedy, and Harm Betting in Event Trading Systems Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-03-21T03:53:22Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend the Commodity Exchange Act to prohibit the listing of contracts relating to war, death, and similar activities.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-03-21T03:48:27Z"
    }
  ]
}
```
