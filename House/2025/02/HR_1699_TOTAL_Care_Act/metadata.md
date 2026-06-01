# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/1699?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/1699
- Title: TOTAL Care Act
- Congress: 119
- Bill type: HR
- Bill number: 1699
- Origin chamber: House
- Introduced date: 2025-02-27
- Update date: 2025-09-09T08:05:25Z
- Update date including text: 2025-09-09T08:05:25Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-02-27: Introduced in House
- 2025-02-27 - IntroReferral: Introduced in House
- 2025-02-27 - IntroReferral: Introduced in House
- 2025-02-27 - IntroReferral: Referred to the House Committee on Armed Services.
- Latest action: 2025-02-27: Introduced in House

## Actions

- 2025-02-27 - IntroReferral: Introduced in House
- 2025-02-27 - IntroReferral: Introduced in House
- 2025-02-27 - IntroReferral: Referred to the House Committee on Armed Services.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-02-27",
    "latestAction": {
      "actionDate": "2025-02-27",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/1699",
    "number": "1699",
    "originChamber": "House",
    "policyArea": {
      "name": "Armed Forces and National Security"
    },
    "sponsors": [
      {
        "bioguideId": "H001066",
        "district": "4",
        "firstName": "Steven",
        "fullName": "Rep. Horsford, Steven [D-NV-4]",
        "lastName": "Horsford",
        "party": "D",
        "state": "NV"
      }
    ],
    "title": "TOTAL Care Act",
    "type": "HR",
    "updateDate": "2025-09-09T08:05:25Z",
    "updateDateIncludingText": "2025-09-09T08:05:25Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-02-27",
      "committees": {
        "item": {
          "name": "Armed Services Committee",
          "systemCode": "hsas00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Armed Services.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-02-27",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-02-27",
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
          "date": "2025-02-27T14:13:00Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Armed Services Committee",
      "systemCode": "hsas00",
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
      "bioguideId": "H001085",
      "district": "6",
      "firstName": "Chrissy",
      "fullName": "Rep. Houlahan, Chrissy [D-PA-6]",
      "isOriginalCosponsor": "True",
      "lastName": "Houlahan",
      "party": "D",
      "sponsorshipDate": "2025-02-27",
      "state": "PA"
    },
    {
      "bioguideId": "S000168",
      "district": "27",
      "firstName": "Maria",
      "fullName": "Rep. Salazar, Maria Elvira [R-FL-27]",
      "isOriginalCosponsor": "True",
      "lastName": "Salazar",
      "middleName": "Elvira",
      "party": "R",
      "sponsorshipDate": "2025-02-27",
      "state": "FL"
    },
    {
      "bioguideId": "S001159",
      "district": "10",
      "firstName": "Marilyn",
      "fullName": "Rep. Strickland, Marilyn [D-WA-10]",
      "isOriginalCosponsor": "True",
      "lastName": "Strickland",
      "party": "D",
      "sponsorshipDate": "2025-02-27",
      "state": "WA"
    },
    {
      "bioguideId": "J000305",
      "district": "51",
      "firstName": "Sara",
      "fullName": "Rep. Jacobs, Sara [D-CA-51]",
      "isOriginalCosponsor": "True",
      "lastName": "Jacobs",
      "party": "D",
      "sponsorshipDate": "2025-02-27",
      "state": "CA"
    },
    {
      "bioguideId": "T000487",
      "district": "2",
      "firstName": "Jill",
      "fullName": "Rep. Tokuda, Jill N. [D-HI-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Tokuda",
      "middleName": "N.",
      "party": "D",
      "sponsorshipDate": "2025-02-27",
      "state": "HI"
    },
    {
      "bioguideId": "T000463",
      "district": "10",
      "firstName": "Michael",
      "fullName": "Rep. Turner, Michael R. [R-OH-10]",
      "isOriginalCosponsor": "True",
      "lastName": "Turner",
      "middleName": "R.",
      "party": "R",
      "sponsorshipDate": "2025-02-27",
      "state": "OH"
    },
    {
      "bioguideId": "J000288",
      "district": "4",
      "firstName": "Henry",
      "fullName": "Rep. Johnson, Henry C. \"Hank\" [D-GA-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Johnson",
      "middleName": "C. \"Hank\"",
      "party": "D",
      "sponsorshipDate": "2025-02-27",
      "state": "GA"
    },
    {
      "bioguideId": "G000604",
      "district": "2",
      "firstName": "Maggie",
      "fullName": "Rep. Goodlander, Maggie [D-NH-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Goodlander",
      "party": "D",
      "sponsorshipDate": "2025-02-27",
      "state": "NH"
    },
    {
      "bioguideId": "M001238",
      "district": "0",
      "firstName": "Sarah",
      "fullName": "Rep. McBride, Sarah [D-DE-At Large]",
      "isOriginalCosponsor": "True",
      "lastName": "McBride",
      "party": "D",
      "sponsorshipDate": "2025-02-27",
      "state": "DE"
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
      "sponsorshipDate": "2025-03-25",
      "state": "PA"
    },
    {
      "bioguideId": "B001298",
      "district": "2",
      "firstName": "Don",
      "fullName": "Rep. Bacon, Don [R-NE-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Bacon",
      "party": "R",
      "sponsorshipDate": "2025-06-03",
      "state": "NE"
    },
    {
      "bioguideId": "K000397",
      "district": "40",
      "firstName": "Young",
      "fullName": "Rep. Kim, Young [R-CA-40]",
      "isOriginalCosponsor": "False",
      "lastName": "Kim",
      "party": "R",
      "sponsorshipDate": "2025-06-03",
      "state": "CA"
    },
    {
      "bioguideId": "L000599",
      "district": "17",
      "firstName": "Michael",
      "fullName": "Rep. Lawler, Michael [R-NY-17]",
      "isOriginalCosponsor": "False",
      "lastName": "Lawler",
      "party": "R",
      "sponsorshipDate": "2025-06-09",
      "state": "NY"
    },
    {
      "bioguideId": "J000310",
      "district": "32",
      "firstName": "Julie",
      "fullName": "Rep. Johnson, Julie [D-TX-32]",
      "isOriginalCosponsor": "False",
      "lastName": "Johnson",
      "party": "D",
      "sponsorshipDate": "2025-07-02",
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
      "sponsorshipDate": "2025-07-14",
      "state": "NJ"
    },
    {
      "bioguideId": "H001099",
      "district": "8",
      "firstName": "Mike",
      "fullName": "Rep. Haridopolos, Mike [R-FL-8]",
      "isOriginalCosponsor": "False",
      "lastName": "Haridopolos",
      "party": "R",
      "sponsorshipDate": "2025-09-08",
      "state": "FL"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1699ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 1699\nIN THE HOUSE OF REPRESENTATIVES\nFebruary 27, 2025 Mr. Horsford (for himself, Ms. Houlahan , Ms. Salazar , Ms. Strickland , Ms. Jacobs , Ms. Tokuda , Mr. Turner of Ohio , Mr. Johnson of Georgia , Ms. Goodlander , and Ms. McBride ) introduced the following bill; which was referred to the Committee on Armed Services\nA BILL\nTo direct the Secretary of Defense to carry out a pilot program under which a TRICARE Prime beneficiary may access obstetrical and gynecological care without a referral, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the TRICARE OBGYN Treatment and Access without Lags in Care Act or the TOTAL Care Act .\n#### 2. Pilot program on access to obstetrical and gynecological care under TRICARE Prime program\n##### (a) Pilot program\nBeginning not later than 180 days after the date of the enactment of this Act, the Secretary of Defense shall carry out a pilot program under which\u2014\n**(1)**\nthe referral requirement in section 1095f(a)(1) of title 10, United States Code, does not apply with respect to obstetrical and gynecological care for covered participants, including the ordering of related obstetrical and gynecological items and services; and\n**(2)**\ncovered participants may elect to designate an obstetrical or gynecological care provider under the TRICARE program as an additional designated primary care manager under such section.\n##### (b) Duration\nThe Secretary shall carry out the pilot program for a period of five years.\n##### (c) Report\nNot later than four years after the date of the enactment of this Act, the Secretary shall submit to the congressional defense committees a report on the pilot program that includes the following:\n**(1)**\nAn assessment of any increases or decreases to TRICARE Prime enrollment during the period in which the Secretary carries out the pilot program.\n**(2)**\nAn assessment of any changes in the associated costs of providing obstetrical and gynecological care under TRICARE Prime.\n**(3)**\nAny other matters the Secretary determines appropriate.\n##### (d) Definitions\nIn this section:\n**(1)**\nThe term congressional defense committees has the meaning given that term in section 101(a)(16) of title 10, United States Code.\n**(2)**\nThe term covered participant means a female beneficiary enrolled in TRICARE Prime who elects to participate in the pilot program.\n**(3)**\nThe terms TRICARE Prime and TRICARE program have the meaning given those terms in section 1072 of title 10, United States Code.",
      "versionDate": "2025-02-27",
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
            "updateDate": "2025-09-02T17:56:20Z"
          },
          {
            "name": "Health care coverage and access",
            "updateDate": "2025-09-02T17:56:26Z"
          },
          {
            "name": "Health programs administration and funding",
            "updateDate": "2025-09-02T17:56:16Z"
          },
          {
            "name": "Military medicine",
            "updateDate": "2025-09-02T17:56:04Z"
          },
          {
            "name": "Sex and reproductive health",
            "updateDate": "2025-09-02T17:56:12Z"
          },
          {
            "name": "Women's health",
            "updateDate": "2025-09-02T17:56:08Z"
          }
        ]
      },
      "policyArea": {
        "name": "Armed Forces and National Security",
        "updateDate": "2025-05-14T15:47:41Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-02-27",
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
          "measure-id": "id119hr1699",
          "measure-number": "1699",
          "measure-type": "hr",
          "orig-publish-date": "2025-02-27",
          "originChamber": "HOUSE",
          "update-date": "2025-08-14"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr1699v00",
            "update-date": "2025-08-14"
          },
          "action-date": "2025-02-27",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>TRICARE OBGYN Treatment and Access without Lags in Care Act or the TOTAL Care Act</strong></p><p>This bill requires the Department of Defense (DOD) to implement a five-year pilot program under which female beneficiaries enrolled in TRICARE Prime may receive obstetrical and gynecological care without a referral. (Generally, the TRICARE Prime program requires a beneficiary to obtain a referral for care through a designated primary care manager.)</p><p>Under the pilot program, participating female beneficiaries may elect to designate an obstetrical or gynecological care provider under the TRICARE program (i.e., the various programs carried out by DOD, including TRICARE Prime) as an additional designated primary care manager.</p>"
        },
        "title": "TOTAL Care Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr1699.xml",
    "summary": {
      "actionDate": "2025-02-27",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>TRICARE OBGYN Treatment and Access without Lags in Care Act or the TOTAL Care Act</strong></p><p>This bill requires the Department of Defense (DOD) to implement a five-year pilot program under which female beneficiaries enrolled in TRICARE Prime may receive obstetrical and gynecological care without a referral. (Generally, the TRICARE Prime program requires a beneficiary to obtain a referral for care through a designated primary care manager.)</p><p>Under the pilot program, participating female beneficiaries may elect to designate an obstetrical or gynecological care provider under the TRICARE program (i.e., the various programs carried out by DOD, including TRICARE Prime) as an additional designated primary care manager.</p>",
      "updateDate": "2025-08-14",
      "versionCode": "id119hr1699"
    },
    "title": "TOTAL Care Act"
  },
  "summaries": [
    {
      "actionDate": "2025-02-27",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>TRICARE OBGYN Treatment and Access without Lags in Care Act or the TOTAL Care Act</strong></p><p>This bill requires the Department of Defense (DOD) to implement a five-year pilot program under which female beneficiaries enrolled in TRICARE Prime may receive obstetrical and gynecological care without a referral. (Generally, the TRICARE Prime program requires a beneficiary to obtain a referral for care through a designated primary care manager.)</p><p>Under the pilot program, participating female beneficiaries may elect to designate an obstetrical or gynecological care provider under the TRICARE program (i.e., the various programs carried out by DOD, including TRICARE Prime) as an additional designated primary care manager.</p>",
      "updateDate": "2025-08-14",
      "versionCode": "id119hr1699"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-02-27",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1699ih.xml"
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
      "title": "TOTAL Care Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-03-19T09:53:22Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "TOTAL Care Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-19T09:53:19Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "TRICARE OBGYN Treatment and Access without Lags in Care Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-19T09:53:19Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To direct the Secretary of Defense to carry out a pilot program under which a TRICARE Prime beneficiary may access obstetrical and gynecological care without a referral, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-19T09:48:28Z"
    }
  ]
}
```
