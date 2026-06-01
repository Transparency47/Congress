# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/6522?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/6522
- Title: CARING for Our Veterans Health Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 6522
- Origin chamber: House
- Introduced date: 2025-12-09
- Update date: 2026-01-09T09:06:57Z
- Update date including text: 2026-01-09T09:06:57Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-12-09: Introduced in House
- 2025-12-09 - IntroReferral: Introduced in House
- 2025-12-09 - IntroReferral: Introduced in House
- 2025-12-09 - IntroReferral: Referred to the House Committee on Veterans' Affairs.
- 2026-01-05 - Committee: Referred to the Subcommittee on Health.
- Latest action: 2025-12-09: Introduced in House

## Actions

- 2025-12-09 - IntroReferral: Introduced in House
- 2025-12-09 - IntroReferral: Introduced in House
- 2025-12-09 - IntroReferral: Referred to the House Committee on Veterans' Affairs.
- 2026-01-05 - Committee: Referred to the Subcommittee on Health.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-12-09",
    "latestAction": {
      "actionDate": "2025-12-09",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/6522",
    "number": "6522",
    "originChamber": "House",
    "policyArea": {
      "name": "Armed Forces and National Security"
    },
    "sponsors": [
      {
        "bioguideId": "H001098",
        "district": "8",
        "firstName": "Abraham",
        "fullName": "Rep. Hamadeh, Abraham J. [R-AZ-8]",
        "lastName": "Hamadeh",
        "party": "R",
        "state": "AZ"
      }
    ],
    "title": "CARING for Our Veterans Health Act of 2025",
    "type": "HR",
    "updateDate": "2026-01-09T09:06:57Z",
    "updateDateIncludingText": "2026-01-09T09:06:57Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-01-05",
      "committees": {
        "item": {
          "name": "Health Subcommittee",
          "systemCode": "hsvr03"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Referred to the Subcommittee on Health.",
      "type": "Committee"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-12-09",
      "committees": {
        "item": {
          "name": "Veterans' Affairs Committee",
          "systemCode": "hsvr00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Veterans' Affairs.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-12-09",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-12-09",
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
          "date": "2025-12-09T17:03:35Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Veterans' Affairs Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": {
              "date": "2026-01-05T14:13:39Z",
              "name": "Referred to"
            }
          },
          "name": "Health Subcommittee",
          "systemCode": "hsvr03"
        }
      },
      "systemCode": "hsvr00",
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
      "bioguideId": "C001133",
      "district": "6",
      "firstName": "Juan",
      "fullName": "Rep. Ciscomani, Juan [R-AZ-6]",
      "isOriginalCosponsor": "False",
      "lastName": "Ciscomani",
      "party": "R",
      "sponsorshipDate": "2025-12-10",
      "state": "AZ"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6522ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 6522\nIN THE HOUSE OF REPRESENTATIVES\nDecember 9, 2025 Mr. Hamadeh of Arizona introduced the following bill; which was referred to the Committee on Veterans' Affairs\nA BILL\nTo require implementation by the Under Secretary for Health of the Department of Veterans Affairs of certain recommendations relating to the provision of health care through community care providers, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Coordinating and Aligning Records to Improve and Normalize Governance for Our Veterans Health Act of 2025 or the CARING for Our Veterans Health Act of 2025 .\n#### 2. Implementation by Department of Veterans Affairs of certain recommendations with respect to care in the community\n##### (a) In general\nThe Under Secretary for Health of the Department of Veterans Affairs shall ensure that the Office of Integrated Veteran Care, or successor office\u2014\n**(1)**\ndevelops guidance for the efforts of medical centers of the Department of Veterans Affairs in obtaining final medical documentation after a veteran receives services from a community care provider pursuant to a referral from that medical center;\n**(2)**\nestablishes goals and related performance measures for medical centers of the Department in obtaining initial and final medical documentation from community care providers;\n**(3)**\nestablishes and monitors goals and related performance measures for the completion by such providers of core trainings and ensures that such providers complete the required training course; and\n**(4)**\ntakes steps to ensure that the Office of Integrated Veteran Care, or successor office, and any contractor for that Office communicate clear and accurate information to such providers regarding the core trainings recommended or required by that Office, including whether such training is recommended or required.\n##### (b) Report\nNot later than 120 days after the date of the enactment of this Act, and every 120 days thereafter until the requirements under subsection (a) are fully implemented, the Under Secretary for Health shall submit to the Committee on Veterans\u2019 Affairs of the Senate and the Committee on Veterans\u2019 Affairs of the House of Representatives a report on steps taken by the Under Secretary to implement those requirements.",
      "versionDate": "2025-12-09",
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
        "text": "Committee on Veterans' Affairs. Hearings held."
      },
      "number": "2397",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "CARING for Our Veterans Health Act of 2025",
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
        "updateDate": "2026-01-06T16:47:58Z"
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
      "date": "2025-12-09",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6522ih.xml"
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
      "title": "CARING for Our Veterans Health Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-12-27T05:38:19Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "CARING for Our Veterans Health Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-12-27T05:38:18Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Coordinating and Aligning Records to Improve and Normalize Governance for Our Veterans Health Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-12-27T05:38:18Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To require implementation by the Under Secretary for Health of the Department of Veterans Affairs of certain recommendations relating to the provision of health care through community care providers, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-12-27T05:33:24Z"
    }
  ]
}
```
