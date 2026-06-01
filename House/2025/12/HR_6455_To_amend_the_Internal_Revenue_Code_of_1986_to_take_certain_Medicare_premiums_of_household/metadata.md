# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/6455?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/6455
- Title: Health Insurance Premium Fairness Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 6455
- Origin chamber: House
- Introduced date: 2025-12-04
- Update date: 2026-01-06T16:00:43Z
- Update date including text: 2026-01-06T16:00:43Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-12-04: Introduced in House
- 2025-12-04 - IntroReferral: Introduced in House
- 2025-12-04 - IntroReferral: Introduced in House
- 2025-12-04 - IntroReferral: Referred to the House Committee on Ways and Means.
- Latest action: 2025-12-04: Introduced in House

## Actions

- 2025-12-04 - IntroReferral: Introduced in House
- 2025-12-04 - IntroReferral: Introduced in House
- 2025-12-04 - IntroReferral: Referred to the House Committee on Ways and Means.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-12-04",
    "latestAction": {
      "actionDate": "2025-12-04",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/6455",
    "number": "6455",
    "originChamber": "House",
    "policyArea": {
      "name": "Taxation"
    },
    "sponsors": [
      {
        "bioguideId": "L000593",
        "district": "49",
        "firstName": "Mike",
        "fullName": "Rep. Levin, Mike [D-CA-49]",
        "lastName": "Levin",
        "party": "D",
        "state": "CA"
      }
    ],
    "title": "Health Insurance Premium Fairness Act of 2025",
    "type": "HR",
    "updateDate": "2026-01-06T16:00:43Z",
    "updateDateIncludingText": "2026-01-06T16:00:43Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-12-04",
      "committees": {
        "item": {
          "name": "Ways and Means Committee",
          "systemCode": "hswm00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Ways and Means.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-12-04",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-12-04",
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
          "date": "2025-12-04T14:07:30Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Ways and Means Committee",
      "systemCode": "hswm00",
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
      "bioguideId": "S001156",
      "district": "38",
      "firstName": "Linda",
      "fullName": "Rep. S\u00e1nchez, Linda T. [D-CA-38]",
      "isOriginalCosponsor": "True",
      "lastName": "S\u00e1nchez",
      "middleName": "T.",
      "party": "D",
      "sponsorshipDate": "2025-12-04",
      "state": "CA"
    },
    {
      "bioguideId": "J000310",
      "district": "32",
      "firstName": "Julie",
      "fullName": "Rep. Johnson, Julie [D-TX-32]",
      "isOriginalCosponsor": "True",
      "lastName": "Johnson",
      "party": "D",
      "sponsorshipDate": "2025-12-04",
      "state": "TX"
    },
    {
      "bioguideId": "N000147",
      "district": "0",
      "firstName": "Eleanor",
      "fullName": "Del. Norton, Eleanor Holmes [D-DC-At Large]",
      "isOriginalCosponsor": "True",
      "lastName": "Norton",
      "middleName": "Holmes",
      "party": "D",
      "sponsorshipDate": "2025-12-04",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6455ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 6455\nIN THE HOUSE OF REPRESENTATIVES\nDecember 4, 2025 Mr. Levin (for himself, Ms. S\u00e1nchez , Ms. Johnson of Texas , and Ms. Norton ) introduced the following bill; which was referred to the Committee on Ways and Means\nA BILL\nTo amend the Internal Revenue Code of 1986 to take certain Medicare premiums of household members into account in determining the health care insurance premiums tax credit.\n#### 1. Short title\nThis Act may be cited as the Health Insurance Premium Fairness Act of 2025 .\n#### 2. Certain Medicare premiums of household members taken into account in determining health care insurance premiums tax credit\n##### (a) In general\nSection 36B(b) of the Internal Revenue Code of 1986 is amended by adding at the end the following new paragraph:\n(4) Adjustment for certain Medicare premiums of household members (A) In general In the case of any applicable taxpayer who elects (at such time and in such manner as the Secretary may provide) the application of this paragraph with respect to any coverage month, the amount determined under paragraph (2)(B)(ii) with respect to such coverage month shall be reduced (but not below zero) by the aggregate amount of specified Medicare premiums of such applicable taxpayer\u2019s household members for such month. (B) Household members For purposes of this paragraph, the term household member means, with respect to any applicable taxpayer, any individual who is taken into account in determining the family size of such applicable taxpayer under subsection (d)(1). (C) Specified Medicare premiums For purposes of this paragraph, the term specified Medicare premiums means premiums paid by the applicable taxpayer or such taxpayer\u2019s household members (and not reimbursed by any other person) for coverage under part A, B, C, or D of title XVIII of the Social Security Act, and premiums for coverage under a Medicare supplemental policy under section 1882 of such Act. .\n##### (b) Effective date\nThe amendments made by this section shall apply to coverage months beginning after December 31, 2025.",
      "versionDate": "2025-12-04",
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
        "name": "Taxation",
        "updateDate": "2026-01-06T16:00:43Z"
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
      "date": "2025-12-04",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6455ih.xml"
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
      "title": "Health Insurance Premium Fairness Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-12-27T05:38:18Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Health Insurance Premium Fairness Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-12-27T05:38:17Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Internal Revenue Code of 1986 to take certain Medicare premiums of household members into account in determining the health care insurance premiums tax credit.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-12-27T05:33:16Z"
    }
  ]
}
```
