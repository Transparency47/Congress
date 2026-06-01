# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/6468?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/6468
- Title: Rural Residency Planning and Development Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 6468
- Origin chamber: House
- Introduced date: 2025-12-04
- Update date: 2026-05-14T08:08:33Z
- Update date including text: 2026-05-14T08:08:33Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-12-04: Introduced in House
- 2025-12-04 - IntroReferral: Introduced in House
- 2025-12-04 - IntroReferral: Introduced in House
- 2025-12-04 - IntroReferral: Referred to the House Committee on Energy and Commerce.
- Latest action: 2025-12-04: Introduced in House

## Actions

- 2025-12-04 - IntroReferral: Introduced in House
- 2025-12-04 - IntroReferral: Introduced in House
- 2025-12-04 - IntroReferral: Referred to the House Committee on Energy and Commerce.

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
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/6468",
    "number": "6468",
    "originChamber": "House",
    "policyArea": {
      "name": "Health"
    },
    "sponsors": [
      {
        "bioguideId": "M001205",
        "district": "1",
        "firstName": "Carol",
        "fullName": "Rep. Miller, Carol D. [R-WV-1]",
        "lastName": "Miller",
        "party": "R",
        "state": "WV"
      }
    ],
    "title": "Rural Residency Planning and Development Act of 2025",
    "type": "HR",
    "updateDate": "2026-05-14T08:08:33Z",
    "updateDateIncludingText": "2026-05-14T08:08:33Z"
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
          "date": "2025-12-04T14:01:05Z",
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
      "bioguideId": "T000487",
      "district": "2",
      "firstName": "Jill",
      "fullName": "Rep. Tokuda, Jill N. [D-HI-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Tokuda",
      "middleName": "N.",
      "party": "D",
      "sponsorshipDate": "2025-12-04",
      "state": "HI"
    },
    {
      "bioguideId": "S001172",
      "district": "3",
      "firstName": "Adrian",
      "fullName": "Rep. Smith, Adrian [R-NE-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Smith",
      "party": "R",
      "sponsorshipDate": "2025-12-04",
      "state": "NE"
    },
    {
      "bioguideId": "C001125",
      "district": "2",
      "firstName": "Troy",
      "fullName": "Rep. Carter, Troy A. [D-LA-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Carter",
      "middleName": "A.",
      "party": "D",
      "sponsorshipDate": "2025-12-04",
      "state": "LA"
    },
    {
      "bioguideId": "V000138",
      "district": "7",
      "firstName": "Eugene",
      "fullName": "Rep. Vindman, Eugene Simon [D-VA-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Vindman",
      "middleName": "Simon",
      "party": "D",
      "sponsorshipDate": "2025-12-16",
      "state": "VA"
    },
    {
      "bioguideId": "M001219",
      "district": "0",
      "firstName": "James",
      "fullName": "Del. Moylan, James C. [R-GU-At Large]",
      "isOriginalCosponsor": "False",
      "lastName": "Moylan",
      "middleName": "C.",
      "party": "R",
      "sponsorshipDate": "2026-02-09",
      "state": "GU"
    },
    {
      "bioguideId": "B000490",
      "district": "2",
      "firstName": "Sanford",
      "fullName": "Rep. Bishop, Sanford D. [D-GA-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Bishop",
      "middleName": "D.",
      "party": "D",
      "sponsorshipDate": "2026-02-09",
      "state": "GA"
    },
    {
      "bioguideId": "T000467",
      "district": "15",
      "firstName": "Glenn",
      "fullName": "Rep. Thompson, Glenn [R-PA-15]",
      "isOriginalCosponsor": "False",
      "lastName": "Thompson",
      "party": "R",
      "sponsorshipDate": "2026-02-23",
      "state": "PA"
    },
    {
      "bioguideId": "F000481",
      "district": "2",
      "firstName": "Shomari",
      "fullName": "Rep. Figures, Shomari [D-AL-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Figures",
      "party": "D",
      "sponsorshipDate": "2026-04-16",
      "state": "AL"
    },
    {
      "bioguideId": "B001318",
      "district": "0",
      "firstName": "Becca",
      "fullName": "Rep. Balint, Becca [D-VT-At Large]",
      "isOriginalCosponsor": "False",
      "lastName": "Balint",
      "party": "D",
      "sponsorshipDate": "2026-04-28",
      "state": "VT"
    },
    {
      "bioguideId": "D000629",
      "district": "3",
      "firstName": "Sharice",
      "fullName": "Rep. Davids, Sharice [D-KS-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Davids",
      "party": "D",
      "sponsorshipDate": "2026-05-13",
      "state": "KS"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6468ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 6468\nIN THE HOUSE OF REPRESENTATIVES\nDecember 4, 2025 Mrs. Miller of West Virginia (for herself, Ms. Tokuda , Mr. Smith of Nebraska , and Mr. Carter of Louisiana ) introduced the following bill; which was referred to the Committee on Energy and Commerce\nA BILL\nTo amend the Public Health Service Act to authorize rural residency planning and development grant programs, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Rural Residency Planning and Development Act of 2025 .\n#### 2. Rural residency planning and development programs\nTitle III of the Public Health Service Act ( 42 U.S.C. 241 et seq. ) is amended by inserting after section 330A\u20132 ( 42 U.S.C. 254c\u20131b ) the following:\n330A\u20133. Rural residency planning and development program and rural residency planning and development technical assistance program (a) Rural residency planning and development program (1) Grants (A) In general The Secretary may award grants to eligible entities to establish new rural residency programs (including adding new rural training sites to existing rural track programs). (B) Funding Grants awarded under this subsection may be fully funded at the time of the award. (C) Term The term of a grant under this subsection shall be 3 years and may be extended at the discretion of the Secretary. (2) Applications (A) In general To be eligible to receive a grant under this subsection, an eligible entity shall prepare and submit to the Secretary an application at such time, in such manner, and containing such information as the Secretary may require, including a description of the pathway of the rural residency program as described in subparagraph (B). (B) Pathway A pathway of a rural residency program supported under this subsection shall be for\u2014 (i) general primary care and high-need specialty care, including family medicine, internal medicine, preventive medicine, psychiatry, or general surgery; (ii) maternal health and obstetrics, which may be obstetrics and gynecology or family medicine with enhanced obstetrical training; or (iii) any other pathway as determined appropriate by the Secretary. (b) Rural residency planning and development technical assistance program (1) Grants (A) In general The Secretary may award grants to eligible entities to provide technical assistance to awardees of and potential applicants of the program described in subsection (b). (B) Funding Grants awarded under this subsection may be fully funded at the time of the award. (C) Term The term of a grant under this subsection shall be 4 years and may be extended at the discretion of the Secretary. (2) Applications To be eligible to receive a grant under this subsection, an eligible entity shall prepare and submit to the Secretary an application at such time, in such manner, and containing such information as the Secretary may require. (c) Definitions In this section: (1) Eligible entity The term eligible entity \u2014 (A) means\u2014 (i) a domestic public or private nonprofit or for-profit entity; or (ii) an Indian Tribe or Tribal organization; and (B) may include faith-based or community-based organizations, rural hospitals, rural community-based ambulatory patient care centers (including rural health clinics), health centers operated by an Indian Tribe, Tribal organization, or urban Indian organization, graduate medical education consortiums (including institutions of higher education, such as schools of allopathic medicine, schools of osteopathic medicine, or historically Black colleges or universities), or other organizations as determined appropriate by the Secretary. (2) Rural residency program The term rural residency program means a physician residency program, including a rural track program, accredited by the Accreditation Council for Graduate Medical Education (or a similar body) that\u2014 (A) trains residents in rural areas (as defined by the Secretary) for more than 50 percent of the total time of their residency; and (B) primarily focuses on producing physicians who will practice in rural areas, as defined by the Secretary. (d) Authorization of appropriations (1) In general There is authorized to be appropriated to carry out this section $12,700,000 for each of fiscal years 2026 through 2030. (2) Availability Any amounts appropriated under paragraph (1) shall remain available to the Secretary until expended. .",
      "versionDate": "2025-12-04",
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
        "actionDate": "2025-06-10",
        "text": "Referred to the Committee on Energy and Commerce, and in addition to the Committee on Ways and Means, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned."
      },
      "number": "3890",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Resident Physician Shortage Reduction Act of 2025",
      "type": "HR"
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
        "updateDate": "2026-01-09T13:13:27Z"
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
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6468ih.xml"
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
      "title": "Rural Residency Planning and Development Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-01-07T06:23:31Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Rural Residency Planning and Development Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-01-07T06:23:31Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Public Health Service Act to authorize rural residency planning and development grant programs, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-01-07T06:18:14Z"
    }
  ]
}
```
