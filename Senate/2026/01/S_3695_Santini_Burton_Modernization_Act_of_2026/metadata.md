# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/3695?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/3695
- Title: Santini-Burton Modernization Act of 2026
- Congress: 119
- Bill type: S
- Bill number: 3695
- Origin chamber: Senate
- Introduced date: 2026-01-27
- Update date: 2026-03-24T12:48:03Z
- Update date including text: 2026-03-24T12:48:03Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2026-01-27: Introduced in Senate
- 2026-01-27 - IntroReferral: Introduced in Senate
- 2026-01-27 - IntroReferral: Read twice and referred to the Committee on Energy and Natural Resources.
- 2026-02-12 - Committee: Committee on Energy and Natural Resources Subcommittee on Public Lands, Forests, and Mining. Hearings held.
- Latest action: 2026-01-27: Introduced in Senate

## Actions

- 2026-01-27 - IntroReferral: Introduced in Senate
- 2026-01-27 - IntroReferral: Read twice and referred to the Committee on Energy and Natural Resources.
- 2026-02-12 - Committee: Committee on Energy and Natural Resources Subcommittee on Public Lands, Forests, and Mining. Hearings held.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-01-27",
    "latestAction": {
      "actionDate": "2026-01-27",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/3695",
    "number": "3695",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Public Lands and Natural Resources"
    },
    "sponsors": [
      {
        "bioguideId": "C001113",
        "district": "",
        "firstName": "Catherine",
        "fullName": "Sen. Cortez Masto, Catherine [D-NV]",
        "lastName": "Cortez Masto",
        "party": "D",
        "state": "NV"
      }
    ],
    "title": "Santini-Burton Modernization Act of 2026",
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
      "actionDate": "2026-02-12",
      "committees": {
        "item": {
          "name": "Public Lands, Forests, and Mining Subcommittee",
          "systemCode": "sseg03"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Committee on Energy and Natural Resources Subcommittee on Public Lands, Forests, and Mining. Hearings held.",
      "type": "Committee"
    },
    {
      "actionDate": "2026-01-27",
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
      "actionDate": "2026-01-27",
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
          "date": "2026-01-27T21:50:06Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Energy and Natural Resources Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": {
              "date": "2026-02-12T15:00:44Z",
              "name": "Hearings By (subcommittee)"
            }
          },
          "name": "Public Lands, Forests, and Mining Subcommittee",
          "systemCode": "sseg03"
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
      "bioguideId": "R000608",
      "firstName": "Jacky",
      "fullName": "Sen. Rosen, Jacky [D-NV]",
      "isOriginalCosponsor": "True",
      "lastName": "Rosen",
      "party": "D",
      "sponsorshipDate": "2026-01-27",
      "state": "NV"
    },
    {
      "bioguideId": "P000145",
      "firstName": "Alex",
      "fullName": "Sen. Padilla, Alex [D-CA]",
      "isOriginalCosponsor": "True",
      "lastName": "Padilla",
      "party": "D",
      "sponsorshipDate": "2026-01-27",
      "state": "CA"
    },
    {
      "bioguideId": "S001150",
      "firstName": "Adam",
      "fullName": "Sen. Schiff, Adam B. [D-CA]",
      "isOriginalCosponsor": "True",
      "lastName": "Schiff",
      "middleName": "B.",
      "party": "D",
      "sponsorshipDate": "2026-01-27",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s3695is.xml",
      "text": "II\n119th CONGRESS\n2d Session\nS. 3695\nIN THE SENATE OF THE UNITED STATES\nJanuary 27, 2026 Ms. Cortez Masto (for herself, Ms. Rosen , Mr. Padilla , and Mr. Schiff ) introduced the following bill; which was read twice and referred to the Committee on Energy and Natural Resources\nA BILL\nTo amend Public Law 96\u2013586 to modernize the authority of the Forest Service to acquire and administer land under that Act, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Santini-Burton Modernization Act of 2026 .\n#### 2. Environmentally sensitive land in the Lake Tahoe Basin\n##### (a) Findings; purpose\nSection 1 of Public Law 96\u2013586 (94 Stat. 3381) (commonly known as the Santini-Burton Act ) is amended\u2014\n**(1)**\nin subsection (a)\u2014\n**(A)**\nin paragraph (6), by striking and at the end;\n**(B)**\nin paragraph (7), by striking the period at the end and inserting ; and ; and\n**(C)**\nby adding at the end the following:\n(8) the Lake Tahoe Basin is the homeland of the Washoe Tribe of Nevada and California, but that Tribe owns less than 0.5 percent of the land in the Lake Tahoe Basin, and that limited land ownership and the presence of that land in the Lake Tahoe Basin hamper the ability of the Washoe Tribe of Nevada and California to provide access and cultural resources for the members of that Tribe. ; and\n**(2)**\nin subsection (b), by inserting and management after acquisition .\n##### (b) Acquisitions; land management\nSection 3 of Public Law 96\u2013586 (94 Stat. 3383; 114 Stat. 2357; 130 Stat. 1790) (commonly known as the Santini-Burton Act ) is amended\u2014\n**(1)**\nin subsection (a)(3), in the first sentence, by inserting the Washoe Tribe of Nevada and California, and after local government agencies, ;\n**(2)**\nin subsection (b)\u2014\n**(A)**\nin paragraph (1)\u2014\n**(i)**\nby striking Land and inserting the following:\n(A) National Forest System Except as provided in subparagraph (B), land ;\n**(ii)**\nin subparagraph (A) (as so designated), by striking United States National Forest System; except that the Secretary and inserting the following: \u201cNational Forest System.\n(B) Transfers (i) In general The Secretary ; and\n**(iii)**\nin subparagraph (B) (as so designated)\u2014\n**(I)**\nin clause (i)\u2014\n**(aa)**\nby striking lands each place it appears and inserting land ;\n**(bb)**\nby striking which are unsuitable and inserting acquired under this section that is unsuitable ; and\n**(cc)**\nby inserting or to the Washoe Tribe of Nevada and California after local government ; and\n**(II)**\nby adding at the end the following:\n(ii) Funding Amounts made available to carry out this section may be used for the administrative costs of transfers of land and interests in land under this subsection. ; and\n**(B)**\nby adding at the end the following:\n(7) Land management (A) Acquired land Notwithstanding any other provision of law, funds appropriated pursuant to this Act for the purpose of the acquisition of land and interests in land under this section may be used by the Secretary of Agriculture, acting through the Chief of the Forest Service, for\u2014 (i) land management activities on land acquired under this section within the Lake Tahoe Basin; and (ii) land management activities on National Forest System land within the boundaries of the Lake Tahoe Basin Management Unit. (B) Transferred land Notwithstanding any other provision of law, the Secretary of Agriculture may transfer funds made available pursuant to this Act for the purpose of the acquisition of land and interests in land under this section to appropriate units of State or local government or to the Washoe Tribe of Nevada and California to carry out land management activities on land acquired under this section and transferred to that unit of State or local government or to that Tribe. (C) Included land management activities Land management activities that may be carried out under subparagraphs (A) and (B) shall include activities for the purposes of\u2014 (i) maintaining forest health; (ii) maintaining the wildland-urban interface (as defined in section 101 of the Healthy Forests Restoration Act of 2003 ( 16 U.S.C. 6511 )); (iii) maintaining water quality; (iv) preventing and mitigating environmental impacts due to recreational use; (v) preserving cultural sites and indigenous management practices; and (vi) scientific research to support decisions relating to land management activities described in clauses (i) through (v). (D) Partnerships (i) Federal agencies The Secretary of Agriculture, acting through the Chief of the Forest Service, may enter into partnerships with the heads of applicable Federal agencies to carry out land management activities under subparagraph (A). (ii) Other partnerships Notwithstanding any other provision of law, the Secretary of Agriculture, acting through the Chief of the Forest Service, may enter into partnerships with, and transfer funds appropriated pursuant to this Act for the purpose of the acquisition of land and interests in land under this section to, appropriate units of State or local government, the Tahoe Regional Planning Agency, or the Washoe Tribe of Nevada and California to develop and implement the land management activities described in subparagraph (C) and projects to provide public access to\u2014 (I) land in the Lake Tahoe Basin acquired under this section; (II) land with a nexus to Federal land in the Lake Tahoe Basin or the shoreline of Lake Tahoe; or (III) land in the Lake Tahoe Basin that is of cultural significance to the Washoe Tribe of Nevada and California. (E) Spending plan (i) In general Not later than March 15 of each fiscal year, the Secretary of Agriculture, acting through the Forest Supervisor of the Lake Tahoe Basin Management Unit, shall develop a spending plan for activities under this paragraph for the next fiscal year consistent with the priorities of the Lake Tahoe Environmental Improvement Program. (ii) Consultation In developing the spending plan under clause (i), the Secretary of Agriculture, acting through the Forest Supervisor of the Lake Tahoe Basin Management Unit, shall consult with\u2014 (I) the Tahoe Regional Planning Agency; (II) the States of California and Nevada; (III) the Washoe Tribe of Nevada and California; and (IV) appropriate units of local government. (iii) Criteria The ranking of management activities in the spending plan developed under clause (i) shall be based on\u2014 (I) the potential to significantly contribute to the achievement and maintenance of the environmental threshold carrying capacities adopted by the Tahoe Regional Planning Agency and the Tahoe Regional Planning Compact ( Public Law 96\u2013551 ; 94 Stat. 3233); (II) the 4-year threshold carrying capacity evaluation; (III) the ability to measure progress or success of the management activity; (IV) the ability of the management activity to have multiple benefits; (V) the ability of the management activity to leverage other contributions; (VI) inclusion on the 5-year priority list for the Lake Tahoe Environmental Improvement Program; and (VII) whether there is stakeholder support for the management activity. (iv) Funding for administration; availability Any funds made available under this paragraph and allocated under the spending plan developed under clause (i)\u2014 (I) may be used for administrative costs of carrying out the spending plan; and (II) shall remain available until expended. (F) Maintenance of funding Notwithstanding any other provision of law, any funds made available under this paragraph shall supplement, and not supplant, any other amounts available to the Secretary of Agriculture for expenditure in the Lake Tahoe Basin and any other amounts made available by Congress. (G) Consideration as non-Federal matching funds Notwithstanding any other provision of law, any funds transferred under this paragraph to the Washoe Tribe of Nevada and California, an appropriate unit of State or local government, or the Tahoe Regional Planning Agency shall be considered to be non-Federal matching funds for purposes of any other provision of Federal law. ;\n**(3)**\nin subsection (c)(4)\u2014\n**(A)**\nin subparagraph (A), by striking and at the end;\n**(B)**\nby redesignating subparagraph (B) as subparagraph (C); and\n**(C)**\nby inserting after subparagraph (A) the following:\n(B) Lake Tahoe Basin Management Unit means the land area included in the management unit created by the Forest Service in 1973; and ;\n**(4)**\nby redesignating subsection (g) as subsection (h); and\n**(5)**\nby inserting after subsection (f) the following:\n(g) Acquisition and management of land of cultural significance to the Washoe Tribe of Nevada and California Notwithstanding any other provision of law, the Secretary of Agriculture, acting through the Chief of the Forest Service, may transfer funds appropriated pursuant to this Act for the purpose of the acquisition of land and interests in land under this section to the Washoe Tribe of Nevada and California to acquire and manage land of cultural significance to that Tribe in the Lake Tahoe Basin for the purposes of preservation, access, and land management. .",
      "versionDate": "2026-01-27",
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
        "actionDate": "2026-01-27",
        "text": "Referred to the House Committee on Natural Resources."
      },
      "number": "7255",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Santini-Burton Modernization Act of 2026",
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
      "legislativeSubjects": {
        "item": [
          {
            "name": "California",
            "updateDate": "2026-02-27T18:03:29Z"
          },
          {
            "name": "Intergovernmental relations",
            "updateDate": "2026-02-27T18:03:38Z"
          },
          {
            "name": "Land transfers",
            "updateDate": "2026-02-27T18:03:20Z"
          },
          {
            "name": "Land use and conservation",
            "updateDate": "2026-02-27T18:03:25Z"
          },
          {
            "name": "Nevada",
            "updateDate": "2026-02-27T18:03:33Z"
          }
        ]
      },
      "policyArea": {
        "name": "Public Lands and Natural Resources",
        "updateDate": "2026-02-18T19:53:22Z"
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
      "date": "2026-01-27",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s3695is.xml"
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
      "title": "Santini-Burton Modernization Act of 2026",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-02-13T11:58:28Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Santini-Burton Modernization Act of 2026",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-02-13T04:43:23Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend Public Law 96-586 to modernize the authority of the Forest Service to acquire and administer land under that Act, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-02-13T04:18:31Z"
    }
  ]
}
```
