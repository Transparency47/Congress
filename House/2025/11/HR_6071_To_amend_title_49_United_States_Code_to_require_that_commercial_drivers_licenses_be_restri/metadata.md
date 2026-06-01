# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/6071?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/6071
- Title: Safer Truckers Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 6071
- Origin chamber: House
- Introduced date: 2025-11-17
- Update date: 2026-01-07T09:05:43Z
- Update date including text: 2026-01-07T09:05:43Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-11-17: Introduced in House
- 2025-11-17 - IntroReferral: Introduced in House
- 2025-11-17 - IntroReferral: Introduced in House
- 2025-11-17 - IntroReferral: Referred to the House Committee on Transportation and Infrastructure.
- 2025-11-18 - Committee: Referred to the Subcommittee on Highways and Transit.
- Latest action: 2025-11-17: Introduced in House

## Actions

- 2025-11-17 - IntroReferral: Introduced in House
- 2025-11-17 - IntroReferral: Introduced in House
- 2025-11-17 - IntroReferral: Referred to the House Committee on Transportation and Infrastructure.
- 2025-11-18 - Committee: Referred to the Subcommittee on Highways and Transit.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-11-17",
    "latestAction": {
      "actionDate": "2025-11-17",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/6071",
    "number": "6071",
    "originChamber": "House",
    "policyArea": {
      "name": "Transportation and Public Works"
    },
    "sponsors": [
      {
        "bioguideId": "S001214",
        "district": "17",
        "firstName": "W.",
        "fullName": "Rep. Steube, W. Gregory [R-FL-17]",
        "lastName": "Steube",
        "party": "R",
        "state": "FL"
      }
    ],
    "title": "Safer Truckers Act of 2025",
    "type": "HR",
    "updateDate": "2026-01-07T09:05:43Z",
    "updateDateIncludingText": "2026-01-07T09:05:43Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-11-18",
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
      "actionDate": "2025-11-17",
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
      "actionDate": "2025-11-17",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-11-17",
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
          "date": "2025-11-17T17:03:10Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Transportation and Infrastructure Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": {
              "date": "2025-11-18T18:20:00Z",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6071ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 6071\nIN THE HOUSE OF REPRESENTATIVES\nNovember 17, 2025 Mr. Steube introduced the following bill; which was referred to the Committee on Transportation and Infrastructure\nA BILL\nTo amend title 49, United States Code, to require that commercial driver\u2019s licenses be restricted to United States citizens, lawful permanent residents, and individuals authorized by U.S. Citizenship and Immigration Services to engage in employment in the United States that includes driving a commercial motor vehicle, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Safer Truckers Act of 2025 .\n#### 2. Establishment of residency requirements for CDLs\nSection 31308(1) of title 49, United States Code, is amended\u2014\n**(1)**\nin subparagraph (A), by striking and at the end;\n**(2)**\nin subparagraph (B), by adding and after the semicolon at the end; and\n**(3)**\nby adding at the end the following:\n(C) be a citizen or lawful permanent resident of the United States or authorized by U.S. Citizenship and Immigration Services to engage in employment in the United States that includes driving a commercial motor vehicle; .\n#### 3. Reporting requirements and withholding of amounts for noncompliance\nSection 31311(a) of title 49, United States Code, is amended by adding at the end the following:\n(26) The State may issue a commercial driver\u2019s license to an individual only if the individual is a citizen or lawful permanent resident of the United States or is authorized by U.S. Citizenship and Immigration Services to engage in employment in the United States that includes driving a commercial motor vehicle. (27) Not later than 180 days after the date of enactment of this paragraph, and by December 31 of each year thereafter, the State shall submit to the Secretary a report describing the policies and actions of the State to uphold and enforce the English-language proficiency requirements for drivers of commercial motor vehicles, as described in section 391.11(b)(2) of title 49, Code of Federal Regulations (or a successor regulation). .",
      "versionDate": "2025-11-17",
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
        "actionDate": "2025-09-03",
        "text": "Read twice and referred to the Committee on Commerce, Science, and Transportation."
      },
      "number": "2690",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Safer Truckers Act of 2025",
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
        "updateDate": "2025-12-01T17:13:04Z"
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
      "date": "2025-11-17",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6071ih.xml"
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
      "title": "Safer Truckers Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-11-29T05:38:19Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Safer Truckers Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-11-29T05:38:18Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend title 49, United States Code, to require that commercial driver's licenses be restricted to United States citizens, lawful permanent residents, and individuals authorized by U.S. Citizenship and Immigration Services to engage in employment in the United States that includes driving a commercial motor vehicle, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-11-29T05:33:23Z"
    }
  ]
}
```
