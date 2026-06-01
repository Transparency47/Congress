# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/6256?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/6256
- Title: Floodplain Enhancement and Recovery Act
- Congress: 119
- Bill type: HR
- Bill number: 6256
- Origin chamber: House
- Introduced date: 2025-11-21
- Update date: 2026-04-17T08:07:26Z
- Update date including text: 2026-04-17T08:07:26Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-11-21: Introduced in House
- 2025-11-21 - IntroReferral: Introduced in House
- 2025-11-21 - IntroReferral: Introduced in House
- 2025-11-21 - IntroReferral: Referred to the House Committee on Financial Services.
- Latest action: 2025-11-21: Introduced in House

## Actions

- 2025-11-21 - IntroReferral: Introduced in House
- 2025-11-21 - IntroReferral: Introduced in House
- 2025-11-21 - IntroReferral: Referred to the House Committee on Financial Services.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-11-21",
    "latestAction": {
      "actionDate": "2025-11-21",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/6256",
    "number": "6256",
    "originChamber": "House",
    "policyArea": {
      "name": "Finance and Financial Sector"
    },
    "sponsors": [
      {
        "bioguideId": "D000634",
        "district": "2",
        "firstName": "Troy",
        "fullName": "Rep. Downing, Troy [R-MT-2]",
        "lastName": "Downing",
        "party": "R",
        "state": "MT"
      }
    ],
    "title": "Floodplain Enhancement and Recovery Act",
    "type": "HR",
    "updateDate": "2026-04-17T08:07:26Z",
    "updateDateIncludingText": "2026-04-17T08:07:26Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-11-21",
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
      "actionDate": "2025-11-21",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-11-21",
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
          "date": "2025-11-21T14:05:10Z",
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
      "bioguideId": "B001326",
      "district": "5",
      "firstName": "Janelle",
      "fullName": "Rep. Bynum, Janelle S. [D-OR-5]",
      "isOriginalCosponsor": "True",
      "lastName": "Bynum",
      "middleName": "S.",
      "party": "D",
      "sponsorshipDate": "2025-11-21",
      "state": "OR"
    },
    {
      "bioguideId": "S001213",
      "district": "1",
      "firstName": "Bryan",
      "fullName": "Rep. Steil, Bryan [R-WI-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Steil",
      "party": "R",
      "sponsorshipDate": "2025-11-21",
      "state": "WI"
    },
    {
      "bioguideId": "G000600",
      "district": "3",
      "firstName": "Marie",
      "fullName": "Rep. Perez, Marie Gluesenkamp [D-WA-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Perez",
      "middleName": "Gluesenkamp",
      "party": "D",
      "sponsorshipDate": "2025-11-21",
      "state": "WA"
    },
    {
      "bioguideId": "G000576",
      "district": "6",
      "firstName": "Glenn",
      "fullName": "Rep. Grothman, Glenn [R-WI-6]",
      "isOriginalCosponsor": "False",
      "lastName": "Grothman",
      "party": "R",
      "sponsorshipDate": "2026-02-12",
      "state": "WI"
    },
    {
      "bioguideId": "V000136",
      "district": "2",
      "firstName": "Gabe",
      "fullName": "Rep. Vasquez, Gabe [D-NM-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Vasquez",
      "party": "D",
      "sponsorshipDate": "2026-03-16",
      "state": "NM"
    },
    {
      "bioguideId": "W000829",
      "district": "8",
      "firstName": "Tony",
      "fullName": "Rep. Wied, Tony [R-WI-8]",
      "isOriginalCosponsor": "False",
      "lastName": "Wied",
      "party": "R",
      "sponsorshipDate": "2026-03-16",
      "state": "WI"
    },
    {
      "bioguideId": "V000135",
      "district": "3",
      "firstName": "Derrick",
      "fullName": "Rep. Van Orden, Derrick [R-WI-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Van Orden",
      "party": "R",
      "sponsorshipDate": "2026-04-13",
      "state": "WI"
    },
    {
      "bioguideId": "J000298",
      "district": "7",
      "firstName": "Pramila",
      "fullName": "Rep. Jayapal, Pramila [D-WA-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Jayapal",
      "party": "D",
      "sponsorshipDate": "2026-04-16",
      "state": "WA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6256ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 6256\nIN THE HOUSE OF REPRESENTATIVES\nNovember 21, 2025 Mr. Downing (for himself, Ms. Bynum , Mr. Steil , and Ms. Perez ) introduced the following bill; which was referred to the Committee on Financial Services\nA BILL\nTo amend the Homeowner Flood Insurance Affordability Act of 2014 to address ecosystem restoration projects, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Floodplain Enhancement and Recovery Act .\n#### 2. Ecosystem restoration projects\n##### (a) In general\nSection 22 of the Homeowner Flood Insurance Affordability Act of 2014 ( 42 U.S.C. 4101e ) is amended to read as follows:\n22. Ecosystem restoration projects (a) Definition In this section, the term ecosystem restoration project means a project proposed for the primary purpose of manipulating the physical, chemical, or biological characteristics of a site with the goal of\u2014 (1) recovering natural and beneficial functions to a former or degraded aquatic resource or floodplain; or (2) enhancing, accelerating, reclaiming, or improving a specific, natural, and beneficial function of an aquatic resource or floodplain. (b) Exemption from fees for flood hazard change requests for ecosystem restoration projects Notwithstanding any other provision of law, a requester shall be exempt from submitting a review or processing fee for a request for a flood insurance rate map change based on an ecosystem restoration project. (c) Exemption from conditional approval for certain ecosystem restoration projects A community may permit an ecosystem restoration project within an adopted regulatory floodway that would result in an increase in base flood elevations, if\u2014 (1) a professional engineer uses the best judgment of the engineer to determine that the cumulative effect of the proposed ecosystem restoration project, when combined with all other existing development, will not increase the water surface elevation of the base flood by more than 1 foot (or a greater amount or metric determined appropriate by the Administrator); (2) no insurable structure or any critical infrastructure is located in an area that would be adversely impacted by the increased base flood elevation; and (3) not later than 180 days after the date on which the ecosystem restoration project is completed, the community submits to the Administrator an analysis regarding the changed conditions caused by the ecosystem restoration project. (d) Rule of construction Nothing in this section may be construed to affect the procedure (as in effect on the day before the date of enactment of the Floodplain Enhancement and Recovery Act ) for providing notification to a landowner with respect to development in a regulatory floodway. .\n##### (b) Technical and conforming amendment\nThe table of contents for the Homeowner Flood Insurance Affordability Act of 2014 ( Public Law 113\u201389 ) is amended by striking the item relating to section 22 and inserting the following:\nSec. 22. Ecosystem restoration projects. .\n##### (c) Guidance\n**(1) Definitions**\nIn this subsection:\n**(A) Administrator**\nThe term Administrator means the Administrator of the Federal Emergency Management Agency.\n**(B) Covered agencies**\nThe term covered agencies means Federal and State natural resource agencies, as determined by the Administrator.\n**(2) Issuance**\nNot later than 180 days after the date of enactment of this Act, and after consultation with the heads of covered agencies, the Administrator shall issue guidance to implement section 22 of the Homeowner Flood Insurance Affordability Act of 2014 ( 42 U.S.C. 4101e ), as amended by this section.",
      "versionDate": "2025-11-21",
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
        "actionDate": "2025-05-01",
        "text": "Read twice and referred to the Committee on Banking, Housing, and Urban Affairs."
      },
      "number": "1564",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Floodplain Enhancement and Recovery Act",
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
        "name": "Finance and Financial Sector",
        "updateDate": "2025-12-18T16:13:33Z"
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
      "date": "2025-11-21",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6256ih.xml"
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
      "title": "Floodplain Enhancement and Recovery Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-12-17T04:23:23Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Floodplain Enhancement and Recovery Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-12-17T04:23:22Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Homeowner Flood Insurance Affordability Act of 2014 to address ecosystem restoration projects, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-12-17T04:18:20Z"
    }
  ]
}
```
