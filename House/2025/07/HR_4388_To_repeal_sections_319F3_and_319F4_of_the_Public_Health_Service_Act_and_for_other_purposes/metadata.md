# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/4388?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/4388
- Title: PREP Repeal Act
- Congress: 119
- Bill type: HR
- Bill number: 4388
- Origin chamber: House
- Introduced date: 2025-07-15
- Update date: 2025-12-16T09:05:27Z
- Update date including text: 2025-12-16T09:05:27Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-07-15: Introduced in House
- 2025-07-15 - IntroReferral: Introduced in House
- 2025-07-15 - IntroReferral: Introduced in House
- 2025-07-15 - IntroReferral: Referred to the House Committee on Energy and Commerce.
- Latest action: 2025-07-15: Introduced in House

## Actions

- 2025-07-15 - IntroReferral: Introduced in House
- 2025-07-15 - IntroReferral: Introduced in House
- 2025-07-15 - IntroReferral: Referred to the House Committee on Energy and Commerce.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-07-15",
    "latestAction": {
      "actionDate": "2025-07-15",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/4388",
    "number": "4388",
    "originChamber": "House",
    "policyArea": {
      "name": "Health"
    },
    "sponsors": [
      {
        "bioguideId": "M001184",
        "district": "4",
        "firstName": "Thomas",
        "fullName": "Rep. Massie, Thomas [R-KY-4]",
        "lastName": "Massie",
        "party": "R",
        "state": "KY"
      }
    ],
    "title": "PREP Repeal Act",
    "type": "HR",
    "updateDate": "2025-12-16T09:05:27Z",
    "updateDateIncludingText": "2025-12-16T09:05:27Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-07-15",
      "committees": {
        "item": {
          "name": "Energy and Commerce Committee",
          "systemCode": "hsif00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Energy and Commerce.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-07-15",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-07-15",
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
          "date": "2025-07-15T14:03:10Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Energy and Commerce Committee",
      "systemCode": "hsif00",
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
      "bioguideId": "G000565",
      "district": "9",
      "firstName": "Paul",
      "fullName": "Rep. Gosar, Paul A. [R-AZ-9]",
      "isOriginalCosponsor": "True",
      "lastName": "Gosar",
      "middleName": "A.",
      "party": "R",
      "sponsorshipDate": "2025-07-15",
      "state": "AZ"
    },
    {
      "bioguideId": "D000626",
      "district": "8",
      "firstName": "Warren",
      "fullName": "Rep. Davidson, Warren [R-OH-8]",
      "isOriginalCosponsor": "False",
      "lastName": "Davidson",
      "party": "R",
      "sponsorshipDate": "2025-07-16",
      "state": "OH"
    },
    {
      "bioguideId": "G000576",
      "district": "6",
      "firstName": "Glenn",
      "fullName": "Rep. Grothman, Glenn [R-WI-6]",
      "isOriginalCosponsor": "False",
      "lastName": "Grothman",
      "party": "R",
      "sponsorshipDate": "2025-12-15",
      "state": "WI"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr4388ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 4388\nIN THE HOUSE OF REPRESENTATIVES\nJuly 15, 2025 Mr. Massie (for himself and Mr. Gosar ) introduced the following bill; which was referred to the Committee on Energy and Commerce\nA BILL\nTo repeal sections 319F\u20133 and 319F\u20134 of the Public Health Service Act, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the PREP Repeal Act .\n#### 2. Findings\nCongress finds the following:\n**(1)**\nLiability shields granted under section 319F\u20133 of the Public Health Service Act ( 42 U.S.C. 247d\u20136d ) have undermined public trust and accountability during public health emergencies.\n**(2)**\nThe ability of citizens to seek redress for injury or harm is a fundamental principle of justice and due process.\n**(3)**\nThe Public Readiness and Emergency Preparedness Act ( Public Law 109\u2013148 ) (commonly referred to as the PREP Act ) has enabled regulatory capture and legal immunity for pharmaceutical manufacturers at the expense of individual rights.\n#### 3. Repeal of liability immunity for pandemic products\n##### (a) Repeals\nThe following sections are repealed:\n**(1)**\nSection 319F\u20133 of the Public Health Service Act ( 42 U.S.C. 247d\u20136d ).\n**(2)**\nSection 319F\u20134 of the Public Health Service Act ( 42 U.S.C. 247d\u20136e ).\n##### (b) Rescission\nThe unobligated balances of amounts in the Covered Countermeasure Process Fund, as established by section 319F\u20134(a) of the Public Health Service Act (42 U.S.C. 247d\u20136e(a)), as in effect on the day before the date of enactment of this Act, are rescinded.\n##### (c) References\n**(1) In general**\nAny reference in Federal law to a section described in subsection (a) or a provision thereof shall be construed to be a reference to such section or provision as in effect on the day before the date of enactment of this Act.\n**(2) Amendment**\nSection 565(b)(1) of the Federal Food, Drug, and Cosmetic Act ( 21 U.S.C. 360bbb\u20134(b)(1) ) is amended by striking 319F\u20133, .\n#### 4. Preservation of existing rights\nNothing in this Act shall be construed to limit the ability of any person to pursue civil remedies under Federal or State law for injury or harm arising from the development, administration, or distribution of any\u2014\n**(1)**\ndrug or device (as such terms are defined in section 201 of the Federal Food, Drug, and Cosmetic Act ( 21 U.S.C. 321 ));\n**(2)**\nbiological product (as defined in section 351(i) of the Public Health Service Act ( 42 U.S.C. 262(i) )); or\n**(3)**\ncovered countermeasure (as defined in section 319F\u20133(i) of the Public Health Service Act (42 U.S.C. 247d\u20136d(i)), as in effect on the day before the date of enactment of this Act).\n#### 5. Application\nThis Act, including the repeals under section 3(a), shall only apply with respect to actions, claims, or proceedings that\u2014\n**(1)**\non the date of enactment of this Act, are pending (including actions, claims, or proceedings for which a right of appeal has not been exhausted); or\n**(2)**\nare commenced on or after such date of enactment.\n#### 6. Severability\nIf any provision of this Act or the application thereof to any person or circumstance is held invalid, the remainder of the Act and the application of such provision to other persons or circumstances shall not be affected.",
      "versionDate": "2025-07-15",
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
        "name": "Health",
        "updateDate": "2025-08-01T15:07:39Z"
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
      "date": "2025-07-15",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr4388ih.xml"
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
      "title": "PREP Repeal Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-07-24T01:38:21Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "PREP Repeal Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-07-24T01:38:19Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To repeal sections 319F-3 and 319F-4 of the Public Health Service Act, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-07-24T01:33:22Z"
    }
  ]
}
```
