# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/2543?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/2543
- Title: Stop the SWARM Act of 2025
- Congress: 119
- Bill type: S
- Bill number: 2543
- Origin chamber: Senate
- Introduced date: 2025-07-30
- Update date: 2026-04-28T14:18:44Z
- Update date including text: 2026-04-28T14:18:44Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-07-30: Introduced in Senate
- 2025-07-30 - IntroReferral: Introduced in Senate
- 2025-07-30 - IntroReferral: Read twice and referred to the Committee on Agriculture, Nutrition, and Forestry.
- Latest action: 2025-07-30: Introduced in Senate

## Actions

- 2025-07-30 - IntroReferral: Introduced in Senate
- 2025-07-30 - IntroReferral: Read twice and referred to the Committee on Agriculture, Nutrition, and Forestry.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-07-30",
    "latestAction": {
      "actionDate": "2025-07-30",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/2543",
    "number": "2543",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Agriculture and Food"
    },
    "sponsors": [
      {
        "bioguideId": "C001056",
        "district": "",
        "firstName": "John",
        "fullName": "Sen. Cornyn, John [R-TX]",
        "lastName": "Cornyn",
        "party": "R",
        "state": "TX"
      }
    ],
    "title": "Stop the SWARM Act of 2025",
    "type": "S",
    "updateDate": "2026-04-28T14:18:44Z",
    "updateDateIncludingText": "2026-04-28T14:18:44Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-07-30",
      "committees": {
        "item": {
          "name": "Agriculture, Nutrition, and Forestry Committee",
          "systemCode": "ssaf00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Agriculture, Nutrition, and Forestry.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-07-30",
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
          "date": "2025-07-30T19:31:42Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Agriculture, Nutrition, and Forestry Committee",
      "systemCode": "ssaf00",
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
      "bioguideId": "H001046",
      "firstName": "Martin",
      "fullName": "Sen. Heinrich, Martin [D-NM]",
      "isOriginalCosponsor": "True",
      "lastName": "Heinrich",
      "party": "D",
      "sponsorshipDate": "2025-07-30",
      "state": "NM"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2543is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 2543\nIN THE SENATE OF THE UNITED STATES\nJuly 30, 2025 Mr. Cornyn (for himself and Mr. Heinrich ) introduced the following bill; which was read twice and referred to the Committee on Agriculture, Nutrition, and Forestry\nA BILL\nTo direct the Secretary of Agriculture to submit a report on New World screwworm readiness and response.\n#### 1. Short title\nThis Act may be cited as the Stop the Screwworms With Active Readiness and Mitigation Act of 2025 or the Stop the SWARM Act of 2025 .\n#### 2. Report on New World screwworm readiness and response\nNot later than 30 days after the date of enactment of this Act, the Secretary of Agriculture shall submit to Congress a report on the New World Screwworm domestic readiness and response initiative of the Animal and Plant Health Inspection Service, with a particular focus on\u2014\n**(1)**\n**(A)**\ndomestic readiness, including the construction of a domestic production facility in the event of a threat of a domestic outbreak; and\n**(B)**\nexploring partnerships with States and industry with respect to that construction and other domestic preparedness efforts;\n**(2)**\nsterile fly production technology and other eradication tools and technologies; and\n**(3)**\nthe benefits of and barriers, including timelines and costs, to enhanced domestic, as compared to international, sterile fly production.",
      "versionDate": "2025-07-30",
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
      "legislativeSubjects": "",
      "policyArea": {
        "name": "Agriculture and Food",
        "updateDate": "2025-09-16T22:35:51Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-07-30",
    "originChamber": "Senate",
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
          "measure-id": "id119s2543",
          "measure-number": "2543",
          "measure-type": "s",
          "orig-publish-date": "2025-07-30",
          "originChamber": "SENATE",
          "update-date": "2026-04-28"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "SENATE",
            "summary-id": "id119s2543v00",
            "update-date": "2026-04-28"
          },
          "action-date": "2025-07-30",
          "action-desc": "Introduced in Senate",
          "summary-text": "<p><strong>Stop the Screwworms With Active Readiness and Mitigation Act of 2025 or the Stop the SWARM Act of 2025</strong></p><p>This bill directs the Department of Agriculture to submit a report to Congress on the New\u00a0World Screwworm (NWS) domestic readiness and response initiative of the Animal and Plant Health Inspection Service.</p><p>NWS is a species of parasitic fly. The flies lay eggs in open wounds and body openings of warm-blooded animals (e.g., livestock, pets, and wildlife) and people. The eggs hatch into parasitic maggots that burrow into and feed on living tissue or flesh.</p>"
        },
        "title": "Stop the SWARM Act of 2025"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/s/BILLSUM-119s2543.xml",
    "summary": {
      "actionDate": "2025-07-30",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Stop the Screwworms With Active Readiness and Mitigation Act of 2025 or the Stop the SWARM Act of 2025</strong></p><p>This bill directs the Department of Agriculture to submit a report to Congress on the New\u00a0World Screwworm (NWS) domestic readiness and response initiative of the Animal and Plant Health Inspection Service.</p><p>NWS is a species of parasitic fly. The flies lay eggs in open wounds and body openings of warm-blooded animals (e.g., livestock, pets, and wildlife) and people. The eggs hatch into parasitic maggots that burrow into and feed on living tissue or flesh.</p>",
      "updateDate": "2026-04-28",
      "versionCode": "id119s2543"
    },
    "title": "Stop the SWARM Act of 2025"
  },
  "summaries": [
    {
      "actionDate": "2025-07-30",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Stop the Screwworms With Active Readiness and Mitigation Act of 2025 or the Stop the SWARM Act of 2025</strong></p><p>This bill directs the Department of Agriculture to submit a report to Congress on the New\u00a0World Screwworm (NWS) domestic readiness and response initiative of the Animal and Plant Health Inspection Service.</p><p>NWS is a species of parasitic fly. The flies lay eggs in open wounds and body openings of warm-blooded animals (e.g., livestock, pets, and wildlife) and people. The eggs hatch into parasitic maggots that burrow into and feed on living tissue or flesh.</p>",
      "updateDate": "2026-04-28",
      "versionCode": "id119s2543"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-07-30",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2543is.xml"
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
      "title": "Stop the SWARM Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-08-09T03:38:25Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Stop the SWARM Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-08-09T03:38:22Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Stop the Screwworms With Active Readiness and Mitigation Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-08-09T03:38:22Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to direct the Secretary of Agriculture to submit a report on New World screwworm readiness and response.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-08-09T03:33:37Z"
    }
  ]
}
```
