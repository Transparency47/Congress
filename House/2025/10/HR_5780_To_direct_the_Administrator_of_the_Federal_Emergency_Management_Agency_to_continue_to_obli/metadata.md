# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/5780?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/5780
- Title: Federal Emergency Management Continuity Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 5780
- Origin chamber: House
- Introduced date: 2025-10-17
- Update date: 2025-12-02T09:05:38Z
- Update date including text: 2025-12-02T09:05:38Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-10-17: Introduced in House
- 2025-10-17 - IntroReferral: Introduced in House
- 2025-10-17 - IntroReferral: Introduced in House
- 2025-10-17 - IntroReferral: Referred to the House Committee on Transportation and Infrastructure.
- 2025-12-01 - Committee: Referred to the Subcommittee on Economic Development, Public Buildings, and Emergency Management.
- Latest action: 2025-10-17: Introduced in House

## Actions

- 2025-10-17 - IntroReferral: Introduced in House
- 2025-10-17 - IntroReferral: Introduced in House
- 2025-10-17 - IntroReferral: Referred to the House Committee on Transportation and Infrastructure.
- 2025-12-01 - Committee: Referred to the Subcommittee on Economic Development, Public Buildings, and Emergency Management.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-10-17",
    "latestAction": {
      "actionDate": "2025-10-17",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/5780",
    "number": "5780",
    "originChamber": "House",
    "policyArea": {
      "name": "Emergency Management"
    },
    "sponsors": [
      {
        "bioguideId": "M001217",
        "district": "23",
        "firstName": "Jared",
        "fullName": "Rep. Moskowitz, Jared [D-FL-23]",
        "lastName": "Moskowitz",
        "party": "D",
        "state": "FL"
      }
    ],
    "title": "Federal Emergency Management Continuity Act of 2025",
    "type": "HR",
    "updateDate": "2025-12-02T09:05:38Z",
    "updateDateIncludingText": "2025-12-02T09:05:38Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-12-01",
      "committees": {
        "item": {
          "name": "Economic Development, Public Buildings, and Emergency Management Subcommittee",
          "systemCode": "hspw13"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Referred to the Subcommittee on Economic Development, Public Buildings, and Emergency Management.",
      "type": "Committee"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-10-17",
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
      "actionDate": "2025-10-17",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-10-17",
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
          "date": "2025-10-17T18:00:05Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Transportation and Infrastructure Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": {
              "date": "2025-12-01T19:50:06Z",
              "name": "Referred to"
            }
          },
          "name": "Economic Development, Public Buildings, and Emergency Management Subcommittee",
          "systemCode": "hspw13"
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
      "bioguideId": "C001125",
      "district": "2",
      "firstName": "Troy",
      "fullName": "Rep. Carter, Troy A. [D-LA-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Carter",
      "middleName": "A.",
      "party": "D",
      "sponsorshipDate": "2025-10-17",
      "state": "LA"
    },
    {
      "bioguideId": "G000583",
      "district": "5",
      "firstName": "Josh",
      "fullName": "Rep. Gottheimer, Josh [D-NJ-5]",
      "isOriginalCosponsor": "False",
      "lastName": "Gottheimer",
      "party": "D",
      "sponsorshipDate": "2025-10-24",
      "state": "NJ"
    },
    {
      "bioguideId": "W000830",
      "district": "27",
      "firstName": "George",
      "fullName": "Rep. Whitesides, George [D-CA-27]",
      "isOriginalCosponsor": "False",
      "lastName": "Whitesides",
      "party": "D",
      "sponsorshipDate": "2025-10-28",
      "state": "CA"
    },
    {
      "bioguideId": "S001200",
      "district": "9",
      "firstName": "Darren",
      "fullName": "Rep. Soto, Darren [D-FL-9]",
      "isOriginalCosponsor": "False",
      "lastName": "Soto",
      "party": "D",
      "sponsorshipDate": "2025-11-04",
      "state": "FL"
    },
    {
      "bioguideId": "H001103",
      "district": "0",
      "firstName": "Pablo",
      "fullName": "Rescom. Hern\u00e1ndez, Pablo Jose [D-PR-At Large]",
      "isOriginalCosponsor": "False",
      "lastName": "Hern\u00e1ndez",
      "middleName": "Jose",
      "party": "D",
      "sponsorshipDate": "2025-11-04",
      "state": "PR"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr5780ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 5780\nIN THE HOUSE OF REPRESENTATIVES\nOctober 17, 2025 Mr. Moskowitz (for himself and Mr. Carter of Louisiana ) introduced the following bill; which was referred to the Committee on Transportation and Infrastructure\nA BILL\nTo direct the Administrator of the Federal Emergency Management Agency to continue to obligate and disburse covered funds in the Disaster Relief Fund during a lapse in appropriations, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Federal Emergency Management Continuity Act of 2025 .\n#### 2. Continuity of operations of FEMA\n##### (a) In general\nNotwithstanding any other provision of law, during a lapse in appropriations to the Federal Emergency Management Agency, the Administrator of the Agency shall continue obligating and disbursing covered funds available in the Disaster Relief Fund for covered programs.\n##### (b) Employees\nEmployees necessary to carry out disbursements or related program activities under subsection (a) shall be treated as excepted employees under section 1341 of title 31, United States Code (commonly referred to as the \u2018Anti-Deficiency Act') and such employees may not be subject to furlough or reduction in force due to the applicable lapse in appropriations.\n##### (c) Definitions\nIn this section:\n**(1) Covered funds**\nThe term covered funds means any funds in the Disaster Relief Fund that have been appropriated before the applicable lapse in appropriation and remain available to be expended.\n**(2) Covered programs**\nThe term covered program means any disaster relief, emergency assistance, and recovery program authorized under the Robert T. Stafford Disaster Relief and Emergency Assistance Act ( 42 U.S.C. 5121 et seq. ), including individual assistance under section 408 of such Act, public assistance under sections 403, 406, 407, and 502, and other disbursements and obligations made from the Disaster Relief Fund for programs or activities necessary to protect life and property during a lapse in appropriations.",
      "versionDate": "2025-10-17",
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
        "name": "Emergency Management",
        "updateDate": "2025-10-23T18:10:53Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-10-17",
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
          "measure-id": "id119hr5780",
          "measure-number": "5780",
          "measure-type": "hr",
          "orig-publish-date": "2025-10-17",
          "originChamber": "HOUSE",
          "update-date": "2025-10-23"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr5780v00",
            "update-date": "2025-10-23"
          },
          "action-date": "2025-10-17",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Federal Emergency Management Continuity Act of 2025</strong></p><p>This bill requires the Federal Emergency Management Agency (FEMA) to continue using certain funds in the Disaster Relief Fund (DRF) during a lapse in appropriations (i.e., government shutdown).</p><p>Specifically, FEMA must continue obligating and disbursing funds in the DRF that were appropriated before the lapse in appropriations and remain available to be expended. The funds may be used for any disaster relief, emergency assistance, and recovery program authorized under the Robert\u00a0T. Stafford Disaster Relief and Emergency Assistance Act, including individual assistance, public assistance, and other disbursements and obligations\u00a0for\u00a0programs or activities necessary to protect life and property during a lapse in appropriations.</p><p>The bill also requires employees who are necessary to carry out these disbursements or related program activities to be treated as excepted employees under the Anti-Deficiency Act. (Excepted employees are required to work during a lapse in appropriations.) The bill also prohibits these employees from being subject to a furlough or a reduction in force due to a lapse in appropriations.\u00a0</p>"
        },
        "title": "Federal Emergency Management Continuity Act of 2025"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr5780.xml",
    "summary": {
      "actionDate": "2025-10-17",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Federal Emergency Management Continuity Act of 2025</strong></p><p>This bill requires the Federal Emergency Management Agency (FEMA) to continue using certain funds in the Disaster Relief Fund (DRF) during a lapse in appropriations (i.e., government shutdown).</p><p>Specifically, FEMA must continue obligating and disbursing funds in the DRF that were appropriated before the lapse in appropriations and remain available to be expended. The funds may be used for any disaster relief, emergency assistance, and recovery program authorized under the Robert\u00a0T. Stafford Disaster Relief and Emergency Assistance Act, including individual assistance, public assistance, and other disbursements and obligations\u00a0for\u00a0programs or activities necessary to protect life and property during a lapse in appropriations.</p><p>The bill also requires employees who are necessary to carry out these disbursements or related program activities to be treated as excepted employees under the Anti-Deficiency Act. (Excepted employees are required to work during a lapse in appropriations.) The bill also prohibits these employees from being subject to a furlough or a reduction in force due to a lapse in appropriations.\u00a0</p>",
      "updateDate": "2025-10-23",
      "versionCode": "id119hr5780"
    },
    "title": "Federal Emergency Management Continuity Act of 2025"
  },
  "summaries": [
    {
      "actionDate": "2025-10-17",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Federal Emergency Management Continuity Act of 2025</strong></p><p>This bill requires the Federal Emergency Management Agency (FEMA) to continue using certain funds in the Disaster Relief Fund (DRF) during a lapse in appropriations (i.e., government shutdown).</p><p>Specifically, FEMA must continue obligating and disbursing funds in the DRF that were appropriated before the lapse in appropriations and remain available to be expended. The funds may be used for any disaster relief, emergency assistance, and recovery program authorized under the Robert\u00a0T. Stafford Disaster Relief and Emergency Assistance Act, including individual assistance, public assistance, and other disbursements and obligations\u00a0for\u00a0programs or activities necessary to protect life and property during a lapse in appropriations.</p><p>The bill also requires employees who are necessary to carry out these disbursements or related program activities to be treated as excepted employees under the Anti-Deficiency Act. (Excepted employees are required to work during a lapse in appropriations.) The bill also prohibits these employees from being subject to a furlough or a reduction in force due to a lapse in appropriations.\u00a0</p>",
      "updateDate": "2025-10-23",
      "versionCode": "id119hr5780"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-10-17",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr5780ih.xml"
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
      "title": "Federal Emergency Management Continuity Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-10-22T06:23:15Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Federal Emergency Management Continuity Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-10-22T06:23:14Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To direct the Administrator of the Federal Emergency Management Agency to continue to obligate and disburse covered funds in the Disaster Relief Fund during a lapse in appropriations, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-10-22T06:18:18Z"
    }
  ]
}
```
