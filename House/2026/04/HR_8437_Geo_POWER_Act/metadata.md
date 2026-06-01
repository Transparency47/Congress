# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/8437?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/8437
- Title: Geo POWER Act
- Congress: 119
- Bill type: HR
- Bill number: 8437
- Origin chamber: House
- Introduced date: 2026-04-22
- Update date: 2026-05-22T08:08:50Z
- Update date including text: 2026-05-22T08:08:50Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2026-04-22: Introduced in House
- 2026-04-22 - IntroReferral: Introduced in House
- 2026-04-22 - IntroReferral: Introduced in House
- 2026-04-22 - IntroReferral: Referred to the House Committee on Science, Space, and Technology.
- Latest action: 2026-04-22: Introduced in House

## Actions

- 2026-04-22 - IntroReferral: Introduced in House
- 2026-04-22 - IntroReferral: Introduced in House
- 2026-04-22 - IntroReferral: Referred to the House Committee on Science, Space, and Technology.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-04-22",
    "latestAction": {
      "actionDate": "2026-04-22",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/8437",
    "number": "8437",
    "originChamber": "House",
    "policyArea": {
      "name": "Energy"
    },
    "sponsors": [
      {
        "bioguideId": "B001323",
        "district": "",
        "firstName": "Nicholas",
        "fullName": "Rep. Begich, Nicholas J. [R-AK-At Large]",
        "lastName": "Begich",
        "party": "R",
        "state": "AK"
      }
    ],
    "title": "Geo POWER Act",
    "type": "HR",
    "updateDate": "2026-05-22T08:08:50Z",
    "updateDateIncludingText": "2026-05-22T08:08:50Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2026-04-22",
      "committees": {
        "item": {
          "name": "Science, Space, and Technology Committee",
          "systemCode": "hssy00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Science, Space, and Technology.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2026-04-22",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-04-22",
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
          "date": "2026-04-22T15:04:30Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Science, Space, and Technology Committee",
      "systemCode": "hssy00",
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
      "bioguideId": "L000590",
      "district": "3",
      "firstName": "Susie",
      "fullName": "Rep. Lee, Susie [D-NV-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Lee",
      "party": "D",
      "sponsorshipDate": "2026-04-22",
      "state": "NV"
    },
    {
      "bioguideId": "K000397",
      "district": "40",
      "firstName": "Young",
      "fullName": "Rep. Kim, Young [R-CA-40]",
      "isOriginalCosponsor": "False",
      "lastName": "Kim",
      "party": "R",
      "sponsorshipDate": "2026-04-30",
      "state": "CA"
    },
    {
      "bioguideId": "M001228",
      "district": "2",
      "firstName": "Celeste",
      "fullName": "Rep. Maloy, Celeste [R-UT-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Maloy",
      "party": "R",
      "sponsorshipDate": "2026-05-13",
      "state": "UT"
    },
    {
      "bioguideId": "H001103",
      "district": "0",
      "firstName": "Pablo",
      "fullName": "Rescom. Hern\u00e1ndez, Pablo Jose [D-PR-At Large]",
      "isOriginalCosponsor": "False",
      "lastName": "Hern\u00e1ndez",
      "middleName": "Jose",
      "party": "D",
      "sponsorshipDate": "2026-05-21",
      "state": "PR"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr8437ih.xml",
      "text": "I\n119th CONGRESS\n2d Session\nH. R. 8437\nIN THE HOUSE OF REPRESENTATIVES\nApril 22, 2026 Mr. Begich (for himself and Ms. Lee of Nevada ) introduced the following bill; which was referred to the Committee on Science, Space, and Technology\nA BILL\nTo advance next-generation geothermal electricity generation demonstration projects in new regions, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Geothermal Power Opportunity With Expanded Regions Act or the Geo POWER Act .\n#### 2. Purpose\nThe purpose of this Act is to advance next-generation geothermal demonstration projects\u2014\n**(1)**\nto accelerate the commercialization of next-generation geothermal technologies in diverse geologies and regions across the United States;\n**(2)**\nto overcome high upfront capital costs for geothermal exploration and drilling;\n**(3)**\nto generate public data to de-risk future geothermal projects in new geologies and regions; and\n**(4)**\nto catalyze geothermal demonstration projects and innovation through milestone-based financing to de-risk future geothermal projects.\n#### 3. Innovative financing for geothermal demonstration projects\nSection 615 of the Energy Independence and Security Act of 2007 ( 42 U.S.C. 17194 ) is amended\u2014\n**(1)**\nin subsection (a), by inserting the milestone-based geothermal demonstration program for projects in low permeability and impermeable reservoirs described in subsection (e) and after including ;\n**(2)**\nin subsection (d), by striking paragraph (3); and\n**(3)**\nby adding at the end the following:\n(e) Milestone-Based geothermal demonstration program (1) Definitions In this subsection: (A) Innovative financing The term innovative financing means financial instruments used to support geothermal energy project development, including transactions that the Secretary may enter into under section 646 of the Department of Energy Organization Act ( 42 U.S.C. 7256 ). (B) Program The term Program means the Milestone-Based Geothermal Demonstration Program established under paragraph (2). (2) Establishment Not later than 180 days after the date of enactment of this subsection, the Secretary shall establish a program, to be known as the Milestone-Based Geothermal Demonstration Program , to award innovative financing to geothermal projects in low-permeability and impermeable reservoirs through a competitive process based on the achievement of technical and financial milestones, prioritizing\u2014 (A) geothermal projects in regions and geologies that have limited or no geothermal electricity generation as of the date of enactment of this paragraph, including on or near Indian land (as defined in section 2601 of the Energy Policy Act of 1992 ( 25 U.S.C. 3501 )); (B) geothermal projects that support the collection and dissemination of data to characterize new geothermal resources and technologies to catalyze future private investment; (C) new geothermal electricity production facilities with aggregate electricity generation capacity potential of not less than 30 megawatts or geothermal projects that advance innovative drilling or other innovations that enable the viability of commercial-scale geothermal electricity generation of not less than 30 megawatts; and (D) projects with the potential for attracting significant private sector investment. (3) Requirements (A) Proposals In carrying out the Program, the Secretary shall request proposals for projects from project sponsors that meet the criteria described in paragraph (2). (B) Differentiation The Secretary shall award innovative financing under paragraph (2)\u2014 (i) to not less than 3 different proposals in at least 3 different States; and (ii) to not less than 3 different project sponsors. (C) Staffing The Secretary shall maintain staffing levels sufficient to administer innovative financing under paragraph (2). (4) Authority The Secretary shall carry out a project under this subsection as a milestone-based demonstration project under section 9005 of the Energy Act of 2020 ( 42 U.S.C. 7256c ). (f) Authorization of appropriations There are authorized to be appropriated to the Secretary such sums as are necessary to carry out subsections (d) and (e). .",
      "versionDate": "2026-04-22",
      "versionType": "Introduced in House"
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
        "actionDate": "2026-03-17",
        "text": "Read twice and referred to the Committee on Energy and Natural Resources."
      },
      "number": "4116",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Geo POWER Act",
      "type": "S"
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
        "updateDate": "2026-05-07T20:55:23Z"
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
      "date": "2026-04-22",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr8437ih.xml"
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
      "title": "Geo POWER Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-04-28T08:53:25Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Geo POWER Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-04-28T08:53:24Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Geothermal Power Opportunity With Expanded Regions Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-04-28T08:53:24Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To advance next-generation geothermal electricity generation demonstration projects in new regions, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-04-28T08:48:36Z"
    }
  ]
}
```
