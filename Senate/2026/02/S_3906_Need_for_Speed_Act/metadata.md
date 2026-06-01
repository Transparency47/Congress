# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/3906?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/3906
- Title: Need for Speed Act
- Congress: 119
- Bill type: S
- Bill number: 3906
- Origin chamber: Senate
- Introduced date: 2026-02-24
- Update date: 2026-03-13T15:14:10Z
- Update date including text: 2026-03-13T15:14:10Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2026-02-24: Introduced in Senate
- 2026-02-24 - IntroReferral: Introduced in Senate
- 2026-02-24 - IntroReferral: Read twice and referred to the Committee on Environment and Public Works.
- Latest action: 2026-02-24: Introduced in Senate

## Actions

- 2026-02-24 - IntroReferral: Introduced in Senate
- 2026-02-24 - IntroReferral: Read twice and referred to the Committee on Environment and Public Works.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-02-24",
    "latestAction": {
      "actionDate": "2026-02-24",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/3906",
    "number": "3906",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Transportation and Public Works"
    },
    "sponsors": [
      {
        "bioguideId": "C001056",
        "district": "",
        "firstName": "John",
        "fullName": "Sen. Cornyn, John [R-TX]",
        "lastName": "Cornyn",
        "party": "R",
        "state": "TX"
      }
    ],
    "title": "Need for Speed Act",
    "type": "S",
    "updateDate": "2026-03-13T15:14:10Z",
    "updateDateIncludingText": "2026-03-13T15:14:10Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-02-24",
      "committees": {
        "item": {
          "name": "Environment and Public Works Committee",
          "systemCode": "ssev00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Environment and Public Works.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2026-02-24",
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
          "date": "2026-02-24T22:30:30Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Environment and Public Works Committee",
      "systemCode": "ssev00",
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
      "bioguideId": "A000382",
      "firstName": "Angela",
      "fullName": "Sen. Alsobrooks, Angela D. [D-MD]",
      "isOriginalCosponsor": "True",
      "lastName": "Alsobrooks",
      "party": "D",
      "sponsorshipDate": "2026-02-24",
      "state": "MD"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s3906is.xml",
      "text": "II\n119th CONGRESS\n2d Session\nS. 3906\nIN THE SENATE OF THE UNITED STATES\nFebruary 24, 2026 Mr. Cornyn (for himself and Ms. Alsobrooks ) introduced the following bill; which was read twice and referred to the Committee on Environment and Public Works\nA BILL\nTo amend title 23, United States Code, to require the Secretary of Transportation to develop a national infrastructure intelligence tool for congestion mitigation, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Need for Speed Act .\n#### 2. National infrastructure intelligence tool\n##### (a) In general\nChapter 5 of title 23, United States Code, is amended by inserting after section 505 the following:\n506. National infrastructure intelligence tool (a) In general The Secretary, in coordination with relevant Federal agencies and departments, as appropriate, shall engage with a university-based transportation research institute with a history of research related to traffic and freight mobility, safety, freight and supply chains (including truck parking), asset conditions, congestion mitigation, performance measurement and management, and data integration, to develop and maintain a national infrastructure intelligence tool with consistent data aligned to a roadway inventory network database, such as the official public highway performance monitoring system, for use by the Department of Transportation, State and local transportation agencies, metropolitan planning organizations, other transportation agencies, coalitions of public agencies, and regional planning agencies. (b) Purpose The tool developed pursuant to subsection (a) shall serve as a consistent and ongoing national congestion mitigation resource to leverage and integrate relevant Federal, State, local, and private, but publicly available, data sets with the official public highway performance monitoring system or roadway inventory network\u2014 (1) to identify the locations of congestion; (2) to provide context to determine the cause of congestion; (3) to quantify impacts of congestion; and (4) to enable the expeditious deployment of congestion mitigation resources through investment and operational decisions. (c) Components In developing the tool pursuant to subsection (a), the Secretary shall leverage and include the following types of publicly available data sources and measures: (1) The official highway performance monitoring system or roadway inventory network used by States and the Department of Transportation. (2) The following data sources, leveraging existing data sources to the extent possible, which shall be aligned with the official highway performance monitoring system or roadway inventory network: (A) A national speed data set, including operating speeds and posted speed limits, with not less than 3 years of historical data for all available public, paved roads functionally classified 1 through 6. (B) A national vehicle origin and destination information dataset with not less than 3 years of historical data on all public road travel. (C) Crash and other relevant safety data. (D) Asset condition data, such as data available in the Highway Performance Monitoring System dataset of the Federal Highway Administration. (E) Commodity data, including type, tonnage, and value of commodities on the roadway. (F) Truck parking demand and supply data, as available. (3) Federal congestion performance measurement resources, such as the Urban Congestion Report of the Federal Highway Administration and related performance measurement materials. (4) The performance measures for safety and infrastructure condition established pursuant to section 150(c). (5) The Freight Mobility Trends tool of the Federal Highway Administration. (6) The Urban Mobility Report of the Texas A&M Transportation Institute. (7) Relevant State and local congestion and infrastructure intelligence tools, as appropriate, such as\u2014 (A) the Texas Department of Transportation Texas Top 100 Congested Road Segments annual assessment and the associated Texas Assessment of Congested Roadways Tool; (B) the Texas Congestion Management Process Assessment Tool; (C) the Texas Truck Congestion Analysis Tool; (D) the University of Maryland Center for Advanced Transportation Technology Lab causes of congestion tool and methodology; (E) the Texas Freight Fluidity Tool; (F) the Maryland Department of Transportation Truck Parking Tool; (G) the Maryland Roadway Performance Tool; and (H) the University of Maryland Center for Advanced Transportation Technology Lab Regional Integrated Transportation Information System resource. (8) Other relevant sources, new data, and measures, as determined appropriate by the Secretary. (d) Updates The Secretary shall update the tool developed pursuant to subsection (a) as necessary, but not less frequently than annually. (e) Consultation The Secretary shall consult with State departments of transportation, transportation advocacy organizations, and other appropriate organizations, as determined by the Secretary, in the development of the tool pursuant to subsection (a). (f) Authorization of appropriations (1) In general There is authorized to be appropriated out of the Highway Trust Fund (other than the Mass Transit Account) $50,000,000 to carry out this section. (2) Availability Notwithstanding any other provision of law, the amounts made available under paragraph (1) shall be available for a period of 5 fiscal years. (3) Additional funds Amounts made available under paragraph (1) shall be in addition to any amounts otherwise made available to carry out this section, including through an appropriations Act. .\n##### (b) Clerical amendment\nChapter 5 of title 23, United States Code, is amended by inserting after the item relating to section 505 the following:\n506. National infrastructure intelligence tool. .",
      "versionDate": "2026-02-24",
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
        "name": "Transportation and Public Works",
        "updateDate": "2026-03-13T15:14:10Z"
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
      "date": "2026-02-24",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s3906is.xml"
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
      "title": "Need for Speed Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-03-12T04:23:29Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Need for Speed Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-03-12T04:23:28Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend title 23, United States Code, to require the Secretary of Transportation to develop a national infrastructure intelligence tool for congestion mitigation, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-03-12T04:18:26Z"
    }
  ]
}
```
