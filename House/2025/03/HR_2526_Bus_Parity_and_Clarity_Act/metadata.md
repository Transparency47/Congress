# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/2526?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/2526
- Title: Bus Parity and Clarity Act
- Congress: 119
- Bill type: HR
- Bill number: 2526
- Origin chamber: House
- Introduced date: 2025-03-31
- Update date: 2026-04-29T20:40:02Z
- Update date including text: 2026-04-29T20:40:02Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-03-31: Introduced in House
- 2025-03-31 - IntroReferral: Introduced in House
- 2025-03-31 - IntroReferral: Introduced in House
- 2025-03-31 - IntroReferral: Referred to the House Committee on Transportation and Infrastructure.
- 2025-03-31 - Committee: Referred to the Subcommittee on Highways and Transit.
- Latest action: 2025-03-31: Introduced in House

## Actions

- 2025-03-31 - IntroReferral: Introduced in House
- 2025-03-31 - IntroReferral: Introduced in House
- 2025-03-31 - IntroReferral: Referred to the House Committee on Transportation and Infrastructure.
- 2025-03-31 - Committee: Referred to the Subcommittee on Highways and Transit.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-03-31",
    "latestAction": {
      "actionDate": "2025-03-31",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/2526",
    "number": "2526",
    "originChamber": "House",
    "policyArea": {
      "name": "Transportation and Public Works"
    },
    "sponsors": [
      {
        "bioguideId": "V000133",
        "district": "2",
        "firstName": "Jefferson",
        "fullName": "Rep. Van Drew, Jefferson [R-NJ-2]",
        "lastName": "Van Drew",
        "party": "R",
        "state": "NJ"
      }
    ],
    "title": "Bus Parity and Clarity Act",
    "type": "HR",
    "updateDate": "2026-04-29T20:40:02Z",
    "updateDateIncludingText": "2026-04-29T20:40:02Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-03-31",
      "committees": {
        "item": {
          "name": "Highways and Transit Subcommittee",
          "systemCode": "hspw12"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Referred to the Subcommittee on Highways and Transit.",
      "type": "Committee"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-03-31",
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
      "actionDate": "2025-03-31",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-03-31",
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
          "date": "2025-03-31T16:04:40Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Transportation and Infrastructure Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": {
              "date": "2025-03-31T21:17:53Z",
              "name": "Referred to"
            }
          },
          "name": "Highways and Transit Subcommittee",
          "systemCode": "hspw12"
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
      "bioguideId": "G000583",
      "district": "5",
      "firstName": "Josh",
      "fullName": "Rep. Gottheimer, Josh [D-NJ-5]",
      "isOriginalCosponsor": "True",
      "lastName": "Gottheimer",
      "party": "D",
      "sponsorshipDate": "2025-03-31",
      "state": "NJ"
    },
    {
      "bioguideId": "V000138",
      "district": "7",
      "firstName": "Eugene",
      "fullName": "Rep. Vindman, Eugene Simon [D-VA-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Vindman",
      "middleName": "Simon",
      "party": "D",
      "sponsorshipDate": "2025-10-24",
      "state": "VA"
    },
    {
      "bioguideId": "W000822",
      "district": "12",
      "firstName": "Bonnie",
      "fullName": "Rep. Watson Coleman, Bonnie [D-NJ-12]",
      "isOriginalCosponsor": "False",
      "lastName": "Watson Coleman",
      "party": "D",
      "sponsorshipDate": "2026-01-12",
      "state": "NJ"
    },
    {
      "bioguideId": "B001309",
      "district": "2",
      "firstName": "Tim",
      "fullName": "Rep. Burchett, Tim [R-TN-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Burchett",
      "party": "R",
      "sponsorshipDate": "2026-04-16",
      "state": "TN"
    },
    {
      "bioguideId": "L000599",
      "district": "17",
      "firstName": "Michael",
      "fullName": "Rep. Lawler, Michael [R-NY-17]",
      "isOriginalCosponsor": "False",
      "lastName": "Lawler",
      "party": "R",
      "sponsorshipDate": "2026-04-22",
      "state": "NY"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr2526ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 2526\nIN THE HOUSE OF REPRESENTATIVES\nMarch 31, 2025 Mr. Van Drew (for himself and Mr. Gottheimer ) introduced the following bill; which was referred to the Committee on Transportation and Infrastructure\nA BILL\nTo amend title 23, United States Code, to clarify provisions relating to equal access for over-the-road buses, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Bus Parity and Clarity Act .\n#### 2. Clarification of equal access for over-the-road buses\n##### (a) In general\n**(1) Toll roads, bridges, tunnels, and ferries**\nSection 129(a) of title 23, United States Code, is amended\u2014\n**(A)**\nin paragraph (9)(A) by striking that serves the public and inserting in scheduled or charter service ; and\n**(B)**\nin paragraph (11) by adding at the end the following:\n(F) Charter service The term charter service has the meaning given the term in part 604 of title 49, Code of Federal Regulations. .\n**(2) HOV facilities**\nSection 166 of title 23, United States Code, is amended\u2014\n**(A)**\nin subsection (b)(3)(C) by striking serving the public and inserting in scheduled or charter service ; and\n**(B)**\nin subsection (f) by adding at the end the following:\n(7) Charter service The term charter service has the meaning given the term in part 604 of title 49, Code of Federal Regulations. .\n##### (b) Value pricing pilot program\nIn carrying out a value pricing pilot program under section 1012(b) of the Intermodal Surface Transportation Efficiency Act of 1991 ( 23 U.S.C. 149 note), a public authority with jurisdiction over a toll facility shall provide to an over-the-road bus in scheduled or charter service access to a toll facility under the same rates, terms, and conditions as a public transportation vehicle, consistent with section 129(a)(9) of title 23, United States Code.\n##### (c) Publication\nNot later than 180 days after the date of enactment of this Act, and annually thereafter, the Administrator of the Federal Highway Administration shall publish on a publicly available website a unified database containing information with respect to the rates, terms, and conditions of each toll facility covered under the equal access provisions described in sections 129(a)(9) and 166(b)(3) of title 23, United States Code.\n##### (d) Definitions\nIn this Act:\n**(1) Charter service**\nThe term charter service has the meaning given the term in part 604 of title 49, Code of Federal Regulations.\n**(2) Over-the-road bus**\nThe term over-the-road bus has the meaning given the term in section 301 of the Americans with Disabilities Act of 1990 ( 42 U.S.C. 12181 ).\n**(3) Public authority; toll facility**\nThe terms public authority and toll facility have the meanings given the terms in section 129(a) of title 23, United States Code.\n**(4) Public transportation vehicle**\nThe term public transportation vehicle has the meaning given the term in section 166 of title 23, United States Code.",
      "versionDate": "2025-03-31",
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
        "updateDate": "2025-04-08T12:52:03Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-03-31",
    "originChamber": "House",
    "payload": {
      "dublinCore": {
        "contributor": "Congressional Research Service, Library of Congress",
        "description": "This file contains bill summaries for federal legislation. A bill summary describes the most significant provisions of a piece of legislation and details the effects the legislative text may have on current law and federal programs. Bill summaries are authored by the Congressional Research Service (CRS) of the Library of Congress. As stated in Public Law 91-510 (2 USC 166 (d)(6)), one of the duties of CRS is \"to prepare summaries and digests of bills and resolutions of a public general nature introduced in the Senate or House of Representatives\". For more information, refer to the User Guide that accompanies this file.",
        "format": "text/xml",
        "language": "EN",
        "rights": "Pursuant to Title 17 Section 105 of the United States Code, this file is not subject to copyright protection and is in the public domain."
      },
      "item": {
        "@attributes": {
          "congress": "119",
          "measure-id": "id119hr2526",
          "measure-number": "2526",
          "measure-type": "hr",
          "orig-publish-date": "2025-03-31",
          "originChamber": "HOUSE",
          "update-date": "2026-04-29"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr2526v00",
            "update-date": "2026-04-29"
          },
          "action-date": "2025-03-31",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Bus Parity and Clarity Act</strong></p><p>This bill specifies that charter bus service has the same access to tolling rates and roads as public transportation vehicles.</p><p>Current law applies the same access to tolling rates to public transportation vehicles\u00a0and over-the-road buses (i.e., buses with an elevated passenger deck located over a baggage compartment) that serve the public.</p><p>The bill specifies that the same access to rates apply to over-the-road buses in (1) scheduled service (e.g., intercity bus service), and (2) charter service.\u00a0This applies to charter\u00a0bus service for\u00a0tolling for federal-aid highways, bridges, and tunnels;\u00a0high occupancy vehicle (HOV) lanes and facilities; and the Value Pricing Pilot Program of the Federal Highway Administration (FHWA).</p><p>Charter service includes transportation provided</p><ul><li>at the request of a third party for the exclusive use of a bus for a negotiated price\u00a0(e.g., for a wedding or\u00a0corporate event); or</li><li>to the public for events or functions that occur on an irregular basis or for a limited duration, and a premium fare is charged or third party pays for the service (e.g.,\u00a0providing shuttle service for a public event).</li></ul><p>In addition, the FHWA must annually publish on a publicly available website a unified database containing the rates, terms, and conditions of each toll facility covered under these provisions.</p>"
        },
        "title": "Bus Parity and Clarity Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr2526.xml",
    "summary": {
      "actionDate": "2025-03-31",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Bus Parity and Clarity Act</strong></p><p>This bill specifies that charter bus service has the same access to tolling rates and roads as public transportation vehicles.</p><p>Current law applies the same access to tolling rates to public transportation vehicles\u00a0and over-the-road buses (i.e., buses with an elevated passenger deck located over a baggage compartment) that serve the public.</p><p>The bill specifies that the same access to rates apply to over-the-road buses in (1) scheduled service (e.g., intercity bus service), and (2) charter service.\u00a0This applies to charter\u00a0bus service for\u00a0tolling for federal-aid highways, bridges, and tunnels;\u00a0high occupancy vehicle (HOV) lanes and facilities; and the Value Pricing Pilot Program of the Federal Highway Administration (FHWA).</p><p>Charter service includes transportation provided</p><ul><li>at the request of a third party for the exclusive use of a bus for a negotiated price\u00a0(e.g., for a wedding or\u00a0corporate event); or</li><li>to the public for events or functions that occur on an irregular basis or for a limited duration, and a premium fare is charged or third party pays for the service (e.g.,\u00a0providing shuttle service for a public event).</li></ul><p>In addition, the FHWA must annually publish on a publicly available website a unified database containing the rates, terms, and conditions of each toll facility covered under these provisions.</p>",
      "updateDate": "2026-04-29",
      "versionCode": "id119hr2526"
    },
    "title": "Bus Parity and Clarity Act"
  },
  "summaries": [
    {
      "actionDate": "2025-03-31",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Bus Parity and Clarity Act</strong></p><p>This bill specifies that charter bus service has the same access to tolling rates and roads as public transportation vehicles.</p><p>Current law applies the same access to tolling rates to public transportation vehicles\u00a0and over-the-road buses (i.e., buses with an elevated passenger deck located over a baggage compartment) that serve the public.</p><p>The bill specifies that the same access to rates apply to over-the-road buses in (1) scheduled service (e.g., intercity bus service), and (2) charter service.\u00a0This applies to charter\u00a0bus service for\u00a0tolling for federal-aid highways, bridges, and tunnels;\u00a0high occupancy vehicle (HOV) lanes and facilities; and the Value Pricing Pilot Program of the Federal Highway Administration (FHWA).</p><p>Charter service includes transportation provided</p><ul><li>at the request of a third party for the exclusive use of a bus for a negotiated price\u00a0(e.g., for a wedding or\u00a0corporate event); or</li><li>to the public for events or functions that occur on an irregular basis or for a limited duration, and a premium fare is charged or third party pays for the service (e.g.,\u00a0providing shuttle service for a public event).</li></ul><p>In addition, the FHWA must annually publish on a publicly available website a unified database containing the rates, terms, and conditions of each toll facility covered under these provisions.</p>",
      "updateDate": "2026-04-29",
      "versionCode": "id119hr2526"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-03-31",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr2526ih.xml"
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
      "title": "Bus Parity and Clarity Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-04-08T04:23:16Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Bus Parity and Clarity Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-04-08T04:23:15Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend title 23, United States Code, to clarify provisions relating to equal access for over-the-road buses, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-04-08T04:18:26Z"
    }
  ]
}
```
