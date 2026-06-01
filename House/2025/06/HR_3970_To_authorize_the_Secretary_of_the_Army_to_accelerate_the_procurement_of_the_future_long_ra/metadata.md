# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/3970?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/3970
- Title: FLRAA Production Acceleration Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 3970
- Origin chamber: House
- Introduced date: 2025-06-12
- Update date: 2025-12-05T22:08:01Z
- Update date including text: 2025-12-05T22:08:01Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-06-12: Introduced in House
- 2025-06-12 - IntroReferral: Introduced in House
- 2025-06-12 - IntroReferral: Introduced in House
- 2025-06-12 - IntroReferral: Referred to the House Committee on Armed Services.
- Latest action: 2025-06-12: Introduced in House

## Actions

- 2025-06-12 - IntroReferral: Introduced in House
- 2025-06-12 - IntroReferral: Introduced in House
- 2025-06-12 - IntroReferral: Referred to the House Committee on Armed Services.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-06-12",
    "latestAction": {
      "actionDate": "2025-06-12",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/3970",
    "number": "3970",
    "originChamber": "House",
    "policyArea": {
      "name": "Armed Forces and National Security"
    },
    "sponsors": [
      {
        "bioguideId": "J000304",
        "district": "13",
        "firstName": "Ronny",
        "fullName": "Rep. Jackson, Ronny [R-TX-13]",
        "lastName": "Jackson",
        "party": "R",
        "state": "TX"
      }
    ],
    "title": "FLRAA Production Acceleration Act of 2025",
    "type": "HR",
    "updateDate": "2025-12-05T22:08:01Z",
    "updateDateIncludingText": "2025-12-05T22:08:01Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-06-12",
      "committees": {
        "item": {
          "name": "Armed Services Committee",
          "systemCode": "hsas00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Armed Services.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-06-12",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-06-12",
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
          "date": "2025-06-12T14:08:00Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Armed Services Committee",
      "systemCode": "hsas00",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr3970ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 3970\nIN THE HOUSE OF REPRESENTATIVES\nJune 12, 2025 Mr. Jackson of Texas introduced the following bill; which was referred to the Committee on Armed Services\nA BILL\nTo authorize the Secretary of the Army to accelerate the procurement of the future long range assault aircraft by initiating early production of not more than 24 such aircraft, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the FLRAA Production Acceleration Act of 2025 .\n#### 2. Authorization to initiate early production of future long range assault aircraft\n##### (a) Authorization\nThe Secretary of the Army may enter into contracts, in advance of full-rate production, for the procurement of not more than 24 future long range assault aircraft as part of an accelerated low-rate early production effort.\n##### (b) Objectives\nIn carrying out the early production effort described in subsection (a), the Secretary of the Army shall pursue the following objectives:\n**(1)**\nTo expedite delivery of future long range assault aircraft operational capability to the warfighter.\n**(2)**\nTo maintain momentum and learning continuity between test article completion and full production ramp-up.\n**(3)**\nTo stabilize and retain the specialized workforce and industrial base supporting future long range assault aircraft, including critical suppliers and production facilities in Texas, Kansas, and other States.\n**(4)**\nTo mitigate cost escalation risks and improve program affordability across the life cycle.\n##### (c) Considerations\nIn executing the authority provided by subsection (a), the Secretary shall\u2014\n**(1)**\nprioritize program continuity, cost-efficiency, and workforce retention across the supply chain for tiltrotor aircraft;\n**(2)**\nensure that aircraft procured as part of the early production effort described in subsection (a) incorporate lessons learned from test article evaluations; and\n**(3)**\nmaintain flexibility in design to accommodate future upgrades through the modular open systems architecture and digital backbone.\n#### 3. Report to Congress\nNot later than 180 days after the date of the enactment of this Act, the Secretary of the Army shall submit to the congressional defense committees a report detailing\u2014\n**(1)**\nthe implementation plan and timeline for the procurement and early production effort described in subsection (a);\n**(2)**\nthe status of industrial base readiness and supply chain coordination; and\n**(3)**\nestimated long-term cost savings and operational benefits derived from such early production effort.",
      "versionDate": "2025-06-12",
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
        "actionDate": "2025-06-12",
        "text": "Read twice and referred to the Committee on Armed Services."
      },
      "number": "2080",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "FLRAA Production Acceleration Act of 2025",
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
        "name": "Armed Forces and National Security",
        "updateDate": "2025-07-16T15:28:45Z"
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
      "date": "2025-06-12",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr3970ih.xml"
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
      "title": "FLRAA Production Acceleration Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-06-21T04:53:20Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "FLRAA Production Acceleration Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-06-21T04:53:18Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To authorize the Secretary of the Army to accelerate the procurement of the future long range assault aircraft by initiating early production of not more than 24 such aircraft, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-06-21T04:48:28Z"
    }
  ]
}
```
