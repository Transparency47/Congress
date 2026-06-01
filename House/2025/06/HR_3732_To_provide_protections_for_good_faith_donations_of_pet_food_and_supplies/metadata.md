# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/3732?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/3732
- Title: BARK Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 3732
- Origin chamber: House
- Introduced date: 2025-06-04
- Update date: 2026-05-05T12:24:41Z
- Update date including text: 2026-05-05T12:24:41Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-06-04: Introduced in House
- 2025-06-04 - IntroReferral: Introduced in House
- 2025-06-04 - IntroReferral: Introduced in House
- 2025-06-04 - IntroReferral: Referred to the House Committee on the Judiciary.
- Latest action: 2025-06-04: Introduced in House

## Actions

- 2025-06-04 - IntroReferral: Introduced in House
- 2025-06-04 - IntroReferral: Introduced in House
- 2025-06-04 - IntroReferral: Referred to the House Committee on the Judiciary.

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
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/3732",
    "number": "3732",
    "originChamber": "House",
    "policyArea": {
      "name": "Agriculture and Food"
    },
    "sponsors": [
      {
        "bioguideId": "R000606",
        "district": "8",
        "firstName": "Jamie",
        "fullName": "Rep. Raskin, Jamie [D-MD-8]",
        "lastName": "Raskin",
        "party": "D",
        "state": "MD"
      }
    ],
    "title": "BARK Act of 2025",
    "type": "HR",
    "updateDate": "2026-05-05T12:24:41Z",
    "updateDateIncludingText": "2026-05-05T12:24:41Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-06-04",
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
      "text": "Referred to the House Committee on the Judiciary.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-06-04",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-06-04",
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
          "date": "2025-06-04T14:02:15Z",
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
      "bioguideId": "K000397",
      "district": "40",
      "firstName": "Young",
      "fullName": "Rep. Kim, Young [R-CA-40]",
      "isOriginalCosponsor": "True",
      "lastName": "Kim",
      "party": "R",
      "sponsorshipDate": "2025-06-04",
      "state": "CA"
    },
    {
      "bioguideId": "M001208",
      "district": "6",
      "firstName": "Lucy",
      "fullName": "Rep. McBath, Lucy [D-GA-6]",
      "isOriginalCosponsor": "True",
      "lastName": "McBath",
      "party": "D",
      "sponsorshipDate": "2025-06-04",
      "state": "GA"
    },
    {
      "bioguideId": "F000466",
      "district": "1",
      "firstName": "Brian",
      "fullName": "Rep. Fitzpatrick, Brian K. [R-PA-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Fitzpatrick",
      "middleName": "K.",
      "party": "R",
      "sponsorshipDate": "2025-06-04",
      "state": "PA"
    },
    {
      "bioguideId": "D000624",
      "district": "6",
      "firstName": "Debbie",
      "fullName": "Rep. Dingell, Debbie [D-MI-6]",
      "isOriginalCosponsor": "True",
      "lastName": "Dingell",
      "party": "D",
      "sponsorshipDate": "2025-06-04",
      "state": "MI"
    },
    {
      "bioguideId": "M000317",
      "district": "11",
      "firstName": "Nicole",
      "fullName": "Rep. Malliotakis, Nicole [R-NY-11]",
      "isOriginalCosponsor": "True",
      "lastName": "Malliotakis",
      "party": "R",
      "sponsorshipDate": "2025-06-04",
      "state": "NY"
    },
    {
      "bioguideId": "T000468",
      "district": "1",
      "firstName": "Dina",
      "fullName": "Rep. Titus, Dina [D-NV-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Titus",
      "party": "D",
      "sponsorshipDate": "2025-06-05",
      "state": "NV"
    },
    {
      "bioguideId": "T000478",
      "district": "24",
      "firstName": "Claudia",
      "fullName": "Rep. Tenney, Claudia [R-NY-24]",
      "isOriginalCosponsor": "False",
      "lastName": "Tenney",
      "party": "R",
      "sponsorshipDate": "2025-06-05",
      "state": "NY"
    },
    {
      "bioguideId": "S001228",
      "district": "2",
      "firstName": "Derek",
      "fullName": "Rep. Schmidt, Derek [R-KS-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Schmidt",
      "party": "R",
      "sponsorshipDate": "2025-07-10",
      "state": "KS"
    },
    {
      "bioguideId": "E000301",
      "district": "3",
      "firstName": "Sarah",
      "fullName": "Rep. Elfreth, Sarah [D-MD-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Elfreth",
      "party": "D",
      "sponsorshipDate": "2025-07-10",
      "state": "MD"
    },
    {
      "bioguideId": "S001229",
      "district": "6",
      "firstName": "Jefferson",
      "fullName": "Rep. Shreve, Jefferson [R-IN-6]",
      "isOriginalCosponsor": "False",
      "lastName": "Shreve",
      "party": "R",
      "sponsorshipDate": "2025-07-14",
      "state": "IN"
    },
    {
      "bioguideId": "P000607",
      "district": "2",
      "firstName": "Mark",
      "fullName": "Rep. Pocan, Mark [D-WI-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Pocan",
      "party": "D",
      "sponsorshipDate": "2025-07-14",
      "state": "WI"
    },
    {
      "bioguideId": "H001085",
      "district": "6",
      "firstName": "Chrissy",
      "fullName": "Rep. Houlahan, Chrissy [D-PA-6]",
      "isOriginalCosponsor": "False",
      "lastName": "Houlahan",
      "party": "D",
      "sponsorshipDate": "2025-07-16",
      "state": "PA"
    },
    {
      "bioguideId": "V000133",
      "district": "2",
      "firstName": "Jefferson",
      "fullName": "Rep. Van Drew, Jefferson [R-NJ-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Van Drew",
      "party": "R",
      "sponsorshipDate": "2025-11-07",
      "state": "NJ"
    },
    {
      "bioguideId": "S001221",
      "district": "3",
      "firstName": "Hillary",
      "fullName": "Rep. Scholten, Hillary J. [D-MI-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Scholten",
      "middleName": "J.",
      "party": "D",
      "sponsorshipDate": "2025-11-07",
      "state": "MI"
    },
    {
      "bioguideId": "L000596",
      "district": "13",
      "firstName": "Anna Paulina",
      "fullName": "Rep. Luna, Anna Paulina [R-FL-13]",
      "isOriginalCosponsor": "False",
      "lastName": "Luna",
      "party": "R",
      "sponsorshipDate": "2026-02-11",
      "state": "FL"
    },
    {
      "bioguideId": "D000623",
      "district": "10",
      "firstName": "Mark",
      "fullName": "Rep. DeSaulnier, Mark [D-CA-10]",
      "isOriginalCosponsor": "False",
      "lastName": "DeSaulnier",
      "party": "D",
      "sponsorshipDate": "2026-02-11",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr3732ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 3732\nIN THE HOUSE OF REPRESENTATIVES\nJune 4, 2025 Mr. Raskin (for himself, Mrs. Kim , Mrs. McBath , Mr. Fitzpatrick , Mrs. Dingell , and Ms. Malliotakis ) introduced the following bill; which was referred to the Committee on the Judiciary\nA BILL\nTo provide protections for good faith donations of pet food and supplies.\n#### 1. Short title\nThis Act may be cited as the Bring Animals Relief and Kibble Act of 2025 or the BARK Act of 2025 .\n#### 2. Liability for damages from good faith donations of pet food and supplies\n##### (a) In general\n**(1) Liability of persons**\nA person shall not be subject to civil or criminal liability arising from the nature, age, packaging, or condition of an apparently fit pet-related product that the person donates in good faith to a State or unit of local government or a nonprofit organization for ultimate distribution to qualified animals.\n**(2) Liability of nonprofit organizations**\nA nonprofit organization shall not be subject to civil or criminal liability arising from the nature, age, packaging, or condition of an apparently fit pet-related product that the nonprofit organization received as a donation from a person in good faith for ultimate distribution to qualified animals.\n**(3) Liability of State and local governments**\nA State or unit of local government shall not be subject to liability arising from the nature, age, packaging, or condition of an apparently fit pet-related product that the State or unit of local government received as a donation from a person in good faith for ultimate distribution to qualified animals.\n**(4) Waiver not applicable to gross negligence or intentional misconduct**\nParagraphs (1), (2), and (3) shall not apply to an injury to, or death of, an ultimate user or recipient of the apparently fit pet-related product that results from an act or omission of the person, nonprofit organization, or State or unit of local government, as applicable, constituting gross negligence or intentional misconduct.\n##### (b) Partial compliance\nIf a person donates in good faith pet food or pet supplies that do not meet all quality and labeling standards imposed by Federal, State, and local laws and regulations, such person shall not be subject to civil or criminal liability in accordance with this section if the State or unit of local government or nonprofit organization to which the food or supplies are donated\u2014\n**(1)**\nis informed by such person of the distressed or defective condition of the food or supplies;\n**(2)**\nagrees to recondition such food or supplies to comply with such quality and labeling standards prior to distribution of such food or supplies; and\n**(3)**\nis knowledgeable of such quality and labeling standards to properly recondition such food or supplies.\n##### (c) Construction\nNothing in this section shall be construed to\u2014\n**(1)**\ncreate any liability; or\n**(2)**\nsupercede State or local health regulations.\n##### (d) Definitions\nIn this section:\n**(1) Apparently fit pet-related product**\nThe term apparently fit pet-related product means any pet food or pet supply that meets all quality and labeling standards imposed by Federal, State, and local laws and regulations even though the product may not be readily marketable due to appearance, age, freshness, grade, size, surplus, or other conditions.\n**(2) Child Nutrition Act of 1966 terms**\nThe terms donate , gross negligence , intentional misconduct , nonprofit organization , and person have the meanings given such terms in section 22(b) of the Child Nutrition Act of 1966 ( 42 U.S.C. 1791(b) ).\n**(3) Emotional support animal**\nThe term emotional support animal means an animal that\u2014\n**(A)**\nis covered by the exclusion specified in section 5.303 of title 24, Code of Federal Regulations (or successor regulation); and\n**(B)**\nis not a service animal.\n**(4) Pet**\nThe term pet means a domesticated animal, such as a dog, cat, bird, rodent, fish, turtle, or other animal that is kept for pleasure rather than for commercial purposes.\n**(5) Pet food**\nThe term pet food means any raw, cooked, processed, or prepared edible substance, ice, beverage, or ingredient used or intended for use in whole or in part for consumption by a qualified animal.\n**(6) Pet supply**\nThe term pet supply means tangible personal property used for qualified animals, including pet carriers, crates, kennels, houses, cages, clothing, bedding, toys, collars, leashes, leads, tie-outs, feeders, bowls, dishes, pet gates, or pet doors.\n**(7) Qualified animal**\nThe term qualified animal means a pet, an emotional support animal, or a service animal.\n**(8) Service animal**\nThe term service animal has the meaning given the term in section 36.104 of title 28, Code of Federal Regulations (or successor regulation).",
      "versionDate": "2025-06-04",
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
        "actionDate": "2026-05-01",
        "text": "Placed on the Union Calendar, Calendar No. 548."
      },
      "number": "8646",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Agriculture, Rural Development, Food and Drug Administration, and Related Agency Appropriations Act, 2027",
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
        "name": "Agriculture and Food",
        "updateDate": "2025-07-28T14:01:57Z"
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
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr3732ih.xml"
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
      "title": "BARK Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-07-17T11:33:36Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "BARK Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-06-11T06:53:19Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Bring Animals Relief and Kibble Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-06-11T06:53:19Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To provide protections for good faith donations of pet food and supplies.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-06-11T06:48:46Z"
    }
  ]
}
```
