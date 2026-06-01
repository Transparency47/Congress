# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hres/76?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-resolution/76
- Title: Recognizing Gold Shield Families and affirming that their sacrifices and difficulties should not be forgotten.
- Congress: 119
- Bill type: HRES
- Bill number: 76
- Origin chamber: House
- Introduced date: 2025-01-28
- Update date: 2026-04-07T16:24:39Z
- Update date including text: 2026-04-07T16:24:39Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-01-28: Introduced in House
- 2025-01-28 - IntroReferral: Referred to the House Committee on Transportation and Infrastructure.
- 2025-01-28 - Committee: Submitted in House
- Latest action: 2025-01-28: Submitted in House

## Actions

- 2025-01-28 - IntroReferral: Referred to the House Committee on Transportation and Infrastructure.
- 2025-01-28 - Committee: Submitted in House

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-01-28",
    "latestAction": {
      "actionDate": "2025-01-28",
      "text": "Submitted in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-resolution/76",
    "number": "76",
    "originChamber": "House",
    "policyArea": {
      "name": "Emergency Management"
    },
    "sponsors": [
      {
        "bioguideId": "M001204",
        "district": "9",
        "firstName": "Daniel",
        "fullName": "Rep. Meuser, Daniel [R-PA-9]",
        "lastName": "Meuser",
        "party": "R",
        "state": "PA"
      }
    ],
    "title": "Recognizing Gold Shield Families and affirming that their sacrifices and difficulties should not be forgotten.",
    "type": "HRES",
    "updateDate": "2026-04-07T16:24:39Z",
    "updateDateIncludingText": "2026-04-07T16:24:39Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-01-28",
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
      "actionCode": "H12100",
      "actionDate": "2025-01-28",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Submitted in House",
      "type": "Committee"
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
          "date": "2025-01-28T16:06:30Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Transportation and Infrastructure Committee",
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
      "bioguideId": "M000317",
      "district": "11",
      "firstName": "Nicole",
      "fullName": "Rep. Malliotakis, Nicole [R-NY-11]",
      "isOriginalCosponsor": "True",
      "lastName": "Malliotakis",
      "party": "R",
      "sponsorshipDate": "2025-01-28",
      "state": "NY"
    },
    {
      "bioguideId": "B001298",
      "district": "2",
      "firstName": "Don",
      "fullName": "Rep. Bacon, Don [R-NE-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Bacon",
      "party": "R",
      "sponsorshipDate": "2025-01-28",
      "state": "NE"
    },
    {
      "bioguideId": "F000466",
      "district": "1",
      "firstName": "Brian",
      "fullName": "Rep. Fitzpatrick, Brian K. [R-PA-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Fitzpatrick",
      "middleName": "K.",
      "party": "R",
      "sponsorshipDate": "2025-01-28",
      "state": "PA"
    },
    {
      "bioguideId": "P000613",
      "district": "19",
      "firstName": "Jimmy",
      "fullName": "Rep. Panetta, Jimmy [D-CA-19]",
      "isOriginalCosponsor": "True",
      "lastName": "Panetta",
      "party": "D",
      "sponsorshipDate": "2025-01-28",
      "state": "CA"
    },
    {
      "bioguideId": "L000601",
      "district": "1",
      "firstName": "Greg",
      "fullName": "Rep. Landsman, Greg [D-OH-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Landsman",
      "party": "D",
      "sponsorshipDate": "2025-01-28",
      "state": "OH"
    },
    {
      "bioguideId": "G000583",
      "district": "5",
      "firstName": "Josh",
      "fullName": "Rep. Gottheimer, Josh [D-NJ-5]",
      "isOriginalCosponsor": "True",
      "lastName": "Gottheimer",
      "party": "D",
      "sponsorshipDate": "2025-01-28",
      "state": "NJ"
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
      "sponsorshipDate": "2025-01-28",
      "state": "TN"
    },
    {
      "bioguideId": "K000392",
      "district": "8",
      "firstName": "David",
      "fullName": "Rep. Kustoff, David [R-TN-8]",
      "isOriginalCosponsor": "True",
      "lastName": "Kustoff",
      "party": "R",
      "sponsorshipDate": "2025-01-28",
      "state": "TN"
    },
    {
      "bioguideId": "H001090",
      "district": "9",
      "firstName": "Josh",
      "fullName": "Rep. Harder, Josh [D-CA-9]",
      "isOriginalCosponsor": "True",
      "lastName": "Harder",
      "party": "D",
      "sponsorshipDate": "2025-01-28",
      "state": "CA"
    },
    {
      "bioguideId": "P000614",
      "district": "1",
      "firstName": "Chris",
      "fullName": "Rep. Pappas, Chris [D-NH-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Pappas",
      "party": "D",
      "sponsorshipDate": "2025-01-28",
      "state": "NH"
    },
    {
      "bioguideId": "B001260",
      "district": "16",
      "firstName": "Vern",
      "fullName": "Rep. Buchanan, Vern [R-FL-16]",
      "isOriginalCosponsor": "True",
      "lastName": "Buchanan",
      "party": "R",
      "sponsorshipDate": "2025-01-28",
      "state": "FL"
    },
    {
      "bioguideId": "F000246",
      "district": "4",
      "firstName": "Pat",
      "fullName": "Rep. Fallon, Pat [R-TX-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Fallon",
      "party": "R",
      "sponsorshipDate": "2025-01-28",
      "state": "TX"
    },
    {
      "bioguideId": "L000599",
      "district": "17",
      "firstName": "Michael",
      "fullName": "Rep. Lawler, Michael [R-NY-17]",
      "isOriginalCosponsor": "True",
      "lastName": "Lawler",
      "party": "R",
      "sponsorshipDate": "2025-01-28",
      "state": "NY"
    },
    {
      "bioguideId": "H001099",
      "district": "8",
      "firstName": "Mike",
      "fullName": "Rep. Haridopolos, Mike [R-FL-8]",
      "isOriginalCosponsor": "False",
      "lastName": "Haridopolos",
      "party": "R",
      "sponsorshipDate": "2025-02-04",
      "state": "FL"
    },
    {
      "bioguideId": "M000871",
      "district": "1",
      "firstName": "Tracey",
      "fullName": "Rep. Mann, Tracey [R-KS-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Mann",
      "party": "R",
      "sponsorshipDate": "2025-02-27",
      "state": "KS"
    },
    {
      "bioguideId": "Y000067",
      "district": "2",
      "firstName": "Rudy",
      "fullName": "Rep. Yakym, Rudy [R-IN-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Yakym",
      "party": "R",
      "sponsorshipDate": "2025-03-31",
      "state": "IN"
    },
    {
      "bioguideId": "C001039",
      "district": "3",
      "firstName": "Kat",
      "fullName": "Rep. Cammack, Kat [R-FL-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Cammack",
      "party": "R",
      "sponsorshipDate": "2025-03-31",
      "state": "FL"
    },
    {
      "bioguideId": "N000026",
      "district": "22",
      "firstName": "Troy",
      "fullName": "Rep. Nehls, Troy E. [R-TX-22]",
      "isOriginalCosponsor": "False",
      "lastName": "Nehls",
      "middleName": "E.",
      "party": "R",
      "sponsorshipDate": "2025-03-31",
      "state": "TX"
    },
    {
      "bioguideId": "R000622",
      "district": "19",
      "firstName": "Josh",
      "fullName": "Rep. Riley, Josh [D-NY-19]",
      "isOriginalCosponsor": "False",
      "lastName": "Riley",
      "party": "D",
      "sponsorshipDate": "2025-12-10",
      "state": "NY"
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
      "sponsorshipDate": "2025-12-18",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hres/BILLS-119hres76ih.xml",
      "text": "IV\n119th CONGRESS\n1st Session\nH. RES. 76\nIN THE HOUSE OF REPRESENTATIVES\nJanuary 28, 2025 Mr. Meuser (for himself, Ms. Malliotakis , Mr. Bacon , Mr. Fitzpatrick , Mr. Panetta , Mr. Landsman , Mr. Gottheimer , Mr. Rose , Mr. Kustoff , Mr. Harder of California , Mr. Pappas , Mr. Buchanan , Mr. Fallon , and Mr. Lawler ) submitted the following resolution; which was referred to the Committee on Transportation and Infrastructure\nRESOLUTION\nRecognizing Gold Shield Families and affirming that their sacrifices and difficulties should not be forgotten.\nThat by the House of Representatives\u2014\n**(1)**\nthat Gold Shield Families, consisting of the families of fallen police officers, firefighters, emergency medical technicians (EMTs), correction officers, emergency dispatch officers, and emergency service providers, are hereby recognized and honored for their immeasurable sacrifices and steadfast support of their loved ones in service to our Nation;\n**(2)**\nthat this recognition stands as a testament to the enduring gratitude and appreciation of the United States for the tremendous contributions and sacrifices made by Gold Shield Families; and\n**(3)**\nthat a copy of this resolution be transmitted to the President of the United States and made publicly available to honor and recognize Gold Shield Families for their sacrifices and unwavering support of our Nation's first responders and emergency service providers, affirming that their sacrifices and difficulties should not be forgotten.",
      "versionDate": "2025-01-28",
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
        "name": "Emergency Management",
        "updateDate": "2025-01-31T18:20:37Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-01-28",
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
          "measure-id": "id119hres76",
          "measure-number": "76",
          "measure-type": "hres",
          "orig-publish-date": "2025-01-28",
          "originChamber": "HOUSE",
          "update-date": "2026-04-07"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hres76v00",
            "update-date": "2026-04-07"
          },
          "action-date": "2025-01-28",
          "action-desc": "Introduced in House",
          "summary-text": "<p>This resolution recognizes and honors Gold Shield Families for their sacrifices and support of their loved ones in service to our nation. Gold Shield Families consist of the families of fallen police officers, firefighters, emergency medical technicians (EMTs), correction officers, emergency dispatch officers, and emergency service providers.</p>"
        },
        "title": "Recognizing Gold Shield Families and affirming that their sacrifices and difficulties should not be forgotten."
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hres/BILLSUM-119hres76.xml",
    "summary": {
      "actionDate": "2025-01-28",
      "actionDesc": "Introduced in House",
      "text": "<p>This resolution recognizes and honors Gold Shield Families for their sacrifices and support of their loved ones in service to our nation. Gold Shield Families consist of the families of fallen police officers, firefighters, emergency medical technicians (EMTs), correction officers, emergency dispatch officers, and emergency service providers.</p>",
      "updateDate": "2026-04-07",
      "versionCode": "id119hres76"
    },
    "title": "Recognizing Gold Shield Families and affirming that their sacrifices and difficulties should not be forgotten."
  },
  "summaries": [
    {
      "actionDate": "2025-01-28",
      "actionDesc": "Introduced in House",
      "text": "<p>This resolution recognizes and honors Gold Shield Families for their sacrifices and support of their loved ones in service to our nation. Gold Shield Families consist of the families of fallen police officers, firefighters, emergency medical technicians (EMTs), correction officers, emergency dispatch officers, and emergency service providers.</p>",
      "updateDate": "2026-04-07",
      "versionCode": "id119hres76"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-01-28",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hres/BILLS-119hres76ih.xml"
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
      "title": "Recognizing Gold Shield Families and affirming that their sacrifices and difficulties should not be forgotten.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-01-29T11:48:21Z"
    },
    {
      "title": "Recognizing Gold Shield Families and affirming that their sacrifices and difficulties should not be forgotten.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-01-29T09:05:55Z"
    }
  ]
}
```
