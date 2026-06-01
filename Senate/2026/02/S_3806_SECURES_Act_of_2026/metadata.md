# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/3806?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/3806
- Title: SECURES Act of 2026
- Congress: 119
- Bill type: S
- Bill number: 3806
- Origin chamber: Senate
- Introduced date: 2026-02-09
- Update date: 2026-02-27T19:33:43Z
- Update date including text: 2026-02-27T19:33:43Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2026-02-09: Introduced in Senate
- 2026-02-09 - IntroReferral: Introduced in Senate
- 2026-02-09 - IntroReferral: Read twice and referred to the Committee on Commerce, Science, and Transportation.
- Latest action: 2026-02-09: Introduced in Senate

## Actions

- 2026-02-09 - IntroReferral: Introduced in Senate
- 2026-02-09 - IntroReferral: Read twice and referred to the Committee on Commerce, Science, and Transportation.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-02-09",
    "latestAction": {
      "actionDate": "2026-02-09",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/3806",
    "number": "3806",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Transportation and Public Works"
    },
    "sponsors": [
      {
        "bioguideId": "B001288",
        "district": "",
        "firstName": "Cory",
        "fullName": "Sen. Booker, Cory A. [D-NJ]",
        "lastName": "Booker",
        "party": "D",
        "state": "NJ"
      }
    ],
    "title": "SECURES Act of 2026",
    "type": "S",
    "updateDate": "2026-02-27T19:33:43Z",
    "updateDateIncludingText": "2026-02-27T19:33:43Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-02-09",
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
      "actionDate": "2026-02-09",
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
          "date": "2026-02-09T22:03:02Z",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s3806is.xml",
      "text": "II\n119th CONGRESS\n2d Session\nS. 3806\nIN THE SENATE OF THE UNITED STATES\nFebruary 9, 2026 Mr. Booker introduced the following bill; which was read twice and referred to the Committee on Commerce, Science, and Transportation\nA BILL\nTo require the Secretary of Transportation to publish a notice of proposed rulemaking concerning seat belts on school buses, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Secure Every Child Under the Right Equipment Standards Act of 2026 or the SECURES Act of 2026 .\n#### 2. Proposed rulemaking\n##### (a) Requirements\nNot later than 180 days after the date of enactment of this Act, the Secretary of Transportation shall publish a notice of proposed rulemaking on new Federal standards for school bus seat belt requirements on all new school buses, regardless of gross vehicle weight rating.\n##### (b) Considerations\nIn the proposed rulemaking, the Secretary shall consider\u2014\n**(1)**\nthe safety benefits of a lap/shoulder belt system (also known as a Type 2 seat belt assembly );\n**(2)**\nthe conclusion of the National Transportation Safety Board that Lap/shoulder belts provide the highest level of protection for school bus passengers and that Properly worn lap belts provide some benefit, while Properly worn lap/shoulder belts provide greater benefit by reducing injuries related to upper body flailing ;\n**(3)**\nthe 2015 announcement by the Administrator of the National Highway Traffic Safety Administration Mark Rosekind, stating that the agency believes that every child on every school bus should have a three-point seat belt ;\n**(4)**\nany innovative approaches to seat belt detection, seat belt reminder systems, and seat belt violation alert systems that could be incorporated into school bus designs; and\n**(5)**\nexisting experience from the States that have already required school buses to be equipped with seat belts.",
      "versionDate": "2026-02-09",
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
        "actionDate": "2026-02-09",
        "text": "Referred to the House Committee on Transportation and Infrastructure."
      },
      "number": "7428",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "SECURES Act of 2026",
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
        "name": "Transportation and Public Works",
        "updateDate": "2026-02-27T19:33:43Z"
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
      "date": "2026-02-09",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s3806is.xml"
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
      "title": "A bill to require the Secretary of Transportation to publish a notice of proposed rulemaking concerning seat belts on school buses, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-02-26T07:48:41Z"
    },
    {
      "title": "SECURES Act of 2026",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-02-26T07:38:16Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "SECURES Act of 2026",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-02-26T07:38:15Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Secure Every Child Under the Right Equipment Standards Act of 2026",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-02-26T07:38:15Z"
    }
  ]
}
```
