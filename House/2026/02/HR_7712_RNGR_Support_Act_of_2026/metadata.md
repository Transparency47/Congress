# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/7712?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/7712
- Title: RNGR Support Act of 2026
- Congress: 119
- Bill type: HR
- Bill number: 7712
- Origin chamber: House
- Introduced date: 2026-02-25
- Update date: 2026-03-27T21:26:16Z
- Update date including text: 2026-03-27T21:26:16Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2026-02-25: Introduced in House
- 2026-02-25 - IntroReferral: Introduced in House
- 2026-02-25 - IntroReferral: Introduced in House
- 2026-02-25 - IntroReferral: Referred to the House Committee on Agriculture.
- Latest action: 2026-02-25: Introduced in House

## Actions

- 2026-02-25 - IntroReferral: Introduced in House
- 2026-02-25 - IntroReferral: Introduced in House
- 2026-02-25 - IntroReferral: Referred to the House Committee on Agriculture.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-02-25",
    "latestAction": {
      "actionDate": "2026-02-25",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/7712",
    "number": "7712",
    "originChamber": "House",
    "policyArea": {
      "name": "Agriculture and Food"
    },
    "sponsors": [
      {
        "bioguideId": "S001216",
        "district": "8",
        "firstName": "Kim",
        "fullName": "Rep. Schrier, Kim [D-WA-8]",
        "lastName": "Schrier",
        "party": "D",
        "state": "WA"
      }
    ],
    "title": "RNGR Support Act of 2026",
    "type": "HR",
    "updateDate": "2026-03-27T21:26:16Z",
    "updateDateIncludingText": "2026-03-27T21:26:16Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2026-02-25",
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
      "actionDate": "2026-02-25",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-02-25",
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
          "date": "2026-02-25T14:02:10Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Agriculture Committee",
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
      "bioguideId": "B001301",
      "district": "1",
      "firstName": "Jack",
      "fullName": "Rep. Bergman, Jack [R-MI-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Bergman",
      "party": "R",
      "sponsorshipDate": "2026-02-25",
      "state": "MI"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7712ih.xml",
      "text": "I\n119th CONGRESS\n2d Session\nH. R. 7712\nIN THE HOUSE OF REPRESENTATIVES\nFebruary 25, 2026 Ms. Schrier (for herself and Mr. Bergman ) introduced the following bill; which was referred to the Committee on Agriculture\nA BILL\nTo direct the Secretary of Agriculture to collaborate with various entities, and to establish a grant program, as a means of supporting nurseries and seed orchards, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Reforestation, Nurseries, and Genetic Resources Support Act of 2026 or the RNGR Support Act of 2026 .\n#### 2. Nursery and seed orchard support\n##### (a) Partnerships, collaboration, and other assistance in support of nurseries and seed orchards\nThe Secretary of Agriculture, acting through the Chief of the Forest Service, shall\u2014\n**(1)**\npartner with Federal and State agencies, Indian Tribes, institutions of higher education, nonprofit organizations, and private nurseries to provide training, technical assistance, and research to nursery and tree establishment programs that support natural regeneration, reforestation, agroforestry, and afforestation;\n**(2)**\npromote information sharing to improve technical knowledge and practices, and to better understand reforestation needs, relating to seeds or seedlings, effects of climate change, tree genetics for resistance to pathogens and drought, and other issues necessary to address all facets of the reforestation supply chain;\n**(3)**\nprovide technical and financial assistance to international nursery and tree establishment programs through the Forest Service International Programs, the Institute of Pacific Islands Forestry, and the International Institute of Tropical Forestry;\n**(4)**\ncollaborate with other relevant Federal departments and agencies, including the Foreign Agricultural Service of the Department of Agriculture, the United States Agency for International Development, the United States Fish and Wildlife Service, and international organizations, including the Food and Agriculture Organization of the United Nations, to provide technical and financial assistance related to nurseries and reforestation;\n**(5)**\ncoordinate the efforts of the Department of Agriculture\u2014\n**(A)**\nto address the challenges associated with the reforestation supply chain, including workforce development; and\n**(B)**\nto leverage economic development assistance for work with private nurseries;\n**(6)**\nexpand reforestation supply chains through science and research, seed collection and storage, workforce development, and nursery infrastructure and operations; and\n**(7)**\nshorten the timeline for approval of permits to collect seeds on National Forest System lands.\n##### (b) Nursery and seed orchard grant program\n**(1) Establishment**\nNot later than 2 years after the date of enactment of this Act, the Secretary shall establish a program to provide grants to eligible recipients to support nurseries and seed orchards.\n**(2) Allowable uses**\nA recipient of grant funds under paragraph (1) may use such funds to carry out a project comprised of 1 or more of the following:\n**(A)**\nThe development, expansion, enhancement, or improvement of nursery production capacity or other infrastructure\u2014\n**(i)**\nto improve seed collection and storage;\n**(ii)**\nto increase seedling production, storage, and distribution; or\n**(iii)**\nto enhance seedling survival and properly manage tree genetic resources.\n**(B)**\nThe establishment or expansion of a nursery or seed orchard, including by acquiring equipment for a nursery or seed orchard.\n**(C)**\nThe development or implementation of quality control measures at nurseries or seed orchards.\n**(D)**\nThe promotion of workforce development within any facet of the reforestation supply chain.\n**(E)**\nAny other activity determined appropriate by the Secretary.\n##### (c) Reforestation Trust Fund\nNotwithstanding subsection (d) of section 303 of Public Law 96\u2013451 ( 16 U.S.C. 1606a ), of amounts in the Reforestation Trust Fund established by subsection (a) of that section that are not otherwise obligated, the Secretary may obligate not more than $5,000,000 for each fiscal year to carry out this section.\n##### (d) Definitions\nIn this section:\n**(1) Eligible recipient**\nThe term eligible recipient means\u2014\n**(A)**\na State forestry agency;\n**(B)**\nan Indian Tribe; and\n**(C)**\na private nursery that has experience growing high-quality native trees of appropriate genetic sources in bareroot or container stocktypes specific for reforestation, restoration, or conservation, including native plants and seeds that are of cultural significance to Indian Tribes.\n**(2) National Forest System**\nThe term National Forest System has the meaning given the term in section 11(a) of the Forest and Rangeland Renewable Resources Planning Act of 1974 ( 16 U.S.C. 1609(a) ).\n**(3) Nursery**\nThe term nursery means a tree or native plant nursery.\n**(4) Seed orchard**\nThe term seed orchard means a tree or native plant seed orchard.\n**(5) State**\nThe term State means each of the several States, the District of Columbia, the Commonwealth of Puerto Rico, and any territory or possession of the United States.",
      "versionDate": "2026-02-25",
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
        "name": "Agriculture and Food",
        "updateDate": "2026-03-27T21:26:16Z"
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
      "date": "2026-02-25",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7712ih.xml"
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
      "title": "RNGR Support Act of 2026",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-03-20T09:53:28Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "RNGR Support Act of 2026",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-03-20T09:53:27Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Reforestation, Nurseries, and Genetic Resources Support Act of 2026",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-03-20T09:53:27Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To direct the Secretary of Agriculture to collaborate with various entities, and to establish a grant program, as a means of supporting nurseries and seed orchards, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-03-20T09:48:21Z"
    }
  ]
}
```
