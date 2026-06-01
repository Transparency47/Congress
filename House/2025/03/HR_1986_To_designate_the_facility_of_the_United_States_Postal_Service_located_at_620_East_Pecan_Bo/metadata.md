# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/1986?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/1986
- Title: To designate the facility of the United States Postal Service located at 620 East Pecan Boulevard in McAllen, Texas, as the "Agent Raul H. Gonzalez Jr. Memorial Post Office Building".
- Congress: 119
- Bill type: HR
- Bill number: 1986
- Origin chamber: House
- Introduced date: 2025-03-10
- Update date: 2026-05-12T08:06:00Z
- Update date including text: 2026-05-12T08:06:00Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, amendments, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-03-10: Introduced in House
- 2025-03-10 - IntroReferral: Introduced in House
- 2025-03-10 - IntroReferral: Introduced in House
- 2025-03-10 - IntroReferral: Referred to the House Committee on Oversight and Government Reform.
- Latest action: 2025-03-10: Introduced in House

## Actions

- 2025-03-10 - IntroReferral: Introduced in House
- 2025-03-10 - IntroReferral: Introduced in House
- 2025-03-10 - IntroReferral: Referred to the House Committee on Oversight and Government Reform.

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
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/1986",
    "number": "1986",
    "originChamber": "House",
    "policyArea": {
      "name": "Government Operations and Politics"
    },
    "sponsors": [
      {
        "bioguideId": "D000594",
        "district": "15",
        "firstName": "Monica",
        "fullName": "Rep. De La Cruz, Monica [R-TX-15]",
        "lastName": "De La Cruz",
        "party": "R",
        "state": "TX"
      }
    ],
    "title": "To designate the facility of the United States Postal Service located at 620 East Pecan Boulevard in McAllen, Texas, as the \"Agent Raul H. Gonzalez Jr. Memorial Post Office Building\".",
    "type": "HR",
    "updateDate": "2026-05-12T08:06:00Z",
    "updateDateIncludingText": "2026-05-12T08:06:00Z"
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
          "name": "Oversight and Government Reform Committee",
          "systemCode": "hsgo00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Oversight and Government Reform.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-03-10",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-03-10",
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

## API Data: amendments

```json
{
  "amendments": [
    {
      "amendment": {
        "actions": {
          "actions": {
            "item": [
              {
                "actionCode": "Intro-S",
                "actionDate": "2025-03-14",
                "sourceSystem": {
                  "code": "9",
                  "name": "Library of Congress"
                },
                "type": "IntroReferral"
              },
              {
                "actionCode": "91000",
                "actionDate": "2025-03-14",
                "sourceSystem": {
                  "code": "9",
                  "name": "Library of Congress"
                },
                "text": "Senate amendment submitted",
                "type": "Floor"
              }
            ]
          },
          "count": "2"
        },
        "amendedBill": {
          "congress": "119",
          "number": "1986",
          "originChamber": "House",
          "originChamberCode": "H",
          "title": "To designate the facility of the United States Postal Service located at 620 East Pecan Boulevard in McAllen, Texas, as the \"Agent Raul H. Gonzalez Jr. Memorial Post Office Building\".",
          "type": "HR",
          "updateDateIncludingText": "2026-05-12"
        },
        "chamber": "Senate",
        "congress": "119",
        "cosponsors": {
          "count": "5",
          "countIncludingWithdrawnCosponsors": "5",
          "item": [
            {
              "bioguideId": "H001076",
              "firstName": "Maggie",
              "fullName": "Sen. Hassan, Margaret Wood [D-NH]",
              "isOriginalCosponsor": "True",
              "lastName": "Hassan",
              "party": "D",
              "sponsorshipDate": "2025-03-14",
              "state": "NH"
            },
            {
              "bioguideId": "K000383",
              "firstName": "Angus",
              "fullName": "Sen. King, Angus S., Jr. [I-ME]",
              "isOriginalCosponsor": "True",
              "lastName": "King",
              "middleName": "S.",
              "party": "I",
              "sponsorshipDate": "2025-03-14",
              "state": "ME"
            },
            {
              "bioguideId": "K000384",
              "firstName": "Timothy",
              "fullName": "Sen. Kaine, Tim [D-VA]",
              "isOriginalCosponsor": "True",
              "lastName": "Kaine",
              "middleName": "M.",
              "party": "D",
              "sponsorshipDate": "2025-03-14",
              "state": "VA"
            },
            {
              "bioguideId": "H001042",
              "firstName": "Mazie",
              "fullName": "Sen. Hirono, Mazie K. [D-HI]",
              "isOriginalCosponsor": "True",
              "lastName": "Hirono",
              "middleName": "K.",
              "party": "D",
              "sponsorshipDate": "2025-03-14",
              "state": "HI"
            },
            {
              "bioguideId": "S001194",
              "firstName": "Brian",
              "fullName": "Sen. Schatz, Brian [D-HI]",
              "isOriginalCosponsor": "True",
              "lastName": "Schatz",
              "party": "D",
              "sponsorshipDate": "2025-03-14",
              "state": "HI"
            }
          ]
        },
        "number": "1286",
        "sponsors": {
          "item": {
            "bioguideId": "S001181",
            "firstName": "Jeanne",
            "fullName": "Sen. Shaheen, Jeanne [D-NH]",
            "lastName": "Shaheen",
            "party": "D",
            "state": "NH"
          }
        },
        "submittedDate": "2025-03-14T04:00:00Z",
        "textVersions": {
          "count": "1"
        },
        "type": "SAMDT",
        "updateDate": "2025-03-14T18:52:40Z"
      }
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
          "date": "2025-03-10T16:01:00Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Oversight and Government Reform Committee",
      "systemCode": "hsgo00",
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
      "bioguideId": "B001291",
      "district": "36",
      "firstName": "Brian",
      "fullName": "Rep. Babin, Brian [R-TX-36]",
      "isOriginalCosponsor": "True",
      "lastName": "Babin",
      "party": "R",
      "sponsorshipDate": "2025-03-10",
      "state": "TX"
    },
    {
      "bioguideId": "W000816",
      "district": "25",
      "firstName": "Roger",
      "fullName": "Rep. Williams, Roger [R-TX-25]",
      "isOriginalCosponsor": "True",
      "lastName": "Williams",
      "party": "R",
      "sponsorshipDate": "2025-03-10",
      "state": "TX"
    },
    {
      "bioguideId": "C001051",
      "district": "31",
      "firstName": "John",
      "fullName": "Rep. Carter, John R. [R-TX-31]",
      "isOriginalCosponsor": "True",
      "lastName": "Carter",
      "middleName": "R.",
      "party": "R",
      "sponsorshipDate": "2025-03-10",
      "state": "TX"
    },
    {
      "bioguideId": "M001157",
      "district": "10",
      "firstName": "Michael",
      "fullName": "Rep. McCaul, Michael T. [R-TX-10]",
      "isOriginalCosponsor": "True",
      "lastName": "McCaul",
      "middleName": "T.",
      "party": "R",
      "sponsorshipDate": "2025-03-10",
      "state": "TX"
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
      "bioguideId": "J000304",
      "district": "13",
      "firstName": "Ronny",
      "fullName": "Rep. Jackson, Ronny [R-TX-13]",
      "isOriginalCosponsor": "True",
      "lastName": "Jackson",
      "party": "R",
      "sponsorshipDate": "2025-03-10",
      "state": "TX"
    },
    {
      "bioguideId": "P000048",
      "district": "11",
      "firstName": "August",
      "fullName": "Rep. Pfluger, August [R-TX-11]",
      "isOriginalCosponsor": "True",
      "lastName": "Pfluger",
      "party": "R",
      "sponsorshipDate": "2025-03-10",
      "state": "TX"
    },
    {
      "bioguideId": "C001120",
      "district": "2",
      "firstName": "Dan",
      "fullName": "Rep. Crenshaw, Dan [R-TX-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Crenshaw",
      "party": "R",
      "sponsorshipDate": "2025-03-10",
      "state": "TX"
    },
    {
      "bioguideId": "V000134",
      "district": "24",
      "firstName": "Beth",
      "fullName": "Rep. Van Duyne, Beth [R-TX-24]",
      "isOriginalCosponsor": "True",
      "lastName": "Van Duyne",
      "party": "R",
      "sponsorshipDate": "2025-03-10",
      "state": "TX"
    },
    {
      "bioguideId": "M001224",
      "district": "1",
      "firstName": "Nathaniel",
      "fullName": "Rep. Moran, Nathaniel [R-TX-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Moran",
      "party": "R",
      "sponsorshipDate": "2025-03-10",
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
      "sponsorshipDate": "2025-03-10",
      "state": "TX"
    },
    {
      "bioguideId": "G000594",
      "district": "23",
      "firstName": "Tony",
      "fullName": "Rep. Gonzales, Tony [R-TX-23]",
      "isOriginalCosponsor": "True",
      "lastName": "Gonzales",
      "party": "R",
      "sponsorshipDate": "2025-03-10",
      "state": "TX"
    },
    {
      "bioguideId": "G000581",
      "district": "34",
      "firstName": "Vicente",
      "fullName": "Rep. Gonzalez, Vicente [D-TX-34]",
      "isOriginalCosponsor": "True",
      "lastName": "Gonzalez",
      "party": "D",
      "sponsorshipDate": "2025-03-10",
      "state": "TX"
    },
    {
      "bioguideId": "A000375",
      "district": "19",
      "firstName": "Jodey",
      "fullName": "Rep. Arrington, Jodey C. [R-TX-19]",
      "isOriginalCosponsor": "True",
      "lastName": "Arrington",
      "middleName": "C.",
      "party": "R",
      "sponsorshipDate": "2025-03-10",
      "state": "TX"
    },
    {
      "bioguideId": "N000026",
      "district": "22",
      "firstName": "Troy",
      "fullName": "Rep. Nehls, Troy E. [R-TX-22]",
      "isOriginalCosponsor": "True",
      "lastName": "Nehls",
      "middleName": "E.",
      "party": "R",
      "sponsorshipDate": "2025-03-10",
      "state": "TX"
    },
    {
      "bioguideId": "F000246",
      "district": "4",
      "firstName": "Pat",
      "fullName": "Rep. Fallon, Pat [R-TX-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Fallon",
      "party": "R",
      "sponsorshipDate": "2025-03-10",
      "state": "TX"
    },
    {
      "bioguideId": "S000250",
      "district": "17",
      "firstName": "Pete",
      "fullName": "Rep. Sessions, Pete [R-TX-17]",
      "isOriginalCosponsor": "True",
      "lastName": "Sessions",
      "party": "R",
      "sponsorshipDate": "2025-03-10",
      "state": "TX"
    },
    {
      "bioguideId": "C001063",
      "district": "28",
      "firstName": "Henry",
      "fullName": "Rep. Cuellar, Henry [D-TX-28]",
      "isOriginalCosponsor": "True",
      "lastName": "Cuellar",
      "party": "D",
      "sponsorshipDate": "2025-03-10",
      "state": "TX"
    },
    {
      "bioguideId": "G000603",
      "district": "26",
      "firstName": "Brandon",
      "fullName": "Rep. Gill, Brandon [R-TX-26]",
      "isOriginalCosponsor": "True",
      "lastName": "Gill",
      "party": "R",
      "sponsorshipDate": "2025-03-10",
      "state": "TX"
    },
    {
      "bioguideId": "C001115",
      "district": "27",
      "firstName": "Michael",
      "fullName": "Rep. Cloud, Michael [R-TX-27]",
      "isOriginalCosponsor": "True",
      "lastName": "Cloud",
      "party": "R",
      "sponsorshipDate": "2025-03-10",
      "state": "TX"
    },
    {
      "bioguideId": "C001091",
      "district": "20",
      "firstName": "Joaquin",
      "fullName": "Rep. Castro, Joaquin [D-TX-20]",
      "isOriginalCosponsor": "False",
      "lastName": "Castro",
      "party": "D",
      "sponsorshipDate": "2025-05-05",
      "state": "TX"
    },
    {
      "bioguideId": "M001237",
      "district": "8",
      "firstName": "Kristen",
      "fullName": "Rep. McDonald Rivet, Kristen [D-MI-8]",
      "isOriginalCosponsor": "False",
      "lastName": "McDonald Rivet",
      "party": "D",
      "sponsorshipDate": "2025-12-16",
      "state": "MI"
    },
    {
      "bioguideId": "L000603",
      "district": "8",
      "firstName": "Morgan",
      "fullName": "Rep. Luttrell, Morgan [R-TX-8]",
      "isOriginalCosponsor": "False",
      "lastName": "Luttrell",
      "party": "R",
      "sponsorshipDate": "2026-02-03",
      "state": "TX"
    },
    {
      "bioguideId": "G000601",
      "district": "12",
      "firstName": "Craig",
      "fullName": "Rep. Goldman, Craig A. [R-TX-12]",
      "isOriginalCosponsor": "False",
      "lastName": "Goldman",
      "middleName": "A.",
      "party": "R",
      "sponsorshipDate": "2026-04-16",
      "state": "TX"
    },
    {
      "bioguideId": "H001095",
      "district": "38",
      "firstName": "Wesley",
      "fullName": "Rep. Hunt, Wesley [R-TX-38]",
      "isOriginalCosponsor": "False",
      "lastName": "Hunt",
      "party": "R",
      "sponsorshipDate": "2026-04-20",
      "state": "TX"
    },
    {
      "bioguideId": "G000589",
      "district": "5",
      "firstName": "Lance",
      "fullName": "Rep. Gooden, Lance [R-TX-5]",
      "isOriginalCosponsor": "False",
      "lastName": "Gooden",
      "party": "R",
      "sponsorshipDate": "2026-05-11",
      "state": "TX"
    },
    {
      "bioguideId": "E000071",
      "district": "6",
      "firstName": "Jake",
      "fullName": "Rep. Ellzey, Jake [R-TX-6]",
      "isOriginalCosponsor": "False",
      "lastName": "Ellzey",
      "party": "R",
      "sponsorshipDate": "2026-05-11",
      "state": "TX"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1986ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 1986\nIN THE HOUSE OF REPRESENTATIVES\nMarch 10, 2025 Ms. De La Cruz (for herself, Mr. Babin , Mr. Williams of Texas , Mr. Carter of Texas , Mr. McCaul , Mr. Self , Mr. Jackson of Texas , Mr. Pfluger , Mr. Crenshaw , Ms. Van Duyne , Mr. Moran , Mr. Weber of Texas , Mr. Tony Gonzales of Texas , Mr. Vicente Gonzalez of Texas , Mr. Arrington , Mr. Nehls , Mr. Fallon , Mr. Sessions , Mr. Cuellar , Mr. Gill of Texas , and Mr. Cloud ) introduced the following bill; which was referred to the Committee on Oversight and Government Reform\nA BILL\nTo designate the facility of the United States Postal Service located at 620 East Pecan Boulevard in McAllen, Texas, as the Agent Raul H. Gonzalez Jr. Memorial Post Office Building .\n#### 1. Agent Raul H. Gonzalez Jr. Memorial Post Office Building\n##### (a) Designation\nThe facility of the United States Postal Service located at 620 East Pecan Boulevard in McAllen, Texas, shall be known and designated as the Agent Raul H. Gonzalez Jr. Memorial Post Office Building .\n##### (b) References\nAny reference in a law, map, regulation, document, paper, or other record of the United States to the facility referred to in subsection (a) shall be deemed to be a reference to the Agent Raul H. Gonzalez Jr. Memorial Post Office Building .",
      "versionDate": "2025-03-10",
      "versionType": "Introduced in House"
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
        "actionDate": "2025-03-10",
        "text": "Read twice and referred to the Committee on Homeland Security and Governmental Affairs."
      },
      "number": "917",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "A bill to designate the facility of the United States Postal Service located at 620 East Pecan Boulevard in McAllen, Texas, as the \"Agent Raul H. Gonzalez Jr. Memorial Post Office\".",
      "type": "S"
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
            "name": "Congressional tributes",
            "updateDate": "2025-08-13T13:42:42Z"
          },
          {
            "name": "Government buildings, facilities, and property",
            "updateDate": "2025-08-13T13:42:42Z"
          },
          {
            "name": "Postal service",
            "updateDate": "2025-08-13T13:42:42Z"
          },
          {
            "name": "Texas",
            "updateDate": "2025-08-13T13:42:45Z"
          }
        ]
      },
      "policyArea": {
        "name": "Government Operations and Politics",
        "updateDate": "2025-03-31T18:54:59Z"
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
          "measure-id": "id119hr1986",
          "measure-number": "1986",
          "measure-type": "hr",
          "orig-publish-date": "2025-03-10",
          "originChamber": "HOUSE",
          "update-date": "2025-08-01"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr1986v00",
            "update-date": "2025-08-01"
          },
          "action-date": "2025-03-10",
          "action-desc": "Introduced in House",
          "summary-text": "This bill designates the facility of the United States Postal Service located at 620 East Pecan Boulevard in McAllen, Texas, as the \"Agent Raul H. Gonzalez Jr. Memorial Post Office Building\"."
        },
        "title": "To designate the facility of the United States Postal Service located at 620 East Pecan Boulevard in McAllen, Texas, as the \"Agent Raul H. Gonzalez Jr. Memorial Post Office Building\"."
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr1986.xml",
    "summary": {
      "actionDate": "2025-03-10",
      "actionDesc": "Introduced in House",
      "text": "This bill designates the facility of the United States Postal Service located at 620 East Pecan Boulevard in McAllen, Texas, as the \"Agent Raul H. Gonzalez Jr. Memorial Post Office Building\".",
      "updateDate": "2025-08-01",
      "versionCode": "id119hr1986"
    },
    "title": "To designate the facility of the United States Postal Service located at 620 East Pecan Boulevard in McAllen, Texas, as the \"Agent Raul H. Gonzalez Jr. Memorial Post Office Building\"."
  },
  "summaries": [
    {
      "actionDate": "2025-03-10",
      "actionDesc": "Introduced in House",
      "text": "This bill designates the facility of the United States Postal Service located at 620 East Pecan Boulevard in McAllen, Texas, as the \"Agent Raul H. Gonzalez Jr. Memorial Post Office Building\".",
      "updateDate": "2025-08-01",
      "versionCode": "id119hr1986"
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
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1986ih.xml"
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
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To designate the facility of the United States Postal Service located at 620 East Pecan Boulevard in McAllen, Texas, as the \"Agent Raul H. Gonzalez Jr. Memorial Post Office Building\".",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-26T02:03:56Z"
    },
    {
      "title": "To designate the facility of the United States Postal Service located at 620 East Pecan Boulevard in McAllen, Texas, as the \"Agent Raul H. Gonzalez Jr. Memorial Post Office Building\".",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-03-11T08:05:44Z"
    }
  ]
}
```
