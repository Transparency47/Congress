# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/4809?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/4809
- Title: INSPECT Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 4809
- Origin chamber: House
- Introduced date: 2025-07-29
- Update date: 2026-04-06T13:18:03Z
- Update date including text: 2026-04-06T13:18:03Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-07-29: Introduced in House
- 2025-07-29 - IntroReferral: Introduced in House
- 2025-07-29 - IntroReferral: Introduced in House
- 2025-07-29 - IntroReferral: Referred to the House Committee on Energy and Commerce.
- Latest action: 2025-07-29: Introduced in House

## Actions

- 2025-07-29 - IntroReferral: Introduced in House
- 2025-07-29 - IntroReferral: Introduced in House
- 2025-07-29 - IntroReferral: Referred to the House Committee on Energy and Commerce.

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
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/4809",
    "number": "4809",
    "originChamber": "House",
    "policyArea": {
      "name": "Energy"
    },
    "sponsors": [
      {
        "bioguideId": "L000593",
        "district": "49",
        "firstName": "Mike",
        "fullName": "Rep. Levin, Mike [D-CA-49]",
        "lastName": "Levin",
        "party": "D",
        "state": "CA"
      }
    ],
    "title": "INSPECT Act of 2025",
    "type": "HR",
    "updateDate": "2026-04-06T13:18:03Z",
    "updateDateIncludingText": "2026-04-06T13:18:03Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-07-29",
      "committees": {
        "item": {
          "name": "Energy and Commerce Committee",
          "systemCode": "hsif00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Energy and Commerce.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-07-29",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-07-29",
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
          "date": "2025-07-29T21:03:10Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Energy and Commerce Committee",
      "systemCode": "hsif00",
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
      "bioguideId": "L000599",
      "district": "17",
      "firstName": "Michael",
      "fullName": "Rep. Lawler, Michael [R-NY-17]",
      "isOriginalCosponsor": "True",
      "lastName": "Lawler",
      "party": "R",
      "sponsorshipDate": "2025-07-29",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr4809ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 4809\nIN THE HOUSE OF REPRESENTATIVES\nJuly 29, 2025 Mr. Levin (for himself and Mr. Lawler ) introduced the following bill; which was referred to the Committee on Energy and Commerce\nA BILL\nTo assign a resident inspector to certain commercial nuclear power plants to conduct inspections of decommissioning activities and spent nuclear fuel transfer activities.\n#### 1. Short title\nThis Act may be cited as the Increasing Nuclear Safety Protocols for Extended Canister Transfers Act of 2025 or the INSPECT Act of 2025 .\n#### 2. Inspection of decommissioning activity and spent nuclear fuel transfer activity\n##### (a) In general\nThe Nuclear Regulatory Commission shall assign, for the duration described in subsection (b), a resident inspector to each commercial nuclear power plant that has permanently ceased operation to conduct inspections of decommissioning activities and spent nuclear fuel transfer activities of the commercial nuclear power plant.\n##### (b) Duration described\nThe duration described in this subsection is the period of time it takes to transfer all spent nuclear fuel from the spent fuel pools of the commercial nuclear power plant to dry storage.\n##### (c) Reassignment\nIf there are no decommissioning activities or spent nuclear fuel transfer activities at the commercial nuclear power plant to which a resident inspector is assigned under subsection (a), the Nuclear Regulatory Commission may assign such resident inspector to other duties as may be appropriate.",
      "versionDate": "2025-07-29",
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
        "name": "Energy",
        "updateDate": "2025-09-17T15:34:15Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-07-29",
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
          "measure-id": "id119hr4809",
          "measure-number": "4809",
          "measure-type": "hr",
          "orig-publish-date": "2025-07-29",
          "originChamber": "HOUSE",
          "update-date": "2026-04-06"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr4809v00",
            "update-date": "2026-04-06"
          },
          "action-date": "2025-07-29",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Increasing Nuclear Safety Protocols for Extended Canister Transfers Act of 2025 or the INSPECT Act\u00a0of 2025</strong></p><p>This bill requires the Nuclear Regulatory Commission to assign a resident inspector to each commercial nuclear power plant that has permanently ceased operation. The inspector must (1) conduct inspections of decommissioning activities and spent nuclear fuel transfer activities, and (2) remain at the plant until all fuel is transferred from its spent fuel pools to dry storage.</p>"
        },
        "title": "INSPECT Act of 2025"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr4809.xml",
    "summary": {
      "actionDate": "2025-07-29",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Increasing Nuclear Safety Protocols for Extended Canister Transfers Act of 2025 or the INSPECT Act\u00a0of 2025</strong></p><p>This bill requires the Nuclear Regulatory Commission to assign a resident inspector to each commercial nuclear power plant that has permanently ceased operation. The inspector must (1) conduct inspections of decommissioning activities and spent nuclear fuel transfer activities, and (2) remain at the plant until all fuel is transferred from its spent fuel pools to dry storage.</p>",
      "updateDate": "2026-04-06",
      "versionCode": "id119hr4809"
    },
    "title": "INSPECT Act of 2025"
  },
  "summaries": [
    {
      "actionDate": "2025-07-29",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Increasing Nuclear Safety Protocols for Extended Canister Transfers Act of 2025 or the INSPECT Act\u00a0of 2025</strong></p><p>This bill requires the Nuclear Regulatory Commission to assign a resident inspector to each commercial nuclear power plant that has permanently ceased operation. The inspector must (1) conduct inspections of decommissioning activities and spent nuclear fuel transfer activities, and (2) remain at the plant until all fuel is transferred from its spent fuel pools to dry storage.</p>",
      "updateDate": "2026-04-06",
      "versionCode": "id119hr4809"
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
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr4809ih.xml"
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
      "title": "INSPECT Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-08-06T05:53:24Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "INSPECT Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-08-06T05:53:22Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Increasing Nuclear Safety Protocols for Extended Canister Transfers Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-08-06T05:53:22Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To assign a resident inspector to certain commercial nuclear power plants to conduct inspections of decommissioning activities and spent nuclear fuel transfer activities.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-08-06T05:48:57Z"
    }
  ]
}
```
