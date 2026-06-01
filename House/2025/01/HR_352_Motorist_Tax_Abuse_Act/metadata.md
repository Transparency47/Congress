# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/352?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/hr/352
- Title: Motorist Tax Abuse Act
- Congress: 119
- Bill type: HR
- Bill number: 352
- Origin chamber: House
- Introduced date: 2025-01-13
- Update date: 2025-02-18T15:44:33Z
- Update date including text: 2025-02-18T15:44:33Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-01-13: Introduced in House
- 2025-01-13 - IntroReferral: Introduced in House
- 2025-01-13 - IntroReferral: Introduced in House
- 2025-01-13 - IntroReferral: Referred to the House Committee on Transportation and Infrastructure.
- 2025-01-14 - Committee: Referred to the Subcommittee on Highways and Transit.
- Latest action: 2025-01-13: Introduced in House

## Actions

- 2025-01-13 - IntroReferral: Introduced in House
- 2025-01-13 - IntroReferral: Introduced in House
- 2025-01-13 - IntroReferral: Referred to the House Committee on Transportation and Infrastructure.
- 2025-01-14 - Committee: Referred to the Subcommittee on Highways and Transit.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-01-13",
    "latestAction": {
      "actionDate": "2025-01-13",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/hr/352",
    "number": "352",
    "originChamber": "House",
    "policyArea": {
      "name": "Transportation and Public Works"
    },
    "sponsors": [
      {
        "bioguideId": "M000317",
        "district": "11",
        "firstName": "Nicole",
        "fullName": "Rep. Malliotakis, Nicole [R-NY-11]",
        "lastName": "Malliotakis",
        "party": "R",
        "state": "NY"
      }
    ],
    "title": "Motorist Tax Abuse Act",
    "type": "HR",
    "updateDate": "2025-02-18T15:44:33Z",
    "updateDateIncludingText": "2025-02-18T15:44:33Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-01-14",
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
      "actionDate": "2025-01-13",
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
      "actionDate": "2025-01-13",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-01-13",
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
          "date": "2025-01-13T17:04:15Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Transportation and Infrastructure Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": {
              "date": "2025-01-14T15:34:23Z",
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
      "isOriginalCosponsor": "False",
      "lastName": "Gottheimer",
      "party": "D",
      "sponsorshipDate": "2025-01-22",
      "state": "NJ"
    },
    {
      "bioguideId": "V000133",
      "district": "2",
      "firstName": "Jefferson",
      "fullName": "Rep. Van Drew, Jefferson [R-NJ-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Van Drew",
      "party": "R",
      "sponsorshipDate": "2025-01-22",
      "state": "NJ"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr352ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 352\nIN THE HOUSE OF REPRESENTATIVES\nJanuary 13, 2025 Ms. Malliotakis introduced the following bill; which was referred to the Committee on Transportation and Infrastructure\nA BILL\nTo amend the Intermodal Surface Transportation Efficiency Act of 1991 to prohibit cordon pricing in the Central Business District Tolling Program for New York City, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Motorist Tax Abuse Act .\n#### 2. Prohibition on congestion pricing\nSection 1012(b) of the Intermodal Surface Transportation Efficiency Act of 1991 ( 23 U.S.C. 149 note) is amended by adding at the end the following:\n(9) Prohibition on congestion pricing Notwithstanding any other provision of this subsection, the Secretary may not establish or maintain cordon pricing under the value pricing pilot program under this section for the Central Business District Tolling Program for New York City. .",
      "versionDate": "2025-01-13",
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
        "updateDate": "2025-02-12T16:33:19Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-01-13",
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
          "measure-id": "id119hr352",
          "measure-number": "352",
          "measure-type": "hr",
          "orig-publish-date": "2025-01-13",
          "originChamber": "HOUSE",
          "update-date": "2025-02-18"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr352v00",
            "update-date": "2025-02-18"
          },
          "action-date": "2025-01-13",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Motorist Tax Abuse Act</strong></p><p>This bill prohibits the Federal Highway Administration (FHWA) from establishing or maintaining cordon pricing for the Central Business District Tolling Program\u00a0for New York City\u00a0under the FHWA's Value Pricing Pilot Program. The New York program charges drivers a toll to enter an area in Manhattan designated as the Congestion Relief Zone.</p><p> In general, cordon pricing is a form of congestion pricing that includes a zone-based pricing system that involves either variable or fixed charges to drive within or into a congested area within a city.</p>"
        },
        "title": "Motorist Tax Abuse Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr352.xml",
    "summary": {
      "actionDate": "2025-01-13",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Motorist Tax Abuse Act</strong></p><p>This bill prohibits the Federal Highway Administration (FHWA) from establishing or maintaining cordon pricing for the Central Business District Tolling Program\u00a0for New York City\u00a0under the FHWA's Value Pricing Pilot Program. The New York program charges drivers a toll to enter an area in Manhattan designated as the Congestion Relief Zone.</p><p> In general, cordon pricing is a form of congestion pricing that includes a zone-based pricing system that involves either variable or fixed charges to drive within or into a congested area within a city.</p>",
      "updateDate": "2025-02-18",
      "versionCode": "id119hr352"
    },
    "title": "Motorist Tax Abuse Act"
  },
  "summaries": [
    {
      "actionDate": "2025-01-13",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Motorist Tax Abuse Act</strong></p><p>This bill prohibits the Federal Highway Administration (FHWA) from establishing or maintaining cordon pricing for the Central Business District Tolling Program\u00a0for New York City\u00a0under the FHWA's Value Pricing Pilot Program. The New York program charges drivers a toll to enter an area in Manhattan designated as the Congestion Relief Zone.</p><p> In general, cordon pricing is a form of congestion pricing that includes a zone-based pricing system that involves either variable or fixed charges to drive within or into a congested area within a city.</p>",
      "updateDate": "2025-02-18",
      "versionCode": "id119hr352"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-01-13",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr352ih.xml"
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
      "title": "Motorist Tax Abuse Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-02-11T05:53:21Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Motorist Tax Abuse Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-02-11T05:53:19Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Intermodal Surface Transportation Efficiency Act of 1991 to prohibit cordon pricing in the Central Business District Tolling Program for New York City, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-02-11T05:48:30Z"
    }
  ]
}
```
