# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/3192?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/3192
- Title: RESTORE Act
- Congress: 119
- Bill type: HR
- Bill number: 3192
- Origin chamber: House
- Introduced date: 2025-05-05
- Update date: 2025-12-12T09:07:43Z
- Update date including text: 2025-12-12T09:07:43Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, subjects, text, titles

## Timeline

- 2025-05-05: Introduced in House
- 2025-05-05 - IntroReferral: Introduced in House
- 2025-05-05 - IntroReferral: Introduced in House
- 2025-05-05 - IntroReferral: Referred to the House Committee on Veterans' Affairs.
- 2025-05-21 - Committee: Referred to the Subcommittee on Oversight and Investigations.
- Latest action: 2025-05-05: Introduced in House

## Actions

- 2025-05-05 - IntroReferral: Introduced in House
- 2025-05-05 - IntroReferral: Introduced in House
- 2025-05-05 - IntroReferral: Referred to the House Committee on Veterans' Affairs.
- 2025-05-21 - Committee: Referred to the Subcommittee on Oversight and Investigations.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-05-05",
    "latestAction": {
      "actionDate": "2025-05-05",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/3192",
    "number": "3192",
    "originChamber": "House",
    "policyArea": {
      "name": "Armed Forces and National Security"
    },
    "sponsors": [
      {
        "bioguideId": "M001188",
        "district": "6",
        "firstName": "Grace",
        "fullName": "Rep. Meng, Grace [D-NY-6]",
        "lastName": "Meng",
        "party": "D",
        "state": "NY"
      }
    ],
    "title": "RESTORE Act",
    "type": "HR",
    "updateDate": "2025-12-12T09:07:43Z",
    "updateDateIncludingText": "2025-12-12T09:07:43Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-05-21",
      "committees": {
        "item": {
          "name": "Oversight and Investigations Subcommittee",
          "systemCode": "hsvr08"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Referred to the Subcommittee on Oversight and Investigations.",
      "type": "Committee"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-05-05",
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
      "actionDate": "2025-05-05",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-05-05",
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
          "date": "2025-05-05T16:02:20Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Veterans' Affairs Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": {
              "date": "2025-05-21T15:48:24Z",
              "name": "Referred to"
            }
          },
          "name": "Oversight and Investigations Subcommittee",
          "systemCode": "hsvr08"
        }
      },
      "systemCode": "hsvr00",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr3192ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 3192\nIN THE HOUSE OF REPRESENTATIVES\nMay 5, 2025 Ms. Meng introduced the following bill; which was referred to the Committee on Veterans' Affairs\nA BILL\nTo provide back pay to reinstated employees of the Department of Veterans Affairs, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Reinstating Employee Salaries To Original Rates and Entitlements Act or the RESTORE Act .\n#### 2. Back pay for reinstated employees of the Department of Veterans Affairs\n##### (a) Back pay\nAny individual who was an employee of the Department of Veterans Affairs (including employees who were serving under a probationary or trial period due to a promotion) and who was involuntarily removed and subsequently reinstated or appointed to a position at the Department during the period beginning on January 20, 2025, and ending on the date of the enactment of this Act shall be entitled to back pay in accordance with section 5596 of title 5, United States Code.\n##### (b) Limitation\nSubsection (a) shall not apply to any individual removed from a political position.\n##### (c) Political position defined\nIn this section, the term political position means\u2014\n**(1)**\na position described under sections 5312 through 5316 of title 5, United States Code (relating to the Executive Schedule);\n**(2)**\na noncareer appointee (as that term is defined in section 3132(a) of such title); or\n**(3)**\na position in the executive branch of the Government of a confidential or policy-determining character under schedule C of subpart C of part 213 of title 5, Code of Federal Regulations.",
      "versionDate": "2025-05-05",
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
        "updateDate": "2025-06-04T14:30:22Z"
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
      "date": "2025-05-05",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr3192ih.xml"
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
      "title": "RESTORE Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-05-13T05:53:22Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "RESTORE Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-05-13T05:53:21Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "This Act may be cited as the Reinstating Employee Salaries To Original Rates and Entitlements Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-05-13T05:53:21Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To provide back pay to reinstated employees of the Department of Veterans Affairs, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-05-13T05:48:39Z"
    }
  ]
}
```
