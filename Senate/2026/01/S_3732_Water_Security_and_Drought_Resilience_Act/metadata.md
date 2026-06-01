# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/3732?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/3732
- Title: Water Security and Drought Resilience Act
- Congress: 119
- Bill type: S
- Bill number: 3732
- Origin chamber: Senate
- Introduced date: 2026-01-29
- Update date: 2026-03-30T18:15:09Z
- Update date including text: 2026-03-30T18:15:09Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2026-01-29: Introduced in Senate
- 2026-01-29 - IntroReferral: Introduced in Senate
- 2026-01-29 - IntroReferral: Read twice and referred to the Committee on Energy and Natural Resources.
- 2026-03-17 - Committee: Committee on Energy and Natural Resources Subcommittee on Water and Power. Hearings held.
- Latest action: 2026-01-29: Introduced in Senate

## Actions

- 2026-01-29 - IntroReferral: Introduced in Senate
- 2026-01-29 - IntroReferral: Read twice and referred to the Committee on Energy and Natural Resources.
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
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/3732",
    "number": "3732",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Water Resources Development"
    },
    "sponsors": [
      {
        "bioguideId": "G000574",
        "district": "",
        "firstName": "Ruben",
        "fullName": "Sen. Gallego, Ruben [D-AZ]",
        "lastName": "Gallego",
        "party": "D",
        "state": "AZ"
      }
    ],
    "title": "Water Security and Drought Resilience Act",
    "type": "S",
    "updateDate": "2026-03-30T18:15:09Z",
    "updateDateIncludingText": "2026-03-30T18:15:09Z"
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
      "text": "Read twice and referred to the Committee on Energy and Natural Resources.",
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
          "date": "2026-01-29T17:54:51Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Energy and Natural Resources Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": {
              "date": "2026-03-17T14:00:24Z",
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

## API Data: cosponsors

```json
{
  "cosponsors": [
    {
      "bioguideId": "K000377",
      "firstName": "Mark",
      "fullName": "Sen. Kelly, Mark [D-AZ]",
      "isOriginalCosponsor": "True",
      "lastName": "Kelly",
      "party": "D",
      "sponsorshipDate": "2026-01-29",
      "state": "AZ"
    },
    {
      "bioguideId": "P000145",
      "firstName": "Alex",
      "fullName": "Sen. Padilla, Alex [D-CA]",
      "isOriginalCosponsor": "True",
      "lastName": "Padilla",
      "party": "D",
      "sponsorshipDate": "2026-01-29",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s3732is.xml",
      "text": "II\n119th CONGRESS\n2d Session\nS. 3732\nIN THE SENATE OF THE UNITED STATES\nJanuary 29, 2026 Mr. Gallego (for himself, Mr. Kelly , and Mr. Padilla ) introduced the following bill; which was read twice and referred to the Committee on Energy and Natural Resources\nA BILL\nTo amend the Water Infrastructure Improvements for the Nation Act to authorize assistance under the storage program, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Water Security and Drought Resilience Act .\n#### 2. Authorization to provide assistance for storage program\nSection 4007 of the Water Infrastructure Improvements for the Nation Act ( 43 U.S.C. 390b note; Public Law 114\u2013322 ) is amended by striking subsection (d) and inserting the following:\n(d) Authority To provide assistance (1) In general The Secretary of the Interior may provide financial assistance under this subtitle to carry out projects within any Reclamation State. (2) Additional project Notwithstanding subsection (i) or section 4013, any project for which a feasibility study is authorized under subsection (a)(1)(B)(i) of section 40902 of the Infrastructure Investment and Jobs Act ( 43 U.S.C. 3202 ) shall, pursuant to the construction funding requirements under subsection (a)(2) of that section, as applicable, be eligible for funding under this section. (3) Distribution among multiple reclamation states In providing financial assistance under this subtitle, the Secretary of the Interior shall ensure that the financial assistance is distributed among projects across multiple Reclamation States. .\n#### 3. Reauthorization of small storage program\n##### (a) Eligibility and selection\nSection 40903(b) of the Infrastructure Investment and Jobs Act ( 43 U.S.C. 3203(b) ) is amended\u2014\n**(1)**\nin paragraph (1), by striking subparagraph (B) and inserting the following:\n(B) Eligible projects A project shall be considered eligible for consideration for a grant under this section if the project\u2014 (i) (I) has water storage capacity of not less than 200 acre-feet and not more than 30,000 acre-feet; and (II) (aa) increases surface water or groundwater storage; or (bb) conveys water, directly or indirectly, to or from surface water or groundwater storage; or (ii) (I) has water storage capacity for recharges of not less than 200 acre-feet and not more than 150,000 acre-feet on an average annual basis over the life of the project for storage or use; and (II) (aa) increases groundwater aquifer storage; (bb) conveys water, directly or indirectly, to, or recovers water from, groundwater storage; (cc) both increases groundwater aquifer storage and conveys water, directly or indirectly, to or recovers water from groundwater storage; and (dd) stabilizes groundwater levels. ; and\n**(2)**\nby adding at the end the following:\n(6) Distribution among multiple Reclamation States In awarding grants to projects under this section, the Secretary shall ensure that grants are distributed across multiple Reclamation States. .\n##### (b) Termination of authority\nSection 40903 of the Infrastructure Investment and Jobs Act ( 43 U.S.C. 3203 ) is amended\u2014\n**(1)**\nby redesignating subsection (e) as subsection (g); and\n**(2)**\nin subsection (g) (as so redesignated), by striking 5 and inserting 10 .\n##### (c) Authorization of appropriations; effect\nSection 40903 of the Infrastructure Investment and Jobs Act ( 43 U.S.C. 3203 ) is amended by inserting after subsection (d) the following:\n(e) Authorization of appropriations There is authorized to be appropriated to the Secretary to carry out this section $20,000,000 for each of fiscal years 2027 through 2033. (f) Effect Nothing in this section\u2014 (1) supersedes or in any manner affects or conflicts with State water law, Federal water law, interstate compacts, or treaty obligations; (2) authorizes any acquisition of water by the Federal Government; or (3) supersedes or infringes on any water rights. .\n#### 4. Natural water retention and release project grants\n##### (a) Definitions\nIn this section:\n**(1) Eligible entity**\nThe term eligible entity means\u2014\n**(A)**\na State, Indian Tribe, municipality, irrigation district, water district, wastewater district, or other organization with water or power delivery authority;\n**(B)**\na State, regional, or local authority, the members of which include 1 or more organizations with water or power delivery authority; or\n**(C)**\na qualified partner.\n**(2) Natural water retention and release project**\nThe term natural water retention and release project means a project that is designed and developed to increase water availability for optimal management through aquifer recharge, floodplain retention, the alteration of the timing of runoff to allow increased utilization of existing storage facilities, or another mechanism that\u2014\n**(A)**\nuses primarily natural materials appropriate to the specific site and landscape setting;\n**(B)**\nsubstantially mimics natural riverine, wetland, ecosystem, or hydrologic processes; and\n**(C)**\nmay include multiple distributed natural water retention and release projects across a watershed.\n**(3) Qualified partner**\nThe term qualified partner means a nonprofit organization operating in a Reclamation State that is acting with the written support of an eligible entity described in subparagraph (A) or (B) of paragraph (1).\n**(4) Reclamation State**\nThe term Reclamation State has the meaning given the term in section 4014 of the Water Infrastructure Improvements for the Nation Act ( 43 U.S.C. 390b note; Public Law 114\u2013322 ).\n**(5) Secretary**\nThe term Secretary means the Secretary of the Interior, acting through the Commissioner of Reclamation.\n##### (b) Authorization for grants\nThe Secretary may award to an eligible entity a grant for a natural water retention and release project under this section, if\u2014\n**(1)**\nin the case of a natural water retention and release project that costs not more than $20,000,000, the eligible entity demonstrates that the natural water retention and release project would help optimize the storage or delivery of water in a watershed in which a Bureau of Reclamation facility is located; and\n**(2)**\nin the case of a natural water retention and release project that costs more than $20,000,000\u2014\n**(A)**\nthe requirements described in paragraph (1) have been met with respect to the natural water retention and release project; and\n**(B)**\nthe eligible entity determines, and the Secretary concurs, that\u2014\n**(i)**\nthe natural water retention and release project would produce or allow additional retention or delivery of water in a watershed in which a Bureau of Reclamation facility is located; and\n**(ii)**\nthere is a credible estimate of the quantity of the storage benefit of the natural water retention and release project during each of a wet year, a normal year, and a dry year.\n##### (c) Distribution among multiple Reclamation States\nIn providing grants for natural water retention and release projects under this section, the Secretary shall ensure that grants are distributed across multiple Reclamation States.\n##### (d) Federal cost-Share\nThe Federal share of the cost of a natural water retention and release project provided a grant under this section shall not exceed 90 percent of the total cost of the natural water retention and release project.\n##### (e) Reimbursability\nAny Federal funds provided by the Secretary to an eligible entity under this section shall be considered nonreimbursable to the United States.\n##### (f) Authorization of appropriations\nThere is authorized to be appropriated to the Secretary to carry out this section $15,000,000 for each of fiscal years 2027 through 2031.",
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
            "name": "Water resources funding",
            "updateDate": "2026-03-30T18:14:59Z"
          },
          {
            "name": "Water storage",
            "updateDate": "2026-03-30T18:14:53Z"
          },
          {
            "name": "Water use and supply",
            "updateDate": "2026-03-30T18:15:09Z"
          },
          {
            "name": "Watersheds",
            "updateDate": "2026-03-30T18:15:03Z"
          }
        ]
      },
      "policyArea": {
        "name": "Water Resources Development",
        "updateDate": "2026-02-23T21:58:20Z"
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
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s3732is.xml"
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
      "title": "Water Security and Drought Resilience Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-03-18T11:03:18Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Water Security and Drought Resilience Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-02-19T05:23:24Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend the Water Infrastructure Improvements for the Nation Act to authorize assistance under the storage program, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-02-19T05:18:36Z"
    }
  ]
}
```
