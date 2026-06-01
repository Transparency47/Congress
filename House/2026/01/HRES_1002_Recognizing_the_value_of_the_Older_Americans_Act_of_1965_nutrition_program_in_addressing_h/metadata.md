# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hres/1002?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-resolution/1002
- Title: Recognizing the value of the Older Americans Act of 1965 nutrition program in addressing hunger, malnutrition, and isolation, and improving the health and quality of life for millions of our Nations seniors each year.
- Congress: 119
- Bill type: HRES
- Bill number: 1002
- Origin chamber: House
- Introduced date: 2026-01-15
- Update date: 2026-04-03T19:57:29Z
- Update date including text: 2026-04-03T19:57:29Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2026-01-15: Introduced in House
- 2026-01-15 - IntroReferral: Referred to the House Committee on Education and Workforce.
- 2026-01-15 - IntroReferral: Submitted in House
- 2026-01-15 - IntroReferral: Submitted in House
- 2026-02-04 - IntroReferral: Sponsor introductory remarks on measure. (CR H1992-1993)
- Latest action: 2026-01-15: Submitted in House

## Actions

- 2026-01-15 - IntroReferral: Referred to the House Committee on Education and Workforce.
- 2026-01-15 - IntroReferral: Submitted in House
- 2026-01-15 - IntroReferral: Submitted in House
- 2026-02-04 - IntroReferral: Sponsor introductory remarks on measure. (CR H1992-1993)

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-01-15",
    "latestAction": {
      "actionDate": "2026-01-15",
      "text": "Submitted in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-resolution/1002",
    "number": "1002",
    "originChamber": "House",
    "policyArea": {
      "name": "Social Welfare"
    },
    "sponsors": [
      {
        "bioguideId": "B001278",
        "district": "1",
        "firstName": "Suzanne",
        "fullName": "Rep. Bonamici, Suzanne [D-OR-1]",
        "lastName": "Bonamici",
        "party": "D",
        "state": "OR"
      }
    ],
    "title": "Recognizing the value of the Older Americans Act of 1965 nutrition program in addressing hunger, malnutrition, and isolation, and improving the health and quality of life for millions of our Nations seniors each year.",
    "type": "HRES",
    "updateDate": "2026-04-03T19:57:29Z",
    "updateDateIncludingText": "2026-04-03T19:57:29Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "B00100",
      "actionDate": "2026-02-04",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Sponsor introductory remarks on measure. (CR H1992-1993)",
      "type": "IntroReferral"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2026-01-15",
      "committees": {
        "item": {
          "name": "Education and Workforce Committee",
          "systemCode": "hsed00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Education and Workforce.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2026-01-15",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Submitted in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1025",
      "actionDate": "2026-01-15",
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
          "date": "2026-01-15T14:02:50Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Education and Workforce Committee",
      "systemCode": "hsed00",
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
      "bioguideId": "F000466",
      "district": "1",
      "firstName": "Brian",
      "fullName": "Rep. Fitzpatrick, Brian K. [R-PA-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Fitzpatrick",
      "middleName": "K.",
      "party": "R",
      "sponsorshipDate": "2026-01-15",
      "state": "PA"
    },
    {
      "bioguideId": "W000797",
      "district": "25",
      "firstName": "Debbie",
      "fullName": "Rep. Wasserman Schultz, Debbie [D-FL-25]",
      "isOriginalCosponsor": "True",
      "lastName": "Wasserman Schultz",
      "party": "D",
      "sponsorshipDate": "2026-01-15",
      "state": "FL"
    },
    {
      "bioguideId": "K000376",
      "district": "16",
      "firstName": "Mike",
      "fullName": "Rep. Kelly, Mike [R-PA-16]",
      "isOriginalCosponsor": "True",
      "lastName": "Kelly",
      "party": "R",
      "sponsorshipDate": "2026-01-15",
      "state": "PA"
    },
    {
      "bioguideId": "D000629",
      "district": "3",
      "firstName": "Sharice",
      "fullName": "Rep. Davids, Sharice [D-KS-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Davids",
      "party": "D",
      "sponsorshipDate": "2026-01-15",
      "state": "KS"
    },
    {
      "bioguideId": "F000462",
      "district": "22",
      "firstName": "Lois",
      "fullName": "Rep. Frankel, Lois [D-FL-22]",
      "isOriginalCosponsor": "True",
      "lastName": "Frankel",
      "party": "D",
      "sponsorshipDate": "2026-01-15",
      "state": "FL"
    },
    {
      "bioguideId": "S001145",
      "district": "9",
      "firstName": "Janice",
      "fullName": "Rep. Schakowsky, Janice D. [D-IL-9]",
      "isOriginalCosponsor": "True",
      "lastName": "Schakowsky",
      "middleName": "D.",
      "party": "D",
      "sponsorshipDate": "2026-01-15",
      "state": "IL"
    },
    {
      "bioguideId": "G000587",
      "district": "29",
      "firstName": "Sylvia",
      "fullName": "Rep. Garcia, Sylvia R. [D-TX-29]",
      "isOriginalCosponsor": "True",
      "lastName": "Garcia",
      "middleName": "R.",
      "party": "D",
      "sponsorshipDate": "2026-01-15",
      "state": "TX"
    },
    {
      "bioguideId": "C001068",
      "district": "9",
      "firstName": "Steve",
      "fullName": "Rep. Cohen, Steve [D-TN-9]",
      "isOriginalCosponsor": "True",
      "lastName": "Cohen",
      "party": "D",
      "sponsorshipDate": "2026-01-15",
      "state": "TN"
    },
    {
      "bioguideId": "D000624",
      "district": "6",
      "firstName": "Debbie",
      "fullName": "Rep. Dingell, Debbie [D-MI-6]",
      "isOriginalCosponsor": "True",
      "lastName": "Dingell",
      "party": "D",
      "sponsorshipDate": "2026-01-15",
      "state": "MI"
    },
    {
      "bioguideId": "B000490",
      "district": "2",
      "firstName": "Sanford",
      "fullName": "Rep. Bishop, Sanford D. [D-GA-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Bishop",
      "middleName": "D.",
      "party": "D",
      "sponsorshipDate": "2026-01-15",
      "state": "GA"
    },
    {
      "bioguideId": "N000147",
      "district": "0",
      "firstName": "Eleanor",
      "fullName": "Del. Norton, Eleanor Holmes [D-DC-At Large]",
      "isOriginalCosponsor": "True",
      "lastName": "Norton",
      "middleName": "Holmes",
      "party": "D",
      "sponsorshipDate": "2026-01-15",
      "state": "DC"
    },
    {
      "bioguideId": "M000312",
      "district": "2",
      "firstName": "James",
      "fullName": "Rep. McGovern, James P. [D-MA-2]",
      "isOriginalCosponsor": "True",
      "lastName": "McGovern",
      "middleName": "P.",
      "party": "D",
      "sponsorshipDate": "2026-01-15",
      "state": "MA"
    },
    {
      "bioguideId": "P000613",
      "district": "19",
      "firstName": "Jimmy",
      "fullName": "Rep. Panetta, Jimmy [D-CA-19]",
      "isOriginalCosponsor": "True",
      "lastName": "Panetta",
      "party": "D",
      "sponsorshipDate": "2026-01-15",
      "state": "CA"
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
      "sponsorshipDate": "2026-01-15",
      "state": "MI"
    },
    {
      "bioguideId": "M001206",
      "district": "25",
      "firstName": "Joseph",
      "fullName": "Rep. Morelle, Joseph D. [D-NY-25]",
      "isOriginalCosponsor": "True",
      "lastName": "Morelle",
      "middleName": "D.",
      "party": "D",
      "sponsorshipDate": "2026-01-15",
      "state": "NY"
    },
    {
      "bioguideId": "W000808",
      "district": "24",
      "firstName": "Frederica",
      "fullName": "Rep. Wilson, Frederica S. [D-FL-24]",
      "isOriginalCosponsor": "False",
      "lastName": "Wilson",
      "middleName": "S.",
      "party": "D",
      "sponsorshipDate": "2026-01-20",
      "state": "FL"
    },
    {
      "bioguideId": "H001081",
      "district": "5",
      "firstName": "Jahana",
      "fullName": "Rep. Hayes, Jahana [D-CT-5]",
      "isOriginalCosponsor": "False",
      "lastName": "Hayes",
      "party": "D",
      "sponsorshipDate": "2026-01-22",
      "state": "CT"
    },
    {
      "bioguideId": "T000487",
      "district": "2",
      "firstName": "Jill",
      "fullName": "Rep. Tokuda, Jill N. [D-HI-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Tokuda",
      "middleName": "N.",
      "party": "D",
      "sponsorshipDate": "2026-02-02",
      "state": "HI"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hres/BILLS-119hres1002ih.xml",
      "text": "IV\n119th CONGRESS\n2d Session\nH. RES. 1002\nIN THE HOUSE OF REPRESENTATIVES\nJanuary 15, 2026 Ms. Bonamici (for herself, Mr. Fitzpatrick , Ms. Wasserman Schultz , Mr. Kelly of Pennsylvania , Ms. Davids of Kansas , Ms. Lois Frankel of Florida , Ms. Schakowsky , Ms. Garcia of Texas , Mr. Cohen , Mrs. Dingell , Mr. Bishop , Ms. Norton , Mr. McGovern , Mr. Panetta , Ms. Stevens , and Mr. Morelle ) submitted the following resolution; which was referred to the Committee on Education and Workforce\nRESOLUTION\nRecognizing the value of the Older Americans Act of 1965 nutrition program in addressing hunger, malnutrition, and isolation, and improving the health and quality of life for millions of our Nations seniors each year.\nThat the House of Representatives\u2014\n**(1)**\nrecognizes and values the important work of local Older Americans Act of 1965 (OAA) nutrition programs nationwide in giving voice to millions of our Nation\u2019s seniors each year, improving their quality of life and addressing senior hunger, malnutrition, and isolation;\n**(2)**\nrecognizes and values the important role that local OAA nutrition programs and national organizations play in increasing awareness of the growing unmet need for these programs and in raising additional non-Federal funds and soliciting volunteers to support and assist the important missions of these programs;\n**(3)**\nrecognizes and values volunteers as the backbone of the OAA nutrition program, noting that they deliver nutritious meals to seniors and individuals with disabilities who are at significant risk of hunger, malnutrition, and isolation, and provide caring concern and attention to the welfare of program participants; and\n**(4)**\nencourages Members of Congress to support their local OAA nutrition programs by\u2014\n**(A)**\ndelivering meals to homebound seniors or serving them in a congregate setting with a program in their district or State; and\n**(B)**\nworking to secure sustained Federal funding for the OAA nutrition program that will allow local providers to keep pace with increased program costs and demand.",
      "versionDate": "2026-01-15",
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
        "name": "Social Welfare",
        "updateDate": "2026-01-20T14:40:46Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2026-01-15",
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
          "measure-id": "id119hres1002",
          "measure-number": "1002",
          "measure-type": "hres",
          "orig-publish-date": "2026-01-15",
          "originChamber": "HOUSE",
          "update-date": "2026-04-03"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hres1002v00",
            "update-date": "2026-04-03"
          },
          "action-date": "2026-01-15",
          "action-desc": "Introduced in House",
          "summary-text": "<p>This resolution recognizes the important role that local nutrition programs supported through the Older Americans Act of 1965 play in addressing senior hunger, malnutrition, and isolation.</p>"
        },
        "title": "Recognizing the value of the Older Americans Act of 1965 nutrition program in addressing hunger, malnutrition, and isolation, and improving the health and quality of life for millions of our Nations seniors each year."
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hres/BILLSUM-119hres1002.xml",
    "summary": {
      "actionDate": "2026-01-15",
      "actionDesc": "Introduced in House",
      "text": "<p>This resolution recognizes the important role that local nutrition programs supported through the Older Americans Act of 1965 play in addressing senior hunger, malnutrition, and isolation.</p>",
      "updateDate": "2026-04-03",
      "versionCode": "id119hres1002"
    },
    "title": "Recognizing the value of the Older Americans Act of 1965 nutrition program in addressing hunger, malnutrition, and isolation, and improving the health and quality of life for millions of our Nations seniors each year."
  },
  "summaries": [
    {
      "actionDate": "2026-01-15",
      "actionDesc": "Introduced in House",
      "text": "<p>This resolution recognizes the important role that local nutrition programs supported through the Older Americans Act of 1965 play in addressing senior hunger, malnutrition, and isolation.</p>",
      "updateDate": "2026-04-03",
      "versionCode": "id119hres1002"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2026-01-15",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hres/BILLS-119hres1002ih.xml"
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
      "title": "Recognizing the value of the Older Americans Act of 1965 nutrition program in addressing hunger, malnutrition, and isolation, and improving the health and quality of life for millions of our Nations seniors each year.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-01-16T09:18:41Z"
    },
    {
      "title": "Recognizing the value of the Older Americans Act of 1965 nutrition program in addressing hunger, malnutrition, and isolation, and improving the health and quality of life for millions of our Nations seniors each year.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-01-16T09:06:39Z"
    }
  ]
}
```
