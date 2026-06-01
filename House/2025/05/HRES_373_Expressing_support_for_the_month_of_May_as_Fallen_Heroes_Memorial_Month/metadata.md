# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hres/373?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/hres/373
- Title: Expressing support for the month of May as "Fallen Heroes Memorial Month".
- Congress: 119
- Bill type: HRES
- Bill number: 373
- Origin chamber: House
- Introduced date: 2025-05-01
- Update date: 2025-07-03T20:18:16Z
- Update date including text: 2025-07-03T20:18:16Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-05-01: Introduced in House
- 2025-05-01 - IntroReferral: Referred to the Committee on Armed Services, and in addition to the Committee on Veterans' Affairs, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-05-01 - IntroReferral: Referred to the Committee on Armed Services, and in addition to the Committee on Veterans' Affairs, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-05-01 - IntroReferral: Submitted in House
- 2025-05-01 - IntroReferral: Submitted in House
- Latest action: 2025-05-01: Submitted in House

## Actions

- 2025-05-01 - IntroReferral: Referred to the Committee on Armed Services, and in addition to the Committee on Veterans' Affairs, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-05-01 - IntroReferral: Referred to the Committee on Armed Services, and in addition to the Committee on Veterans' Affairs, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-05-01 - IntroReferral: Submitted in House
- 2025-05-01 - IntroReferral: Submitted in House

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-05-01",
    "latestAction": {
      "actionDate": "2025-05-01",
      "text": "Submitted in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/hres/373",
    "number": "373",
    "originChamber": "House",
    "policyArea": {
      "name": "Armed Forces and National Security"
    },
    "sponsors": [
      {
        "bioguideId": "M001212",
        "district": "1",
        "firstName": "Barry",
        "fullName": "Rep. Moore, Barry [R-AL-1]",
        "lastName": "Moore",
        "party": "R",
        "state": "AL"
      }
    ],
    "title": "Expressing support for the month of May as \"Fallen Heroes Memorial Month\".",
    "type": "HRES",
    "updateDate": "2025-07-03T20:18:16Z",
    "updateDateIncludingText": "2025-07-03T20:18:16Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-05-01",
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
      "text": "Referred to the Committee on Armed Services, and in addition to the Committee on Veterans' Affairs, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-05-01",
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
      "text": "Referred to the Committee on Armed Services, and in addition to the Committee on Veterans' Affairs, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-05-01",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Submitted in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1025",
      "actionDate": "2025-05-01",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Submitted in House",
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
          "date": "2025-05-01T13:00:10Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Veterans' Affairs Committee",
      "systemCode": "hsvr00",
      "type": "Standing"
    },
    {
      "activities": {
        "item": {
          "date": "2025-05-01T13:00:05Z",
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
      "bioguideId": "C001120",
      "district": "2",
      "firstName": "Dan",
      "fullName": "Rep. Crenshaw, Dan [R-TX-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Crenshaw",
      "party": "R",
      "sponsorshipDate": "2025-05-01",
      "state": "TX"
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
      "sponsorshipDate": "2025-05-01",
      "state": "TX"
    },
    {
      "bioguideId": "T000478",
      "district": "24",
      "firstName": "Claudia",
      "fullName": "Rep. Tenney, Claudia [R-NY-24]",
      "isOriginalCosponsor": "True",
      "lastName": "Tenney",
      "party": "R",
      "sponsorshipDate": "2025-05-01",
      "state": "NY"
    },
    {
      "bioguideId": "C001103",
      "district": "1",
      "firstName": "Earl",
      "fullName": "Rep. Carter, Earl L. \"Buddy\" [R-GA-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Carter",
      "middleName": "L. \"Buddy\"",
      "party": "R",
      "sponsorshipDate": "2025-05-01",
      "state": "GA"
    },
    {
      "bioguideId": "B000740",
      "district": "5",
      "firstName": "Stephanie",
      "fullName": "Rep. Bice, Stephanie I. [R-OK-5]",
      "isOriginalCosponsor": "True",
      "lastName": "Bice",
      "middleName": "I.",
      "party": "R",
      "sponsorshipDate": "2025-05-01",
      "state": "OK"
    },
    {
      "bioguideId": "V000129",
      "district": "22",
      "firstName": "David",
      "fullName": "Rep. Valadao, David G. [R-CA-22]",
      "isOriginalCosponsor": "True",
      "lastName": "Valadao",
      "middleName": "G.",
      "party": "R",
      "sponsorshipDate": "2025-05-01",
      "state": "CA"
    },
    {
      "bioguideId": "L000603",
      "district": "8",
      "firstName": "Morgan",
      "fullName": "Rep. Luttrell, Morgan [R-TX-8]",
      "isOriginalCosponsor": "True",
      "lastName": "Luttrell",
      "party": "R",
      "sponsorshipDate": "2025-05-01",
      "state": "TX"
    },
    {
      "bioguideId": "W000806",
      "district": "11",
      "firstName": "Daniel",
      "fullName": "Rep. Webster, Daniel [R-FL-11]",
      "isOriginalCosponsor": "True",
      "lastName": "Webster",
      "party": "R",
      "sponsorshipDate": "2025-05-01",
      "state": "FL"
    },
    {
      "bioguideId": "V000135",
      "district": "3",
      "firstName": "Derrick",
      "fullName": "Rep. Van Orden, Derrick [R-WI-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Van Orden",
      "party": "R",
      "sponsorshipDate": "2025-05-05",
      "state": "WI"
    },
    {
      "bioguideId": "P000048",
      "district": "11",
      "firstName": "August",
      "fullName": "Rep. Pfluger, August [R-TX-11]",
      "isOriginalCosponsor": "False",
      "lastName": "Pfluger",
      "party": "R",
      "sponsorshipDate": "2025-05-13",
      "state": "TX"
    },
    {
      "bioguideId": "E000246",
      "district": "11",
      "firstName": "Chuck",
      "fullName": "Rep. Edwards, Chuck [R-NC-11]",
      "isOriginalCosponsor": "False",
      "lastName": "Edwards",
      "party": "R",
      "sponsorshipDate": "2025-05-23",
      "state": "NC"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hres/BILLS-119hres373ih.xml",
      "text": "IV\n119th CONGRESS\n1st Session\nH. RES. 373\nIN THE HOUSE OF REPRESENTATIVES\nMay 1, 2025 Mr. Moore of Alabama (for himself, Mr. Crenshaw , Mr. Weber of Texas , Ms. Tenney , Mr. Carter of Georgia , Mrs. Bice , Mr. Valadao , Mr. Luttrell , and Mr. Webster of Florida ) submitted the following resolution; which was referred to the Committee on Armed Services , and in addition to the Committee on Veterans' Affairs , for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned\nRESOLUTION\nExpressing support for the month of May as Fallen Heroes Memorial Month .\nThat the House of Representatives\u2014\n**(1)**\nhonors the more than 1,300,000 veterans who gave their lives in service to the United States;\n**(2)**\nrecognizes the families and loved ones of the Nation\u2019s fallen heroes and lifts them up in prayer;\n**(3)**\nurges the people of the United States to reflect on the contributions of America\u2019s heroes and to honor the memory of those who paid the ultimate sacrifice in securing the blessings of liberty for our country; and\n**(4)**\nrequests that the President issue an annual proclamation\u2014\n**(A)**\ndesignating Fallen Heroes Memorial Month ;\n**(B)**\naffirming the Nation\u2019s everlasting gratitude for members of the Armed Forces who made the ultimate sacrifice; and\n**(C)**\ncalling on Americans to remember and honor our Nation\u2019s fallen heroes and to pay tribute to them through volunteering and supporting veteran service organizations.",
      "versionDate": "2025-05-01",
      "versionType": "IH"
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
        "name": "Armed Forces and National Security",
        "updateDate": "2025-06-03T19:20:35Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-05-01",
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
          "measure-id": "id119hres373",
          "measure-number": "373",
          "measure-type": "hres",
          "orig-publish-date": "2025-05-01",
          "originChamber": "HOUSE",
          "update-date": "2025-07-03"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hres373v00",
            "update-date": "2025-07-03"
          },
          "action-date": "2025-05-01",
          "action-desc": "Introduced in House",
          "summary-text": "<p>This resolution honors the veterans who gave their lives in service to the country and recognizes the families and loved ones of such veterans. Additionally, the resolution requests that the President issue an annual proclamation designating Fallen Heroes Memorial Month.</p>"
        },
        "title": "Expressing support for the month of May as \"Fallen Heroes Memorial Month\"."
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hres/BILLSUM-119hres373.xml",
    "summary": {
      "actionDate": "2025-05-01",
      "actionDesc": "Introduced in House",
      "text": "<p>This resolution honors the veterans who gave their lives in service to the country and recognizes the families and loved ones of such veterans. Additionally, the resolution requests that the President issue an annual proclamation designating Fallen Heroes Memorial Month.</p>",
      "updateDate": "2025-07-03",
      "versionCode": "id119hres373"
    },
    "title": "Expressing support for the month of May as \"Fallen Heroes Memorial Month\"."
  },
  "summaries": [
    {
      "actionDate": "2025-05-01",
      "actionDesc": "Introduced in House",
      "text": "<p>This resolution honors the veterans who gave their lives in service to the country and recognizes the families and loved ones of such veterans. Additionally, the resolution requests that the President issue an annual proclamation designating Fallen Heroes Memorial Month.</p>",
      "updateDate": "2025-07-03",
      "versionCode": "id119hres373"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-05-01",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hres/BILLS-119hres373ih.xml"
        }
      ],
      "type": "IH"
    }
  ]
}
```

## API Data: titles

```json
{
  "titles": [
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Expressing support for the month of May as \"Fallen Heroes Memorial Month\".",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-05-02T08:48:21Z"
    },
    {
      "title": "Expressing support for the month of May as \"Fallen Heroes Memorial Month\".",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-05-02T08:06:27Z"
    }
  ]
}
```
