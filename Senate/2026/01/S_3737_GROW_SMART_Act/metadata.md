# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/3737?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/3737
- Title: GROW SMART Act
- Congress: 119
- Bill type: S
- Bill number: 3737
- Origin chamber: Senate
- Introduced date: 2026-01-29
- Update date: 2026-04-02T18:14:50Z
- Update date including text: 2026-04-02T18:14:50Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, subjects, text, titles

## Timeline

- 2026-01-29: Introduced in Senate
- 2026-01-29 - IntroReferral: Introduced in Senate
- 2026-01-29 - IntroReferral: Read twice and referred to the Committee on Energy and Natural Resources. (Sponsor introductory remarks on measure: CR S380)
- 2026-03-17 - Committee: Committee on Energy and Natural Resources Subcommittee on Water and Power. Hearings held.
- Latest action: 2026-01-29: Introduced in Senate

## Actions

- 2026-01-29 - IntroReferral: Introduced in Senate
- 2026-01-29 - IntroReferral: Read twice and referred to the Committee on Energy and Natural Resources. (Sponsor introductory remarks on measure: CR S380)
- 2026-03-17 - Committee: Committee on Energy and Natural Resources Subcommittee on Water and Power. Hearings held.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-01-29",
    "latestAction": {
      "actionDate": "2026-01-29",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/3737",
    "number": "3737",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Water Resources Development"
    },
    "sponsors": [
      {
        "bioguideId": "P000145",
        "district": "",
        "firstName": "Alex",
        "fullName": "Sen. Padilla, Alex [D-CA]",
        "lastName": "Padilla",
        "party": "D",
        "state": "CA"
      }
    ],
    "title": "GROW SMART Act",
    "type": "S",
    "updateDate": "2026-04-02T18:14:50Z",
    "updateDateIncludingText": "2026-04-02T18:14:50Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-03-17",
      "committees": {
        "item": {
          "name": "Water and Power Subcommittee",
          "systemCode": "sseg07"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Committee on Energy and Natural Resources Subcommittee on Water and Power. Hearings held.",
      "type": "Committee"
    },
    {
      "actionDate": "2026-01-29",
      "committees": {
        "item": {
          "name": "Energy and Natural Resources Committee",
          "systemCode": "sseg00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Energy and Natural Resources. (Sponsor introductory remarks on measure: CR S380)",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2026-01-29",
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
          "date": "2026-01-29T19:24:33Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Energy and Natural Resources Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": {
              "date": "2026-03-17T14:00:28Z",
              "name": "Hearings By (subcommittee)"
            }
          },
          "name": "Water and Power Subcommittee",
          "systemCode": "sseg07"
        }
      },
      "systemCode": "sseg00",
      "type": "Standing"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s3737is.xml",
      "text": "II\n119th CONGRESS\n2d Session\nS. 3737\nIN THE SENATE OF THE UNITED STATES\nJanuary 29, 2026 Mr. Padilla introduced the following bill; which was read twice and referred to the Committee on Energy and Natural Resources\nA BILL\nTo amend the Reclamation States Emergency Drought Relief Act of 1991 to provide financial and technical assistance to eligible entities for the conduct of innovative approaches to voluntary water partnership agreements among multiple water users and projects conducted by individual agricultural entities, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Growing Resilient Operations from Water Saving and Municipal-Agricultural Reciprocally-beneficial Transactions Act or the GROW SMART Act .\n#### 2. Project planning in support of innovative voluntary water sharing agreements and voluntary use of water-thrifty crops\nTitle II of the Reclamation States Emergency Drought Relief Act of 1991 ( 43 U.S.C. 2221 et seq. ) is amended by inserting after section 201 the following:\n201A. Project planning in support of innovative voluntary water sharing agreements and voluntary use of water-thrifty crops to prepare for and respond to drought (a) In general The Secretary, in order to prepare for and respond to drought conditions, may, using funds made available to carry out this title and under subsection (g), provide to qualified applicants technical and financial assistance to provide planning support for the implementation of voluntary projects incorporating innovative approaches that\u2014 (1) (A) keep agricultural land in production; and (B) support income and employment levels in rural communities; (2) provide affordable water supplies, redundant water supplies, shared storage, or other benefits; and (3) rely over the long term on sources other than Federal funding for implementation. (b) Description of innovative approach An innovative approach referred to in subsection (a)\u2014 (1) shall\u2014 (A) be new; or (B) lack a well-established track record in the applicable area; (2) shall include an approach that\u2014 (A) insulates agricultural water users from the risk of crop failures or water shortages through voluntary financial, water storage, or water sharing agreements between at least 1 party described in subsection (c)(1)(A)(i) and 1 party described in subsection (c)(1)(A)(ii); (B) brings water-saving commodities or practices into production; or (C) involves voluntary methods for reducing agricultural consumptive water use, including\u2014 (i) hydroponics; (ii) agrovoltaics; (iii) agroforestry; (iv) innovative irrigation technologies, including gravity-powered drip irrigation and automated high-efficiency surface irrigation; (v) root-zone-based irrigation management systems; (vi) implementation of regenerative agricultural practices that decrease net water consumption; or (vii) concentration of crop production on a reduced irrigated acreage that results in an equal or greater financial return; and (3) shall not include an approach that\u2014 (A) fallows agricultural land for\u2014 (i) the majority of the growing season in the applicable area; or (ii) in the case of a drought-year agreement, is reasonably anticipated to result in fallowing for the majority of years under the drought-year agreement; or (B) involves crops in the applicable area (other than crops using an approach described in paragraph (2)) that are\u2014 (i) widely used or planted; or (ii) well understood in terms of yield, cost, and other key production factors. (c) Qualified applicants (1) In general Except as provided in paragraph (3), to qualify for financial or technical assistance under this section, an applicant shall\u2014 (A) propose a voluntary partnership among\u2014 (i) 1 or more agricultural entities (including irrigation districts); and (ii) 1 or more\u2014 (I) State, municipal, or other community water providers; (II) industrial or commercial entities, including data centers; (III) States, State agencies, or subdivisions of a State; or (IV) nonprofit conservation organizations; and (B) submit to the Secretary an application signed by at least 1 party described in subparagraph (A)(i) and 1 party described in subparagraph (A)(ii). (2) No limits on participation of Tribal entities Each of the parties described in clauses (i) and (ii) of paragraph (1)(A) may be Tribal entities. (3) Projects without voluntary partnerships (A) In general Notwithstanding paragraph (1), the Secretary may award to a State, State agency, or subdivision of a State, Indian Tribe, or agricultural entity that is not in a voluntary partnership with other entities described in paragraph (1)(A) a portion of the financial assistance authorized under this section for the planning or conduct of a voluntary project that\u2014 (i) uses an innovative approach described in paragraphs (1) and (2) of subsection (b); or (ii) with respect to a voluntary project conducted by a State, State agency, or Indian Tribe, would advance other long-term efforts to reverse declining\u2014 (I) groundwater supplies; or (II) freshwater inflows to inland lakes. (B) Priority consideration The Secretary shall give priority consideration to an application for financial assistance under this paragraph for which the following thresholds have been met or are projected to be met: (i) In the case of an application from an agricultural entity or subdivision of a State, a reduction of 40 percent or more in the annual water supply of the agricultural entity or subdivision of the State, due to factors outside the control of the agricultural entity or subdivision of the State. (ii) In the case of an application from a State, State agency, or Indian Tribe, a reduction of 40 percent or more in\u2014 (I) groundwater supplies; or (II) freshwater inflows to inland lakes. (d) Application requirements The Secretary shall ensure that applications for financial or technical assistance under this section\u2014 (1) shall be limited to\u2014 (A) a brief description of why the proposed approach to be provided assistance is consistent with this section and the priorities described in subsection (e); and (B) any basic information on the applicant that the Secretary determines to be necessary; and (2) shall not require any preparation of supporting reports by the applicant or other entities. (e) Priority The Secretary shall prioritize applications for financial or technical assistance under this section based on\u2014 (1) for projects involving a voluntary partnership under subsection (c)(1), whether the proposed project would dedicate a portion of the water saved in the project area to increase water supplies for\u2014 (A) other members of the water district within which the project is located; or (B) in the case of a project not within a water district, other members of the municipality, Indian Tribe, acequia, or other community unit within which the project is located; (2) the extent to which the proposed approach is innovative in terms of\u2014 (A) the practices implemented or the crops planted; (B) the financial or other aspects of the voluntary partnership among the agricultural entities and municipal or industrial entities or nonprofit conservation organizations; or (C) a combination of the factors described in subparagraphs (A) and (B); (3) the extent to which the proposed approach is preliminarily estimated to reduce consumptive agricultural water use compared to existing practices while keeping agricultural land in production; (4) the extent to which the proposed approach is preliminarily estimated to support income and employment levels in the relevant agricultural community compared to existing practices (whether due to increased yields, lower input costs, or other factors); (5) the assessment of the Secretary of the likelihood that the proposed approach is likely to be successfully implemented as proposed; (6) whether the voluntary water sharing agreements among the agricultural entities and municipal or industrial entities or nonprofit conservation organizations are proposed for a period of not less than 10 years; (7) the likelihood of the project to sustain the project long-term without the need for additional Federal funding after the project demonstration phase; and (8) such other factors as the Secretary determines to be appropriate, consistent with subsection (c)(3). (f) Cost-Sharing requirement (1) In general The Federal share of activities provided financial assistance under this section shall not exceed 75 percent of the cost of the activities. (2) Waiver The Secretary may waive the cost-sharing requirement under paragraph (1) for Tribal entities. (g) Funding (1) In general Notwithstanding any other provision of law, the Secretary may use not more than 10 percent of the amounts made available under section 9504(e) of the Omnibus Public Land Management Act of 2009 ( 42 U.S.C. 10364(e) ) to carry out this section. (2) Authorization of appropriations In addition to any amounts otherwise made available to carry out this title and amounts made available under paragraph (1), there is authorized to be appropriated to the Secretary to carry out this section $5,000,000 for each of fiscal years 2028 through 2034. .",
      "versionDate": "2026-01-29",
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
      "legislativeSubjects": {
        "item": [
          {
            "name": "Agricultural practices and innovations",
            "updateDate": "2026-04-02T18:14:45Z"
          },
          {
            "name": "Public-private cooperation",
            "updateDate": "2026-04-02T18:14:50Z"
          },
          {
            "name": "Water resources funding",
            "updateDate": "2026-04-02T18:13:42Z"
          },
          {
            "name": "Water storage",
            "updateDate": "2026-04-02T18:14:17Z"
          },
          {
            "name": "Water use and supply",
            "updateDate": "2026-04-02T18:14:36Z"
          }
        ]
      },
      "policyArea": {
        "name": "Water Resources Development",
        "updateDate": "2026-02-23T21:55:06Z"
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
      "date": "2026-01-29",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s3737is.xml"
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
      "title": "GROW SMART Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-03-18T11:03:18Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "GROW SMART Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-02-19T05:23:24Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Growing Resilient Operations from Water Saving and Municipal-Agricultural Reciprocally-beneficial Transactions Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-02-19T05:23:24Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend the Reclamation States Emergency Drought Relief Act of 1991 to provide financial and technical assistance to eligible entities for the conduct of innovative approaches to voluntary water partnership agreements among multiple water users and projects conducted by individual agricultural entities, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-02-19T05:18:37Z"
    }
  ]
}
```
