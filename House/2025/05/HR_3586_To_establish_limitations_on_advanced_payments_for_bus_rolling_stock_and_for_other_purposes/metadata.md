# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/3586?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/hr/3586
- Title: To establish limitations on advanced payments for bus rolling stock, and for other purposes.
- Congress: 119
- Bill type: HR
- Bill number: 3586
- Origin chamber: House
- Introduced date: 2025-05-23
- Update date: 2025-07-23T14:12:40Z
- Update date including text: 2025-07-23T14:12:40Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-05-23: Introduced in House
- 2025-05-23 - IntroReferral: Introduced in House
- 2025-05-23 - IntroReferral: Introduced in House
- 2025-05-23 - IntroReferral: Referred to the House Committee on Transportation and Infrastructure.
- 2025-05-24 - Committee: Referred to the Subcommittee on Highways and Transit.
- Latest action: 2025-05-23: Introduced in House

## Actions

- 2025-05-23 - IntroReferral: Introduced in House
- 2025-05-23 - IntroReferral: Introduced in House
- 2025-05-23 - IntroReferral: Referred to the House Committee on Transportation and Infrastructure.
- 2025-05-24 - Committee: Referred to the Subcommittee on Highways and Transit.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-05-23",
    "latestAction": {
      "actionDate": "2025-05-23",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/hr/3586",
    "number": "3586",
    "originChamber": "House",
    "policyArea": {
      "name": "Transportation and Public Works"
    },
    "sponsors": [
      {
        "bioguideId": "F000470",
        "district": "7",
        "firstName": "Michelle",
        "fullName": "Rep. Fischbach, Michelle [R-MN-7]",
        "lastName": "Fischbach",
        "party": "R",
        "state": "MN"
      }
    ],
    "title": "To establish limitations on advanced payments for bus rolling stock, and for other purposes.",
    "type": "HR",
    "updateDate": "2025-07-23T14:12:40Z",
    "updateDateIncludingText": "2025-07-23T14:12:40Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-05-24",
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
      "actionDate": "2025-05-23",
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
      "actionDate": "2025-05-23",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-05-23",
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
          "date": "2025-05-23T14:04:05Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Transportation and Infrastructure Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": {
              "date": "2025-05-24T18:51:01Z",
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
      "bioguideId": "S001212",
      "district": "8",
      "firstName": "Pete",
      "fullName": "Rep. Stauber, Pete [R-MN-8]",
      "isOriginalCosponsor": "True",
      "lastName": "Stauber",
      "party": "R",
      "sponsorshipDate": "2025-05-23",
      "state": "MN"
    },
    {
      "bioguideId": "C001119",
      "district": "2",
      "firstName": "Angie",
      "fullName": "Rep. Craig, Angie [D-MN-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Craig",
      "party": "D",
      "sponsorshipDate": "2025-05-23",
      "state": "MN"
    },
    {
      "bioguideId": "R000575",
      "district": "3",
      "firstName": "Mike",
      "fullName": "Rep. Rogers, Mike D. [R-AL-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Rogers",
      "party": "R",
      "sponsorshipDate": "2025-07-21",
      "state": "AL"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr3586ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 3586\nIN THE HOUSE OF REPRESENTATIVES\nMay 23, 2025 Mrs. Fischbach (for herself, Mr. Stauber , and Ms. Craig ) introduced the following bill; which was referred to the Committee on Transportation and Infrastructure\nA BILL\nTo establish limitations on advanced payments for bus rolling stock, and for other purposes.\n#### 1. Limitations on advanced payments for bus rolling stock\nSection 5323 of title 49, United States Code, is amended by adding at the end the following:\n(w) Limitations on advanced payments for bus rolling stock (1) In general Notwithstanding any provision of this chapter or part 200 of title 2, Code of Federal Regulations, or any successor regulation, a recipient may use assistance made available under this chapter to make an advance payment on a bus rolling stock vehicle without the transit vehicle manufacturer obtaining a performance bond or similar financial arrangement. (2) Limitations A recipient making an advance payment under paragraph (1)\u2014 (A) shall have\u2014 (i) a signed purchase order and executed contract with a transit vehicle manufacturer that includes advance payment provisions; (ii) preaward authority; and (iii) met the requirements under subsection (m) and section 5318(e) of this title; and (B) shall not provide an advanced payment that is more than 20 percent of the total purchase order value. .",
      "versionDate": "2025-05-23",
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
        "updateDate": "2025-06-03T14:33:40Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-05-23",
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
          "measure-id": "id119hr3586",
          "measure-number": "3586",
          "measure-type": "hr",
          "orig-publish-date": "2025-05-23",
          "originChamber": "HOUSE",
          "update-date": "2025-06-04"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr3586v00",
            "update-date": "2025-06-04"
          },
          "action-date": "2025-05-23",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong></strong>This bill allows a state or local authority (e.g., a transit authority) to use public transportation grants to make a partial advance payment for bus rolling stock (e.g., transit buses).\u00a0</p><p>Specifically, a public transportation grant recipient may use grant funds to make an advance payment of not more than 20% of the total purchase order value of a bus rolling stock vehicle without requiring the vehicle manufacturer to provide a performance bond (or\u00a0similar financial arrangement). In order to make an advance payment, the\u00a0recipient must meet certain requirements. For example, the recipient must have a signed purchase order and an executed contract with a vehicle manufacturer that includes advance payment provisions.</p>"
        },
        "title": "To establish limitations on advanced payments for bus rolling stock, and for other purposes."
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr3586.xml",
    "summary": {
      "actionDate": "2025-05-23",
      "actionDesc": "Introduced in House",
      "text": "<p><strong></strong>This bill allows a state or local authority (e.g., a transit authority) to use public transportation grants to make a partial advance payment for bus rolling stock (e.g., transit buses).\u00a0</p><p>Specifically, a public transportation grant recipient may use grant funds to make an advance payment of not more than 20% of the total purchase order value of a bus rolling stock vehicle without requiring the vehicle manufacturer to provide a performance bond (or\u00a0similar financial arrangement). In order to make an advance payment, the\u00a0recipient must meet certain requirements. For example, the recipient must have a signed purchase order and an executed contract with a vehicle manufacturer that includes advance payment provisions.</p>",
      "updateDate": "2025-06-04",
      "versionCode": "id119hr3586"
    },
    "title": "To establish limitations on advanced payments for bus rolling stock, and for other purposes."
  },
  "summaries": [
    {
      "actionDate": "2025-05-23",
      "actionDesc": "Introduced in House",
      "text": "<p><strong></strong>This bill allows a state or local authority (e.g., a transit authority) to use public transportation grants to make a partial advance payment for bus rolling stock (e.g., transit buses).\u00a0</p><p>Specifically, a public transportation grant recipient may use grant funds to make an advance payment of not more than 20% of the total purchase order value of a bus rolling stock vehicle without requiring the vehicle manufacturer to provide a performance bond (or\u00a0similar financial arrangement). In order to make an advance payment, the\u00a0recipient must meet certain requirements. For example, the recipient must have a signed purchase order and an executed contract with a vehicle manufacturer that includes advance payment provisions.</p>",
      "updateDate": "2025-06-04",
      "versionCode": "id119hr3586"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-05-23",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr3586ih.xml"
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
      "title": "To establish limitations on advanced payments for bus rolling stock, and for other purposes.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-07-23T14:12:40Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To establish limitations on advanced payments for bus rolling stock, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-06-03T04:33:28Z"
    }
  ]
}
```
