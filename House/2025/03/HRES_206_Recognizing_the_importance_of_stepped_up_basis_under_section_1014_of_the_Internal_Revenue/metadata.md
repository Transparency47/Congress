# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hres/206?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-resolution/206
- Title: Recognizing the importance of stepped-up basis under section 1014 of the Internal Revenue Code of 1986 in preserving family-owned farms and small businesses.
- Congress: 119
- Bill type: HRES
- Bill number: 206
- Origin chamber: House
- Introduced date: 2025-03-10
- Update date: 2026-05-07T14:00:38Z
- Update date including text: 2026-05-07T14:00:38Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-03-10: Introduced in House
- 2025-03-10 - IntroReferral: Referred to the House Committee on Ways and Means.
- 2025-03-10 - IntroReferral: Submitted in House
- 2025-03-10 - IntroReferral: Submitted in House
- Latest action: 2025-03-10: Submitted in House

## Actions

- 2025-03-10 - IntroReferral: Referred to the House Committee on Ways and Means.
- 2025-03-10 - IntroReferral: Submitted in House
- 2025-03-10 - IntroReferral: Submitted in House

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-03-10",
    "latestAction": {
      "actionDate": "2025-03-10",
      "text": "Submitted in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-resolution/206",
    "number": "206",
    "originChamber": "House",
    "policyArea": {
      "name": "Taxation"
    },
    "sponsors": [
      {
        "bioguideId": "M000871",
        "district": "1",
        "firstName": "Tracey",
        "fullName": "Rep. Mann, Tracey [R-KS-1]",
        "lastName": "Mann",
        "party": "R",
        "state": "KS"
      }
    ],
    "title": "Recognizing the importance of stepped-up basis under section 1014 of the Internal Revenue Code of 1986 in preserving family-owned farms and small businesses.",
    "type": "HRES",
    "updateDate": "2026-05-07T14:00:38Z",
    "updateDateIncludingText": "2026-05-07T14:00:38Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-03-10",
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
      "actionCode": "H11100",
      "actionDate": "2025-03-10",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Submitted in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1025",
      "actionDate": "2025-03-10",
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
          "date": "2025-03-10T16:01:40Z",
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
      "bioguideId": "C001059",
      "district": "21",
      "firstName": "Jim",
      "fullName": "Rep. Costa, Jim [D-CA-21]",
      "isOriginalCosponsor": "True",
      "lastName": "Costa",
      "party": "D",
      "sponsorshipDate": "2025-03-10",
      "state": "CA"
    },
    {
      "bioguideId": "P000613",
      "district": "19",
      "firstName": "Jimmy",
      "fullName": "Rep. Panetta, Jimmy [D-CA-19]",
      "isOriginalCosponsor": "True",
      "lastName": "Panetta",
      "party": "D",
      "sponsorshipDate": "2025-03-10",
      "state": "CA"
    },
    {
      "bioguideId": "C001119",
      "district": "2",
      "firstName": "Angie",
      "fullName": "Rep. Craig, Angie [D-MN-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Craig",
      "party": "D",
      "sponsorshipDate": "2025-03-10",
      "state": "MN"
    },
    {
      "bioguideId": "S001172",
      "district": "3",
      "firstName": "Adrian",
      "fullName": "Rep. Smith, Adrian [R-NE-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Smith",
      "party": "R",
      "sponsorshipDate": "2025-03-10",
      "state": "NE"
    },
    {
      "bioguideId": "F000475",
      "district": "1",
      "firstName": "Brad",
      "fullName": "Rep. Finstad, Brad [R-MN-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Finstad",
      "party": "R",
      "sponsorshipDate": "2025-03-10",
      "state": "MN"
    },
    {
      "bioguideId": "F000446",
      "district": "4",
      "firstName": "Randy",
      "fullName": "Rep. Feenstra, Randy [R-IA-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Feenstra",
      "party": "R",
      "sponsorshipDate": "2025-03-10",
      "state": "IA"
    },
    {
      "bioguideId": "M001204",
      "district": "9",
      "firstName": "Daniel",
      "fullName": "Rep. Meuser, Daniel [R-PA-9]",
      "isOriginalCosponsor": "True",
      "lastName": "Meuser",
      "party": "R",
      "sponsorshipDate": "2025-03-10",
      "state": "PA"
    },
    {
      "bioguideId": "L000566",
      "district": "5",
      "firstName": "Robert",
      "fullName": "Rep. Latta, Robert E. [R-OH-5]",
      "isOriginalCosponsor": "True",
      "lastName": "Latta",
      "middleName": "E.",
      "party": "R",
      "sponsorshipDate": "2025-03-10",
      "state": "OH"
    },
    {
      "bioguideId": "F000469",
      "district": "1",
      "firstName": "Russ",
      "fullName": "Rep. Fulcher, Russ [R-ID-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Fulcher",
      "party": "R",
      "sponsorshipDate": "2025-03-10",
      "state": "ID"
    },
    {
      "bioguideId": "W000812",
      "district": "2",
      "firstName": "Ann",
      "fullName": "Rep. Wagner, Ann [R-MO-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Wagner",
      "party": "R",
      "sponsorshipDate": "2025-03-10",
      "state": "MO"
    },
    {
      "bioguideId": "T000478",
      "district": "24",
      "firstName": "Claudia",
      "fullName": "Rep. Tenney, Claudia [R-NY-24]",
      "isOriginalCosponsor": "True",
      "lastName": "Tenney",
      "party": "R",
      "sponsorshipDate": "2025-03-10",
      "state": "NY"
    },
    {
      "bioguideId": "N000189",
      "district": "4",
      "firstName": "Dan",
      "fullName": "Rep. Newhouse, Dan [R-WA-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Newhouse",
      "party": "R",
      "sponsorshipDate": "2025-03-10",
      "state": "WA"
    },
    {
      "bioguideId": "F000459",
      "district": "3",
      "firstName": "Charles",
      "fullName": "Rep. Fleischmann, Charles J. \"Chuck\" [R-TN-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Fleischmann",
      "middleName": "J. \"Chuck\"",
      "party": "R",
      "sponsorshipDate": "2025-03-10",
      "state": "TN"
    },
    {
      "bioguideId": "A000379",
      "district": "4",
      "firstName": "Mark",
      "fullName": "Rep. Alford, Mark [R-MO-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Alford",
      "party": "R",
      "sponsorshipDate": "2025-03-10",
      "state": "MO"
    },
    {
      "bioguideId": "M001194",
      "district": "2",
      "firstName": "John",
      "fullName": "Rep. Moolenaar, John R. [R-MI-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Moolenaar",
      "middleName": "R.",
      "party": "R",
      "sponsorshipDate": "2025-03-10",
      "state": "MI"
    },
    {
      "bioguideId": "G000546",
      "district": "6",
      "firstName": "Sam",
      "fullName": "Rep. Graves, Sam [R-MO-6]",
      "isOriginalCosponsor": "True",
      "lastName": "Graves",
      "party": "R",
      "sponsorshipDate": "2025-03-10",
      "state": "MO"
    },
    {
      "bioguideId": "L000491",
      "district": "3",
      "firstName": "Frank",
      "fullName": "Rep. Lucas, Frank D. [R-OK-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Lucas",
      "middleName": "D.",
      "party": "R",
      "sponsorshipDate": "2025-03-10",
      "state": "OK"
    },
    {
      "bioguideId": "S001224",
      "district": "3",
      "firstName": "Keith",
      "fullName": "Rep. Self, Keith [R-TX-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Self",
      "party": "R",
      "sponsorshipDate": "2025-03-10",
      "state": "TX"
    },
    {
      "bioguideId": "G000591",
      "district": "3",
      "firstName": "Michael",
      "fullName": "Rep. Guest, Michael [R-MS-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Guest",
      "party": "R",
      "sponsorshipDate": "2025-03-10",
      "state": "MS"
    },
    {
      "bioguideId": "S001228",
      "district": "2",
      "firstName": "Derek",
      "fullName": "Rep. Schmidt, Derek [R-KS-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Schmidt",
      "party": "R",
      "sponsorshipDate": "2025-03-10",
      "state": "KS"
    },
    {
      "bioguideId": "M001211",
      "district": "15",
      "firstName": "Mary",
      "fullName": "Rep. Miller, Mary E. [R-IL-15]",
      "isOriginalCosponsor": "True",
      "lastName": "Miller",
      "middleName": "E.",
      "party": "R",
      "sponsorshipDate": "2025-03-10",
      "state": "IL"
    },
    {
      "bioguideId": "R000612",
      "district": "6",
      "firstName": "John",
      "fullName": "Rep. Rose, John W. [R-TN-6]",
      "isOriginalCosponsor": "True",
      "lastName": "Rose",
      "middleName": "W.",
      "party": "R",
      "sponsorshipDate": "2025-03-10",
      "state": "TN"
    },
    {
      "bioguideId": "C001053",
      "district": "4",
      "firstName": "Tom",
      "fullName": "Rep. Cole, Tom [R-OK-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Cole",
      "party": "R",
      "sponsorshipDate": "2025-03-10",
      "state": "OK"
    },
    {
      "bioguideId": "M001212",
      "district": "1",
      "firstName": "Barry",
      "fullName": "Rep. Moore, Barry [R-AL-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Moore",
      "party": "R",
      "sponsorshipDate": "2025-03-10",
      "state": "AL"
    },
    {
      "bioguideId": "V000135",
      "district": "3",
      "firstName": "Derrick",
      "fullName": "Rep. Van Orden, Derrick [R-WI-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Van Orden",
      "party": "R",
      "sponsorshipDate": "2025-03-11",
      "state": "WI"
    },
    {
      "bioguideId": "L000585",
      "district": "16",
      "firstName": "Darin",
      "fullName": "Rep. LaHood, Darin [R-IL-16]",
      "isOriginalCosponsor": "False",
      "lastName": "LaHood",
      "party": "R",
      "sponsorshipDate": "2025-03-11",
      "state": "IL"
    },
    {
      "bioguideId": "E000300",
      "district": "8",
      "firstName": "Gabe",
      "fullName": "Rep. Evans, Gabe [R-CO-8]",
      "isOriginalCosponsor": "False",
      "lastName": "Evans",
      "party": "R",
      "sponsorshipDate": "2025-03-25",
      "state": "CO"
    },
    {
      "bioguideId": "M001224",
      "district": "1",
      "firstName": "Nathaniel",
      "fullName": "Rep. Moran, Nathaniel [R-TX-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Moran",
      "party": "R",
      "sponsorshipDate": "2025-03-26",
      "state": "TX"
    },
    {
      "bioguideId": "S001196",
      "district": "21",
      "firstName": "Elise",
      "fullName": "Rep. Stefanik, Elise M. [R-NY-21]",
      "isOriginalCosponsor": "False",
      "lastName": "Stefanik",
      "middleName": "M.",
      "party": "R",
      "sponsorshipDate": "2025-04-09",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hres/BILLS-119hres206ih.xml",
      "text": "IV\n119th CONGRESS\n1st Session\nH. RES. 206\nIN THE HOUSE OF REPRESENTATIVES\nMarch 10, 2025 Mr. Mann (for himself, Mr. Costa , Mr. Panetta , Ms. Craig , Mr. Smith of Nebraska , Mr. Finstad , Mr. Feenstra , Mr. Meuser , Mr. Latta , Mr. Fulcher , Mrs. Wagner , Ms. Tenney , Mr. Newhouse , Mr. Fleischmann , Mr. Alford , Mr. Moolenaar , Mr. Graves , Mr. Lucas , Mr. Self , Mr. Guest , Mr. Schmidt , Mrs. Miller of Illinois , Mr. Rose , Mr. Cole , and Mr. Moore of Alabama ) submitted the following resolution; which was referred to the Committee on Ways and Means\nRESOLUTION\nRecognizing the importance of stepped-up basis under section 1014 of the Internal Revenue Code of 1986 in preserving family-owned farms and small businesses.\nThat the House of Representatives\u2014\n**(1)**\nsupports the preservation of the stepped-up basis;\n**(2)**\nopposes any efforts to impose new taxes on family farms or small businesses; and\n**(3)**\nrecognizes the importance of generational transfers of farm and family-owned business operations.",
      "versionDate": "2025-03-10",
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
        "name": "Taxation",
        "updateDate": "2025-05-06T14:10:20Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-03-10",
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
          "measure-id": "id119hres206",
          "measure-number": "206",
          "measure-type": "hres",
          "orig-publish-date": "2025-03-10",
          "originChamber": "HOUSE",
          "update-date": "2026-05-07"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hres206v00",
            "update-date": "2026-05-07"
          },
          "action-date": "2025-03-10",
          "action-desc": "Introduced in House",
          "summary-text": "<p>This resolution supports preserving the stepped-up basis of certain inherited assets (such as land, equipment, or buildings), opposes any efforts to impose new taxes on family farms or small businesses, and recognizes the importance of generational transfers of farm and family-owned businesses.\u00a0</p><p>As background, the basis for federal tax purposes of certain inherited assets is reset (or stepped\u00a0up) from the original cost basis to the fair market value of the asset on the date of the previous owner\u2019s death. Thus, any gain or loss on the subsequent sale of an inherited asset generally is calculated based on the asset\u2019s stepped-up basis (and not the original cost basis).</p>"
        },
        "title": "Recognizing the importance of stepped-up basis under section 1014 of the Internal Revenue Code of 1986 in preserving family-owned farms and small businesses."
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hres/BILLSUM-119hres206.xml",
    "summary": {
      "actionDate": "2025-03-10",
      "actionDesc": "Introduced in House",
      "text": "<p>This resolution supports preserving the stepped-up basis of certain inherited assets (such as land, equipment, or buildings), opposes any efforts to impose new taxes on family farms or small businesses, and recognizes the importance of generational transfers of farm and family-owned businesses.\u00a0</p><p>As background, the basis for federal tax purposes of certain inherited assets is reset (or stepped\u00a0up) from the original cost basis to the fair market value of the asset on the date of the previous owner\u2019s death. Thus, any gain or loss on the subsequent sale of an inherited asset generally is calculated based on the asset\u2019s stepped-up basis (and not the original cost basis).</p>",
      "updateDate": "2026-05-07",
      "versionCode": "id119hres206"
    },
    "title": "Recognizing the importance of stepped-up basis under section 1014 of the Internal Revenue Code of 1986 in preserving family-owned farms and small businesses."
  },
  "summaries": [
    {
      "actionDate": "2025-03-10",
      "actionDesc": "Introduced in House",
      "text": "<p>This resolution supports preserving the stepped-up basis of certain inherited assets (such as land, equipment, or buildings), opposes any efforts to impose new taxes on family farms or small businesses, and recognizes the importance of generational transfers of farm and family-owned businesses.\u00a0</p><p>As background, the basis for federal tax purposes of certain inherited assets is reset (or stepped\u00a0up) from the original cost basis to the fair market value of the asset on the date of the previous owner\u2019s death. Thus, any gain or loss on the subsequent sale of an inherited asset generally is calculated based on the asset\u2019s stepped-up basis (and not the original cost basis).</p>",
      "updateDate": "2026-05-07",
      "versionCode": "id119hres206"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-03-10",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hres/BILLS-119hres206ih.xml"
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
      "title": "Recognizing the importance of stepped-up basis under section 1014 of the Internal Revenue Code of 1986 in preserving family-owned farms and small businesses.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-11T08:48:24Z"
    },
    {
      "title": "Recognizing the importance of stepped-up basis under section 1014 of the Internal Revenue Code of 1986 in preserving family-owned farms and small businesses.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-03-11T08:06:16Z"
    }
  ]
}
```
