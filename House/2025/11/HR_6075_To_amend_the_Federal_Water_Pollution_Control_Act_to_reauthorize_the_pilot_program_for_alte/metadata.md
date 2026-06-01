# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/6075?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/6075
- Title: Water Infrastructure Modernization Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 6075
- Origin chamber: House
- Introduced date: 2025-11-18
- Update date: 2026-02-14T09:06:08Z
- Update date including text: 2026-02-14T09:06:08Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-11-18: Introduced in House
- 2025-11-18 - IntroReferral: Introduced in House
- 2025-11-18 - IntroReferral: Introduced in House
- 2025-11-18 - IntroReferral: Referred to the House Committee on Transportation and Infrastructure.
- 2025-11-19 - Committee: Referred to the Subcommittee on Water Resources and Environment.
- Latest action: 2025-11-18: Introduced in House

## Actions

- 2025-11-18 - IntroReferral: Introduced in House
- 2025-11-18 - IntroReferral: Introduced in House
- 2025-11-18 - IntroReferral: Referred to the House Committee on Transportation and Infrastructure.
- 2025-11-19 - Committee: Referred to the Subcommittee on Water Resources and Environment.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-11-18",
    "latestAction": {
      "actionDate": "2025-11-18",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/6075",
    "number": "6075",
    "originChamber": "House",
    "policyArea": {
      "name": "Water Resources Development"
    },
    "sponsors": [
      {
        "bioguideId": "B001327",
        "district": "8",
        "firstName": "Robert",
        "fullName": "Rep. Bresnahan, Robert P. [R-PA-8]",
        "lastName": "Bresnahan",
        "party": "R",
        "state": "PA"
      }
    ],
    "title": "Water Infrastructure Modernization Act of 2025",
    "type": "HR",
    "updateDate": "2026-02-14T09:06:08Z",
    "updateDateIncludingText": "2026-02-14T09:06:08Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-11-19",
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
      "actionDate": "2025-11-18",
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
      "actionDate": "2025-11-18",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-11-18",
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
          "date": "2025-11-18T15:03:15Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Transportation and Infrastructure Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": {
              "date": "2025-11-19T18:20:12Z",
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
      "bioguideId": "M001237",
      "district": "8",
      "firstName": "Kristen",
      "fullName": "Rep. McDonald Rivet, Kristen [D-MI-8]",
      "isOriginalCosponsor": "True",
      "lastName": "McDonald Rivet",
      "party": "D",
      "sponsorshipDate": "2025-11-18",
      "state": "MI"
    },
    {
      "bioguideId": "F000110",
      "district": "6",
      "firstName": "Cleo",
      "fullName": "Rep. Fields, Cleo [D-LA-6]",
      "isOriginalCosponsor": "False",
      "lastName": "Fields",
      "party": "D",
      "sponsorshipDate": "2025-11-19",
      "state": "LA"
    },
    {
      "bioguideId": "M001232",
      "district": "6",
      "firstName": "April",
      "fullName": "Rep. McClain Delaney, April [D-MD-6]",
      "isOriginalCosponsor": "False",
      "lastName": "McClain Delaney",
      "party": "D",
      "sponsorshipDate": "2025-11-19",
      "state": "MD"
    },
    {
      "bioguideId": "P000621",
      "district": "9",
      "firstName": "Nellie",
      "fullName": "Rep. Pou, Nellie [D-NJ-9]",
      "isOriginalCosponsor": "False",
      "lastName": "Pou",
      "party": "D",
      "sponsorshipDate": "2025-11-20",
      "state": "NJ"
    },
    {
      "bioguideId": "G000583",
      "district": "5",
      "firstName": "Josh",
      "fullName": "Rep. Gottheimer, Josh [D-NJ-5]",
      "isOriginalCosponsor": "False",
      "lastName": "Gottheimer",
      "party": "D",
      "sponsorshipDate": "2025-12-02",
      "state": "NJ"
    },
    {
      "bioguideId": "K000404",
      "district": "0",
      "firstName": "Kimberlyn",
      "fullName": "Del. King-Hinds, Kimberlyn [R-MP-At Large]",
      "isOriginalCosponsor": "False",
      "lastName": "King-Hinds",
      "party": "R",
      "sponsorshipDate": "2025-12-03",
      "state": "MP"
    },
    {
      "bioguideId": "H001090",
      "district": "9",
      "firstName": "Josh",
      "fullName": "Rep. Harder, Josh [D-CA-9]",
      "isOriginalCosponsor": "False",
      "lastName": "Harder",
      "party": "D",
      "sponsorshipDate": "2025-12-03",
      "state": "CA"
    },
    {
      "bioguideId": "Q000023",
      "district": "5",
      "firstName": "Mike",
      "fullName": "Rep. Quigley, Mike [D-IL-5]",
      "isOriginalCosponsor": "False",
      "lastName": "Quigley",
      "party": "D",
      "sponsorshipDate": "2025-12-03",
      "state": "IL"
    },
    {
      "bioguideId": "S001211",
      "district": "4",
      "firstName": "Greg",
      "fullName": "Rep. Stanton, Greg [D-AZ-4]",
      "isOriginalCosponsor": "False",
      "lastName": "Stanton",
      "party": "D",
      "sponsorshipDate": "2025-12-05",
      "state": "AZ"
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
      "sponsorshipDate": "2025-12-09",
      "state": "VA"
    },
    {
      "bioguideId": "M001241",
      "district": "47",
      "firstName": "Dave",
      "fullName": "Rep. Min, Dave [D-CA-47]",
      "isOriginalCosponsor": "False",
      "lastName": "Min",
      "party": "D",
      "sponsorshipDate": "2025-12-17",
      "state": "CA"
    },
    {
      "bioguideId": "N000191",
      "district": "2",
      "firstName": "Joe",
      "fullName": "Rep. Neguse, Joe [D-CO-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Neguse",
      "party": "D",
      "sponsorshipDate": "2025-12-17",
      "state": "CO"
    },
    {
      "bioguideId": "S001225",
      "district": "17",
      "firstName": "Eric",
      "fullName": "Rep. Sorensen, Eric [D-IL-17]",
      "isOriginalCosponsor": "False",
      "lastName": "Sorensen",
      "party": "D",
      "sponsorshipDate": "2025-12-17",
      "state": "IL"
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
      "sponsorshipDate": "2025-12-30",
      "state": "CA"
    },
    {
      "bioguideId": "L000593",
      "district": "49",
      "firstName": "Mike",
      "fullName": "Rep. Levin, Mike [D-CA-49]",
      "isOriginalCosponsor": "False",
      "lastName": "Levin",
      "party": "D",
      "sponsorshipDate": "2025-12-30",
      "state": "CA"
    },
    {
      "bioguideId": "D000629",
      "district": "3",
      "firstName": "Sharice",
      "fullName": "Rep. Davids, Sharice [D-KS-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Davids",
      "party": "D",
      "sponsorshipDate": "2026-01-06",
      "state": "KS"
    },
    {
      "bioguideId": "L000397",
      "district": "18",
      "firstName": "Zoe",
      "fullName": "Rep. Lofgren, Zoe [D-CA-18]",
      "isOriginalCosponsor": "False",
      "lastName": "Lofgren",
      "party": "D",
      "sponsorshipDate": "2026-01-06",
      "state": "CA"
    },
    {
      "bioguideId": "G000602",
      "district": "4",
      "firstName": "Laura",
      "fullName": "Rep. Gillen, Laura [D-NY-4]",
      "isOriginalCosponsor": "False",
      "lastName": "Gillen",
      "party": "D",
      "sponsorshipDate": "2026-01-27",
      "state": "NY"
    },
    {
      "bioguideId": "L000590",
      "district": "3",
      "firstName": "Susie",
      "fullName": "Rep. Lee, Susie [D-NV-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Lee",
      "party": "D",
      "sponsorshipDate": "2026-02-13",
      "state": "NV"
    },
    {
      "bioguideId": "C001055",
      "district": "1",
      "firstName": "Ed",
      "fullName": "Rep. Case, Ed [D-HI-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Case",
      "party": "D",
      "sponsorshipDate": "2026-02-13",
      "state": "HI"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6075ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 6075\nIN THE HOUSE OF REPRESENTATIVES\nNovember 18, 2025 Mr. Bresnahan (for himself and Ms. McDonald Rivet ) introduced the following bill; which was referred to the Committee on Transportation and Infrastructure\nA BILL\nTo amend the Federal Water Pollution Control Act to reauthorize the pilot program for alternative water source projects, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Water Infrastructure Modernization Act of 2025 .\n#### 2. Intelligent water infrastructure technology\nSection 220 of the Federal Water Pollution Control Act ( 33 U.S.C. 1300 ) is amended\u2014\n**(1)**\nin subsection (b), by adding at the end the following:\n(3) Intelligent water infrastructure technology The term intelligent water infrastructure technology means\u2014 (A) intelligent wastewater treatment and collection systems and stormwater management operations, including technologies that rely on\u2014 (i) the use of real-time monitoring, management, analytics, and data collection tools, embedded intelligence, and predictive maintenance capabilities that improve the energy efficiency, cost efficiency, reliability, and resiliency of wastewater treatment and collection systems; (ii) real-time remote sensors that provide continuous monitoring of water quality to support optimization; and (iii) the use of artificial intelligence and other intelligent optimization tools that\u2014 (I) reduce operational costs, including operational costs relating to energy consumption and chemical treatment; and (II) improve decisionmaking; (B) innovative and alternative combined sewer and stormwater control projects, including groundwater banking, that rely on real-time data acquisition to support predictive aquifer recharge through water reuse and stormwater management capabilities; (C) advanced digital design and construction management tools, including advanced digital technologies; (D) technology that can identify or reduce water losses in a nondestructive or nondisruptive manner, including through analytical software, flow and pressure monitoring, or acoustic data collection; (E) predictive and diagnostic tools for informed decisionmaking; (F) technology that can provide comprehensive data on pipe integrity to identify the presence of leaks or gas pockets; (G) technology that can provide information on the extent of leaks or gas pockets, with an emphasis on detecting weakness of, vulnerability of, or damage to pipe barrels, pipe joints, or other pipe features; (H) real-time remote sensing technologies, including the use of advanced data management and analytics, that detect and alert owners and operators to wastewater and water supply treatment facilities operations, including leakages, and pipe bursts on a real-time basis, including persistent sensor networks capable of measuring\u2014 (i) acoustic signals; (ii) pressure transient; (iii) water quality; or (iv) water flow; (I) advanced metering infrastructure, including meter data analytics and ratepayer technology\u2014 (i) to improve end-user conservation; and (ii) in support of disadvantaged communities; (J) resilient water supply projects that may provide real-time monitoring of weather patterns and weather-related impacts on water quality and flood protection reservoirs and dams that enhance operations, including\u2014 (i) improved water supply reliability and management; (ii) protection of natural resources, including fisheries; and (iii) temperature control; (K) innovative and alternative water supply projects, including groundwater banking, that rely on real-time data acquisition to support predictive aquifer recharge through water reuse and stormwater management capabilities; (L) artificial intelligence and other intelligent optimization tools that\u2014 (i) reduce operational costs, including costs relating to energy consumption and chemical treatment of wastewater and stormwater; and (ii) improve decisionmaking; and (M) advanced digital design and construction management technologies and tools relating to water treatment systems and distribution networks the development of advanced digital models. ;\n**(2)**\nby striking subsection (f) and inserting the following:\n(f) Uses of grants (1) In general Amounts from grants received under this section may be used for engineering, design, construction, and final testing of alternative water source projects designed to meet critical water supply needs. (2) Prohibition Amounts from grants received under this section may not be used for planning, feasibility studies, operation, or maintenance. (3) Intelligent water infrastructure technologies (A) In general Amounts from grants received under this section may be used for engineering, design, construction, implementation, training, and operations relating to the adoption and use of intelligent water infrastructure technology. (B) Applicability For purposes of paragraph (2), any costs with respect to intelligent water infrastructure technology shall not be considered operation or maintenance costs. ;\n**(3)**\nby striking subsection (h) and inserting the following:\n(h) Reports (1) In general Not later than 180 days after the date of enactment of the Water Infrastructure Modernization Act of 2025 , and not less frequently than annually thereafter, the Administrator shall submit to Congress a report that\u2014 (A) describes\u2014 (i) the projects awarded grants for the purposes described in subsection (f)(3); and (ii) the improvements in the resiliency that resulted from grants awarded under this section; and (B) includes any recommendations of the Administrator to improve the ability of grants under this section to achieve the uses described in subsection (f). (2) Initial report In the initial report required under paragraph (1), the Administrator shall include a description of the implementation of this section, including a description of\u2014 (A) the projects for which a grant was sought under this section for the purposes described in subsection (f)(3) that were denied; and (B) for each of the projects described in subparagraph (A), the reasons for which the grant was denied. ; and\n**(4)**\nin subsection (i)(1)\u2014\n**(A)**\nby striking $25,000,000 and inserting $50,000,000 ; and\n**(B)**\nby striking 2026 and inserting 2028 .",
      "versionDate": "2025-11-18",
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
        "actionDate": "2025-07-23",
        "text": "Read twice and referred to the Committee on Environment and Public Works."
      },
      "number": "2388",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Water Infrastructure Modernization Act of 2025",
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
        "name": "Water Resources Development",
        "updateDate": "2025-12-02T21:34:46Z"
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
      "date": "2025-11-18",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6075ih.xml"
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
      "title": "Water Infrastructure Modernization Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-11-29T05:38:19Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Water Infrastructure Modernization Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-11-29T05:38:18Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Federal Water Pollution Control Act to reauthorize the pilot program for alternative water source projects, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-11-29T05:33:36Z"
    }
  ]
}
```
