# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/6668?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/6668
- Title: Clean Water Standards for PFAS Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 6668
- Origin chamber: House
- Introduced date: 2025-12-11
- Update date: 2026-02-03T09:05:22Z
- Update date including text: 2026-02-03T09:05:22Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-12-11: Introduced in House
- 2025-12-11 - IntroReferral: Introduced in House
- 2025-12-11 - IntroReferral: Introduced in House
- 2025-12-11 - IntroReferral: Referred to the House Committee on Transportation and Infrastructure.
- 2026-02-02 - Committee: Referred to the Subcommittee on Water Resources and Environment.
- Latest action: 2025-12-11: Introduced in House

## Actions

- 2025-12-11 - IntroReferral: Introduced in House
- 2025-12-11 - IntroReferral: Introduced in House
- 2025-12-11 - IntroReferral: Referred to the House Committee on Transportation and Infrastructure.
- 2026-02-02 - Committee: Referred to the Subcommittee on Water Resources and Environment.

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
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/6668",
    "number": "6668",
    "originChamber": "House",
    "policyArea": {
      "name": "Environmental Protection"
    },
    "sponsors": [
      {
        "bioguideId": "P000614",
        "district": "1",
        "firstName": "Chris",
        "fullName": "Rep. Pappas, Chris [D-NH-1]",
        "lastName": "Pappas",
        "party": "D",
        "state": "NH"
      }
    ],
    "title": "Clean Water Standards for PFAS Act of 2025",
    "type": "HR",
    "updateDate": "2026-02-03T09:05:22Z",
    "updateDateIncludingText": "2026-02-03T09:05:22Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-02-02",
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
      "actionDate": "2025-12-11",
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
          "date": "2025-12-11T16:10:05Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Transportation and Infrastructure Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": {
              "date": "2026-02-02T19:38:14Z",
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
      "bioguideId": "F000466",
      "district": "1",
      "firstName": "Brian",
      "fullName": "Rep. Fitzpatrick, Brian K. [R-PA-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Fitzpatrick",
      "middleName": "K.",
      "party": "R",
      "sponsorshipDate": "2025-12-11",
      "state": "PA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6668ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 6668\nIN THE HOUSE OF REPRESENTATIVES\nDecember 11, 2025 Mr. Pappas (for himself and Mr. Fitzpatrick ) introduced the following bill; which was referred to the Committee on Transportation and Infrastructure\nA BILL\nTo establish effluent limitations guidelines and standards and water quality criteria for perfluoroalkyl and polyfluoroalkyl substances under the Federal Water Pollution Control Act, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Clean Water Standards for PFAS Act of 2025 .\n#### 2. Clean Water Act effluent limitations guidelines and standards and water quality criteria for PFAS\n##### (a) Definitions\nIn this section:\n**(1) Administrator**\nThe term Administrator means the Administrator of the Environmental Protection Agency.\n**(2) Effluent limitation**\nThe term effluent limitation has the meaning given the term in section 502 of the Federal Water Pollution Control Act ( 33 U.S.C. 1362 ).\n**(3) Measurable**\nThe term measurable , with respect to a perfluoroalkyl substance, a polyfluoroalkyl substance, or a class of those substances, means that the substance or class of substances is capable of being measured using any test method promulgated under part 136 of title 40, Code of Federal Regulations (or successor regulations).\n**(4) Perfluoroalkyl substance**\nThe term perfluoroalkyl substance means a chemical of which all of the carbon atoms are fully fluorinated carbon atoms.\n**(5) Polyfluoroalkyl substance**\nThe term polyfluoroalkyl substance means a chemical containing at least 1 fully fluorinated carbon atom and at least 1 carbon atom that is not a fully fluorinated carbon atom.\n**(6) Treatment works**\nThe term treatment works has the meaning given the term in section 212 of the Federal Water Pollution Control Act ( 33 U.S.C. 1292 ).\n##### (b) Deadlines\n**(1) Water quality criteria**\nNot later than 3 years after the date of enactment of this Act, the Administrator shall publish in the Federal Register human health water quality criteria under section 304(a)(1) of the Federal Water Pollution Control Act ( 33 U.S.C. 1314(a)(1) ) to address each measurable perfluoroalkyl substance, polyfluoroalkyl substance, and class of those substances.\n**(2) Effluent limitations guidelines and standards for priority industry categories**\nNot later than the following dates, the Administrator shall take final action on a rule establishing effluent limitations guidelines and standards, in accordance with the Federal Water Pollution Control Act ( 33 U.S.C. 1251 et seq. ), for each of the following industry categories for the discharge (including a discharge into a publicly owned treatment works) of each measurable perfluoroalkyl substance, polyfluoroalkyl substance, or class of those substances:\n**(A) During calendar year 2026**\nNot later than September 30, 2026, for the following point source categories:\n**(i)**\nOrganic chemicals, plastics, and synthetic fibers, as identified in part 414 of title 40, Code of Federal Regulations (or successor regulations).\n**(ii)**\nElectroplating, as identified in part 413 of title 40, Code of Federal Regulations (or successor regulations).\n**(iii)**\nMetal finishing, as identified in part 433 of title 40, Code of Federal Regulations (or successor regulations).\n**(B) During calendar year 2027**\nNot later than September 30, 2027, for the following point source categories:\n**(i)**\nTextile mills, as identified in part 410 of title 40, Code of Federal Regulations (or successor regulations).\n**(ii)**\nLandfills, as identified in part 445 of title 40, Code of Federal Regulations (or successor regulations).\n**(C) During calendar year 2028**\nNot later than September 30, 2028, for the following point source categories:\n**(i)**\nLeather tanning and finishing, as identified in part 425 of title 40, Code of Federal Regulations (or successor regulations).\n**(ii)**\nPaint formulating, as identified in part 446 of title 40, Code of Federal Regulations (or successor regulations).\n**(iii)**\nPlastics molding and forming, as identified in part 463 of title 40, Code of Federal Regulations (or successor regulations).\n##### (c) Monitoring\n**(1) Monitoring requirements**\n**(A) In general**\nEffective beginning on the date of enactment of this Act, the Administrator shall require monitoring of the discharges (including discharges into a publicly owned treatment works) of each measurable perfluoroalkyl substance, polyfluoroalkyl substance, and class of those substances for the point source categories and entities described in subparagraphs (A), (B), and (C) of subsection (b)(2).\n**(B) Certain monitoring required**\nEffective beginning on the date of enactment of this Act, the Administrator shall require monitoring of the discharges (including discharges into a publicly owned treatment works) of each measurable perfluoroalkyl substance, polyfluoroalkyl substance, and class of those substances for the following point source categories and entities:\n**(i)**\nPulp, paper, and paperboard, as identified in part 430 of title 40, Code of Federal Regulations (or successor regulations).\n**(ii)**\nAirports (as defined in section 47102 of title 49, United States Code).\n**(iii)**\nElectrical and electronic components, as identified in part 469 of title 40, Code of Federal Regulations (or successor regulations).\n**(2) Determination**\n**(A) In general**\nNot later than December 31, 2026, the Administrator shall make a determination\u2014\n**(i)**\nto commence developing effluent limitations guidelines and standards for the point source categories and entities listed in paragraph (1)(B); or\n**(ii)**\nto not commence developing effluent limitations guidelines and standards for those point source categories and entities, including an explanation of the reasoning for this determination.\n**(B) Requirement**\nAny effluent limitations guidelines and standards for the point source categories and entities listed in paragraph (1)(B) shall be published in the Federal Register by not later than December 31, 2028.\n##### (d) Method promulgation\nSubject to the requirements of subchapter II of chapter 5 of title 5, United States Code (commonly referred to as the Administrative Procedure Act ), not later than January 31, 2026, the Administrator shall promulgate Method 1633A, as described in the document of the Environmental Protection Agency entitled Method 1633, Revision A Analysis of Per- and Polyfluoroalkyl Substances (PFAS) in Aqueous, Solid, Biosolids, and Tissue Samples by LC\u2013MS/MS and dated December 2024 (or a successor method of equal or greater validity and standard), under part 136 of title 40, Code of Federal Regulations (or successor regulations).\n##### (e) Notification\nThe Administrator shall notify the Committee on Transportation and Infrastructure of the House of Representatives and the Committee on Environment and Public Works of the Senate of each publication made under this section.\n##### (f) Pretreatment program\n**(1) In general**\nSubject to the availability of appropriations, the Administrator shall award grants to owners and operators of publicly owned treatment works\u2014\n**(A)**\nto carry out pretreatment program activities conducted in accordance with part 403 of title 40, Code of Federal Regulations (or successor regulations), that address contamination by perfluoroalkyl substances and polyfluoroalkyl substances; and\n**(B)**\nto further monitor, assess, or analyze local sources of perfluoroalkyl substances and polyfluoroalkyl substances that enter into the treatment works.\n**(2) Authorization of appropriations**\nThere is authorized to be appropriated to the Administrator to carry out this subsection $200,000,000 for each of fiscal years 2026 through 2030, to remain available until expended.\n##### (g) Authorization of appropriations\nThere is authorized to be appropriated to the Administrator to carry out this section (except subsection (f)) $12,000,000 for each of fiscal years 2026 to 2030, to remain available until expended.",
      "versionDate": "2025-12-11",
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
        "actionDate": "2025-12-11",
        "text": "Read twice and referred to the Committee on Environment and Public Works."
      },
      "number": "3457",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Clean Water Standards for PFAS Act of 2025",
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
        "name": "Environmental Protection",
        "updateDate": "2026-01-08T15:14:27Z"
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
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6668ih.xml"
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
      "title": "Clean Water Standards for PFAS Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-01-04T06:23:16Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Clean Water Standards for PFAS Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-01-04T06:23:16Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To establish effluent limitations guidelines and standards and water quality criteria for perfluoroalkyl and polyfluoroalkyl substances under the Federal Water Pollution Control Act, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-01-04T06:18:21Z"
    }
  ]
}
```
