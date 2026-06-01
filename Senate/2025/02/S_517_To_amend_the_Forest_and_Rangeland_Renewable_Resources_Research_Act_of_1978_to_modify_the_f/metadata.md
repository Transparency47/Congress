# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/517?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/517
- Title: Forest Data Modernization Act of 2025
- Congress: 119
- Bill type: S
- Bill number: 517
- Origin chamber: Senate
- Introduced date: 2025-02-11
- Update date: 2026-02-19T22:11:02Z
- Update date including text: 2026-02-19T22:11:02Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-02-11: Introduced in Senate
- 2025-02-11 - IntroReferral: Introduced in Senate
- 2025-02-11 - IntroReferral: Read twice and referred to the Committee on Agriculture, Nutrition, and Forestry.
- Latest action: 2025-02-11: Introduced in Senate

## Actions

- 2025-02-11 - IntroReferral: Introduced in Senate
- 2025-02-11 - IntroReferral: Read twice and referred to the Committee on Agriculture, Nutrition, and Forestry.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-02-11",
    "latestAction": {
      "actionDate": "2025-02-11",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/517",
    "number": "517",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Public Lands and Natural Resources"
    },
    "sponsors": [
      {
        "bioguideId": "O000174",
        "district": "",
        "firstName": "Jon",
        "fullName": "Sen. Ossoff, Jon [D-GA]",
        "lastName": "Ossoff",
        "party": "D",
        "state": "GA"
      }
    ],
    "title": "Forest Data Modernization Act of 2025",
    "type": "S",
    "updateDate": "2026-02-19T22:11:02Z",
    "updateDateIncludingText": "2026-02-19T22:11:02Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-02-11",
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
      "actionDate": "2025-02-11",
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
          "date": "2025-02-11T20:27:17Z",
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
      "bioguideId": "C001075",
      "firstName": "Bill",
      "fullName": "Sen. Cassidy, Bill [R-LA]",
      "isOriginalCosponsor": "True",
      "lastName": "Cassidy",
      "party": "R",
      "sponsorshipDate": "2025-02-11",
      "state": "LA"
    },
    {
      "bioguideId": "W000790",
      "firstName": "Raphael",
      "fullName": "Sen. Warnock, Raphael G. [D-GA]",
      "isOriginalCosponsor": "False",
      "lastName": "Warnock",
      "party": "D",
      "sponsorshipDate": "2025-02-25",
      "state": "GA"
    },
    {
      "bioguideId": "H001079",
      "firstName": "Cindy",
      "fullName": "Sen. Hyde-Smith, Cindy [R-MS]",
      "isOriginalCosponsor": "False",
      "lastName": "Hyde-Smith",
      "party": "R",
      "sponsorshipDate": "2025-02-25",
      "state": "MS"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s517is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 517\nIN THE SENATE OF THE UNITED STATES\nFebruary 11, 2025 Mr. Ossoff (for himself and Mr. Cassidy ) introduced the following bill; which was read twice and referred to the Committee on Agriculture, Nutrition, and Forestry\nA BILL\nTo amend the Forest and Rangeland Renewable Resources Research Act of 1978 to modify the forest inventory and analysis program.\n#### 1. Short title\nThis Act may be cited as the Forest Data Modernization Act of 2025 .\n#### 2. Forest inventory and analysis\n##### (a) In general\nSection 3(e) of the Forest and Rangeland Renewable Resources Research Act of 1978 ( 16 U.S.C. 1642(e) ) is amended\u2014\n**(1)**\nin paragraph (1)\u2014\n**(A)**\nby striking their resources and inserting the resources of those forests, including forest carbon, ;\n**(B)**\nby striking In compliance and inserting the following:\n(A) In general In compliance ; and\n**(C)**\nby adding at the end the following:\n(B) Additional methods Under the program under this subsection, the Secretary shall carry out, as a data collection method\u2014 (i) a timber products output study; and (ii) a national woodland owner survey. ;\n**(2)**\nin paragraph (3)(C), by inserting including with respect to available forest carbon data, after 2 decades, ;\n**(3)**\nin paragraph (4)\u2014\n**(A)**\nin the second sentence, by striking The standards and inserting the following:\n(B) Inclusions The standards described in subparagraph (A) ;\n**(B)**\nby striking (4) National standards and definitions .\u2014To ensure and inserting the following:\n(4) National consistency (A) Standards and definitions To ensure ; and\n**(C)**\nby adding at the end the following:\n(C) Terminology The Secretary shall include a clear description of the definition of forest used for purposes of reporting data from inventories and analyses of forests and the resources of forests under this subsection with\u2014 (i) any data or report provided under the program under this subsection; (ii) Renewable Resource Assessments prepared under section 3(a) of the Forest and Rangeland Renewable Resources Planning Act of 1974 ( 16 U.S.C. 1601(a) ); and (iii) any data or report provided to an entity outside the United States. ;\n**(4)**\nin paragraph (6)\u2014\n**(A)**\nin the matter preceding subparagraph (A), by striking Not later than 180 days after the date of enactment of this subsection, and inserting In accordance with paragraph (7), ; and\n**(B)**\nby striking subparagraphs (D) and (E) and inserting the following:\n(D) the organization and procedures necessary to understand and report on changes in land cover and use; (E) the organization and procedures necessary to evaluate carbon-related data variables, including soil carbon, collected from forest inventory and analysis plots, timber products output studies, and national woodland owner surveys to ensure that carbon accounting information needs can be met; and ; and\n**(5)**\nby adding at the end the following:\n(7) Updates to strategic plan (A) In general Not later than 180 days after the date of enactment of this paragraph, the Secretary shall prepare an update to the strategic plan under paragraph (6) to include\u2014 (i) a plan to implement nationally consistent data collection protocols and procedures to improve the statistical precision of base program estimates; (ii) pathways to integrate and report on changes in forest carbon, including below-ground carbon; (iii) plans, including the identification of challenges, to collaborate with other Federal agencies, non-Federal partners, and the private sector to integrate existing nationally available data sets and best available commercial technologies, such as remote sensing, spatial analysis techniques, and other new technologies; (iv) a plan to increase transparency and clarity in reporting in accordance with paragraph (4)(C); (v) a plan to expand current data collection, further integrate remote sensing technology, or both, to include procedures to improve the statistical precision of estimates at the sub-State level; (vi) a plan to expand current data collection, further integrate remote sensing technology, or both, to include information on renewable biomass supplies and carbon stocks at the local, State, regional, and national levels, including by ownership type; and (vii) such other matters as the Secretary determines to be appropriate based on recommendations of the Forest Inventory and Analysis National User Group. (B) Submission Not later than 180 days after the date of enactment of this paragraph, the Secretary shall submit to the Committee on Agriculture, Nutrition, and Forestry of the Senate and the Committee on Agriculture of the House of Representatives the update to the strategic plan prepared under subparagraph (A). (C) Further updates Not later than 5 years after the date on which the update is submitted under subparagraph (B), and every 5 years thereafter, the Secretary shall\u2014 (i) prepare an additional update to the strategic plan; and (ii) submit the additional update to the committees described in subparagraph (B). (8) Accessibility The Secretary shall ensure that data collected under this subsection is\u2014 (A) easily accessible to all public- and private-sector entities; and (B) collected using means that ensure the confidentiality, in accordance with section 1770 of the Food Security Act of 1985 ( 7 U.S.C. 2276 ), of\u2014 (i) plot locations; (ii) nonaggregated data of woodland owners; and (iii) forest industry information. (9) Biennial compilations Biennially, the Secretary shall prepare and make publicly available a compilation of national forest inventory and analysis forest statistics, which shall be similar to the tables contained in the Renewable Resource Assessments prepared under section 3(a) of the Forest and Rangeland Renewable Resources Planning Act of 1974 ( 16 U.S.C. 1601(a) ). (10) External complex data requests (A) In general The Secretary shall establish an office, a data platform, or both to process and respond to complex data requests submitted by external organizations relating to the program under this subsection. (B) Fees To cover the costs of processing of and responding to complex data requests described in subparagraph (A), the Secretary may impose fees on the external organizations submitting the requests. (11) Reports Each year, the Secretary shall publish as part of the forest inventory and analysis business report a detailed description of the progress of the Secretary in implementing the programmatic elements of the strategic plan described in paragraph (6), including\u2014 (A) the costs and priorities of the strategic plan; and (B) how the program under this subsection leverages new technology, improves and standardizes collection protocols, and increases workforce capacity. .\n##### (b) Remote sensing technologies\nSection 8632(1) of the Agriculture Improvement Act of 2018 ( 16 U.S.C. 1642 note; Public Law 115\u2013334 ) is amended by striking technologies and inserting technologies, such as microwave, LiDAR, hyperspectral, and high-resolution remote sensing data for data collection, and machine learning for improved modeling, .",
      "versionDate": "2025-02-11",
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
        "actionDate": "2026-02-13",
        "text": "Referred to the House Committee on Agriculture."
      },
      "number": "7567",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Farm, Food, and National Security Act of 2026",
      "type": "HR"
    },
    {
      "congress": "119",
      "latestAction": {
        "actionDate": "2025-02-11",
        "text": "Referred to the House Committee on Agriculture."
      },
      "number": "1213",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Forest Data Modernization Act of 2025",
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
        "updateDate": "2025-05-12T14:49:26Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-02-11",
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
          "measure-id": "id119s517",
          "measure-number": "517",
          "measure-type": "s",
          "orig-publish-date": "2025-02-11",
          "originChamber": "SENATE",
          "update-date": "2026-02-19"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "SENATE",
            "summary-id": "id119s517v00",
            "update-date": "2026-02-19"
          },
          "action-date": "2025-02-11",
          "action-desc": "Introduced in Senate",
          "summary-text": "<p><strong>Forest Data Modernization Act of 2025</strong></p><p>This bill directs the Forest Service to expand and update its Forest Inventory and Analysis (FIA) program. Under the existing program, the Forest Service collects, analyzes, and reports on information about the condition of forest resources in the United States, such as data concerning wildfires or other forest management issues.</p><p>The bill directs FIA to include forest carbon in its inventory.\u00a0</p><p>The bill also requires FIA's strategic plan to\u00a0include a detailed description of the organization and procedures necessary to (1) understand and report on changes in land cover and use, and (2) evaluate carbon-related data variables.</p><p>FIA must\u00a0update the strategic plan within six months and every five years thereafter. Among other items, the first update must include (1) a plan to implement nationally consistent data collection protocols and procedures; and (2) a plan to expand current data collection, further integrate remote sensing technology, or both.\u00a0</p><p>FIA must also prepare and publish a\u00a0compilation of certain forest statistics every two years.</p><p>Additionally, the bill requires FIA to continue (1) the Timber Products Output\u00a0survey, and (2) the National Woodland Owner Survey.</p><p>To provide data consistency,\u00a0FIA must include a clear definition of <em>forest</em> when reporting data.</p><p>Finally, FIA (1) must also establish an office, a data platform, or both to process and respond to complex data requests submitted by external organizations; and (2) may impose fees on the organizations submitting the requests.</p>"
        },
        "title": "Forest Data Modernization Act of 2025"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/s/BILLSUM-119s517.xml",
    "summary": {
      "actionDate": "2025-02-11",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Forest Data Modernization Act of 2025</strong></p><p>This bill directs the Forest Service to expand and update its Forest Inventory and Analysis (FIA) program. Under the existing program, the Forest Service collects, analyzes, and reports on information about the condition of forest resources in the United States, such as data concerning wildfires or other forest management issues.</p><p>The bill directs FIA to include forest carbon in its inventory.\u00a0</p><p>The bill also requires FIA's strategic plan to\u00a0include a detailed description of the organization and procedures necessary to (1) understand and report on changes in land cover and use, and (2) evaluate carbon-related data variables.</p><p>FIA must\u00a0update the strategic plan within six months and every five years thereafter. Among other items, the first update must include (1) a plan to implement nationally consistent data collection protocols and procedures; and (2) a plan to expand current data collection, further integrate remote sensing technology, or both.\u00a0</p><p>FIA must also prepare and publish a\u00a0compilation of certain forest statistics every two years.</p><p>Additionally, the bill requires FIA to continue (1) the Timber Products Output\u00a0survey, and (2) the National Woodland Owner Survey.</p><p>To provide data consistency,\u00a0FIA must include a clear definition of <em>forest</em> when reporting data.</p><p>Finally, FIA (1) must also establish an office, a data platform, or both to process and respond to complex data requests submitted by external organizations; and (2) may impose fees on the organizations submitting the requests.</p>",
      "updateDate": "2026-02-19",
      "versionCode": "id119s517"
    },
    "title": "Forest Data Modernization Act of 2025"
  },
  "summaries": [
    {
      "actionDate": "2025-02-11",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Forest Data Modernization Act of 2025</strong></p><p>This bill directs the Forest Service to expand and update its Forest Inventory and Analysis (FIA) program. Under the existing program, the Forest Service collects, analyzes, and reports on information about the condition of forest resources in the United States, such as data concerning wildfires or other forest management issues.</p><p>The bill directs FIA to include forest carbon in its inventory.\u00a0</p><p>The bill also requires FIA's strategic plan to\u00a0include a detailed description of the organization and procedures necessary to (1) understand and report on changes in land cover and use, and (2) evaluate carbon-related data variables.</p><p>FIA must\u00a0update the strategic plan within six months and every five years thereafter. Among other items, the first update must include (1) a plan to implement nationally consistent data collection protocols and procedures; and (2) a plan to expand current data collection, further integrate remote sensing technology, or both.\u00a0</p><p>FIA must also prepare and publish a\u00a0compilation of certain forest statistics every two years.</p><p>Additionally, the bill requires FIA to continue (1) the Timber Products Output\u00a0survey, and (2) the National Woodland Owner Survey.</p><p>To provide data consistency,\u00a0FIA must include a clear definition of <em>forest</em> when reporting data.</p><p>Finally, FIA (1) must also establish an office, a data platform, or both to process and respond to complex data requests submitted by external organizations; and (2) may impose fees on the organizations submitting the requests.</p>",
      "updateDate": "2026-02-19",
      "versionCode": "id119s517"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-02-11",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s517is.xml"
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
      "title": "Forest Data Modernization Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-03-14T03:23:18Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Forest Data Modernization Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-14T03:23:17Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend the Forest and Rangeland Renewable Resources Research Act of 1978 to modify the forest inventory and analysis program.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-14T03:18:20Z"
    }
  ]
}
```
