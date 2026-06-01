# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/507?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/507
- Title: Promoting Precision Agriculture Act of 2025
- Congress: 119
- Bill type: S
- Bill number: 507
- Origin chamber: Senate
- Introduced date: 2025-02-11
- Update date: 2025-12-05T21:59:47Z
- Update date including text: 2025-12-05T21:59:47Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-02-11: Introduced in Senate
- 2025-02-11 - IntroReferral: Introduced in Senate
- 2025-02-11 - IntroReferral: Read twice and referred to the Committee on Agriculture, Nutrition, and Forestry. (text: CR S861-862)
- Latest action: 2025-02-11: Introduced in Senate

## Actions

- 2025-02-11 - IntroReferral: Introduced in Senate
- 2025-02-11 - IntroReferral: Read twice and referred to the Committee on Agriculture, Nutrition, and Forestry. (text: CR S861-862)

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
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/507",
    "number": "507",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Agriculture and Food"
    },
    "sponsors": [
      {
        "bioguideId": "T000250",
        "district": "",
        "firstName": "John",
        "fullName": "Sen. Thune, John [R-SD]",
        "lastName": "Thune",
        "party": "R",
        "state": "SD"
      }
    ],
    "title": "Promoting Precision Agriculture Act of 2025",
    "type": "S",
    "updateDate": "2025-12-05T21:59:47Z",
    "updateDateIncludingText": "2025-12-05T21:59:47Z"
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
      "text": "Read twice and referred to the Committee on Agriculture, Nutrition, and Forestry. (text: CR S861-862)",
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
          "date": "2025-02-11T15:51:14Z",
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
      "bioguideId": "W000790",
      "firstName": "Raphael",
      "fullName": "Sen. Warnock, Raphael G. [D-GA]",
      "isOriginalCosponsor": "True",
      "lastName": "Warnock",
      "party": "D",
      "sponsorshipDate": "2025-02-11",
      "state": "GA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s507is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 507\nIN THE SENATE OF THE UNITED STATES\nFebruary 11, 2025 Mr. Thune (for himself and Mr. Warnock ) introduced the following bill; which was read twice and referred to the Committee on Agriculture, Nutrition, and Forestry\nA BILL\nTo enhance the participation of precision agriculture in the United States, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Promoting Precision Agriculture Act of 2025 .\n#### 2. Definitions\nIn this Act:\n**(1) Advanced wireless communications technology**\nThe term advanced wireless communications technology means advanced technology that contributes to mobile (5G or beyond) networks, next-generation Wi-Fi networks, or other future networks using other technologies, regardless of whether the network is operating on an exclusive licensed, shared licensed, or unlicensed frequency band.\n**(2) Artificial intelligence**\nThe term artificial intelligence has the meaning given the term in section 238(g) of the John S. McCain National Defense Authorization Act for Fiscal Year 2019 ( Public Law 115\u2013232 ; 10 U.S.C. note prec. 4061).\n**(3) Foreign adversary**\nThe term foreign adversary means any foreign government or foreign nongovernment person engaged in a long-term pattern or serious instances of conduct significantly adverse to the national security of the United States, or security and safety of United States persons.\n**(4) Precision agriculture**\nThe term precision agriculture means managing, tracking, or reducing crop or livestock production inputs, including seed, feed, fertilizer, chemicals, water, time, and such other inputs as the Secretary determines to be appropriate, at a heightened level of spatial and temporal granularity to improve efficiencies, reduce waste, and maintain environmental quality.\n**(5) Precision agriculture equipment**\nThe term precision agriculture equipment means any equipment or technology that directly contributes to a reduction in, or improved efficiency of, inputs used in crop or livestock production, including\u2014\n**(A)**\nglobal positioning system-based or geospatial mapping;\n**(B)**\nsatellite or aerial imagery;\n**(C)**\nyield monitors;\n**(D)**\nsoil mapping;\n**(E)**\nsensors for gathering data on crop, soil, and livestock conditions;\n**(F)**\nInternet of Things and technology that relies on edge and cloud computing;\n**(G)**\ndata management software and advanced analytics;\n**(H)**\nnetwork connectivity products and solutions, including public and private wireless networks;\n**(I)**\nglobal positioning system guidance, auto-steer systems, autonomous fleeting, and other machine-to-machine operations;\n**(J)**\nvariable rate technology for applying inputs, such as section control; and\n**(K)**\nany other technology that leads to a reduction in, or improves efficiency of, crop and livestock production inputs, which may include\u2014\n**(i)**\nseed;\n**(ii)**\nfeed;\n**(iii)**\nfertilizer;\n**(iv)**\nchemicals;\n**(v)**\nwater;\n**(vi)**\ntime;\n**(vii)**\nfuel;\n**(viii)**\nemissions; and\n**(ix)**\nsuch other inputs as the Secretary determines to be appropriate.\n**(6) Secretary**\nThe term Secretary means the Secretary of Agriculture.\n**(7) Trusted**\nThe term trusted means, with respect to a provider of advanced communications service or a supplier of communications equipment or service, that the Secretary has determined that the provider or supplier is not owned by, controlled by, or subject to the influence of, a foreign adversary.\n**(8) Voluntary consensus standards development organization**\nThe term voluntary consensus standards development organization means an organization that develops standards in a process that meets the principles for the development of voluntary consensus standards (as defined in the document of the Office of Management and Budget entitled Federal Participation in the Development and Use of Voluntary Consensus Standards and in Conformity Assessment Activities (OMB Circular A\u2013119)).\n#### 3. Purposes\nThe purposes of this Act are\u2014\n**(1)**\nto enhance the participation of precision agriculture in the United States; and\n**(2)**\nto promote United States leadership in voluntary consensus standards development organizations that set standards for precision agriculture.\n#### 4. Interconnectivity standards for precision agriculture\n##### (a) In general\nNot later than 2 years after the date of enactment of this Act, the Secretary, in consultation with the Director of the National Institute of Standards and Technology and the Federal Communications Commission, shall\u2014\n**(1)**\ndevelop voluntary, consensus-based, private sector-led interconnectivity standards, guidelines, and best practices for precision agriculture that will promote economies of scale and ease the burden of the adoption of precision agriculture; and\n**(2)**\nin carrying out paragraph (1)\u2014\n**(A)**\ncoordinate with relevant public and trusted private sector stakeholders and other relevant industry organizations, including voluntary consensus standards development organizations; and\n**(B)**\nconsult with sector-specific agencies, other appropriate agencies, and State and local governments.\n##### (b) Considerations\nThe Secretary, in carrying out subsection (a), shall, in consultation with the Director of the National Institute of Standards and Technology and the Federal Communications Commission, consider\u2014\n**(1)**\nthe evolving demands of precision agriculture;\n**(2)**\nthe connectivity needs of precision agriculture equipment;\n**(3)**\nthe cybersecurity challenges facing precision agriculture, including cybersecurity threats for agriculture producers and agriculture supply chains;\n**(4)**\nthe impact of advanced wireless communications technology on precision agriculture; and\n**(5)**\nthe impact of artificial intelligence on precision agriculture.\n#### 5. GAO assessment of precision agriculture standards\n##### (a) Study\nNot later than 1 year after the Secretary develops standards under section 4, and every 2 years thereafter for the following 8 years, the Comptroller General of the United States shall conduct a study that assesses those standards, including the extent to which those standards, as applicable\u2014\n**(1)**\nare voluntary;\n**(2)**\nwere developed in coordination with relevant industry organizations, including voluntary consensus standards development organizations; and\n**(3)**\nhave successfully encouraged the adoption of precision agriculture.\n##### (b) Report\nThe Comptroller General of the United States shall submit to the Committee on Commerce, Science, and Transportation and the Committee on Agriculture, Nutrition, and Forestry of the Senate and the Committee on Science, Space, and Technology and the Committee on Agriculture of the House of Representatives a report that summarizes the findings of each study conducted under subsection (a).",
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
        "actionDate": "2025-03-28",
        "text": "Referred to the Subcommittee on Commodity Markets, Digital Assets, and Rural Development."
      },
      "number": "1985",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Promoting Precision Agriculture Act",
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
        "updateDate": "2025-03-20T19:44:20Z"
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
          "measure-id": "id119s507",
          "measure-number": "507",
          "measure-type": "s",
          "orig-publish-date": "2025-02-11",
          "originChamber": "SENATE",
          "update-date": "2025-05-14"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "SENATE",
            "summary-id": "id119s507v00",
            "update-date": "2025-05-14"
          },
          "action-date": "2025-02-11",
          "action-desc": "Introduced in Senate",
          "summary-text": "<p><strong>Promoting Precision Agriculture Act of 2025 </strong></p><p>This bill requires the Department of Agriculture (USDA) to develop voluntary standards for precision agriculture (i.e., managing, tracking, or reducing crop or livestock production inputs, including seed, feed, fertilizer, chemicals, water, and time at a heightened level of spatial and temporal granularity to improve efficiencies, reduce waste, and maintain environmental quality).</p><p>USDA, in consultation with the National Institute of Standards and Technology (NIST) and the Federal Communications Commission (FCC), must develop voluntary, consensus-based, private sector-led interconnectivity standards, guidelines,\u00a0and best practices for precision agriculture to promote economies of scale and ease the burden of adoption. USDA must (1) coordinate with relevant public and trusted private sector stakeholders and relevant industry organizations, and (2) consult with sector-specific agencies and state and local governments.</p><p>Further, in developing the standards, USDA must, in consultation with NIST and the FCC, consider the</p><ul><li>connectivity needs of precision agriculture equipment,</li><li>cybersecurity challenges facing precision agriculture, and</li><li>impact of artificial intelligence on this area.</li></ul><p>The Government Accountability Office must periodically assess and report to Congress on the standards.</p>"
        },
        "title": "Promoting Precision Agriculture Act of 2025"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/s/BILLSUM-119s507.xml",
    "summary": {
      "actionDate": "2025-02-11",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Promoting Precision Agriculture Act of 2025 </strong></p><p>This bill requires the Department of Agriculture (USDA) to develop voluntary standards for precision agriculture (i.e., managing, tracking, or reducing crop or livestock production inputs, including seed, feed, fertilizer, chemicals, water, and time at a heightened level of spatial and temporal granularity to improve efficiencies, reduce waste, and maintain environmental quality).</p><p>USDA, in consultation with the National Institute of Standards and Technology (NIST) and the Federal Communications Commission (FCC), must develop voluntary, consensus-based, private sector-led interconnectivity standards, guidelines,\u00a0and best practices for precision agriculture to promote economies of scale and ease the burden of adoption. USDA must (1) coordinate with relevant public and trusted private sector stakeholders and relevant industry organizations, and (2) consult with sector-specific agencies and state and local governments.</p><p>Further, in developing the standards, USDA must, in consultation with NIST and the FCC, consider the</p><ul><li>connectivity needs of precision agriculture equipment,</li><li>cybersecurity challenges facing precision agriculture, and</li><li>impact of artificial intelligence on this area.</li></ul><p>The Government Accountability Office must periodically assess and report to Congress on the standards.</p>",
      "updateDate": "2025-05-14",
      "versionCode": "id119s507"
    },
    "title": "Promoting Precision Agriculture Act of 2025"
  },
  "summaries": [
    {
      "actionDate": "2025-02-11",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Promoting Precision Agriculture Act of 2025 </strong></p><p>This bill requires the Department of Agriculture (USDA) to develop voluntary standards for precision agriculture (i.e., managing, tracking, or reducing crop or livestock production inputs, including seed, feed, fertilizer, chemicals, water, and time at a heightened level of spatial and temporal granularity to improve efficiencies, reduce waste, and maintain environmental quality).</p><p>USDA, in consultation with the National Institute of Standards and Technology (NIST) and the Federal Communications Commission (FCC), must develop voluntary, consensus-based, private sector-led interconnectivity standards, guidelines,\u00a0and best practices for precision agriculture to promote economies of scale and ease the burden of adoption. USDA must (1) coordinate with relevant public and trusted private sector stakeholders and relevant industry organizations, and (2) consult with sector-specific agencies and state and local governments.</p><p>Further, in developing the standards, USDA must, in consultation with NIST and the FCC, consider the</p><ul><li>connectivity needs of precision agriculture equipment,</li><li>cybersecurity challenges facing precision agriculture, and</li><li>impact of artificial intelligence on this area.</li></ul><p>The Government Accountability Office must periodically assess and report to Congress on the standards.</p>",
      "updateDate": "2025-05-14",
      "versionCode": "id119s507"
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
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s507is.xml"
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
      "title": "Promoting Precision Agriculture Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-03-12T02:38:30Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Promoting Precision Agriculture Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-12T02:38:23Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to enhance the participation of precision agriculture in the United States, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-12T02:33:48Z"
    }
  ]
}
```
