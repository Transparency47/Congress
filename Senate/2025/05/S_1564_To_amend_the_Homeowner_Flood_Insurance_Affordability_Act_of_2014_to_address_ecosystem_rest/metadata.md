# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/1564?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/1564
- Title: Floodplain Enhancement and Recovery Act
- Congress: 119
- Bill type: S
- Bill number: 1564
- Origin chamber: Senate
- Introduced date: 2025-05-01
- Update date: 2026-04-16T11:03:24Z
- Update date including text: 2026-04-16T11:03:24Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-05-01: Introduced in Senate
- 2025-05-01 - IntroReferral: Introduced in Senate
- 2025-05-01 - IntroReferral: Read twice and referred to the Committee on Banking, Housing, and Urban Affairs.
- Latest action: 2025-05-01: Introduced in Senate

## Actions

- 2025-05-01 - IntroReferral: Introduced in Senate
- 2025-05-01 - IntroReferral: Read twice and referred to the Committee on Banking, Housing, and Urban Affairs.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-05-01",
    "latestAction": {
      "actionDate": "2025-05-01",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/1564",
    "number": "1564",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Finance and Financial Sector"
    },
    "sponsors": [
      {
        "bioguideId": "M001111",
        "district": "",
        "firstName": "Patty",
        "fullName": "Sen. Murray, Patty [D-WA]",
        "lastName": "Murray",
        "party": "D",
        "state": "WA"
      }
    ],
    "title": "Floodplain Enhancement and Recovery Act",
    "type": "S",
    "updateDate": "2026-04-16T11:03:24Z",
    "updateDateIncludingText": "2026-04-16T11:03:24Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-05-01",
      "committees": {
        "item": {
          "name": "Banking, Housing, and Urban Affairs Committee",
          "systemCode": "ssbk00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Banking, Housing, and Urban Affairs.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-05-01",
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
        "item": [
          {
            "date": "2025-05-01T16:56:38Z",
            "name": "Referred To"
          },
          {
            "date": "2025-05-01T16:56:38Z",
            "name": "Referred To"
          }
        ]
      },
      "chamber": "Senate",
      "name": "Banking, Housing, and Urban Affairs Committee",
      "systemCode": "ssbk00",
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
      "sponsorshipDate": "2025-05-01",
      "state": "MT"
    },
    {
      "bioguideId": "T000476",
      "firstName": "Thomas",
      "fullName": "Sen. Tillis, Thomas [R-NC]",
      "isOriginalCosponsor": "False",
      "lastName": "Tillis",
      "middleName": "Roland",
      "party": "R",
      "sponsorshipDate": "2026-04-15",
      "state": "NC"
    },
    {
      "bioguideId": "A000382",
      "firstName": "Angela",
      "fullName": "Sen. Alsobrooks, Angela D. [D-MD]",
      "isOriginalCosponsor": "False",
      "lastName": "Alsobrooks",
      "party": "D",
      "sponsorshipDate": "2026-04-15",
      "state": "MD"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1564is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 1564\nIN THE SENATE OF THE UNITED STATES\nMay 1, 2025 Mrs. Murray (for herself and Mr. Daines ) introduced the following bill; which was read twice and referred to the Committee on Banking, Housing, and Urban Affairs\nA BILL\nTo amend the Homeowner Flood Insurance Affordability Act of 2014 to address ecosystem restoration projects, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Floodplain Enhancement and Recovery Act .\n#### 2. Ecosystem restoration projects\n##### (a) In general\nSection 22 of the Homeowner Flood Insurance Affordability Act of 2014 ( 42 U.S.C. 4101e ) is amended to read as follows:\n22. Ecosystem restoration projects (a) Definition In this section, the term ecosystem restoration project means a project proposed for the primary purpose of manipulating the physical, chemical, or biological characteristics of a site with the goal of\u2014 (1) recovering natural and beneficial functions to a former or degraded aquatic resource or floodplain; or (2) enhancing, accelerating, reclaiming, or improving a specific, natural, and beneficial function of an aquatic resource or floodplain. (b) Exemption from fees for flood hazard change requests for ecosystem restoration projects Notwithstanding any other provision of law, a requester shall be exempt from submitting a review or processing fee for a request for a flood insurance rate map change based on an ecosystem restoration project. (c) Exemption from conditional approval for certain ecosystem restoration projects A community may permit an ecosystem restoration project within an adopted regulatory floodway that would result in an increase in base flood elevations, if\u2014 (1) a professional engineer uses the best judgment of the engineer to determine that the cumulative effect of the proposed ecosystem restoration project, when combined with all other existing development, will not increase the water surface elevation of the base flood by more than 1 foot (or a greater amount or metric determined appropriate by the Administrator); (2) no insurable structure or any critical infrastructure is located in an area that would be adversely impacted by the increased base flood elevation; and (3) not later than 180 days after the date on which the ecosystem restoration project is completed, the community submits to the Administrator an analysis regarding the changed conditions caused by the ecosystem restoration project. (d) Rule of construction Nothing in this section may be construed to affect the procedure (as in effect on the day before the date of enactment of the Floodplain Enhancement and Recovery Act ) for providing notification to a landowner with respect to development in a regulatory floodway. .\n##### (b) Technical and conforming amendment\nThe table of contents for the Homeowner Flood Insurance Affordability Act of 2014 ( Public Law 113\u201389 ) is amended by striking the item relating to section 22 and inserting the following:\nSec. 22. Ecosystem restoration projects. .\n##### (c) Guidance\n**(1) Definitions**\nIn this subsection:\n**(A) Administrator**\nThe term Administrator means the Administrator of the Federal Emergency Management Agency.\n**(B) Covered agencies**\nThe term covered agencies means Federal and State natural resource agencies, as determined by the Administrator.\n**(2) Issuance**\nNot later than 180 days after the date of enactment of this Act, and after consultation with the heads of covered agencies, the Administrator shall issue guidance to implement section 22 of the Homeowner Flood Insurance Affordability Act of 2014 ( 42 U.S.C. 4101e ), as amended by this section.",
      "versionDate": "2025-05-01",
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
        "actionDate": "2025-11-21",
        "text": "Referred to the House Committee on Financial Services."
      },
      "number": "6256",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Floodplain Enhancement and Recovery Act",
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
        "name": "Finance and Financial Sector",
        "updateDate": "2025-05-21T12:01:39Z"
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
      "date": "2025-05-01",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1564is.xml"
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
      "title": "Floodplain Enhancement and Recovery Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-04-16T11:03:24Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Floodplain Enhancement and Recovery Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-05-14T04:23:20Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend the Homeowner Flood Insurance Affordability Act of 2014 to address ecosystem restoration projects, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-05-14T04:18:48Z"
    }
  ]
}
```
