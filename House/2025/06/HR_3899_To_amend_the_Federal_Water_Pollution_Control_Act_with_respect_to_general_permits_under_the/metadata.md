# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/3899?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/3899
- Title: Clarifying Federal General Permits Act
- Congress: 119
- Bill type: HR
- Bill number: 3899
- Origin chamber: House
- Introduced date: 2025-06-11
- Update date: 2026-02-04T05:06:16Z
- Update date including text: 2026-02-04T05:06:16Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, subjects, text, titles

## Timeline

- 2025-06-11: Introduced in House
- 2025-06-11 - IntroReferral: Introduced in House
- 2025-06-11 - IntroReferral: Introduced in House
- 2025-06-11 - IntroReferral: Referred to the House Committee on Transportation and Infrastructure.
- 2025-06-13 - Committee: Referred to the Subcommittee on Water Resources and Environment.
- Latest action: 2025-06-11: Introduced in House

## Actions

- 2025-06-11 - IntroReferral: Introduced in House
- 2025-06-11 - IntroReferral: Introduced in House
- 2025-06-11 - IntroReferral: Referred to the House Committee on Transportation and Infrastructure.
- 2025-06-13 - Committee: Referred to the Subcommittee on Water Resources and Environment.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-06-11",
    "latestAction": {
      "actionDate": "2025-06-11",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/3899",
    "number": "3899",
    "originChamber": "House",
    "policyArea": {
      "name": "Environmental Protection"
    },
    "sponsors": [
      {
        "bioguideId": "C001129",
        "district": "10",
        "firstName": "Mike",
        "fullName": "Rep. Collins, Mike [R-GA-10]",
        "lastName": "Collins",
        "party": "R",
        "state": "GA"
      }
    ],
    "title": "Clarifying Federal General Permits Act",
    "type": "HR",
    "updateDate": "2026-02-04T05:06:16Z",
    "updateDateIncludingText": "2026-02-04T05:06:16Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-06-13",
      "committees": {
        "item": {
          "name": "Water Resources and Environment Subcommittee",
          "systemCode": "hspw02"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Referred to the Subcommittee on Water Resources and Environment.",
      "type": "Committee"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-06-11",
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
      "actionDate": "2025-06-11",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-06-11",
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
          "date": "2025-06-11T14:04:40Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Transportation and Infrastructure Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": {
              "date": "2025-06-13T15:17:41Z",
              "name": "Referred to"
            }
          },
          "name": "Water Resources and Environment Subcommittee",
          "systemCode": "hspw02"
        }
      },
      "systemCode": "hspw00",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr3899ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 3899\nIN THE HOUSE OF REPRESENTATIVES\nJune 11, 2025 Mr. Collins introduced the following bill; which was referred to the Committee on Transportation and Infrastructure\nA BILL\nTo amend the Federal Water Pollution Control Act with respect to general permits under the national pollutant discharge elimination system, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Clarifying Federal General Permits Act .\n#### 2. Federal general permits\nSection 402(a) of the Federal Water Pollution Control Act ( 33 U.S.C. 1342(a) ) is amended by adding at the end the following:\n(6) (A) The Administrator may issue general permits under this section on a State, regional, or nationwide basis, or for a delineated area, for discharges associated with any category of activities, which discharges are of similar types and from similar sources. (B) If a general permit issued under this section will expire and the Administrator decides not to issue a new general permit for discharges similar to those covered by the expiring general permit, the Administrator shall publish in the Federal Register a notice of such decision at least two years prior to the expiration of the general permit. (C) (i) If a general permit issued under this section expires and the Administrator has not published a notice in accordance with subparagraph (B), the Administrator shall, until the date described in clause (ii)\u2014 (I) continue to apply the terms, conditions, and requirements of the expired general permit to any discharge that was covered by the expired general permit; and (II) apply such terms, conditions, and requirements to any discharge that would have been covered by the expired general permit (in accordance with any relevant requirements for such coverage) if the discharge had occurred before such expiration. (ii) The date described in this clause is the earlier of\u2014 (I) the date on which the Administrator issues a new general permit for discharges similar to those covered by the expired general permit; or (II) the date that is 2 years after the date on which the Administrator publishes in the Federal Register a notice of a decision not to issue a new general permit for discharges similar to those covered by the expired general permit. .",
      "versionDate": "2025-06-11",
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
        "name": "Environmental Protection",
        "updateDate": "2025-07-01T12:54:12Z"
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
      "date": "2025-06-11",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr3899ih.xml"
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
      "title": "Clarifying Federal General Permits Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-06-17T06:23:19Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Clarifying Federal General Permits Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-06-17T06:23:18Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Federal Water Pollution Control Act with respect to general permits under the national pollutant discharge elimination system, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-06-17T06:18:28Z"
    }
  ]
}
```
