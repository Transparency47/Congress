# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/8494?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/8494
- Title: To prohibit the Department of Homeland Security from entering into, modifying, extending, or renewing, any contract or intergovernmental service agreement to establish or operate any new immigration detention model, including the use of warehouses, modular facilities, soft-sided structures, tent systems, and processing centers.
- Congress: 119
- Bill type: HR
- Bill number: 8494
- Origin chamber: House
- Introduced date: 2026-04-23
- Update date: 2026-05-30T08:06:06Z
- Update date including text: 2026-05-30T08:06:06Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2026-04-23: Introduced in House
- 2026-04-23 - IntroReferral: Introduced in House
- 2026-04-23 - IntroReferral: Introduced in House
- 2026-04-23 - IntroReferral: Referred to the Committee on the Judiciary, and in addition to the Committee on Homeland Security, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2026-04-23 - IntroReferral: Referred to the Committee on the Judiciary, and in addition to the Committee on Homeland Security, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2026-04-24 - Committee: Referred to the Subcommittee on Oversight, Investigations, and Accountability.
- Latest action: 2026-04-23: Introduced in House

## Actions

- 2026-04-23 - IntroReferral: Introduced in House
- 2026-04-23 - IntroReferral: Introduced in House
- 2026-04-23 - IntroReferral: Referred to the Committee on the Judiciary, and in addition to the Committee on Homeland Security, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2026-04-23 - IntroReferral: Referred to the Committee on the Judiciary, and in addition to the Committee on Homeland Security, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2026-04-24 - Committee: Referred to the Subcommittee on Oversight, Investigations, and Accountability.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-04-23",
    "latestAction": {
      "actionDate": "2026-04-23",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/8494",
    "number": "8494",
    "originChamber": "House",
    "policyArea": {
      "name": "Immigration"
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
    "title": "To prohibit the Department of Homeland Security from entering into, modifying, extending, or renewing, any contract or intergovernmental service agreement to establish or operate any new immigration detention model, including the use of warehouses, modular facilities, soft-sided structures, tent systems, and processing centers.",
    "type": "HR",
    "updateDate": "2026-05-30T08:06:06Z",
    "updateDateIncludingText": "2026-05-30T08:06:06Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-04-24",
      "committees": {
        "item": {
          "name": "Oversight, Investigations, and Accountability Subcommittee",
          "systemCode": "hshm09"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Referred to the Subcommittee on Oversight, Investigations, and Accountability.",
      "type": "Committee"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2026-04-23",
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
      "actionDate": "2026-04-23",
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
      "actionDate": "2026-04-23",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-04-23",
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
          "date": "2026-04-23T13:03:25Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Homeland Security Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": {
              "date": "2026-04-24T19:43:44Z",
              "name": "Referred to"
            }
          },
          "name": "Oversight, Investigations, and Accountability Subcommittee",
          "systemCode": "hshm09"
        }
      },
      "systemCode": "hshm00",
      "type": "Standing"
    },
    {
      "activities": {
        "item": {
          "date": "2026-04-23T13:03:20Z",
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
      "bioguideId": "M001232",
      "district": "6",
      "firstName": "April",
      "fullName": "Rep. McClain Delaney, April [D-MD-6]",
      "isOriginalCosponsor": "True",
      "lastName": "McClain Delaney",
      "party": "D",
      "sponsorshipDate": "2026-04-23",
      "state": "MD"
    },
    {
      "bioguideId": "C001067",
      "district": "9",
      "firstName": "Yvette",
      "fullName": "Rep. Clarke, Yvette D. [D-NY-9]",
      "isOriginalCosponsor": "True",
      "lastName": "Clarke",
      "middleName": "D.",
      "party": "D",
      "sponsorshipDate": "2026-04-23",
      "state": "NY"
    },
    {
      "bioguideId": "R000617",
      "district": "3",
      "firstName": "Delia",
      "fullName": "Rep. Ramirez, Delia C. [D-IL-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Ramirez",
      "middleName": "C.",
      "party": "D",
      "sponsorshipDate": "2026-04-23",
      "state": "IL"
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
      "sponsorshipDate": "2026-04-23",
      "state": "DC"
    },
    {
      "bioguideId": "G000599",
      "district": "10",
      "firstName": "Daniel",
      "fullName": "Rep. Goldman, Daniel S. [D-NY-10]",
      "isOriginalCosponsor": "True",
      "lastName": "Goldman",
      "middleName": "S.",
      "party": "D",
      "sponsorshipDate": "2026-04-23",
      "state": "NY"
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
      "sponsorshipDate": "2026-04-23",
      "state": "IL"
    },
    {
      "bioguideId": "M001234",
      "district": "3",
      "firstName": "Kelly",
      "fullName": "Rep. Morrison, Kelly [D-MN-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Morrison",
      "party": "D",
      "sponsorshipDate": "2026-04-23",
      "state": "MN"
    },
    {
      "bioguideId": "T000488",
      "district": "13",
      "firstName": "Shri",
      "fullName": "Rep. Thanedar, Shri [D-MI-13]",
      "isOriginalCosponsor": "True",
      "lastName": "Thanedar",
      "party": "D",
      "sponsorshipDate": "2026-04-23",
      "state": "MI"
    },
    {
      "bioguideId": "S001226",
      "district": "6",
      "firstName": "Andrea",
      "fullName": "Rep. Salinas, Andrea [D-OR-6]",
      "isOriginalCosponsor": "True",
      "lastName": "Salinas",
      "party": "D",
      "sponsorshipDate": "2026-04-23",
      "state": "OR"
    },
    {
      "bioguideId": "D000096",
      "district": "7",
      "firstName": "Danny",
      "fullName": "Rep. Davis, Danny K. [D-IL-7]",
      "isOriginalCosponsor": "True",
      "lastName": "Davis",
      "middleName": "K.",
      "party": "D",
      "sponsorshipDate": "2026-04-23",
      "state": "IL"
    },
    {
      "bioguideId": "G000553",
      "district": "9",
      "firstName": "Al",
      "fullName": "Rep. Green, Al [D-TX-9]",
      "isOriginalCosponsor": "True",
      "lastName": "Green",
      "party": "D",
      "sponsorshipDate": "2026-04-23",
      "state": "TX"
    },
    {
      "bioguideId": "G000606",
      "district": "7",
      "firstName": "Adelita",
      "fullName": "Rep. Grijalva, Adelita S. [D-AZ-7]",
      "isOriginalCosponsor": "True",
      "lastName": "Grijalva",
      "middleName": "S.",
      "party": "D",
      "sponsorshipDate": "2026-04-23",
      "state": "AZ"
    },
    {
      "bioguideId": "C001091",
      "district": "20",
      "firstName": "Joaquin",
      "fullName": "Rep. Castro, Joaquin [D-TX-20]",
      "isOriginalCosponsor": "True",
      "lastName": "Castro",
      "party": "D",
      "sponsorshipDate": "2026-04-23",
      "state": "TX"
    },
    {
      "bioguideId": "S001231",
      "district": "12",
      "firstName": "Lateefah",
      "fullName": "Rep. Simon, Lateefah [D-CA-12]",
      "isOriginalCosponsor": "False",
      "lastName": "Simon",
      "party": "D",
      "sponsorshipDate": "2026-04-27",
      "state": "CA"
    },
    {
      "bioguideId": "C001131",
      "district": "35",
      "firstName": "Greg",
      "fullName": "Rep. Casar, Greg [D-TX-35]",
      "isOriginalCosponsor": "False",
      "lastName": "Casar",
      "party": "D",
      "sponsorshipDate": "2026-04-27",
      "state": "TX"
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
      "sponsorshipDate": "2026-04-27",
      "state": "TX"
    },
    {
      "bioguideId": "T000472",
      "district": "39",
      "firstName": "Mark",
      "fullName": "Rep. Takano, Mark [D-CA-39]",
      "isOriginalCosponsor": "False",
      "lastName": "Takano",
      "party": "D",
      "sponsorshipDate": "2026-04-27",
      "state": "CA"
    },
    {
      "bioguideId": "C001119",
      "district": "2",
      "firstName": "Angie",
      "fullName": "Rep. Craig, Angie [D-MN-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Craig",
      "party": "D",
      "sponsorshipDate": "2026-04-30",
      "state": "MN"
    },
    {
      "bioguideId": "M000687",
      "district": "7",
      "firstName": "Kweisi",
      "fullName": "Rep. Mfume, Kweisi [D-MD-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Mfume",
      "party": "D",
      "sponsorshipDate": "2026-04-30",
      "state": "MD"
    },
    {
      "bioguideId": "W000808",
      "district": "24",
      "firstName": "Frederica",
      "fullName": "Rep. Wilson, Frederica S. [D-FL-24]",
      "isOriginalCosponsor": "False",
      "lastName": "Wilson",
      "middleName": "S.",
      "party": "D",
      "sponsorshipDate": "2026-05-07",
      "state": "FL"
    },
    {
      "bioguideId": "E000299",
      "district": "16",
      "firstName": "Veronica",
      "fullName": "Rep. Escobar, Veronica [D-TX-16]",
      "isOriginalCosponsor": "False",
      "lastName": "Escobar",
      "party": "D",
      "sponsorshipDate": "2026-05-12",
      "state": "TX"
    },
    {
      "bioguideId": "M001143",
      "district": "4",
      "firstName": "Betty",
      "fullName": "Rep. McCollum, Betty [D-MN-4]",
      "isOriginalCosponsor": "False",
      "lastName": "McCollum",
      "party": "D",
      "sponsorshipDate": "2026-05-14",
      "state": "MN"
    },
    {
      "bioguideId": "J000298",
      "district": "7",
      "firstName": "Pramila",
      "fullName": "Rep. Jayapal, Pramila [D-WA-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Jayapal",
      "party": "D",
      "sponsorshipDate": "2026-05-19",
      "state": "WA"
    },
    {
      "bioguideId": "H001094",
      "district": "4",
      "firstName": "Val",
      "fullName": "Rep. Hoyle, Val T. [D-OR-4]",
      "isOriginalCosponsor": "False",
      "lastName": "Hoyle",
      "middleName": "T.",
      "party": "D",
      "sponsorshipDate": "2026-05-29",
      "state": "OR"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr8494ih.xml",
      "text": "I\n119th CONGRESS\n2d Session\nH. R. 8494\nIN THE HOUSE OF REPRESENTATIVES\nApril 23, 2026 Ms. Tlaib (for herself, Mrs. McClain Delaney , Ms. Clarke of New York , Mrs. Ramirez , Ms. Norton , Mr. Goldman of New York , Mr. Garc\u00eda of Illinois , Ms. Morrison , Mr. Thanedar , Ms. Salinas , Mr. Davis of Illinois , Mr. Green of Texas , Mrs. Grijalva , and Mr. Castro of Texas ) introduced the following bill; which was referred to the Committee on the Judiciary , and in addition to the Committee on Homeland Security , for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned\nA BILL\nTo prohibit the Department of Homeland Security from entering into, modifying, extending, or renewing, any contract or intergovernmental service agreement to establish or operate any new immigration detention model, including the use of warehouses, modular facilities, soft-sided structures, tent systems, and processing centers.\n#### 1. Prohibition on new immigration models\n##### (a) Findings\nCongress finds the following:\n**(1)**\nThe Department of Homeland Security, acting through U.S. Immigration and Customs Enforcement, has announced plans to spend approximately $38,300,000,000 to acquire and retrofit warehouses and industrial facilities into large-scale immigration detention centers.\n**(2)**\nSuch planned expansion includes the use of warehouses, modular facilities, soft-sided structures, tent systems, processing centers, or other alternative detention facility models.\n**(3)**\nThe facilities that the Department of Homeland Security is attempting to develop are similar to facilities used to incarcerate about 120,000 people of Japanese descent, as well as many others, in internment camps in the United States from 1942 through 1946, a grave violation of human rights and a dark chapter in our history.\n**(4)**\nImmigration detention has detrimental and long-lasting impacts on individuals detained, their families, and their communities.\n**(5)**\nDecades of documentation have proven that, across the immigration detention system, U.S. Immigration and Customs Enforcement subjects people to violations of their basic rights and unconscionable conditions, including medical neglect, overcrowding, cruel and unusual conditions of confinement, and rampant transfers that disappear people deeper into the detention system, sowing confusion and cutting people off from their loved ones and support networks.\n**(6)**\nDeaths in immigration detention facilities have occurred under the supervision of the Department of Homeland Security, including 33 reported deaths in 2025 and 13 deaths so far in 2026.\n**(7)**\nThe expansion of immigration facilities adversely harms surrounding communities through increased surveillance, infrastructure strain, environmental impact, and diversion of local resources.\n**(8)**\nThe expansion, creation, or repurposing of buildings as detention facilities diverts critical resources such as water and electricity away from the local communities, could cut off local tax revenue, and forecloses other economic opportunities for local communities.\n**(9)**\nFacilities not originally constructed for the purposes of detaining or processing individuals drastically lack appropriate infrastructure, including sewage, sanitation, and water systems necessary to protect public health and would further exacerbate the unacceptable conditions named above.\n**(10)**\nCongress has the authority to condition and prohibit the use of Federal funds and facilities.\n##### (b) Prohibition on new immigration models\nNotwithstanding any other provision of law, a covered agency may not\u2014\n**(1)**\nestablish or implement any new immigration detention model; or\n**(2)**\nestablish, operate, expand, convert, or renovate any warehouse, industrial facility, tent, soft-sided structure, modular unit, or similar building or structure for the purposes of housing, processing, or detaining individuals under civil immigration authority.\n##### (c) Prohibition on use of funds\n**(1) In general**\nNotwithstanding any other provision of law, none of the amounts made available before the date of the enactment of this Act for any fiscal year or otherwise made available to any covered agency may be obligated or expended to establish, construct, renovate, expand, or operate any new immigration detention model, including any warehouse, industrial facility, tent, soft-sided structure, modular unit, or similar building or structure, whether directly operated by U.S. Immigration and Customs Enforcement or by another governmental or nongovernmental contractor.\n**(2) Prohibition on transfer**\nNone of the amounts made available before the date of the enactment of this Act, may be reprogrammed or transferred for the purposes of operating or constructing immigration detention facilities, processing facilities, holding facilities, or non-traditional facilities.\n**(3) Transfer of funds**\nAmounts obligated to operate new immigration detention models, including any warehouse, industrial facility, tent, soft-sided structure, modular unit, or similar building or structure shall be transferred to needed services such as affordable health care and housing.\n##### (d) Definitions\nIn this section:\n**(1) Covered agency**\nThe term covered agency means the Department of Homeland Security, including U.S. Immigration and Customs Enforcement, and any component thereof.\n**(2) Department**\nThe term Department means the Department of Homeland Security.\n**(3) Detention facility**\nThe term detention facility means any facility, building, or structure used to hold, process, house, or detain individuals pursuant to civil immigration authority.\n**(4) Expand**\nThe term expand includes constructing, acquiring, leasing, retrofitting, modifying, renovating, or increasing the bed capacity of a detention facility.\n**(5) New immigration model**\nThe term new immigration model means any newly created, rebranded, temporary, emergency, or alternative detention framework that results in immigration detention.\n##### (e) Effective date\nThis Act shall take effect on the date of the enactment of this Act.",
      "versionDate": "2026-04-23",
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
        "updateDate": "2026-05-06T15:29:58Z"
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
      "date": "2026-04-23",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr8494ih.xml"
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
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To prohibit the Department of Homeland Security from entering into, modifying, extending, or renewing, any contract or intergovernmental service agreement to establish or operate any new immigration detention model, including the use of warehouses, modular facilities, soft-sided structures, tent systems, and processing centers.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-04-28T05:48:27Z"
    },
    {
      "title": "To prohibit the Department of Homeland Security from entering into, modifying, extending, or renewing, any contract or intergovernmental service agreement to establish or operate any new immigration detention model, including the use of warehouses, modular facilities, soft-sided structures, tent systems, and processing centers.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-04-24T08:06:26Z"
    }
  ]
}
```
