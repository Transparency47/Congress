# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/439?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/439
- Title: Veterans Foreign Medical Coverage Equality and Modernization Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 439
- Origin chamber: House
- Introduced date: 2025-01-15
- Update date: 2025-12-12T09:08:01Z
- Update date including text: 2025-12-12T09:08:01Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-01-15: Introduced in House
- 2025-01-15 - IntroReferral: Introduced in House
- 2025-01-15 - IntroReferral: Introduced in House
- 2025-01-15 - IntroReferral: Referred to the House Committee on Veterans' Affairs.
- 2025-02-20 - Committee: Referred to the Subcommittee on Health.
- Latest action: 2025-01-15: Introduced in House

## Actions

- 2025-01-15 - IntroReferral: Introduced in House
- 2025-01-15 - IntroReferral: Introduced in House
- 2025-01-15 - IntroReferral: Referred to the House Committee on Veterans' Affairs.
- 2025-02-20 - Committee: Referred to the Subcommittee on Health.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-01-15",
    "latestAction": {
      "actionDate": "2025-01-15",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/439",
    "number": "439",
    "originChamber": "House",
    "policyArea": {
      "name": "Armed Forces and National Security"
    },
    "sponsors": [
      {
        "bioguideId": "L000598",
        "district": "1",
        "firstName": "Nick",
        "fullName": "Rep. LaLota, Nick [R-NY-1]",
        "lastName": "LaLota",
        "party": "R",
        "state": "NY"
      }
    ],
    "title": "Veterans Foreign Medical Coverage Equality and Modernization Act of 2025",
    "type": "HR",
    "updateDate": "2025-12-12T09:08:01Z",
    "updateDateIncludingText": "2025-12-12T09:08:01Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-02-20",
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
      "actionDate": "2025-01-15",
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
      "actionDate": "2025-01-15",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-01-15",
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
          "date": "2025-01-15T15:06:45Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Veterans' Affairs Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": {
              "date": "2025-02-20T17:41:30Z",
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
      "bioguideId": "L000590",
      "district": "3",
      "firstName": "Susie",
      "fullName": "Rep. Lee, Susie [D-NV-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Lee",
      "party": "D",
      "sponsorshipDate": "2025-01-22",
      "state": "NV"
    },
    {
      "bioguideId": "V000133",
      "district": "2",
      "firstName": "Jefferson",
      "fullName": "Rep. Van Drew, Jefferson [R-NJ-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Van Drew",
      "party": "R",
      "sponsorshipDate": "2025-02-04",
      "state": "NJ"
    },
    {
      "bioguideId": "E000299",
      "district": "16",
      "firstName": "Veronica",
      "fullName": "Rep. Escobar, Veronica [D-TX-16]",
      "isOriginalCosponsor": "False",
      "lastName": "Escobar",
      "party": "D",
      "sponsorshipDate": "2025-02-24",
      "state": "TX"
    },
    {
      "bioguideId": "C001110",
      "district": "46",
      "firstName": "J.",
      "fullName": "Rep. Correa, J. Luis [D-CA-46]",
      "isOriginalCosponsor": "False",
      "lastName": "Correa",
      "middleName": "Luis",
      "party": "D",
      "sponsorshipDate": "2025-03-05",
      "state": "CA"
    },
    {
      "bioguideId": "T000468",
      "district": "1",
      "firstName": "Dina",
      "fullName": "Rep. Titus, Dina [D-NV-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Titus",
      "party": "D",
      "sponsorshipDate": "2025-03-06",
      "state": "NV"
    },
    {
      "bioguideId": "S000168",
      "district": "27",
      "firstName": "Maria",
      "fullName": "Rep. Salazar, Maria Elvira [R-FL-27]",
      "isOriginalCosponsor": "False",
      "lastName": "Salazar",
      "middleName": "Elvira",
      "party": "R",
      "sponsorshipDate": "2025-03-18",
      "state": "FL"
    },
    {
      "bioguideId": "D000230",
      "district": "1",
      "firstName": "Donald",
      "fullName": "Rep. Davis, Donald G. [D-NC-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Davis",
      "middleName": "G.",
      "party": "D",
      "sponsorshipDate": "2025-03-27",
      "state": "NC"
    },
    {
      "bioguideId": "S001201",
      "district": "3",
      "firstName": "Thomas",
      "fullName": "Rep. Suozzi, Thomas R. [D-NY-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Suozzi",
      "middleName": "R.",
      "party": "D",
      "sponsorshipDate": "2025-04-07",
      "state": "NY"
    },
    {
      "bioguideId": "L000599",
      "district": "17",
      "firstName": "Michael",
      "fullName": "Rep. Lawler, Michael [R-NY-17]",
      "isOriginalCosponsor": "False",
      "lastName": "Lawler",
      "party": "R",
      "sponsorshipDate": "2025-04-14",
      "state": "NY"
    },
    {
      "bioguideId": "G000602",
      "district": "4",
      "firstName": "Laura",
      "fullName": "Rep. Gillen, Laura [D-NY-4]",
      "isOriginalCosponsor": "False",
      "lastName": "Gillen",
      "party": "D",
      "sponsorshipDate": "2025-04-24",
      "state": "NY"
    },
    {
      "bioguideId": "S001225",
      "district": "17",
      "firstName": "Eric",
      "fullName": "Rep. Sorensen, Eric [D-IL-17]",
      "isOriginalCosponsor": "False",
      "lastName": "Sorensen",
      "party": "D",
      "sponsorshipDate": "2025-05-15",
      "state": "IL"
    },
    {
      "bioguideId": "C001063",
      "district": "28",
      "firstName": "Henry",
      "fullName": "Rep. Cuellar, Henry [D-TX-28]",
      "isOriginalCosponsor": "False",
      "lastName": "Cuellar",
      "party": "D",
      "sponsorshipDate": "2025-05-20",
      "state": "TX"
    },
    {
      "bioguideId": "G000583",
      "district": "5",
      "firstName": "Josh",
      "fullName": "Rep. Gottheimer, Josh [D-NJ-5]",
      "isOriginalCosponsor": "False",
      "lastName": "Gottheimer",
      "party": "D",
      "sponsorshipDate": "2025-06-05",
      "state": "NJ"
    },
    {
      "bioguideId": "C001072",
      "district": "7",
      "firstName": "Andr\u00e9",
      "fullName": "Rep. Carson, Andr\u00e9 [D-IN-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Carson",
      "party": "D",
      "sponsorshipDate": "2025-07-10",
      "state": "IN"
    },
    {
      "bioguideId": "V000138",
      "district": "7",
      "firstName": "Eugene",
      "fullName": "Rep. Vindman, Eugene Simon [D-VA-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Vindman",
      "middleName": "Simon",
      "party": "D",
      "sponsorshipDate": "2025-07-10",
      "state": "VA"
    },
    {
      "bioguideId": "T000488",
      "district": "13",
      "firstName": "Shri",
      "fullName": "Rep. Thanedar, Shri [D-MI-13]",
      "isOriginalCosponsor": "False",
      "lastName": "Thanedar",
      "party": "D",
      "sponsorshipDate": "2025-07-14",
      "state": "MI"
    },
    {
      "bioguideId": "G000597",
      "district": "2",
      "firstName": "Andrew",
      "fullName": "Rep. Garbarino, Andrew R. [R-NY-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Garbarino",
      "middleName": "R.",
      "party": "R",
      "sponsorshipDate": "2025-08-05",
      "state": "NY"
    },
    {
      "bioguideId": "F000466",
      "district": "1",
      "firstName": "Brian",
      "fullName": "Rep. Fitzpatrick, Brian K. [R-PA-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Fitzpatrick",
      "middleName": "K.",
      "party": "R",
      "sponsorshipDate": "2025-08-15",
      "state": "PA"
    },
    {
      "bioguideId": "M000317",
      "district": "11",
      "firstName": "Nicole",
      "fullName": "Rep. Malliotakis, Nicole [R-NY-11]",
      "isOriginalCosponsor": "False",
      "lastName": "Malliotakis",
      "party": "R",
      "sponsorshipDate": "2025-08-26",
      "state": "NY"
    },
    {
      "bioguideId": "S001216",
      "district": "8",
      "firstName": "Kim",
      "fullName": "Rep. Schrier, Kim [D-WA-8]",
      "isOriginalCosponsor": "False",
      "lastName": "Schrier",
      "party": "D",
      "sponsorshipDate": "2025-11-07",
      "state": "WA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr439ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 439\nIN THE HOUSE OF REPRESENTATIVES\nJanuary 15, 2025 Mr. LaLota introduced the following bill; which was referred to the Committee on Veterans' Affairs\nA BILL\nTo amend title 38, United States Code, to require the Department of Veterans Affairs to furnish hospital care and medical services outside a State to veterans with service-connected disabilities rated as permanent and total, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Veterans Foreign Medical Coverage Equality and Modernization Act of 2025 .\n#### 2. Department of Veterans Affairs furnishing of hospital care and medical services outside a State to veterans with service-connected disabilities rated as permanent and total\n##### (a) In general\nSection 1724 of title 38, United States Code, is amended\u2014\n**(1)**\nin subsection (a), by striking and (f) and inserting (f), and (g) ; and\n**(2)**\nby adding at the end the following new subsections:\n(g) The Secretary shall furnish hospital care and medical services outside a State to a veteran with a service-connected disability rated as permanent and total who is otherwise eligible to receive hospital care and medical services if the Secretary determines that\u2014 (1) the hospital care or medical services furnished are consistent with the standard medical practice in the United States; and (2) in the case of any prescription medication furnished, such medication is approved by the Food and Drug Administration. (h) In carrying out this section, the Secretary shall ensure that\u2014 (1) reimbursements made to veterans and medical providers can be made by direct deposit payments in such a manner as to expedite such reimbursements, improve efficiency, and reduce administrative costs; and (2) the appropriate mobile applications of the Department provide for\u2014 (A) the digital submission and real-time tracking of any forms and supporting documentation required for the receipt of hospital care or medical services, or reimbursement for such care or services, under this section; and (B) the availability of any benefits authorization letter, predetermination letter, or continuity of care document associated with hospital care or medical services furnished under this section. .\n##### (b) Effective date\nThe amendments made by subsection (a) shall take effect on the date that is 90 days after the date of the enactment of this Act and apply with respect to hospital care or medical services furnished on or after such date.\n##### (c) Report\nNot later than two years after the date of the enactment of this Act, the Secretary of Veterans Affairs shall submit to Congress a report on the amendments made by this Act. Such report shall include an analysis of the implementation of such amendments, any challenges encountered, and the efficacy of the hospital care and medical services furnished pursuant to such amendments.",
      "versionDate": "2025-01-15",
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
            "name": "Congressional oversight",
            "updateDate": "2025-03-06T16:51:41Z"
          },
          {
            "name": "Diplomacy, foreign officials, Americans abroad",
            "updateDate": "2025-03-06T16:51:29Z"
          },
          {
            "name": "Health care coverage and access",
            "updateDate": "2025-03-06T16:51:24Z"
          },
          {
            "name": "Internet, web applications, social media",
            "updateDate": "2025-03-06T16:51:34Z"
          },
          {
            "name": "Veterans' medical care",
            "updateDate": "2025-03-06T16:51:17Z"
          }
        ]
      },
      "policyArea": {
        "name": "Armed Forces and National Security",
        "updateDate": "2025-02-12T15:44:46Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-01-15",
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
          "measure-id": "id119hr439",
          "measure-number": "439",
          "measure-type": "hr",
          "orig-publish-date": "2025-01-15",
          "originChamber": "HOUSE",
          "update-date": "2025-02-18"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr439v00",
            "update-date": "2025-02-18"
          },
          "action-date": "2025-01-15",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Veterans Foreign Medical Coverage Equality and Modernization Act of 2025</strong></p><p>This bill requires the Department of Veterans Affairs (VA) to furnish hospital care and medical services abroad (i.e., outside any state) to a veteran with a service-connected disability rated as permanent and total who is otherwise eligible for such care if the VA determines certain requirements are met. Specifically, the VA must furnish such care to an eligible veteran if it determines (1) the hospital care or medical services are consistent with the standard medical practice in the United States, and (2) any prescription medication furnished is approved by the Food and Drug Administration.</p><p>For any care provided abroad, the VA must ensure (1) reimbursements made to veterans and medical providers can be made by direct deposit; and (2) the VA\u2019s mobile applications provide for digital submission, real-time tracking of required forms, and the availability of specified documents associated with care or services, such as a benefits authorization letter.</p>"
        },
        "title": "Veterans Foreign Medical Coverage Equality and Modernization Act of 2025"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr439.xml",
    "summary": {
      "actionDate": "2025-01-15",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Veterans Foreign Medical Coverage Equality and Modernization Act of 2025</strong></p><p>This bill requires the Department of Veterans Affairs (VA) to furnish hospital care and medical services abroad (i.e., outside any state) to a veteran with a service-connected disability rated as permanent and total who is otherwise eligible for such care if the VA determines certain requirements are met. Specifically, the VA must furnish such care to an eligible veteran if it determines (1) the hospital care or medical services are consistent with the standard medical practice in the United States, and (2) any prescription medication furnished is approved by the Food and Drug Administration.</p><p>For any care provided abroad, the VA must ensure (1) reimbursements made to veterans and medical providers can be made by direct deposit; and (2) the VA\u2019s mobile applications provide for digital submission, real-time tracking of required forms, and the availability of specified documents associated with care or services, such as a benefits authorization letter.</p>",
      "updateDate": "2025-02-18",
      "versionCode": "id119hr439"
    },
    "title": "Veterans Foreign Medical Coverage Equality and Modernization Act of 2025"
  },
  "summaries": [
    {
      "actionDate": "2025-01-15",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Veterans Foreign Medical Coverage Equality and Modernization Act of 2025</strong></p><p>This bill requires the Department of Veterans Affairs (VA) to furnish hospital care and medical services abroad (i.e., outside any state) to a veteran with a service-connected disability rated as permanent and total who is otherwise eligible for such care if the VA determines certain requirements are met. Specifically, the VA must furnish such care to an eligible veteran if it determines (1) the hospital care or medical services are consistent with the standard medical practice in the United States, and (2) any prescription medication furnished is approved by the Food and Drug Administration.</p><p>For any care provided abroad, the VA must ensure (1) reimbursements made to veterans and medical providers can be made by direct deposit; and (2) the VA\u2019s mobile applications provide for digital submission, real-time tracking of required forms, and the availability of specified documents associated with care or services, such as a benefits authorization letter.</p>",
      "updateDate": "2025-02-18",
      "versionCode": "id119hr439"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-01-15",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr439ih.xml"
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
      "title": "Veterans Foreign Medical Coverage Equality and Modernization Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-02-11T06:53:18Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Veterans Foreign Medical Coverage Equality and Modernization Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-02-11T06:53:16Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend title 38, United States Code, to require the Department of Veterans Affairs to furnish hospital care and medical services outside a State to veterans with service-connected disabilities rated as permanent and total, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-02-11T06:48:20Z"
    }
  ]
}
```
