# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/5695?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/5695
- Title: No Taxation Without Operation Act
- Congress: 119
- Bill type: HR
- Bill number: 5695
- Origin chamber: House
- Introduced date: 2025-10-06
- Update date: 2025-10-22T14:56:13Z
- Update date including text: 2025-10-22T14:56:13Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-10-06: Introduced in House
- 2025-10-06 - IntroReferral: Introduced in House
- 2025-10-06 - IntroReferral: Introduced in House
- 2025-10-06 - IntroReferral: Referred to the House Committee on Ways and Means.
- Latest action: 2025-10-06: Introduced in House

## Actions

- 2025-10-06 - IntroReferral: Introduced in House
- 2025-10-06 - IntroReferral: Introduced in House
- 2025-10-06 - IntroReferral: Referred to the House Committee on Ways and Means.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-10-06",
    "latestAction": {
      "actionDate": "2025-10-06",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/5695",
    "number": "5695",
    "originChamber": "House",
    "policyArea": {
      "name": "Taxation"
    },
    "sponsors": [
      {
        "bioguideId": "B001327",
        "district": "8",
        "firstName": "Robert",
        "fullName": "Rep. Bresnahan, Robert P. [R-PA-8]",
        "lastName": "Bresnahan",
        "party": "R",
        "state": "PA"
      }
    ],
    "title": "No Taxation Without Operation Act",
    "type": "HR",
    "updateDate": "2025-10-22T14:56:13Z",
    "updateDateIncludingText": "2025-10-22T14:56:13Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-10-06",
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
      "actionDate": "2025-10-06",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-10-06",
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
          "date": "2025-10-06T19:01:20Z",
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
      "bioguideId": "W000829",
      "district": "8",
      "firstName": "Tony",
      "fullName": "Rep. Wied, Tony [R-WI-8]",
      "isOriginalCosponsor": "False",
      "lastName": "Wied",
      "party": "R",
      "sponsorshipDate": "2025-10-14",
      "state": "WI"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr5695ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 5695\nIN THE HOUSE OF REPRESENTATIVES\nOctober 6, 2025 Mr. Bresnahan introduced the following bill; which was referred to the Committee on Ways and Means\nA BILL\nTo suspend Federal individual income taxes during a lapse in appropriations, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the No Taxation Without Operation Act .\n#### 2. Suspension of Federal income tax collection during a lapse in appropriations\n##### (a) In general\nNotwithstanding any other provision of law, during any partial or full government shutdown\u2014\n**(1)**\nno citizen subject to ordinary Federal income taxes on wages shall be liable for\u2014\n**(A)**\nFederal income taxes during the duration of a partial or full government shutdown, or\n**(B)**\nthe accrual of any penalty or interest with respect to any Federal individual income tax payment or any Federal individual income tax return,\n**(2)**\nfor any furloughed Federal employee or contractor who is furloughed or working without pay during a partial or full government shutdown and is subject to the Government Employee Fair Treatment Act of 2019, their backpay shall not be subject to Federal income taxes, and\n**(3)**\nthe Treasury Department shall issue guidelines for employers to ensure compliance of this Act for tipped, hourly wage, salaried, and all other covered employees.\n##### (b) Partial or full government shutdown\nFor purposes of this section, the term partial or full government shutdown means any period during which a lapse in Federal appropriations results in a partial or full government shutdown.",
      "versionDate": "2025-10-06",
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
        "updateDate": "2025-10-17T12:49:12Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-10-06",
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
          "measure-id": "id119hr5695",
          "measure-number": "5695",
          "measure-type": "hr",
          "orig-publish-date": "2025-10-06",
          "originChamber": "HOUSE",
          "update-date": "2025-10-22"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr5695v00",
            "update-date": "2025-10-22"
          },
          "action-date": "2025-10-06",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>No Taxation Without Operation Act</strong></p><p>This bill suspends the collection of certain federal income taxes during a partial or full government shutdown that occurs due to a lapse in appropriations.</p><p>If a partial or full government shutdown occurs, the bill provides that no citizen who is subject to ordinary federal income taxes on wages is liable for (1) federal income taxes during the shutdown, or (2) the accrual of any penalty or interest with respect to any federal individual income tax payment or any federal individual income tax return.</p><p>The bill also exempts back pay from federal income taxes if it is received by certain federal employees or contractors who were not paid during a government shutdown and are subject to the Government Employee Fair Treatment Act of 2019.\u00a0</p><p>The Department of the Treasury must issue guidelines for employers to ensure compliance with this bill for tipped, hourly wage, salaried, and all other covered employees.</p>"
        },
        "title": "No Taxation Without Operation Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr5695.xml",
    "summary": {
      "actionDate": "2025-10-06",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>No Taxation Without Operation Act</strong></p><p>This bill suspends the collection of certain federal income taxes during a partial or full government shutdown that occurs due to a lapse in appropriations.</p><p>If a partial or full government shutdown occurs, the bill provides that no citizen who is subject to ordinary federal income taxes on wages is liable for (1) federal income taxes during the shutdown, or (2) the accrual of any penalty or interest with respect to any federal individual income tax payment or any federal individual income tax return.</p><p>The bill also exempts back pay from federal income taxes if it is received by certain federal employees or contractors who were not paid during a government shutdown and are subject to the Government Employee Fair Treatment Act of 2019.\u00a0</p><p>The Department of the Treasury must issue guidelines for employers to ensure compliance with this bill for tipped, hourly wage, salaried, and all other covered employees.</p>",
      "updateDate": "2025-10-22",
      "versionCode": "id119hr5695"
    },
    "title": "No Taxation Without Operation Act"
  },
  "summaries": [
    {
      "actionDate": "2025-10-06",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>No Taxation Without Operation Act</strong></p><p>This bill suspends the collection of certain federal income taxes during a partial or full government shutdown that occurs due to a lapse in appropriations.</p><p>If a partial or full government shutdown occurs, the bill provides that no citizen who is subject to ordinary federal income taxes on wages is liable for (1) federal income taxes during the shutdown, or (2) the accrual of any penalty or interest with respect to any federal individual income tax payment or any federal individual income tax return.</p><p>The bill also exempts back pay from federal income taxes if it is received by certain federal employees or contractors who were not paid during a government shutdown and are subject to the Government Employee Fair Treatment Act of 2019.\u00a0</p><p>The Department of the Treasury must issue guidelines for employers to ensure compliance with this bill for tipped, hourly wage, salaried, and all other covered employees.</p>",
      "updateDate": "2025-10-22",
      "versionCode": "id119hr5695"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-10-06",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr5695ih.xml"
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
      "title": "No Taxation Without Operation Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-10-16T09:38:15Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "No Taxation Without Operation Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-10-16T09:38:13Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To suspend Federal individual income taxes during a lapse in appropriations, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-10-16T09:33:16Z"
    }
  ]
}
```
