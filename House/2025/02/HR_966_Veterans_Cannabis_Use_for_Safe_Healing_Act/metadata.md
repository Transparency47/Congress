# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/966?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/966
- Title: Veterans Cannabis Use for Safe Healing Act
- Congress: 119
- Bill type: HR
- Bill number: 966
- Origin chamber: House
- Introduced date: 2025-02-04
- Update date: 2026-05-20T08:07:10Z
- Update date including text: 2026-05-20T08:07:10Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-02-04: Introduced in House
- 2025-02-04 - IntroReferral: Introduced in House
- 2025-02-04 - IntroReferral: Introduced in House
- 2025-02-04 - IntroReferral: Referred to the House Committee on Veterans' Affairs.
- 2025-03-06 - Committee: Referred to the Subcommittee on Health.
- Latest action: 2025-02-04: Introduced in House

## Actions

- 2025-02-04 - IntroReferral: Introduced in House
- 2025-02-04 - IntroReferral: Introduced in House
- 2025-02-04 - IntroReferral: Referred to the House Committee on Veterans' Affairs.
- 2025-03-06 - Committee: Referred to the Subcommittee on Health.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-02-04",
    "latestAction": {
      "actionDate": "2025-02-04",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/966",
    "number": "966",
    "originChamber": "House",
    "policyArea": {
      "name": "Armed Forces and National Security"
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
    "title": "Veterans Cannabis Use for Safe Healing Act",
    "type": "HR",
    "updateDate": "2026-05-20T08:07:10Z",
    "updateDateIncludingText": "2026-05-20T08:07:10Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-03-06",
      "committees": {
        "item": {
          "name": "Health Subcommittee",
          "systemCode": "hsvr03"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Referred to the Subcommittee on Health.",
      "type": "Committee"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-02-04",
      "committees": {
        "item": {
          "name": "Veterans' Affairs Committee",
          "systemCode": "hsvr00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Veterans' Affairs.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-02-04",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-02-04",
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
          "date": "2025-02-04T17:03:45Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Veterans' Affairs Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": {
              "date": "2025-03-06T22:43:41Z",
              "name": "Referred to"
            }
          },
          "name": "Health Subcommittee",
          "systemCode": "hsvr03"
        }
      },
      "systemCode": "hsvr00",
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
      "bioguideId": "C001068",
      "district": "9",
      "firstName": "Steve",
      "fullName": "Rep. Cohen, Steve [D-TN-9]",
      "isOriginalCosponsor": "False",
      "lastName": "Cohen",
      "party": "D",
      "sponsorshipDate": "2025-11-04",
      "state": "TN"
    },
    {
      "bioguideId": "N000147",
      "district": "0",
      "firstName": "Eleanor",
      "fullName": "Del. Norton, Eleanor Holmes [D-DC-At Large]",
      "isOriginalCosponsor": "False",
      "lastName": "Norton",
      "middleName": "Holmes",
      "party": "D",
      "sponsorshipDate": "2026-05-19",
      "state": "DC"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr966ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 966\nIN THE HOUSE OF REPRESENTATIVES\nFebruary 4, 2025 Mr. Steube introduced the following bill; which was referred to the Committee on Veterans' Affairs\nA BILL\nTo prohibit the Secretary of Veterans Affairs from denying a veteran benefits administered by the Secretary by reason of the veteran participating in a State-approved marijuana program, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Veterans Cannabis Use for Safe Healing Act .\n#### 2. Veteran participation in State-approved marijuana programs\n##### (a) Provision of benefits\nNotwithstanding any other provision of law, the Secretary of Veterans Affairs may not deny a veteran any benefit under the laws administered by the Secretary by reason of the veteran participating in a State-approved marijuana program.\n##### (b) Consultation\nWith respect to a veteran who is enrolled in the system of patient enrollment under section 1705 of title 38, United States Code, and participates in a State-approved marijuana program, the Secretary shall ensure that physicians and other health care providers of the Veterans Health Administration\u2014\n**(1)**\ndiscuss marijuana use with the veteran and adjust medical treatment plans accordingly; and\n**(2)**\nrecord such use in the medical records of the veteran.\n##### (c) Provision of information\nNotwithstanding any other provision of law, the Secretary shall authorize physicians and other health care providers of the Veterans Health Administration of the Department of Veterans Affairs to provide recommendations and opinions to veterans who are residents of States with State-approved marijuana programs regarding the participation of veterans in such programs.\n##### (d) Definitions\nIn this section:\n**(1)**\nThe term marijuana has the meaning given the term marihuana in section 102 of the Controlled Substances Act ( 21 U.S.C. 802 ).\n**(2)**\nThe term State has the meaning given that term in section 101 of title 38, United States Code.",
      "versionDate": "2025-02-04",
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
            "name": "Drug, alcohol, tobacco use",
            "updateDate": "2025-04-11T18:18:59Z"
          },
          {
            "name": "Health care coverage and access",
            "updateDate": "2025-04-11T18:18:59Z"
          },
          {
            "name": "Health information and medical records",
            "updateDate": "2025-04-11T18:18:59Z"
          },
          {
            "name": "Veterans' medical care",
            "updateDate": "2025-04-11T18:18:59Z"
          },
          {
            "name": "Veterans' pensions and compensation",
            "updateDate": "2025-04-11T18:18:59Z"
          }
        ]
      },
      "policyArea": {
        "name": "Armed Forces and National Security",
        "updateDate": "2025-03-19T14:10:15Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-02-04",
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
          "measure-id": "id119hr966",
          "measure-number": "966",
          "measure-type": "hr",
          "orig-publish-date": "2025-02-04",
          "originChamber": "HOUSE",
          "update-date": "2025-03-20"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr966v00",
            "update-date": "2025-03-20"
          },
          "action-date": "2025-02-04",
          "action-desc": "Introduced in House",
          "summary-text": "<p><b>Veterans Cannabis Use for Safe Healing Act</b></p> <p>This bill prohibits the Department of Veterans Affairs (VA) from denying a veteran any VA benefit due to participation in a state-approved marijuana program. For veterans participating in these approved programs, the VA must ensure its health care providers (1) discuss marijuana use with such veterans and adjust treatment plans accordingly, and (2) record such use in the veterans' medical records.</p> <p>Under the bill, the VA shall authorize physicians and other VA health care providers to provide recommendations to veterans who are residents of states with approved programs.</p>"
        },
        "title": "Veterans Cannabis Use for Safe Healing Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr966.xml",
    "summary": {
      "actionDate": "2025-02-04",
      "actionDesc": "Introduced in House",
      "text": "<p><b>Veterans Cannabis Use for Safe Healing Act</b></p> <p>This bill prohibits the Department of Veterans Affairs (VA) from denying a veteran any VA benefit due to participation in a state-approved marijuana program. For veterans participating in these approved programs, the VA must ensure its health care providers (1) discuss marijuana use with such veterans and adjust treatment plans accordingly, and (2) record such use in the veterans' medical records.</p> <p>Under the bill, the VA shall authorize physicians and other VA health care providers to provide recommendations to veterans who are residents of states with approved programs.</p>",
      "updateDate": "2025-03-20",
      "versionCode": "id119hr966"
    },
    "title": "Veterans Cannabis Use for Safe Healing Act"
  },
  "summaries": [
    {
      "actionDate": "2025-02-04",
      "actionDesc": "Introduced in House",
      "text": "<p><b>Veterans Cannabis Use for Safe Healing Act</b></p> <p>This bill prohibits the Department of Veterans Affairs (VA) from denying a veteran any VA benefit due to participation in a state-approved marijuana program. For veterans participating in these approved programs, the VA must ensure its health care providers (1) discuss marijuana use with such veterans and adjust treatment plans accordingly, and (2) record such use in the veterans' medical records.</p> <p>Under the bill, the VA shall authorize physicians and other VA health care providers to provide recommendations to veterans who are residents of states with approved programs.</p>",
      "updateDate": "2025-03-20",
      "versionCode": "id119hr966"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-02-04",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr966ih.xml"
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
      "title": "Veterans Cannabis Use for Safe Healing Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-03-05T05:23:24Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Veterans Cannabis Use for Safe Healing Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-05T05:23:20Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To prohibit the Secretary of Veterans Affairs from denying a veteran benefits administered by the Secretary by reason of the veteran participating in a State-approved marijuana program, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-05T05:18:36Z"
    }
  ]
}
```
