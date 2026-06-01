# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hres/151?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-resolution/151
- Title: Expressing support for the designation of February 16, 2025, as "International Black Aviation Professionals Day".
- Congress: 119
- Bill type: HRES
- Bill number: 151
- Origin chamber: House
- Introduced date: 2025-02-21
- Update date: 2026-02-18T20:48:50Z
- Update date including text: 2026-02-18T20:48:50Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-02-21: Introduced in House
- 2025-02-21 - IntroReferral: Referred to the Committee on Transportation and Infrastructure, and in addition to the Committee on Education and Workforce, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-02-21 - IntroReferral: Referred to the Committee on Transportation and Infrastructure, and in addition to the Committee on Education and Workforce, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-02-21 - Committee: Referred to the Subcommittee on Aviation.
- Latest action: 2025-02-21: Referred to the Committee on Transportation and Infrastructure, and in addition to the Committee on Education and Workforce, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.

## Actions

- 2025-02-21 - IntroReferral: Referred to the Committee on Transportation and Infrastructure, and in addition to the Committee on Education and Workforce, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-02-21 - IntroReferral: Referred to the Committee on Transportation and Infrastructure, and in addition to the Committee on Education and Workforce, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-02-21 - Committee: Referred to the Subcommittee on Aviation.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-02-21",
    "latestAction": {
      "actionDate": "2025-02-21",
      "text": "Referred to the Committee on Transportation and Infrastructure, and in addition to the Committee on Education and Workforce, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned."
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-resolution/151",
    "number": "151",
    "originChamber": "House",
    "policyArea": {
      "name": "Transportation and Public Works"
    },
    "sponsors": [
      {
        "bioguideId": "W000788",
        "district": "5",
        "firstName": "Nikema",
        "fullName": "Rep. Williams, Nikema [D-GA-5]",
        "lastName": "Williams",
        "party": "D",
        "state": "GA"
      }
    ],
    "title": "Expressing support for the designation of February 16, 2025, as \"International Black Aviation Professionals Day\".",
    "type": "HRES",
    "updateDate": "2026-02-18T20:48:50Z",
    "updateDateIncludingText": "2026-02-18T20:48:50Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-02-21",
      "committees": {
        "item": {
          "name": "Aviation Subcommittee",
          "systemCode": "hspw05"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Referred to the Subcommittee on Aviation.",
      "type": "Committee"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-02-21",
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
      "text": "Referred to the Committee on Transportation and Infrastructure, and in addition to the Committee on Education and Workforce, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-02-21",
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
      "text": "Referred to the Committee on Transportation and Infrastructure, and in addition to the Committee on Education and Workforce, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
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
          "date": "2025-02-21T20:31:35Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Transportation and Infrastructure Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": {
              "date": "2025-02-21T22:21:59Z",
              "name": "Referred to"
            }
          },
          "name": "Aviation Subcommittee",
          "systemCode": "hspw05"
        }
      },
      "systemCode": "hspw00",
      "type": "Standing"
    },
    {
      "activities": {
        "item": {
          "date": "2025-02-21T20:31:40Z",
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
      "bioguideId": "M001208",
      "district": "6",
      "firstName": "Lucy",
      "fullName": "Rep. McBath, Lucy [D-GA-6]",
      "isOriginalCosponsor": "True",
      "lastName": "McBath",
      "party": "D",
      "sponsorshipDate": "2025-02-21",
      "state": "GA"
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
      "sponsorshipDate": "2025-02-21",
      "state": "GA"
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
      "sponsorshipDate": "2025-02-21",
      "state": "GA"
    },
    {
      "bioguideId": "A000370",
      "district": "12",
      "firstName": "Alma",
      "fullName": "Rep. Adams, Alma S. [D-NC-12]",
      "isOriginalCosponsor": "True",
      "lastName": "Adams",
      "middleName": "S.",
      "party": "D",
      "sponsorshipDate": "2025-02-21",
      "state": "NC"
    },
    {
      "bioguideId": "B001300",
      "district": "44",
      "firstName": "Nanette",
      "fullName": "Rep. Barrag\u00e1n, Nanette Diaz [D-CA-44]",
      "isOriginalCosponsor": "True",
      "lastName": "Barrag\u00e1n",
      "middleName": "Diaz",
      "party": "D",
      "sponsorshipDate": "2025-02-21",
      "state": "CA"
    },
    {
      "bioguideId": "B001315",
      "district": "13",
      "firstName": "Nikki",
      "fullName": "Rep. Budzinski, Nikki [D-IL-13]",
      "isOriginalCosponsor": "True",
      "lastName": "Budzinski",
      "party": "D",
      "sponsorshipDate": "2025-02-21",
      "state": "IL"
    },
    {
      "bioguideId": "B001326",
      "district": "5",
      "firstName": "Janelle",
      "fullName": "Rep. Bynum, Janelle [D-OR-5]",
      "isOriginalCosponsor": "True",
      "lastName": "Bynum",
      "middleName": "S.",
      "party": "D",
      "sponsorshipDate": "2025-02-21",
      "state": "OR"
    },
    {
      "bioguideId": "C001072",
      "district": "7",
      "firstName": "Andr\u00e9",
      "fullName": "Rep. Carson, Andr\u00e9 [D-IN-7]",
      "isOriginalCosponsor": "True",
      "lastName": "Carson",
      "party": "D",
      "sponsorshipDate": "2025-02-21",
      "state": "IN"
    },
    {
      "bioguideId": "D000629",
      "district": "3",
      "firstName": "Sharice",
      "fullName": "Rep. Davids, Sharice [D-KS-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Davids",
      "party": "D",
      "sponsorshipDate": "2025-02-21",
      "state": "KS"
    },
    {
      "bioguideId": "F000110",
      "district": "6",
      "firstName": "CLEO",
      "fullName": "Rep. Fields, Cleo [D-LA-6]",
      "isOriginalCosponsor": "True",
      "lastName": "FIELDS",
      "party": "D",
      "sponsorshipDate": "2025-02-21",
      "state": "LA"
    },
    {
      "bioguideId": "K000385",
      "district": "2",
      "firstName": "Robin",
      "fullName": "Rep. Kelly, Robin L. [D-IL-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Kelly",
      "middleName": "L.",
      "party": "D",
      "sponsorshipDate": "2025-02-21",
      "state": "IL"
    },
    {
      "bioguideId": "M001229",
      "district": "10",
      "firstName": "LaMonica",
      "fullName": "Rep. McIver, LaMonica [D-NJ-10]",
      "isOriginalCosponsor": "True",
      "lastName": "McIver",
      "party": "D",
      "sponsorshipDate": "2025-02-21",
      "state": "NJ"
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
      "sponsorshipDate": "2025-02-21",
      "state": "DC"
    },
    {
      "bioguideId": "P000610",
      "district": "0",
      "firstName": "Stacey",
      "fullName": "Del. Plaskett, Stacey E. [D-VI-At Large]",
      "isOriginalCosponsor": "True",
      "lastName": "Plaskett",
      "middleName": "E.",
      "party": "D",
      "sponsorshipDate": "2025-02-21",
      "state": "VI"
    },
    {
      "bioguideId": "S001159",
      "district": "10",
      "firstName": "Marilyn",
      "fullName": "Rep. Strickland, Marilyn [D-WA-10]",
      "isOriginalCosponsor": "True",
      "lastName": "Strickland",
      "party": "D",
      "sponsorshipDate": "2025-02-21",
      "state": "WA"
    },
    {
      "bioguideId": "T000468",
      "district": "1",
      "firstName": "Dina",
      "fullName": "Rep. Titus, Dina [D-NV-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Titus",
      "party": "D",
      "sponsorshipDate": "2025-02-21",
      "state": "NV"
    },
    {
      "bioguideId": "T000489",
      "district": "18",
      "firstName": "Sylvester",
      "fullName": "Rep. Turner, Sylvester [D-TX-18]",
      "isOriginalCosponsor": "True",
      "lastName": "Turner",
      "party": "D",
      "sponsorshipDate": "2025-02-21",
      "state": "TX"
    },
    {
      "bioguideId": "W000822",
      "district": "12",
      "firstName": "Bonnie",
      "fullName": "Rep. Watson Coleman, Bonnie [D-NJ-12]",
      "isOriginalCosponsor": "True",
      "lastName": "Watson Coleman",
      "party": "D",
      "sponsorshipDate": "2025-02-21",
      "state": "NJ"
    },
    {
      "bioguideId": "B001313",
      "district": "11",
      "firstName": "Shontel",
      "fullName": "Rep. Brown, Shontel M. [D-OH-11]",
      "isOriginalCosponsor": "False",
      "lastName": "Brown",
      "middleName": "M.",
      "party": "D",
      "sponsorshipDate": "2025-03-14",
      "state": "OH"
    },
    {
      "bioguideId": "S000510",
      "district": "9",
      "firstName": "Adam",
      "fullName": "Rep. Smith, Adam [D-WA-9]",
      "isOriginalCosponsor": "False",
      "lastName": "Smith",
      "party": "D",
      "sponsorshipDate": "2025-03-14",
      "state": "WA"
    },
    {
      "bioguideId": "C001068",
      "district": "9",
      "firstName": "Steve",
      "fullName": "Rep. Cohen, Steve [D-TN-9]",
      "isOriginalCosponsor": "False",
      "lastName": "Cohen",
      "party": "D",
      "sponsorshipDate": "2025-03-14",
      "state": "TN"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hres/BILLS-119hres151ih.xml",
      "text": "IV\n119th CONGRESS\n1st Session\nH. RES. 151\nIN THE HOUSE OF REPRESENTATIVES\nFebruary 21, 2025 Ms. Williams of Georgia (for herself, Mrs. McBath , Mr. Bishop , Mr. Johnson of Georgia , Ms. Adams , Ms. Barrag\u00e1n , Ms. Budzinski , Ms. Bynum , Mr. Carson , Ms. Davids of Kansas , Mr. Fields , Ms. Kelly of Illinois , Mrs. McIver , Ms. Norton , Ms. Plaskett , Ms. Strickland , Ms. Titus , Mr. Turner of Texas , and Mrs. Watson Coleman ) submitted the following resolution; which was referred to the Committee on Transportation and Infrastructure , and in addition to the Committee on Education and Workforce , for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned\nRESOLUTION\nExpressing support for the designation of February 16, 2025, as International Black Aviation Professionals Day .\nThat the House of Representatives\u2014\n**(1)**\nexpresses support for the designation of International Black Aviation Professionals Day ;\n**(2)**\nencourages the observation of International Black Aviation Professionals Day through recognition and celebration of the contributions of Black aviation professionals; and\n**(3)**\nrequests that the President issue a proclamation calling upon the people of the United States to\u2014\n**(A)**\nrecognize the stories and contributions of Black American aviation professionals who broke barriers, innovated, and took aviation to greater heights;\n**(B)**\nprovide enhanced curriculum in schools, libraries, and other places of learning to educate all people of the United States with respect to the contributions of Black aviation pioneers; and\n**(C)**\nsupport greater opportunities for Black Americans in all areas of aviation.",
      "versionDate": "2025-02-21",
      "versionType": "IH"
    }
  ]
}
```

## API Data: relatedbills

```json
{
  "relatedBills": [
    {
      "congress": "119",
      "latestAction": {
        "actionDate": "2026-02-12",
        "text": "Referred to the Committee on Transportation and Infrastructure, and in addition to the Committee on Education and Workforce, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned."
      },
      "number": "1064",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Expressing support for the designation of February 16, 2026, as \"International Black Aviation Professionals Day\".",
      "type": "HRES"
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
            "name": "Aviation and airports",
            "updateDate": "2025-04-16T17:47:47Z"
          },
          {
            "name": "Commemorative events and holidays",
            "updateDate": "2025-04-16T17:47:47Z"
          },
          {
            "name": "Congressional tributes",
            "updateDate": "2025-04-16T17:47:47Z"
          },
          {
            "name": "Racial and ethnic relations",
            "updateDate": "2025-04-16T17:47:47Z"
          }
        ]
      },
      "policyArea": {
        "name": "Transportation and Public Works",
        "updateDate": "2025-02-25T15:53:20Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-02-21",
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
          "measure-id": "id119hres151",
          "measure-number": "151",
          "measure-type": "hres",
          "orig-publish-date": "2025-02-21",
          "originChamber": "HOUSE",
          "update-date": "2025-02-25"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hres151v00",
            "update-date": "2025-02-25"
          },
          "action-date": "2025-02-21",
          "action-desc": "Introduced in House",
          "summary-text": "<p>This resolution expresses support for the designation of International Black Aviation Professionals Day. It also encourages the observation of the day through recognition and celebration of the contributions of Black aviation professionals.</p>"
        },
        "title": "Expressing support for the designation of February 16, 2025, as \"International Black Aviation Professionals Day\"."
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hres/BILLSUM-119hres151.xml",
    "summary": {
      "actionDate": "2025-02-21",
      "actionDesc": "Introduced in House",
      "text": "<p>This resolution expresses support for the designation of International Black Aviation Professionals Day. It also encourages the observation of the day through recognition and celebration of the contributions of Black aviation professionals.</p>",
      "updateDate": "2025-02-25",
      "versionCode": "id119hres151"
    },
    "title": "Expressing support for the designation of February 16, 2025, as \"International Black Aviation Professionals Day\"."
  },
  "summaries": [
    {
      "actionDate": "2025-02-21",
      "actionDesc": "Introduced in House",
      "text": "<p>This resolution expresses support for the designation of International Black Aviation Professionals Day. It also encourages the observation of the day through recognition and celebration of the contributions of Black aviation professionals.</p>",
      "updateDate": "2025-02-25",
      "versionCode": "id119hres151"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-02-21",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hres/BILLS-119hres151ih.xml"
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
      "title": "Expressing support for the designation of February 16, 2025, as \"International Black Aviation Professionals Day\".",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-02-22T09:48:40Z"
    },
    {
      "title": "Expressing support for the designation of February 16, 2025, as \"International Black Aviation Professionals Day\".",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-02-22T09:05:55Z"
    }
  ]
}
```
