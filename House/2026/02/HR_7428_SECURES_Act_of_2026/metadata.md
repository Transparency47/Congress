# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/7428?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/7428
- Title: SECURES Act of 2026
- Congress: 119
- Bill type: HR
- Bill number: 7428
- Origin chamber: House
- Introduced date: 2026-02-09
- Update date: 2026-02-27T19:33:24Z
- Update date including text: 2026-02-27T19:33:24Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2026-02-09: Introduced in House
- 2026-02-09 - IntroReferral: Introduced in House
- 2026-02-09 - IntroReferral: Introduced in House
- 2026-02-09 - IntroReferral: Referred to the House Committee on Transportation and Infrastructure.
- Latest action: 2026-02-09: Introduced in House

## Actions

- 2026-02-09 - IntroReferral: Introduced in House
- 2026-02-09 - IntroReferral: Introduced in House
- 2026-02-09 - IntroReferral: Referred to the House Committee on Transportation and Infrastructure.

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
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/7428",
    "number": "7428",
    "originChamber": "House",
    "policyArea": {
      "name": "Transportation and Public Works"
    },
    "sponsors": [
      {
        "bioguideId": "G000583",
        "district": "5",
        "firstName": "Josh",
        "fullName": "Rep. Gottheimer, Josh [D-NJ-5]",
        "lastName": "Gottheimer",
        "party": "D",
        "state": "NJ"
      }
    ],
    "title": "SECURES Act of 2026",
    "type": "HR",
    "updateDate": "2026-02-27T19:33:24Z",
    "updateDateIncludingText": "2026-02-27T19:33:24Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2026-02-09",
      "committees": {
        "item": {
          "name": "Transportation and Infrastructure Committee",
          "systemCode": "hspw00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Transportation and Infrastructure.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2026-02-09",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-02-09",
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
          "date": "2026-02-09T17:01:35Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Transportation and Infrastructure Committee",
      "systemCode": "hspw00",
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
      "bioguideId": "L000599",
      "district": "17",
      "firstName": "Michael",
      "fullName": "Rep. Lawler, Michael [R-NY-17]",
      "isOriginalCosponsor": "True",
      "lastName": "Lawler",
      "party": "R",
      "sponsorshipDate": "2026-02-09",
      "state": "NY"
    },
    {
      "bioguideId": "N000147",
      "district": "0",
      "firstName": "Eleanor",
      "fullName": "Del. Norton, Eleanor Holmes [D-DC-At Large]",
      "isOriginalCosponsor": "False",
      "lastName": "Norton",
      "middleName": "Holmes",
      "party": "D",
      "sponsorshipDate": "2026-02-11",
      "state": "DC"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7428ih.xml",
      "text": "I\n119th CONGRESS\n2d Session\nH. R. 7428\nIN THE HOUSE OF REPRESENTATIVES\nFebruary 9, 2026 Mr. Gottheimer (for himself and Mr. Lawler ) introduced the following bill; which was referred to the Committee on Transportation and Infrastructure\nA BILL\nTo require the Secretary of Transportation to publish a notice of proposed rulemaking concerning seat belts on school buses, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Secure Every Child Under the Right Equipment Standards Act of 2026 or the SECURES Act of 2026 .\n#### 2. Proposed rulemaking\n##### (a) Requirements\nNot later than 180 days after the date of enactment of this Act, the Secretary of Transportation shall publish a notice of proposed rulemaking on new Federal standards for school bus seat belt requirements on all new school buses, regardless of gross vehicle weight rating.\n##### (b) Considerations\nIn the proposed rulemaking, the Secretary shall consider\u2014\n**(1)**\nthe safety benefits of a lap/shoulder belt system (also known as a Type 2 seat belt assembly );\n**(2)**\nthe conclusion of the National Transportation Safety Board that Lap/shoulder belts provide the highest level of protection for school bus passengers and that Properly worn lap belts provide some benefit, while Properly worn lap/shoulder belts provide greater benefit by reducing injuries related to upper body flailing ;\n**(3)**\nthe 2015 announcement by the Administrator of the National Highway Traffic Safety Administration Mark Rosekind, stating that the agency believes that every child on every school bus should have a three-point seat belt ;\n**(4)**\nany innovative approaches to seat belt detection, seat belt reminder systems, and seat belt violation alert systems that could be incorporated into school bus designs; and\n**(5)**\nexisting experience from the States that have already required school buses to be equipped with seat belts.",
      "versionDate": "2026-02-09",
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
        "actionDate": "2026-02-09",
        "text": "Read twice and referred to the Committee on Commerce, Science, and Transportation."
      },
      "number": "3806",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "SECURES Act of 2026",
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
        "name": "Transportation and Public Works",
        "updateDate": "2026-02-27T19:32:12Z"
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
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7428ih.xml"
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
      "title": "SECURES Act of 2026",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-02-23T13:23:23Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "SECURES Act of 2026",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-02-23T13:23:21Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Secure Every Child Under the Right Equipment Standards Act of 2026",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-02-23T13:23:21Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To require the Secretary of Transportation to publish a notice of proposed rulemaking concerning seat belts on school buses, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-02-23T13:18:25Z"
    }
  ]
}
```
