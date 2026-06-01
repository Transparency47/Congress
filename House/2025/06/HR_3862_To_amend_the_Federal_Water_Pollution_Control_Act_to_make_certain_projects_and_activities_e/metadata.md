# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/3862?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/3862
- Title: Clean Water SRF Parity Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 3862
- Origin chamber: House
- Introduced date: 2025-06-10
- Update date: 2026-04-07T08:05:45Z
- Update date including text: 2026-04-07T08:05:45Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-06-10: Introduced in House
- 2025-06-10 - IntroReferral: Introduced in House
- 2025-06-10 - IntroReferral: Introduced in House
- 2025-06-10 - IntroReferral: Referred to the House Committee on Transportation and Infrastructure.
- 2025-06-11 - Committee: Referred to the Subcommittee on Water Resources and Environment.
- Latest action: 2025-06-10: Introduced in House

## Actions

- 2025-06-10 - IntroReferral: Introduced in House
- 2025-06-10 - IntroReferral: Introduced in House
- 2025-06-10 - IntroReferral: Referred to the House Committee on Transportation and Infrastructure.
- 2025-06-11 - Committee: Referred to the Subcommittee on Water Resources and Environment.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-06-10",
    "latestAction": {
      "actionDate": "2025-06-10",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/3862",
    "number": "3862",
    "originChamber": "House",
    "policyArea": {
      "name": "Environmental Protection"
    },
    "sponsors": [
      {
        "bioguideId": "B001295",
        "district": "12",
        "firstName": "Mike",
        "fullName": "Rep. Bost, Mike [R-IL-12]",
        "lastName": "Bost",
        "party": "R",
        "state": "IL"
      }
    ],
    "title": "Clean Water SRF Parity Act of 2025",
    "type": "HR",
    "updateDate": "2026-04-07T08:05:45Z",
    "updateDateIncludingText": "2026-04-07T08:05:45Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-06-11",
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
      "actionDate": "2025-06-10",
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
      "actionDate": "2025-06-10",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-06-10",
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
          "date": "2025-06-10T14:02:15Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Transportation and Infrastructure Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": {
              "date": "2025-06-11T20:30:45Z",
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

## API Data: cosponsors

```json
{
  "cosponsors": [
    {
      "bioguideId": "G000559",
      "district": "8",
      "firstName": "John",
      "fullName": "Rep. Garamendi, John [D-CA-8]",
      "isOriginalCosponsor": "True",
      "lastName": "Garamendi",
      "party": "D",
      "sponsorshipDate": "2025-06-10",
      "state": "CA"
    },
    {
      "bioguideId": "B001327",
      "district": "8",
      "firstName": "Robert",
      "fullName": "Rep. Bresnahan, Robert P. [R-PA-8]",
      "isOriginalCosponsor": "False",
      "lastName": "Bresnahan",
      "middleName": "P.",
      "party": "R",
      "sponsorshipDate": "2025-07-02",
      "state": "PA"
    },
    {
      "bioguideId": "N000188",
      "district": "1",
      "firstName": "Donald",
      "fullName": "Rep. Norcross, Donald [D-NJ-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Norcross",
      "party": "D",
      "sponsorshipDate": "2025-07-29",
      "state": "NJ"
    },
    {
      "bioguideId": "T000467",
      "district": "15",
      "firstName": "Glenn",
      "fullName": "Rep. Thompson, Glenn [R-PA-15]",
      "isOriginalCosponsor": "False",
      "lastName": "Thompson",
      "party": "R",
      "sponsorshipDate": "2025-09-04",
      "state": "PA"
    },
    {
      "bioguideId": "C001136",
      "district": "3",
      "firstName": "Herbert",
      "fullName": "Rep. Conaway, Herbert C. [D-NJ-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Conaway",
      "middleName": "C.",
      "party": "D",
      "sponsorshipDate": "2026-04-06",
      "state": "NJ"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr3862ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 3862\nIN THE HOUSE OF REPRESENTATIVES\nJune 10, 2025 Mr. Bost (for himself and Mr. Garamendi ) introduced the following bill; which was referred to the Committee on Transportation and Infrastructure\nA BILL\nTo amend the Federal Water Pollution Control Act to make certain projects and activities eligible for financial assistance under a State water pollution control revolving fund, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Clean Water SRF Parity Act of 2025 .\n#### 2. Projects and activities eligible for assistance\nSection 603 of the Federal Water Pollution Control Act ( 33 U.S.C. 1383 ) is amended\u2014\n**(1)**\nin subsection (c)\u2014\n**(A)**\nin paragraph (11)(B) by striking and at the end;\n**(B)**\nin paragraph (12)(B) by striking the period at the end and inserting ; and ; and\n**(C)**\nby adding at the end the following:\n(13) to any qualified nonprofit entity, as determined by the Administrator, to provide assistance for the construction or acquisition of, or improvements to, a treatment works, or for any other activity described in paragraphs (1) through (10). ;\n**(2)**\nin subsection (i)(3), by adding at the end the following:\n(E) Certain activities ineligible A State may not provide additional subsidization under this subsection to a qualified nonprofit entity for assistance described in subsection (c)(13) or to the owner or operator of a privately owned treatment works for assistance described in subsection (l). ; and\n**(3)**\nby adding at the end the following:\n(l) Special rule for privately owned treatment works (1) In general In any fiscal year funds may be used to provide financial assistance under this section to the owner or operator of a privately owned treatment works for\u2014 (A) improvements to such privately owned treatment works; (B) the construction of, or improvements to, another privately owned treatment works; (C) measures to reduce the demand for privately owned treatment works capacity through water conservation, efficiency, or reuse; (D) measures to reduce the energy consumption needs for privately owned treatment works; (E) measures to increase the security of privately owned treatment works; and (F) any other activity described in paragraphs (1) through (10) of subsection (c). (2) Limitation Financial assistance may only be provided under this subsection to the owner or operator of a privately owned treatment works for activities described in paragraph (1) that primarily and directly benefit the individuals or entities served by the privately owned treatment works, and not the shareholders or owners of the treatment works, as determined by the instrumentality of the State responsible for administering the water pollution control revolving fund through which such financial assistance is provided. .",
      "versionDate": "2025-06-10",
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
        "updateDate": "2025-06-27T13:20:54Z"
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
      "date": "2025-06-10",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr3862ih.xml"
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
      "title": "Clean Water SRF Parity Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-07-30T12:51:40Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Clean Water SRF Parity Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-06-13T06:53:18Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Federal Water Pollution Control Act to make certain projects and activities eligible for financial assistance under a State water pollution control revolving fund, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-06-13T06:48:28Z"
    }
  ]
}
```
