# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/616?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/616
- Title: To amend the Internal Revenue Code of 1986 to double the dollar limitation for the energy efficient home improvement credit with respect to heat pumps, heat pump water heaters, biomass stoves, and boilers.
- Congress: 119
- Bill type: HR
- Bill number: 616
- Origin chamber: House
- Introduced date: 2025-01-22
- Update date: 2025-09-10T20:24:04Z
- Update date including text: 2025-09-10T20:24:04Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-01-22: Introduced in House
- 2025-01-22 - IntroReferral: Introduced in House
- 2025-01-22 - IntroReferral: Introduced in House
- 2025-01-22 - IntroReferral: Referred to the House Committee on Ways and Means.
- Latest action: 2025-01-22: Introduced in House

## Actions

- 2025-01-22 - IntroReferral: Introduced in House
- 2025-01-22 - IntroReferral: Introduced in House
- 2025-01-22 - IntroReferral: Referred to the House Committee on Ways and Means.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-01-22",
    "latestAction": {
      "actionDate": "2025-01-22",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/616",
    "number": "616",
    "originChamber": "House",
    "policyArea": {
      "name": "Taxation"
    },
    "sponsors": [
      {
        "bioguideId": "G000583",
        "district": "5",
        "firstName": "Josh",
        "fullName": "Rep. Gottheimer, Josh [D-NJ-5]",
        "lastName": "Gottheimer",
        "party": "D",
        "state": "NJ"
      }
    ],
    "title": "To amend the Internal Revenue Code of 1986 to double the dollar limitation for the energy efficient home improvement credit with respect to heat pumps, heat pump water heaters, biomass stoves, and boilers.",
    "type": "HR",
    "updateDate": "2025-09-10T20:24:04Z",
    "updateDateIncludingText": "2025-09-10T20:24:04Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-01-22",
      "committees": {
        "item": {
          "name": "Ways and Means Committee",
          "systemCode": "hswm00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Ways and Means.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-01-22",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-01-22",
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
          "date": "2025-01-22T15:04:35Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Ways and Means Committee",
      "systemCode": "hswm00",
      "type": "Standing"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr616ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 616\nIN THE HOUSE OF REPRESENTATIVES\nJanuary 22, 2025 Mr. Gottheimer introduced the following bill; which was referred to the Committee on Ways and Means\nA BILL\nTo amend the Internal Revenue Code of 1986 to double the dollar limitation for the energy efficient home improvement credit with respect to heat pumps, heat pump water heaters, biomass stoves, and boilers.\n#### 1. Increased limitation for heat pump and heat pump water heaters; biomass stoves and boilers\n##### (a) In general\nSection 25C(b)(5) of the Internal Revenue Code of 1986 is amended by striking $2,000 and inserting $4,000 .\n##### (b) Effective date\nThe amendment made by this section shall apply to taxable years beginning after December 31, 2024.",
      "versionDate": "2025-01-22",
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
      "legislativeSubjects": {
        "item": [
          {
            "name": "Alternative and renewable resources",
            "updateDate": "2025-09-10T20:24:04Z"
          },
          {
            "name": "Energy efficiency and conservation",
            "updateDate": "2025-09-10T20:23:37Z"
          },
          {
            "name": "Income tax credits",
            "updateDate": "2025-09-10T20:23:21Z"
          },
          {
            "name": "Lighting, heating, cooling",
            "updateDate": "2025-09-10T20:23:28Z"
          },
          {
            "name": "Residential rehabilitation and home repair",
            "updateDate": "2025-09-10T20:23:48Z"
          }
        ]
      },
      "policyArea": {
        "name": "Taxation",
        "updateDate": "2025-02-25T20:35:17Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-01-22",
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
          "measure-id": "id119hr616",
          "measure-number": "616",
          "measure-type": "hr",
          "orig-publish-date": "2025-01-22",
          "originChamber": "HOUSE",
          "update-date": "2025-04-17"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr616v00",
            "update-date": "2025-04-17"
          },
          "action-date": "2025-01-22",
          "action-desc": "Introduced in House",
          "summary-text": "<p>This bill increases the limit on the energy efficient home improvement tax credit to $4,000 (from $2,000) for the cost of an electric or natural gas heat pump, an electric or natural gas heat pump water heater, a biomass stove, or a biomass boiler.</p><p>Under current law, a taxpayer may claim a nonrefundable tax credit of 30% of the cost, up to $2,000, for an electric or natural gas heat pump, an electric or natural gas heat pump water heater, a biomass stove, or a biomass boiler for a principal residence. (Under current law, taxpayers may also claim a nonrefundable tax credit of 30% of the costs, up to $1,200, for certain other eligible energy-efficient property such that some taxpayers may qualify for a maximum tax credit of $3,200.)</p>"
        },
        "title": "To amend the Internal Revenue Code of 1986 to double the dollar limitation for the energy efficient home improvement credit with respect to heat pumps, heat pump water heaters, biomass stoves, and boilers."
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr616.xml",
    "summary": {
      "actionDate": "2025-01-22",
      "actionDesc": "Introduced in House",
      "text": "<p>This bill increases the limit on the energy efficient home improvement tax credit to $4,000 (from $2,000) for the cost of an electric or natural gas heat pump, an electric or natural gas heat pump water heater, a biomass stove, or a biomass boiler.</p><p>Under current law, a taxpayer may claim a nonrefundable tax credit of 30% of the cost, up to $2,000, for an electric or natural gas heat pump, an electric or natural gas heat pump water heater, a biomass stove, or a biomass boiler for a principal residence. (Under current law, taxpayers may also claim a nonrefundable tax credit of 30% of the costs, up to $1,200, for certain other eligible energy-efficient property such that some taxpayers may qualify for a maximum tax credit of $3,200.)</p>",
      "updateDate": "2025-04-17",
      "versionCode": "id119hr616"
    },
    "title": "To amend the Internal Revenue Code of 1986 to double the dollar limitation for the energy efficient home improvement credit with respect to heat pumps, heat pump water heaters, biomass stoves, and boilers."
  },
  "summaries": [
    {
      "actionDate": "2025-01-22",
      "actionDesc": "Introduced in House",
      "text": "<p>This bill increases the limit on the energy efficient home improvement tax credit to $4,000 (from $2,000) for the cost of an electric or natural gas heat pump, an electric or natural gas heat pump water heater, a biomass stove, or a biomass boiler.</p><p>Under current law, a taxpayer may claim a nonrefundable tax credit of 30% of the cost, up to $2,000, for an electric or natural gas heat pump, an electric or natural gas heat pump water heater, a biomass stove, or a biomass boiler for a principal residence. (Under current law, taxpayers may also claim a nonrefundable tax credit of 30% of the costs, up to $1,200, for certain other eligible energy-efficient property such that some taxpayers may qualify for a maximum tax credit of $3,200.)</p>",
      "updateDate": "2025-04-17",
      "versionCode": "id119hr616"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-01-22",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr616ih.xml"
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
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Internal Revenue Code of 1986 to double the dollar limitation for the energy efficient home improvement credit with respect to heat pumps, heat pump water heaters, biomass stoves, and boilers.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-02-21T06:49:30Z"
    },
    {
      "title": "To amend the Internal Revenue Code of 1986 to double the dollar limitation for the energy efficient home improvement credit with respect to heat pumps, heat pump water heaters, biomass stoves, and boilers.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-01-23T09:05:30Z"
    }
  ]
}
```
