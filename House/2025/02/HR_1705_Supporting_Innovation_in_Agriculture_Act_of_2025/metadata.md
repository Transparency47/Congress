# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/1705?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/1705
- Title: Supporting Innovation in Agriculture Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 1705
- Origin chamber: House
- Introduced date: 2025-02-27
- Update date: 2025-10-04T08:05:48Z
- Update date including text: 2025-10-04T08:05:48Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-02-27: Introduced in House
- 2025-02-27 - IntroReferral: Introduced in House
- 2025-02-27 - IntroReferral: Introduced in House
- 2025-02-27 - IntroReferral: Referred to the House Committee on Ways and Means.
- Latest action: 2025-02-27: Introduced in House

## Actions

- 2025-02-27 - IntroReferral: Introduced in House
- 2025-02-27 - IntroReferral: Introduced in House
- 2025-02-27 - IntroReferral: Referred to the House Committee on Ways and Means.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-02-27",
    "latestAction": {
      "actionDate": "2025-02-27",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/1705",
    "number": "1705",
    "originChamber": "House",
    "policyArea": {
      "name": "Taxation"
    },
    "sponsors": [
      {
        "bioguideId": "K000376",
        "district": "16",
        "firstName": "Mike",
        "fullName": "Rep. Kelly, Mike [R-PA-16]",
        "lastName": "Kelly",
        "party": "R",
        "state": "PA"
      }
    ],
    "title": "Supporting Innovation in Agriculture Act of 2025",
    "type": "HR",
    "updateDate": "2025-10-04T08:05:48Z",
    "updateDateIncludingText": "2025-10-04T08:05:48Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-02-27",
      "committees": {
        "item": {
          "name": "Ways and Means Committee",
          "systemCode": "hswm00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Ways and Means.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-02-27",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-02-27",
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
          "date": "2025-02-27T14:02:35Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Ways and Means Committee",
      "systemCode": "hswm00",
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
      "bioguideId": "T000460",
      "district": "4",
      "firstName": "Mike",
      "fullName": "Rep. Thompson, Mike [D-CA-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Thompson",
      "party": "D",
      "sponsorshipDate": "2025-02-27",
      "state": "CA"
    },
    {
      "bioguideId": "M001222",
      "district": "7",
      "firstName": "Max",
      "fullName": "Rep. Miller, Max L. [R-OH-7]",
      "isOriginalCosponsor": "True",
      "lastName": "Miller",
      "middleName": "L.",
      "party": "R",
      "sponsorshipDate": "2025-02-27",
      "state": "OH"
    },
    {
      "bioguideId": "P000613",
      "district": "19",
      "firstName": "Jimmy",
      "fullName": "Rep. Panetta, Jimmy [D-CA-19]",
      "isOriginalCosponsor": "True",
      "lastName": "Panetta",
      "party": "D",
      "sponsorshipDate": "2025-02-27",
      "state": "CA"
    },
    {
      "bioguideId": "T000478",
      "district": "24",
      "firstName": "Claudia",
      "fullName": "Rep. Tenney, Claudia [R-NY-24]",
      "isOriginalCosponsor": "True",
      "lastName": "Tenney",
      "party": "R",
      "sponsorshipDate": "2025-02-27",
      "state": "NY"
    },
    {
      "bioguideId": "R000622",
      "district": "19",
      "firstName": "Josh",
      "fullName": "Rep. Riley, Josh [D-NY-19]",
      "isOriginalCosponsor": "True",
      "lastName": "Riley",
      "party": "D",
      "sponsorshipDate": "2025-02-27",
      "state": "NY"
    },
    {
      "bioguideId": "L000578",
      "district": "1",
      "firstName": "Doug",
      "fullName": "Rep. LaMalfa, Doug [R-CA-1]",
      "isOriginalCosponsor": "True",
      "lastName": "LaMalfa",
      "party": "R",
      "sponsorshipDate": "2025-02-27",
      "state": "CA"
    },
    {
      "bioguideId": "H001081",
      "district": "5",
      "firstName": "Jahana",
      "fullName": "Rep. Hayes, Jahana [D-CT-5]",
      "isOriginalCosponsor": "True",
      "lastName": "Hayes",
      "party": "D",
      "sponsorshipDate": "2025-02-27",
      "state": "CT"
    },
    {
      "bioguideId": "B001326",
      "district": "5",
      "firstName": "Janelle",
      "fullName": "Rep. Bynum, Janelle [D-OR-5]",
      "isOriginalCosponsor": "True",
      "lastName": "Bynum",
      "middleName": "S.",
      "party": "D",
      "sponsorshipDate": "2025-02-27",
      "state": "OR"
    },
    {
      "bioguideId": "M001224",
      "district": "1",
      "firstName": "Nathaniel",
      "fullName": "Rep. Moran, Nathaniel [R-TX-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Moran",
      "party": "R",
      "sponsorshipDate": "2025-02-27",
      "state": "TX"
    },
    {
      "bioguideId": "V000129",
      "district": "22",
      "firstName": "David",
      "fullName": "Rep. Valadao, David G. [R-CA-22]",
      "isOriginalCosponsor": "True",
      "lastName": "Valadao",
      "middleName": "G.",
      "party": "R",
      "sponsorshipDate": "2025-02-27",
      "state": "CA"
    },
    {
      "bioguideId": "H001090",
      "district": "9",
      "firstName": "Josh",
      "fullName": "Rep. Harder, Josh [D-CA-9]",
      "isOriginalCosponsor": "True",
      "lastName": "Harder",
      "party": "D",
      "sponsorshipDate": "2025-02-27",
      "state": "CA"
    },
    {
      "bioguideId": "E000296",
      "district": "3",
      "firstName": "Dwight",
      "fullName": "Rep. Evans, Dwight [D-PA-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Evans",
      "party": "D",
      "sponsorshipDate": "2025-03-03",
      "state": "PA"
    },
    {
      "bioguideId": "T000487",
      "district": "2",
      "firstName": "Jill",
      "fullName": "Rep. Tokuda, Jill N. [D-HI-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Tokuda",
      "middleName": "N.",
      "party": "D",
      "sponsorshipDate": "2025-03-03",
      "state": "HI"
    },
    {
      "bioguideId": "S001216",
      "district": "8",
      "firstName": "Kim",
      "fullName": "Rep. Schrier, Kim [D-WA-8]",
      "isOriginalCosponsor": "False",
      "lastName": "Schrier",
      "party": "D",
      "sponsorshipDate": "2025-03-03",
      "state": "WA"
    },
    {
      "bioguideId": "S001226",
      "district": "6",
      "firstName": "Andrea",
      "fullName": "Rep. Salinas, Andrea [D-OR-6]",
      "isOriginalCosponsor": "False",
      "lastName": "Salinas",
      "party": "D",
      "sponsorshipDate": "2025-03-04",
      "state": "OR"
    },
    {
      "bioguideId": "C001103",
      "district": "1",
      "firstName": "Earl",
      "fullName": "Rep. Carter, Earl L. \"Buddy\" [R-GA-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Carter",
      "middleName": "L. \"Buddy\"",
      "party": "R",
      "sponsorshipDate": "2025-03-18",
      "state": "GA"
    },
    {
      "bioguideId": "M001237",
      "district": "8",
      "firstName": "Kristen",
      "fullName": "Rep. McDonald Rivet, Kristen [D-MI-8]",
      "isOriginalCosponsor": "False",
      "lastName": "McDonald Rivet",
      "party": "D",
      "sponsorshipDate": "2025-03-18",
      "state": "MI"
    },
    {
      "bioguideId": "M001208",
      "district": "6",
      "firstName": "Lucy",
      "fullName": "Rep. McBath, Lucy [D-GA-6]",
      "isOriginalCosponsor": "False",
      "lastName": "McBath",
      "party": "D",
      "sponsorshipDate": "2025-03-24",
      "state": "GA"
    },
    {
      "bioguideId": "C001126",
      "district": "15",
      "firstName": "Mike",
      "fullName": "Rep. Carey, Mike [R-OH-15]",
      "isOriginalCosponsor": "False",
      "lastName": "Carey",
      "party": "R",
      "sponsorshipDate": "2025-04-07",
      "state": "OH"
    },
    {
      "bioguideId": "V000138",
      "district": "7",
      "firstName": "Eugene",
      "fullName": "Rep. Vindman, Eugene Simon [D-VA-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Vindman",
      "middleName": "Simon",
      "party": "D",
      "sponsorshipDate": "2025-09-09",
      "state": "VA"
    },
    {
      "bioguideId": "V000136",
      "district": "2",
      "firstName": "Gabe",
      "fullName": "Rep. Vasquez, Gabe [D-NM-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Vasquez",
      "party": "D",
      "sponsorshipDate": "2025-10-03",
      "state": "NM"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1705ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 1705\nIN THE HOUSE OF REPRESENTATIVES\nFebruary 27, 2025 Mr. Kelly of Pennsylvania (for himself, Mr. Thompson of California , Mr. Miller of Ohio , Mr. Panetta , Ms. Tenney , Mr. Riley of New York , Mr. LaMalfa , Mrs. Hayes , Ms. Bynum , Mr. Moran , Mr. Valadao , and Mr. Harder of California ) introduced the following bill; which was referred to the Committee on Ways and Means\nA BILL\nTo amend the Internal Revenue Code of 1986 to establish a credit for investments in innovative agricultural technology.\n#### 1. Short title\nThis Act may be cited as the Supporting Innovation in Agriculture Act of 2025 .\n#### 2. Credit for investment in innovative agricultural technology\n##### (a) In general\nSubpart E of part IV of subchapter A of chapter 1 of the Internal Revenue Code of 1986 is amended by inserting after section 48E the following new section:\n48F. Innovative agricultural technology investment credit (a) In general For purposes of section 46, the innovative agricultural technology investment credit for any taxable year is an amount equal to 30 percent of the qualified investment for such taxable year with respect to any innovative agricultural technology project. (b) Qualified investment (1) In general For purposes of subsection (a), the qualified investment with respect to any innovative agricultural technology project for any taxable year is the basis of any qualified property placed in service by the taxpayer during such taxable year which is part of an innovative agricultural technology project. (2) Qualified property For purposes of this section, the term qualified property means property\u2014 (A) which is\u2014 (i) tangible personal property, whether or not affixed to real property (including equipment, systems and their components, materials, machinery, accessories, and structural components), which is used as an integral part of an innovative agricultural technology project, or (ii) software, a computer system, or similar technology, (B) with respect to which depreciation (or amortization in lieu of depreciation) is allowable, and (C) (i) the construction, reconstruction, or erection of which is completed by the taxpayer, or (ii) which is acquired by the taxpayer if the original use of such property commences with the taxpayer. (3) Innovative agricultural technology project The term innovative agricultural technology project means an agricultural technology or system\u2014 (A) which is placed in service before December 31, 2035, and (B) for which the primary purpose is to produce, store, process, and package specialty crops (as defined in section 3 of the Specialty Crops Competitiveness Act of 2004) using\u2014 (i) precision agriculture, or (ii) controlled environment agriculture. (c) Special rules (1) Certain process expenditure rules made Applicable Rules similar to the rules of subsections (c)(4) and (d) of section 46 (as in effect on the day before the date of the enactment of the Revenue Reconciliation Act of 1990) shall apply for purposes of subsection (a). (2) Denial of double benefit under grant programs Rules similar to the rules of section 48(d) shall apply for purposes of this section with respect to\u2014 (A) any renewable energy system, energy efficiency improvement, or equipment or system purchased, made, or installed using a grant provided under section 9007(c) of the Farm Security and Rural Investment Act of 2002 ( 7 U.S.C. 8107(c) ), or (B) any physical improvement to land made using a payment provided under the environmental quality incentives program established under subchapter A of chapter 4 of subtitle D of title XII of the Food Security Act of 1985 ( 16 U.S.C. 3839aa et seq. ). (d) Definitions In this section\u2014 (1) Controlled environment agriculture The term controlled environment agriculture means a closed, indoor agricultural production system using controlled environment agriculture technology in which the environment and inputs can be controlled throughout the lifecycle of a crop. (2) Controlled environment agriculture technology The term controlled environment agriculture technology means any technology (including equipment, systems and their components, materials, and accessories that are necessary for the deployment of such technology) that is required to create, support, and maintain the necessary growing environment for plants and directly contributes to the efficient production, harvesting, processing, or packaging of agricultural products and goods, including\u2014 (A) heating, cooling, thermal screening, humidification, dehumidification, and air circulation systems, (B) horticultural lighting systems and glazing materials, (C) irrigation and water treatment and filtration systems, (D) nutrient delivery and management, (E) sensors and vision systems for gathering data within a commercial controlled environment agricultural facility, (F) software, including data management software, advanced analytics, machine learning systems and artificial intelligence systems, designed as part of or sold in connection with controlled environment agriculture technology, (G) robotics, conveyance, and automation systems, including automated storage and retrieval equipment, (H) automatic harvesting, seeding, transplanting, and sanitation systems, and (I) any other technology, as determined by the Secretary, that contributes to the efficient production, harvesting, processing, or packaging of agricultural products and goods in commercial controlled environment agricultural facilities. (3) Precision agriculture The term precision agriculture means the use of on-farm precision agriculture technology in\u2014 (A) managing, tracking, or reducing crop production inputs, including seed, land, fertilizer, chemicals, water, and time, (B) optimizing weed, pest, and disease identification, (C) managing and tracking crop harvest and on-farm storage at a heightened level of spatial and temporal granularity to improve efficiencies, reduce waste, and maintain environmental quality, and (D) improving on-farm water conservation and irrigation efficiency. (4) Precision agriculture technology The term precision agriculture technology means any technology (including equipment that is necessary for the deployment of such technology) that directly contributes to a reduction in, or improved efficiency of, inputs used in specialty crop production, harvesting, and on-farm storage including\u2014 (A) Global Positioning System-based or geospatial mapping, (B) satellite or aerial imagery, (C) yield monitors, (D) soil mapping, (E) non-chemical weed and pest control technologies, including autonomous laser weeders, (F) vision systems, remote sensors, and temperature and soil moisture monitors, (G) internet of things and telematics technologies, (H) software, including data management, advanced analytics, machine learning, and artificial intelligence systems, designed as part of or sold in connection with other precision agriculture technology, (I) network connectivity products and solutions, (J) Global Positioning System guidance or auto-steer systems, (K) variable rate technology for applying inputs, such as section control, (L) robotics, (M) uncrewed aircraft systems and uncrewed ground vehicles, and (N) any other technology, as determined by the Secretary, that leads to a reduction in, or improves efficiency of, inputs used in crop production and harvesting, which may include seed, fertilizer, chemicals, water, and time. .\n##### (b) Elective payment of credit\nSection 6417 of such Code is amended\u2014\n**(1)**\nin subsection (b), by adding at the end the following:\n(13) The innovative agricultural technology investment credit under section 48F. , and\n**(2)**\nin subsection (d)(1)\u2014\n**(A)**\nin subparagraph (E), by striking (C), or (D) each place such term appears and inserting (C), (D), or (E) ,\n**(B)**\nby redesignating subparagraph (E) (as amended by clause (i)) as subparagraph (F), and\n**(C)**\nby inserting after subparagraph (D) the following:\n(E) Election with respect to innovative agricultural technology investment credit If a taxpayer other than an entity described in subparagraph (A) makes an election under this subparagraph with respect to any taxable year in which such taxpayer has, after December 31, 2023, placed in service qualified property which is part of an innovative agricultural technology project (as defined in section 48F(b)), such taxpayer shall be treated as an applicable entity for purposes of this section for such taxable year, but only with respect to the credit described in subsection (b)(13). .\n##### (c) Transferability\nSection 6418(f)(1)(A) of such Code is amended by adding at the end the following new clause:\n(xii) The innovative agricultural technology investment credit determined under section 48F. .\n##### (d) Conforming amendments\n**(1)**\nSection 46 of such Code is amended\u2014\n**(A)**\nin paragraph (6), by striking and at the end,\n**(B)**\nin paragraph (7), by striking the period at the end and inserting , and , and\n**(C)**\nby adding at the end the following new paragraph:\n(8) the innovative agricultural technology investment credit. .\n**(2)**\nSection 49(a)(1)(C) of such Code is amended\u2014\n**(A)**\nin clause (vii), by striking and at the end,\n**(B)**\nin clause (viii), by striking the period at the end and inserting , and , and\n**(C)**\nby adding at the end the following new clause:\n(ix) the basis of any qualified property which is part of an innovative agricultural technology project under section 48F. .\n**(3)**\nSection 50(a)(2)(E) of such Code is amended by striking or 48E(e) and inserting 48E(e), or 48F(c)(1) .\n**(4)**\nThe table of sections for subpart E of part IV of subchapter A of chapter 1 of such Code is amended by inserting after the item relating to section 48E the following new item:\nSec. 48F. Innovative agricultural technology investment credit. .\n##### (e) Effective date\nThe amendments made by this section shall apply to property the construction of which began after January 1, 2025.",
      "versionDate": "2025-02-27",
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
        "name": "Taxation",
        "updateDate": "2025-05-07T16:09:08Z"
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
      "date": "2025-02-27",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1705ih.xml"
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
      "title": "Supporting Innovation in Agriculture Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-03-19T09:53:22Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Supporting Innovation in Agriculture Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-19T09:53:19Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Internal Revenue Code of 1986 to establish a credit for investments in innovative agricultural technology.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-19T09:48:26Z"
    }
  ]
}
```
