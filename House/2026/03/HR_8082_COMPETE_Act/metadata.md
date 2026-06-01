# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/8082?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/8082
- Title: COMPETE Act
- Congress: 119
- Bill type: HR
- Bill number: 8082
- Origin chamber: House
- Introduced date: 2026-03-25
- Update date: 2026-04-14T13:37:41Z
- Update date including text: 2026-04-14T13:37:41Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2026-03-25: Introduced in House
- 2026-03-25 - IntroReferral: Introduced in House
- 2026-03-25 - IntroReferral: Introduced in House
- 2026-03-25 - IntroReferral: Referred to the House Committee on Energy and Commerce.
- Latest action: 2026-03-25: Introduced in House

## Actions

- 2026-03-25 - IntroReferral: Introduced in House
- 2026-03-25 - IntroReferral: Introduced in House
- 2026-03-25 - IntroReferral: Referred to the House Committee on Energy and Commerce.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-03-25",
    "latestAction": {
      "actionDate": "2026-03-25",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/8082",
    "number": "8082",
    "originChamber": "House",
    "policyArea": {
      "name": "Health"
    },
    "sponsors": [
      {
        "bioguideId": "G000576",
        "district": "6",
        "firstName": "Glenn",
        "fullName": "Rep. Grothman, Glenn [R-WI-6]",
        "lastName": "Grothman",
        "party": "R",
        "state": "WI"
      }
    ],
    "title": "COMPETE Act",
    "type": "HR",
    "updateDate": "2026-04-14T13:37:41Z",
    "updateDateIncludingText": "2026-04-14T13:37:41Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2026-03-25",
      "committees": {
        "item": {
          "name": "Energy and Commerce Committee",
          "systemCode": "hsif00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Energy and Commerce.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2026-03-25",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-03-25",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
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
          "date": "2026-03-25T14:03:30Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Energy and Commerce Committee",
      "systemCode": "hsif00",
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
      "bioguideId": "F000469",
      "district": "1",
      "firstName": "Russ",
      "fullName": "Rep. Fulcher, Russ [R-ID-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Fulcher",
      "party": "R",
      "sponsorshipDate": "2026-03-25",
      "state": "ID"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr8082ih.xml",
      "text": "I\n119th CONGRESS\n2d Session\nH. R. 8082\nIN THE HOUSE OF REPRESENTATIVES\nMarch 25, 2026 Mr. Grothman (for himself and Mr. Fulcher ) introduced the following bill; which was referred to the Committee on Energy and Commerce\nA BILL\nTo ensure competition in health insurance markets.\n#### 1. Short title\nThis Act may be cited as the Competition and Openness in Markets to Promote Efficiency, Transparency, and Enhanced affordability Act or the COMPETE Act .\n#### 2. Short-term limited duration insurance\nSection 2791(b) of the Public Health Service Act ( 42 U.S.C. 300gg\u201391(b) ) is amended by adding at the end the following:\n(6) Short-term limited duration insurance The term short-term limited duration insurance means a plan providing health insurance coverage pursuant to a contract with a health insurance issuer\u2014 (A) that has an expiration date specified in the contract that is not more than 12 months after the original effective date of the contract; and (B) which may include a renewal guarantee that permits a policyholder to elect to purchase, for periods of time following expiration of the initial contract, another policy or policies at some future date, at a premium that would not reflect any additional underwriting. .",
      "versionDate": "2026-03-25",
      "versionType": "Introduced in House"
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
        "actionDate": "2025-12-10",
        "text": "Read twice and referred to the Committee on Health, Education, Labor, and Pensions."
      },
      "number": "3418",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "COMPETE Act",
      "type": "S"
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
        "name": "Health",
        "updateDate": "2026-04-14T13:37:41Z"
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
      "date": "2026-03-25",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr8082ih.xml"
        }
      ],
      "type": "Introduced in House"
    }
  ]
}
```

## API Data: titles

```json
{
  "titles": [
    {
      "title": "COMPETE Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-04-09T03:53:24Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "COMPETE Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-04-09T03:53:23Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Competition and Openness in Markets to Promote Efficiency, Transparency, and Enhanced affordability Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-04-09T03:53:23Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To ensure competition in health insurance markets.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-04-09T03:48:29Z"
    }
  ]
}
```
