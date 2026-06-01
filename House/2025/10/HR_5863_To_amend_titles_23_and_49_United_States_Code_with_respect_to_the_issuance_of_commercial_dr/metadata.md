# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/5863?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/5863
- Title: No CDLs for Illegals Act
- Congress: 119
- Bill type: HR
- Bill number: 5863
- Origin chamber: House
- Introduced date: 2025-10-28
- Update date: 2026-01-07T09:05:47Z
- Update date including text: 2026-01-07T09:05:47Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, subjects, text, titles

## Timeline

- 2025-10-28: Introduced in House
- 2025-10-28 - IntroReferral: Introduced in House
- 2025-10-28 - IntroReferral: Introduced in House
- 2025-10-28 - IntroReferral: Referred to the House Committee on Transportation and Infrastructure.
- 2025-10-29 - Committee: Referred to the Subcommittee on Highways and Transit.
- Latest action: 2025-10-28: Introduced in House

## Actions

- 2025-10-28 - IntroReferral: Introduced in House
- 2025-10-28 - IntroReferral: Introduced in House
- 2025-10-28 - IntroReferral: Referred to the House Committee on Transportation and Infrastructure.
- 2025-10-29 - Committee: Referred to the Subcommittee on Highways and Transit.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-10-28",
    "latestAction": {
      "actionDate": "2025-10-28",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/5863",
    "number": "5863",
    "originChamber": "House",
    "policyArea": {
      "name": "Transportation and Public Works"
    },
    "sponsors": [
      {
        "bioguideId": "V000133",
        "district": "2",
        "firstName": "Jefferson",
        "fullName": "Rep. Van Drew, Jefferson [R-NJ-2]",
        "lastName": "Van Drew",
        "party": "R",
        "state": "NJ"
      }
    ],
    "title": "No CDLs for Illegals Act",
    "type": "HR",
    "updateDate": "2026-01-07T09:05:47Z",
    "updateDateIncludingText": "2026-01-07T09:05:47Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-10-29",
      "committees": {
        "item": {
          "name": "Highways and Transit Subcommittee",
          "systemCode": "hspw12"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Referred to the Subcommittee on Highways and Transit.",
      "type": "Committee"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-10-28",
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
      "actionDate": "2025-10-28",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-10-28",
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
          "date": "2025-10-28T17:00:15Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Transportation and Infrastructure Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": {
              "date": "2025-10-29T17:02:47Z",
              "name": "Referred to"
            }
          },
          "name": "Highways and Transit Subcommittee",
          "systemCode": "hspw12"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr5863ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 5863\nIN THE HOUSE OF REPRESENTATIVES\nOctober 28, 2025 Mr. Van Drew introduced the following bill; which was referred to the Committee on Transportation and Infrastructure\nA BILL\nTo amend titles 23 and 49, United States Code, with respect to the issuance of commercial driver\u2019s licenses to certain unauthorized individuals, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the No CDLs for Illegals Act .\n#### 2. Commercial driver\u2019s license requirements\n##### (a) In general\nSection 31308 of title 49, United States Code, is amended\u2014\n**(1)**\nin paragraph (1)\u2014\n**(A)**\nin subparagraph (A) by striking and at the end; and\n**(B)**\nby adding at the end the following:\n(C) present valid documentation proving citizenship status, lawful permanent resident status, or a valid work authorization; and (D) present valid documentation of domicile in the State in which the commercial driver\u2019s license is issued; ; and\n**(2)**\nin paragraph (3) by striking and at the end;\n**(3)**\nin paragraph (4)(E) by striking the period and inserting a semicolon; and\n**(4)**\nby adding at the end the following:\n(5) prohibit a State from issuing a commercial driver\u2019s license to an individual who is not domiciled in such State; and (6) require States to use the SAVE system for any non-citizen applicant for a commercial driver\u2019s license and deny any applicant if the SAVE system does not confirm lawful presence of such applicant. .\n##### (b) Penalties\n**(1) In general**\nChapter 1 of title 23, United States Code, is amended by adding at the end the following:\n155. Suspension of funds for licensing unauthorized commercial drivers (a) Suspension Notwithstanding any other provision of law, the Secretary of Transportation shall suspend a State\u2019s apportionment of funds under section 104(b) if the Secretary determines that the State has issued commercial driver\u2019s licenses in contravention of section 31308(6) of title 49. (b) Determination (1) In general The Secretary of Transportation shall, on an annual basis, review the commercial driver\u2019s licensing policies and practices of each State to determine compliance with this section. (2) Information The Secretary may request any information necessary from a State to make such a determination. (c) Reinstatement Funds suspended under subsection (a) shall be reinstated to a State when the Secretary certifies that the State has taken all necessary measures to comply with section 31308(6) of title 49. (d) Applicability This section shall apply to any State that receives funds under section 104(b). .\n**(2) Clerical amendment**\nThe analysis for chapter 1 of title 23, United States Code, is amended by inserting after the item relating to section 154 the following:\n155. Suspension of funds for licensing unauthorized commercial drivers. .\n**(3) Rulemaking**\nThe Secretary of Transportation shall issue such regulations as are necessary to set fines for trucking companies that knowingly employ drivers that do not hold a valid commercial driver\u2019s license that complies with section 31308 of title 49, United States Code.",
      "versionDate": "2025-10-28",
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
        "name": "Transportation and Public Works",
        "updateDate": "2025-11-26T15:27:29Z"
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
      "date": "2025-10-28",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr5863ih.xml"
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
      "title": "No CDLs for Illegals Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-10-30T09:38:15Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "No CDLs for Illegals Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-10-30T09:38:14Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend titles 23 and 49, United States Code, with respect to the issuance of commercial driver's licenses to certain unauthorized individuals, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-10-30T09:33:18Z"
    }
  ]
}
```
