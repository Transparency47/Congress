# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/4940?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/4940
- Title: AIRFARE Act
- Congress: 119
- Bill type: HR
- Bill number: 4940
- Origin chamber: House
- Introduced date: 2025-08-08
- Update date: 2026-05-16T08:07:52Z
- Update date including text: 2026-05-16T08:07:52Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-08-08: Introduced in House
- 2025-08-08 - IntroReferral: Introduced in House
- 2025-08-08 - IntroReferral: Introduced in House
- 2025-08-08 - IntroReferral: Referred to the House Committee on Homeland Security.
- 2025-08-11 - Committee: Referred to the Subcommittee on Transportation and Maritime Security.
- Latest action: 2025-08-08: Introduced in House

## Actions

- 2025-08-08 - IntroReferral: Introduced in House
- 2025-08-08 - IntroReferral: Introduced in House
- 2025-08-08 - IntroReferral: Referred to the House Committee on Homeland Security.
- 2025-08-11 - Committee: Referred to the Subcommittee on Transportation and Maritime Security.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-08-08",
    "latestAction": {
      "actionDate": "2025-08-08",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/4940",
    "number": "4940",
    "originChamber": "House",
    "policyArea": {
      "name": "Transportation and Public Works"
    },
    "sponsors": [
      {
        "bioguideId": "S001214",
        "district": "17",
        "firstName": "W.",
        "fullName": "Rep. Steube, W. Gregory [R-FL-17]",
        "lastName": "Steube",
        "party": "R",
        "state": "FL"
      }
    ],
    "title": "AIRFARE Act",
    "type": "HR",
    "updateDate": "2026-05-16T08:07:52Z",
    "updateDateIncludingText": "2026-05-16T08:07:52Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-08-11",
      "committees": {
        "item": {
          "name": "Transportation and Maritime Security Subcommittee",
          "systemCode": "hshm07"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Referred to the Subcommittee on Transportation and Maritime Security.",
      "type": "Committee"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-08-08",
      "committees": {
        "item": {
          "name": "Homeland Security Committee",
          "systemCode": "hshm00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Homeland Security.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-08-08",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-08-08",
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
          "date": "2025-08-08T15:31:35Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Homeland Security Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": {
              "date": "2025-08-11T20:19:39Z",
              "name": "Referred to"
            }
          },
          "name": "Transportation and Maritime Security Subcommittee",
          "systemCode": "hshm07"
        }
      },
      "systemCode": "hshm00",
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
      "bioguideId": "V000138",
      "district": "7",
      "firstName": "Eugene",
      "fullName": "Rep. Vindman, Eugene Simon [D-VA-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Vindman",
      "middleName": "Simon",
      "party": "D",
      "sponsorshipDate": "2025-09-10",
      "state": "VA"
    },
    {
      "bioguideId": "M001229",
      "district": "10",
      "firstName": "LaMonica",
      "fullName": "Rep. McIver, LaMonica [D-NJ-10]",
      "isOriginalCosponsor": "False",
      "lastName": "McIver",
      "party": "D",
      "sponsorshipDate": "2025-10-21",
      "state": "NJ"
    },
    {
      "bioguideId": "T000491",
      "district": "45",
      "firstName": "Derek",
      "fullName": "Rep. Tran, Derek [D-CA-45]",
      "isOriginalCosponsor": "False",
      "lastName": "Tran",
      "party": "D",
      "sponsorshipDate": "2026-01-07",
      "state": "CA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr4940ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 4940\nIN THE HOUSE OF REPRESENTATIVES\nAugust 8, 2025 Mr. Steube introduced the following bill; which was referred to the Committee on Homeland Security\nA BILL\nTo establish a system to expedite gate passes and flight access procedures at domestic airports to allow caregivers, parents, and guardians to accompany minors and passengers needing assistance to their flights, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Accommodating Individuals Requesting Familial Assistance in Riding Efficiently Act or the AIRFARE Act .\n#### 2. Establishment of system to expedite gate passes and flight access procedures to allow caregivers, parents, and guardians to accompany minors and passengers needing assistance to their flights\n##### (a) Definitions\nIn this section:\n**(1) Caregivers**\nThe term caregivers means individuals responsible for the care of minors or passengers needing assistance.\n**(2) Minors**\nThe term minors means individuals under the age of 18.\n**(3) Passengers needing assistance**\nThe term passengers needing assistance means individuals requiring special assistance related to their health or mobility, such as wheelchair users.\n##### (b) Implementation\nNot later than 180 days after the date of the enactment of this Act, the Administrator of the Transportation Security Administration (TSA) shall establish a system at domestic airports to expedite gate passes and flight access procedures. The system shall ensure the following:\n**(1)**\nAir carriers may offer up to two gate passes to caregivers, parents, and guardians who are accompanying a minor or a passenger needing assistance to a departing flight.\n**(2)**\nIf applicable, caregivers, parents, and guardians may apply their existing TSA Pre-Check privileges to such gate passes via their Known Traveler Numbers, and such gate passes shall note such status in the same manner and to the same extent as such status would be noted on a ticket issued to such caregivers, parents, and guardians.\n##### (c) Requirement\nIn the case of a passenger needing assistance who makes use of a wheelchair, a gate pass may be issued to a caregiver of such passenger pursuant to subsection (b) only if such caregiver is the individual pushing such wheelchair.",
      "versionDate": "2025-08-08",
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
        "updateDate": "2025-09-18T20:13:41Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-08-08",
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
          "measure-id": "id119hr4940",
          "measure-number": "4940",
          "measure-type": "hr",
          "orig-publish-date": "2025-08-08",
          "originChamber": "HOUSE",
          "update-date": "2026-04-07"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr4940v00",
            "update-date": "2026-04-07"
          },
          "action-date": "2025-08-08",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Accommodating Individuals Requesting Familial Assistance in Riding Efficiently Act or the AIRFARE Act</strong></p><p>This bill directs the Transportation Security Administration (TSA) to allow caregivers, parents, and guardians to accompany minors and passengers needing assistance to their flights.</p><p>Specifically, the TSA must establish a system to expedite gate passes and flight access procedures for these individuals.</p><p>The system must ensure that</p><ul><li>air carriers may offer up to two gate passes to caregivers, parents, and guardians who are accompanying a minor or a passenger needing assistance to a departing flight; and</li><li>these individuals may apply their existing\u00a0TSA PreCheck privileges to such gate passes.</li></ul><p>The\u00a0TSA\u00a0PreCheck\u00a0program expedites traveler screening through participating\u00a0TSA security checkpoints.</p>"
        },
        "title": "AIRFARE Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr4940.xml",
    "summary": {
      "actionDate": "2025-08-08",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Accommodating Individuals Requesting Familial Assistance in Riding Efficiently Act or the AIRFARE Act</strong></p><p>This bill directs the Transportation Security Administration (TSA) to allow caregivers, parents, and guardians to accompany minors and passengers needing assistance to their flights.</p><p>Specifically, the TSA must establish a system to expedite gate passes and flight access procedures for these individuals.</p><p>The system must ensure that</p><ul><li>air carriers may offer up to two gate passes to caregivers, parents, and guardians who are accompanying a minor or a passenger needing assistance to a departing flight; and</li><li>these individuals may apply their existing\u00a0TSA PreCheck privileges to such gate passes.</li></ul><p>The\u00a0TSA\u00a0PreCheck\u00a0program expedites traveler screening through participating\u00a0TSA security checkpoints.</p>",
      "updateDate": "2026-04-07",
      "versionCode": "id119hr4940"
    },
    "title": "AIRFARE Act"
  },
  "summaries": [
    {
      "actionDate": "2025-08-08",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Accommodating Individuals Requesting Familial Assistance in Riding Efficiently Act or the AIRFARE Act</strong></p><p>This bill directs the Transportation Security Administration (TSA) to allow caregivers, parents, and guardians to accompany minors and passengers needing assistance to their flights.</p><p>Specifically, the TSA must establish a system to expedite gate passes and flight access procedures for these individuals.</p><p>The system must ensure that</p><ul><li>air carriers may offer up to two gate passes to caregivers, parents, and guardians who are accompanying a minor or a passenger needing assistance to a departing flight; and</li><li>these individuals may apply their existing\u00a0TSA PreCheck privileges to such gate passes.</li></ul><p>The\u00a0TSA\u00a0PreCheck\u00a0program expedites traveler screening through participating\u00a0TSA security checkpoints.</p>",
      "updateDate": "2026-04-07",
      "versionCode": "id119hr4940"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-08-08",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr4940ih.xml"
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
      "title": "AIRFARE Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-08-13T03:23:18Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "AIRFARE Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-08-13T03:23:17Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Accommodating Individuals Requesting Familial Assistance in Riding Efficiently Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-08-13T03:23:17Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To establish a system to expedite gate passes and flight access procedures at domestic airports to allow caregivers, parents, and guardians to accompany minors and passengers needing assistance to their flights, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-08-13T03:18:25Z"
    }
  ]
}
```
