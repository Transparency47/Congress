# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/5020?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/5020
- Title: Supporting Our Shelters Act
- Congress: 119
- Bill type: HR
- Bill number: 5020
- Origin chamber: House
- Introduced date: 2025-08-22
- Update date: 2026-05-16T08:08:05Z
- Update date including text: 2026-05-16T08:08:05Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-08-22: Introduced in House
- 2025-08-22 - IntroReferral: Introduced in House
- 2025-08-22 - IntroReferral: Introduced in House
- 2025-08-22 - IntroReferral: Referred to the House Committee on Agriculture.
- 2026-01-13 - Committee: Referred to the Subcommittee on Livestock, Dairy, and Poultry.
- Latest action: 2025-08-22: Introduced in House

## Actions

- 2025-08-22 - IntroReferral: Introduced in House
- 2025-08-22 - IntroReferral: Introduced in House
- 2025-08-22 - IntroReferral: Referred to the House Committee on Agriculture.
- 2026-01-13 - Committee: Referred to the Subcommittee on Livestock, Dairy, and Poultry.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-08-22",
    "latestAction": {
      "actionDate": "2025-08-22",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/5020",
    "number": "5020",
    "originChamber": "House",
    "policyArea": {
      "name": "Animals"
    },
    "sponsors": [
      {
        "bioguideId": "E000299",
        "district": "16",
        "firstName": "Veronica",
        "fullName": "Rep. Escobar, Veronica [D-TX-16]",
        "lastName": "Escobar",
        "party": "D",
        "state": "TX"
      }
    ],
    "title": "Supporting Our Shelters Act",
    "type": "HR",
    "updateDate": "2026-05-16T08:08:05Z",
    "updateDateIncludingText": "2026-05-16T08:08:05Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-01-13",
      "committees": {
        "item": {
          "name": "Livestock, Dairy, and Poultry Subcommittee",
          "systemCode": "hsag29"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Referred to the Subcommittee on Livestock, Dairy, and Poultry.",
      "type": "Committee"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-08-22",
      "committees": {
        "item": {
          "name": "Agriculture Committee",
          "systemCode": "hsag00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Agriculture.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-08-22",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-08-22",
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
          "date": "2025-08-22T13:01:50Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Agriculture Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": {
              "date": "2026-01-13T19:51:33Z",
              "name": "Referred to"
            }
          },
          "name": "Livestock, Dairy, and Poultry Subcommittee",
          "systemCode": "hsag29"
        }
      },
      "systemCode": "hsag00",
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
      "bioguideId": "G000587",
      "district": "29",
      "firstName": "Sylvia",
      "fullName": "Rep. Garcia, Sylvia R. [D-TX-29]",
      "isOriginalCosponsor": "True",
      "lastName": "Garcia",
      "middleName": "R.",
      "party": "D",
      "sponsorshipDate": "2025-08-22",
      "state": "TX"
    },
    {
      "bioguideId": "K000391",
      "district": "8",
      "firstName": "Raja",
      "fullName": "Rep. Krishnamoorthi, Raja [D-IL-8]",
      "isOriginalCosponsor": "True",
      "lastName": "Krishnamoorthi",
      "party": "D",
      "sponsorshipDate": "2025-08-22",
      "state": "IL"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr5020ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 5020\nIN THE HOUSE OF REPRESENTATIVES\nAugust 22, 2025 Ms. Escobar (for herself, Ms. Garcia of Texas , and Mr. Krishnamoorthi ) introduced the following bill; which was referred to the Committee on Agriculture\nA BILL\nTo amend the Animal Welfare Act to direct the Secretary of Agriculture to establish a program under which the Secretary will award grants to entities for purposes of supporting the capability of such entities to provide care to animals in their care, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Supporting Our Shelters Act .\n#### 2. Grants to support animal shelters\nSection 28 of the Animal Welfare Act ( 7 U.S.C. 2158 ) is amended by striking subsection (d) and inserting the following:\n(d) Grants To support animal shelters (1) In general The Secretary shall establish a program under which the Secretary will award grants to entities described in subsection (a)(2) for purposes of supporting the capability of such entities to provide care to animals in their care, including feeding, sheltering, veterinary care, recreational activities, and the hiring, training, and retention of staff to provide such care. (2) Term The term of a grant under this subsection shall not exceed 3 years. Such term is renewable if the grantee submits a report to the Secretary under paragraph (4) prior to the expiration of the respective term. (3) Report to Secretary Beginning not later than 180 days after the date on which the first grant is awarded under this subsection and each year thereafter, each recipient of a grant under this subsection shall submit to the Secretary a detailed accounting of\u2014 (A) the number of each species taken into the shelter and the outcome for each species during the period covered by the report; and (B) how the recipient of the grant used grant funds during the period covered by the report. (4) Report to Congress Beginning not later than 180 days after the date of the enactment of this subsection and each year thereafter, the Secretary shall submit to the Committee on Agriculture of the House of Representatives and the Committee on Agriculture, Nutrition, and Forestry of the Senate a report on the program under paragraph (1), including an accounting of how the funds made available to carry out this subsection were used by recipients of grants under this subsection to improve animal care. (e) Regulations The Secretary shall promulgate regulations to carry out this section. Not later than 180 days after the date of the enactment of subsection (d), the Secretary shall promulgate regulations to carry out such subsection. .",
      "versionDate": "2025-08-22",
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
        "name": "Animals",
        "updateDate": "2026-04-06T14:51:00Z"
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
      "date": "2025-08-22",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr5020ih.xml"
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
      "title": "Supporting Our Shelters Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-08-23T08:23:23Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Supporting Our Shelters Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-08-23T08:23:22Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Animal Welfare Act to direct the Secretary of Agriculture to establish a program under which the Secretary will award grants to entities for purposes of supporting the capability of such entities to provide care to animals in their care, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-08-23T08:18:25Z"
    }
  ]
}
```
