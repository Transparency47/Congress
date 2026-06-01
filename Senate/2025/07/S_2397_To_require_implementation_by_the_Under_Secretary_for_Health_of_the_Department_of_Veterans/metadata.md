# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/2397?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/2397
- Title: CARING for Our Veterans Health Act of 2025
- Congress: 119
- Bill type: S
- Bill number: 2397
- Origin chamber: Senate
- Introduced date: 2025-07-23
- Update date: 2026-04-21T15:35:25Z
- Update date including text: 2026-04-21T15:35:25Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-07-23: Introduced in Senate
- 2025-07-23 - IntroReferral: Introduced in Senate
- 2025-07-23 - IntroReferral: Read twice and referred to the Committee on Veterans' Affairs.
- 2025-12-10 - Committee: Committee on Veterans' Affairs. Hearings held.
- 2026-03-18 - Committee: Committee on Veterans' Affairs. Ordered to be reported with an amendment in the nature of a substitute favorably.
- Latest action: 2025-07-23: Introduced in Senate

## Actions

- 2025-07-23 - IntroReferral: Introduced in Senate
- 2025-07-23 - IntroReferral: Read twice and referred to the Committee on Veterans' Affairs.
- 2025-12-10 - Committee: Committee on Veterans' Affairs. Hearings held.
- 2026-03-18 - Committee: Committee on Veterans' Affairs. Ordered to be reported with an amendment in the nature of a substitute favorably.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-07-23",
    "latestAction": {
      "actionDate": "2025-07-23",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/2397",
    "number": "2397",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Armed Forces and National Security"
    },
    "sponsors": [
      {
        "bioguideId": "R000618",
        "district": "",
        "firstName": "Pete",
        "fullName": "Sen. Ricketts, Pete [R-NE]",
        "lastName": "Ricketts",
        "party": "R",
        "state": "NE"
      }
    ],
    "title": "CARING for Our Veterans Health Act of 2025",
    "type": "S",
    "updateDate": "2026-04-21T15:35:25Z",
    "updateDateIncludingText": "2026-04-21T15:35:25Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-03-18",
      "committees": {
        "item": {
          "name": "Veterans' Affairs Committee",
          "systemCode": "ssva00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Committee on Veterans' Affairs. Ordered to be reported with an amendment in the nature of a substitute favorably.",
      "type": "Committee"
    },
    {
      "actionDate": "2025-12-10",
      "committees": {
        "item": {
          "name": "Veterans' Affairs Committee",
          "systemCode": "ssva00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Committee on Veterans' Affairs. Hearings held.",
      "type": "Committee"
    },
    {
      "actionDate": "2025-07-23",
      "committees": {
        "item": {
          "name": "Veterans' Affairs Committee",
          "systemCode": "ssva00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Veterans' Affairs.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-07-23",
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
            "date": "2026-03-18T20:00:24Z",
            "name": "Markup By"
          },
          {
            "date": "2025-12-10T21:00:28Z",
            "name": "Hearings By (full committee)"
          },
          {
            "date": "2025-07-23T16:19:38Z",
            "name": "Referred To"
          }
        ]
      },
      "chamber": "Senate",
      "name": "Veterans' Affairs Committee",
      "systemCode": "ssva00",
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
      "bioguideId": "K000383",
      "firstName": "Angus",
      "fullName": "Sen. King, Angus S., Jr. [I-ME]",
      "isOriginalCosponsor": "True",
      "lastName": "King",
      "middleName": "S.",
      "party": "I",
      "sponsorshipDate": "2025-07-23",
      "state": "ME"
    },
    {
      "bioguideId": "S001208",
      "firstName": "Elissa",
      "fullName": "Sen. Slotkin, Elissa [D-MI]",
      "isOriginalCosponsor": "False",
      "lastName": "Slotkin",
      "party": "D",
      "sponsorshipDate": "2025-12-10",
      "state": "MI"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2397is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 2397\nIN THE SENATE OF THE UNITED STATES\nJuly 23, 2025 Mr. Ricketts (for himself and Mr. King ) introduced the following bill; which was read twice and referred to the Committee on Veterans' Affairs\nA BILL\nTo require implementation by the Under Secretary for Health of the Department of Veterans Affairs of certain recommendations relating to the provision of health care through community care providers, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Coordinating and Aligning Records to Improve and Normalize Governance for Our Veterans Health Act of 2025 or the CARING for Our Veterans Health Act of 2025 .\n#### 2. Implementation by Department of Veterans Affairs of certain recommendations with respect to care in the community\n##### (a) In general\nThe Under Secretary for Health of the Department of Veterans Affairs shall ensure that the Office of Integrated Veteran Care, or successor office\u2014\n**(1)**\ndevelops guidance for the efforts of medical centers of the Department of Veterans Affairs in obtaining final medical documentation after a veteran receives services from a community care provider pursuant to a referral from that medical center;\n**(2)**\nestablishes goals and related performance measures for medical centers of the Department in obtaining initial and final medical documentation from community care providers;\n**(3)**\nestablishes and monitors goals and related performance measures for the completion by such providers of core trainings and ensures that such providers complete the required training course; and\n**(4)**\ntakes steps to ensure that the Office of Integrated Veteran Care, or successor office, and any contractor for that Office communicate clear and accurate information to such providers regarding the core trainings recommended or required by that Office, including whether such training is recommended or required.\n##### (b) Report\nNot later than 120 days after the date of the enactment of this Act, and every 120 days thereafter until the requirements under subsection (a) are fully implemented, the Under Secretary for Health shall submit to the Committee on Veterans\u2019 Affairs of the Senate and the Committee on Veterans\u2019 Affairs of the House of Representatives a report on steps taken by the Under Secretary to implement those requirements.",
      "versionDate": "2025-07-23",
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
        "actionDate": "2026-01-05",
        "text": "Referred to the Subcommittee on Health."
      },
      "number": "6522",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "CARING for Our Veterans Health Act of 2025",
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
            "name": "Congressional oversight",
            "updateDate": "2026-01-09T16:24:38Z"
          },
          {
            "name": "Health care coverage and access",
            "updateDate": "2026-01-09T16:24:32Z"
          },
          {
            "name": "Veterans' medical care",
            "updateDate": "2026-01-09T16:24:28Z"
          }
        ]
      },
      "policyArea": {
        "name": "Armed Forces and National Security",
        "updateDate": "2025-08-07T15:46:01Z"
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
      "date": "2025-07-23",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2397is.xml"
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
      "title": "CARING for Our Veterans Health Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-03-19T11:03:27Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "CARING for Our Veterans Health Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-08-06T04:53:21Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Coordinating and Aligning Records to Improve and Normalize Governance for Our Veterans Health Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-08-06T04:53:21Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to require implementation by the Under Secretary for Health of the Department of Veterans Affairs of certain recommendations relating to the provision of health care through community care providers, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-08-06T04:48:31Z"
    }
  ]
}
```
