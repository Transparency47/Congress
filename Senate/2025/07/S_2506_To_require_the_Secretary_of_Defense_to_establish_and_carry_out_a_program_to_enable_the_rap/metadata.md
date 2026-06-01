# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/2506?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/2506
- Title: SkyFoundry Act of 2025
- Congress: 119
- Bill type: S
- Bill number: 2506
- Origin chamber: Senate
- Introduced date: 2025-07-29
- Update date: 2026-05-13T11:03:32Z
- Update date including text: 2026-05-13T11:03:32Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-07-29: Introduced in Senate
- 2025-07-29 - IntroReferral: Introduced in Senate
- 2025-07-29 - IntroReferral: Read twice and referred to the Committee on Armed Services.
- Latest action: 2025-07-29: Introduced in Senate

## Actions

- 2025-07-29 - IntroReferral: Introduced in Senate
- 2025-07-29 - IntroReferral: Read twice and referred to the Committee on Armed Services.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-07-29",
    "latestAction": {
      "actionDate": "2025-07-29",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/2506",
    "number": "2506",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Armed Forces and National Security"
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
    "title": "SkyFoundry Act of 2025",
    "type": "S",
    "updateDate": "2026-05-13T11:03:32Z",
    "updateDateIncludingText": "2026-05-13T11:03:32Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-07-29",
      "committees": {
        "item": {
          "name": "Armed Services Committee",
          "systemCode": "ssas00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Armed Services.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-07-29",
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
            "date": "2025-07-29T18:51:20Z",
            "name": "Referred To"
          },
          {
            "date": "2025-07-29T18:51:20Z",
            "name": "Referred To"
          }
        ]
      },
      "chamber": "Senate",
      "name": "Armed Services Committee",
      "systemCode": "ssas00",
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
      "bioguideId": "B001236",
      "firstName": "John",
      "fullName": "Sen. Boozman, John [R-AR]",
      "isOriginalCosponsor": "True",
      "lastName": "Boozman",
      "party": "R",
      "sponsorshipDate": "2025-07-29",
      "state": "AR"
    },
    {
      "bioguideId": "C001095",
      "firstName": "Tom",
      "fullName": "Sen. Cotton, Tom [R-AR]",
      "isOriginalCosponsor": "True",
      "lastName": "Cotton",
      "party": "R",
      "sponsorshipDate": "2025-07-29",
      "state": "AR"
    },
    {
      "bioguideId": "C001056",
      "firstName": "John",
      "fullName": "Sen. Cornyn, John [R-TX]",
      "isOriginalCosponsor": "True",
      "lastName": "Cornyn",
      "party": "R",
      "sponsorshipDate": "2025-07-29",
      "state": "TX"
    },
    {
      "bioguideId": "R000584",
      "firstName": "James",
      "fullName": "Sen. Risch, James E. [R-ID]",
      "isOriginalCosponsor": "False",
      "lastName": "Risch",
      "middleName": "E.",
      "party": "R",
      "sponsorshipDate": "2025-10-16",
      "state": "ID"
    },
    {
      "bioguideId": "M001243",
      "firstName": "David",
      "fullName": "Sen. McCormick, David [R-PA]",
      "isOriginalCosponsor": "False",
      "lastName": "McCormick",
      "middleName": "H.",
      "party": "R",
      "sponsorshipDate": "2026-05-12",
      "state": "PA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2506is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 2506\nIN THE SENATE OF THE UNITED STATES\nJuly 29, 2025 Mr. Cruz (for himself, Mr. Boozman , Mr. Cotton , and Mr. Cornyn ) introduced the following bill; which was read twice and referred to the Committee on Armed Services\nA BILL\nTo require the Secretary of Defense to establish and carry out a program to enable the rapid development, testing, and scalable manufacture of small unmanned aircraft systems, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the SkyFoundry Act of 2025 .\n#### 2. SkyFoundry Program\n##### (a) Establishment\n**(1) Program required**\nThe Secretary of Defense shall establish and carry out a program to enable the rapid development, testing, and scalable manufacture of small unmanned aircraft systems, with potential expansion to associated energetics and other autonomous systems as determined by the Secretary.\n**(2) Designation**\nThe program established pursuant to paragraph (1) shall be known as the SkyFoundry Program (in this section the Program ).\n**(3) Administration**\nThe Secretary shall\u2014\n**(A)**\nadminister the Program through the Secretary of the Army; and\n**(B)**\nestablish the Program as part of the Defense Industrial Resilience Consortium.\n##### (b) Alternative acquisition mechanism\nIn carrying out the Program, the Secretary shall leverage alternative acquisition mechanisms to accelerate development and production. Such mechanisms shall include the use of other transaction authority under section 4022 of title 10, United States Code, and the use of the middle tier of acquisition pathway for rapid prototyping and rapid fielding as authorized by section 3602 of such title.\n##### (c) Components\nThe Program shall have two components as follows:\n**(1) Innovation facility**\nA Government-owned innovation facility for the development of small unmanned aircraft systems that is operated by the United States Army Materiel Command in coordination with United States Futures Command and serves as the research, development, and testing hub, integrating lessons learned from global conflicts to rapidly evolve United States small unmanned aircraft systems designs.\n**(2) Production facility**\nThe Commander of United States Army Materiel Command shall identify a Government-owned production facility with the competencies for producing various forms of small unmanned aircraft systems. The facility shall be operated by United States Army Materiel Command and have the capability to produce 1,000,000 small unmanned aircraft systems annually once fully established.\n##### (d) Government-Owned Government-Operated Contractor Augmented Model\nThe Secretary may\u2014\n**(1)**\nenter into multiyear contracts or agreements for contractor augmented support to the Program, including integrating specialized contractor personnel within Program facilities as part of hybrid teams alongside military and civilian personnel; and\n**(2)**\nenter into public-private partnership agreements with private industry, academic institutions, and nonprofit entities in support of the Program.\n##### (e) Facilities and infrastructure\n**(1) In general**\nIn carrying out the Program, the Secretary shall prioritize utilizing or modifying existing Army Depot facilities and select at least two separate sites for the Program, one to house the innovation facility required by subsection (b)(1) and one to house the production facility required by subsection (b)(2).\n**(2) Authority to renovate, expand, and construct**\nThe Secretary may renovate, expand, or construct facilities for the Program using available funds, notwithstanding chapter 169 of title 10, United States Code.\n**(3) Selection of sites**\nWhen selecting sites for the Program, the Secretary shall consider that the production facility required by subsection (b)(2) shall be housed at an existing Army Depot that meets the following requirements:\n**(A)**\nThe Army Depot shall be comprised of 15,000 acres of land.\n**(B)**\nThe Army Depot shall have approximately 10,000 buildable acres of land.\n**(C)**\nThe Army Depot shall have approximately 8,000,000 square feet of facilities.\n**(D)**\nThe Army Depot shall be located within 50 miles of four States.\n##### (f) Intellectual property rights\nThe Secretary shall ensure that the United States retains appropriate intellectual property and technical data rights for any systems or technologies developed under the Program. At a minimum, the Secretary shall secure Government purpose rights in intellectual property developed jointly with contractors, to enable the Government\u2019s continued production, sustainment, modification, and competitive procurement of such systems.\n##### (g) Defense Production Act designation\nThe President (or the Secretary of Defense under delegated authority) shall utilize authorities under title III of the Defense Production Act of 1950 ( 50 U.S.C. 4531 et seq. ) to prioritize and support domestic industrial base capacity for small unmanned aircraft systems and associated energetics and autonomous systems. Such items shall be deemed essential for the national defense industrial base, and Title III efforts may include investments in production scale-up, establishment of strategic materials stockpiles, and surge manufacturing capacity for these systems and components.\n##### (h) Expedited approvals and waivers\nThe Secretary, or the Secretary of the Army under explicit delegated authority, may expedite, and as appropriate to waive or modify Department of Defense regulatory requirements and internal procedures that would otherwise impede the rapid development, acquisition, or production activities of the Program.",
      "versionDate": "2025-07-29",
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
        "actionDate": "2025-09-02",
        "text": "Referred to the Committee on Armed Services, and in addition to the Committee on Financial Services, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned."
      },
      "number": "5086",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "SkyFoundry Act of 2025",
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
        "name": "Armed Forces and National Security",
        "updateDate": "2025-09-19T17:52:13Z"
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
      "date": "2025-07-29",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2506is.xml"
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
      "title": "SkyFoundry Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-05-13T11:03:32Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "SkyFoundry Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-08-09T03:38:21Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to require the Secretary of Defense to establish and carry out a program to enable the rapid development, testing, and scalable manufacture of small unmanned aircraft systems, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-08-09T03:33:28Z"
    }
  ]
}
```
