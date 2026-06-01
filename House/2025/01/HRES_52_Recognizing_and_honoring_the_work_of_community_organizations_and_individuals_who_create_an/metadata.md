# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hres/52?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/hres/52
- Title: Recognizing and honoring the work of community organizations and individuals who create and maintain services and educational programs for marginalized groups ensuring the resilience and prosperity of members of the LGBTQIA+ community.
- Congress: 119
- Bill type: HRES
- Bill number: 52
- Origin chamber: House
- Introduced date: 2025-01-16
- Update date: 2025-02-11T09:00:16Z
- Update date including text: 2025-02-11T09:00:16Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-01-16: Introduced in House
- 2025-01-16 - IntroReferral: Referred to the House Committee on the Judiciary.
- 2025-01-16 - Committee: Submitted in House
- 2025-01-16 - IntroReferral: Submitted in House
- Latest action: 2025-01-16: Submitted in House

## Actions

- 2025-01-16 - IntroReferral: Referred to the House Committee on the Judiciary.
- 2025-01-16 - Committee: Submitted in House
- 2025-01-16 - IntroReferral: Submitted in House

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-01-16",
    "latestAction": {
      "actionDate": "2025-01-16",
      "text": "Submitted in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/hres/52",
    "number": "52",
    "originChamber": "House",
    "policyArea": {
      "name": "Civil Rights and Liberties, Minority Issues"
    },
    "sponsors": [
      {
        "bioguideId": "W000822",
        "district": "12",
        "firstName": "Bonnie",
        "fullName": "Rep. Watson Coleman, Bonnie [D-NJ-12]",
        "lastName": "Watson Coleman",
        "party": "D",
        "state": "NJ"
      }
    ],
    "title": "Recognizing and honoring the work of community organizations and individuals who create and maintain services and educational programs for marginalized groups ensuring the resilience and prosperity of members of the LGBTQIA+ community.",
    "type": "HRES",
    "updateDate": "2025-02-11T09:00:16Z",
    "updateDateIncludingText": "2025-02-11T09:00:16Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-01-16",
      "committees": {
        "item": {
          "name": "Judiciary Committee",
          "systemCode": "hsju00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on the Judiciary.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "H12100",
      "actionDate": "2025-01-16",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Submitted in House",
      "type": "Committee"
    },
    {
      "actionCode": "1025",
      "actionDate": "2025-01-16",
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
          "date": "2025-01-16T14:05:35Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Judiciary Committee",
      "systemCode": "hsju00",
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
      "bioguideId": "T000481",
      "district": "12",
      "firstName": "Rashida",
      "fullName": "Rep. Tlaib, Rashida [D-MI-12]",
      "isOriginalCosponsor": "True",
      "lastName": "Tlaib",
      "party": "D",
      "sponsorshipDate": "2025-01-16",
      "state": "MI"
    },
    {
      "bioguideId": "E000297",
      "district": "13",
      "firstName": "Adriano",
      "fullName": "Rep. Espaillat, Adriano [D-NY-13]",
      "isOriginalCosponsor": "True",
      "lastName": "Espaillat",
      "party": "D",
      "sponsorshipDate": "2025-01-16",
      "state": "NY"
    },
    {
      "bioguideId": "V000081",
      "district": "7",
      "firstName": "Nydia",
      "fullName": "Rep. Vel\u00e1zquez, Nydia M. [D-NY-7]",
      "isOriginalCosponsor": "True",
      "lastName": "Vel\u00e1zquez",
      "middleName": "M.",
      "party": "D",
      "sponsorshipDate": "2025-01-16",
      "state": "NY"
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
      "sponsorshipDate": "2025-01-16",
      "state": "DC"
    },
    {
      "bioguideId": "M001229",
      "district": "10",
      "firstName": "LaMonica",
      "fullName": "Rep. McIver, LaMonica [D-NJ-10]",
      "isOriginalCosponsor": "True",
      "lastName": "McIver",
      "party": "D",
      "sponsorshipDate": "2025-01-16",
      "state": "NJ"
    },
    {
      "bioguideId": "Q000023",
      "district": "5",
      "firstName": "Mike",
      "fullName": "Rep. Quigley, Mike [D-IL-5]",
      "isOriginalCosponsor": "True",
      "lastName": "Quigley",
      "party": "D",
      "sponsorshipDate": "2025-01-16",
      "state": "IL"
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
      "sponsorshipDate": "2025-01-16",
      "state": "GA"
    },
    {
      "bioguideId": "M001225",
      "district": "15",
      "firstName": "Kevin",
      "fullName": "Rep. Mullin, Kevin [D-CA-15]",
      "isOriginalCosponsor": "True",
      "lastName": "Mullin",
      "party": "D",
      "sponsorshipDate": "2025-01-16",
      "state": "CA"
    },
    {
      "bioguideId": "T000468",
      "district": "1",
      "firstName": "Dina",
      "fullName": "Rep. Titus, Dina [D-NV-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Titus",
      "party": "D",
      "sponsorshipDate": "2025-01-16",
      "state": "NV"
    },
    {
      "bioguideId": "E000296",
      "district": "3",
      "firstName": "Dwight",
      "fullName": "Rep. Evans, Dwight [D-PA-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Evans",
      "party": "D",
      "sponsorshipDate": "2025-01-16",
      "state": "PA"
    },
    {
      "bioguideId": "S001185",
      "district": "7",
      "firstName": "Terri",
      "fullName": "Rep. Sewell, Terri A. [D-AL-7]",
      "isOriginalCosponsor": "True",
      "lastName": "Sewell",
      "middleName": "A.",
      "party": "D",
      "sponsorshipDate": "2025-01-16",
      "state": "AL"
    },
    {
      "bioguideId": "H001081",
      "district": "5",
      "firstName": "Jahana",
      "fullName": "Rep. Hayes, Jahana [D-CT-5]",
      "isOriginalCosponsor": "True",
      "lastName": "Hayes",
      "party": "D",
      "sponsorshipDate": "2025-01-16",
      "state": "CT"
    },
    {
      "bioguideId": "M001217",
      "district": "23",
      "firstName": "Jared",
      "fullName": "Rep. Moskowitz, Jared [D-FL-23]",
      "isOriginalCosponsor": "True",
      "lastName": "Moskowitz",
      "party": "D",
      "sponsorshipDate": "2025-01-16",
      "state": "FL"
    },
    {
      "bioguideId": "G000583",
      "district": "5",
      "firstName": "Josh",
      "fullName": "Rep. Gottheimer, Josh [D-NJ-5]",
      "isOriginalCosponsor": "True",
      "lastName": "Gottheimer",
      "party": "D",
      "sponsorshipDate": "2025-01-16",
      "state": "NJ"
    },
    {
      "bioguideId": "K000391",
      "district": "8",
      "firstName": "Raja",
      "fullName": "Rep. Krishnamoorthi, Raja [D-IL-8]",
      "isOriginalCosponsor": "True",
      "lastName": "Krishnamoorthi",
      "party": "D",
      "sponsorshipDate": "2025-01-16",
      "state": "IL"
    },
    {
      "bioguideId": "D000399",
      "district": "37",
      "firstName": "Lloyd",
      "fullName": "Rep. Doggett, Lloyd [D-TX-37]",
      "isOriginalCosponsor": "True",
      "lastName": "Doggett",
      "party": "D",
      "sponsorshipDate": "2025-01-16",
      "state": "TX"
    },
    {
      "bioguideId": "R000617",
      "district": "3",
      "firstName": "Delia",
      "fullName": "Rep. Ramirez, Delia C. [D-IL-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Ramirez",
      "middleName": "C.",
      "party": "D",
      "sponsorshipDate": "2025-01-16",
      "state": "IL"
    },
    {
      "bioguideId": "P000034",
      "district": "6",
      "firstName": "Frank",
      "fullName": "Rep. Pallone, Frank [D-NJ-6]",
      "isOriginalCosponsor": "True",
      "lastName": "Pallone",
      "party": "D",
      "sponsorshipDate": "2025-01-16",
      "state": "NJ"
    },
    {
      "bioguideId": "S001193",
      "district": "14",
      "firstName": "Eric",
      "fullName": "Rep. Swalwell, Eric [D-CA-14]",
      "isOriginalCosponsor": "True",
      "lastName": "Swalwell",
      "party": "D",
      "sponsorshipDate": "2025-01-16",
      "state": "CA"
    },
    {
      "bioguideId": "C001072",
      "district": "7",
      "firstName": "Andr\u00e9",
      "fullName": "Rep. Carson, Andr\u00e9 [D-IN-7]",
      "isOriginalCosponsor": "True",
      "lastName": "Carson",
      "party": "D",
      "sponsorshipDate": "2025-01-16",
      "state": "IN"
    },
    {
      "bioguideId": "F000477",
      "district": "4",
      "firstName": "Valerie",
      "fullName": "Rep. Foushee, Valerie P. [D-NC-4]",
      "isOriginalCosponsor": "False",
      "lastName": "Foushee",
      "middleName": "P.",
      "party": "D",
      "sponsorshipDate": "2025-01-21",
      "state": "NC"
    },
    {
      "bioguideId": "O000176",
      "district": "2",
      "firstName": "Johnny",
      "fullName": "Rep. Olszewski, Johnny [D-MD-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Olszewski",
      "party": "D",
      "sponsorshipDate": "2025-01-21",
      "state": "MD"
    },
    {
      "bioguideId": "R000621",
      "district": "6",
      "firstName": "Emily",
      "fullName": "Rep. Randall, Emily [D-WA-6]",
      "isOriginalCosponsor": "False",
      "lastName": "Randall",
      "party": "D",
      "sponsorshipDate": "2025-01-22",
      "state": "WA"
    },
    {
      "bioguideId": "G000551",
      "district": "7",
      "firstName": "Ra\u00fal",
      "fullName": "Rep. Grijalva, Ra\u00fal M. [D-AZ-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Grijalva",
      "middleName": "M.",
      "party": "D",
      "sponsorshipDate": "2025-01-23",
      "state": "AZ"
    },
    {
      "bioguideId": "G000586",
      "district": "4",
      "firstName": "Jes\u00fas",
      "fullName": "Rep. Garc\u00eda, Jes\u00fas G. \"Chuy\" [D-IL-4]",
      "isOriginalCosponsor": "False",
      "lastName": "Garc\u00eda",
      "middleName": "G. \"Chuy\"",
      "party": "D",
      "sponsorshipDate": "2025-01-23",
      "state": "IL"
    },
    {
      "bioguideId": "C001080",
      "district": "28",
      "firstName": "Judy",
      "fullName": "Rep. Chu, Judy [D-CA-28]",
      "isOriginalCosponsor": "False",
      "lastName": "Chu",
      "party": "D",
      "sponsorshipDate": "2025-02-06",
      "state": "CA"
    },
    {
      "bioguideId": "M001223",
      "district": "2",
      "firstName": "Seth",
      "fullName": "Rep. Magaziner, Seth [D-RI-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Magaziner",
      "party": "D",
      "sponsorshipDate": "2025-02-10",
      "state": "RI"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hres/BILLS-119hres52ih.xml",
      "text": "IV\n119th CONGRESS\n1st Session\nH. RES. 52\nIN THE HOUSE OF REPRESENTATIVES\nJanuary 16, 2025 Mrs. Watson Coleman (for herself, Ms. Tlaib , Mr. Espaillat , Ms. Vel\u00e1zquez , Ms. Norton , Mrs. McIver , Mr. Quigley , Mr. Johnson of Georgia , Mr. Mullin , Ms. Titus , Mr. Evans of Pennsylvania , Ms. Sewell , Mrs. Hayes , Mr. Moskowitz , Mr. Gottheimer , Mr. Krishnamoorthi , Mr. Doggett , Mrs. Ramirez , Mr. Pallone , Mr. Swalwell , and Mr. Carson ) submitted the following resolution; which was referred to the Committee on the Judiciary\nRESOLUTION\nRecognizing and honoring the work of community organizations and individuals who create and maintain services and educational programs for marginalized groups ensuring the resilience and prosperity of members of the LGBTQIA+ community.\nThat the House of Representatives\u2014\n**(1)**\nrecognizes the necessity and work of those who create LGBTQIA+ community spaces with the goals of equality;\n**(2)**\ncommends those who foster community partnerships between marginalized groups and local resources;\n**(3)**\nacknowledges the historical importance of community-building spaces in the intersectional fight against homophobic, racist, misogynistic, and hateful oppression;\n**(4)**\nhonors current and past organizations and individuals dedicated to providing marginalized groups, like the LGBTQIA+ community and people of color, with space to commune and organize;\n**(5)**\naffirms the importance of education and awareness initiatives that highlight the historical and cultural significance of LGBTQIA+ community spaces; and\n**(6)**\nencourages continued support by Congress for community organizations and individuals who continue to create community for marginalized groups.",
      "versionDate": "2025-01-16",
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
            "name": "Community life and organization",
            "updateDate": "2025-01-22T14:47:03Z"
          },
          {
            "name": "Congressional tributes",
            "updateDate": "2025-01-22T14:46:56Z"
          },
          {
            "name": "Sex, gender, sexual orientation discrimination",
            "updateDate": "2025-01-22T14:46:40Z"
          },
          {
            "name": "Social work, volunteer service, charitable organizations",
            "updateDate": "2025-01-22T14:46:47Z"
          }
        ]
      },
      "policyArea": {
        "name": "Civil Rights and Liberties, Minority Issues",
        "updateDate": "2025-01-21T13:13:55Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-01-16",
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
          "measure-id": "id119hres52",
          "measure-number": "52",
          "measure-type": "hres",
          "orig-publish-date": "2025-01-16",
          "originChamber": "HOUSE",
          "update-date": "2025-02-03"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hres52v00",
            "update-date": "2025-02-03"
          },
          "action-date": "2025-01-16",
          "action-desc": "Introduced in House",
          "summary-text": "<p>This resolution recognizes the necessity and work of those who create LGBTQIA+ community spaces with the goals of equality and commends those who foster community partnerships between marginalized groups and local resources.</p>"
        },
        "title": "Recognizing and honoring the work of community organizations and individuals who create and maintain services and educational programs for marginalized groups ensuring the resilience and prosperity of members of the LGBTQIA+ community."
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hres/BILLSUM-119hres52.xml",
    "summary": {
      "actionDate": "2025-01-16",
      "actionDesc": "Introduced in House",
      "text": "<p>This resolution recognizes the necessity and work of those who create LGBTQIA+ community spaces with the goals of equality and commends those who foster community partnerships between marginalized groups and local resources.</p>",
      "updateDate": "2025-02-03",
      "versionCode": "id119hres52"
    },
    "title": "Recognizing and honoring the work of community organizations and individuals who create and maintain services and educational programs for marginalized groups ensuring the resilience and prosperity of members of the LGBTQIA+ community."
  },
  "summaries": [
    {
      "actionDate": "2025-01-16",
      "actionDesc": "Introduced in House",
      "text": "<p>This resolution recognizes the necessity and work of those who create LGBTQIA+ community spaces with the goals of equality and commends those who foster community partnerships between marginalized groups and local resources.</p>",
      "updateDate": "2025-02-03",
      "versionCode": "id119hres52"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-01-16",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hres/BILLS-119hres52ih.xml"
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
      "title": "Recognizing and honoring the work of community organizations and individuals who create and maintain services and educational programs for marginalized groups ensuring the resilience and prosperity of members of the LGBTQIA+ community.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-01-17T09:18:24Z"
    },
    {
      "title": "Recognizing and honoring the work of community organizations and individuals who create and maintain services and educational programs for marginalized groups ensuring the resilience and prosperity of members of the LGBTQIA+ community.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-01-17T09:05:39Z"
    }
  ]
}
```
