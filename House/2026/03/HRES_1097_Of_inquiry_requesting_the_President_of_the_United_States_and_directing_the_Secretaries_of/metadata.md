# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hres/1097?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-resolution/1097
- Title: Of inquiry requesting the President of the United States, and directing the Secretaries of the Treasury and Homeland Security, to furnish certain information to the House of Representatives relating to the implementation and enforcement of the "Memorandum of Understanding for the Exchange of Information for Nontax Criminal Enforcement" between the Department of the Treasury and the Department of Homeland Security.
- Congress: 119
- Bill type: HRES
- Bill number: 1097
- Origin chamber: House
- Introduced date: 2026-03-03
- Update date: 2026-04-07T15:45:54Z
- Update date including text: 2026-04-07T15:45:54Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2026-03-03: Introduced in House
- 2026-03-03 - IntroReferral: Referred to the House Committee on Ways and Means.
- 2026-03-03 - IntroReferral: Submitted in House
- 2026-03-03 - IntroReferral: Submitted in House
- Latest action: 2026-03-03: Submitted in House

## Actions

- 2026-03-03 - IntroReferral: Referred to the House Committee on Ways and Means.
- 2026-03-03 - IntroReferral: Submitted in House
- 2026-03-03 - IntroReferral: Submitted in House

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-03-03",
    "latestAction": {
      "actionDate": "2026-03-03",
      "text": "Submitted in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-resolution/1097",
    "number": "1097",
    "originChamber": "House",
    "policyArea": {
      "name": "Immigration"
    },
    "sponsors": [
      {
        "bioguideId": "G000585",
        "district": "34",
        "firstName": "Jimmy",
        "fullName": "Rep. Gomez, Jimmy [D-CA-34]",
        "lastName": "Gomez",
        "party": "D",
        "state": "CA"
      }
    ],
    "title": "Of inquiry requesting the President of the United States, and directing the Secretaries of the Treasury and Homeland Security, to furnish certain information to the House of Representatives relating to the implementation and enforcement of the \"Memorandum of Understanding for the Exchange of Information for Nontax Criminal Enforcement\" between the Department of the Treasury and the Department of Homeland Security.",
    "type": "HRES",
    "updateDate": "2026-04-07T15:45:54Z",
    "updateDateIncludingText": "2026-04-07T15:45:54Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2026-03-03",
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
      "actionDate": "2026-03-03",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Submitted in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1025",
      "actionDate": "2026-03-03",
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
          "date": "2026-03-03T17:02:30Z",
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
      "bioguideId": "S001156",
      "district": "38",
      "firstName": "Linda",
      "fullName": "Rep. S\u00e1nchez, Linda T. [D-CA-38]",
      "isOriginalCosponsor": "True",
      "lastName": "S\u00e1nchez",
      "middleName": "T.",
      "party": "D",
      "sponsorshipDate": "2026-03-03",
      "state": "CA"
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
      "sponsorshipDate": "2026-03-03",
      "state": "WA"
    },
    {
      "bioguideId": "D000399",
      "district": "37",
      "firstName": "Lloyd",
      "fullName": "Rep. Doggett, Lloyd [D-TX-37]",
      "isOriginalCosponsor": "True",
      "lastName": "Doggett",
      "party": "D",
      "sponsorshipDate": "2026-03-03",
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
      "sponsorshipDate": "2026-03-03",
      "state": "CA"
    },
    {
      "bioguideId": "L000557",
      "district": "1",
      "firstName": "John",
      "fullName": "Rep. Larson, John B. [D-CT-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Larson",
      "middleName": "B.",
      "party": "D",
      "sponsorshipDate": "2026-03-03",
      "state": "CT"
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
      "sponsorshipDate": "2026-03-03",
      "state": "IL"
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
      "sponsorshipDate": "2026-03-03",
      "state": "AL"
    },
    {
      "bioguideId": "C001080",
      "district": "28",
      "firstName": "Judy",
      "fullName": "Rep. Chu, Judy [D-CA-28]",
      "isOriginalCosponsor": "True",
      "lastName": "Chu",
      "party": "D",
      "sponsorshipDate": "2026-03-03",
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
      "sponsorshipDate": "2026-03-03",
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
      "sponsorshipDate": "2026-03-03",
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
      "sponsorshipDate": "2026-03-03",
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
      "sponsorshipDate": "2026-03-03",
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
      "sponsorshipDate": "2026-03-03",
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
      "sponsorshipDate": "2026-03-03",
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
      "sponsorshipDate": "2026-03-03",
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
      "sponsorshipDate": "2026-03-03",
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
      "sponsorshipDate": "2026-03-03",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hres/BILLS-119hres1097ih.xml",
      "text": "IV\n119th CONGRESS\n2d Session\nH. RES. 1097\nIN THE HOUSE OF REPRESENTATIVES\nMarch 3, 2026 Mr. Gomez (for himself, Ms. S\u00e1nchez , Ms. DelBene , Mr. Doggett , Mr. Thompson of California , Mr. Larson of Connecticut , Mr. Davis of Illinois , Ms. Sewell , Ms. Chu , Ms. Moore of Wisconsin , Mr. Boyle of Pennsylvania , Mr. Beyer , Mr. Evans of Pennsylvania , Mr. Schneider , Mr. Panetta , Mr. Horsford , Ms. Plaskett , and Mr. Suozzi ) submitted the following resolution; which was referred to the Committee on Ways and Means\nRESOLUTION\nOf inquiry requesting the President of the United States, and directing the Secretaries of the Treasury and Homeland Security, to furnish certain information to the House of Representatives relating to the implementation and enforcement of the Memorandum of Understanding for the Exchange of Information for Nontax Criminal Enforcement between the Department of the Treasury and the Department of Homeland Security.\nThat the President of the United States is requested, and the Secretaries of the Treasury and Homeland Security are directed, to furnish to the House of Representatives, not later than 14 days following the adoption of this resolution, copies, with appropriate redactions to the extent necessary to comply with Federal law, of any document, record, audio recording, memorandum, call log, correspondence (electronic or otherwise), audit trail, audit log, written agreement, or other communication, or any portion of any of the foregoing, in the possession of the President or the Secretaries, that refers or relates to the implementation or enforcement of the Memorandum of Understanding for the Exchange of Information for Nontax Criminal Enforcement (hereinafter the Memorandum of Understanding ) between the Department of the Treasury and the Department of Homeland Security, including (but not limited to) the following:\n**(1)**\nAny request by, or disclosure or provision of access to, the Department of Homeland Security with respect to any return information (as defined in section 6103(b)(2) of the Internal Revenue Code of 1986) of any taxpayer, including (but not limited to) information from any of the following Systems of Records:\n**(A)**\nTreasury/IRS 22.060 - Automated Non-Master File, 80 FR 54064 (Sept. 8, 2015).\n**(B)**\nTreasury/IRS 22.061 - Information Return Master File, 80 FR 54064 (Sept. 8, 2015).\n**(C)**\nTreasury/IRS 24.030 - Customer Account Data Engine Individual Master File, 80 FR 54064 (Sept. 8, 2015).\n**(D)**\nTreasury/IRS 24.046 - Customer Account Data Engine Business Master File, 80 FR 54064 (Sept. 8, 2015).\n**(E)**\nTreasury/IRS 34.037 - Audit Trail and Security Records, 80 FR 54064 (Sept. 8, 2015).\n**(F)**\nTreasury/IRS 42.008 - Audit Information Management System, 80 FR 54064 (Sept. 8, 2015).\n**(2)**\nAny policy, procedure, standard, or guideline of the Department of the Treasury or the Department of Homeland Security that refers or relates to the handling of any information described in paragraph (1) pursuant to the Memorandum of Understanding.\n**(3)**\nAny information that refers or relates to\u2014\n**(A)**\nthe implementation or enforcement of, or compliance with, any policy, procedure, standard, or guideline described in paragraph (2),\n**(B)**\nany request by, or disclosure or provision of access to, the Department of Homeland Security with respect to any information described in paragraph (1) in violation of\u2014\n**(i)**\nsection 6103 of the Internal Revenue Code of 1986, or\n**(ii)**\nany policy, procedure, standard, or guideline described in paragraph (2), and\n**(C)**\nthe discovery of, and all subsequent action (both taken and considered) with respect to, any violation described in subparagraph (B).",
      "versionDate": "2026-03-03",
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
        "name": "Immigration",
        "updateDate": "2026-04-07T15:45:53Z"
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
      "date": "2026-03-03",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hres/BILLS-119hres1097ih.xml"
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
      "title": "Of inquiry requesting the President of the United States, and directing the Secretaries of the Treasury and Homeland Security, to furnish certain information to the House of Representatives relating to the implementation and enforcement of the \"Memorandum of Understanding for the Exchange of Information for Nontax Criminal Enforcement\" between the Department of the Treasury and the Department of Homeland Security.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-03-04T09:18:43Z"
    },
    {
      "title": "Of inquiry requesting the President of the United States, and directing the Secretaries of the Treasury and Homeland Security, to furnish certain information to the House of Representatives relating to the implementation and enforcement of the \"Memorandum of Understanding for the Exchange of Information for Nontax Criminal Enforcement\" between the Department of the Treasury and the Department of Homeland Security.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-03-04T09:06:39Z"
    }
  ]
}
```
