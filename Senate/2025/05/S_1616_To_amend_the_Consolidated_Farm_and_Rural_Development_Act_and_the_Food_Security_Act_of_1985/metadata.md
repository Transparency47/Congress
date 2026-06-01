# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/1616?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/1616
- Title: PRECISE Act of 2025
- Congress: 119
- Bill type: S
- Bill number: 1616
- Origin chamber: Senate
- Introduced date: 2025-05-06
- Update date: 2025-09-29T16:10:16Z
- Update date including text: 2025-09-29T16:10:16Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-05-06: Introduced in Senate
- 2025-05-06 - IntroReferral: Introduced in Senate
- 2025-05-06 - IntroReferral: Read twice and referred to the Committee on Agriculture, Nutrition, and Forestry.
- Latest action: 2025-05-06: Introduced in Senate

## Actions

- 2025-05-06 - IntroReferral: Introduced in Senate
- 2025-05-06 - IntroReferral: Read twice and referred to the Committee on Agriculture, Nutrition, and Forestry.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-05-06",
    "latestAction": {
      "actionDate": "2025-05-06",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/1616",
    "number": "1616",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Agriculture and Food"
    },
    "sponsors": [
      {
        "bioguideId": "F000463",
        "district": "",
        "firstName": "Deb",
        "fullName": "Sen. Fischer, Deb [R-NE]",
        "lastName": "Fischer",
        "party": "R",
        "state": "NE"
      }
    ],
    "title": "PRECISE Act of 2025",
    "type": "S",
    "updateDate": "2025-09-29T16:10:16Z",
    "updateDateIncludingText": "2025-09-29T16:10:16Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-05-06",
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
      "actionDate": "2025-05-06",
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
          "date": "2025-05-06T17:17:03Z",
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
      "bioguideId": "K000367",
      "firstName": "Amy",
      "fullName": "Sen. Klobuchar, Amy [D-MN]",
      "isOriginalCosponsor": "True",
      "lastName": "Klobuchar",
      "party": "D",
      "sponsorshipDate": "2025-05-06",
      "state": "MN"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1616is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 1616\nIN THE SENATE OF THE UNITED STATES\nMay 6, 2025 Mrs. Fischer (for herself and Ms. Klobuchar ) introduced the following bill; which was read twice and referred to the Committee on Agriculture, Nutrition, and Forestry\nA BILL\nTo amend the Consolidated Farm and Rural Development Act and the Food Security Act of 1985 to leverage incentives for the adoption of precision agriculture practices and technology, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Producing Responsible Energy and Conservation Incentives and Solutions for the Environment Act of 2025 or the PRECISE Act of 2025 .\n#### 2. Assistance to rural entities\nSection 310B(a) of the Consolidated Farm and Rural Development Act ( 7 U.S.C. 1932(a) ) is amended\u2014\n**(1)**\nin paragraph (1)\u2014\n**(A)**\nby redesignating subparagraph (B) as subparagraph (C); and\n**(B)**\nby inserting after subparagraph (A) the following:\n(B) Precision agriculture; precision agriculture technology The terms precision agriculture and precision agriculture technology have the meanings given those terms in section 1201(a) of the Food Security Act of 1985 ( 16 U.S.C. 3801(a) ). ; and\n**(2)**\nin paragraph (2)\u2014\n**(A)**\nin subparagraph (C), by striking and at the end;\n**(B)**\nin subparagraph (D)\u2014\n**(i)**\nby striking to facilitate and inserting facilitating ; and\n**(ii)**\nby striking the period at the end and inserting ; and ; and\n**(C)**\nby adding at the end the following:\n(E) expanding the adoption of precision agriculture practices, including by financing the acquisition of precision agriculture technology, in order to promote best practices, reduce costs, and improve the environment. .\n#### 3. Food Security Act of 1985 definitions\nSection 1201(a) of the Food Security Act of 1985 ( 16 U.S.C. 3801(a) ) is amended\u2014\n**(1)**\nin each of paragraphs (1), (5), (6), (7), (10), (11), (12), (13), (15), (20), (21), (22), (24), (26), and (27), by inserting a paragraph heading, the text of which comprises the term defined in that paragraph;\n**(2)**\nby redesignating paragraphs (20) through (27) as paragraphs (22) through (29), respectively; and\n**(3)**\nby inserting after paragraph (19) the following:\n(20) Precision agriculture The term precision agriculture means managing, tracking, or reducing any crop or livestock production input, including seed, feed, fertilizer, chemicals, water, and time, at a heightened level of spatial and temporal granularity to improve efficiencies, reduce waste, and maintain environmental quality. (21) Precision agriculture technology The term precision agriculture technology means any technology (including equipment that is necessary for the deployment of such a technology) that directly contributes to a reduction in, or improved efficiency of, an input used in crop or livestock production, including\u2014 (A) Global Positioning System-based or geospatial mapping; (B) satellite or aerial imagery; (C) yield monitors; (D) soil mapping; (E) sensors for gathering data relating to crop, soil, or livestock conditions; (F) Internet of Things and telematics technologies; (G) data management software and advanced analytics; (H) network connectivity products and solutions; (I) Global Positioning System guidance or auto-steer systems; (J) variable rate technology for applying inputs, such as section control; and (K) any other technology, as determined by the Secretary, that leads to a reduction in, or improves efficiency of, a crop or livestock production input, which may include seed, feed, fertilizer, chemicals, water, and time. .\n#### 4. Environmental Quality Incentives Program\n##### (a) Definitions\nSection 1240A(6)(B)(v) of the Food Security Act of 1985 ( 16 U.S.C. 3839aa\u20131(6)(B)(v) ) is amended by inserting (including the adoption of precision agriculture practices and the acquisition of precision agriculture technology) after planning .\n##### (b) Payments\n**(1) Other payments**\nSection 1240B(d)(6) of the Food Security Act of 1985 ( 16 U.S.C. 3839aa\u20132(d)(6) ) is amended\u2014\n**(A)**\nby striking A producer shall and inserting the following:\n(A) Payments under this subtitle A producer shall ; and\n**(B)**\nby adding at the end the following:\n(B) Conservation loan and loan guarantee program payments (i) In general A producer receiving payments for practices on eligible land under the program may also receive a loan or loan guarantee under section 304 of the Consolidated Farm and Rural Development Act ( 7 U.S.C. 1924 ) to cover costs for the same practices on the same land. (ii) Notice to producers The Secretary shall inform a producer participating in the program, in writing, that the producer may apply to receive a loan or loan guarantee under section 304 of the Consolidated Farm and Rural Development Act ( 7 U.S.C. 1924 ) with respect to the costs of implementing practices under the program. .\n**(2) Increased payments for State-determined high-priority practices**\nSection 1240B(d)(7) of the Food Security Act of 1985 ( 16 U.S.C. 3839aa\u20132(d)(7) ) is amended, in the paragraph heading, by inserting State-determined before high-priority .\n**(3) Increased payments for precision agriculture**\nSection 1240B(d) of the Food Security Act of 1985 ( 16 U.S.C. 3839aa\u20132(d) ) is amended by adding at the end the following:\n(8) Increased payments for precision agriculture Notwithstanding paragraph (2), the Secretary may increase the amount that would otherwise be provided for a practice under this subsection to not more than 90 percent of the costs associated with adopting precision agriculture practices and acquiring precision agriculture technology for the purpose of implementing a conservation practice. .\n##### (c) Conservation incentive contracts\nSection 1240B(j)(2)(A)(i) of the Food Security Act of 1985 ( 16 U.S.C. 3839aa\u20132(j)(2)(A)(i) ) is amended by inserting (which may include the adoption of precision agriculture practices and the acquisition of precision agriculture technology) after incentive practices .\n#### 5. Conservation Stewardship Program supplemental payments\n##### (a) Conservation stewardship payments\nSection 1240L(c) of the Food Security Act of 1985 ( 16 U.S.C. 3839aa\u201324(c) ) is amended by striking paragraph (3) and inserting the following:\n(3) Exclusion A payment to a producer under this subsection shall not be provided for any conservation activities for which there is no cost incurred or income forgone by the producer. .\n##### (b) Supplemental payments for resource-Conserving crop rotations and advanced grazing management\nSection 1240L(d) of the Food Security Act of 1985 ( 16 U.S.C. 3839aa\u201324(d) ) is amended\u2014\n**(1)**\nin the subsection heading, by striking and advanced grazing management and inserting , advanced grazing management, and precision agriculture ;\n**(2)**\nin paragraph (2)\u2014\n**(A)**\nin subparagraph (A), by striking or at the end;\n**(B)**\nin subparagraph (B), by striking the period at the end and inserting ; or ; and\n**(C)**\nby adding at the end the following:\n(C) precision agriculture. ; and\n**(3)**\nin paragraph (3), by striking or advanced grazing management and inserting , advanced grazing management, or precision agriculture conservation activities .\n#### 6. Delivery of technical assistance\nSection 1242(f) of the Food Security Act of 1985 ( 16 U.S.C. 3842(f) ) is amended by adding at the end the following:\n(6) Soil health planning The Secretary shall emphasize the use of third-party providers in providing technical assistance for soil health planning, including planning relating to the use of cover crops, precision agriculture practices, comprehensive nutrient management planning, and other innovative plans. .",
      "versionDate": "2025-05-06",
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
        "updateDate": "2025-06-05T13:08:33Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-05-06",
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
          "measure-id": "id119s1616",
          "measure-number": "1616",
          "measure-type": "s",
          "orig-publish-date": "2025-05-06",
          "originChamber": "SENATE",
          "update-date": "2025-09-29"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "SENATE",
            "summary-id": "id119s1616v00",
            "update-date": "2025-09-29"
          },
          "action-date": "2025-05-06",
          "action-desc": "Introduced in Senate",
          "summary-text": "<p><strong>Producing Responsible Energy and Conservation Incentives and Solutions for the Environment Act of 2025 or the PRECISE Act</strong> <strong>of 2025</strong></p><p>This bill incorporates support for precision agriculture into various programs of the Department of Agriculture (USDA). <em>Precision agriculture</em> refers to managing, tracking, or reducing crop or livestock production inputs, including seed, feed, fertilizer, chemicals, water, and time, at a heightened level of spatial and temporal granularity to improve efficiencies, reduce waste, and maintain environmental quality. <em>Precision agriculture technology </em>includes any technology and equipment that directly contributes to a reduction in, or improved efficiency of, inputs used in crop or livestock production.</p><p>Specifically, the bill makes changes to eligibility criteria, payments, and other aspects of the Environmental Quality Incentives Program and the Conservation Stewardship Program. These changes include allowing the programs to support the adoption of precision agriculture practices and acquisition of precision agriculture technologies.</p><p>In addition, the bill expands a program through which USDA makes and insures loans to for-profit and nonprofit organizations that invest in rural areas by allowing the loans to be used for precision agriculture practices.</p><p>Also, USDA must emphasize the use of third-party providers when providing technical assistance on matters related to soil health for participants in certain USDA conservation programs. This includes planning related to the use of cover crops, precision agriculture practices, and comprehensive nutrient management.</p>"
        },
        "title": "PRECISE Act of 2025"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/s/BILLSUM-119s1616.xml",
    "summary": {
      "actionDate": "2025-05-06",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Producing Responsible Energy and Conservation Incentives and Solutions for the Environment Act of 2025 or the PRECISE Act</strong> <strong>of 2025</strong></p><p>This bill incorporates support for precision agriculture into various programs of the Department of Agriculture (USDA). <em>Precision agriculture</em> refers to managing, tracking, or reducing crop or livestock production inputs, including seed, feed, fertilizer, chemicals, water, and time, at a heightened level of spatial and temporal granularity to improve efficiencies, reduce waste, and maintain environmental quality. <em>Precision agriculture technology </em>includes any technology and equipment that directly contributes to a reduction in, or improved efficiency of, inputs used in crop or livestock production.</p><p>Specifically, the bill makes changes to eligibility criteria, payments, and other aspects of the Environmental Quality Incentives Program and the Conservation Stewardship Program. These changes include allowing the programs to support the adoption of precision agriculture practices and acquisition of precision agriculture technologies.</p><p>In addition, the bill expands a program through which USDA makes and insures loans to for-profit and nonprofit organizations that invest in rural areas by allowing the loans to be used for precision agriculture practices.</p><p>Also, USDA must emphasize the use of third-party providers when providing technical assistance on matters related to soil health for participants in certain USDA conservation programs. This includes planning related to the use of cover crops, precision agriculture practices, and comprehensive nutrient management.</p>",
      "updateDate": "2025-09-29",
      "versionCode": "id119s1616"
    },
    "title": "PRECISE Act of 2025"
  },
  "summaries": [
    {
      "actionDate": "2025-05-06",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Producing Responsible Energy and Conservation Incentives and Solutions for the Environment Act of 2025 or the PRECISE Act</strong> <strong>of 2025</strong></p><p>This bill incorporates support for precision agriculture into various programs of the Department of Agriculture (USDA). <em>Precision agriculture</em> refers to managing, tracking, or reducing crop or livestock production inputs, including seed, feed, fertilizer, chemicals, water, and time, at a heightened level of spatial and temporal granularity to improve efficiencies, reduce waste, and maintain environmental quality. <em>Precision agriculture technology </em>includes any technology and equipment that directly contributes to a reduction in, or improved efficiency of, inputs used in crop or livestock production.</p><p>Specifically, the bill makes changes to eligibility criteria, payments, and other aspects of the Environmental Quality Incentives Program and the Conservation Stewardship Program. These changes include allowing the programs to support the adoption of precision agriculture practices and acquisition of precision agriculture technologies.</p><p>In addition, the bill expands a program through which USDA makes and insures loans to for-profit and nonprofit organizations that invest in rural areas by allowing the loans to be used for precision agriculture practices.</p><p>Also, USDA must emphasize the use of third-party providers when providing technical assistance on matters related to soil health for participants in certain USDA conservation programs. This includes planning related to the use of cover crops, precision agriculture practices, and comprehensive nutrient management.</p>",
      "updateDate": "2025-09-29",
      "versionCode": "id119s1616"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-05-06",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1616is.xml"
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
      "title": "PRECISE Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-05-31T03:23:18Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "PRECISE Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-05-31T03:23:16Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Producing Responsible Energy and Conservation Incentives and Solutions for the Environment Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-05-31T03:23:16Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend the Consolidated Farm and Rural Development Act and the Food Security Act of 1985 to leverage incentives for the adoption of precision agriculture practices and technology, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-05-31T03:18:24Z"
    }
  ]
}
```
