# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hres/1241?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-resolution/1241
- Title: Of inquiry requesting the President of the United States to furnish certain information to the House of Representatives relating to access to and usage of NUMIDENT, death information, and other personally identifiable information in the possession of the Social Security Administration by an individual acting for or on behalf of the Department of Government Efficiency.
- Congress: 119
- Bill type: HRES
- Bill number: 1241
- Origin chamber: House
- Introduced date: 2026-04-30
- Update date: 2026-05-14T18:41:34Z
- Update date including text: 2026-05-14T18:41:34Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2026-04-30: Introduced in House
- 2026-04-30 - IntroReferral: Referred to the House Committee on Ways and Means.
- 2026-04-30 - IntroReferral: Submitted in House
- Latest action: 2026-04-30: Submitted in House

## Actions

- 2026-04-30 - IntroReferral: Referred to the House Committee on Ways and Means.
- 2026-04-30 - IntroReferral: Submitted in House

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-04-30",
    "latestAction": {
      "actionDate": "2026-04-30",
      "text": "Submitted in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-resolution/1241",
    "number": "1241",
    "originChamber": "House",
    "policyArea": {
      "name": "Social Welfare"
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
    "title": "Of inquiry requesting the President of the United States to furnish certain information to the House of Representatives relating to access to and usage of NUMIDENT, death information, and other personally identifiable information in the possession of the Social Security Administration by an individual acting for or on behalf of the Department of Government Efficiency.",
    "type": "HRES",
    "updateDate": "2026-05-14T18:41:34Z",
    "updateDateIncludingText": "2026-05-14T18:41:34Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2026-04-30",
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
      "actionCode": "1025",
      "actionDate": "2026-04-30",
      "committees": {
        "item": {
          "name": "Ways and Means Committee",
          "systemCode": "hswm00"
        }
      },
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
          "date": "2026-04-30T13:08:20Z",
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
      "sponsorshipDate": "2026-04-30",
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
      "sponsorshipDate": "2026-04-30",
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
      "sponsorshipDate": "2026-04-30",
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
      "sponsorshipDate": "2026-04-30",
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
      "sponsorshipDate": "2026-04-30",
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
      "sponsorshipDate": "2026-04-30",
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
      "sponsorshipDate": "2026-04-30",
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
      "sponsorshipDate": "2026-04-30",
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
      "sponsorshipDate": "2026-04-30",
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
      "sponsorshipDate": "2026-04-30",
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
      "sponsorshipDate": "2026-04-30",
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
      "sponsorshipDate": "2026-04-30",
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
      "sponsorshipDate": "2026-04-30",
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
      "sponsorshipDate": "2026-04-30",
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
      "sponsorshipDate": "2026-04-30",
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
      "sponsorshipDate": "2026-04-30",
      "state": "NV"
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
      "sponsorshipDate": "2026-04-30",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hres/BILLS-119hres1241ih.xml",
      "text": "IV\n119th CONGRESS\n2d Session\nH. RES. 1241\nIN THE HOUSE OF REPRESENTATIVES\nApril 30, 2026 Mr. Larson of Connecticut (for himself, Mr. Neal , Mr. Doggett , Mr. Thompson of California , Mr. Davis of Illinois , Ms. S\u00e1nchez , Ms. Sewell , Ms. DelBene , Ms. Chu , Ms. Moore of Wisconsin , Mr. Boyle of Pennsylvania , Mr. Beyer , Mr. Evans of Pennsylvania , Mr. Schneider , Mr. Panetta , Mr. Gomez , Mr. Horsford , and Mr. Suozzi ) submitted the following resolution; which was referred to the Committee on Ways and Means\nRESOLUTION\nOf inquiry requesting the President of the United States to furnish certain information to the House of Representatives relating to access to and usage of NUMIDENT, death information, and other personally identifiable information in the possession of the Social Security Administration by an individual acting for or on behalf of the Department of Government Efficiency.\nThat the President of the United States is requested to furnish the House of Representatives, not later than 14 days after the date of adoption of this resolution, copies of any document, record, audio recording, memorandum, call log, correspondence (electronic or otherwise), audit trails and audit logs, written agreements, or other communication in his possession, or any portion of any document, record, audio recording, memorandum, call log, correspondence (electronic or otherwise), or other communication, that refers or relates to the following:\n**(1)**\nNumerical Identification System (hereafter referred to as NUMIDENT ) information, death information, and other personally identifiable information in the possession of the Social Security Administration which an individual acting for or on behalf of the Department of Government Efficiency (hereafter referred to as DOGE ) reportedly duplicated onto a personal thumb drive or other personal electronic device.\n**(2)**\nReported efforts by an individual acting for or on behalf of DOGE to share with the individual\u2019s private sector employer the NUMIDENT information, death information, and other personally identifiable information duplicated from the Social Security Administration onto a personal thumb drive or other personal electronic device.\n**(3)**\nReported statements by an individual acting for or on behalf of DOGE regarding expectations of receiving a presidential pardon if actions with respect to personally identifying information in the possession of the Social Security Administration were deemed to be illegal.",
      "versionDate": "2026-04-30",
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
        "updateDate": "2026-05-14T18:41:33Z"
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
      "date": "2026-04-30",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hres/BILLS-119hres1241ih.xml"
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
      "title": "Of inquiry requesting the President of the United States to furnish certain information to the House of Representatives relating to access to and usage of NUMIDENT, death information, and other personally identifiable information in the possession of the Social Security Administration by an individual acting for or on behalf of the Department of Government Efficiency.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-05-01T08:48:44Z"
    },
    {
      "title": "Of inquiry requesting the President of the United States to furnish certain information to the House of Representatives relating to access to and usage of NUMIDENT, death information, and other personally identifiable information in the possession of the Social Security Administration by an individual acting for or on behalf of the Department of Government Efficiency.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-05-01T08:09:21Z"
    }
  ]
}
```
