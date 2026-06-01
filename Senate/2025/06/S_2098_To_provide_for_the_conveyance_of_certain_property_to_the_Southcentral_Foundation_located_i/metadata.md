# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/2098?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/2098
- Title: Southcentral Foundation Land Transfer Act of 2025
- Congress: 119
- Bill type: S
- Bill number: 2098
- Origin chamber: Senate
- Introduced date: 2025-06-17
- Update date: 2026-05-21T11:03:37Z
- Update date including text: 2026-05-21T11:03:37Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-06-17: Introduced in Senate
- 2025-06-17 - IntroReferral: Introduced in Senate
- 2025-06-17 - IntroReferral: Read twice and referred to the Committee on Indian Affairs.
- 2026-02-04 - Committee: Committee on Indian Affairs. Hearings held.
- 2026-05-20 - Committee: Committee on Indian Affairs. Ordered to be reported without amendment favorably.
- Latest action: 2025-06-17: Introduced in Senate

## Actions

- 2025-06-17 - IntroReferral: Introduced in Senate
- 2025-06-17 - IntroReferral: Read twice and referred to the Committee on Indian Affairs.
- 2026-02-04 - Committee: Committee on Indian Affairs. Hearings held.
- 2026-05-20 - Committee: Committee on Indian Affairs. Ordered to be reported without amendment favorably.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-06-17",
    "latestAction": {
      "actionDate": "2025-06-17",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/2098",
    "number": "2098",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Public Lands and Natural Resources"
    },
    "sponsors": [
      {
        "bioguideId": "M001153",
        "district": "",
        "firstName": "Lisa",
        "fullName": "Sen. Murkowski, Lisa [R-AK]",
        "lastName": "Murkowski",
        "party": "R",
        "state": "AK"
      }
    ],
    "title": "Southcentral Foundation Land Transfer Act of 2025",
    "type": "S",
    "updateDate": "2026-05-21T11:03:37Z",
    "updateDateIncludingText": "2026-05-21T11:03:37Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-05-20",
      "committees": {
        "item": {
          "name": "Indian Affairs Committee",
          "systemCode": "slia00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Committee on Indian Affairs. Ordered to be reported without amendment favorably.",
      "type": "Committee"
    },
    {
      "actionDate": "2026-02-04",
      "committees": {
        "item": {
          "name": "Indian Affairs Committee",
          "systemCode": "slia00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Committee on Indian Affairs. Hearings held.",
      "type": "Committee"
    },
    {
      "actionDate": "2025-06-17",
      "committees": {
        "item": {
          "name": "Indian Affairs Committee",
          "systemCode": "slia00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Indian Affairs.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-06-17",
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
            "date": "2026-05-20T18:30:12Z",
            "name": "Markup By"
          },
          {
            "date": "2026-02-04T19:15:04Z",
            "name": "Hearings By (full committee)"
          },
          {
            "date": "2025-06-17T20:01:43Z",
            "name": "Referred To"
          }
        ]
      },
      "chamber": "Senate",
      "name": "Indian Affairs Committee",
      "systemCode": "slia00",
      "type": "Other"
    }
  ]
}
```

## API Data: cosponsors

```json
{
  "cosponsors": [
    {
      "bioguideId": "S001198",
      "firstName": "Dan",
      "fullName": "Sen. Sullivan, Dan [R-AK]",
      "isOriginalCosponsor": "True",
      "lastName": "Sullivan",
      "party": "R",
      "sponsorshipDate": "2025-06-17",
      "state": "AK"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2098is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 2098\nIN THE SENATE OF THE UNITED STATES\nJune 17, 2025 Ms. Murkowski (for herself and Mr. Sullivan ) introduced the following bill; which was read twice and referred to the Committee on Indian Affairs\nA BILL\nTo provide for the conveyance of certain property to the Southcentral Foundation located in Anchorage, Alaska, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Southcentral Foundation Land Transfer Act of 2025 .\n#### 2. Definitions\nIn this Act:\n**(1) SCF**\nThe term SCF means the Southcentral Foundation located in Anchorage, Alaska.\n**(2) Secretary**\nThe term Secretary means the Secretary of Health and Human Services.\n#### 3. Conveyance of property to SCF\n##### (a) In general\nAs soon as practicable, but not later than 2 years, after the date of enactment of this Act, the Secretary shall convey to SCF all right, title, and interest of the United States in and to the property described in subsection (b) for use in connection with health and social services programs.\n##### (b) Property described\nThe property, including all land, improvements, and appurtenances, referred to in this Act is the approximately 3.372 acres located in Lot 1A, Block 36 East Addition, Anchorage Townsite Subdivision in Anchorage, Alaska, according to the official plat thereof, filed under Plat No. 2025\u201311, records of the Anchorage Recording District, Third Judicial District, State of Alaska.\n#### 4. Conditions of conveyance\n##### (a) Conditions\nThe conveyance under subsection (a) of section 3\u2014\n**(1)**\nshall be made by warranty deed; and\n**(2)**\nshall not\u2014\n**(A)**\nrequire any consideration from SCF for the property described in subsection (b) of that section;\n**(B)**\nimpose any obligation, term, or condition on SCF relating to that property; or\n**(C)**\nallow for any reversionary interest of the United States in that property.\n##### (b) Effect on any quitclaim deed\nThe conveyance by the Secretary under subsection (a) of section 3 by warranty deed shall, on the effective date of the conveyance, supersede, and render of no future effect, any quitclaim deed to the property described in subsection (b) of that section executed by the Secretary and SCF.\n##### (c) Easement\nThe Secretary shall be accorded any easement or access to the property conveyed under section 3(a) as may be reasonably necessary to satisfy any retained obligation or liability of the Secretary.\n#### 5. Environmental liability\n##### (a) In general\nNotwithstanding any other provision of law, SCF shall not be liable for any soil, surface water, groundwater, or other contamination resulting from the disposal, release, or presence of any environmental contamination described in subsection (b) on any portion of the property described in section 3(b) that occurred on or before the date on which the property is conveyed to SCF under section 3(a), except that the Secretary shall not be liable for any contamination that occurred after the date that SCF controlled, occupied, and used the property.\n##### (b) Environmental contamination\nEnvironmental contamination referred to in subsection (a) includes any oil or petroleum products, hazardous substances, hazardous materials, hazardous waste, pollutants, toxic substances, solid waste, or any other environmental contamination or hazard as defined in any Federal or State of Alaska law.\n##### (c) Notice of hazardous substance activity and warranty\nIn carrying out this section, the Secretary shall comply with section 120(h) of the Comprehensive Environmental Response, Compensation, and Liability Act of 1980 ( 42 U.S.C. 9620(h) ).\n##### (d) Limitation on applicability\nThis section shall only apply to the property conveyance specifically required by this Act.",
      "versionDate": "2025-06-17",
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
        "actionDate": "2026-05-20",
        "text": "Committee on Indian Affairs. Ordered to be reported without amendment favorably."
      },
      "number": "3620",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Southcentral Foundation Land Transfer Act of 2025",
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
            "name": "Alaska",
            "updateDate": "2025-07-11T18:32:07Z"
          },
          {
            "name": "Hazardous wastes and toxic substances",
            "updateDate": "2025-07-11T18:32:07Z"
          },
          {
            "name": "Land transfers",
            "updateDate": "2025-07-11T18:32:07Z"
          }
        ]
      },
      "policyArea": {
        "name": "Public Lands and Natural Resources",
        "updateDate": "2025-07-14T18:09:10Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-06-17",
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
          "measure-id": "id119s2098",
          "measure-number": "2098",
          "measure-type": "s",
          "orig-publish-date": "2025-06-17",
          "originChamber": "SENATE",
          "update-date": "2026-04-17"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "SENATE",
            "summary-id": "id119s2098v00",
            "update-date": "2026-04-17"
          },
          "action-date": "2025-06-17",
          "action-desc": "Introduced in Senate",
          "summary-text": "<p><strong>Southcentral Foundation Land Transfer Act of 2025</strong></p><p>This bill directs the Department of Health and Human Services (HHS) to convey approximately 3.4 acres in Anchorage, Alaska, to the Southcentral Foundation (SCF) for use in connection with health and social services programs.</p><p>The conveyance must be made by warranty deed. The conveyance may not (1) require any consideration (such as payment) from the SCF for the property; (2) impose any obligation, term, or condition on the SCF relating to that property; or (3) allow for any U.S. reversionary interest in the property.</p><p>HHS must be accorded any easement or access to the property as may be reasonably necessary to satisfy any retained obligation or liability of HHS.</p><p>The bill prohibits the SCF from being liable for certain environmental contamination that occurred on or before the date on which the property is conveyed to the SCF. In turn, HHS may not be liable for any contamination that occurred after the date that the SCF controlled, occupied, and used the property.\u00a0</p>"
        },
        "title": "Southcentral Foundation Land Transfer Act of 2025"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/s/BILLSUM-119s2098.xml",
    "summary": {
      "actionDate": "2025-06-17",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Southcentral Foundation Land Transfer Act of 2025</strong></p><p>This bill directs the Department of Health and Human Services (HHS) to convey approximately 3.4 acres in Anchorage, Alaska, to the Southcentral Foundation (SCF) for use in connection with health and social services programs.</p><p>The conveyance must be made by warranty deed. The conveyance may not (1) require any consideration (such as payment) from the SCF for the property; (2) impose any obligation, term, or condition on the SCF relating to that property; or (3) allow for any U.S. reversionary interest in the property.</p><p>HHS must be accorded any easement or access to the property as may be reasonably necessary to satisfy any retained obligation or liability of HHS.</p><p>The bill prohibits the SCF from being liable for certain environmental contamination that occurred on or before the date on which the property is conveyed to the SCF. In turn, HHS may not be liable for any contamination that occurred after the date that the SCF controlled, occupied, and used the property.\u00a0</p>",
      "updateDate": "2026-04-17",
      "versionCode": "id119s2098"
    },
    "title": "Southcentral Foundation Land Transfer Act of 2025"
  },
  "summaries": [
    {
      "actionDate": "2025-06-17",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Southcentral Foundation Land Transfer Act of 2025</strong></p><p>This bill directs the Department of Health and Human Services (HHS) to convey approximately 3.4 acres in Anchorage, Alaska, to the Southcentral Foundation (SCF) for use in connection with health and social services programs.</p><p>The conveyance must be made by warranty deed. The conveyance may not (1) require any consideration (such as payment) from the SCF for the property; (2) impose any obligation, term, or condition on the SCF relating to that property; or (3) allow for any U.S. reversionary interest in the property.</p><p>HHS must be accorded any easement or access to the property as may be reasonably necessary to satisfy any retained obligation or liability of HHS.</p><p>The bill prohibits the SCF from being liable for certain environmental contamination that occurred on or before the date on which the property is conveyed to the SCF. In turn, HHS may not be liable for any contamination that occurred after the date that the SCF controlled, occupied, and used the property.\u00a0</p>",
      "updateDate": "2026-04-17",
      "versionCode": "id119s2098"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-06-17",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2098is.xml"
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
      "title": "Southcentral Foundation Land Transfer Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-05-21T11:03:37Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Southcentral Foundation Land Transfer Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-06-27T02:23:18Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to provide for the conveyance of certain property to the Southcentral Foundation located in Anchorage, Alaska, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-06-27T02:18:20Z"
    }
  ]
}
```
