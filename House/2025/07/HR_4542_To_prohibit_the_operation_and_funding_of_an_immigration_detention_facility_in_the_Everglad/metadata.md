# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/4542?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/4542
- Title: No Cages in the Everglades Act
- Congress: 119
- Bill type: HR
- Bill number: 4542
- Origin chamber: House
- Introduced date: 2025-07-17
- Update date: 2026-05-16T08:07:01Z
- Update date including text: 2026-05-16T08:07:01Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-07-17: Introduced in House
- 2025-07-17 - IntroReferral: Introduced in House
- 2025-07-17 - IntroReferral: Introduced in House
- 2025-07-17 - IntroReferral: Referred to the Committee on the Judiciary, and in addition to the Committee on Homeland Security, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-07-17 - IntroReferral: Referred to the Committee on the Judiciary, and in addition to the Committee on Homeland Security, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-07-18 - Committee: Referred to the Subcommittee on Border Security and Enforcement.
- Latest action: 2025-07-17: Introduced in House

## Actions

- 2025-07-17 - IntroReferral: Introduced in House
- 2025-07-17 - IntroReferral: Introduced in House
- 2025-07-17 - IntroReferral: Referred to the Committee on the Judiciary, and in addition to the Committee on Homeland Security, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-07-17 - IntroReferral: Referred to the Committee on the Judiciary, and in addition to the Committee on Homeland Security, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-07-18 - Committee: Referred to the Subcommittee on Border Security and Enforcement.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-07-17",
    "latestAction": {
      "actionDate": "2025-07-17",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/4542",
    "number": "4542",
    "originChamber": "House",
    "policyArea": {
      "name": "Immigration"
    },
    "sponsors": [
      {
        "bioguideId": "W000797",
        "district": "25",
        "firstName": "Debbie",
        "fullName": "Rep. Wasserman Schultz, Debbie [D-FL-25]",
        "lastName": "Wasserman Schultz",
        "party": "D",
        "state": "FL"
      }
    ],
    "title": "No Cages in the Everglades Act",
    "type": "HR",
    "updateDate": "2026-05-16T08:07:01Z",
    "updateDateIncludingText": "2026-05-16T08:07:01Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-07-18",
      "committees": {
        "item": {
          "name": "Border Security and Enforcement Subcommittee",
          "systemCode": "hshm11"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Referred to the Subcommittee on Border Security and Enforcement.",
      "type": "Committee"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-07-17",
      "committees": {
        "item": {
          "name": "Homeland Security Committee",
          "systemCode": "hshm00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the Committee on the Judiciary, and in addition to the Committee on Homeland Security, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-07-17",
      "committees": {
        "item": {
          "name": "Judiciary Committee",
          "systemCode": "hsju00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the Committee on the Judiciary, and in addition to the Committee on Homeland Security, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-07-17",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-07-17",
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
          "date": "2025-07-17T13:08:45Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Homeland Security Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": {
              "date": "2025-07-18T20:24:30Z",
              "name": "Referred to"
            }
          },
          "name": "Border Security and Enforcement Subcommittee",
          "systemCode": "hshm11"
        }
      },
      "systemCode": "hshm00",
      "type": "Standing"
    },
    {
      "activities": {
        "item": {
          "date": "2025-07-17T13:08:40Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Judiciary Committee",
      "systemCode": "hsju00",
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
      "bioguideId": "F000476",
      "district": "10",
      "firstName": "Maxwell",
      "fullName": "Rep. Frost, Maxwell [D-FL-10]",
      "isOriginalCosponsor": "True",
      "lastName": "Frost",
      "party": "D",
      "sponsorshipDate": "2025-07-17",
      "state": "FL"
    },
    {
      "bioguideId": "C001066",
      "district": "14",
      "firstName": "Kathy",
      "fullName": "Rep. Castor, Kathy [D-FL-14]",
      "isOriginalCosponsor": "True",
      "lastName": "Castor",
      "party": "D",
      "sponsorshipDate": "2025-07-17",
      "state": "FL"
    },
    {
      "bioguideId": "S001200",
      "district": "9",
      "firstName": "Darren",
      "fullName": "Rep. Soto, Darren [D-FL-9]",
      "isOriginalCosponsor": "True",
      "lastName": "Soto",
      "party": "D",
      "sponsorshipDate": "2025-07-17",
      "state": "FL"
    },
    {
      "bioguideId": "F000462",
      "district": "22",
      "firstName": "Lois",
      "fullName": "Rep. Frankel, Lois [D-FL-22]",
      "isOriginalCosponsor": "True",
      "lastName": "Frankel",
      "party": "D",
      "sponsorshipDate": "2025-07-17",
      "state": "FL"
    },
    {
      "bioguideId": "W000808",
      "district": "24",
      "firstName": "Frederica",
      "fullName": "Rep. Wilson, Frederica S. [D-FL-24]",
      "isOriginalCosponsor": "True",
      "lastName": "Wilson",
      "middleName": "S.",
      "party": "D",
      "sponsorshipDate": "2025-07-17",
      "state": "FL"
    },
    {
      "bioguideId": "C001127",
      "district": "20",
      "firstName": "Sheila",
      "fullName": "Rep. Cherfilus-McCormick, Sheila [D-FL-20]",
      "isOriginalCosponsor": "True",
      "lastName": "Cherfilus-McCormick",
      "party": "D",
      "sponsorshipDate": "2025-07-17",
      "state": "FL"
    },
    {
      "bioguideId": "M001217",
      "district": "23",
      "firstName": "Jared",
      "fullName": "Rep. Moskowitz, Jared [D-FL-23]",
      "isOriginalCosponsor": "True",
      "lastName": "Moskowitz",
      "party": "D",
      "sponsorshipDate": "2025-07-17",
      "state": "FL"
    },
    {
      "bioguideId": "N000147",
      "district": "0",
      "firstName": "Eleanor",
      "fullName": "Del. Norton, Eleanor Holmes [D-DC-At Large]",
      "isOriginalCosponsor": "False",
      "lastName": "Norton",
      "middleName": "Holmes",
      "party": "D",
      "sponsorshipDate": "2025-07-22",
      "state": "DC"
    },
    {
      "bioguideId": "J000288",
      "district": "4",
      "firstName": "Henry",
      "fullName": "Rep. Johnson, Henry C. \"Hank\" [D-GA-4]",
      "isOriginalCosponsor": "False",
      "lastName": "Johnson",
      "middleName": "C. \"Hank\"",
      "party": "D",
      "sponsorshipDate": "2025-07-22",
      "state": "GA"
    },
    {
      "bioguideId": "C001130",
      "district": "30",
      "firstName": "Jasmine",
      "fullName": "Rep. Crockett, Jasmine [D-TX-30]",
      "isOriginalCosponsor": "False",
      "lastName": "Crockett",
      "party": "D",
      "sponsorshipDate": "2025-07-29",
      "state": "TX"
    },
    {
      "bioguideId": "L000602",
      "district": "12",
      "firstName": "Summer",
      "fullName": "Rep. Lee, Summer L. [D-PA-12]",
      "isOriginalCosponsor": "False",
      "lastName": "Lee",
      "middleName": "L.",
      "party": "D",
      "sponsorshipDate": "2025-07-29",
      "state": "PA"
    },
    {
      "bioguideId": "T000488",
      "district": "13",
      "firstName": "Shri",
      "fullName": "Rep. Thanedar, Shri [D-MI-13]",
      "isOriginalCosponsor": "False",
      "lastName": "Thanedar",
      "party": "D",
      "sponsorshipDate": "2025-07-29",
      "state": "MI"
    },
    {
      "bioguideId": "T000481",
      "district": "12",
      "firstName": "Rashida",
      "fullName": "Rep. Tlaib, Rashida [D-MI-12]",
      "isOriginalCosponsor": "False",
      "lastName": "Tlaib",
      "party": "D",
      "sponsorshipDate": "2025-07-29",
      "state": "MI"
    },
    {
      "bioguideId": "C001131",
      "district": "35",
      "firstName": "Greg",
      "fullName": "Rep. Casar, Greg [D-TX-35]",
      "isOriginalCosponsor": "False",
      "lastName": "Casar",
      "party": "D",
      "sponsorshipDate": "2025-08-15",
      "state": "TX"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr4542ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 4542\nIN THE HOUSE OF REPRESENTATIVES\nJuly 17, 2025 Ms. Wasserman Schultz (for herself, Mr. Frost , Ms. Castor of Florida , Mr. Soto , Ms. Lois Frankel of Florida , Ms. Wilson of Florida , Mrs. Cherfilus-McCormick , and Mr. Moskowitz ) introduced the following bill; which was referred to the Committee on the Judiciary , and in addition to the Committee on Homeland Security , for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned\nA BILL\nTo prohibit the operation and funding of an immigration detention facility in the Everglades, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the No Cages in the Everglades Act .\n#### 2. Prohibition on operation and funding of immigration detention facility in the Everglades\n##### (a) In general\nNotwithstanding any other provision of law, no funds made available to the Department of Homeland Security, including U.S. Immigration and Customs Enforcement, may be obligated or expended for the following:\n**(1)**\nPlanning, construction, leasing, operation, staffing, or maintenance of any immigration detention facility located within or adjacent to the Everglades ecosystem.\n**(2)**\nContracting with any public entity for the purposes described in paragraph (1).\n##### (b) Right of access\n**(1) In general**\nNotwithstanding any other provision of law, any facility, including any facility described in subsection (a)(1), used to detain or house individuals in the custody of the Department of Homeland Security, including U.S. Immigration and Customs Enforcement, or that is used to detain or house individuals by the Department, whether operated by the Federal Government or a State or local government, shall allow Members of Congress and designated congressional staff to conduct announced or unannounced inspections of such facility at any time, consistent with applicable security and safety protocols.\n**(2) Prohibition on limitation**\nThe right of access described in paragraph (1) may not be waived, limited, or conditioned by any contract, lease, memorandum of understanding, or other agreement between the Department of Homeland Security and any State or local government operator of a facility described in paragraph (1).\n**(3) Rule of construction**\nNothing in this subsection may be construed to require a Member of Congress or designated congressional staff to provide prior notice of the intent to enter a facility described in paragraph (1) for the purpose of conducting oversight.\n##### (c) Independent report\n**(1) In general**\nNot later than 90 days after the date of the enactment of this Act, the Inspector General of the Department of Homeland Security shall conduct an independent inquiry and submit to the appropriate congressional committees a report regarding the facility described in subsection (a)(1). Such report shall contain the following:\n**(A)**\nAn accounting of the use of funds allocated to or made available to the Department for such facility.\n**(B)**\nA description of the process that led to the construction of such facility.\n**(C)**\nAn evaluation of whether such facility satisfies minimum Federal standards, including the following:\n**(i)**\nNational Detention Standards (NDS) 2000.\n**(ii)**\nPerformance-Based National Detention Standards (PBNDS) 2008.\n**(iii)**\nPBNDS 2011.\n**(iv)**\nNDS 2019.\n**(v)**\nFamily Residential Standards 2020.\n**(vi)**\nTemporary Housing Standards.\n**(D)**\nA description of any formal or informal complaints registered by individuals detained at such facility regarding detention conditions, access to counsel, or treatment.\n**(E)**\nAn assessment of ecological risks resulting from the construction and operation of such facility, as well as the risks for detained individuals, officers, and staff at such facility as a result of flooding, hurricanes, or other natural disasters.\n**(2) Briefings**\nThe Inspector General of the Department of Homeland Security shall provide to the appropriate congressional committees briefings on the contents of the report required under paragraph (1).\n##### (d) Definitions\nIn this section:\n**(1) Appropriate congressional committees**\nThe term appropriate congressional committees means the following:\n**(A)**\nIn the House of Representatives, the following:\n**(i)**\nThe Committee on Homeland Security.\n**(ii)**\nThe Committee on the Judiciary.\n**(iii)**\nThe Committee on Appropriations.\n**(B)**\nIn the Senate, the following:\n**(i)**\nThe Committee on Homeland Security and Governmental Affairs.\n**(ii)**\nThe Committee on the Judiciary.\n**(iii)**\nThe Committee on Appropriations.\n**(2) Designated congressional staff**\nThe term designated congressional staff means any employee employed by the official office of a Member of Congress, or employed by an official Committee of the House of Representatives or the Senate.\n**(3) Everglades ecosystem**\nThe term Everglades ecosystem means the hydrologically connected wetland areas of southern Florida, including Big Cypress National Preserve, Everglades National Park, Water Conservation Areas, and adjacent wetlands.\n**(4) Facility**\nThe term facility means any building, site, or structure at which individuals in Department of Homeland Security custody are housed or detained.",
      "versionDate": "2025-07-17",
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
        "name": "Immigration",
        "updateDate": "2025-09-11T17:03:35Z"
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
      "date": "2025-07-17",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr4542ih.xml"
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
      "title": "No Cages in the Everglades Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-07-31T05:23:23Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "No Cages in the Everglades Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-07-31T05:23:22Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To prohibit the operation and funding of an immigration detention facility in the Everglades, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-07-31T05:18:39Z"
    }
  ]
}
```
