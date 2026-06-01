# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/718?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/718
- Title: Public Lands in Public Hands Act
- Congress: 119
- Bill type: HR
- Bill number: 718
- Origin chamber: House
- Introduced date: 2025-01-23
- Update date: 2026-04-21T08:06:06Z
- Update date including text: 2026-04-21T08:06:06Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-01-23: Introduced in House
- 2025-01-23 - IntroReferral: Introduced in House
- 2025-01-23 - IntroReferral: Introduced in House
- 2025-01-23 - IntroReferral: Referred to the Committee on Natural Resources, and in addition to the Committee on Agriculture, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-01-23 - IntroReferral: Referred to the Committee on Natural Resources, and in addition to the Committee on Agriculture, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-02-28 - Committee: Referred to the Subcommittee on Forestry and Horticulture.
- Latest action: 2025-01-23: Introduced in House

## Actions

- 2025-01-23 - IntroReferral: Introduced in House
- 2025-01-23 - IntroReferral: Introduced in House
- 2025-01-23 - IntroReferral: Referred to the Committee on Natural Resources, and in addition to the Committee on Agriculture, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-01-23 - IntroReferral: Referred to the Committee on Natural Resources, and in addition to the Committee on Agriculture, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-02-28 - Committee: Referred to the Subcommittee on Forestry and Horticulture.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-01-23",
    "latestAction": {
      "actionDate": "2025-01-23",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/718",
    "number": "718",
    "originChamber": "House",
    "policyArea": {
      "name": "Public Lands and Natural Resources"
    },
    "sponsors": [
      {
        "bioguideId": "Z000018",
        "district": "1",
        "firstName": "Ryan",
        "fullName": "Rep. Zinke, Ryan K. [R-MT-1]",
        "lastName": "Zinke",
        "party": "R",
        "state": "MT"
      }
    ],
    "title": "Public Lands in Public Hands Act",
    "type": "HR",
    "updateDate": "2026-04-21T08:06:06Z",
    "updateDateIncludingText": "2026-04-21T08:06:06Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-02-28",
      "committees": {
        "item": {
          "name": "Forestry and Horticulture Subcommittee",
          "systemCode": "hsag15"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Referred to the Subcommittee on Forestry and Horticulture.",
      "type": "Committee"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-01-23",
      "committees": {
        "item": {
          "name": "Agriculture Committee",
          "systemCode": "hsag00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the Committee on Natural Resources, and in addition to the Committee on Agriculture, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-01-23",
      "committees": {
        "item": {
          "name": "Natural Resources Committee",
          "systemCode": "hsii00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the Committee on Natural Resources, and in addition to the Committee on Agriculture, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-01-23",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-01-23",
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
          "date": "2025-01-23T15:02:15Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Agriculture Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": {
              "date": "2025-02-28T17:14:33Z",
              "name": "Referred to"
            }
          },
          "name": "Forestry and Horticulture Subcommittee",
          "systemCode": "hsag15"
        }
      },
      "systemCode": "hsag00",
      "type": "Standing"
    },
    {
      "activities": {
        "item": {
          "date": "2025-01-23T15:02:10Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Natural Resources Committee",
      "systemCode": "hsii00",
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
      "bioguideId": "V000136",
      "district": "2",
      "firstName": "Gabe",
      "fullName": "Rep. Vasquez, Gabe [D-NM-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Vasquez",
      "party": "D",
      "sponsorshipDate": "2025-01-23",
      "state": "NM"
    },
    {
      "bioguideId": "S001148",
      "district": "2",
      "firstName": "Michael",
      "fullName": "Rep. Simpson, Michael K. [R-ID-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Simpson",
      "middleName": "K.",
      "party": "R",
      "sponsorshipDate": "2025-04-08",
      "state": "ID"
    },
    {
      "bioguideId": "D000634",
      "district": "2",
      "firstName": "Troy",
      "fullName": "Rep. Downing, Troy [R-MT-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Downing",
      "party": "R",
      "sponsorshipDate": "2025-04-08",
      "state": "MT"
    },
    {
      "bioguideId": "B001326",
      "district": "5",
      "firstName": "Janelle",
      "fullName": "Rep. Bynum, Janelle S. [D-OR-5]",
      "isOriginalCosponsor": "False",
      "lastName": "Bynum",
      "middleName": "S.",
      "party": "D",
      "sponsorshipDate": "2025-06-03",
      "state": "OR"
    },
    {
      "bioguideId": "K000397",
      "district": "40",
      "firstName": "Young",
      "fullName": "Rep. Kim, Young [R-CA-40]",
      "isOriginalCosponsor": "False",
      "lastName": "Kim",
      "party": "R",
      "sponsorshipDate": "2025-06-27",
      "state": "CA"
    },
    {
      "bioguideId": "G000604",
      "district": "2",
      "firstName": "Maggie",
      "fullName": "Rep. Goodlander, Maggie [D-NH-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Goodlander",
      "party": "D",
      "sponsorshipDate": "2025-07-10",
      "state": "NH"
    },
    {
      "bioguideId": "S001216",
      "district": "8",
      "firstName": "Kim",
      "fullName": "Rep. Schrier, Kim [D-WA-8]",
      "isOriginalCosponsor": "False",
      "lastName": "Schrier",
      "party": "D",
      "sponsorshipDate": "2025-07-17",
      "state": "WA"
    },
    {
      "bioguideId": "K000398",
      "district": "7",
      "firstName": "Thomas",
      "fullName": "Rep. Kean, Thomas H. [R-NJ-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Kean",
      "middleName": "H.",
      "party": "R",
      "sponsorshipDate": "2025-07-29",
      "state": "NJ"
    },
    {
      "bioguideId": "V000138",
      "district": "7",
      "firstName": "Eugene",
      "fullName": "Rep. Vindman, Eugene Simon [D-VA-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Vindman",
      "middleName": "Simon",
      "party": "D",
      "sponsorshipDate": "2025-09-09",
      "state": "VA"
    },
    {
      "bioguideId": "C001133",
      "district": "6",
      "firstName": "Juan",
      "fullName": "Rep. Ciscomani, Juan [R-AZ-6]",
      "isOriginalCosponsor": "False",
      "lastName": "Ciscomani",
      "party": "R",
      "sponsorshipDate": "2025-09-15",
      "state": "AZ"
    },
    {
      "bioguideId": "N000191",
      "district": "2",
      "firstName": "Joe",
      "fullName": "Rep. Neguse, Joe [D-CO-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Neguse",
      "party": "D",
      "sponsorshipDate": "2025-12-16",
      "state": "CO"
    },
    {
      "bioguideId": "W000822",
      "district": "12",
      "firstName": "Bonnie",
      "fullName": "Rep. Watson Coleman, Bonnie [D-NJ-12]",
      "isOriginalCosponsor": "False",
      "lastName": "Watson Coleman",
      "party": "D",
      "sponsorshipDate": "2026-01-07",
      "state": "NJ"
    },
    {
      "bioguideId": "D000624",
      "district": "6",
      "firstName": "Debbie",
      "fullName": "Rep. Dingell, Debbie [D-MI-6]",
      "isOriginalCosponsor": "False",
      "lastName": "Dingell",
      "party": "D",
      "sponsorshipDate": "2026-01-30",
      "state": "MI"
    },
    {
      "bioguideId": "H001094",
      "district": "4",
      "firstName": "Val",
      "fullName": "Rep. Hoyle, Val T. [D-OR-4]",
      "isOriginalCosponsor": "False",
      "lastName": "Hoyle",
      "middleName": "T.",
      "party": "D",
      "sponsorshipDate": "2026-02-04",
      "state": "OR"
    },
    {
      "bioguideId": "S001211",
      "district": "4",
      "firstName": "Greg",
      "fullName": "Rep. Stanton, Greg [D-AZ-4]",
      "isOriginalCosponsor": "False",
      "lastName": "Stanton",
      "party": "D",
      "sponsorshipDate": "2026-02-24",
      "state": "AZ"
    },
    {
      "bioguideId": "K000401",
      "district": "3",
      "firstName": "Kevin",
      "fullName": "Rep. Kiley, Kevin [I-CA-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Kiley",
      "party": "I",
      "sponsorshipDate": "2026-04-16",
      "state": "CA"
    },
    {
      "bioguideId": "P000613",
      "district": "19",
      "firstName": "Jimmy",
      "fullName": "Rep. Panetta, Jimmy [D-CA-19]",
      "isOriginalCosponsor": "False",
      "lastName": "Panetta",
      "party": "D",
      "sponsorshipDate": "2026-04-20",
      "state": "CA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr718ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 718\nIN THE HOUSE OF REPRESENTATIVES\nJanuary 23, 2025 Mr. Zinke (for himself and Mr. Vasquez ) introduced the following bill; which was referred to the Committee on Natural Resources , and in addition to the Committee on Agriculture , for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned\nA BILL\nTo prohibit the Secretary of the Interior and the Secretary of Agriculture from transferring certain Federal land, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Public Lands in Public Hands Act .\n#### 2. Definitions\nIn this Act, the term publicly accessible tract means a tract of Federal land managed by the Secretary of the Interior or the Chief of the Forest Service that can be accessed by public road, public trail, public waterway, public easement, or public right-of-way.\n#### 3. Restriction on transfer of certain Federal land\n##### (a) In general\nThe Secretary of the Interior and the Secretary of Agriculture are prohibited from transferring title to Federal land to a non-Federal entity, if the Federal land is\u2014\n**(1)**\na publicly accessible tract; or\n**(2)**\ncontiguous with\u2014\n**(A)**\na publicly accessible tract; or\n**(B)**\na tract of land that\u2014\n**(i)**\nis owned by a State, county, or municipal government; and\n**(ii)**\ncan be accessed by public road, public trail, public waterway, public easement, or public right-of-way.\n##### (b) Exception\nSubsection (a) shall not apply to a transfer\u2014\n**(1)**\nof Federal land that is\u2014\n**(A)**\n**(i)**\nless than 300 acres; or\n**(ii)**\nless than 5 acres and accessible via a public waterway; and\n**(B)**\nauthorized to be transferred under and subject to the Federal Land Policy and Management Act of 1976;\n**(2)**\nauthorized by\u2014\n**(A)**\nthe Southern Nevada Public Land Management Act of 1998;\n**(B)**\nthe Sisk Act ( 16 U.S.C. 479a );\n**(C)**\nPublic Law 85\u2013569, commonly known as the Townsites Act of 1958 ;\n**(D)**\nthe Small Tract Act of 1983;\n**(E)**\nthe Act of May 17, 1906, commonly known as the Native Allotment Act of 1906 ;\n**(F)**\nPublic Law 85\u2013508, commonly known as the Alaska Statehood Act of 1959 ;\n**(G)**\nthe Alaska Native Claims Settlement Act;\n**(H)**\nthe Alaska Native Vietnam-era Veterans Land Allotment Program authorized by section 1119 of the John D. Dingell, Jr. Conservation, Management, and Recreation Act;\n**(I)**\nthe Recreation and Public Purposes Act; or\n**(J)**\nthe Weeks Act of 1911;\n**(3)**\nexplicitly authorized by Federal law; or\n**(4)**\ncompleted through a land exchange authorized by Federal law.\n##### (c) Limitation\nThe Secretary shall not subdivide Federal land to meet acreage minimums described in subsection (b)(1).\n#### 4. Statutory construction\nNothing in this Act shall be used to influence or interpret the legality of stepping over a property corner from one parcel of public land to another.",
      "versionDate": "2025-01-23",
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
            "name": "Intergovernmental relations",
            "updateDate": "2025-03-25T17:25:33Z"
          },
          {
            "name": "Land transfers",
            "updateDate": "2025-03-25T17:25:26Z"
          }
        ]
      },
      "policyArea": {
        "name": "Public Lands and Natural Resources",
        "updateDate": "2025-02-27T21:11:12Z"
      }
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-01-23",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr718ih.xml"
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
      "title": "Public Lands in Public Hands Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-07-30T12:51:47Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Public Lands in Public Hands Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-02-22T06:23:19Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To prohibit the Secretary of the Interior and the Secretary of Agriculture from transferring certain Federal land, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-02-22T06:18:30Z"
    }
  ]
}
```
