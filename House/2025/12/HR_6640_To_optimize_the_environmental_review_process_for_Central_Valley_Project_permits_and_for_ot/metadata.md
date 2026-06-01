# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/6640?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/6640
- Title: Build Now Act
- Congress: 119
- Bill type: HR
- Bill number: 6640
- Origin chamber: House
- Introduced date: 2025-12-11
- Update date: 2026-04-10T14:36:23Z
- Update date including text: 2026-04-10T14:36:23Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-12-11: Introduced in House
- 2025-12-11 - IntroReferral: Introduced in House
- 2025-12-11 - IntroReferral: Introduced in House
- 2025-12-11 - IntroReferral: Referred to the House Committee on Natural Resources.
- Latest action: 2025-12-11: Introduced in House

## Actions

- 2025-12-11 - IntroReferral: Introduced in House
- 2025-12-11 - IntroReferral: Introduced in House
- 2025-12-11 - IntroReferral: Referred to the House Committee on Natural Resources.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-12-11",
    "latestAction": {
      "actionDate": "2025-12-11",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/6640",
    "number": "6640",
    "originChamber": "House",
    "policyArea": {
      "name": "Environmental Protection"
    },
    "sponsors": [
      {
        "bioguideId": "G000605",
        "district": "13",
        "firstName": "Adam",
        "fullName": "Rep. Gray, Adam [D-CA-13]",
        "lastName": "Gray",
        "party": "D",
        "state": "CA"
      }
    ],
    "title": "Build Now Act",
    "type": "HR",
    "updateDate": "2026-04-10T14:36:23Z",
    "updateDateIncludingText": "2026-04-10T14:36:23Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-12-11",
      "committees": {
        "item": {
          "name": "Natural Resources Committee",
          "systemCode": "hsii00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Natural Resources.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-12-11",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-12-11",
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
          "date": "2025-12-11T16:01:50Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Natural Resources Committee",
      "systemCode": "hsii00",
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
      "bioguideId": "C001059",
      "district": "21",
      "firstName": "Jim",
      "fullName": "Rep. Costa, Jim [D-CA-21]",
      "isOriginalCosponsor": "True",
      "lastName": "Costa",
      "party": "D",
      "sponsorshipDate": "2025-12-11",
      "state": "CA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6640ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 6640\nIN THE HOUSE OF REPRESENTATIVES\nDecember 11, 2025 Mr. Gray (for himself and Mr. Costa ) introduced the following bill; which was referred to the Committee on Natural Resources\nA BILL\nTo optimize the environmental review process for Central Valley Project permits, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Build Now Act .\n#### 2. Central Valley Project Environmental Review Timeline\n##### (a) In general\nNotwithstanding any other provision of law, if a federally issued permit for a CVP enhancement project requires an environmental review, the environmental review shall be completed not later than 1 year after the date on which the permit application is submitted by the permit applicant.\n##### (b) Failure To meet deadline\nIf the agency responsible for carrying out an environmental review described in subsection (a) is unable to meet the timeline under that subsection, the head of the agency issuing the applicable permit shall\u2014\n**(1)**\nwith the approval of the permit applicant, grant an extension for the environmental review; or\n**(2)**\ndeny the permit.\n##### (c) Action after denial\n**(1) In general**\nAn applicant for a permit that is denied due to a failure to meet the timeline under this section may re-apply for the permit at any time after the denial is issued.\n**(2) Lead agency**\nIf an applicant re-applies for a permit under paragraph (1), the head of the agency responsible for carrying out the environmental review required under the previous application shall furnish to the applicant, to the extent permitted by law, any information gathered as part of, or related to, such environmental review to facilitate an expedited environmental review for the new application.\n##### (d) Definitions\nIn this Act:\n**(1) CVP enhancement project**\nThe term CVP enhancement project means a project with a primary purpose of supporting, enhancing, or maintaining the Central Valley Project and related infrastructure, including\u2014\n**(A)**\ngroundwater recharge projects;\n**(B)**\naquifer storage projects; and\n**(C)**\nwater source substitution projects.\n**(2) Environmental review**\nThe term environmental review means fulfilling the requirements applicable to a CVP enhancement project permit under the National Environmental Policy Act of 1969 ( 42 U.S.C. 4331 et seq. ) and section 7 of the Endangered Species Act of 1973 ( 16 U.S.C. 1536 ).",
      "versionDate": "2025-12-11",
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
        "updateDate": "2026-04-10T14:36:23Z"
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
      "date": "2025-12-11",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6640ih.xml"
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
      "title": "Build Now Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-01-03T06:53:18Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Build Now Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-01-03T06:53:18Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To optimize the environmental review process for Central Valley Project permits, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-01-03T06:48:24Z"
    }
  ]
}
```
