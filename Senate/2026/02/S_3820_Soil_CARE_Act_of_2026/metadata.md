# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/3820?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/3820
- Title: Soil CARE Act of 2026
- Congress: 119
- Bill type: S
- Bill number: 3820
- Origin chamber: Senate
- Introduced date: 2026-02-10
- Update date: 2026-05-11T16:52:36Z
- Update date including text: 2026-05-11T16:52:36Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2026-02-10: Introduced in Senate
- 2026-02-10 - IntroReferral: Introduced in Senate
- 2026-02-10 - IntroReferral: Read twice and referred to the Committee on Agriculture, Nutrition, and Forestry.
- Latest action: 2026-02-10: Introduced in Senate

## Actions

- 2026-02-10 - IntroReferral: Introduced in Senate
- 2026-02-10 - IntroReferral: Read twice and referred to the Committee on Agriculture, Nutrition, and Forestry.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-02-10",
    "latestAction": {
      "actionDate": "2026-02-10",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/3820",
    "number": "3820",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Agriculture and Food"
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
    "title": "Soil CARE Act of 2026",
    "type": "S",
    "updateDate": "2026-05-11T16:52:36Z",
    "updateDateIncludingText": "2026-05-11T16:52:36Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-02-10",
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
      "actionDate": "2026-02-10",
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
        "item": {
          "date": "2026-02-10T20:34:26Z",
          "name": "Referred To"
        }
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
      "bioguideId": "W000779",
      "firstName": "Ron",
      "fullName": "Sen. Wyden, Ron [D-OR]",
      "isOriginalCosponsor": "True",
      "lastName": "Wyden",
      "party": "D",
      "sponsorshipDate": "2026-02-10",
      "state": "OR"
    },
    {
      "bioguideId": "W000800",
      "firstName": "Peter",
      "fullName": "Sen. Welch, Peter [D-VT]",
      "isOriginalCosponsor": "True",
      "lastName": "Welch",
      "party": "D",
      "sponsorshipDate": "2026-02-10",
      "state": "VT"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s3820is.xml",
      "text": "II\n119th CONGRESS\n2d Session\nS. 3820\nIN THE SENATE OF THE UNITED STATES\nFebruary 10, 2026 Mr. Merkley (for himself, Mr. Wyden , and Mr. Welch ) introduced the following bill; which was read twice and referred to the Committee on Agriculture, Nutrition, and Forestry\nA BILL\nTo require the Secretary of Agriculture to establish and maintain a training program for Natural Resources Conservation Service personnel and third-party providers on the rapidly evolving methodologies, science, and practices of soil health management systems on agricultural land, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Soil Conservation And Regeneration Education Act of 2026 or the Soil CARE Act of 2026 .\n#### 2. Training for soil health in NRCS programs for agricultural producers\nSection 1242 of the Food Security Act of 1985 ( 16 U.S.C. 3842 ) is amended\u2014\n**(1)**\nin subsection (d), by inserting of Agriculture after Department ; and\n**(2)**\nby adding at the end the following:\n(j) Training for soil health management (1) Definitions In this subsection: (A) Service The term Service means the Natural Resources Conservation Service. (B) Soil biology The term soil biology includes the collective biomass and activities of soil-dwelling organisms from an array of trophic levels. (C) Soil health management The term soil health management means land management methods that are employed to increase and balance soil health, such as microbial biomass and macrofauna, for the purpose of improving biological functions, including forming and stabilizing soil structure, cycling nutrients, controlling pests and disease, and degrading or detoxifying contaminants. (D) Training program The term training program means the training program established under paragraph (2). (2) Establishment of training program Not later than 1 year after the date of enactment of this subsection, the Secretary shall establish a training program\u2014 (A) to provide education, resources, and technical support to Service personnel and third-party providers on the rapidly evolving methodologies, science, and practices for improving soil health; and (B) to assist Service personnel and third-party providers in supporting agricultural producers in understanding and implementing soil health management systems that regenerate farmland. (3) Program development and delivery (A) In general The training program shall\u2014 (i) be made available in each Service region twice every 2 years; and (ii) include\u2014 (I) a nationally available online curriculum on soil health management systems that is\u2014 (aa) developed through cooperative agreements with entities described in subparagraph (B); and (bb) delivered by the Service; and (II) in-person training workshops on soil health management systems that regenerate farmland, that\u2014 (aa) include coverage across regions and geography types; (bb) are developed through cooperative agreements with entities described in subparagraph (B); and (cc) are delivered by the Service. (B) Cooperative agreements (i) In general The training program shall be developed and delivered through cooperative agreements with entities with soil health management systems expertise and experience working with and training producers, including\u2014 (I) farming consultants, including producers and producer cooperatives; (II) nonprofit organizations serving organic, agroecological, and other regenerative producers; (III) conservation districts; (IV) land-grant colleges and universities (as defined in section 1404 of the National Agricultural Research, Extension, and Teaching Policy Act of 1977 ( 7 U.S.C. 3103 )); (V) Long-Term Agroecosystem Research sites; and (VI) other entities with adequate expertise in soil health management systems, as determined by the Secretary. (ii) Initial agreements Not later than 1 year after the date of enactment of this subsection, the Secretary shall enter into cooperative agreements under clause (i) for the initial development and delivery of the training program. (C) Participation (i) In general The Secretary shall encourage relevant Service personnel and third-party providers\u2014 (I) to complete the online curriculum described in subparagraph (A)(ii)(I); and (II) to the extent practicable, to attend at least 1 in-person training workshop described in subparagraph (A)(ii)(II). (ii) Relevant Service personnel For purposes of clause (i), relevant Service personnel shall include, at a minimum, Service personnel involved in conservation planning activities with, and the delivery of technical assistance to, producers, including field office staff of the Service. (iii) Completion schedules for third-party providers (I) Establishment of schedules The Secretary shall establish\u2014 (aa) a schedule for the completion by third-party providers of the online curriculum described in subparagraph (A)(ii)(I); and (bb) a schedule of in-person training workshops that will be provided in accordance with subparagraph (A)(ii)(II). (II) Use of schedules The Secretary shall encourage each third-party provider\u2014 (aa) to complete the online curriculum in accordance with the schedule established under subclause (I)(aa); and (bb) to the extent practicable, to attend at least 1 training workshop identified on the schedule established under subclause (I)(bb). (D) Continuing education The Secretary shall provide continuing education for relevant Service personnel and third-party providers, with a focus on the use of new conservation practice standards related to soil health. (E) Materials for producers The Secretary shall require relevant Service personnel and third-party providers to provide soil health education materials to producers through the programs and conservation activities of the Service, including materials relating to the topics covered by the curriculum described in paragraph (4). (4) Curriculum (A) In general The training program shall include the following minimum curriculum components: (i) A unit on the principles of soil health published by the Service, with a focus on biological function and regional context. (ii) A unit on\u2014 (I) the transition to agriculture management systems that build soil health, including operations, infrastructure, regulations, finance, and marketing needs; and (II) associated risks and opportunities, including reducing input costs by building on-farm and ranch fertility. (iii) A unit on organic production and soil health management. (iv) A unit on diversified production systems, including\u2014 (I) perennial cropping systems; (II) agroforestry or silvopasture systems; (III) livestock integration into cropping systems; and (IV) prescribed grazing. (v) A unit on the body of research on soil biology and agriculture that regenerates farmland, including potential impacts on soil health, water quality and security, biodiversity, ecosystem function, resilience to extreme weather, carbon sequestration, and agricultural profitability. (vi) A unit on key conservation practices that maximize soil health and mitigate climate impacts by implementing soil health principles. (vii) A unit on\u2014 (I) issues specific to Indian Tribes; and (II) traditional ecological knowledge. (viii) A unit on\u2014 (I) the special needs of new, small scale, and underserved producers; and (II) how best to meet those needs. (ix) A unit on approaches, tools, and skills to support farmers in performing soil health tests. (x) A unit on all conservation programs available to producers that improve soil health, reduce production inputs, and regenerate soil, farmland, and nearby ecosystems. (B) Updates The Secretary shall review and update the curriculum and all materials of the training program every 2 years based on the latest\u2014 (i) soil health management innovations; and (ii) scientific and technological advancements. (5) Authorization of appropriations There is authorized to be appropriated to the Secretary to carry out this subsection $10,000,000 for the period of fiscal years 2027 through 2032. .",
      "versionDate": "2026-02-10",
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
        "actionDate": "2026-02-10",
        "text": "Referred to the House Committee on Agriculture."
      },
      "number": "7474",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Soil CARE Act of 2026",
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
        "updateDate": "2026-02-27T16:29:39Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2026-02-10",
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
          "measure-id": "id119s3820",
          "measure-number": "3820",
          "measure-type": "s",
          "orig-publish-date": "2026-02-10",
          "originChamber": "SENATE",
          "update-date": "2026-05-11"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "SENATE",
            "summary-id": "id119s3820v00",
            "update-date": "2026-05-11"
          },
          "action-date": "2026-02-10",
          "action-desc": "Introduced in Senate",
          "summary-text": "<p><strong>Soil Conservation And Regeneration Education Act of 2026 or the Soil CARE Act of 2026</strong></p><p>This bill directs the Department of Agriculture (USDA) to establish a training program for soil health management in Natural Resources Conservation Service (NRCS) programs.</p><p>Under the bill,<em> soil health management</em> means land management methods used to increase and balance soil health, such as microbial biomass and macrofauna, for the purpose of improving biological functions, including forming and stabilizing soil structure, cycling nutrients, controlling pests and disease, and degrading or detoxifying contaminants.</p><p>The training program must (1) provide education, resources, and technical support to NRCS personnel and third-party providers on the rapidly evolving methodologies, science, and practices for improving soil health; and (2) assist NRCS personnel and third-party providers in supporting agricultural producers in understanding and implementing soil health management systems that regenerate farmland.</p><p>The training program must be available twice every two years in each NRCS region and include both an online curriculum and in-person training workshops.</p><p>The training program must be developed and delivered through cooperative agreements with entities with soil health management systems expertise and experience working with and training producers.</p><p>The bill includes minimum curriculum requirements for the training program, including specific units on soil health and diversified production systems.</p><p>USDA must review and update the training program curriculum and materials every two years.</p>"
        },
        "title": "Soil CARE Act of 2026"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/s/BILLSUM-119s3820.xml",
    "summary": {
      "actionDate": "2026-02-10",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Soil Conservation And Regeneration Education Act of 2026 or the Soil CARE Act of 2026</strong></p><p>This bill directs the Department of Agriculture (USDA) to establish a training program for soil health management in Natural Resources Conservation Service (NRCS) programs.</p><p>Under the bill,<em> soil health management</em> means land management methods used to increase and balance soil health, such as microbial biomass and macrofauna, for the purpose of improving biological functions, including forming and stabilizing soil structure, cycling nutrients, controlling pests and disease, and degrading or detoxifying contaminants.</p><p>The training program must (1) provide education, resources, and technical support to NRCS personnel and third-party providers on the rapidly evolving methodologies, science, and practices for improving soil health; and (2) assist NRCS personnel and third-party providers in supporting agricultural producers in understanding and implementing soil health management systems that regenerate farmland.</p><p>The training program must be available twice every two years in each NRCS region and include both an online curriculum and in-person training workshops.</p><p>The training program must be developed and delivered through cooperative agreements with entities with soil health management systems expertise and experience working with and training producers.</p><p>The bill includes minimum curriculum requirements for the training program, including specific units on soil health and diversified production systems.</p><p>USDA must review and update the training program curriculum and materials every two years.</p>",
      "updateDate": "2026-05-11",
      "versionCode": "id119s3820"
    },
    "title": "Soil CARE Act of 2026"
  },
  "summaries": [
    {
      "actionDate": "2026-02-10",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Soil Conservation And Regeneration Education Act of 2026 or the Soil CARE Act of 2026</strong></p><p>This bill directs the Department of Agriculture (USDA) to establish a training program for soil health management in Natural Resources Conservation Service (NRCS) programs.</p><p>Under the bill,<em> soil health management</em> means land management methods used to increase and balance soil health, such as microbial biomass and macrofauna, for the purpose of improving biological functions, including forming and stabilizing soil structure, cycling nutrients, controlling pests and disease, and degrading or detoxifying contaminants.</p><p>The training program must (1) provide education, resources, and technical support to NRCS personnel and third-party providers on the rapidly evolving methodologies, science, and practices for improving soil health; and (2) assist NRCS personnel and third-party providers in supporting agricultural producers in understanding and implementing soil health management systems that regenerate farmland.</p><p>The training program must be available twice every two years in each NRCS region and include both an online curriculum and in-person training workshops.</p><p>The training program must be developed and delivered through cooperative agreements with entities with soil health management systems expertise and experience working with and training producers.</p><p>The bill includes minimum curriculum requirements for the training program, including specific units on soil health and diversified production systems.</p><p>USDA must review and update the training program curriculum and materials every two years.</p>",
      "updateDate": "2026-05-11",
      "versionCode": "id119s3820"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2026-02-10",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s3820is.xml"
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
      "title": "Soil CARE Act of 2026",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-02-25T04:53:19Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Soil CARE Act of 2026",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-02-25T04:53:19Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Soil Conservation And Regeneration Education Act of 2026",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-02-25T04:53:19Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to require the Secretary of Agriculture to establish and maintain a training program for Natural Resources Conservation Service personnel and third-party providers on the rapidly evolving methodologies, science, and practices of soil health management systems on agricultural land, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-02-25T04:48:24Z"
    }
  ]
}
```
