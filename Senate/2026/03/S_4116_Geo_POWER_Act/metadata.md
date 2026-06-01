# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/4116?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/4116
- Title: Geo POWER Act
- Congress: 119
- Bill type: S
- Bill number: 4116
- Origin chamber: Senate
- Introduced date: 2026-03-17
- Update date: 2026-05-07T20:55:16Z
- Update date including text: 2026-05-07T20:55:16Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2026-03-17: Introduced in Senate
- 2026-03-17 - IntroReferral: Introduced in Senate
- 2026-03-17 - IntroReferral: Read twice and referred to the Committee on Energy and Natural Resources.
- Latest action: 2026-03-17: Introduced in Senate

## Actions

- 2026-03-17 - IntroReferral: Introduced in Senate
- 2026-03-17 - IntroReferral: Read twice and referred to the Committee on Energy and Natural Resources.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-03-17",
    "latestAction": {
      "actionDate": "2026-03-17",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/4116",
    "number": "4116",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Energy"
    },
    "sponsors": [
      {
        "bioguideId": "H000273",
        "district": "",
        "firstName": "John",
        "fullName": "Sen. Hickenlooper, John W. [D-CO]",
        "lastName": "Hickenlooper",
        "party": "D",
        "state": "CO"
      }
    ],
    "title": "Geo POWER Act",
    "type": "S",
    "updateDate": "2026-05-07T20:55:16Z",
    "updateDateIncludingText": "2026-05-07T20:55:16Z"
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
      "actionDate": "2026-03-17",
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
          "date": "2026-03-17T19:25:08Z",
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
      "bioguideId": "D000618",
      "firstName": "Steve",
      "fullName": "Sen. Daines, Steve [R-MT]",
      "isOriginalCosponsor": "True",
      "lastName": "Daines",
      "party": "R",
      "sponsorshipDate": "2026-03-17",
      "state": "MT"
    },
    {
      "bioguideId": "P000145",
      "firstName": "Alex",
      "fullName": "Sen. Padilla, Alex [D-CA]",
      "isOriginalCosponsor": "True",
      "lastName": "Padilla",
      "party": "D",
      "sponsorshipDate": "2026-03-17",
      "state": "CA"
    },
    {
      "bioguideId": "C001114",
      "firstName": "John",
      "fullName": "Sen. Curtis, John R. [R-UT]",
      "isOriginalCosponsor": "True",
      "lastName": "Curtis",
      "party": "R",
      "sponsorshipDate": "2026-03-17",
      "state": "UT"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s4116is.xml",
      "text": "II\n119th CONGRESS\n2d Session\nS. 4116\nIN THE SENATE OF THE UNITED STATES\nMarch 17, 2026 Mr. Hickenlooper (for himself, Mr. Daines , Mr. Padilla , and Mr. Curtis ) introduced the following bill; which was read twice and referred to the Committee on Energy and Natural Resources\nA BILL\nTo advance next-generation geothermal electricity generation demonstration projects in new regions, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Geothermal Power Opportunity With Expanded Regions Act or the Geo POWER Act .\n#### 2. Purpose\nThe purpose of this Act is to advance next-generation geothermal demonstration projects\u2014\n**(1)**\nto accelerate the commercialization of next-generation geothermal technologies in diverse geologies and regions across the United States;\n**(2)**\nto overcome high upfront capital costs for geothermal exploration and drilling;\n**(3)**\nto generate public data to de-risk future geothermal projects in new geologies and regions; and\n**(4)**\nto catalyze geothermal demonstration projects and innovation through milestone-based financing to de-risk future geothermal projects.\n#### 3. Innovative financing for geothermal demonstration projects\nSection 615 of the Energy Independence and Security Act of 2007 ( 42 U.S.C. 17194 ) is amended\u2014\n**(1)**\nin subsection (a), by inserting the milestone-based geothermal demonstration program for projects in low permeability and impermeable reservoirs described in subsection (e) and after including ;\n**(2)**\nin subsection (d), by striking paragraph (3); and\n**(3)**\nby adding at the end the following:\n(e) Milestone-Based geothermal demonstration program (1) Definitions In this subsection: (A) Innovative financing The term innovative financing means financial instruments used to support geothermal energy project development, including transactions that the Secretary may enter into under section 646 of the Department of Energy Organization Act ( 42 U.S.C. 7256 ). (B) Program The term Program means the Milestone-Based Geothermal Demonstration Program established under paragraph (2). (2) Establishment Not later than 180 days after the date of enactment of this subsection, the Secretary shall establish a program, to be known as the Milestone-Based Geothermal Demonstration Program , to award innovative financing to geothermal projects in low-permeability and impermeable reservoirs through a competitive process based on the achievement of technical and financial milestones, prioritizing\u2014 (A) geothermal projects in regions and geologies that have limited or no geothermal electricity generation as of the date of enactment of this paragraph, including on or near Indian land (as defined in section 2601 of the Energy Policy Act of 1992 ( 25 U.S.C. 3501 )); (B) geothermal projects that support the collection and dissemination of data to characterize new geothermal resources and technologies to catalyze future private investment; (C) new geothermal electricity production facilities with aggregate electricity generation capacity potential of not less than 30 megawatts or geothermal projects that advance innovative drilling or other innovations that enable the viability of commercial-scale geothermal electricity generation of not less than 30 megawatts; and (D) projects with the potential for attracting significant private sector investment. (3) Requirements (A) Proposals In carrying out the Program, the Secretary shall request proposals for projects from project sponsors that meet the criteria described in paragraph (2). (B) Differentiation The Secretary shall award innovative financing under paragraph (2)\u2014 (i) to not less than 3 different proposals in at least 3 different States; and (ii) to not less than 3 different project sponsors. (C) Staffing The Secretary shall maintain staffing levels sufficient to administer innovative financing under paragraph (2). (4) Authority The Secretary shall carry out a project under this subsection as a milestone-based demonstration project under section 9005 of the Energy Act of 2020 ( 42 U.S.C. 7256c ). (f) Authorization of appropriations There are authorized to be appropriated to the Secretary such sums as are necessary to carry out subsections (d) and (e). .",
      "versionDate": "2026-03-17",
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
        "actionDate": "2026-04-22",
        "text": "Referred to the House Committee on Science, Space, and Technology."
      },
      "number": "8437",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Geo POWER Act",
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
        "name": "Energy",
        "updateDate": "2026-03-31T12:06:24Z"
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
      "date": "2026-03-17",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s4116is.xml"
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
      "title": "Geo POWER Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-03-25T03:53:22Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Geo POWER Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-03-25T03:53:21Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Geothermal Power Opportunity With Expanded Regions Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-03-25T03:53:21Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to advance next-generation geothermal electricity generation demonstration projects in new regions, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-03-25T03:48:36Z"
    }
  ]
}
```
