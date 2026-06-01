# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/2179?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/2179
- Title: Canyon’s Law
- Congress: 119
- Bill type: S
- Bill number: 2179
- Origin chamber: Senate
- Introduced date: 2025-06-26
- Update date: 2026-01-06T12:04:06Z
- Update date including text: 2026-01-06T12:04:06Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-06-26: Introduced in Senate
- 2025-06-26 - IntroReferral: Introduced in Senate
- 2025-06-26 - IntroReferral: Read twice and referred to the Committee on Environment and Public Works.
- Latest action: 2025-06-26: Introduced in Senate

## Actions

- 2025-06-26 - IntroReferral: Introduced in Senate
- 2025-06-26 - IntroReferral: Read twice and referred to the Committee on Environment and Public Works.

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
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/2179",
    "number": "2179",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Public Lands and Natural Resources"
    },
    "sponsors": [
      {
        "bioguideId": "M001176",
        "district": "",
        "firstName": "Jeff",
        "fullName": "Sen. Merkley, Jeff [D-OR]",
        "lastName": "Merkley",
        "party": "D",
        "state": "OR"
      }
    ],
    "title": "Canyon\u2019s Law",
    "type": "S",
    "updateDate": "2026-01-06T12:04:06Z",
    "updateDateIncludingText": "2026-01-06T12:04:06Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-06-26",
      "committees": {
        "item": {
          "name": "Environment and Public Works Committee",
          "systemCode": "ssev00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Environment and Public Works.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-06-26",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in Senate",
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
        "item": [
          {
            "date": "2025-06-26T19:54:12Z",
            "name": "Referred To"
          },
          {
            "date": "2025-06-26T19:54:12Z",
            "name": "Referred To"
          }
        ]
      },
      "chamber": "Senate",
      "name": "Environment and Public Works Committee",
      "systemCode": "ssev00",
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
      "bioguideId": "S000033",
      "firstName": "Bernie",
      "fullName": "Sen. Sanders, Bernard [I-VT]",
      "isOriginalCosponsor": "True",
      "lastName": "Sanders",
      "party": "I",
      "sponsorshipDate": "2025-06-26",
      "state": "VT"
    },
    {
      "bioguideId": "W000779",
      "firstName": "Ron",
      "fullName": "Sen. Wyden, Ron [D-OR]",
      "isOriginalCosponsor": "True",
      "lastName": "Wyden",
      "party": "D",
      "sponsorshipDate": "2025-06-26",
      "state": "OR"
    },
    {
      "bioguideId": "W000802",
      "firstName": "Sheldon",
      "fullName": "Sen. Whitehouse, Sheldon [D-RI]",
      "isOriginalCosponsor": "True",
      "lastName": "Whitehouse",
      "party": "D",
      "sponsorshipDate": "2025-06-26",
      "state": "RI"
    },
    {
      "bioguideId": "V000128",
      "firstName": "Chris",
      "fullName": "Sen. Van Hollen, Chris [D-MD]",
      "isOriginalCosponsor": "True",
      "lastName": "Van Hollen",
      "party": "D",
      "sponsorshipDate": "2025-06-26",
      "state": "MD"
    },
    {
      "bioguideId": "H001046",
      "firstName": "Martin",
      "fullName": "Sen. Heinrich, Martin [D-NM]",
      "isOriginalCosponsor": "True",
      "lastName": "Heinrich",
      "party": "D",
      "sponsorshipDate": "2025-06-26",
      "state": "NM"
    },
    {
      "bioguideId": "S001150",
      "firstName": "Adam",
      "fullName": "Sen. Schiff, Adam B. [D-CA]",
      "isOriginalCosponsor": "True",
      "lastName": "Schiff",
      "middleName": "B.",
      "party": "D",
      "sponsorshipDate": "2025-06-26",
      "state": "CA"
    },
    {
      "bioguideId": "A000382",
      "firstName": "Angela",
      "fullName": "Sen. Alsobrooks, Angela D. [D-MD]",
      "isOriginalCosponsor": "True",
      "lastName": "Alsobrooks",
      "party": "D",
      "sponsorshipDate": "2025-06-26",
      "state": "MD"
    },
    {
      "bioguideId": "K000394",
      "firstName": "Andy",
      "fullName": "Sen. Kim, Andy [D-NJ]",
      "isOriginalCosponsor": "False",
      "lastName": "Kim",
      "party": "D",
      "sponsorshipDate": "2026-01-05",
      "state": "NJ"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2179is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 2179\nIN THE SENATE OF THE UNITED STATES\nJune 26 (legislative day, June 24), 2025 Mr. Merkley (for himself, Mr. Sanders , Mr. Wyden , Mr. Whitehouse , Mr. Van Hollen , Mr. Heinrich , Mr. Schiff , and Ms. Alsobrooks ) introduced the following bill; which was read twice and referred to the Committee on Environment and Public Works\nA BILL\nTo prohibit the use of M\u201344 devices, commonly known as cyanide bombs , on public land, and for other purposes.\n#### 1. Short title\nThis Act may be cited as Canyon\u2019s Law .\n#### 2. Findings\nCongress finds the following:\n**(1)**\nSodium cyanide is the highly toxic pesticide active ingredient used in M\u201344 devices, also known as cyanide bombs , and is used to kill coyotes, foxes, and wild dogs suspected of preying on livestock and poultry.\n**(2)**\nSodium cyanide is registered for restricted use under the Federal Insecticide, Fungicide, and Rodenticide Act ( 7 U.S.C. 136 et seq. ) as a Category One acute toxicant, the most hazardous Environmental Protection Agency classification available, due to the harm it poses to people and the environment.\n**(3)**\nPoisoning by sodium cyanide leads to central nervous system depression, cardiac arrest, respiratory failure, paralysis, and blindness.\n**(4)**\nThe Environmental Protection Agency authorizes the use of M\u201344 devices nationwide, and in recent years, M\u201344s were used in Colorado, Montana, North Dakota, Nebraska, New Mexico, Nevada, Oklahoma, Texas, West Virginia, and Wyoming.\n**(5)**\nIn 2017, an M\u201344 device exposed an Idaho child to a sublethal dose of sodium cyanide with subsequent short-term and long-term medical complications. Two Wyoming children were also exposed to the poison from another M\u201344 device. Three family dogs died in these two separate incidents. More than 50 family dogs have been documented as killed by M\u201344 devices since 1990. The full count is estimated to be significantly higher.\n**(6)**\nThe indiscriminate M\u201344 device commonly harms nontarget wildlife and people; at least 42 people have accidentally triggered a cyanide bomb causing exposure to cyanide gas and injuries since 1984. A Utah man, who was poisoned by an M\u201344 device in 2003 and permanently disabled, died in 2018 with cyanide poisoning from exposure to an M\u201344 device listed as a contributing cause of death on his death certificate.\n**(7)**\nM\u201344 devices kill targeted animals only 53 percent of the time. Thousands of nontarget species of animals have been killed by M\u201344s, including bald eagles, golden eagles, gray wolves, black bears, grizzly bears, bobcats, fishers, and family dogs.\n**(8)**\nDespite the United States Fish and Wildlife Service determining in 1993 that M\u201344 devices could kill endangered species like the California Condor, the use of the M\u201344 continues in areas where endangered species are found and continues to result in the deaths of endangered species.\n#### 3. Use of M\u201344 devices on public land prohibited\n##### (a) In general\nPreparing, placing, installing, setting, deploying, or otherwise using an M\u201344 device on public land is prohibited.\n##### (b) Removal\nNot later than 30 days after the date of the enactment of this Act, any Federal, State, or county agency that has prepared, placed, installed, set, or deployed an M\u201344 device on public land shall remove each such M\u201344 device from public land.\n##### (c) Definitions\nIn this Act:\n**(1) M\u201344 device**\n**(A) In general**\nThe term M\u201344 device means a device designed to propel sodium cyanide when triggered by an animal.\n**(B) Common names**\nThe term M\u201344 device includes any device that may be commonly known as an M\u201344 ejector device or an M\u201344 predator control device .\n**(2) Public land**\nThe term public land means any Federal land under the administrative jurisdiction of a public land management agency.\n**(3) Public land management agency**\nThe term public land management agency means each of, or a combination of, the following:\n**(A)**\nThe National Park Service.\n**(B)**\nThe United States Fish and Wildlife Service.\n**(C)**\nThe Bureau of Land Management.\n**(D)**\nThe Bureau of Reclamation.\n**(E)**\nThe Forest Service.",
      "versionDate": "2025-06-26",
      "versionType": "Introduced in Senate"
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
        "text": "Referred to the Committee on Natural Resources, and in addition to the Committee on Agriculture, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned."
      },
      "number": "4180",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Canyon\u2019s Law",
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
        "name": "Public Lands and Natural Resources",
        "updateDate": "2025-07-30T22:21:10Z"
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
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2179is.xml"
        }
      ],
      "type": "Introduced in Senate"
    }
  ]
}
```

## API Data: titles

```json
{
  "titles": [
    {
      "title": "Canyon\u2019s Law",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-01-06T12:04:06Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Canyon\u2019s Law",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-07-16T03:38:18Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to prohibit the use of M-44 devices, commonly known as \"cyanide bombs\", on public land, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-07-16T03:33:24Z"
    }
  ]
}
```
