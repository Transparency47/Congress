# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/7326?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/7326
- Title: ABODE Act
- Congress: 119
- Bill type: HR
- Bill number: 7326
- Origin chamber: House
- Introduced date: 2026-02-03
- Update date: 2026-02-25T16:47:20Z
- Update date including text: 2026-02-25T16:47:20Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2026-02-03: Introduced in House
- 2026-02-03 - IntroReferral: Introduced in House
- 2026-02-03 - IntroReferral: Introduced in House
- 2026-02-03 - IntroReferral: Referred to the House Committee on Financial Services.
- Latest action: 2026-02-03: Introduced in House

## Actions

- 2026-02-03 - IntroReferral: Introduced in House
- 2026-02-03 - IntroReferral: Introduced in House
- 2026-02-03 - IntroReferral: Referred to the House Committee on Financial Services.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-02-03",
    "latestAction": {
      "actionDate": "2026-02-03",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/7326",
    "number": "7326",
    "originChamber": "House",
    "policyArea": {
      "name": "Housing and Community Development"
    },
    "sponsors": [
      {
        "bioguideId": "F000454",
        "district": "11",
        "firstName": "Bill",
        "fullName": "Rep. Foster, Bill [D-IL-11]",
        "lastName": "Foster",
        "party": "D",
        "state": "IL"
      }
    ],
    "title": "ABODE Act",
    "type": "HR",
    "updateDate": "2026-02-25T16:47:20Z",
    "updateDateIncludingText": "2026-02-25T16:47:20Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2026-02-03",
      "committees": {
        "item": {
          "name": "Financial Services Committee",
          "systemCode": "hsba00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Financial Services.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2026-02-03",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-02-03",
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
          "date": "2026-02-03T15:02:50Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Financial Services Committee",
      "systemCode": "hsba00",
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
      "bioguideId": "P000620",
      "district": "7",
      "firstName": "Brittany",
      "fullName": "Rep. Pettersen, Brittany [D-CO-7]",
      "isOriginalCosponsor": "True",
      "lastName": "Pettersen",
      "party": "D",
      "sponsorshipDate": "2026-02-03",
      "state": "CO"
    },
    {
      "bioguideId": "F000110",
      "district": "6",
      "firstName": "Cleo",
      "fullName": "Rep. Fields, Cleo [D-LA-6]",
      "isOriginalCosponsor": "True",
      "lastName": "Fields",
      "party": "D",
      "sponsorshipDate": "2026-02-03",
      "state": "LA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7326ih.xml",
      "text": "I\n119th CONGRESS\n2d Session\nH. R. 7326\nIN THE HOUSE OF REPRESENTATIVES\nFebruary 3, 2026 Mr. Foster (for himself, Ms. Pettersen , and Mr. Fields ) introduced the following bill; which was referred to the Committee on Financial Services\nA BILL\nTo direct the Secretary of Housing and Urban Development to conduct a grant competition for the development of single- and multi-family homes, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Advancing Better Options for Dwellings Everywhere Act or the ABODE Act .\n#### 2. Competition\n##### (a) In general\nThe Secretary of Housing and Urban Development (in this section referred to as the Secretary ), in consultation with the Department of Energy and the Environmental Protection Agency, shall\u2014\n**(1)**\nconduct a grant competition to provide grants to academic organizations, nonprofit organizations, and for-profit or nonprofit mission-driven developers to develop, or rehabilitate existing, single- and multi-family homes\u2014\n**(A)**\nfor households with an income that is not more than 50 percent of the area median income; and\n**(B)**\nwith a focus on\u2014\n**(i)**\nreducing development costs;\n**(ii)**\nincreasing resiliency, energy efficiency, accessibility for individuals with disabilities; and\n**(iii)**\nselecting projects that are built to scale; and\n**(2)**\nstudy the short- and long-term savings of the resiliency and energy efficiency measures that were implemented in the homes described in paragraph (1).\n##### (b) Use of funds\nA grant awarded under this section shall be awarded at completion of the contract for building a pre-determined number of homes that abide by pre-determined resiliency and energy efficiency measures.\n##### (c) Priority\nThe Secretary shall prioritize grant awards that\u2014\n**(1)**\ndevelop or rehabilitate homes in areas with a severe affordable housing shortage;\n**(2)**\nfocus on quality, durability and maintenance costs, and neighborhood design compatibility; or\n**(3)**\ndevelop or rehabilitate homes with universal design that provides access for individuals with disabilities.\n##### (d) Report\nNot later than 2 years after the date of enactment of this Act, the Secretary shall submit to Congress a report on the competition and study conducted under this section, which shall include\u2014\n**(1)**\na description of the projects funded and completed;\n**(2)**\nthe number and sales or rental price, as applicable, of affordable houses built; and\n**(3)**\nthe results of the study described in subsection (a)(2).\n##### (e) Authorization of appropriations\nThere is authorized to be appropriated such sums as may be necessary to carry out this section.",
      "versionDate": "2026-02-03",
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
        "actionDate": "2026-02-03",
        "text": "Read twice and referred to the Committee on Banking, Housing, and Urban Affairs. (text: CR S472)"
      },
      "number": "3768",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "ABODE Act",
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
        "name": "Housing and Community Development",
        "updateDate": "2026-02-25T16:46:24Z"
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
      "date": "2026-02-03",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7326ih.xml"
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
      "title": "ABODE Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-02-19T08:38:23Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "ABODE Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-02-19T08:38:20Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Advancing Better Options for Dwellings Everywhere Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-02-19T08:38:20Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To direct the Secretary of Housing and Urban Development to conduct a grant competition for the development of single- and multi-family homes, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-02-19T08:34:00Z"
    }
  ]
}
```
