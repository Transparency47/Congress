# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/2838?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/2838
- Title: Ending Intermittent Energy Subsidies Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 2838
- Origin chamber: House
- Introduced date: 2025-04-10
- Update date: 2026-04-15T13:29:06Z
- Update date including text: 2026-04-15T13:29:06Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-04-10: Introduced in House
- 2025-04-10 - IntroReferral: Introduced in House
- 2025-04-10 - IntroReferral: Introduced in House
- 2025-04-10 - IntroReferral: Referred to the House Committee on Ways and Means.
- Latest action: 2025-04-10: Introduced in House

## Actions

- 2025-04-10 - IntroReferral: Introduced in House
- 2025-04-10 - IntroReferral: Introduced in House
- 2025-04-10 - IntroReferral: Referred to the House Committee on Ways and Means.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-04-10",
    "latestAction": {
      "actionDate": "2025-04-10",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/2838",
    "number": "2838",
    "originChamber": "House",
    "policyArea": {
      "name": "Taxation"
    },
    "sponsors": [
      {
        "bioguideId": "F000482",
        "district": "",
        "firstName": "Julie",
        "fullName": "Rep. Fedorchak, Julie [R-ND-At Large]",
        "lastName": "Fedorchak",
        "party": "R",
        "state": "ND"
      }
    ],
    "title": "Ending Intermittent Energy Subsidies Act of 2025",
    "type": "HR",
    "updateDate": "2026-04-15T13:29:06Z",
    "updateDateIncludingText": "2026-04-15T13:29:06Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-04-10",
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
      "actionDate": "2025-04-10",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-04-10",
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
          "date": "2025-04-10T13:05:50Z",
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

## API Data: cosponsors

```json
{
  "cosponsors": [
    {
      "bioguideId": "G000601",
      "district": "12",
      "firstName": "Craig",
      "fullName": "Rep. Goldman, Craig [R-TX-12]",
      "isOriginalCosponsor": "True",
      "lastName": "Goldman",
      "middleName": "A.",
      "party": "R",
      "sponsorshipDate": "2025-04-10",
      "state": "TX"
    },
    {
      "bioguideId": "P000609",
      "district": "6",
      "firstName": "Gary",
      "fullName": "Rep. Palmer, Gary J. [R-AL-6]",
      "isOriginalCosponsor": "True",
      "lastName": "Palmer",
      "middleName": "J.",
      "party": "R",
      "sponsorshipDate": "2025-04-10",
      "state": "AL"
    },
    {
      "bioguideId": "W000814",
      "district": "14",
      "firstName": "Randy",
      "fullName": "Rep. Weber, Randy K. Sr. [R-TX-14]",
      "isOriginalCosponsor": "True",
      "lastName": "Weber",
      "middleName": "K.",
      "party": "R",
      "sponsorshipDate": "2025-04-10",
      "state": "TX"
    },
    {
      "bioguideId": "P000048",
      "district": "11",
      "firstName": "August",
      "fullName": "Rep. Pfluger, August [R-TX-11]",
      "isOriginalCosponsor": "False",
      "lastName": "Pfluger",
      "party": "R",
      "sponsorshipDate": "2025-04-24",
      "state": "TX"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr2838ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 2838\nIN THE HOUSE OF REPRESENTATIVES\nApril 10, 2025 Ms. Fedorchak (for herself, Mr. Goldman of Texas , Mr. Palmer , and Mr. Weber of Texas ) introduced the following bill; which was referred to the Committee on Ways and Means\nA BILL\nTo amend the Internal Revenue Code of 1986 to phase-out the clean electricity production and investment credits with respect to wind and solar energy.\n#### 1. Short title\nThis Act may be cited as the Ending Intermittent Energy Subsidies Act of 2025 .\n#### 2. Termination of transferability of portion of clean electricity credits attributable to wind or solar energy\n##### (a) Clean electricity production credit\nSection 6418(f)(1)(A)(vii) of the Internal Revenue Code of 1986 is amended to read as follows:\n(vii) so much of the clean electricity production credit determined under section 45Y as is not attributable to electricity produced using solar or wind energy. .\n##### (b) Clean electricity investment credit\nSection 6418(f)(1)(A)(xi) of such Code is amended to read as follows:\n(xi) so much of the clean electricity investment credit determined under section 48E as is not allowed with respect to a qualified facility (as defined in such section) which is used for the generation of electricity using wind or solar energy. .\n##### (c) Effective date\nThe amendment made by this section shall apply to taxable years beginning after the date of the enactment of this Act.\n#### 3. Phase-out of clean electricity production credit with respect to solar and wind power\n##### (a) In general\nSection 45Y(d) of the Internal Revenue Code of 1986 is amended by adding at the end the following new paragraph:\n(4) Special rule for solar and wind energy In the case of electricity produced from solar or wind energy, the amount of the credit determined under subsection (a) (determined without regard to this paragraph) shall be equal to the product of the amount otherwise so determined, multiplied by\u2014 (A) in the case of electricity produced during the first calendar year beginning after the date of the enactment of the Ending Intermittent Energy Subsidies Act of 2025 , 80 percent, (B) in the case of electricity produced during the second calendar year beginning after the date of the enactment of the Ending Intermittent Energy Subsidies Act of 2025 , 60 percent, (C) in the case of electricity produced during the third calendar year beginning after the date of the enactment of the Ending Intermittent Energy Subsidies Act of 2025 , 40 percent, (D) in the case of electricity produced during the fourth calendar year beginning after the date of the enactment of the Ending Intermittent Energy Subsidies Act of 2025 , 20 percent, or (E) in the case of electricity produced after such fourth calendar year, zero percent, .\n##### (b) Effective date\nThe amendments made by this section shall apply to electricity produced after the date of the enactment of this Act.\n#### 4. Phase-out of clean electricity investment credit\n##### (a) In general\nSection 48E(e) of the Internal Revenue Code of 1986 is amended by adding at the end the following new paragraph:\n(4) Special rule for solar and wind energy The amount of the clean electricity investment credit under subsection (a) with respect to any qualified investment in a qualified facility which generates electricity using wind or solar energy shall be equal to the product of\u2014 (A) the amount of the credit determined under subsection (a) without regard to this subsection, multiplied by (B) in the case of a facility placed in service\u2014 (i) during the first calendar year beginning after the date of the enactment of the Ending Intermittent Energy Subsidies Act of 2025 , 80 percent, (ii) during the second calendar year beginning after the date of the enactment of the Ending Intermittent Energy Subsidies Act of 2025 , 60 percent, (iii) during the third calendar year beginning after the date of the enactment of the Ending Intermittent Energy Subsidies Act of 2025 , 40 percent, (iv) during the fourth calendar year beginning after the date of the enactment of the Ending Intermittent Energy Subsidies Act of 2025 , 20 percent, or (v) after such fourth calendar year, zero percent, .\n##### (b) Effective date\nThe amendments made by this section shall apply to property placed in service after the date of the enactment of this Act.",
      "versionDate": "2025-04-10",
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
        "name": "Taxation",
        "updateDate": "2025-05-28T13:58:31Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-04-10",
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
          "measure-id": "id119hr2838",
          "measure-number": "2838",
          "measure-type": "hr",
          "orig-publish-date": "2025-04-10",
          "originChamber": "HOUSE",
          "update-date": "2026-04-15"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr2838v00",
            "update-date": "2026-04-15"
          },
          "action-date": "2025-04-10",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Ending Intermittent Energy Subsidies Act of 2025</strong></p><p>This bill phases out and eliminates the ability to transfer federal tax credits for solar and wind investments and energy production.\u00a0</p><p>Specifically, the bill phases out over five years the (1) clean electricity investment tax credit for investments in a facility that generates electricity using\u00a0solar or wind energy, and (2) clean electricity production tax credit for electricity produced from solar or wind energy.\u00a0</p><p>Further, the bill eliminates the ability of a taxpayer to transfer to a third\u00a0party in exchange for cash any portion of the clean electricity investment tax credit and clean electricity production tax credit attributable to solar or wind energy.</p>"
        },
        "title": "Ending Intermittent Energy Subsidies Act of 2025"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr2838.xml",
    "summary": {
      "actionDate": "2025-04-10",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Ending Intermittent Energy Subsidies Act of 2025</strong></p><p>This bill phases out and eliminates the ability to transfer federal tax credits for solar and wind investments and energy production.\u00a0</p><p>Specifically, the bill phases out over five years the (1) clean electricity investment tax credit for investments in a facility that generates electricity using\u00a0solar or wind energy, and (2) clean electricity production tax credit for electricity produced from solar or wind energy.\u00a0</p><p>Further, the bill eliminates the ability of a taxpayer to transfer to a third\u00a0party in exchange for cash any portion of the clean electricity investment tax credit and clean electricity production tax credit attributable to solar or wind energy.</p>",
      "updateDate": "2026-04-15",
      "versionCode": "id119hr2838"
    },
    "title": "Ending Intermittent Energy Subsidies Act of 2025"
  },
  "summaries": [
    {
      "actionDate": "2025-04-10",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Ending Intermittent Energy Subsidies Act of 2025</strong></p><p>This bill phases out and eliminates the ability to transfer federal tax credits for solar and wind investments and energy production.\u00a0</p><p>Specifically, the bill phases out over five years the (1) clean electricity investment tax credit for investments in a facility that generates electricity using\u00a0solar or wind energy, and (2) clean electricity production tax credit for electricity produced from solar or wind energy.\u00a0</p><p>Further, the bill eliminates the ability of a taxpayer to transfer to a third\u00a0party in exchange for cash any portion of the clean electricity investment tax credit and clean electricity production tax credit attributable to solar or wind energy.</p>",
      "updateDate": "2026-04-15",
      "versionCode": "id119hr2838"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-04-10",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr2838ih.xml"
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
      "title": "Ending Intermittent Energy Subsidies Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-04-29T04:23:19Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Ending Intermittent Energy Subsidies Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-04-29T04:23:17Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Internal Revenue Code of 1986 to phase-out the clean electricity production and investment credits with respect to wind and solar energy.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-04-29T04:18:27Z"
    }
  ]
}
```
