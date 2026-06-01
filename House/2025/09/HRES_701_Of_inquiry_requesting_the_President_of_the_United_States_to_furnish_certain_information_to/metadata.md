# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hres/701?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-resolution/701
- Title: Of inquiry requesting the President of the United States to furnish certain information to the House of Representatives relating to the Department of Government Efficiency's access to and usage of NUMIDENT and other personally identifiable information in the possession of the Social Security Administration.
- Congress: 119
- Bill type: HRES
- Bill number: 701
- Origin chamber: House
- Introduced date: 2025-09-11
- Update date: 2025-09-23T18:23:05Z
- Update date including text: 2025-09-23T18:23:05Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-09-11: Introduced in House
- 2025-09-11 - IntroReferral: Referred to the House Committee on Ways and Means.
- 2025-09-11 - IntroReferral: Submitted in House
- 2025-09-11 - IntroReferral: Submitted in House
- Latest action: 2025-09-11: Submitted in House

## Actions

- 2025-09-11 - IntroReferral: Referred to the House Committee on Ways and Means.
- 2025-09-11 - IntroReferral: Submitted in House
- 2025-09-11 - IntroReferral: Submitted in House

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-09-11",
    "latestAction": {
      "actionDate": "2025-09-11",
      "text": "Submitted in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-resolution/701",
    "number": "701",
    "originChamber": "House",
    "policyArea": {
      "name": "Government Operations and Politics"
    },
    "sponsors": [
      {
        "bioguideId": "L000557",
        "district": "1",
        "firstName": "John",
        "fullName": "Rep. Larson, John B. [D-CT-1]",
        "lastName": "Larson",
        "party": "D",
        "state": "CT"
      }
    ],
    "title": "Of inquiry requesting the President of the United States to furnish certain information to the House of Representatives relating to the Department of Government Efficiency's access to and usage of NUMIDENT and other personally identifiable information in the possession of the Social Security Administration.",
    "type": "HRES",
    "updateDate": "2025-09-23T18:23:05Z",
    "updateDateIncludingText": "2025-09-23T18:23:05Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-09-11",
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
      "actionDate": "2025-09-11",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Submitted in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1025",
      "actionDate": "2025-09-11",
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
          "date": "2025-09-11T13:02:10Z",
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
      "bioguideId": "N000015",
      "district": "1",
      "firstName": "Richard",
      "fullName": "Rep. Neal, Richard E. [D-MA-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Neal",
      "middleName": "E.",
      "party": "D",
      "sponsorshipDate": "2025-09-11",
      "state": "MA"
    },
    {
      "bioguideId": "D000399",
      "district": "37",
      "firstName": "Lloyd",
      "fullName": "Rep. Doggett, Lloyd [D-TX-37]",
      "isOriginalCosponsor": "True",
      "lastName": "Doggett",
      "party": "D",
      "sponsorshipDate": "2025-09-11",
      "state": "TX"
    },
    {
      "bioguideId": "T000460",
      "district": "4",
      "firstName": "Mike",
      "fullName": "Rep. Thompson, Mike [D-CA-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Thompson",
      "party": "D",
      "sponsorshipDate": "2025-09-11",
      "state": "CA"
    },
    {
      "bioguideId": "D000096",
      "district": "7",
      "firstName": "Danny",
      "fullName": "Rep. Davis, Danny K. [D-IL-7]",
      "isOriginalCosponsor": "True",
      "lastName": "Davis",
      "middleName": "K.",
      "party": "D",
      "sponsorshipDate": "2025-09-11",
      "state": "IL"
    },
    {
      "bioguideId": "S001156",
      "district": "38",
      "firstName": "Linda",
      "fullName": "Rep. S\u00e1nchez, Linda T. [D-CA-38]",
      "isOriginalCosponsor": "True",
      "lastName": "S\u00e1nchez",
      "middleName": "T.",
      "party": "D",
      "sponsorshipDate": "2025-09-11",
      "state": "CA"
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
      "sponsorshipDate": "2025-09-11",
      "state": "AL"
    },
    {
      "bioguideId": "D000617",
      "district": "1",
      "firstName": "Suzan",
      "fullName": "Rep. DelBene, Suzan K. [D-WA-1]",
      "isOriginalCosponsor": "True",
      "lastName": "DelBene",
      "middleName": "K.",
      "party": "D",
      "sponsorshipDate": "2025-09-11",
      "state": "WA"
    },
    {
      "bioguideId": "C001080",
      "district": "28",
      "firstName": "Judy",
      "fullName": "Rep. Chu, Judy [D-CA-28]",
      "isOriginalCosponsor": "True",
      "lastName": "Chu",
      "party": "D",
      "sponsorshipDate": "2025-09-11",
      "state": "CA"
    },
    {
      "bioguideId": "M001160",
      "district": "4",
      "firstName": "Gwen",
      "fullName": "Rep. Moore, Gwen [D-WI-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Moore",
      "party": "D",
      "sponsorshipDate": "2025-09-11",
      "state": "WI"
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
      "sponsorshipDate": "2025-09-11",
      "state": "PA"
    },
    {
      "bioguideId": "B001292",
      "district": "8",
      "firstName": "Donald",
      "fullName": "Rep. Beyer, Donald S. [D-VA-8]",
      "isOriginalCosponsor": "True",
      "lastName": "Beyer",
      "middleName": "S.",
      "party": "D",
      "sponsorshipDate": "2025-09-11",
      "state": "VA"
    },
    {
      "bioguideId": "E000296",
      "district": "3",
      "firstName": "Dwight",
      "fullName": "Rep. Evans, Dwight [D-PA-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Evans",
      "party": "D",
      "sponsorshipDate": "2025-09-11",
      "state": "PA"
    },
    {
      "bioguideId": "S001190",
      "district": "10",
      "firstName": "Bradley",
      "fullName": "Rep. Schneider, Bradley Scott [D-IL-10]",
      "isOriginalCosponsor": "True",
      "lastName": "Schneider",
      "middleName": "Scott",
      "party": "D",
      "sponsorshipDate": "2025-09-11",
      "state": "IL"
    },
    {
      "bioguideId": "P000613",
      "district": "19",
      "firstName": "Jimmy",
      "fullName": "Rep. Panetta, Jimmy [D-CA-19]",
      "isOriginalCosponsor": "True",
      "lastName": "Panetta",
      "party": "D",
      "sponsorshipDate": "2025-09-11",
      "state": "CA"
    },
    {
      "bioguideId": "G000585",
      "district": "34",
      "firstName": "Jimmy",
      "fullName": "Rep. Gomez, Jimmy [D-CA-34]",
      "isOriginalCosponsor": "True",
      "lastName": "Gomez",
      "party": "D",
      "sponsorshipDate": "2025-09-11",
      "state": "CA"
    },
    {
      "bioguideId": "H001066",
      "district": "4",
      "firstName": "Steven",
      "fullName": "Rep. Horsford, Steven [D-NV-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Horsford",
      "party": "D",
      "sponsorshipDate": "2025-09-11",
      "state": "NV"
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
      "sponsorshipDate": "2025-09-11",
      "state": "VI"
    },
    {
      "bioguideId": "S001201",
      "district": "3",
      "firstName": "Thomas",
      "fullName": "Rep. Suozzi, Thomas R. [D-NY-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Suozzi",
      "middleName": "R.",
      "party": "D",
      "sponsorshipDate": "2025-09-11",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hres/BILLS-119hres701ih.xml",
      "text": "IV\n119th CONGRESS\n1st Session\nH. RES. 701\nIN THE HOUSE OF REPRESENTATIVES\nSeptember 11, 2025 Mr. Larson of Connecticut (for himself, Mr. Neal , Mr. Doggett , Mr. Thompson of California , Mr. Davis of Illinois , Ms. S\u00e1nchez , Ms. Sewell , Ms. DelBene , Ms. Chu , Ms. Moore of Wisconsin , Mr. Boyle of Pennsylvania , Mr. Beyer , Mr. Evans of Pennsylvania , Mr. Schneider , Mr. Panetta , Mr. Gomez , Mr. Horsford , Ms. Plaskett , and Mr. Suozzi ) submitted the following resolution; which was referred to the Committee on Ways and Means\nRESOLUTION\nOf inquiry requesting the President of the United States to furnish certain information to the House of Representatives relating to the Department of Government Efficiency\u2019s access to and usage of NUMIDENT and other personally identifiable information in the possession of the Social Security Administration.\nThat the President of the United States is requested to furnish the House of Representatives, not later than 14 days after the date of adoption of this resolution, copies of any document, record, audio recording, memorandum, call log, correspondence (electronic or otherwise), audit trails and audit logs, written agreements, or other communication in his possession, or any portion of any document, record, audio recording, memorandum, call log, correspondence (electronic or otherwise), or other communication, that refers or relates to the following:\n**(1)**\nThe development of a cloud environment that hosts a copy of the Social Security Administration\u2019s Numerical Identification System (hereafter referred to as NUMIDENT ), including risk assessments and security protocols.\n**(2)**\nThe purpose of creating a cloud environment that hosts a copy of the NUMIDENT, including whether the copy will be used to:\n**(A)**\nconduct Federal audits and investigations;\n**(B)**\nrestrict or deny Social Security benefits, Medicare coverage, or any other benefits;\n**(C)**\ndevelop a centralized database for the Federal Government that compiles citizens\u2019 personal information across Federal agencies and departments;\n**(D)**\nsell or make available information contained in the copy for private purchase; or\n**(E)**\ntrain and enhance artificial intelligence.\n**(3)**\nAccess to, and usage of, NUMIDENT information hosted in such cloud environment by Edward Coristine, Aram Moghaddassi, John Solly, Michael Russo, or any other individual, including those acting for or on behalf of the Department of Government Efficiency (hereafter referred to as DOGE ).\n**(4)**\nAccess to, and usage of, personally identifiable information inside the Social Security Administration\u2019s Enterprise Data Warehouse on or after March 14, 2025, by Payton Rehling, Aram Moghaddassi, or any other individuals acting for or on behalf of DOGE.",
      "versionDate": "2025-09-11",
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
        "name": "Government Operations and Politics",
        "updateDate": "2025-09-23T18:23:05Z"
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
      "date": "2025-09-11",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hres/BILLS-119hres701ih.xml"
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
      "title": "Of inquiry requesting the President of the United States to furnish certain information to the House of Representatives relating to the Department of Government Efficiency's access to and usage of NUMIDENT and other personally identifiable information in the possession of the Social Security Administration.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-09-12T08:18:19Z"
    },
    {
      "title": "Of inquiry requesting the President of the United States to furnish certain information to the House of Representatives relating to the Department of Government Efficiency's access to and usage of NUMIDENT and other personally identifiable information in the possession of the Social Security Administration.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-09-12T08:07:08Z"
    }
  ]
}
```
