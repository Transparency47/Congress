# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/3016?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/3016
- Title: Advancing Research in Nuclear Fuel Recycling Act of 2025
- Congress: 119
- Bill type: S
- Bill number: 3016
- Origin chamber: Senate
- Introduced date: 2025-10-16
- Update date: 2026-03-24T12:48:03Z
- Update date including text: 2026-03-24T12:48:03Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-10-16: Introduced in Senate
- 2025-10-16 - IntroReferral: Introduced in Senate
- 2025-10-16 - IntroReferral: Read twice and referred to the Committee on Energy and Natural Resources.
- Latest action: 2025-10-16: Introduced in Senate

## Actions

- 2025-10-16 - IntroReferral: Introduced in Senate
- 2025-10-16 - IntroReferral: Read twice and referred to the Committee on Energy and Natural Resources.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-10-16",
    "latestAction": {
      "actionDate": "2025-10-16",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/3016",
    "number": "3016",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Energy"
    },
    "sponsors": [
      {
        "bioguideId": "C001098",
        "district": "",
        "firstName": "Ted",
        "fullName": "Sen. Cruz, Ted [R-TX]",
        "lastName": "Cruz",
        "party": "R",
        "state": "TX"
      }
    ],
    "title": "Advancing Research in Nuclear Fuel Recycling Act of 2025",
    "type": "S",
    "updateDate": "2026-03-24T12:48:03Z",
    "updateDateIncludingText": "2026-03-24T12:48:03Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-10-16",
      "committees": {
        "item": {
          "name": "Energy and Natural Resources Committee",
          "systemCode": "sseg00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Energy and Natural Resources.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-10-16",
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
          "date": "2025-10-16T18:47:02Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Energy and Natural Resources Committee",
      "systemCode": "sseg00",
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
      "bioguideId": "H001046",
      "firstName": "Martin",
      "fullName": "Sen. Heinrich, Martin [D-NM]",
      "isOriginalCosponsor": "True",
      "lastName": "Heinrich",
      "party": "D",
      "sponsorshipDate": "2025-10-16",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s3016is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 3016\nIN THE SENATE OF THE UNITED STATES\nOctober 16, 2025 Mr. Cruz (for himself and Mr. Heinrich ) introduced the following bill; which was read twice and referred to the Committee on Energy and Natural Resources\nA BILL\nTo require the Secretary of Energy to study new technologies and opportunities for recycling spent nuclear fuel.\n#### 1. Short title\nThis Act may be cited as the Advancing Research in Nuclear Fuel Recycling Act of 2025 .\n#### 2. Study on new technologies to recycle spent nuclear fuel\n##### (a) Definitions\nIn this section:\n**(1) National laboratory**\nThe term National Laboratory has the meaning given the term in section 2 of the Energy Policy Act of 2005 ( 42 U.S.C. 15801 ).\n**(2) Nuclear waste**\nThe term nuclear waste means spent nuclear fuel and high-level radioactive waste (as defined in section 2 of the Nuclear Waste Policy Act of 1982 ( 42 U.S.C. 10101 )).\n**(3) Recycling**\nThe term recycling means the recovery of valuable radionuclides, including fissile materials, from nuclear waste, and any subsequent processes, such as enrichment and fuel fabrication, necessary for reuse in nuclear reactors or other commercial applications.\n**(4) Secretary**\nThe term Secretary means the Secretary of Energy.\n**(5) Spent nuclear fuel**\nThe term spent nuclear fuel has the meaning given the term in section 2 of the Nuclear Waste Policy Act of 1982 ( 42 U.S.C. 10101 ).\n##### (b) Study\nNot later than 90 days after the date of enactment of this Act, the Secretary, acting through the Assistant Secretary for Nuclear Energy, shall carry out a study\u2014\n**(1)**\nto analyze the practicability, potential benefits, costs, and risks, including proliferation, of using dedicated recycling facilities to convert spent nuclear fuel, including spent high-assay low-enriched uranium fuel, into useable nuclear fuels, such as those for\u2014\n**(A)**\ncommercial light water reactors;\n**(B)**\nadvanced nuclear reactors; and\n**(C)**\nmedical, space-based, advanced-battery, and other non-reactor applications, as determined by the Secretary;\n**(2)**\n**(A)**\nto analyze the practicability, potential benefits, costs, and risks of recycling spent nuclear fuel, which is taken from temporary storage sites throughout the United States, and using it as fuel or input for advanced nuclear reactors, existing reactors, or commercial applications;\n**(B)**\nto compare such practicability, potential benefits, costs, and risks of recycling spent nuclear fuel with the practicability, potential benefits, costs, and risks of the once-through fuel cycle, including temporary and permanent storage requirements; and\n**(C)**\nto analyze the practicability, potential benefits, costs, and risks of aqueous (such as PUREX and the derivatives of PUREX) recycling processes with the practicability, potential benefits, costs, and risk of non-aqueous (such as pyro-electrochemistry) recycling processes;\n**(3)**\nto analyze the technical and economic feasibility of utilizing nuclear waste processing to extract certain isotopes needed for domestic and international use, including medical, industrial, space-based power source, and advanced-battery applications;\n**(4)**\nto analyze the practicability, potential benefits, costs, risks, and potential approaches for coupling or collocating recycling facilities with other pertinent facilities, such as advanced nuclear reactors (that can use the recycled fuel), interim storage, and fuel-fabrication facilities, including through\u2014\n**(A)**\nrelevant analyses, such as capital and operating cost estimates, public-private partnerships to encourage investment, infrastructure requirements, timeline to full-scale commercial deployment, and distinguishing characteristics or requirements of such facilities;\n**(B)**\ninput from interested private technology developers and relevant assumptions regarding cost; and\n**(C)**\ncomparison with the practicability, potential benefits, costs, and risks of the once-through fuel cycle, including temporary and permanent storage requirements;\n**(5)**\nto identify parties, including individuals, communities, businesses, and local and Tribal governments, that are impacted economically, or through health, safety, or environmental risks, by the current practice of indefinite temporary storage of spent nuclear fuel, and assess potential risks and benefits for those parties should spent nuclear fuel be removed from their sites for the purposes of nuclear waste recycling;\n**(6)**\nto assess different approaches for siting and sizing nuclear waste recycling facilities, including a centralized national facility, regional facilities, on-site facilities where spent nuclear fuel is currently stored, and on-site facilities where newly recycled fuel can be used by an on-site reactor, and recommend one or more approaches that consider environmental, transportation, infrastructure, capital, and other risks;\n**(7)**\nto identify tracking and accountability methods for new recycled fuel and radioactive waste streams for byproducts of the recycling process;\n**(8)**\n**(A)**\nto identify any regulatory gaps related to nuclear waste management and recycling, including accuracy and consistency of relevant definitions for radioactive waste (including high-level radioactive waste , spent nuclear fuel , low-level radioactive waste , reprocessing , recycling , and vitrification ) and classifications of radioactive waste that exist in Federal law on the date of enactment of this Act;\n**(B)**\nto compare such definitions to those used by other nations that manage radioactive waste; and\n**(C)**\nto make recommendations for modernizing such definitions; and\n**(9)**\nto evaluate\u2014\n**(A)**\npotential Federal and State-level policy changes to support development and deployment of recycling and waste-utilizing reactor technologies; and\n**(B)**\nimpacts of spent nuclear fuel recycling on requirements for domestic nuclear waste storage.\n##### (c) Report\nNot later than 1 year after the date of enactment of this Act, the Secretary, acting through the Assistant Secretary for Nuclear Energy, shall submit to the Committee on Energy and Natural Resources of the Senate, the Committee on Energy and Commerce of the House of Representatives, the Committee on Science, Space, and Technology of the House of Representatives, and the Committee on Natural Resources of the House of Representatives, a report that complies with each of the following:\n**(1)**\nDescribes the results of the study carried out under subsection (b).\n**(2)**\nIs released to the public.\n**(3)**\nTotals not more than 120 pages (excluding Front Matter, References, and Appendices) written and formatted to facilitate review by a nonspecialist readership, including the following sections:\n**(A)**\nA Front Matter section that includes a cover page with identifying information, tables of contents, figures, and tables.\n**(B)**\nAn Executive Summary section.\n**(C)**\nAn Introductory section that includes a historical overview that also explains why recycling is not performed in the United States today, such as economic, political, or technological obstacles.\n**(D)**\nResults and Findings sections that summarize the results and findings of the study carried out under subsection (b).\n**(E)**\nA Key Remaining Challenges and Barriers section that identifies key technical and nontechnical (such as economic) challenges and barriers that need to be addressed to enable scale-up and commercial adoption of spent nuclear fuel recycling, with preference given to secure, proliferation resistant, environmentally safe, and economical recycling methods.\n**(F)**\nA Policy Recommendations section that\u2014\n**(i)**\nlists policy recommendations to address remaining technical and nontechnical (such as economic) challenges and barriers to enable scale-up and commercial adoption of spent nuclear fuel recycling, including with government support;\n**(ii)**\ncontrasts the potential benefits and risks of each policy; and\n**(iii)**\ncompares benefits to current or past policies.\n**(G)**\nAn Other section in which other relevant information may be added.\n**(H)**\nA References section.\n**(I)**\nAn Appendices section.",
      "versionDate": "2025-10-16",
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
        "name": "Energy",
        "updateDate": "2025-12-08T16:34:39Z"
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
      "date": "2025-10-16",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s3016is.xml"
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
      "title": "Advancing Research in Nuclear Fuel Recycling Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-10-23T02:53:15Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Advancing Research in Nuclear Fuel Recycling Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-10-23T02:53:14Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to require the Secretary of Energy to study new technologies and opportunities for recycling spent nuclear fuel.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-10-23T02:48:16Z"
    }
  ]
}
```
