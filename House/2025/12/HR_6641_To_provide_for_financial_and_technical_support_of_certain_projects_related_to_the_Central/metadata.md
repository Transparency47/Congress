# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/6641?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/6641
- Title: Central Valley Water Solution Act
- Congress: 119
- Bill type: HR
- Bill number: 6641
- Origin chamber: House
- Introduced date: 2025-12-11
- Update date: 2026-01-07T23:07:42Z
- Update date including text: 2026-01-07T23:07:42Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-12-11: Introduced in House
- 2025-12-11 - IntroReferral: Introduced in House
- 2025-12-11 - IntroReferral: Introduced in House
- 2025-12-11 - IntroReferral: Referred to the House Committee on Natural Resources.
- Latest action: 2025-12-11: Introduced in House

## Actions

- 2025-12-11 - IntroReferral: Introduced in House
- 2025-12-11 - IntroReferral: Introduced in House
- 2025-12-11 - IntroReferral: Referred to the House Committee on Natural Resources.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-12-11",
    "latestAction": {
      "actionDate": "2025-12-11",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/6641",
    "number": "6641",
    "originChamber": "House",
    "policyArea": {
      "name": "Water Resources Development"
    },
    "sponsors": [
      {
        "bioguideId": "G000605",
        "district": "13",
        "firstName": "Adam",
        "fullName": "Rep. Gray, Adam [D-CA-13]",
        "lastName": "Gray",
        "party": "D",
        "state": "CA"
      }
    ],
    "title": "Central Valley Water Solution Act",
    "type": "HR",
    "updateDate": "2026-01-07T23:07:42Z",
    "updateDateIncludingText": "2026-01-07T23:07:42Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-12-11",
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
      "actionDate": "2025-12-11",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-12-11",
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
          "date": "2025-12-11T16:02:00Z",
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
      "bioguideId": "C001059",
      "district": "21",
      "firstName": "Jim",
      "fullName": "Rep. Costa, Jim [D-CA-21]",
      "isOriginalCosponsor": "True",
      "lastName": "Costa",
      "party": "D",
      "sponsorshipDate": "2025-12-11",
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
      "sponsorshipDate": "2025-12-11",
      "state": "CA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6641ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 6641\nIN THE HOUSE OF REPRESENTATIVES\nDecember 11, 2025 Mr. Gray (for himself, Mr. Costa , and Mr. Harder of California ) introduced the following bill; which was referred to the Committee on Natural Resources\nA BILL\nTo provide for financial and technical support of certain projects related to the Central Valley Project, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Central Valley Water Solution Act .\n#### 2. Central Valley Project Water projects\n##### (a) Projects authorized\nThe Secretary shall provide financial and technical assistance for the following projects in the State, and there is authorized to be appropriated to the Secretary the corresponding amounts in parentheses to carry out this section:\n**(1)**\nWestland Water District Recharge Basins ($85,000,000), for the purchase by the District on a willing seller basis of 1,800 acres of land along the Coalinga Canal to build recharge basins in prime areas with greater percolation rates and within the unconfined zone of the subbasin, retrofitting the Coalinga Canal's existing turnouts to improve the conveyance capacity to the recharge facilities, and the construction of terraced berms to retain water at the recharge sites to enhance percolation and eliminate runoff.\n**(2)**\nWestlands Water District Reverse Osmosis Treatment Plants and High-Capacity Shallow Aquifer Wells ($30,000,000), for constructing 2 reverse osmosis treatment plants and 8 high-capacity shallow aquifer wells to reclaim approximately 20,000 acre-feet of poor-quality, perched groundwater to drinking quality levels.\n**(3)**\nEast San Joaquin Valley Groundwater Banking and Storage Program ($360,000,000), for a suite of groundwater banking, in-lieu groundwater recharge, groundwater quality treatment, and storage projects.\n**(4)**\nLindsay-Strathmore Irrigation District\u2014Rancho de Kaweah Groundwater Bank ($30,000,000), for constructing 1,200 acres of groundwater banking in multiple phases, including recovery wells, pipelines, and a new turnout and pilots to determine recharge and recovery rates.\n**(5)**\nPixley Irrigation District Joint Groundwater Bank ($25,000,000), for constructing 560 acres of groundwater banking in multiple phases, including recovery wells, pipelines, a new turnout and pilots to determine recharge and recovery rates. The project is anticipated to be completed within 2\u20133 years of funding availability.\n**(6)**\nShafter-Wasco Irrigation District Annex Groundwater Bank ($55,000,000), for constructing 3,000 acres of groundwater banking in multiple phases, including recovery wells, pipelines, and a new turnout and pilots to determine recharge and recovery rates.\n**(7)**\nArvin Edison Water Storage District DiGiorgio Unit In-Lieu Project ($12,900,000), for constructing a total of 11.8 miles of pipeline to convey and deliver surface water to support in-lieu groundwater recharge.\n**(8)**\nArvin Edison Water Storage District Frick Unit In-Lieu Project ($8,100,000), for constructing a total of 6 miles of pipeline to serve 2,843 acres of irrigated agriculture to support in-lieu groundwater recharge.\n**(9)**\nArvin Edison Water Storage District Panama Unit In-Lieu Project ($13,400,000), for constructing a total of 8.8 miles of pipeline to serve 4,816 acres of irrigated agriculture to support in-lieu groundwater recharge.\n**(10)**\nArvin Edison Water Storage District Sandrini Unit In-Lieu Project ($28,300,000), for constructing 1 mile of new canal and 21.1 miles of pipeline to serve 11,000 acres of irrigated agriculture to support in-lieu groundwater recharge.\n**(11)**\nArvin Edison Water Storage District Recovery Wells and Groundwater Quality Treatment Project ($174,000,000), for constructing 7 new wells, and providing water quality treatment for new wells and over 65 existing wells to meet treatment standards and support conjunctive use and operational flexibility of the California Aqueduct.\n**(12)**\nTulare Irrigation District Seaborn Reservoir ($23,000,000), for constructing an internal berm and inlet, outlet, and pump facilities off of the St. Johns River, and native habitat improvements.\n**(13)**\nCity of Tracy Recycled Water and Exchange Program ($10,000,000), for expanding the City of Tracy\u2019s Recycled Water Project project, including a pumping station and associated conveyance pipeline to convey recycled water to city infrastructure and to the DMC to supplement the City\u2019s CVP supply.\n**(14)**\nCity of Tracy Aquifer Storage and Recovery Program ($22,000,000), for installing 4 Aquifer Storage and Recovery wells.\n**(15)**\nWater Conservation Improvement Projects Planning Work ($1,000,000), for developing a feasibility and environmental study to analyze lining areas within the Exchange Contractors service area that are drainage impacted to generate conserved water for future implementation.\n**(16)**\nDel Puerto Canyon Reservoir Project ($1,010,000), for constructing an 82,000 acre-foot reservoir located on Del Puerto Creek, providing needed South of Delta storage to provide drought resistance for the region\u2019s agricultural and environmental water supplies, supporting disadvantaged communities, and providing public safety flood protection for the City of Patterson.\n**(17)**\nUpper Delta-Mendota Canal Reverse Flow Pumpback Project ($25,000,000), for designing and constructing 3 permanent lift stations along the DMC that will allow reverse flow of CVP and non-CVP water stored in the San Luis Reservoir (SLR) to be delivered to the CVP contractors along the northern reaches of the DMC, mitigating drought related water supply shortages for Upper DMC contractors.\n**(18)**\nLower Delta-Mendota Canal Reverse Flow Pumpback Project ($280,000,000), for planning and constructing facilities enabling reverse flow of the DMC from the Mendota Pool to O\u2019Neil Forebay and interconnecting the Central California Irrigation District Outside and Main Canals to the DMC to convey flood water into the San Luis Reservoir for storage or direct use, or exchange.\n**(19)**\nDelta-Mendota Canal Subsidence Correction Project ($830,000,000), for modifying the 116-mile-long DMC to restore the original design conveyance capacity and avoid constraints on the operation of the Central Valley Project, and addressing operational safety concerns generated by subsidence.\n**(20)**\nSan Luis Canal/California Aqueduct Subsidence Correction Project ($850,000,000), for modifying the San Luis Canal/California Aqueduct to restore the original design conveyance capacity and avoid constraints on the operation of the Central Valley Project, and addressing operational safety concerns generated by subsidence.\n**(21)**\nFriant-Kern Canal Phase II Capacity Correction Project ($730,000,000), for remaining pre-construction and construction activities for Upper and Lower Reach Capacity Correction, including embankment and lining raises, and structure modifications or replacements necessary to restore the design capacity of the from the Kings River Check to the Fifth Avenue Check, and from Reservoir Check to the Kern Check.\n**(22)**\nTurlock Irrigation Intertie Project ($800,000,000), for connecting the New Melones and Don Pedro Reservoirs.\n##### (b) Coordination\nThe Secretary shall participate in and enter into agreements and coordinate with affected Indian Tribes, the State (including subdivisions and departments of the State), and public agencies organized pursuant to State law (including irrigation entities) as necessary to carry out this Act.\n##### (c) Cost sharing\n**(1) In general**\nExcept as provided in paragraph (2)\u2014\n**(A)**\nfor the purposes of section 203 of the Reclamation Reform Act of 1982 ( 43 U.S.C. 390cc ) or section 3404(a) of the Reclamation Projects Authorization and Adjustment Act of 1992 ( Public Law 102\u2013575 ; 106 Stat. 4708), a contract or agreement entered into pursuant to this section shall not be treated as a new or amended contract; and\n**(B)**\nnone of the funds provided under this section shall be reimbursable or subject to matching or cost sharing requirements.\n**(2) Exception**\nParagraph (1) does not apply to the study described in subsection (a)(15).\n##### (d) Environmental laws\nIn providing funding for a project under this section, the Secretary shall comply with all applicable environmental laws, including\u2014\n**(1)**\nthe National Environmental Policy Act of 1969 ( 42 U.S.C. 4321 et seq. );\n**(2)**\nany obligations for fish, wildlife, or water quality protection in permits or licenses granted by a Federal agency or the State; and\n**(3)**\nany applicable Federal or State laws (including regulations).\n##### (e) Definitions\nIn this Act:\n**(1) Secretary**\nThe term Secretary means the Secretary of the Interior, acting through the Commissioner of Reclamation.\n**(2) State**\nThe term State means the State of California.\n**(3) CVP**\nThe term CVP means the Central Valley Project.\n**(4) DMC**\nThe term DMC means the Delta-Mendota Canal.",
      "versionDate": "2025-12-11",
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
        "name": "Water Resources Development",
        "updateDate": "2026-01-07T23:07:42Z"
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
      "date": "2025-12-11",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6641ih.xml"
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
      "title": "Central Valley Water Solution Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-01-03T06:53:18Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Central Valley Water Solution Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-01-03T06:53:17Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To provide for financial and technical support of certain projects related to the Central Valley Project, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-01-03T06:48:22Z"
    }
  ]
}
```
