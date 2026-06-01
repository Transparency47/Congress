# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/664?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/664
- Title: American Seabed Protection Act
- Congress: 119
- Bill type: HR
- Bill number: 664
- Origin chamber: House
- Introduced date: 2025-01-23
- Update date: 2026-03-26T08:06:27Z
- Update date including text: 2026-03-26T08:06:27Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-01-23: Introduced in House
- 2025-01-23 - IntroReferral: Introduced in House
- 2025-01-23 - IntroReferral: Introduced in House
- 2025-01-23 - IntroReferral: Referred to the House Committee on Natural Resources.
- 2025-02-04 - IntroReferral: Sponsor introductory remarks on measure. (CR E86-87)
- Latest action: 2025-01-23: Introduced in House

## Actions

- 2025-01-23 - IntroReferral: Introduced in House
- 2025-01-23 - IntroReferral: Introduced in House
- 2025-01-23 - IntroReferral: Referred to the House Committee on Natural Resources.
- 2025-02-04 - IntroReferral: Sponsor introductory remarks on measure. (CR E86-87)

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-01-23",
    "latestAction": {
      "actionDate": "2025-01-23",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/664",
    "number": "664",
    "originChamber": "House",
    "policyArea": {
      "name": "Energy"
    },
    "sponsors": [
      {
        "bioguideId": "C001055",
        "district": "1",
        "firstName": "Ed",
        "fullName": "Rep. Case, Ed [D-HI-1]",
        "lastName": "Case",
        "party": "D",
        "state": "HI"
      }
    ],
    "title": "American Seabed Protection Act",
    "type": "HR",
    "updateDate": "2026-03-26T08:06:27Z",
    "updateDateIncludingText": "2026-03-26T08:06:27Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "B00100",
      "actionDate": "2025-02-04",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Sponsor introductory remarks on measure. (CR E86-87)",
      "type": "IntroReferral"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-01-23",
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
      "actionDate": "2025-01-23",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-01-23",
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
          "date": "2025-01-23T15:10:00Z",
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
      "bioguideId": "B001278",
      "district": "1",
      "firstName": "Suzanne",
      "fullName": "Rep. Bonamici, Suzanne [D-OR-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Bonamici",
      "party": "D",
      "sponsorshipDate": "2025-01-23",
      "state": "OR"
    },
    {
      "bioguideId": "N000147",
      "district": "0",
      "firstName": "Eleanor",
      "fullName": "Del. Norton, Eleanor Holmes [D-DC]",
      "isOriginalCosponsor": "True",
      "lastName": "Norton",
      "middleName": "Holmes",
      "party": "D",
      "sponsorshipDate": "2025-01-23",
      "state": "DC"
    },
    {
      "bioguideId": "T000481",
      "district": "12",
      "firstName": "Rashida",
      "fullName": "Rep. Tlaib, Rashida [D-MI-12]",
      "isOriginalCosponsor": "True",
      "lastName": "Tlaib",
      "party": "D",
      "sponsorshipDate": "2025-01-23",
      "state": "MI"
    },
    {
      "bioguideId": "P000597",
      "district": "1",
      "firstName": "Chellie",
      "fullName": "Rep. Pingree, Chellie [D-ME-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Pingree",
      "party": "D",
      "sponsorshipDate": "2025-02-04",
      "state": "ME"
    },
    {
      "bioguideId": "H001068",
      "district": "2",
      "firstName": "Jared",
      "fullName": "Rep. Huffman, Jared [D-CA-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Huffman",
      "party": "D",
      "sponsorshipDate": "2025-02-04",
      "state": "CA"
    },
    {
      "bioguideId": "Q000023",
      "district": "5",
      "firstName": "Mike",
      "fullName": "Rep. Quigley, Mike [D-IL-5]",
      "isOriginalCosponsor": "False",
      "lastName": "Quigley",
      "party": "D",
      "sponsorshipDate": "2025-11-17",
      "state": "IL"
    },
    {
      "bioguideId": "M001219",
      "district": "0",
      "firstName": "James",
      "fullName": "Del. Moylan, James C. [R-GU-At Large]",
      "isOriginalCosponsor": "False",
      "lastName": "Moylan",
      "middleName": "C.",
      "party": "R",
      "sponsorshipDate": "2026-03-25",
      "state": "GU"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr664ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 664\nIN THE HOUSE OF REPRESENTATIVES\nJanuary 23, 2025 Mr. Case (for himself, Ms. Bonamici , Ms. Norton , and Ms. Tlaib ) introduced the following bill; which was referred to the Committee on Natural Resources\nA BILL\nTo prohibit certain mining activities on the deep seabed and Outer Continental Shelf, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the American Seabed Protection Act .\n#### 2. Prohibition of certain mining activities on deep seabed and Outer Continental Shelf\n##### (a) Findings\nCongress finds the following:\n**(1)**\nAs determined by the United Nations, most recently in its Sustainable Development Goals report, our world\u2019s oceans are at great risk from a number of factors, including atmospheric change, resource extraction, and pollution.\n**(2)**\nThe United Nation\u2019s 2030 Agenda for Sustainable Development, launched by the 2015 UN Summit in New York established Sustainable Development Goal 14 (SDS 14), to conserve and sustainably use the oceans, seas, and marine resources. Target 2 of SDS 14 commits States to sustainably manage marine ecosystems to avoid significant adverse impacts and strengthen their resilience.\n**(3)**\nThe international marine scientific and policy consensus is that deep seabed mining presents a major risk to the marine environment, including\u2014\n**(A)**\nthe direct loss of unique and ecologically important species;\n**(B)**\nlarge sediment plumes that will negatively affect ecosystems well beyond the actual mining sites;\n**(C)**\nnoise pollution that will cause physiological and behavioral stress to marine species;\n**(D)**\nlikely contamination of commercially important species of food fish; and\n**(E)**\nlikely negative impacts on carbon sequestration dynamics and deep-ocean carbon storage.\n**(4)**\nThe United Nations Convention on Biological Diversity, 15th Conference of Parties, Decision 15/24 encourages member States to ensure that, before deep seabed mineral exploitation is permitted, the related impacts on the marine environment and biodiversity are sufficiently researched, the risks to the marine ecosystem are sufficiently understood, and sufficient regulation and conditions are imposed to ensure that exploitation does not cause harmful effects to the marine environment and biodiversity.\n**(5)**\nThe 2022 United Nations Environment Programme Financial Initiative report on deep seabed mining states that the financing of such activities is not consistent with Sustainable Blue Economy Finance Principles.\n**(6)**\nThere is currently insufficient scientific information on the deep sea and related marine ecosystems to fully and accurately assess the risks and impacts of deep seabed mining activities.\n##### (b) Prohibition of certain mining activities on deep seabed and Outer Continental Shelf\n**(1) Deep seabed**\nNotwithstanding any provision of the Deep Seabed Hard Mineral Resources Act ( 30 U.S.C. 1401 et seq. ), no license, permit, or other authorization may be issued for exploration or commercial recovery.\n**(2) Outer Continental Shelf**\nNotwithstanding any provision of the Outer Continental Shelf Lands Act ( 43 U.S.C. 1301 et seq. ), no license, permit, or other authorization may be issued for exploration, development, or production of a hardrock mineral on the Outer Continental Shelf.\n**(3) Exception for scientific research**\nParagraphs (1) and (2) shall not apply to the issuance of a license, permit, or other authorization to carry out scientific research activities.\n##### (c) Assessment of environmental impacts of mining activities on deep seabed and Outer Continental Shelf\n**(1) In general**\nNot later than 90 days after the date of the enactment of this section, the Secretary shall seek to enter into an agreement with the National Academies of Science, Engineering, and Medicine to conduct a comprehensive study of the environmental impacts of mining activities on the deep seabed and Outer Continental Shelf.\n**(2) Submission of assessment**\nThe Secretary shall submit to the appropriate Congressional committees a report regarding the findings of the study described in paragraph (1).\n**(3) Contents**\nThe study described in paragraph (1) shall include the following:\n**(A)**\nA characterization of ecosystems\u2014\n**(i)**\non the deep seabed and Outer Continental Shelf;\n**(ii)**\nin the overlying water columns of the deep seabed and Outer Continental Shelf; and\n**(iii)**\non seamounts and hydrothermal vents.\n**(B)**\nAn assessment of the potential impacts associated with mining activities on the deep seabed and Outer Continental Shelf on\u2014\n**(i)**\nhabitats and species on the deep seabed and Outer Continental Shelf and in the overlying water columns of the deep seabed and Outer Continental Shelf, including\u2014\n**(I)**\nan approximate quantification of the spatial extent and timescale of such impacts; and\n**(II)**\nthe potential for the recovery of such habitats and species from such impacts;\n**(ii)**\nthe capacity of deep sea and open ocean processes and ecosystems to sequester greenhouse gases;\n**(iii)**\nusers of the marine environment, including\u2014\n**(I)**\ncommercial and recreational fisheries;\n**(II)**\nrecreational users;\n**(III)**\naquaculture operations; and\n**(IV)**\ndevelopers of subsea infrastructure; and\n**(iv)**\nindigenous peoples and cultures linked to marine species and the marine environment.\n**(C)**\nAn assessment of the potential impacts of sediment plumes from disturbance of the deep seabed and Outer Continental Shelf and collector vessel discharge on pelagic species and food webs.\n**(D)**\nAn approximate quantification of the greenhouse gas emissions associated with mining activities on the deep seabed and Outer Continental Shelf, including such emissions that may result from the alteration of the biology, geology, or chemistry of the sediment on or the overlying water column of the deep seabed and Outer Continental Shelf.\n**(E)**\nAn assessment of the viability of alternatives to the use of minerals found on the deep seabed and Outer Continental Shelf, including\u2014\n**(i)**\ndeveloping a greater capacity for and promoting the reuse and recycling of such minerals in circulation;\n**(ii)**\ndeveloping and promoting the use of substitute minerals and materials that have fewer or less severe environmental impacts associated with such use; and\n**(iii)**\ndeveloping methods to reduce the environmental impacts of terrestrial mining practices and other similar initiatives.\n##### (d) Definitions\nIn this section:\n**(1) Appropriate Congressional committees**\nThe term appropriate Congressional committees means\u2014\n**(A)**\nwith respect to the House of Representatives\u2014\n**(i)**\nthe Committee on Foreign Affairs; and\n**(ii)**\nthe Committee on Natural Resources; and\n**(B)**\nwith respect to the Senate\u2014\n**(i)**\nthe Committee on Commerce, Science, and Transportation;\n**(ii)**\nthe Committee on Energy and Natural Resources; and\n**(iii)**\nthe Committee on Foreign Relations.\n**(2) Commercial recovery**\nThe term commercial recovery has the meaning given the term in section 4 of the Deep Seabed Hard Mineral Resources Act ( 30 U.S.C. 1403 ).\n**(3) Deep seabed**\nThe term deep seabed has the meaning given the term in section 4 of the Deep Seabed Hard Mineral Resources Act ( 30 U.S.C. 1403 ).\n**(4) Development**\nThe term development has the meaning given the term in section 2 of the Outer Continental Shelf Lands Act ( 43 U.S.C. 1331 ).\n**(5) Exploration**\nThe term exploration \u2014\n**(A)**\nwhen used with respect to the deep seabed, has the meaning given the term in section 4 of the Deep Seabed Hard Mineral Resources Act ( 30 U.S.C. 1403 ); and\n**(B)**\nwhen used with respect to the Outer Continental Shelf, has the meaning given the term in section 2 of the Outer Continental Shelf Lands Act ( 43 U.S.C. 1331 ).\n**(6) Outer Continental Shelf**\nThe term Outer Continental Shelf has the meaning given the term outer Continental Shelf in section 2 of the Outer Continental Shelf Lands Act ( 43 U.S.C. 1331 ).\n**(7) Production**\nThe term production has the meaning given the term in section 2 of the Outer Continental Shelf Lands Act ( 43 U.S.C. 1331 ).\n**(8) Secretary**\nThe term Secretary means the Secretary of Commerce, acting through the Administrator of the National Oceanic and Atmospheric Administration.",
      "versionDate": "2025-01-23",
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
        "name": "Energy",
        "updateDate": "2025-02-24T17:15:33Z"
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
      "date": "2025-01-23",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr664ih.xml"
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
      "title": "American Seabed Protection Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-02-22T06:23:53Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "American Seabed Protection Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-02-22T06:23:33Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To prohibit certain mining activities on the deep seabed and Outer Continental Shelf, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-02-22T06:19:01Z"
    }
  ]
}
```
