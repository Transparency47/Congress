# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/2364?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/hr/2364
- Title: Helene Small Business Recovery Act
- Congress: 119
- Bill type: HR
- Bill number: 2364
- Origin chamber: House
- Introduced date: 2025-03-26
- Update date: 2025-06-12T08:07:13Z
- Update date including text: 2025-06-12T08:07:13Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-03-26: Introduced in House
- 2025-03-26 - IntroReferral: Introduced in House
- 2025-03-26 - IntroReferral: Introduced in House
- 2025-03-26 - IntroReferral: Referred to the House Committee on Transportation and Infrastructure.
- 2025-03-26 - Committee: Referred to the Subcommittee on Economic Development, Public Buildings, and Emergency Management.
- Latest action: 2025-03-26: Introduced in House

## Actions

- 2025-03-26 - IntroReferral: Introduced in House
- 2025-03-26 - IntroReferral: Introduced in House
- 2025-03-26 - IntroReferral: Referred to the House Committee on Transportation and Infrastructure.
- 2025-03-26 - Committee: Referred to the Subcommittee on Economic Development, Public Buildings, and Emergency Management.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-03-26",
    "latestAction": {
      "actionDate": "2025-03-26",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/hr/2364",
    "number": "2364",
    "originChamber": "House",
    "policyArea": {
      "name": "Emergency Management"
    },
    "sponsors": [
      {
        "bioguideId": "E000246",
        "district": "11",
        "firstName": "Chuck",
        "fullName": "Rep. Edwards, Chuck [R-NC-11]",
        "lastName": "Edwards",
        "party": "R",
        "state": "NC"
      }
    ],
    "title": "Helene Small Business Recovery Act",
    "type": "HR",
    "updateDate": "2025-06-12T08:07:13Z",
    "updateDateIncludingText": "2025-06-12T08:07:13Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-03-26",
      "committees": {
        "item": {
          "name": "Economic Development, Public Buildings, and Emergency Management Subcommittee",
          "systemCode": "hspw13"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Referred to the Subcommittee on Economic Development, Public Buildings, and Emergency Management.",
      "type": "Committee"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-03-26",
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
      "actionDate": "2025-03-26",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-03-26",
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
          "date": "2025-03-26T14:05:10Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Transportation and Infrastructure Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": {
              "date": "2025-03-26T21:09:01Z",
              "name": "Referred to"
            }
          },
          "name": "Economic Development, Public Buildings, and Emergency Management Subcommittee",
          "systemCode": "hspw13"
        }
      },
      "systemCode": "hspw00",
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
      "sponsorshipDate": "2025-03-26",
      "state": "NC"
    },
    {
      "bioguideId": "F000450",
      "district": "5",
      "firstName": "Virginia",
      "fullName": "Rep. Foxx, Virginia [R-NC-5]",
      "isOriginalCosponsor": "True",
      "lastName": "Foxx",
      "party": "R",
      "sponsorshipDate": "2025-03-26",
      "state": "NC"
    },
    {
      "bioguideId": "R000603",
      "district": "7",
      "firstName": "David",
      "fullName": "Rep. Rouzer, David [R-NC-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Rouzer",
      "party": "R",
      "sponsorshipDate": "2025-03-27",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr2364ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 2364\nIN THE HOUSE OF REPRESENTATIVES\nMarch 26, 2025 Mr. Edwards (for himself, Mr. Davis of North Carolina , and Ms. Foxx ) introduced the following bill; which was referred to the Committee on Transportation and Infrastructure\nA BILL\nTo provide for a waiver of duplication of benefits for certain assistance under the Robert T. Stafford Disaster Relief and Emergency Assistance Act as a result of a major disaster or emergency, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Helene Small Business Recovery Act .\n#### 2. Waiver of duplication of benefits\n##### (a) Waiver of general prohibition\n**(1) In general**\nThe President may waive the general prohibition provided in section 312(a) of the Robert T. Stafford Disaster Relief and Emergency Assistance Act ( 42 U.S.C. 5155(a) ) upon request of a Governor on behalf of the State or on behalf of a person, business concern, or any other entity suffering losses as a result of a major disaster or emergency, if the President finds such waiver is in the public interest and will not result in waste, fraud, or abuse. In making this decision, the President may consider the following:\n**(A)**\nThe recommendations of the Administration of the Federal Emergency Management Agency made in consultation with the Federal agency or agencies administering the duplicative program.\n**(B)**\nIf a wavier is granted, the assistance to be funded is cost effective.\n**(C)**\nEquity and good conscience.\n**(D)**\nOther matters of public policy considered appropriate by the President.\n**(2) Grant or denial of waiver**\nA request under paragraph (1) shall be granted or denied not later than 45 days after submission of such request.\n**(3) Prohibition on determination that loan is a duplication**\nNotwithstanding section 312(c) of the Robert T. Stafford Disaster Relief and Emergency Assistance Act ( 42 U.S.C. 5155(c) ), in carrying out paragraph (1), the President may not determine that a loan is a duplication of assistance, provided that all Federal assistance is used toward a loss suffered as a result of the major disaster or emergency.\n**(4) Prohibition on income threshold**\nIn carrying out this subsection, no income threshold may be applied to limit the eligibility of a recipient from qualifying for a waiver.\n##### (b) Applicability\nSubsection (a) shall apply to the provision of assistance in response to a major disaster declared by the President under the Robert T. Stafford Disaster Relief and Emergency Assistance Act that occurred in calendar year 2023 or 2024.",
      "versionDate": "2025-03-26",
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
        "name": "Emergency Management",
        "updateDate": "2025-05-21T18:01:10Z"
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
      "date": "2025-03-26",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr2364ih.xml"
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
      "title": "Helene Small Business Recovery Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-04-04T05:08:24Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Helene Small Business Recovery Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-04-04T05:08:19Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To provide for a waiver of duplication of benefits for certain assistance under the Robert T. Stafford Disaster Relief and Emergency Assistance Act as a result of a major disaster or emergency, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-04-04T05:03:41Z"
    }
  ]
}
```
