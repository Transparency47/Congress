# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/3459?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/3459
- Title: Empty Lots to Housing Act
- Congress: 119
- Bill type: HR
- Bill number: 3459
- Origin chamber: House
- Introduced date: 2025-05-15
- Update date: 2026-05-21T08:07:40Z
- Update date including text: 2026-05-21T08:07:40Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-05-15: Introduced in House
- 2025-05-15 - IntroReferral: Introduced in House
- 2025-05-15 - IntroReferral: Introduced in House
- 2025-05-15 - IntroReferral: Referred to the House Committee on Transportation and Infrastructure.
- 2025-05-15 - Committee: Referred to the Subcommittee on Highways and Transit.
- Latest action: 2025-05-15: Introduced in House

## Actions

- 2025-05-15 - IntroReferral: Introduced in House
- 2025-05-15 - IntroReferral: Introduced in House
- 2025-05-15 - IntroReferral: Referred to the House Committee on Transportation and Infrastructure.
- 2025-05-15 - Committee: Referred to the Subcommittee on Highways and Transit.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-05-15",
    "latestAction": {
      "actionDate": "2025-05-15",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/3459",
    "number": "3459",
    "originChamber": "House",
    "policyArea": {
      "name": "Transportation and Public Works"
    },
    "sponsors": [
      {
        "bioguideId": "M001225",
        "district": "15",
        "firstName": "Kevin",
        "fullName": "Rep. Mullin, Kevin [D-CA-15]",
        "lastName": "Mullin",
        "party": "D",
        "state": "CA"
      }
    ],
    "title": "Empty Lots to Housing Act",
    "type": "HR",
    "updateDate": "2026-05-21T08:07:40Z",
    "updateDateIncludingText": "2026-05-21T08:07:40Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-05-15",
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
      "actionDate": "2025-05-15",
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
      "actionDate": "2025-05-15",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-05-15",
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
          "date": "2025-05-15T14:00:15Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Transportation and Infrastructure Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": {
              "date": "2025-05-15T21:20:55Z",
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

## API Data: cosponsors

```json
{
  "cosponsors": [
    {
      "bioguideId": "E000246",
      "district": "11",
      "firstName": "Chuck",
      "fullName": "Rep. Edwards, Chuck [R-NC-11]",
      "isOriginalCosponsor": "True",
      "lastName": "Edwards",
      "party": "R",
      "sponsorshipDate": "2025-05-15",
      "state": "NC"
    },
    {
      "bioguideId": "F000466",
      "district": "1",
      "firstName": "Brian",
      "fullName": "Rep. Fitzpatrick, Brian K. [R-PA-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Fitzpatrick",
      "middleName": "K.",
      "party": "R",
      "sponsorshipDate": "2025-05-21",
      "state": "PA"
    },
    {
      "bioguideId": "P000608",
      "district": "50",
      "firstName": "Scott",
      "fullName": "Rep. Peters, Scott H. [D-CA-50]",
      "isOriginalCosponsor": "False",
      "lastName": "Peters",
      "middleName": "H.",
      "party": "D",
      "sponsorshipDate": "2025-05-21",
      "state": "CA"
    },
    {
      "bioguideId": "T000488",
      "district": "13",
      "firstName": "Shri",
      "fullName": "Rep. Thanedar, Shri [D-MI-13]",
      "isOriginalCosponsor": "False",
      "lastName": "Thanedar",
      "party": "D",
      "sponsorshipDate": "2025-05-21",
      "state": "MI"
    },
    {
      "bioguideId": "G000598",
      "district": "42",
      "firstName": "Robert",
      "fullName": "Rep. Garcia, Robert [D-CA-42]",
      "isOriginalCosponsor": "False",
      "lastName": "Garcia",
      "party": "D",
      "sponsorshipDate": "2025-06-04",
      "state": "CA"
    },
    {
      "bioguideId": "A000148",
      "district": "4",
      "firstName": "Jake",
      "fullName": "Rep. Auchincloss, Jake [D-MA-4]",
      "isOriginalCosponsor": "False",
      "lastName": "Auchincloss",
      "party": "D",
      "sponsorshipDate": "2025-06-12",
      "state": "MA"
    },
    {
      "bioguideId": "G000604",
      "district": "2",
      "firstName": "Maggie",
      "fullName": "Rep. Goodlander, Maggie [D-NH-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Goodlander",
      "party": "D",
      "sponsorshipDate": "2025-07-10",
      "state": "NH"
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
      "sponsorshipDate": "2025-08-19",
      "state": "PA"
    },
    {
      "bioguideId": "D000629",
      "district": "3",
      "firstName": "Sharice",
      "fullName": "Rep. Davids, Sharice [D-KS-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Davids",
      "party": "D",
      "sponsorshipDate": "2025-08-19",
      "state": "KS"
    },
    {
      "bioguideId": "N000193",
      "district": "3",
      "firstName": "Zachary",
      "fullName": "Rep. Nunn, Zachary [R-IA-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Nunn",
      "party": "R",
      "sponsorshipDate": "2025-09-30",
      "state": "IA"
    },
    {
      "bioguideId": "H001090",
      "district": "9",
      "firstName": "Josh",
      "fullName": "Rep. Harder, Josh [D-CA-9]",
      "isOriginalCosponsor": "False",
      "lastName": "Harder",
      "party": "D",
      "sponsorshipDate": "2025-10-24",
      "state": "CA"
    },
    {
      "bioguideId": "H001066",
      "district": "4",
      "firstName": "Steven",
      "fullName": "Rep. Horsford, Steven [D-NV-4]",
      "isOriginalCosponsor": "False",
      "lastName": "Horsford",
      "party": "D",
      "sponsorshipDate": "2025-12-11",
      "state": "NV"
    },
    {
      "bioguideId": "F000483",
      "district": "30",
      "firstName": "Laura",
      "fullName": "Rep. Friedman, Laura [D-CA-30]",
      "isOriginalCosponsor": "False",
      "lastName": "Friedman",
      "party": "D",
      "sponsorshipDate": "2026-01-20",
      "state": "CA"
    },
    {
      "bioguideId": "W000797",
      "district": "25",
      "firstName": "Debbie",
      "fullName": "Rep. Wasserman Schultz, Debbie [D-FL-25]",
      "isOriginalCosponsor": "False",
      "lastName": "Wasserman Schultz",
      "party": "D",
      "sponsorshipDate": "2026-05-20",
      "state": "FL"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr3459ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 3459\nIN THE HOUSE OF REPRESENTATIVES\nMay 15, 2025 Mr. Mullin (for himself and Mr. Edwards ) introduced the following bill; which was referred to the Committee on Transportation and Infrastructure\nA BILL\nTo amend title 23, United States Code, to authorize real property acquired with assistance under chapter 1 of such title to be transferred to certain entities for the development of transit-oriented dwelling units, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Empty Lots to Housing Act .\n#### 2. Transfer of real property no longer needed\n##### (a) In general\nChapter 1 of title 23, United States Code, is amended by adding at the end the following:\n180. Transfer of real property no longer needed (a) In general If a recipient of assistance under this chapter decides real property acquired at least in part with such assistance is no longer needed for the purpose for which such real property was acquired, the Secretary may authorize the recipient to transfer such real property, with no further obligation to the Government, to\u2014 (1) a local governmental authority or nonprofit organization for the development of transit-oriented dwelling unit; or (2) to a third-party entity for the development of transit-oriented dwelling units, if the Secretary determines that\u2014 (A) a local government authority or nonprofit organization is unable to receive the real property; (B) the overall benefit of allowing the transfer of the real property is greater than the interest of the Government in selling the property, after considering fair market value and other factors; and (C) the third-party entity has demonstrated a satisfactory history of construction or operating an affordable housing development. (b) Authorization by the Secretary The Secretary may only authorize a transfer under this section if the Secretary has determined that the recipient has contractually required the entity to which the recipient proposes to transfer the real property to, for the duration of the 30-year period beginning on the date such real property is transferred to such entity\u2014 (1) reserve not less than 40 percent of any housing units developed on such real property for families whose adjusted income, as such term is defined by the Secretary, in consultation with the Secretary of Housing and Urban Development by rule, is less than or equal to 60 percent of the area median income and offer such units to such families with a rent that does not exceed 30 percent of the adjusted income of such family; and (2) of the 40 percent of unit reserved under paragraph (1), reserve not less than 20 percent of such units for families whose income is less than or equal to 30 percent of the area median income. .\n##### (b) Clerical amendment\nThe analysis for chapter 1 of title 23, United States Code, is amended by adding at the end the following:\n180. Transfer of real property no longer needed. .",
      "versionDate": "2025-05-15",
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
        "updateDate": "2025-05-29T15:09:23Z"
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
      "date": "2025-05-15",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr3459ih.xml"
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
      "title": "Empty Lots to Housing Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-05-27T04:23:43Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Empty Lots to Housing Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-05-27T04:23:42Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend title 23, United States Code, to authorize real property acquired with assistance under chapter 1 of such title to be transferred to certain entities for the development of transit-oriented dwelling units, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-05-27T04:18:25Z"
    }
  ]
}
```
