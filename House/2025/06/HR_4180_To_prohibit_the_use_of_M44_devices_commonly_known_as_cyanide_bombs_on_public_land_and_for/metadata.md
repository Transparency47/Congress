# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/4180?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/4180
- Title: Canyon’s Law
- Congress: 119
- Bill type: HR
- Bill number: 4180
- Origin chamber: House
- Introduced date: 2025-06-26
- Update date: 2026-05-30T08:05:53Z
- Update date including text: 2026-05-30T08:05:53Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-06-26: Introduced in House
- 2025-06-26 - IntroReferral: Introduced in House
- 2025-06-26 - IntroReferral: Introduced in House
- 2025-06-26 - IntroReferral: Referred to the Committee on Natural Resources, and in addition to the Committee on Agriculture, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-06-26 - IntroReferral: Referred to the Committee on Natural Resources, and in addition to the Committee on Agriculture, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- Latest action: 2025-06-26: Introduced in House

## Actions

- 2025-06-26 - IntroReferral: Introduced in House
- 2025-06-26 - IntroReferral: Introduced in House
- 2025-06-26 - IntroReferral: Referred to the Committee on Natural Resources, and in addition to the Committee on Agriculture, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-06-26 - IntroReferral: Referred to the Committee on Natural Resources, and in addition to the Committee on Agriculture, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-06-26",
    "latestAction": {
      "actionDate": "2025-06-26",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/4180",
    "number": "4180",
    "originChamber": "House",
    "policyArea": {
      "name": "Public Lands and Natural Resources"
    },
    "sponsors": [
      {
        "bioguideId": "H001068",
        "district": "2",
        "firstName": "Jared",
        "fullName": "Rep. Huffman, Jared [D-CA-2]",
        "lastName": "Huffman",
        "party": "D",
        "state": "CA"
      }
    ],
    "title": "Canyon\u2019s Law",
    "type": "HR",
    "updateDate": "2026-05-30T08:05:53Z",
    "updateDateIncludingText": "2026-05-30T08:05:53Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-06-26",
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
      "text": "Referred to the Committee on Natural Resources, and in addition to the Committee on Agriculture, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-06-26",
      "committees": {
        "item": {
          "name": "Natural Resources Committee",
          "systemCode": "hsii00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the Committee on Natural Resources, and in addition to the Committee on Agriculture, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-06-26",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-06-26",
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
          "date": "2025-06-26T14:03:10Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Agriculture Committee",
      "systemCode": "hsag00",
      "type": "Standing"
    },
    {
      "activities": {
        "item": {
          "date": "2025-06-26T14:03:05Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Natural Resources Committee",
      "systemCode": "hsii00",
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
      "bioguideId": "C001068",
      "district": "9",
      "firstName": "Steve",
      "fullName": "Rep. Cohen, Steve [D-TN-9]",
      "isOriginalCosponsor": "True",
      "lastName": "Cohen",
      "party": "D",
      "sponsorshipDate": "2025-06-26",
      "state": "TN"
    },
    {
      "bioguideId": "D000617",
      "district": "1",
      "firstName": "Suzan",
      "fullName": "Rep. DelBene, Suzan K. [D-WA-1]",
      "isOriginalCosponsor": "True",
      "lastName": "DelBene",
      "middleName": "K.",
      "party": "D",
      "sponsorshipDate": "2025-06-26",
      "state": "WA"
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
      "sponsorshipDate": "2025-06-26",
      "state": "DC"
    },
    {
      "bioguideId": "M001241",
      "district": "47",
      "firstName": "Dave",
      "fullName": "Rep. Min, Dave [D-CA-47]",
      "isOriginalCosponsor": "True",
      "lastName": "Min",
      "party": "D",
      "sponsorshipDate": "2025-06-26",
      "state": "CA"
    },
    {
      "bioguideId": "S001145",
      "district": "9",
      "firstName": "Janice",
      "fullName": "Rep. Schakowsky, Janice D. [D-IL-9]",
      "isOriginalCosponsor": "True",
      "lastName": "Schakowsky",
      "middleName": "D.",
      "party": "D",
      "sponsorshipDate": "2025-06-26",
      "state": "IL"
    },
    {
      "bioguideId": "B001285",
      "district": "26",
      "firstName": "Julia",
      "fullName": "Rep. Brownley, Julia [D-CA-26]",
      "isOriginalCosponsor": "True",
      "lastName": "Brownley",
      "party": "D",
      "sponsorshipDate": "2025-06-26",
      "state": "CA"
    },
    {
      "bioguideId": "F000476",
      "district": "10",
      "firstName": "Maxwell",
      "fullName": "Rep. Frost, Maxwell [D-FL-10]",
      "isOriginalCosponsor": "False",
      "lastName": "Frost",
      "party": "D",
      "sponsorshipDate": "2025-07-17",
      "state": "FL"
    },
    {
      "bioguideId": "H001047",
      "district": "4",
      "firstName": "James",
      "fullName": "Rep. Himes, James A. [D-CT-4]",
      "isOriginalCosponsor": "False",
      "lastName": "Himes",
      "middleName": "A.",
      "party": "D",
      "sponsorshipDate": "2025-09-15",
      "state": "CT"
    },
    {
      "bioguideId": "S001201",
      "district": "3",
      "firstName": "Thomas",
      "fullName": "Rep. Suozzi, Thomas R. [D-NY-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Suozzi",
      "middleName": "R.",
      "party": "D",
      "sponsorshipDate": "2025-10-21",
      "state": "NY"
    },
    {
      "bioguideId": "L000593",
      "district": "49",
      "firstName": "Mike",
      "fullName": "Rep. Levin, Mike [D-CA-49]",
      "isOriginalCosponsor": "False",
      "lastName": "Levin",
      "party": "D",
      "sponsorshipDate": "2025-10-28",
      "state": "CA"
    },
    {
      "bioguideId": "L000397",
      "district": "18",
      "firstName": "Zoe",
      "fullName": "Rep. Lofgren, Zoe [D-CA-18]",
      "isOriginalCosponsor": "False",
      "lastName": "Lofgren",
      "party": "D",
      "sponsorshipDate": "2026-01-30",
      "state": "CA"
    },
    {
      "bioguideId": "E000299",
      "district": "16",
      "firstName": "Veronica",
      "fullName": "Rep. Escobar, Veronica [D-TX-16]",
      "isOriginalCosponsor": "False",
      "lastName": "Escobar",
      "party": "D",
      "sponsorshipDate": "2026-05-29",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr4180ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 4180\nIN THE HOUSE OF REPRESENTATIVES\nJune 26, 2025 Mr. Huffman (for himself, Mr. Cohen , Ms. DelBene , Ms. Norton , Mr. Min , Ms. Schakowsky , and Ms. Brownley ) introduced the following bill; which was referred to the Committee on Natural Resources , and in addition to the Committee on Agriculture , for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned\nA BILL\nTo prohibit the use of M\u201344 devices, commonly known as cyanide bombs , on public land, and for other purposes.\n#### 1. Short title\nThis Act may be cited as Canyon\u2019s Law .\n#### 2. Findings\nCongress finds the following:\n**(1)**\nSodium cyanide is the highly toxic pesticide active ingredient used in M\u201344 devices, also known as cyanide bombs , and is used to kill coyotes, foxes, and wild dogs suspected of preying on livestock and poultry.\n**(2)**\nSodium cyanide is registered for restricted use under the Federal Insecticide, Fungicide, and Rodenticide Act ( 7 U.S.C. 136 et seq. ) as a Category One acute toxicant, the most hazardous Environmental Protection Agency classification available, due to the harm it poses to people and the environment.\n**(3)**\nPoisoning by sodium cyanide leads to central nervous system depression, cardiac arrest, respiratory failure, paralysis, and blindness.\n**(4)**\nThe Environmental Protection Agency authorizes the use of M\u201344 devices nationwide, and in recent years, M\u201344s were used in Colorado, Montana, North Dakota, Nebraska, New Mexico, Nevada, Oklahoma, Texas, West Virginia, and Wyoming.\n**(5)**\nIn 2017, an M\u201344 device exposed an Idaho child to a sublethal dose of sodium cyanide with subsequent short-term and long-term medical complications. Two Wyoming children were also exposed to the poison from another M\u201344 device. Three family dogs died in these two separate incidents.\n**(6)**\nMore than 50 family dogs have been documented as killed by M\u201344 devices since 1990, and the full count is estimated to be significantly higher.\n**(7)**\nThe indiscriminate M\u201344 device commonly harms nontarget wildlife and people; at least 42 people have accidentally triggered a cyanide bomb causing exposure to cyanide gas and injuries since 1984.\n**(8)**\nA Utah man, who was poisoned by an M\u201344 in 2003 and permanently disabled, died in 2018 with cyanide poisoning from exposure to an M\u201344 device listed as a contributing cause of death on his death certificate.\n**(9)**\nM\u201344 devices kill targeted animals only 53 percent of the time. Thousands of nontarget species of animals have been killed by M\u201344s, including bald eagles, golden eagles, gray wolves, black bears, grizzly bears, bobcats, fishers, and family dogs.\n**(10)**\nDespite the United States Fish and Wildlife Service determining in 1993 that M\u201344 devices could kill endangered species like the California Condor, the use of the M\u201344 continues in areas where endangered species are found and continues to result in the deaths of endangered species.\n#### 3. Use of M\u201344 devices on public land prohibited\n##### (a) In general\nPreparing, placing, installing, setting, deploying, or otherwise using an M\u201344 device on public land is prohibited.\n##### (b) Removal\nNot later than 30 days after the date of the enactment of this Act, any Federal, State, or county agency that has prepared, placed, installed, set, or deployed an M\u201344 device on public land shall remove each such M\u201344 device from public land.\n##### (c) Definitions\nIn this Act:\n**(1) M\u201344 device**\n**(A) In general**\nThe term M\u201344 device means a device designed to propel sodium cyanide when triggered by an animal.\n**(B) Common names**\nThe term M\u201344 device includes any device that may be commonly known as an M\u201344 ejector device or an M\u201344 predator control device .\n**(2) Public land**\nThe term public land means any Federal land under the administrative jurisdiction of a public land management agency.\n**(3) Public land management agency**\nThe term public land management agency means each of, or a combination of, the following:\n**(A)**\nThe National Park Service.\n**(B)**\nThe United States Fish and Wildlife Service.\n**(C)**\nThe Bureau of Land Management.\n**(D)**\nThe Bureau of Reclamation.\n**(E)**\nThe Forest Service.",
      "versionDate": "2025-06-26",
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
        "actionDate": "2025-06-26",
        "text": "Read twice and referred to the Committee on Environment and Public Works."
      },
      "number": "2179",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Canyon\u2019s Law",
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
        "name": "Public Lands and Natural Resources",
        "updateDate": "2025-07-24T12:44:02Z"
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
      "date": "2025-06-26",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr4180ih.xml"
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
      "title": "Canyon\u2019s Law",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-07-15T04:23:22Z"
    },
    {
      "title": "Canyon\u2019s Law",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-07-15T04:23:22Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To prohibit the use of M-44 devices, commonly known as \"cyanide bombs\", on public land, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-07-15T04:18:29Z"
    }
  ]
}
```
