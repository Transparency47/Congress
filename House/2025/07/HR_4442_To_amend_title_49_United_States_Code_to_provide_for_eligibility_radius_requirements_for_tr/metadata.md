# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/4442?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/4442
- Title: CHARGE Investments Act
- Congress: 119
- Bill type: HR
- Bill number: 4442
- Origin chamber: House
- Introduced date: 2025-07-16
- Update date: 2025-09-11T08:06:03Z
- Update date including text: 2025-09-11T08:06:03Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-07-16: Introduced in House
- 2025-07-16 - IntroReferral: Introduced in House
- 2025-07-16 - IntroReferral: Introduced in House
- 2025-07-16 - IntroReferral: Referred to the House Committee on Transportation and Infrastructure.
- 2025-07-17 - Committee: Referred to the Subcommittee on Railroads, Pipelines, and Hazardous Materials.
- Latest action: 2025-07-16: Introduced in House

## Actions

- 2025-07-16 - IntroReferral: Introduced in House
- 2025-07-16 - IntroReferral: Introduced in House
- 2025-07-16 - IntroReferral: Referred to the House Committee on Transportation and Infrastructure.
- 2025-07-17 - Committee: Referred to the Subcommittee on Railroads, Pipelines, and Hazardous Materials.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-07-16",
    "latestAction": {
      "actionDate": "2025-07-16",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/4442",
    "number": "4442",
    "originChamber": "House",
    "policyArea": {
      "name": "Transportation and Public Works"
    },
    "sponsors": [
      {
        "bioguideId": "C001103",
        "district": "1",
        "firstName": "Earl",
        "fullName": "Rep. Carter, Earl L. \"Buddy\" [R-GA-1]",
        "lastName": "Carter",
        "party": "R",
        "state": "GA"
      }
    ],
    "title": "CHARGE Investments Act",
    "type": "HR",
    "updateDate": "2025-09-11T08:06:03Z",
    "updateDateIncludingText": "2025-09-11T08:06:03Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-07-17",
      "committees": {
        "item": {
          "name": "Railroads, Pipelines, and Hazardous Materials Subcommittee",
          "systemCode": "hspw14"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Referred to the Subcommittee on Railroads, Pipelines, and Hazardous Materials.",
      "type": "Committee"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-07-16",
      "committees": {
        "item": {
          "name": "Transportation and Infrastructure Committee",
          "systemCode": "hspw00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Transportation and Infrastructure.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-07-16",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-07-16",
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
          "date": "2025-07-16T14:03:00Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Transportation and Infrastructure Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": {
              "date": "2025-07-17T17:04:00Z",
              "name": "Referred to"
            }
          },
          "name": "Railroads, Pipelines, and Hazardous Materials Subcommittee",
          "systemCode": "hspw14"
        }
      },
      "systemCode": "hspw00",
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
      "bioguideId": "S001211",
      "district": "4",
      "firstName": "Greg",
      "fullName": "Rep. Stanton, Greg [D-AZ-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Stanton",
      "party": "D",
      "sponsorshipDate": "2025-07-16",
      "state": "AZ"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr4442ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 4442\nIN THE HOUSE OF REPRESENTATIVES\nJuly 16, 2025 Mr. Carter of Georgia (for himself and Mr. Stanton ) introduced the following bill; which was referred to the Committee on Transportation and Infrastructure\nA BILL\nTo amend title 49, United States Code, to provide for eligibility radius requirements for transit-oriented development projects in proximity of intercity passenger rail or fixed guideway rail transit under the railroad rehabilitation and improvement program, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Catalyzing Housing and American Ready Growth and Expansion Investments Act or the CHARGE Investments Act .\n#### 2. Direct loans and loan guarantees\nSection 22402(b) of title 49, United States Code, is amended\u2014\n**(1)**\nin paragraph (1)\u2014\n**(A)**\nin subparagraph (E) by striking or at the end;\n**(B)**\nin subparagraph (F) by striking the period at the end and inserting ; or ; and\n**(C)**\nby adding at the end the following:\n(G) to finance economic development, including commercial and residential development, and related infrastructure and activities, that\u2014 (i) is physically connected to, or is within 1/4 mile of, a fixed guideway transit station that uses rail or a fixed catenary system; (ii) is not less than 2 miles from a downtown core that is not serviced by intercity passenger rail; and (iii) incorporates private investment of greater than 20 percent of total project costs. ; and\n**(2)**\nby adding at the end the following:\n(3) Extended eligibility radius (A) Intercity passenger rail transportation Notwithstanding clause (ii) of paragraph (1)(F), for a project described in such paragraph for a station serving intercity rail passenger transportation that is not located within the boundaries of a downtown core, the eligibility radius for such project shall include the nearest downtown core within a maximum 2-mile radius of such station so long as\u2014 (i) the project is located within the nearest downtown core; and (ii) there is public transportation (as defined in section 5302) between the station serving intercity rail passenger transportation and the designated location described in clause (i). (4) Definitions In this subsection: (A) Downtown core The term downtown core means an area within a municipality or region that\u2014 (i) contains the highest concentration of office square footage or employment density, as determined by the most recent comprehensive plan, zoning map, economic development plan; and (ii) is officially designated by a municipal or regional planning authority using terms such as central business district, downtown core, city center, urban core, business core, or similar terminology. (B) Intercity rail passenger transportation The term intercity rail passenger transportation has the meaning given the term in section 24102. .",
      "versionDate": "2025-07-16",
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
        "updateDate": "2025-09-10T16:59:13Z"
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
      "date": "2025-07-16",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr4442ih.xml"
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
      "title": "CHARGE Investments Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-07-29T07:53:21Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "CHARGE Investments Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-07-29T07:53:20Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Catalyzing Housing and American Ready Growth and Expansion Investments Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-07-29T07:53:20Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend title 49, United States Code, to provide for eligibility radius requirements for transit-oriented development projects in proximity of intercity passenger rail or fixed guideway rail transit under the railroad rehabilitation and improvement program, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-07-29T07:48:22Z"
    }
  ]
}
```
