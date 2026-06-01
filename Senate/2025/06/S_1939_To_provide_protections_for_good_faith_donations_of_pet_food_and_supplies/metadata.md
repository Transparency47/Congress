# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/1939?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/1939
- Title: BARK Act of 2025
- Congress: 119
- Bill type: S
- Bill number: 1939
- Origin chamber: Senate
- Introduced date: 2025-06-04
- Update date: 2026-03-04T12:40:48Z
- Update date including text: 2026-03-04T12:40:48Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-06-04: Introduced in Senate
- 2025-06-04 - IntroReferral: Introduced in Senate
- 2025-06-04 - IntroReferral: Read twice and referred to the Committee on the Judiciary.
- Latest action: 2025-06-04: Introduced in Senate

## Actions

- 2025-06-04 - IntroReferral: Introduced in Senate
- 2025-06-04 - IntroReferral: Read twice and referred to the Committee on the Judiciary.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-06-04",
    "latestAction": {
      "actionDate": "2025-06-04",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/1939",
    "number": "1939",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Agriculture and Food"
    },
    "sponsors": [
      {
        "bioguideId": "W000790",
        "district": "",
        "firstName": "Raphael",
        "fullName": "Sen. Warnock, Raphael G. [D-GA]",
        "lastName": "Warnock",
        "party": "D",
        "state": "GA"
      }
    ],
    "title": "BARK Act of 2025",
    "type": "S",
    "updateDate": "2026-03-04T12:40:48Z",
    "updateDateIncludingText": "2026-03-04T12:40:48Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-06-04",
      "committees": {
        "item": {
          "name": "Judiciary Committee",
          "systemCode": "ssju00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on the Judiciary.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-06-04",
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
            "date": "2025-06-04T15:42:13Z",
            "name": "Referred To"
          },
          {
            "date": "2025-06-04T15:42:13Z",
            "name": "Referred To"
          }
        ]
      },
      "chamber": "Senate",
      "name": "Judiciary Committee",
      "systemCode": "ssju00",
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
      "bioguideId": "T000476",
      "firstName": "Thomas",
      "fullName": "Sen. Tillis, Thomas [R-NC]",
      "isOriginalCosponsor": "True",
      "lastName": "Tillis",
      "middleName": "Roland",
      "party": "R",
      "sponsorshipDate": "2025-06-04",
      "state": "NC"
    },
    {
      "bioguideId": "A000382",
      "firstName": "Angela",
      "fullName": "Sen. Alsobrooks, Angela D. [D-MD]",
      "isOriginalCosponsor": "False",
      "lastName": "Alsobrooks",
      "party": "D",
      "sponsorshipDate": "2025-06-18",
      "state": "MD"
    },
    {
      "bioguideId": "K000394",
      "firstName": "Andy",
      "fullName": "Sen. Kim, Andy [D-NJ]",
      "isOriginalCosponsor": "False",
      "lastName": "Kim",
      "party": "D",
      "sponsorshipDate": "2026-03-03",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1939is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 1939\nIN THE SENATE OF THE UNITED STATES\nJune 4, 2025 Mr. Warnock (for himself and Mr. Tillis ) introduced the following bill; which was read twice and referred to the Committee on the Judiciary\nA BILL\nTo provide protections for good faith donations of pet food and supplies.\n#### 1. Short title\nThis Act may be cited as the Bring Animals Relief and Kibble Act of 2025 or the BARK Act of 2025 .\n#### 2. Protections for good faith donations of pet food and supplies\n##### (a) Definitions\nIn this section:\n**(1) Apparently fit pet-related product**\nThe term apparently fit pet-related product means any pet food or pet supply that meets all quality and labeling standards imposed by Federal, State, and local laws and regulations even though the product may not be readily marketable due to appearance, age, freshness, grade, size, surplus, or other condition.\n**(2) Bill Emerson Good Samaritan Food Donation Act terms**\nThe terms donate , gross negligence , intentional misconduct , nonprofit organization , and person have the meanings given those terms in subsection (b) of the Bill Emerson Good Samaritan Food Donation Act ( 42 U.S.C. 1791(b) ).\n**(3) Emotional support animal**\nThe term emotional support animal means an animal that\u2014\n**(A)**\nis covered by the exclusions in section 5.303 of title 24, Code of Federal Regulations (or successor regulation); and\n**(B)**\nis not a service animal.\n**(4) Pet**\nThe term pet means a domesticated animal, such as a dog, cat, bird, rodent, fish, turtle, or other animal, that is kept for pleasure rather than for commercial purposes.\n**(5) Pet food**\nThe term pet food means any raw, cooked, processed, or prepared edible substance, ice, beverage, or ingredient used or intended for use in whole or in part for consumption by a qualified animal.\n**(6) Pet supply**\nThe term pet supply means tangible personal property used for a qualified animal, including pet carriers, crates, kennels, houses, cages, clothing, bedding, toys, collars, leashes, leads, tie-outs, feeders, bowls, dishes, pet gates, or pet doors.\n**(7) Qualified animal**\nThe term qualified animal means\u2014\n**(A)**\na pet;\n**(B)**\nan emotional support animal; and\n**(C)**\na service animal.\n**(8) Service animal**\nThe term service animal has the meaning given the term in section 36.104 of title 28, Code of Federal Regulations (or successor regulation).\n##### (b) Liability\n**(1) Persons**\nA person shall not be subject to civil or criminal liability arising from the nature, age, packaging, or condition of an apparently fit pet-related product that the person donates in good faith to a State or unit of local government or a nonprofit organization for ultimate distribution to qualified animals.\n**(2) Nonprofit organizations**\nA nonprofit organization shall not be subject to civil or criminal liability arising from the nature, age, packaging, or condition of an apparently fit pet-related product that the nonprofit organization received as a donation from a person in good faith for ultimate distribution to qualified animals.\n**(3) State and local governments**\nA State or unit of local government shall not be subject to liability arising from the nature, age, packaging, or condition of an apparently fit pet-related product that the State or unit of local government received as a donation from a person in good faith for ultimate distribution to qualified animals.\n**(4) Waiver not applicable to gross negligence or intentional misconduct**\nParagraphs (1), (2), and (3) shall not apply to an injury to, or the death of, an ultimate user or recipient of an apparently fit pet-related product that results from an act or omission of the person, nonprofit organization, or State or unit of local government, as applicable, constituting gross negligence or intentional misconduct.\n##### (c) Partial compliance\nIf a person donates, in good faith, pet food or pet supplies that do not meet all quality and labeling standards imposed by Federal, State, and local laws and regulations, that person shall not be subject to civil or criminal liability in accordance with this section if the State or unit of local government or nonprofit organization to which the food or supplies are donated\u2014\n**(1)**\nis informed by that person of the distressed or defective condition of the pet food or pet supplies;\n**(2)**\nagrees to recondition the pet food or pet supplies to comply with applicable quality and labeling standards prior to distribution; and\n**(3)**\nis knowledgeable of the applicable quality and labeling standards to properly recondition the pet food or pet supplies.\n##### (d) Rule of construction\nNothing in this section shall\u2014\n**(1)**\ncreate any liability; or\n**(2)**\nsupercede any State or local health regulations.",
      "versionDate": "2025-06-04",
      "versionType": "Introduced in Senate"
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
        "name": "Agriculture and Food",
        "updateDate": "2025-07-30T22:54:09Z"
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
      "date": "2025-06-04",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1939is.xml"
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
      "title": "BARK Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-03-04T12:40:48Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "BARK Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-06-10T02:53:15Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Bring Animals Relief and Kibble Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-06-10T02:53:15Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to provide protections for good faith donations of pet food and supplies.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-06-10T02:48:20Z"
    }
  ]
}
```
