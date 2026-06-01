# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/382?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/382
- Title: Exported Carbon Emissions Report Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 382
- Origin chamber: House
- Introduced date: 2025-01-14
- Update date: 2026-01-14T16:37:38Z
- Update date including text: 2026-01-14T16:37:38Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-01-14: Introduced in House
- 2025-01-14 - IntroReferral: Introduced in House
- 2025-01-14 - IntroReferral: Introduced in House
- 2025-01-14 - IntroReferral: Referred to the House Committee on Energy and Commerce.
- Latest action: 2025-01-14: Introduced in House

## Actions

- 2025-01-14 - IntroReferral: Introduced in House
- 2025-01-14 - IntroReferral: Introduced in House
- 2025-01-14 - IntroReferral: Referred to the House Committee on Energy and Commerce.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-01-14",
    "latestAction": {
      "actionDate": "2025-01-14",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/382",
    "number": "382",
    "originChamber": "House",
    "policyArea": {
      "name": "Transportation and Public Works"
    },
    "sponsors": [
      {
        "bioguideId": "C001117",
        "district": "6",
        "firstName": "Sean",
        "fullName": "Rep. Casten, Sean [D-IL-6]",
        "lastName": "Casten",
        "party": "D",
        "state": "IL"
      }
    ],
    "title": "Exported Carbon Emissions Report Act of 2025",
    "type": "HR",
    "updateDate": "2026-01-14T16:37:38Z",
    "updateDateIncludingText": "2026-01-14T16:37:38Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-01-14",
      "committees": {
        "item": {
          "name": "Energy and Commerce Committee",
          "systemCode": "hsif00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Energy and Commerce.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-01-14",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-01-14",
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
          "date": "2025-01-14T15:02:40Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Energy and Commerce Committee",
      "systemCode": "hsif00",
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
      "bioguideId": "N000147",
      "district": "0",
      "firstName": "Eleanor",
      "fullName": "Del. Norton, Eleanor Holmes [D-DC]",
      "isOriginalCosponsor": "True",
      "lastName": "Norton",
      "middleName": "Holmes",
      "party": "D",
      "sponsorshipDate": "2025-01-14",
      "state": "DC"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr382ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 382\nIN THE HOUSE OF REPRESENTATIVES\nJanuary 14, 2025 Mr. Casten (for himself and Ms. Norton ) introduced the following bill; which was referred to the Committee on Energy and Commerce\nA BILL\nTo require the Administrator of the Environmental Protection Agency to collect, calculate, and publish information regarding emissions of carbon dioxide and methane outside the boundaries of the United States that are associated with exports of fossil fuels, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Exported Carbon Emissions Report Act of 2025 .\n#### 2. Comparison of trends in domestic and exported carbon emissions\n##### (a) In general\nNot later than 180 days after the enactment of this Act and annually thereafter, the Administrator of the Environmental Protection Agency shall collect, calculate, and publish information, for each of the previous ten calendar years, on\u2014\n**(1)**\nthe total emissions of carbon dioxide and methane that are released within the boundaries of the United States (including the territories of the United States) that are the result of the extraction, processing, transportation, combustion, and other use of fossil fuels; and\n**(2)**\nthe total emissions of carbon dioxide and methane that are released outside the boundaries of the United States (including the territories of the United States) that are the result of leakage and combustion of fossil fuels produced or refined in the United States and subsequently exported from the United States.\n##### (b) Information\nIn collecting and calculating information under this section, the Administrator of the Environmental Protection Agency shall\u2014\n**(1)**\nuse the best available scientific information, including, where available\u2014\n**(A)**\ninformation collected through direct monitoring and measurement; and\n**(B)**\ndisclosures of carbon dioxide and methane emissions by other national and subnational governments; and\n**(2)**\nbe informed by the established international standards for accounting for greenhouse gas emissions, including the protocols established under the Greenhouse Gas Protocol of the World Business Council for Sustainable Development and the World Resources Institute.\n##### (c) Consultation\nIn implementing this section, the Administrator of the Environmental Protection Agency shall consult with\u2014\n**(1)**\nthe Administrator of the Energy Information Administration; and\n**(2)**\nthe executive director of the International Energy Agency.\n##### (d) Publication of information\nThe Administrator of the Environmental Protection Agency shall make the information collected and calculated pursuant to this section widely available to the public, including by publishing such information on the website of the Environmental Protection Agency.\n##### (e) Definition of fossil fuel\nIn this section, the term fossil fuel means carbon-containing material formed in the Earth\u2019s crust from the remains of prehistoric organisms, including coal, oil, and natural gas.",
      "versionDate": "2025-01-14",
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
        "name": "Transportation and Public Works",
        "updateDate": "2026-01-14T16:37:38Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-01-14",
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
          "measure-id": "id119hr382",
          "measure-number": "382",
          "measure-type": "hr",
          "orig-publish-date": "2025-01-14",
          "originChamber": "HOUSE",
          "update-date": "2025-04-03"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr382v00",
            "update-date": "2025-04-03"
          },
          "action-date": "2025-01-14",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Exported Carbon Emissions Report Act of 2025</strong></p><p>This bill directs the Environmental Protection Agency (EPA) to annually collect, calculate, and publish information on certain emissions of carbon dioxide and methane from fossil fuels. Specifically, the EPA must publish information, for each of the previous 10 years, on the total emissions of carbon dioxide and methane that are released (1) within the boundaries of the United States that are the result of the extraction, processing, transportation, combustion, and other use of fossil fuels; and (2) outside the boundaries of the United States that are the result of leakage and combustion of fossil fuels produced or refined in the United States and subsequently exported.</p>"
        },
        "title": "Exported Carbon Emissions Report Act of 2025"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr382.xml",
    "summary": {
      "actionDate": "2025-01-14",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Exported Carbon Emissions Report Act of 2025</strong></p><p>This bill directs the Environmental Protection Agency (EPA) to annually collect, calculate, and publish information on certain emissions of carbon dioxide and methane from fossil fuels. Specifically, the EPA must publish information, for each of the previous 10 years, on the total emissions of carbon dioxide and methane that are released (1) within the boundaries of the United States that are the result of the extraction, processing, transportation, combustion, and other use of fossil fuels; and (2) outside the boundaries of the United States that are the result of leakage and combustion of fossil fuels produced or refined in the United States and subsequently exported.</p>",
      "updateDate": "2025-04-03",
      "versionCode": "id119hr382"
    },
    "title": "Exported Carbon Emissions Report Act of 2025"
  },
  "summaries": [
    {
      "actionDate": "2025-01-14",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Exported Carbon Emissions Report Act of 2025</strong></p><p>This bill directs the Environmental Protection Agency (EPA) to annually collect, calculate, and publish information on certain emissions of carbon dioxide and methane from fossil fuels. Specifically, the EPA must publish information, for each of the previous 10 years, on the total emissions of carbon dioxide and methane that are released (1) within the boundaries of the United States that are the result of the extraction, processing, transportation, combustion, and other use of fossil fuels; and (2) outside the boundaries of the United States that are the result of leakage and combustion of fossil fuels produced or refined in the United States and subsequently exported.</p>",
      "updateDate": "2025-04-03",
      "versionCode": "id119hr382"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-01-14",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr382ih.xml"
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
      "title": "Exported Carbon Emissions Report Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-02-11T05:08:18Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Exported Carbon Emissions Report Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-02-11T05:08:16Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To require the Administrator of the Environmental Protection Agency to collect, calculate, and publish information regarding emissions of carbon dioxide and methane outside the boundaries of the United States that are associated with exports of fossil fuels, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-02-11T05:03:28Z"
    }
  ]
}
```
