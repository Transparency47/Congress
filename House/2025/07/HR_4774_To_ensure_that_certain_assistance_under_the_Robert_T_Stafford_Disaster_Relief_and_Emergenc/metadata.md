# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/4774?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/4774
- Title: Fix Our Flooded Basements Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 4774
- Origin chamber: House
- Introduced date: 2025-07-25
- Update date: 2026-03-03T15:51:45Z
- Update date including text: 2026-03-03T15:51:45Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-07-25: Introduced in House
- 2025-07-23 - IntroReferral: Introduced in House
- 2025-07-23 - IntroReferral: Introduced in House
- 2025-07-23 - IntroReferral: Sponsor introductory remarks on measure. (CR H3625)
- 2025-07-25 - IntroReferral: Referred to the Committee on Transportation and Infrastructure, and in addition to the Committee on Financial Services, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-07-25 - IntroReferral: Referred to the Committee on Transportation and Infrastructure, and in addition to the Committee on Financial Services, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-07-26 - Committee: Referred to the Subcommittee on Economic Development, Public Buildings, and Emergency Management.
- Latest action: 2025-07-23: Introduced in House

## Actions

- 2025-07-23 - IntroReferral: Introduced in House
- 2025-07-23 - IntroReferral: Introduced in House
- 2025-07-23 - IntroReferral: Sponsor introductory remarks on measure. (CR H3625)
- 2025-07-25 - IntroReferral: Referred to the Committee on Transportation and Infrastructure, and in addition to the Committee on Financial Services, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-07-25 - IntroReferral: Referred to the Committee on Transportation and Infrastructure, and in addition to the Committee on Financial Services, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-07-26 - Committee: Referred to the Subcommittee on Economic Development, Public Buildings, and Emergency Management.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-07-25",
    "latestAction": {
      "actionDate": "2025-07-23",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/4774",
    "number": "4774",
    "originChamber": "House",
    "policyArea": {
      "name": "Emergency Management"
    },
    "sponsors": [
      {
        "bioguideId": "T000481",
        "district": "12",
        "firstName": "Rashida",
        "fullName": "Rep. Tlaib, Rashida [D-MI-12]",
        "lastName": "Tlaib",
        "party": "D",
        "state": "MI"
      }
    ],
    "title": "Fix Our Flooded Basements Act of 2025",
    "type": "HR",
    "updateDate": "2026-03-03T15:51:45Z",
    "updateDateIncludingText": "2026-03-03T15:51:45Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-07-26",
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
      "actionDate": "2025-07-25",
      "committees": {
        "item": {
          "name": "Financial Services Committee",
          "systemCode": "hsba00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the Committee on Transportation and Infrastructure, and in addition to the Committee on Financial Services, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-07-25",
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
      "text": "Referred to the Committee on Transportation and Infrastructure, and in addition to the Committee on Financial Services, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-07-23",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "B00100",
      "actionDate": "2025-07-23",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Sponsor introductory remarks on measure. (CR H3625)",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-07-23",
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
          "date": "2025-07-25T15:01:35Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Transportation and Infrastructure Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": {
              "date": "2025-07-26T21:31:38Z",
              "name": "Referred to"
            }
          },
          "name": "Economic Development, Public Buildings, and Emergency Management Subcommittee",
          "systemCode": "hspw13"
        }
      },
      "systemCode": "hspw00",
      "type": "Standing"
    },
    {
      "activities": {
        "item": {
          "date": "2025-07-25T15:01:40Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Financial Services Committee",
      "systemCode": "hsba00",
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
      "bioguideId": "B001313",
      "district": "11",
      "firstName": "Shontel",
      "fullName": "Rep. Brown, Shontel M. [D-OH-11]",
      "isOriginalCosponsor": "True",
      "lastName": "Brown",
      "middleName": "M.",
      "party": "D",
      "sponsorshipDate": "2025-07-25",
      "state": "OH"
    },
    {
      "bioguideId": "P000617",
      "district": "7",
      "firstName": "Ayanna",
      "fullName": "Rep. Pressley, Ayanna [D-MA-7]",
      "isOriginalCosponsor": "True",
      "lastName": "Pressley",
      "party": "D",
      "sponsorshipDate": "2025-07-25",
      "state": "MA"
    },
    {
      "bioguideId": "B001318",
      "district": "0",
      "firstName": "Becca",
      "fullName": "Rep. Balint, Becca [D-VT-At Large]",
      "isOriginalCosponsor": "True",
      "lastName": "Balint",
      "party": "D",
      "sponsorshipDate": "2025-07-25",
      "state": "VT"
    },
    {
      "bioguideId": "B001300",
      "district": "44",
      "firstName": "Nanette",
      "fullName": "Rep. Barrag\u00e1n, Nanette Diaz [D-CA-44]",
      "isOriginalCosponsor": "True",
      "lastName": "Barrag\u00e1n",
      "middleName": "Diaz",
      "party": "D",
      "sponsorshipDate": "2025-07-25",
      "state": "CA"
    },
    {
      "bioguideId": "B001281",
      "district": "3",
      "firstName": "Joyce",
      "fullName": "Rep. Beatty, Joyce [D-OH-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Beatty",
      "party": "D",
      "sponsorshipDate": "2025-07-25",
      "state": "OH"
    },
    {
      "bioguideId": "D000530",
      "district": "17",
      "firstName": "Christopher",
      "fullName": "Rep. Deluzio, Christopher R. [D-PA-17]",
      "isOriginalCosponsor": "True",
      "lastName": "Deluzio",
      "middleName": "R.",
      "party": "D",
      "sponsorshipDate": "2025-07-25",
      "state": "PA"
    },
    {
      "bioguideId": "E000296",
      "district": "3",
      "firstName": "Dwight",
      "fullName": "Rep. Evans, Dwight [D-PA-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Evans",
      "party": "D",
      "sponsorshipDate": "2025-07-25",
      "state": "PA"
    },
    {
      "bioguideId": "F000110",
      "district": "6",
      "firstName": "Cleo",
      "fullName": "Rep. Fields, Cleo [D-LA-6]",
      "isOriginalCosponsor": "True",
      "lastName": "Fields",
      "party": "D",
      "sponsorshipDate": "2025-07-25",
      "state": "LA"
    },
    {
      "bioguideId": "F000481",
      "district": "2",
      "firstName": "Shomari",
      "fullName": "Rep. Figures, Shomari [D-AL-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Figures",
      "party": "D",
      "sponsorshipDate": "2025-07-25",
      "state": "AL"
    },
    {
      "bioguideId": "G000586",
      "district": "4",
      "firstName": "Jes\u00fas",
      "fullName": "Rep. Garc\u00eda, Jes\u00fas G. \"Chuy\" [D-IL-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Garc\u00eda",
      "middleName": "G. \"Chuy\"",
      "party": "D",
      "sponsorshipDate": "2025-07-25",
      "state": "IL"
    },
    {
      "bioguideId": "M001229",
      "district": "10",
      "firstName": "LaMonica",
      "fullName": "Rep. McIver, LaMonica [D-NJ-10]",
      "isOriginalCosponsor": "True",
      "lastName": "McIver",
      "party": "D",
      "sponsorshipDate": "2025-07-25",
      "state": "NJ"
    },
    {
      "bioguideId": "M001188",
      "district": "6",
      "firstName": "Grace",
      "fullName": "Rep. Meng, Grace [D-NY-6]",
      "isOriginalCosponsor": "True",
      "lastName": "Meng",
      "party": "D",
      "sponsorshipDate": "2025-07-25",
      "state": "NY"
    },
    {
      "bioguideId": "M000687",
      "district": "7",
      "firstName": "Kweisi",
      "fullName": "Rep. Mfume, Kweisi [D-MD-7]",
      "isOriginalCosponsor": "True",
      "lastName": "Mfume",
      "party": "D",
      "sponsorshipDate": "2025-07-25",
      "state": "MD"
    },
    {
      "bioguideId": "M001217",
      "district": "23",
      "firstName": "Jared",
      "fullName": "Rep. Moskowitz, Jared [D-FL-23]",
      "isOriginalCosponsor": "True",
      "lastName": "Moskowitz",
      "party": "D",
      "sponsorshipDate": "2025-07-25",
      "state": "FL"
    },
    {
      "bioguideId": "N000147",
      "district": "0",
      "firstName": "Eleanor",
      "fullName": "Del. Norton, Eleanor Holmes [D-DC-At Large]",
      "isOriginalCosponsor": "True",
      "lastName": "Norton",
      "middleName": "Holmes",
      "party": "D",
      "sponsorshipDate": "2025-07-25",
      "state": "DC"
    },
    {
      "bioguideId": "S001205",
      "district": "5",
      "firstName": "Mary Gay",
      "fullName": "Rep. Scanlon, Mary Gay [D-PA-5]",
      "isOriginalCosponsor": "True",
      "lastName": "Scanlon",
      "party": "D",
      "sponsorshipDate": "2025-07-25",
      "state": "PA"
    },
    {
      "bioguideId": "S000185",
      "district": "3",
      "firstName": "Robert",
      "fullName": "Rep. Scott, Robert C. \"Bobby\" [D-VA-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Scott",
      "middleName": "C. \"Bobby\"",
      "party": "D",
      "sponsorshipDate": "2025-07-25",
      "state": "VA"
    },
    {
      "bioguideId": "S001185",
      "district": "7",
      "firstName": "Terri",
      "fullName": "Rep. Sewell, Terri A. [D-AL-7]",
      "isOriginalCosponsor": "True",
      "lastName": "Sewell",
      "middleName": "A.",
      "party": "D",
      "sponsorshipDate": "2025-07-25",
      "state": "AL"
    },
    {
      "bioguideId": "T000488",
      "district": "13",
      "firstName": "Shri",
      "fullName": "Rep. Thanedar, Shri [D-MI-13]",
      "isOriginalCosponsor": "True",
      "lastName": "Thanedar",
      "party": "D",
      "sponsorshipDate": "2025-07-25",
      "state": "MI"
    },
    {
      "bioguideId": "H001103",
      "district": "0",
      "firstName": "Pablo",
      "fullName": "Rescom. Hern\u00e1ndez, Pablo Jose [D-PR-At Large]",
      "isOriginalCosponsor": "False",
      "lastName": "Hern\u00e1ndez",
      "middleName": "Jose",
      "party": "D",
      "sponsorshipDate": "2025-07-29",
      "state": "PR"
    },
    {
      "bioguideId": "G000587",
      "district": "29",
      "firstName": "Sylvia",
      "fullName": "Rep. Garcia, Sylvia R. [D-TX-29]",
      "isOriginalCosponsor": "False",
      "lastName": "Garcia",
      "middleName": "R.",
      "party": "D",
      "sponsorshipDate": "2025-07-29",
      "state": "TX"
    },
    {
      "bioguideId": "L000607",
      "district": "16",
      "firstName": "Sam",
      "fullName": "Rep. Liccardo, Sam T. [D-CA-16]",
      "isOriginalCosponsor": "False",
      "lastName": "Liccardo",
      "middleName": "T.",
      "party": "D",
      "sponsorshipDate": "2025-07-29",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr4774ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 4774\nIN THE HOUSE OF REPRESENTATIVES\nJuly 25, 2025 Ms. Tlaib (for herself, Ms. Brown , Ms. Pressley , Ms. Balint , Ms. Barrag\u00e1n , Mrs. Beatty , Mr. Deluzio , Mr. Evans of Pennsylvania , Mr. Fields , Mr. Figures , Mr. Garc\u00eda of Illinois , Mrs. McIver , Ms. Meng , Mr. Mfume , Mr. Moskowitz , Ms. Norton , Ms. Scanlon , Mr. Scott of Virginia , Ms. Sewell , and Mr. Thanedar ) introduced the following bill; which was referred to the Committee on Transportation and Infrastructure , and in addition to the Committee on Financial Services , for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned\nA BILL\nTo ensure that certain assistance under the Robert T. Stafford Disaster Relief and Emergency Assistance Act is available for flood-damaged basements, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Fix Our Flooded Basements Act of 2025 .\n#### 2. Assistance for flood-damaged basements\n##### (a) Repairs\nIn providing assistance for repairs to flood-damaged basements under section 408(c)(2) of the Robert T. Stafford Disaster Relief and Emergency Assistance Act ( 42 U.S.C. 5174(c)(2) ), the Administrator\u2014\n**(1)**\nmay not limit such assistance to rooms required for the occupancy of the dwelling; and\n**(2)**\nmay provide assistance for any mold, mildew, and moisture damage caused by a major disaster and may not limit such assistance to only mold, mildew, or moisture damage that\u2014\n**(A)**\nmay cause additional loss; or\n**(B)**\naffects the safety, sanitation, and functionality of the home.\n##### (b) Personal property assistance\nIn providing assistance for personal property expenses under section 408(e)(2) of the Robert T. Stafford Disaster Relief and Emergency Assistance Act ( 42 U.S.C. 5174(e)(2) ), the Administrator shall provide assistance\u2014\n**(1)**\nto cover the cost of personal property in a manner that is at least equivalent to the coverage provided under the Standard Flood Insurance Policy for building property and personal property located below the lowest floor of a building, including basements (as defined in section 59.1 of title 44, Code of Federal Regulations, or any successor regulations); and\n**(2)**\nto cover the costs of repair or replacement of all building and personal property located in a flood-damaged basement that is damaged by a major disaster.\n##### (c) Group Flood Insurance Policy\nNot later than 6 months after the date of enactment of this Act, the Administrator shall revise sections 61.17 and 206.119(b)(9) of title 44, Code of Federal Regulations, to make the following changes:\n**(1)**\nPermit applicants who had a previous requirement to maintain flood insurance as a condition of receiving assistance under section 408 of the Robert T. Stafford Disaster Relief and Emergency Assistance Act ( 42 U.S.C. 5174 ) to be eligible for the Group Flood Insurance Policy.\n**(2)**\nPermit applicants residing outside a special flood hazard area to be eligible for the Group Flood Insurance Policy.\n**(3)**\nExpand the coverage under the Group Flood Insurance Policy to be at least equivalent to the maximum coverage available in the Standard Flood Insurance Policy.\n**(4)**\nExpand the Group Flood Insurance Policy to include coverage for the following:\n**(A)**\nReal and personal property components and contents in basements, including repairs to address water damage, appliances, flooring and carpet repairs, and any other items necessary to return the basement to its previous pre-flood condition.\n**(B)**\nAny real and personal property components and contents in basements covered under the additional endorsement for basement coverage for the Standard Flood Insurance Policy, as described in the proposed rule titled National Flood Insurance Program: Standard Flood Insurance Policy, Homeowner Flood Form and issued by the Administrator on February 6, 2024 (89 Fed. Reg. 8282).\n**(C)**\nMold, mildew, and moisture damage in basements.\n##### (d) Maximum amount of financial assistance\nSection 408(h) of the Robert T. Stafford Disaster Relief and Emergency Assistance Act ( 42 U.S.C. 5174(h) ) is amended by adding at the end the following:\n(5) Exclusion of mitigation measures The maximum amount of assistance established under paragraph (1) shall exclude expenses for eligible hazard mitigation measures in flood-damaged basements under subsection (c)(2)(A)(ii). (6) Exclusion of Group Flood Insurance Policy premiums The maximum amount of assistance established under paragraph (1) shall exclude expenses for premiums for the Group Flood Insurance Policy pursuant to subsection (e)(2). .\n##### (e) Definitions\nIn this section:\n**(1) Administrator**\nThe term Administrator means the Administrator of the Federal Emergency Management Agency.\n**(2) Group Flood Insurance Policy**\nThe term Group Flood Insurance Policy means the group flood insurance policy established by the Administrator under section 61.17 of title 44, Code of Federal Regulations.\n**(3) Standard Flood Insurance Policy**\nThe term Standard Flood Insurance Policy means the standard flood insurance policy under the national flood insurance program established pursuant to the National Flood Insurance Act of 1968 ( 42 U.S.C. 4001 et seq. ).",
      "versionDate": "2025-07-25",
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
        "updateDate": "2025-09-16T22:33:18Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-07-25",
    "originChamber": "House",
    "payload": {
      "dublinCore": {
        "contributor": "Congressional Research Service, Library of Congress",
        "description": "This file contains bill summaries for federal legislation. A bill summary describes the most significant provisions of a piece of legislation and details the effects the legislative text may have on current law and federal programs. Bill summaries are authored by the Congressional Research Service (CRS) of the Library of Congress. As stated in Public Law 91-510 (2 USC 166 (d)(6)), one of the duties of CRS is \"to prepare summaries and digests of bills and resolutions of a public general nature introduced in the Senate or House of Representatives\". For more information, refer to the User Guide that accompanies this file.",
        "format": "text/xml",
        "language": "EN",
        "rights": "Pursuant to Title 17 Section 105 of the United States Code, this file is not subject to copyright protection and is in the public domain."
      },
      "item": {
        "@attributes": {
          "congress": "119",
          "measure-id": "id119hr4774",
          "measure-number": "4774",
          "measure-type": "hr",
          "orig-publish-date": "2025-07-25",
          "originChamber": "HOUSE",
          "update-date": "2026-03-03"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr4774v00",
            "update-date": "2026-03-03"
          },
          "action-date": "2025-07-25",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Fix Our Flooded Basements Act of 2025</strong></p><p>This bill expands the disaster assistance provided to individuals and households for repairs to and property in flood-damaged basements. It also expands eligibility and coverage for certain group flood insurance.</p><p>Under current law, the Individual Assistance (IA) program of the Federal Emergency Management Agency (FEMA) limits home repair assistance for flood-damaged basements to damage affecting the safety, sanitation, or functionality of the home (e.g., structural damage, hazardous conditions). The bill allows home repair assistance for disaster-caused mold, mildew, and moisture damage in basements regardless of whether the damage affects safety, sanitation, or functionality. Additionally, flood-damaged basements are eligible for home repair assistance even when the basement is not required for occupying the dwelling.</p><p>Also, currently, IA assistance for flood-damaged personal property in basements is limited to washers, dryers, and property essential for occupying the dwelling. The bill expands IA personal property assistance to more broadly cover property damaged by disaster-caused flooding in basements. The scope of such assistance must at least equal the coverage for such damage by a standard policy under the National Flood Insurance Program (e.g., covering air conditioning units and freezers in basements).\u00a0</p><p>Additionally, FEMA must expand the eligibility and coverage of the group flood insurance it provides to IA recipients, including increasing the maximum coverage and expanding coverage for basements.</p><p>The bill also excludes from the maximum for IA housing assistance expenses for (1) hazard mitigation measures in flood-damaged basements, and (2) premiums for group flood insurance policies.</p>"
        },
        "title": "Fix Our Flooded Basements Act of 2025"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr4774.xml",
    "summary": {
      "actionDate": "2025-07-25",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Fix Our Flooded Basements Act of 2025</strong></p><p>This bill expands the disaster assistance provided to individuals and households for repairs to and property in flood-damaged basements. It also expands eligibility and coverage for certain group flood insurance.</p><p>Under current law, the Individual Assistance (IA) program of the Federal Emergency Management Agency (FEMA) limits home repair assistance for flood-damaged basements to damage affecting the safety, sanitation, or functionality of the home (e.g., structural damage, hazardous conditions). The bill allows home repair assistance for disaster-caused mold, mildew, and moisture damage in basements regardless of whether the damage affects safety, sanitation, or functionality. Additionally, flood-damaged basements are eligible for home repair assistance even when the basement is not required for occupying the dwelling.</p><p>Also, currently, IA assistance for flood-damaged personal property in basements is limited to washers, dryers, and property essential for occupying the dwelling. The bill expands IA personal property assistance to more broadly cover property damaged by disaster-caused flooding in basements. The scope of such assistance must at least equal the coverage for such damage by a standard policy under the National Flood Insurance Program (e.g., covering air conditioning units and freezers in basements).\u00a0</p><p>Additionally, FEMA must expand the eligibility and coverage of the group flood insurance it provides to IA recipients, including increasing the maximum coverage and expanding coverage for basements.</p><p>The bill also excludes from the maximum for IA housing assistance expenses for (1) hazard mitigation measures in flood-damaged basements, and (2) premiums for group flood insurance policies.</p>",
      "updateDate": "2026-03-03",
      "versionCode": "id119hr4774"
    },
    "title": "Fix Our Flooded Basements Act of 2025"
  },
  "summaries": [
    {
      "actionDate": "2025-07-25",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Fix Our Flooded Basements Act of 2025</strong></p><p>This bill expands the disaster assistance provided to individuals and households for repairs to and property in flood-damaged basements. It also expands eligibility and coverage for certain group flood insurance.</p><p>Under current law, the Individual Assistance (IA) program of the Federal Emergency Management Agency (FEMA) limits home repair assistance for flood-damaged basements to damage affecting the safety, sanitation, or functionality of the home (e.g., structural damage, hazardous conditions). The bill allows home repair assistance for disaster-caused mold, mildew, and moisture damage in basements regardless of whether the damage affects safety, sanitation, or functionality. Additionally, flood-damaged basements are eligible for home repair assistance even when the basement is not required for occupying the dwelling.</p><p>Also, currently, IA assistance for flood-damaged personal property in basements is limited to washers, dryers, and property essential for occupying the dwelling. The bill expands IA personal property assistance to more broadly cover property damaged by disaster-caused flooding in basements. The scope of such assistance must at least equal the coverage for such damage by a standard policy under the National Flood Insurance Program (e.g., covering air conditioning units and freezers in basements).\u00a0</p><p>Additionally, FEMA must expand the eligibility and coverage of the group flood insurance it provides to IA recipients, including increasing the maximum coverage and expanding coverage for basements.</p><p>The bill also excludes from the maximum for IA housing assistance expenses for (1) hazard mitigation measures in flood-damaged basements, and (2) premiums for group flood insurance policies.</p>",
      "updateDate": "2026-03-03",
      "versionCode": "id119hr4774"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-07-25",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr4774ih.xml"
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
      "title": "Fix Our Flooded Basements Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-08-06T05:23:21Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Fix Our Flooded Basements Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-08-06T05:23:19Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To ensure that certain assistance under the Robert T. Stafford Disaster Relief and Emergency Assistance Act is available for flood-damaged basements, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-08-06T05:18:47Z"
    }
  ]
}
```
