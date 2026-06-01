# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/6268?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/6268
- Title: LEAD Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 6268
- Origin chamber: House
- Introduced date: 2025-11-21
- Update date: 2026-02-05T09:06:12Z
- Update date including text: 2026-02-05T09:06:12Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-11-21: Introduced in House
- 2025-11-21 - IntroReferral: Introduced in House
- 2025-11-21 - IntroReferral: Introduced in House
- 2025-11-21 - IntroReferral: Referred to the House Committee on Natural Resources.
- Latest action: 2025-11-21: Introduced in House

## Actions

- 2025-11-21 - IntroReferral: Introduced in House
- 2025-11-21 - IntroReferral: Introduced in House
- 2025-11-21 - IntroReferral: Referred to the House Committee on Natural Resources.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-11-21",
    "latestAction": {
      "actionDate": "2025-11-21",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/6268",
    "number": "6268",
    "originChamber": "House",
    "policyArea": {
      "name": "Public Lands and Natural Resources"
    },
    "sponsors": [
      {
        "bioguideId": "L000582",
        "district": "36",
        "firstName": "Ted",
        "fullName": "Rep. Lieu, Ted [D-CA-36]",
        "lastName": "Lieu",
        "party": "D",
        "state": "CA"
      }
    ],
    "title": "LEAD Act of 2025",
    "type": "HR",
    "updateDate": "2026-02-05T09:06:12Z",
    "updateDateIncludingText": "2026-02-05T09:06:12Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-11-21",
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
      "text": "Referred to the House Committee on Natural Resources.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-11-21",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-11-21",
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
          "date": "2025-11-21T14:04:25Z",
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
      "bioguideId": "B001300",
      "district": "44",
      "firstName": "Nanette",
      "fullName": "Rep. Barrag\u00e1n, Nanette Diaz [D-CA-44]",
      "isOriginalCosponsor": "True",
      "lastName": "Barrag\u00e1n",
      "middleName": "Diaz",
      "party": "D",
      "sponsorshipDate": "2025-11-21",
      "state": "CA"
    },
    {
      "bioguideId": "B001285",
      "district": "26",
      "firstName": "Julia",
      "fullName": "Rep. Brownley, Julia [D-CA-26]",
      "isOriginalCosponsor": "True",
      "lastName": "Brownley",
      "party": "D",
      "sponsorshipDate": "2025-11-21",
      "state": "CA"
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
      "sponsorshipDate": "2025-11-21",
      "state": "DC"
    },
    {
      "bioguideId": "D000631",
      "district": "4",
      "firstName": "Madeleine",
      "fullName": "Rep. Dean, Madeleine [D-PA-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Dean",
      "party": "D",
      "sponsorshipDate": "2025-11-21",
      "state": "PA"
    },
    {
      "bioguideId": "N000002",
      "district": "12",
      "firstName": "Jerrold",
      "fullName": "Rep. Nadler, Jerrold [D-NY-12]",
      "isOriginalCosponsor": "True",
      "lastName": "Nadler",
      "party": "D",
      "sponsorshipDate": "2025-11-21",
      "state": "NY"
    },
    {
      "bioguideId": "M001143",
      "district": "4",
      "firstName": "Betty",
      "fullName": "Rep. McCollum, Betty [D-MN-4]",
      "isOriginalCosponsor": "True",
      "lastName": "McCollum",
      "party": "D",
      "sponsorshipDate": "2025-11-21",
      "state": "MN"
    },
    {
      "bioguideId": "M001241",
      "district": "47",
      "firstName": "Dave",
      "fullName": "Rep. Min, Dave [D-CA-47]",
      "isOriginalCosponsor": "True",
      "lastName": "Min",
      "party": "D",
      "sponsorshipDate": "2025-11-21",
      "state": "CA"
    },
    {
      "bioguideId": "R000620",
      "district": "29",
      "firstName": "Luz",
      "fullName": "Rep. Rivas, Luz M. [D-CA-29]",
      "isOriginalCosponsor": "False",
      "lastName": "Rivas",
      "middleName": "M.",
      "party": "D",
      "sponsorshipDate": "2025-12-10",
      "state": "CA"
    },
    {
      "bioguideId": "K000391",
      "district": "8",
      "firstName": "Raja",
      "fullName": "Rep. Krishnamoorthi, Raja [D-IL-8]",
      "isOriginalCosponsor": "False",
      "lastName": "Krishnamoorthi",
      "party": "D",
      "sponsorshipDate": "2025-12-16",
      "state": "IL"
    },
    {
      "bioguideId": "L000397",
      "district": "18",
      "firstName": "Zoe",
      "fullName": "Rep. Lofgren, Zoe [D-CA-18]",
      "isOriginalCosponsor": "False",
      "lastName": "Lofgren",
      "party": "D",
      "sponsorshipDate": "2026-01-21",
      "state": "CA"
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
      "sponsorshipDate": "2026-02-02",
      "state": "TX"
    },
    {
      "bioguideId": "T000468",
      "district": "1",
      "firstName": "Dina",
      "fullName": "Rep. Titus, Dina [D-NV-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Titus",
      "party": "D",
      "sponsorshipDate": "2026-02-04",
      "state": "NV"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6268ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 6268\nIN THE HOUSE OF REPRESENTATIVES\nNovember 21, 2025 Mr. Lieu (for himself, Ms. Barrag\u00e1n , Ms. Brownley , Ms. Norton , Ms. Dean of Pennsylvania , Mr. Nadler , Ms. McCollum , and Mr. Min ) introduced the following bill; which was referred to the Committee on Natural Resources\nA BILL\nTo require the Secretary of the Interior to prohibit the use of lead ammunition on United States Fish and Wildlife Service lands, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Lead Endangers Animals Daily Act of 2025 or the LEAD Act of 2025 .\n#### 2. Findings\nCongress finds the following:\n**(1)**\nIn 1991, the United States Fish and Wildlife Service required the use of nontoxic ammunition for all waterfowl hunting.\n**(2)**\nResearch has shown that the presence of lead in the environment poses a threat to human and wildlife health.\n**(3)**\nThe Environmental Protection Agency has determined that lead is toxic to both humans and animals, and can negatively affect nearly every organ and system in the human body, including the heart, bones, intestines, kidneys, and reproductive and nervous systems. Lead exposure interferes with the development of the nervous system and is therefore particularly toxic to children, causing potentially permanent learning and behavioral disorders.\n**(4)**\nLead is a potent neurotoxin, for which no safe exposure level exists for humans. The use of lead has been outlawed in and removed from paint, gasoline, children\u2019s toys, and many other items to protect human health and wildlife.\n**(5)**\nWildlife, including federally listed threatened and endangered species, is at risk of lead toxicosis through the ingestion of lead ammunition, either directly by ingesting lead from spent ballistic materials while foraging, or indirectly by scavenging carcasses and viscera left by hunters. Lead may also pollute soil and water around outdoor shooting ranges.\n**(6)**\nLead ammunition also endangers human food supplies. Dairy and beef cattle have developed lead poisoning after feeding in areas where spent lead ammunition has accumulated. Spent lead ammunition can also contaminate crops, vegetation, and waterways.\n**(7)**\nHumans are at risk of lead toxicosis through the consumption of game meat harvested with lead ammunition.\n**(8)**\nAlternatives to lead ammunition are readily available, and studies have shown that nonlead ammunition performs just as well as lead-based ammunition.\n**(9)**\nIn January 2017, the outgoing Director of the United States Fish and Wildlife Service issued Director\u2019s Order 219. In March 2017, the Principal Deputy Director of the United States Fish and Wildlife Service repealed this Order.\n#### 3. Nontoxic ammunition\n##### (a) In general\nExcept as provided in subsection (c), and not later than 1 year after enactment, the Secretary, acting through the Director, shall issue final regulations prohibiting the discharge of any firearm using ammunition other than nonlead ammunition certified under subsection (b) on all lands and waters under the jurisdiction and control of the United States Fish and Wildlife Service.\n##### (b) Certification\nThe Director shall, for the purposes of enforcing this section and in consultation with State and Tribal governments, establish and annually update a list of nonlead ammunition.\n##### (c) Exceptions\nThe prohibition under subsection (a) shall not apply to\u2014\n**(1)**\na Government official or agent carrying out a statutory duty unrelated to the management of wildlife;\n**(2)**\na State, local, Tribal, or Federal law enforcement officer or the agent of such officer when carrying out a statutory duty; and\n**(3)**\nan active member of the United States military when carrying out official duties.\n##### (d) Penalties\nA person that knowingly violates subsection (a) may be assessed a civil penalty by the Secretary of no more than $500 for the first violation. A second or subsequent violation shall be punishable by a fine of not less than $1,000 or more than $5,000.\n##### (e) Definitions\nIn this section:\n**(1) Ammunition**\nThe term ammunition means any bullet, ball, sabot, slug, buckshot, shot, pellet, or other projectile that is expelled from a firearm through a barrel by force.\n**(2) Director**\nThe term Director means the Director of the United States Fish and Wildlife Service.\n**(3) Explosive**\nThe term explosive has the meaning given such term in section 844 of title 18, United States Code.\n**(4) Firearm**\nThe term firearm means any weapon which expels ammunition by the action of an explosive or compressed air.\n**(5) Nonlead ammunition**\nThe term nonlead ammunition means ammunition in which there is no lead content, excluding the presence of trace amounts of lead.\n**(6) Secretary**\nThe term Secretary means the Secretary of the Interior.\n**(7) Trace amounts**\nThe term trace amounts means one percent or less by weight of the total weight of the ammunition.",
      "versionDate": "2025-11-21",
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
        "name": "Public Lands and Natural Resources",
        "updateDate": "2025-12-18T19:52:38Z"
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
      "date": "2025-11-21",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6268ih.xml"
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
      "title": "LEAD Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-12-17T07:38:27Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "LEAD Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-12-17T07:38:25Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Lead Endangers Animals Daily Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-12-17T07:38:25Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To require the Secretary of the Interior to prohibit the use of lead ammunition on United States Fish and Wildlife Service lands, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-12-17T07:33:36Z"
    }
  ]
}
```
