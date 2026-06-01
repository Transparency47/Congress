# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/7681?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/7681
- Title: HSA’s For All Act
- Congress: 119
- Bill type: HR
- Bill number: 7681
- Origin chamber: House
- Introduced date: 2026-02-25
- Update date: 2026-05-22T08:07:55Z
- Update date including text: 2026-05-22T08:07:55Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2026-02-25: Introduced in House
- 2026-02-25 - IntroReferral: Introduced in House
- 2026-02-25 - IntroReferral: Introduced in House
- 2026-02-25 - IntroReferral: Referred to the House Committee on Ways and Means.
- Latest action: 2026-02-25: Introduced in House

## Actions

- 2026-02-25 - IntroReferral: Introduced in House
- 2026-02-25 - IntroReferral: Introduced in House
- 2026-02-25 - IntroReferral: Referred to the House Committee on Ways and Means.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-02-25",
    "latestAction": {
      "actionDate": "2026-02-25",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/7681",
    "number": "7681",
    "originChamber": "House",
    "policyArea": {
      "name": "Taxation"
    },
    "sponsors": [
      {
        "bioguideId": "B001314",
        "district": "4",
        "firstName": "Aaron",
        "fullName": "Rep. Bean, Aaron [R-FL-4]",
        "lastName": "Bean",
        "party": "R",
        "state": "FL"
      }
    ],
    "title": "HSA\u2019s For All Act",
    "type": "HR",
    "updateDate": "2026-05-22T08:07:55Z",
    "updateDateIncludingText": "2026-05-22T08:07:55Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2026-02-25",
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
      "actionDate": "2026-02-25",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-02-25",
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
          "date": "2026-02-25T14:01:30Z",
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
      "bioguideId": "B001321",
      "district": "7",
      "firstName": "Tom",
      "fullName": "Rep. Barrett, Tom [R-MI-7]",
      "isOriginalCosponsor": "True",
      "lastName": "Barrett",
      "party": "R",
      "sponsorshipDate": "2026-02-25",
      "state": "MI"
    },
    {
      "bioguideId": "H001099",
      "district": "8",
      "firstName": "Mike",
      "fullName": "Rep. Haridopolos, Mike [R-FL-8]",
      "isOriginalCosponsor": "True",
      "lastName": "Haridopolos",
      "party": "R",
      "sponsorshipDate": "2026-02-25",
      "state": "FL"
    },
    {
      "bioguideId": "M001224",
      "district": "1",
      "firstName": "Nathaniel",
      "fullName": "Rep. Moran, Nathaniel [R-TX-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Moran",
      "party": "R",
      "sponsorshipDate": "2026-03-25",
      "state": "TX"
    },
    {
      "bioguideId": "F000471",
      "district": "5",
      "firstName": "Scott",
      "fullName": "Rep. Fitzgerald, Scott [R-WI-5]",
      "isOriginalCosponsor": "False",
      "lastName": "Fitzgerald",
      "party": "R",
      "sponsorshipDate": "2026-04-22",
      "state": "WI"
    },
    {
      "bioguideId": "M001213",
      "district": "1",
      "firstName": "Blake",
      "fullName": "Rep. Moore, Blake D. [R-UT-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Moore",
      "middleName": "D.",
      "party": "R",
      "sponsorshipDate": "2026-05-21",
      "state": "UT"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7681ih.xml",
      "text": "I\n119th CONGRESS\n2d Session\nH. R. 7681\nIN THE HOUSE OF REPRESENTATIVES\nFebruary 25, 2026 Mr. Bean of Florida (for himself, Mr. Barrett , and Mr. Haridopolos ) introduced the following bill; which was referred to the Committee on Ways and Means\nA BILL\nTo amend the Internal Revenue Code of 1986 to expand eligibility for health savings accounts, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the HSA\u2019s For All Act .\n#### 2. Expansion of eligibility for health savings accounts\n##### (a) In general\nSection 223(c)(1) of the Internal Revenue Code of 1986 is amended to read as follows:\n(1) Eligible individual The term eligible individual means, with respect to any month, any individual if such individual is covered under a covered health plan as of the 1st day of such month. .\n##### (b) Covered health plan\nSection 223(c)(2) of such Code is amended to read as follows:\n(2) Covered health plan The term covered health plan means\u2014 (A) any qualified health plan (as defined in section 1301(a) of the Patient Protection and Affordable Care Act) offered through an Exchange established under such Act, or (B) any group health plan (as defined in section 2791 of the Public Health Service Act). .\n##### (c) Conforming amendments\n**(1)**\nSection 26(b)(2)(S) of such Code is amended by striking high deductible health plan and inserting covered health plan .\n**(2)**\nSection 223 of such Code, as amended by the preceding provisions of this Act, is amended by striking high deductible health plan each place it appears and inserting covered health plan in each such place.\n**(3)**\nSection 223(b)(8)(B) of such Code is amended by striking high deductible health plan in the heading and inserting covered health plan .\n**(4)**\nSection 223(c) of such Code, as amended by the preceding provisions of this Act, is amended\u2014\n**(A)**\nby striking paragraph (3), and\n**(B)**\nby redesignating paragraphs (4) and (5) as paragraphs (3) and (4), respectively.\n**(5)**\nSection 223(g)(1) of such Code is amended\u2014\n**(A)**\nin the matter preceding subparagraph (A), by striking subsections (b)(2), (c)(2)(A), and in the case of taxable years beginning after 2026, (c)(1)(E)(ii)(II) and inserting subsection (b)(2) ,\n**(B)**\nin subparagraph (B), by striking for calendar year 2016 and all that follows through calendar year 2025 . and inserting calendar year 1997 for calendar year 2016 in subparagraph (A)(ii) thereof. , and\n**(C)**\nin the flush sentence at the end, by striking subsections (b)(2), (c)(1)(E)(ii)(II), and (c)(2)(A) and inserting subsection (b)(2) .\n**(6)**\nSection 408(d)(9) of such Code is amended\u2014\n**(A)**\nby striking high deductible health plan each place it appears and inserting covered health plan in each such place, and\n**(B)**\nin subparagraph (D), by striking high deductible health plan in the heading and inserting covered health plan .\n##### (d) Effective date\nThe amendments made by this section shall apply to taxable years beginning after December 31, 2026.",
      "versionDate": "2026-02-25",
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
        "updateDate": "2026-03-13T15:24:24Z"
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
      "date": "2026-02-25",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7681ih.xml"
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
      "title": "HSA\u2019s For All Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-03-12T04:23:29Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "HSA\u2019s For All Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-03-12T04:23:28Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Internal Revenue Code of 1986 to expand eligibility for health savings accounts, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-03-12T04:18:28Z"
    }
  ]
}
```
