# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hres/16?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/hres/16
- Title: Recognizing Russian actions in Ukraine as a genocide.
- Congress: 119
- Bill type: HRES
- Bill number: 16
- Origin chamber: House
- Introduced date: 2025-01-06
- Update date: 2025-02-27T09:06:13Z
- Update date including text: 2025-02-27T09:06:13Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-01-06: Introduced in House
- 2025-01-06 - IntroReferral: Referred to the House Committee on Foreign Affairs.
- 2025-01-06 - Committee: Submitted in House
- 2025-01-06 - IntroReferral: Submitted in House
- Latest action: 2025-01-06: Submitted in House

## Actions

- 2025-01-06 - IntroReferral: Referred to the House Committee on Foreign Affairs.
- 2025-01-06 - Committee: Submitted in House
- 2025-01-06 - IntroReferral: Submitted in House

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-01-06",
    "latestAction": {
      "actionDate": "2025-01-06",
      "text": "Submitted in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/hres/16",
    "number": "16",
    "originChamber": "House",
    "policyArea": {
      "name": "International Affairs"
    },
    "sponsors": [
      {
        "bioguideId": "C001068",
        "district": "9",
        "firstName": "Steve",
        "fullName": "Rep. Cohen, Steve [D-TN-9]",
        "lastName": "Cohen",
        "party": "D",
        "state": "TN"
      }
    ],
    "title": "Recognizing Russian actions in Ukraine as a genocide.",
    "type": "HRES",
    "updateDate": "2025-02-27T09:06:13Z",
    "updateDateIncludingText": "2025-02-27T09:06:13Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-01-06",
      "committees": {
        "item": {
          "name": "Foreign Affairs Committee",
          "systemCode": "hsfa00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Foreign Affairs.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "H12100",
      "actionDate": "2025-01-06",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Submitted in House",
      "type": "Committee"
    },
    {
      "actionCode": "1025",
      "actionDate": "2025-01-06",
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
          "date": "2025-01-06T17:00:15Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Foreign Affairs Committee",
      "systemCode": "hsfa00",
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
      "bioguideId": "W000795",
      "district": "2",
      "firstName": "Joe",
      "fullName": "Rep. Wilson, Joe [R-SC-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Wilson",
      "party": "R",
      "sponsorshipDate": "2025-01-06",
      "state": "SC"
    },
    {
      "bioguideId": "B001296",
      "district": "2",
      "firstName": "Brendan",
      "fullName": "Rep. Boyle, Brendan F. [D-PA-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Boyle",
      "middleName": "F.",
      "party": "D",
      "sponsorshipDate": "2025-01-06",
      "state": "PA"
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
      "sponsorshipDate": "2025-01-06",
      "state": "PA"
    },
    {
      "bioguideId": "D000399",
      "district": "37",
      "firstName": "Lloyd",
      "fullName": "Rep. Doggett, Lloyd [D-TX-37]",
      "isOriginalCosponsor": "True",
      "lastName": "Doggett",
      "party": "D",
      "sponsorshipDate": "2025-01-06",
      "state": "TX"
    },
    {
      "bioguideId": "S001215",
      "district": "11",
      "firstName": "Haley",
      "fullName": "Rep. Stevens, Haley M. [D-MI-11]",
      "isOriginalCosponsor": "True",
      "lastName": "Stevens",
      "middleName": "M.",
      "party": "D",
      "sponsorshipDate": "2025-01-06",
      "state": "MI"
    },
    {
      "bioguideId": "Q000023",
      "district": "5",
      "firstName": "Mike",
      "fullName": "Rep. Quigley, Mike [D-IL-5]",
      "isOriginalCosponsor": "True",
      "lastName": "Quigley",
      "party": "D",
      "sponsorshipDate": "2025-01-06",
      "state": "IL"
    },
    {
      "bioguideId": "L000599",
      "district": "17",
      "firstName": "Michael",
      "fullName": "Rep. Lawler, Michael [R-NY-17]",
      "isOriginalCosponsor": "True",
      "lastName": "Lawler",
      "party": "R",
      "sponsorshipDate": "2025-01-06",
      "state": "NY"
    },
    {
      "bioguideId": "C001059",
      "district": "21",
      "firstName": "Jim",
      "fullName": "Rep. Costa, Jim [D-CA-21]",
      "isOriginalCosponsor": "True",
      "lastName": "Costa",
      "party": "D",
      "sponsorshipDate": "2025-01-06",
      "state": "CA"
    },
    {
      "bioguideId": "N000147",
      "district": "0",
      "firstName": "Eleanor",
      "fullName": "Del. Norton, Eleanor Holmes [D-DC]",
      "isOriginalCosponsor": "True",
      "lastName": "Norton",
      "middleName": "Holmes",
      "party": "D",
      "sponsorshipDate": "2025-01-06",
      "state": "DC"
    },
    {
      "bioguideId": "T000474",
      "district": "35",
      "firstName": "Norma",
      "fullName": "Rep. Torres, Norma J. [D-CA-35]",
      "isOriginalCosponsor": "True",
      "lastName": "Torres",
      "middleName": "J.",
      "party": "D",
      "sponsorshipDate": "2025-01-06",
      "state": "CA"
    },
    {
      "bioguideId": "V000131",
      "district": "33",
      "firstName": "Marc",
      "fullName": "Rep. Veasey, Marc A. [D-TX-33]",
      "isOriginalCosponsor": "True",
      "lastName": "Veasey",
      "middleName": "A.",
      "party": "D",
      "sponsorshipDate": "2025-01-06",
      "state": "TX"
    },
    {
      "bioguideId": "K000375",
      "district": "9",
      "firstName": "William",
      "fullName": "Rep. Keating, William R. [D-MA-9]",
      "isOriginalCosponsor": "True",
      "lastName": "Keating",
      "middleName": "R.",
      "party": "D",
      "sponsorshipDate": "2025-01-06",
      "state": "MA"
    },
    {
      "bioguideId": "K000009",
      "district": "9",
      "firstName": "Marcy",
      "fullName": "Rep. Kaptur, Marcy [D-OH-9]",
      "isOriginalCosponsor": "True",
      "lastName": "Kaptur",
      "party": "D",
      "sponsorshipDate": "2025-01-06",
      "state": "OH"
    },
    {
      "bioguideId": "G000599",
      "district": "10",
      "firstName": "Daniel",
      "fullName": "Rep. Goldman, Daniel S. [D-NY-10]",
      "isOriginalCosponsor": "False",
      "lastName": "Goldman",
      "middleName": "S.",
      "party": "D",
      "sponsorshipDate": "2025-01-16",
      "state": "NY"
    },
    {
      "bioguideId": "G000583",
      "district": "5",
      "firstName": "Josh",
      "fullName": "Rep. Gottheimer, Josh [D-NJ-5]",
      "isOriginalCosponsor": "False",
      "lastName": "Gottheimer",
      "party": "D",
      "sponsorshipDate": "2025-02-04",
      "state": "NJ"
    },
    {
      "bioguideId": "P000620",
      "district": "7",
      "firstName": "Brittany",
      "fullName": "Rep. Pettersen, Brittany [D-CO-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Pettersen",
      "party": "D",
      "sponsorshipDate": "2025-02-04",
      "state": "CO"
    },
    {
      "bioguideId": "M000687",
      "district": "7",
      "firstName": "Kweisi",
      "fullName": "Rep. Mfume, Kweisi [D-MD-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Mfume",
      "party": "D",
      "sponsorshipDate": "2025-02-10",
      "state": "MD"
    },
    {
      "bioguideId": "C001067",
      "district": "9",
      "firstName": "Yvette",
      "fullName": "Rep. Clarke, Yvette D. [D-NY-9]",
      "isOriginalCosponsor": "False",
      "lastName": "Clarke",
      "middleName": "D.",
      "party": "D",
      "sponsorshipDate": "2025-02-26",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hres/BILLS-119hres16ih.xml",
      "text": "IV\n119th CONGRESS\n1st Session\nH. RES. 16\nIN THE HOUSE OF REPRESENTATIVES\nJanuary 6, 2025 Mr. Cohen (for himself, Mr. Wilson of South Carolina , Mr. Boyle of Pennsylvania , Mr. Fitzpatrick , Mr. Doggett , Ms. Stevens , Mr. Quigley , Mr. Lawler , Mr. Costa , Ms. Norton , Mrs. Torres of California , Mr. Veasey , Mr. Keating , and Ms. Kaptur ) submitted the following resolution; which was referred to the Committee on Foreign Affairs\nRESOLUTION\nRecognizing Russian actions in Ukraine as a genocide.\nThat the House of Representatives\u2014\n**(1)**\ncondemns the Russian Federation for committing acts of genocide against the Ukrainian people;\n**(2)**\ncalls on the United States, in cooperation with North Atlantic Treaty Organization and European Union allies, to undertake measures to support the Ukrainian Government to prevent further acts of Russian genocide against the Ukrainian people; and\n**(3)**\nsupports tribunals and international criminal investigations to hold Russian political leaders and military personnel to account for a war of aggression, war crimes, crimes against humanity, and genocide.",
      "versionDate": "2025-01-06",
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
      "legislativeSubjects": {
        "item": [
          {
            "name": "Alliances",
            "updateDate": "2025-01-24T15:18:04Z"
          },
          {
            "name": "Conflicts and wars",
            "updateDate": "2025-01-24T15:17:50Z"
          },
          {
            "name": "Europe",
            "updateDate": "2025-01-24T15:17:43Z"
          },
          {
            "name": "Russia",
            "updateDate": "2025-01-24T15:17:29Z"
          },
          {
            "name": "Ukraine",
            "updateDate": "2025-01-24T15:17:36Z"
          },
          {
            "name": "War crimes, genocide, crimes against humanity",
            "updateDate": "2025-01-24T15:17:57Z"
          }
        ]
      },
      "policyArea": {
        "name": "International Affairs",
        "updateDate": "2025-01-17T13:54:22Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-01-06",
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
          "measure-id": "id119hres16",
          "measure-number": "16",
          "measure-type": "hres",
          "orig-publish-date": "2025-01-06",
          "originChamber": "HOUSE",
          "update-date": "2025-01-31"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hres16v00",
            "update-date": "2025-01-31"
          },
          "action-date": "2025-01-06",
          "action-desc": "Introduced in House",
          "summary-text": "<p>This resolution condemns Russia for committing acts of genocide against the Ukrainian people. It also calls on the United States, in cooperation with North Atlantic Treaty Organization and European Union allies, to undertake measures to support the Ukrainian government to prevent further acts of Russian genocide against the Ukrainian people.</p>"
        },
        "title": "Recognizing Russian actions in Ukraine as a genocide."
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hres/BILLSUM-119hres16.xml",
    "summary": {
      "actionDate": "2025-01-06",
      "actionDesc": "Introduced in House",
      "text": "<p>This resolution condemns Russia for committing acts of genocide against the Ukrainian people. It also calls on the United States, in cooperation with North Atlantic Treaty Organization and European Union allies, to undertake measures to support the Ukrainian government to prevent further acts of Russian genocide against the Ukrainian people.</p>",
      "updateDate": "2025-01-31",
      "versionCode": "id119hres16"
    },
    "title": "Recognizing Russian actions in Ukraine as a genocide."
  },
  "summaries": [
    {
      "actionDate": "2025-01-06",
      "actionDesc": "Introduced in House",
      "text": "<p>This resolution condemns Russia for committing acts of genocide against the Ukrainian people. It also calls on the United States, in cooperation with North Atlantic Treaty Organization and European Union allies, to undertake measures to support the Ukrainian government to prevent further acts of Russian genocide against the Ukrainian people.</p>",
      "updateDate": "2025-01-31",
      "versionCode": "id119hres16"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-01-06",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hres/BILLS-119hres16ih.xml"
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
      "title": "Recognizing Russian actions in Ukraine as a genocide.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-01-07T14:06:35Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Recognizing Russian actions in Ukraine as a genocide.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-01-07T14:06:35Z"
    }
  ]
}
```
