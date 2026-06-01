# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/6716?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/6716
- Title: SATOS Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 6716
- Origin chamber: House
- Introduced date: 2025-12-15
- Update date: 2026-05-16T08:07:41Z
- Update date including text: 2026-05-16T08:07:41Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-12-15: Introduced in House
- 2025-12-15 - IntroReferral: Introduced in House
- 2025-12-15 - IntroReferral: Introduced in House
- 2025-12-15 - IntroReferral: Referred to the House Committee on Agriculture.
- 2026-01-13 - Committee: Referred to the Subcommittee on Commodity Markets, Digital Assets, and Rural Development.
- 2026-01-13 - Committee: Referred to the Subcommittee on Livestock, Dairy, and Poultry.
- Latest action: 2025-12-15: Introduced in House

## Actions

- 2025-12-15 - IntroReferral: Introduced in House
- 2025-12-15 - IntroReferral: Introduced in House
- 2025-12-15 - IntroReferral: Referred to the House Committee on Agriculture.
- 2026-01-13 - Committee: Referred to the Subcommittee on Commodity Markets, Digital Assets, and Rural Development.
- 2026-01-13 - Committee: Referred to the Subcommittee on Livestock, Dairy, and Poultry.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-12-15",
    "latestAction": {
      "actionDate": "2025-12-15",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/6716",
    "number": "6716",
    "originChamber": "House",
    "policyArea": {
      "name": "Animals"
    },
    "sponsors": [
      {
        "bioguideId": "H001103",
        "district": "",
        "firstName": "Pablo",
        "fullName": "Rescom. Hern\u00e1ndez, Pablo Jose [D-PR-At Large]",
        "lastName": "Hern\u00e1ndez",
        "party": "D",
        "state": "PR"
      }
    ],
    "title": "SATOS Act of 2025",
    "type": "HR",
    "updateDate": "2026-05-16T08:07:41Z",
    "updateDateIncludingText": "2026-05-16T08:07:41Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-01-13",
      "committees": {
        "item": {
          "name": "Livestock, Dairy, and Poultry Subcommittee",
          "systemCode": "hsag29"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Referred to the Subcommittee on Livestock, Dairy, and Poultry.",
      "type": "Committee"
    },
    {
      "actionDate": "2026-01-13",
      "committees": {
        "item": {
          "name": "Commodity Markets, Digital Assets, and Rural Development Subcommittee",
          "systemCode": "hsag22"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Referred to the Subcommittee on Commodity Markets, Digital Assets, and Rural Development.",
      "type": "Committee"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-12-15",
      "committees": {
        "item": {
          "name": "Agriculture Committee",
          "systemCode": "hsag00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Agriculture.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-12-15",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-12-15",
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
          "date": "2025-12-15T17:01:00Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Agriculture Committee",
      "subcommittees": {
        "item": [
          {
            "activities": {
              "item": {
                "date": "2026-01-13T20:07:18Z",
                "name": "Referred to"
              }
            },
            "name": "Commodity Markets, Digital Assets, and Rural Development Subcommittee",
            "systemCode": "hsag22"
          },
          {
            "activities": {
              "item": {
                "date": "2026-01-13T20:07:18Z",
                "name": "Referred to"
              }
            },
            "name": "Livestock, Dairy, and Poultry Subcommittee",
            "systemCode": "hsag29"
          }
        ]
      },
      "systemCode": "hsag00",
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
      "bioguideId": "N000147",
      "district": "0",
      "firstName": "Eleanor",
      "fullName": "Del. Norton, Eleanor Holmes [D-DC-At Large]",
      "isOriginalCosponsor": "True",
      "lastName": "Norton",
      "middleName": "Holmes",
      "party": "D",
      "sponsorshipDate": "2025-12-15",
      "state": "DC"
    },
    {
      "bioguideId": "T000468",
      "district": "1",
      "firstName": "Dina",
      "fullName": "Rep. Titus, Dina [D-NV-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Titus",
      "party": "D",
      "sponsorshipDate": "2025-12-15",
      "state": "NV"
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
      "sponsorshipDate": "2026-04-20",
      "state": "GU"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6716ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 6716\nIN THE HOUSE OF REPRESENTATIVES\nDecember 15, 2025 Mr. Hern\u00e1ndez (for himself, Ms. Norton , and Ms. Titus ) introduced the following bill; which was referred to the Committee on Agriculture\nA BILL\nTo establish a program to provide grants and loans to facilitate the care, rehabilitation, and welfare of domestic animals in rural areas, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Save Animals Through Operational Shelters Act of 2025 or the SATOS Act of 2025 .\n#### 2. Findings\nCongress finds the following:\n**(1)**\nRural communities often lack adequate infrastructure (including animal shelters and veterinary care facilities) to support animal welfare.\n**(2)**\nAssociations, units of general local government, nonprofit corporations, and Indian Tribes play a critical role in promoting the health, safety, and humane treatment of animals.\n**(3)**\nInvestment in animal care facilities contributes to public health, safety, and community well-being.\n#### 3. Grants and loans for domestic animal care facilities in rural areas\n##### (a) Establishment\nThe Secretary shall establish a program to provide a grant or loan to an eligible entity\u2014\n**(1)**\nto construct, expand, or renovate a facility in a rural area for\u2014\n**(A)**\nan animal shelter;\n**(B)**\nan animal adoption center;\n**(C)**\na veterinary care clinic;\n**(D)**\na spay and neuter clinic;\n**(E)**\nan animal control operation; or\n**(F)**\nan emergency animal shelter; or\n**(2)**\nto purchase or install equipment, furnishings, vehicles, or technology for such a facility.\n##### (b) Terms of grant\n**(1) Amount**\nThe total amount that may be provided as grants under subsection (a) for a fiscal year may not exceed $10,000,000.\n**(2) Federal share**\n**(A) In general**\nExcept as provided in subparagraphs (B) and (C), the Secretary shall, by rule, establish the amount of the Federal share of the cost of developing a facility pursuant to a grant under subsection (a).\n**(B) Maximum amount**\nThe amount of a grant provided under subsection (a) for a facility may not exceed 75 percent of the cost of developing such facility.\n**(C) Graduated scale**\nThe Secretary shall establish a graduated scale for the amount of the Federal share provided under this paragraph, with a greater Federal share, not more than the maximum amount described in subparagraph (B), for a facility located in a community that has a lesser population or income level, as determined by the Secretary.\n##### (c) Technical assistance and training\n**(1) In general**\nThe Secretary may make a grant to an eligible entity to procure technical assistance and training to\u2014\n**(A)**\nassist such eligible entity in identifying and planning for the needs of a facility developed pursuant to a grant or loan under subsection (a);\n**(B)**\nidentify resources to finance the needs of such a facility;\n**(C)**\nprepare a report or survey to be included in an application for a grant or loan under subsection (a);\n**(D)**\nprepare an application for such grant or loan;\n**(E)**\nimprove the administration, including financial administration, of such a facility; and\n**(F)**\nassist with any other area of need, as identified by the Secretary, relating to the administration of\u2014\n**(i)**\nsuch a facility; or\n**(ii)**\na grant or loan under subsection (a).\n**(2) Selection priority**\nIn selecting a recipient of a grant under this subsection, the Secretary shall give priority to an eligible entity that has experience in the planning, design, operation, or management of a facility described in subsection (a)(1), as demonstrated in the application for such grant submitted by such eligible entity.\n**(3) Funding**\nNot less than 3 nor more than 5 percent of any funds appropriated to carry out this section for a fiscal year shall be reserved for grants under this subsection.\n##### (d) Rule making\nWithin 180 days after the date of enactment of this Act, the Secretary shall finalize a rule to carry out this section.\n##### (e) Implementation\nWithin 1 year after the date of enactment of this Act, the Secretary shall begin providing grants and loans under subsection (a).\n##### (f) Reports\nWithin 2 years after the date of enactment of this Act, and not less frequently than every 2 years thereafter, the Secretary shall submit to the Committee on Agriculture of the House of Representatives and the Committee on Agriculture, Nutrition, and Forestry of the Senate a report describing\u2014\n**(1)**\nthe amount of grants and loans provided under subsections (a) and (c);\n**(2)**\nthe geographic distribution of the recipients of such grants and loans;\n**(3)**\nthe outcomes achieved by such grants and loans; and\n**(4)**\nany recommendations for improving the effectiveness of the program established under subsection (a).\n##### (g) Definitions\nIn this section:\n**(1)**\nThe term domestic animal means an animal, including a dog, cat, guinea pig, hamster, rabbit, or bird, that is not kept by the owner for any commercial purpose.\n**(2)**\nThe term eligible entity means\u2014\n**(A)**\na State, local, or Tribal government or an agency thereof; or\n**(B)**\na nonprofit corporation.\n**(3)**\nThe term rural area means any area other than\u2014\n**(A)**\na city or town that has a population of greater than 50,000 inhabitants; and\n**(B)**\nthe urbanized area contiguous and adjacent to such a city or town.\n**(4)**\nThe term Secretary means the Secretary of Agriculture, acting through the Under Secretary of Agriculture for Rural Development.",
      "versionDate": "2025-12-15",
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
        "name": "Animals",
        "updateDate": "2026-04-10T16:33:54Z"
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
      "date": "2025-12-15",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6716ih.xml"
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
      "title": "SATOS Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-01-06T08:42:13Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "SATOS Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-01-06T08:42:11Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Save Animals Through Operational Shelters Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-01-06T08:42:11Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To establish a program to provide grants and loans to facilitate the care, rehabilitation, and welfare of domestic animals in rural areas, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-01-06T08:33:51Z"
    }
  ]
}
```
