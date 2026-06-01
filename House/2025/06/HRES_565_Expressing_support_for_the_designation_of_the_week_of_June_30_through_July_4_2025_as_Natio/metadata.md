# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hres/565?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-resolution/565
- Title: Expressing support for the designation of the week of June 30 through July 4, 2025, as "National Tire Safety Week" in the United States, and supporting the goals and ideals of "National Tire Safety Week" to educate American motorists about the importance of proper tire care and maintenance.
- Congress: 119
- Bill type: HRES
- Bill number: 565
- Origin chamber: House
- Introduced date: 2025-06-30
- Update date: 2025-09-11T08:06:41Z
- Update date including text: 2025-09-11T08:06:41Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-06-30: Introduced in House
- 2025-06-30 - IntroReferral: Referred to the House Committee on Transportation and Infrastructure.
- 2025-06-30 - IntroReferral: Submitted in House
- 2025-06-30 - IntroReferral: Submitted in House
- 2025-07-01 - Committee: Referred to the Subcommittee on Highways and Transit.
- Latest action: 2025-06-30: Submitted in House

## Actions

- 2025-06-30 - IntroReferral: Referred to the House Committee on Transportation and Infrastructure.
- 2025-06-30 - IntroReferral: Submitted in House
- 2025-06-30 - IntroReferral: Submitted in House
- 2025-07-01 - Committee: Referred to the Subcommittee on Highways and Transit.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-06-30",
    "latestAction": {
      "actionDate": "2025-06-30",
      "text": "Submitted in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-resolution/565",
    "number": "565",
    "originChamber": "House",
    "policyArea": {
      "name": "Transportation and Public Works"
    },
    "sponsors": [
      {
        "bioguideId": "M001236",
        "district": "14",
        "firstName": "Tim",
        "fullName": "Rep. Moore, Tim [R-NC-14]",
        "lastName": "Moore",
        "party": "R",
        "state": "NC"
      }
    ],
    "title": "Expressing support for the designation of the week of June 30 through July 4, 2025, as \"National Tire Safety Week\" in the United States, and supporting the goals and ideals of \"National Tire Safety Week\" to educate American motorists about the importance of proper tire care and maintenance.",
    "type": "HRES",
    "updateDate": "2025-09-11T08:06:41Z",
    "updateDateIncludingText": "2025-09-11T08:06:41Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-07-01",
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
      "actionDate": "2025-06-30",
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
      "actionCode": "H11100",
      "actionDate": "2025-06-30",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Submitted in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1025",
      "actionDate": "2025-06-30",
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
          "date": "2025-06-30T18:02:30Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Transportation and Infrastructure Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": {
              "date": "2025-07-01T16:59:01Z",
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
      "bioguideId": "S001223",
      "district": "13",
      "firstName": "Emilia",
      "fullName": "Rep. Sykes, Emilia Strong [D-OH-13]",
      "isOriginalCosponsor": "True",
      "lastName": "Sykes",
      "middleName": "Strong",
      "party": "D",
      "sponsorshipDate": "2025-06-30",
      "state": "OH"
    },
    {
      "bioguideId": "D000624",
      "district": "6",
      "firstName": "Debbie",
      "fullName": "Rep. Dingell, Debbie [D-MI-6]",
      "isOriginalCosponsor": "True",
      "lastName": "Dingell",
      "party": "D",
      "sponsorshipDate": "2025-06-30",
      "state": "MI"
    },
    {
      "bioguideId": "T000480",
      "district": "4",
      "firstName": "William",
      "fullName": "Rep. Timmons, William R. [R-SC-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Timmons",
      "middleName": "R.",
      "party": "R",
      "sponsorshipDate": "2025-06-30",
      "state": "SC"
    },
    {
      "bioguideId": "N000190",
      "district": "5",
      "firstName": "Ralph",
      "fullName": "Rep. Norman, Ralph [R-SC-5]",
      "isOriginalCosponsor": "True",
      "lastName": "Norman",
      "party": "R",
      "sponsorshipDate": "2025-06-30",
      "state": "SC"
    },
    {
      "bioguideId": "R000603",
      "district": "7",
      "firstName": "David",
      "fullName": "Rep. Rouzer, David [R-NC-7]",
      "isOriginalCosponsor": "True",
      "lastName": "Rouzer",
      "party": "R",
      "sponsorshipDate": "2025-06-30",
      "state": "NC"
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
      "sponsorshipDate": "2025-06-30",
      "state": "GA"
    },
    {
      "bioguideId": "R000619",
      "district": "6",
      "firstName": "Michael",
      "fullName": "Rep. Rulli, Michael A. [R-OH-6]",
      "isOriginalCosponsor": "True",
      "lastName": "Rulli",
      "middleName": "A.",
      "party": "R",
      "sponsorshipDate": "2025-06-30",
      "state": "OH"
    },
    {
      "bioguideId": "H001067",
      "district": "9",
      "firstName": "Richard",
      "fullName": "Rep. Hudson, Richard [R-NC-9]",
      "isOriginalCosponsor": "True",
      "lastName": "Hudson",
      "party": "R",
      "sponsorshipDate": "2025-06-30",
      "state": "NC"
    },
    {
      "bioguideId": "P000614",
      "district": "1",
      "firstName": "Chris",
      "fullName": "Rep. Pappas, Chris [D-NH-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Pappas",
      "party": "D",
      "sponsorshipDate": "2025-06-30",
      "state": "NH"
    },
    {
      "bioguideId": "M001225",
      "district": "15",
      "firstName": "Kevin",
      "fullName": "Rep. Mullin, Kevin [D-CA-15]",
      "isOriginalCosponsor": "True",
      "lastName": "Mullin",
      "party": "D",
      "sponsorshipDate": "2025-06-30",
      "state": "CA"
    },
    {
      "bioguideId": "F000110",
      "district": "6",
      "firstName": "Cleo",
      "fullName": "Rep. Fields, Cleo [D-LA-6]",
      "isOriginalCosponsor": "True",
      "lastName": "Fields",
      "party": "D",
      "sponsorshipDate": "2025-06-30",
      "state": "LA"
    },
    {
      "bioguideId": "D000530",
      "district": "17",
      "firstName": "Christopher",
      "fullName": "Rep. Deluzio, Christopher R. [D-PA-17]",
      "isOriginalCosponsor": "True",
      "lastName": "Deluzio",
      "middleName": "R.",
      "party": "D",
      "sponsorshipDate": "2025-06-30",
      "state": "PA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hres/BILLS-119hres565ih.xml",
      "text": "IV\n119th CONGRESS\n1st Session\nH. RES. 565\nIN THE HOUSE OF REPRESENTATIVES\nJune 30, 2025 Mr. Moore of North Carolina (for himself, Mrs. Sykes , Mrs. Dingell , Mr. Timmons , Mr. Norman , Mr. Rouzer , Mr. Carter of Georgia , Mr. Rulli , Mr. Hudson , Mr. Pappas , Mr. Mullin , Mr. Fields , and Mr. Deluzio ) submitted the following resolution; which was referred to the Committee on Transportation and Infrastructure\nRESOLUTION\nExpressing support for the designation of the week of June 30 through July 4, 2025, as National Tire Safety Week in the United States, and supporting the goals and ideals of National Tire Safety Week to educate American motorists about the importance of proper tire care and maintenance.\nThat the House of Representatives\u2014\n**(1)**\nsupports the designation of National Tire Safety Week ;\n**(2)**\nexpresses strong support for\u2014\n**(A)**\nthe goals and ideals of National Tire Safety Week ; and\n**(B)**\nefforts to reduce tire-related accidents, fatalities, and injuries; and\n**(3)**\nencourages the people of the United States to\u2014\n**(A)**\nparticipate in National Tire Safety Week events and activities; and\n**(B)**\neducate themselves and others on the importance of regularly inspecting and maintaining a vehicle\u2019s tires.",
      "versionDate": "2025-06-30",
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
        "name": "Transportation and Public Works",
        "updateDate": "2025-07-11T12:39:19Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-06-30",
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
          "measure-id": "id119hres565",
          "measure-number": "565",
          "measure-type": "hres",
          "orig-publish-date": "2025-06-30",
          "originChamber": "HOUSE",
          "update-date": "2025-08-18"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hres565v00",
            "update-date": "2025-08-18"
          },
          "action-date": "2025-06-30",
          "action-desc": "Introduced in House",
          "summary-text": "<p>This resolution supports the designation of National Tire Safety Week. The resolution also encourages people to educate themselves and others on the importance of regularly inspecting and maintaining a vehicle's tires.</p>"
        },
        "title": "Expressing support for the designation of the week of June 30 through July 4, 2025, as \"National Tire Safety Week\" in the United States, and supporting the goals and ideals of \"National Tire Safety Week\" to educate American motorists about the importance of proper tire care and maintenance."
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hres/BILLSUM-119hres565.xml",
    "summary": {
      "actionDate": "2025-06-30",
      "actionDesc": "Introduced in House",
      "text": "<p>This resolution supports the designation of National Tire Safety Week. The resolution also encourages people to educate themselves and others on the importance of regularly inspecting and maintaining a vehicle's tires.</p>",
      "updateDate": "2025-08-18",
      "versionCode": "id119hres565"
    },
    "title": "Expressing support for the designation of the week of June 30 through July 4, 2025, as \"National Tire Safety Week\" in the United States, and supporting the goals and ideals of \"National Tire Safety Week\" to educate American motorists about the importance of proper tire care and maintenance."
  },
  "summaries": [
    {
      "actionDate": "2025-06-30",
      "actionDesc": "Introduced in House",
      "text": "<p>This resolution supports the designation of National Tire Safety Week. The resolution also encourages people to educate themselves and others on the importance of regularly inspecting and maintaining a vehicle's tires.</p>",
      "updateDate": "2025-08-18",
      "versionCode": "id119hres565"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-06-30",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hres/BILLS-119hres565ih.xml"
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
      "title": "Expressing support for the designation of the week of June 30 through July 4, 2025, as \"National Tire Safety Week\" in the United States, and supporting the goals and ideals of \"National Tire Safety Week\" to educate American motorists about the importance of proper tire care and maintenance.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-07-01T08:18:21Z"
    },
    {
      "title": "Expressing support for the designation of the week of June 30 through July 4, 2025, as \"National Tire Safety Week\" in the United States, and supporting the goals and ideals of \"National Tire Safety Week\" to educate American motorists about the importance of proper tire care and maintenance.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-07-01T08:05:25Z"
    }
  ]
}
```
