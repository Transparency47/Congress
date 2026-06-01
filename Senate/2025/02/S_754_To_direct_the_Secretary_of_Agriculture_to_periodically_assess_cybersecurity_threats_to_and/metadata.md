# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/754?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/754
- Title: Farm and Food Cybersecurity Act of 2025
- Congress: 119
- Bill type: S
- Bill number: 754
- Origin chamber: Senate
- Introduced date: 2025-02-26
- Update date: 2026-04-23T11:03:25Z
- Update date including text: 2026-04-23T11:03:25Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-02-26: Introduced in Senate
- 2025-02-26 - IntroReferral: Introduced in Senate
- 2025-02-26 - IntroReferral: Read twice and referred to the Committee on Agriculture, Nutrition, and Forestry.
- Latest action: 2025-02-26: Introduced in Senate

## Actions

- 2025-02-26 - IntroReferral: Introduced in Senate
- 2025-02-26 - IntroReferral: Read twice and referred to the Committee on Agriculture, Nutrition, and Forestry.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-02-26",
    "latestAction": {
      "actionDate": "2025-02-26",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/754",
    "number": "754",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Agriculture and Food"
    },
    "sponsors": [
      {
        "bioguideId": "C001095",
        "district": "",
        "firstName": "Tom",
        "fullName": "Sen. Cotton, Tom [R-AR]",
        "lastName": "Cotton",
        "party": "R",
        "state": "AR"
      }
    ],
    "title": "Farm and Food Cybersecurity Act of 2025",
    "type": "S",
    "updateDate": "2026-04-23T11:03:25Z",
    "updateDateIncludingText": "2026-04-23T11:03:25Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-02-26",
      "committees": {
        "item": {
          "name": "Agriculture, Nutrition, and Forestry Committee",
          "systemCode": "ssaf00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Agriculture, Nutrition, and Forestry.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-02-26",
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
            "date": "2025-02-26T20:26:58Z",
            "name": "Referred To"
          },
          {
            "date": "2025-02-26T20:26:58Z",
            "name": "Referred To"
          }
        ]
      },
      "chamber": "Senate",
      "name": "Agriculture, Nutrition, and Forestry Committee",
      "systemCode": "ssaf00",
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
      "bioguideId": "S001208",
      "firstName": "Elissa",
      "fullName": "Sen. Slotkin, Elissa [D-MI]",
      "isOriginalCosponsor": "True",
      "lastName": "Slotkin",
      "party": "D",
      "sponsorshipDate": "2025-02-26",
      "state": "MI"
    },
    {
      "bioguideId": "R000618",
      "firstName": "Pete",
      "fullName": "Sen. Ricketts, Pete [R-NE]",
      "isOriginalCosponsor": "True",
      "lastName": "Ricketts",
      "party": "R",
      "sponsorshipDate": "2025-02-26",
      "state": "NE"
    },
    {
      "bioguideId": "T000476",
      "firstName": "Thomas",
      "fullName": "Sen. Tillis, Thomas [R-NC]",
      "isOriginalCosponsor": "True",
      "lastName": "Tillis",
      "middleName": "Roland",
      "party": "R",
      "sponsorshipDate": "2025-02-26",
      "state": "NC"
    },
    {
      "bioguideId": "L000571",
      "firstName": "Cynthia",
      "fullName": "Sen. Lummis, Cynthia M. [R-WY]",
      "isOriginalCosponsor": "True",
      "lastName": "Lummis",
      "middleName": "M.",
      "party": "R",
      "sponsorshipDate": "2025-02-26",
      "state": "WY"
    },
    {
      "bioguideId": "B001305",
      "firstName": "Ted",
      "fullName": "Sen. Budd, Ted [R-NC]",
      "isOriginalCosponsor": "True",
      "lastName": "Budd",
      "party": "R",
      "sponsorshipDate": "2025-02-26",
      "state": "NC"
    },
    {
      "bioguideId": "B001319",
      "firstName": "Katie",
      "fullName": "Sen. Britt, Katie Boyd [R-AL]",
      "isOriginalCosponsor": "True",
      "lastName": "Britt",
      "party": "R",
      "sponsorshipDate": "2025-02-26",
      "state": "AL"
    },
    {
      "bioguideId": "O000174",
      "firstName": "Jon",
      "fullName": "Sen. Ossoff, Jon [D-GA]",
      "isOriginalCosponsor": "False",
      "lastName": "Ossoff",
      "party": "D",
      "sponsorshipDate": "2025-09-08",
      "state": "GA"
    },
    {
      "bioguideId": "B001261",
      "firstName": "John",
      "fullName": "Sen. Barrasso, John [R-WY]",
      "isOriginalCosponsor": "False",
      "lastName": "Barrasso",
      "party": "R",
      "sponsorshipDate": "2026-03-11",
      "state": "WY"
    },
    {
      "bioguideId": "M001243",
      "firstName": "David",
      "fullName": "Sen. McCormick, David [R-PA]",
      "isOriginalCosponsor": "False",
      "lastName": "McCormick",
      "middleName": "H.",
      "party": "R",
      "sponsorshipDate": "2026-04-22",
      "state": "PA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s754is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 754\nIN THE SENATE OF THE UNITED STATES\nFebruary 26, 2025 Mr. Cotton (for himself, Ms. Slotkin , Mr. Ricketts , Mr. Tillis , Ms. Lummis , Mr. Budd , and Mrs. Britt ) introduced the following bill; which was read twice and referred to the Committee on Agriculture, Nutrition, and Forestry\nA BILL\nTo direct the Secretary of Agriculture to periodically assess cybersecurity threats to, and vulnerabilities in, the agriculture and food critical infrastructure sector and to provide recommendations to enhance their security and resilience, to require the Secretary of Agriculture to conduct an annual cross-sector simulation exercise relating to a food-related emergency or disruption, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Farm and Food Cybersecurity Act of 2025 .\n#### 2. Definitions\nIn this Act:\n**(1) Agriculture and food critical infrastructure sector**\nThe term agriculture and food critical infrastructure sector means\u2014\n**(A)**\nany activity relating to the production, processing, distribution, storage, transportation, consumption, or disposal of agricultural or food products; and\n**(B)**\nany entity involved in an activity described in subparagraph (A), including a farmer, rancher, processor, manufacturer, distributor, retailer, consumer, and regulator.\n**(2) Cybersecurity threat; defensive measure; incident; security vulnerability**\nThe terms cybersecurity threat , defensive measure , incident , and security vulnerability have the meanings given those terms in section 2200 of the Homeland Security Act of 2002 ( 6 U.S.C. 650 ).\n**(3) Secretary**\nThe term Secretary means the Secretary of Agriculture.\n**(4) Sector-specific ISAC**\nThe term sector-specific ISAC means the Food and Agriculture-Information Sharing and Analysis Center.\n#### 3. Assessment of cybersecurity threats and security vulnerabilities in the agriculture and food critical infrastructure sector\n##### (a) Risk assessment\nThe Secretary, in coordination with the Cybersecurity and Infrastructure Security Agency, shall conduct a risk assessment, on a biennial basis, on the cybersecurity threats to, and security vulnerabilities in, the agriculture and food critical infrastructure sector, including\u2014\n**(1)**\nthe nature and extent of cyberattacks and incidents that affect the agriculture and food critical infrastructure sector;\n**(2)**\nthe potential impacts of a cyberattack or incident on the safety, security, and availability of food products, as well as on the economy, public health, and national security of the United States;\n**(3)**\nthe current capability and readiness of the Federal Government, State and local governments, and private sector entities to prevent, detect, mitigate, respond to, and recover from cyberattacks and incidents described in paragraph (2);\n**(4)**\nthe existing policies, standards, guidelines, best practices, and initiatives applicable to the agriculture and food critical infrastructure sector to enhance defensive measures in that sector;\n**(5)**\nthe gaps, challenges, barriers, or opportunities for improving defensive measures in the agriculture and food critical infrastructure sector; and\n**(6)**\nany recommendations for Federal legislative or administrative actions to address the cybersecurity threats to, and security vulnerabilities in, the agriculture and food critical infrastructure sector, including intrusive, duplicative, or conflicting regulatory requirements that may divert attention and resources from operational risk management to a compliance regime that impedes security efforts.\n##### (b) Private sector participation\nIn conducting a risk assessment under subsection (a), the Secretary shall consult with appropriate entities in the private sector, including\u2014\n**(1)**\nthe sector-specific ISAC; and\n**(2)**\nthe appropriate sector coordinating council.\n##### (c) Biennial report\nNot later than 1 year after the date of enactment of this Act, and every 2 years thereafter, the Secretary shall submit a report on each risk assessment conducted under subsection (a) to\u2014\n**(1)**\nthe Committee on Agriculture, Nutrition, and Forestry of the Senate;\n**(2)**\nthe Committee on Homeland Security and Governmental Affairs of the Senate;\n**(3)**\nthe Committee on Agriculture of the House of Representatives; and\n**(4)**\nthe Committee on Homeland Security of the House of Representatives.\n#### 4. Food security and cyber resilience simulation exercise\n##### (a) Establishment\nThe Secretary, in coordination with the Secretary of Homeland Security, the Secretary of Health and Human Services, the Director of National Intelligence, and the heads of other relevant Federal agencies, shall conduct, over a 5-year period, an annual cross-sector crisis simulation exercise relating to a food-related emergency or disruption (referred to in this section as an exercise ).\n##### (b) Purposes\nThe purposes of each exercise are\u2014\n**(1)**\nto assess the preparedness and response capabilities of Federal, State, Tribal, local, and territorial governments and private sector entities in the event of a food-related emergency or disruption;\n**(2)**\nto identify and address gaps and vulnerabilities in the food supply chain and critical infrastructure;\n**(3)**\nto enhance coordination and information sharing among stakeholders involved in food production, processing, distribution, and consumption;\n**(4)**\nto evaluate the effectiveness and efficiency of existing policies, programs, and resources relating to food security and resilience;\n**(5)**\nto develop and disseminate best practices and recommendations for improving food security and resilience; and\n**(6)**\nto identify key stakeholders and categories that were missing from the exercise to ensure the inclusion of those stakeholders and categories in future exercises.\n##### (c) Design\nEach exercise shall\u2014\n**(1)**\ninvolve a realistic and plausible scenario that simulates a food-related emergency or disruption affecting multiple sectors and jurisdictions;\n**(2)**\nincorporate input from experts and stakeholders from various disciplines and sectors, including agriculture, public health, nutrition, emergency management, transportation, energy, water, communications, related equipment suppliers and manufacturers, and cybersecurity, including related academia and private sector information security researchers and practitioners, including the sector-specific ISAC;\n**(3)**\nuse a variety of methods and tools, such as tabletop exercises, workshops, seminars, games, drills, or full-scale exercises; and\n**(4)**\ninclude participants from Federal, State, Tribal, local, and territorial governments and private sector entities, including the sector-specific ISAC and appropriate sector coordinating councils, that have roles and responsibilities relating to food security and resilience.\n##### (d) Private sector participation\nIn conducting an exercise, the Secretary shall consult with appropriate entities in the private sector, including\u2014\n**(1)**\nthe sector-specific ISAC; and\n**(2)**\nthe appropriate sector coordinating councils.\n##### (e) Feedback; report\nAfter each exercise, the Secretary, in consultation with the heads of the Federal agencies described in subsection (a), shall\u2014\n**(1)**\nprovide feedback to, and an evaluation of, the participants in that exercise on their performance and outcomes; and\n**(2)**\nproduce, and submit to Congress, a report that summarizes, with respect to that exercise, the findings of that exercise, lessons learned from that exercise, and recommendations to enhance the cybersecurity and resilience of the agriculture and food critical infrastructure sector.\n##### (f) Authorization of appropriations\nThere is authorized to be appropriated to carry out this section $1,000,000 for each of fiscal years 2026 through 2030.",
      "versionDate": "2025-02-26",
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
        "actionDate": "2025-03-28",
        "text": "Referred to the Subcommittee on Nutrition and Foreign Agriculture."
      },
      "number": "1604",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Farm and Food Cybersecurity Act of 2025",
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
        "updateDate": "2025-05-07T12:46:17Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-02-26",
    "originChamber": "Senate",
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
          "measure-id": "id119s754",
          "measure-number": "754",
          "measure-type": "s",
          "orig-publish-date": "2025-02-26",
          "originChamber": "SENATE",
          "update-date": "2025-06-09"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "SENATE",
            "summary-id": "id119s754v00",
            "update-date": "2025-06-09"
          },
          "action-date": "2025-02-26",
          "action-desc": "Introduced in Senate",
          "summary-text": "<p><strong>Farm and Food Cybersecurity Act of 2025</strong></p><p>This bill directs the Department of Agriculture (USDA) to (1) assess\u00a0cybersecurity threats in the agriculture and food\u00a0critical infrastructure\u00a0sector, and (2) conduct annual crisis simulation exercises for food-related emergencies or disruptions. The agriculture and food\u00a0critical infrastructure\u00a0sector\u00a0includes (1) any activity relating to the production, processing,\u00a0distribution, storage, transportation, consumption, or disposal of agricultural or food products; and (2) any entity involved in any of these activities.</p><p>Specifically, USDA, in coordination with the Department of Homeland Security (DHS)\u00a0Cybersecurity and Infrastructure Security Agency, must conduct a risk assessment every two years on the\u00a0cybersecurity threats to, and security vulnerabilities in, this sector. The risk assessment must include any recommendations for federal legislative or administrative actions to address related threats and vulnerabilities.</p><p>USDA must also conduct an annual simulation exercise relating to a food-related emergency or disruption in coordination with\u00a0DHS, the Department of Health and Human Services (HHS), and the Office of the Director of National Intelligence (ODNI).</p><p>Among other things, the exercise must (1) involve a realistic and plausible scenario that simulates a food-related emergency or disruption that affects multiple sectors and jurisdictions, and (2) incorporate input from experts and stakeholders from various disciplines and sectors (e.g., agriculture, public health, emergency management, transportation, and energy).\u00a0</p><p>USDA, in consultation with DHS, HHS, and ODNI, must submit a report to Congress on each simulation exercise, including recommendations to enhance the\u00a0cybersecurity and resilience of the agriculture and food critical infrastructure sector.</p>"
        },
        "title": "Farm and Food Cybersecurity Act of 2025"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/s/BILLSUM-119s754.xml",
    "summary": {
      "actionDate": "2025-02-26",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Farm and Food Cybersecurity Act of 2025</strong></p><p>This bill directs the Department of Agriculture (USDA) to (1) assess\u00a0cybersecurity threats in the agriculture and food\u00a0critical infrastructure\u00a0sector, and (2) conduct annual crisis simulation exercises for food-related emergencies or disruptions. The agriculture and food\u00a0critical infrastructure\u00a0sector\u00a0includes (1) any activity relating to the production, processing,\u00a0distribution, storage, transportation, consumption, or disposal of agricultural or food products; and (2) any entity involved in any of these activities.</p><p>Specifically, USDA, in coordination with the Department of Homeland Security (DHS)\u00a0Cybersecurity and Infrastructure Security Agency, must conduct a risk assessment every two years on the\u00a0cybersecurity threats to, and security vulnerabilities in, this sector. The risk assessment must include any recommendations for federal legislative or administrative actions to address related threats and vulnerabilities.</p><p>USDA must also conduct an annual simulation exercise relating to a food-related emergency or disruption in coordination with\u00a0DHS, the Department of Health and Human Services (HHS), and the Office of the Director of National Intelligence (ODNI).</p><p>Among other things, the exercise must (1) involve a realistic and plausible scenario that simulates a food-related emergency or disruption that affects multiple sectors and jurisdictions, and (2) incorporate input from experts and stakeholders from various disciplines and sectors (e.g., agriculture, public health, emergency management, transportation, and energy).\u00a0</p><p>USDA, in consultation with DHS, HHS, and ODNI, must submit a report to Congress on each simulation exercise, including recommendations to enhance the\u00a0cybersecurity and resilience of the agriculture and food critical infrastructure sector.</p>",
      "updateDate": "2025-06-09",
      "versionCode": "id119s754"
    },
    "title": "Farm and Food Cybersecurity Act of 2025"
  },
  "summaries": [
    {
      "actionDate": "2025-02-26",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Farm and Food Cybersecurity Act of 2025</strong></p><p>This bill directs the Department of Agriculture (USDA) to (1) assess\u00a0cybersecurity threats in the agriculture and food\u00a0critical infrastructure\u00a0sector, and (2) conduct annual crisis simulation exercises for food-related emergencies or disruptions. The agriculture and food\u00a0critical infrastructure\u00a0sector\u00a0includes (1) any activity relating to the production, processing,\u00a0distribution, storage, transportation, consumption, or disposal of agricultural or food products; and (2) any entity involved in any of these activities.</p><p>Specifically, USDA, in coordination with the Department of Homeland Security (DHS)\u00a0Cybersecurity and Infrastructure Security Agency, must conduct a risk assessment every two years on the\u00a0cybersecurity threats to, and security vulnerabilities in, this sector. The risk assessment must include any recommendations for federal legislative or administrative actions to address related threats and vulnerabilities.</p><p>USDA must also conduct an annual simulation exercise relating to a food-related emergency or disruption in coordination with\u00a0DHS, the Department of Health and Human Services (HHS), and the Office of the Director of National Intelligence (ODNI).</p><p>Among other things, the exercise must (1) involve a realistic and plausible scenario that simulates a food-related emergency or disruption that affects multiple sectors and jurisdictions, and (2) incorporate input from experts and stakeholders from various disciplines and sectors (e.g., agriculture, public health, emergency management, transportation, and energy).\u00a0</p><p>USDA, in consultation with DHS, HHS, and ODNI, must submit a report to Congress on each simulation exercise, including recommendations to enhance the\u00a0cybersecurity and resilience of the agriculture and food critical infrastructure sector.</p>",
      "updateDate": "2025-06-09",
      "versionCode": "id119s754"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-02-26",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s754is.xml"
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
      "title": "Farm and Food Cybersecurity Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-04-23T11:03:25Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Farm and Food Cybersecurity Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-21T04:08:23Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to direct the Secretary of Agriculture to periodically assess cybersecurity threats to, and vulnerabilities in, the agriculture and food critical infrastructure sector and to provide recommendations to enhance their security and resilience, to require the Secretary of Agriculture to conduct an annual cross-sector simulation exercise relating to a food-related emergency or disruption, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-21T04:03:45Z"
    }
  ]
}
```
