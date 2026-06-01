# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/6585?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/6585
- Title: To direct the Secretary of Veterans Affairs to temporarily extend the period during which certain individuals may file claims for medical care under the CHAMPVA program of the Department of Veterans Affairs, and for other purposes.
- Congress: 119
- Bill type: HR
- Bill number: 6585
- Origin chamber: House
- Introduced date: 2025-12-10
- Update date: 2026-01-09T09:06:31Z
- Update date including text: 2026-01-09T09:06:31Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-12-10: Introduced in House
- 2025-12-10 - IntroReferral: Introduced in House
- 2025-12-10 - IntroReferral: Introduced in House
- 2025-12-10 - IntroReferral: Referred to the House Committee on Veterans' Affairs.
- 2026-01-05 - Committee: Referred to the Subcommittee on Health.
- Latest action: 2025-12-10: Introduced in House

## Actions

- 2025-12-10 - IntroReferral: Introduced in House
- 2025-12-10 - IntroReferral: Introduced in House
- 2025-12-10 - IntroReferral: Referred to the House Committee on Veterans' Affairs.
- 2026-01-05 - Committee: Referred to the Subcommittee on Health.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-12-10",
    "latestAction": {
      "actionDate": "2025-12-10",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/6585",
    "number": "6585",
    "originChamber": "House",
    "policyArea": {
      "name": "Armed Forces and National Security"
    },
    "sponsors": [
      {
        "bioguideId": "N000193",
        "district": "3",
        "firstName": "Zachary",
        "fullName": "Rep. Nunn, Zachary [R-IA-3]",
        "lastName": "Nunn",
        "party": "R",
        "state": "IA"
      }
    ],
    "title": "To direct the Secretary of Veterans Affairs to temporarily extend the period during which certain individuals may file claims for medical care under the CHAMPVA program of the Department of Veterans Affairs, and for other purposes.",
    "type": "HR",
    "updateDate": "2026-01-09T09:06:31Z",
    "updateDateIncludingText": "2026-01-09T09:06:31Z"
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
      "actionDate": "2025-12-10",
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
      "actionDate": "2025-12-10",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-12-10",
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
          "date": "2025-12-10T15:04:45Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Veterans' Affairs Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": {
              "date": "2026-01-05T14:12:49Z",
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
      "bioguideId": "D000230",
      "district": "1",
      "firstName": "Donald",
      "fullName": "Rep. Davis, Donald G. [D-NC-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Davis",
      "middleName": "G.",
      "party": "D",
      "sponsorshipDate": "2025-12-10",
      "state": "NC"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6585ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 6585\nIN THE HOUSE OF REPRESENTATIVES\nDecember 10, 2025 Mr. Nunn of Iowa (for himself and Mr. Davis of North Carolina ) introduced the following bill; which was referred to the Committee on Veterans' Affairs\nA BILL\nTo direct the Secretary of Veterans Affairs to temporarily extend the period during which certain individuals may file claims for medical care under the CHAMPVA program of the Department of Veterans Affairs, and for other purposes.\n#### 1. Temporary extension of period during which certain individuals may file claims for medical care under CHAMPVA program\n##### (a) In general\nWith respect to a covered individual who seeks retroactive approval for medical care under section 1781 of title 38, United States Code, the Secretary of Veterans Affairs shall ensure, during the period beginning on the date of the enactment of this Act and ending on September 30, 2027, if such individual is retroactively approved, the period during which the covered individual may file a claim for such medical care\u2014\n**(1)**\nbegins on the date on which the individual receives notice of such retroactive approval; and\n**(2)**\nends not earlier than 365 days after such date.\n##### (b) Regulations\nThe Secretary shall prescribe regulations to carry out subsection (a).\n##### (c) Covered individual defined\nIn this section, the term covered individual means an individual who is eligible for such medical care under such section and also entitled to hospital insurance benefits under part A of the program of health insurance administered by the Secretary of Health and Human Services under title XVIII of the Social Security Act ( 42 U.S.C. 1395 et seq. ).",
      "versionDate": "2025-12-10",
      "versionType": "Introduced in House"
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
        "updateDate": "2026-01-06T16:48:53Z"
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
      "date": "2025-12-10",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6585ih.xml"
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
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To direct the Secretary of Veterans Affairs to temporarily extend the period during which certain individuals may file claims for medical care under the CHAMPVA program of the Department of Veterans Affairs, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-12-29T14:18:18Z"
    },
    {
      "title": "To direct the Secretary of Veterans Affairs to temporarily extend the period during which certain individuals may file claims for medical care under the CHAMPVA program of the Department of Veterans Affairs, and for other purposes.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-12-11T09:06:46Z"
    }
  ]
}
```
