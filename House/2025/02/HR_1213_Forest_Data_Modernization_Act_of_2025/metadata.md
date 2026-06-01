# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/1213?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/1213
- Title: Forest Data Modernization Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 1213
- Origin chamber: House
- Introduced date: 2025-02-11
- Update date: 2026-04-07T08:05:29Z
- Update date including text: 2026-04-07T08:05:29Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-02-11: Introduced in House
- 2025-02-11 - IntroReferral: Introduced in House
- 2025-02-11 - IntroReferral: Introduced in House
- 2025-02-11 - IntroReferral: Referred to the House Committee on Agriculture.
- Latest action: 2025-02-11: Introduced in House

## Actions

- 2025-02-11 - IntroReferral: Introduced in House
- 2025-02-11 - IntroReferral: Introduced in House
- 2025-02-11 - IntroReferral: Referred to the House Committee on Agriculture.

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
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/1213",
    "number": "1213",
    "originChamber": "House",
    "policyArea": {
      "name": "Public Lands and Natural Resources"
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
    "title": "Forest Data Modernization Act of 2025",
    "type": "HR",
    "updateDate": "2026-04-07T08:05:29Z",
    "updateDateIncludingText": "2026-04-07T08:05:29Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-02-11",
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
      "actionDate": "2025-02-11",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-02-11",
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
          "date": "2025-02-11T15:03:05Z",
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
      "bioguideId": "M001212",
      "district": "1",
      "firstName": "Barry",
      "fullName": "Rep. Moore, Barry [R-AL-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Moore",
      "party": "R",
      "sponsorshipDate": "2025-02-11",
      "state": "AL"
    },
    {
      "bioguideId": "S001226",
      "district": "6",
      "firstName": "Andrea",
      "fullName": "Rep. Salinas, Andrea [D-OR-6]",
      "isOriginalCosponsor": "False",
      "lastName": "Salinas",
      "party": "D",
      "sponsorshipDate": "2026-04-06",
      "state": "OR"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1213ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 1213\nIN THE HOUSE OF REPRESENTATIVES\nFebruary 11, 2025 Ms. Schrier (for herself and Mr. Moore of Alabama ) introduced the following bill; which was referred to the Committee on Agriculture\nA BILL\nTo amend the Forest and Rangeland Renewable Resources Research Act of 1978 to modify the forest inventory and analysis program.\n#### 1. Short title\nThis Act may be cited as the Forest Data Modernization Act of 2025 .\n#### 2. Forest inventory and analysis\n##### (a) In general\nSection 3(e) of the Forest and Rangeland Renewable Resources Research Act of 1978 ( 16 U.S.C. 1642(e) ) is amended\u2014\n**(1)**\nin paragraph (1)\u2014\n**(A)**\nby striking their resources and inserting the resources of those forests, including forest carbon, ;\n**(B)**\nby striking In compliance and inserting the following:\n(A) In general In compliance ; and\n**(C)**\nby adding at the end the following:\n(B) Additional methods Under the program under this subsection, the Secretary shall carry out, as a data collection method\u2014 (i) a timber products output study; and (ii) a national woodland owner survey. ;\n**(2)**\nin paragraph (3)(C), by inserting including with respect to available forest carbon data, after 2 decades, ;\n**(3)**\nin paragraph (4)\u2014\n**(A)**\nin the second sentence, by striking The standards and inserting the following:\n(B) Inclusions The standards described in subparagraph (A) ;\n**(B)**\nby striking (4) National standards and definitions .\u2014To ensure and inserting the following:\n(4) National consistency (A) Standards and definitions To ensure ; and\n**(C)**\nby adding at the end the following:\n(C) Terminology The Secretary shall include a clear description of the definition of forest used for purposes of reporting data from inventories and analyses of forests and the resources of forests under this subsection with\u2014 (i) any data or report provided under the program under this subsection; (ii) Renewable Resource Assessments prepared under section 3(a) of the Forest and Rangeland Renewable Resources Planning Act of 1974 ( 16 U.S.C. 1601(a) ); and (iii) any data or report provided to an entity outside the United States. ;\n**(4)**\nin paragraph (6)\u2014\n**(A)**\nin the matter preceding subparagraph (A), by striking Not later than 180 days after the date of enactment of this subsection, and inserting In accordance with paragraph (7), ; and\n**(B)**\nby striking subparagraphs (D) and (E) and inserting the following:\n(D) the organization and procedures necessary to understand and report on changes in land cover and use; (E) the organization and procedures necessary to evaluate carbon-related data variables, including soil carbon, collected from forest inventory and analysis plots, timber products output studies, and national woodland owner surveys to ensure that carbon accounting information needs can be met; and ; and\n**(5)**\nby adding at the end the following:\n(7) Updates to strategic plan (A) In general Not later than 180 days after the date of enactment of this paragraph, the Secretary shall prepare an update to the strategic plan under paragraph (6) to include\u2014 (i) a plan to implement nationally consistent data collection protocols and procedures to improve the statistical precision of base program estimates; (ii) pathways to integrate and report on changes in forest carbon, including below-ground carbon; (iii) plans, including the identification of challenges, to collaborate with other Federal agencies, non-Federal partners, and the private sector to integrate existing nationally available data sets and best available commercial technologies, such as remote sensing, spatial analysis techniques, and other new technologies; (iv) a plan to increase transparency and clarity in reporting in accordance with paragraph (4)(C); (v) a plan to expand current data collection, further integrate remote sensing technology, or both, to include procedures to improve the statistical precision of estimates at the sub-State level; (vi) a plan to expand current data collection, further integrate remote sensing technology, or both, to include information on renewable biomass supplies and carbon stocks at the local, State, regional, and national levels, including by ownership type; and (vii) such other matters as the Secretary determines to be appropriate based on recommendations of the Forest Inventory and Analysis National User Group. (B) Submission Not later than 180 days after the date of enactment of this paragraph, the Secretary shall submit to the Committee on Agriculture, Nutrition, and Forestry of the Senate and the Committee on Agriculture of the House of Representatives the update to the strategic plan prepared under subparagraph (A). (C) Further updates Not later than 5 years after the date on which the update is submitted under subparagraph (B), and every 5 years thereafter, the Secretary shall\u2014 (i) prepare an additional update to the strategic plan; and (ii) submit the additional update to the committees described in subparagraph (B). (8) Accessibility The Secretary shall ensure that data collected under this subsection is\u2014 (A) easily accessible to all public- and private-sector entities; and (B) collected using means that ensure the confidentiality, in accordance with section 1770 of the Food Security Act of 1985 ( 7 U.S.C. 2276 ), of\u2014 (i) plot locations; (ii) nonaggregated data of woodland owners; and (iii) forest industry information. (9) Biennial compilations Biennially, the Secretary shall prepare and make publicly available a compilation of national forest inventory and analysis forest statistics, which shall be similar to the tables contained in the Renewable Resource Assessments prepared under section 3(a) of the Forest and Rangeland Renewable Resources Planning Act of 1974 ( 16 U.S.C. 1601(a) ). (10) External complex data requests (A) In general The Secretary shall establish an office, a data platform, or both to process and respond to complex data requests submitted by external organizations relating to the program under this subsection. (B) Fees To cover the costs of processing of and responding to complex data requests described in subparagraph (A), the Secretary may impose fees on the external organizations submitting the requests. (11) Reports Each year, the Secretary shall publish as part of the forest inventory and analysis business report a detailed description of the progress of the Secretary in implementing the programmatic elements of the strategic plan described in paragraph (6), including\u2014 (A) the costs and priorities of the strategic plan; and (B) how the program under this subsection leverages new technology, improves and standardizes collection protocols, and increases workforce capacity. .\n##### (b) Remote sensing technologies\nSection 8632(1) of the Agriculture Improvement Act of 2018 ( 16 U.S.C. 1642 note; Public Law 115\u2013334 ) is amended by striking technologies and inserting technologies, such as microwave, LiDAR, hyperspectral, and high-resolution remote sensing data for data collection, and machine learning for improved modeling, .",
      "versionDate": "2025-02-11",
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
        "actionDate": "2026-03-05",
        "text": "Ordered to be Reported (Amended) by the Yeas and Nays: 34 - 17."
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
        "text": "Read twice and referred to the Committee on Agriculture, Nutrition, and Forestry."
      },
      "number": "517",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Forest Data Modernization Act of 2025",
      "type": "S"
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
        "updateDate": "2025-05-07T15:07:32Z"
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
    "originChamber": "House",
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
          "measure-id": "id119hr1213",
          "measure-number": "1213",
          "measure-type": "hr",
          "orig-publish-date": "2025-02-11",
          "originChamber": "HOUSE",
          "update-date": "2026-02-13"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr1213v00",
            "update-date": "2026-02-13"
          },
          "action-date": "2025-02-11",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Forest Data Modernization Act of 2025</strong></p><p>This bill directs the Forest Service to expand and update its Forest Inventory and Analysis (FIA) program. Under the existing program, the Forest Service collects, analyzes, and reports on information about the condition of forest resources in the United States, such as data concerning wildfires or other forest management issues.</p><p>The bill directs FIA to include forest carbon in its inventory.\u00a0</p><p>The bill also requires FIA's strategic plan to\u00a0include a detailed description of the organization and procedures necessary to (1) understand and report on changes in land cover and use, and (2) evaluate carbon-related data variables.</p><p>FIA must\u00a0update the strategic plan within six months and every five years thereafter. Among other items, the first update must include (1) a plan to implement nationally consistent data collection protocols and procedures; and (2) a plan to expand current data collection, further integrate remote sensing technology, or both.\u00a0</p><p>FIA must also prepare and publish a\u00a0compilation of certain forest statistics every two years.</p><p>Additionally, the bill requires FIA to continue (1) the Timber Products Output\u00a0survey, and (2) the National Woodland Owner Survey.</p><p>To provide data consistency,\u00a0FIA must include a clear definition of <em>forest</em> when reporting data.</p><p>Finally, FIA (1) must also establish an office, a data platform, or both to process and respond to complex data requests submitted by external organizations; and (2) may impose fees on the organizations submitting the requests.</p>"
        },
        "title": "Forest Data Modernization Act of 2025"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr1213.xml",
    "summary": {
      "actionDate": "2025-02-11",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Forest Data Modernization Act of 2025</strong></p><p>This bill directs the Forest Service to expand and update its Forest Inventory and Analysis (FIA) program. Under the existing program, the Forest Service collects, analyzes, and reports on information about the condition of forest resources in the United States, such as data concerning wildfires or other forest management issues.</p><p>The bill directs FIA to include forest carbon in its inventory.\u00a0</p><p>The bill also requires FIA's strategic plan to\u00a0include a detailed description of the organization and procedures necessary to (1) understand and report on changes in land cover and use, and (2) evaluate carbon-related data variables.</p><p>FIA must\u00a0update the strategic plan within six months and every five years thereafter. Among other items, the first update must include (1) a plan to implement nationally consistent data collection protocols and procedures; and (2) a plan to expand current data collection, further integrate remote sensing technology, or both.\u00a0</p><p>FIA must also prepare and publish a\u00a0compilation of certain forest statistics every two years.</p><p>Additionally, the bill requires FIA to continue (1) the Timber Products Output\u00a0survey, and (2) the National Woodland Owner Survey.</p><p>To provide data consistency,\u00a0FIA must include a clear definition of <em>forest</em> when reporting data.</p><p>Finally, FIA (1) must also establish an office, a data platform, or both to process and respond to complex data requests submitted by external organizations; and (2) may impose fees on the organizations submitting the requests.</p>",
      "updateDate": "2026-02-13",
      "versionCode": "id119hr1213"
    },
    "title": "Forest Data Modernization Act of 2025"
  },
  "summaries": [
    {
      "actionDate": "2025-02-11",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Forest Data Modernization Act of 2025</strong></p><p>This bill directs the Forest Service to expand and update its Forest Inventory and Analysis (FIA) program. Under the existing program, the Forest Service collects, analyzes, and reports on information about the condition of forest resources in the United States, such as data concerning wildfires or other forest management issues.</p><p>The bill directs FIA to include forest carbon in its inventory.\u00a0</p><p>The bill also requires FIA's strategic plan to\u00a0include a detailed description of the organization and procedures necessary to (1) understand and report on changes in land cover and use, and (2) evaluate carbon-related data variables.</p><p>FIA must\u00a0update the strategic plan within six months and every five years thereafter. Among other items, the first update must include (1) a plan to implement nationally consistent data collection protocols and procedures; and (2) a plan to expand current data collection, further integrate remote sensing technology, or both.\u00a0</p><p>FIA must also prepare and publish a\u00a0compilation of certain forest statistics every two years.</p><p>Additionally, the bill requires FIA to continue (1) the Timber Products Output\u00a0survey, and (2) the National Woodland Owner Survey.</p><p>To provide data consistency,\u00a0FIA must include a clear definition of <em>forest</em> when reporting data.</p><p>Finally, FIA (1) must also establish an office, a data platform, or both to process and respond to complex data requests submitted by external organizations; and (2) may impose fees on the organizations submitting the requests.</p>",
      "updateDate": "2026-02-13",
      "versionCode": "id119hr1213"
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
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1213ih.xml"
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
      "title": "Forest Data Modernization Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-04-10T01:53:19Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Forest Data Modernization Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-04-10T01:53:17Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Forest and Rangeland Renewable Resources Research Act of 1978 to modify the forest inventory and analysis program.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-04-10T01:48:32Z"
    }
  ]
}
```
