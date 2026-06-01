# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hres/973?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-resolution/973
- Title: Expressing the sense of the House of Representatives that the designation of the "Donald J. Trump and the John F. Kennedy Memorial Center for the Performing Arts" constitutes a violation of Federal law, and for other purposes.
- Congress: 119
- Bill type: HRES
- Bill number: 973
- Origin chamber: House
- Introduced date: 2025-12-30
- Update date: 2026-02-03T09:05:48Z
- Update date including text: 2026-02-03T09:05:48Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-12-30: Introduced in House
- 2025-12-30 - IntroReferral: Referred to the House Committee on Transportation and Infrastructure.
- 2025-12-30 - IntroReferral: Submitted in House
- 2025-12-30 - IntroReferral: Submitted in House
- 2025-12-30 - IntroReferral: Submitted in House
- 2025-12-30 - IntroReferral: Submitted in House
- 2026-02-02 - Committee: Referred to the Subcommittee on Economic Development, Public Buildings, and Emergency Management.
- Latest action: 2025-12-30: Submitted in House

## Actions

- 2025-12-30 - IntroReferral: Referred to the House Committee on Transportation and Infrastructure.
- 2025-12-30 - IntroReferral: Submitted in House
- 2025-12-30 - IntroReferral: Submitted in House
- 2025-12-30 - IntroReferral: Submitted in House
- 2025-12-30 - IntroReferral: Submitted in House
- 2026-02-02 - Committee: Referred to the Subcommittee on Economic Development, Public Buildings, and Emergency Management.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-12-30",
    "latestAction": {
      "actionDate": "2025-12-30",
      "text": "Submitted in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-resolution/973",
    "number": "973",
    "originChamber": "House",
    "policyArea": {
      "name": "Arts, Culture, Religion"
    },
    "sponsors": [
      {
        "bioguideId": "L000562",
        "district": "8",
        "firstName": "Stephen",
        "fullName": "Rep. Lynch, Stephen F. [D-MA-8]",
        "lastName": "Lynch",
        "party": "D",
        "state": "MA"
      }
    ],
    "title": "Expressing the sense of the House of Representatives that the designation of the \"Donald J. Trump and the John F. Kennedy Memorial Center for the Performing Arts\" constitutes a violation of Federal law, and for other purposes.",
    "type": "HRES",
    "updateDate": "2026-02-03T09:05:48Z",
    "updateDateIncludingText": "2026-02-03T09:05:48Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-02-02",
      "committees": {
        "item": {
          "name": "Economic Development, Public Buildings, and Emergency Management Subcommittee",
          "systemCode": "hspw13"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Referred to the Subcommittee on Economic Development, Public Buildings, and Emergency Management.",
      "type": "Committee"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-12-30",
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
      "actionDate": "2025-12-30",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Submitted in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-12-30",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Submitted in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1025",
      "actionDate": "2025-12-30",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Submitted in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1025",
      "actionDate": "2025-12-30",
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
          "date": "2025-12-30T18:00:10Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Transportation and Infrastructure Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": {
              "date": "2026-02-02T19:46:27Z",
              "name": "Referred to"
            }
          },
          "name": "Economic Development, Public Buildings, and Emergency Management Subcommittee",
          "systemCode": "hspw13"
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
      "bioguideId": "D000096",
      "district": "7",
      "firstName": "Danny",
      "fullName": "Rep. Davis, Danny K. [D-IL-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Davis",
      "middleName": "K.",
      "party": "D",
      "sponsorshipDate": "2026-01-06",
      "state": "IL"
    },
    {
      "bioguideId": "E000296",
      "district": "3",
      "firstName": "Dwight",
      "fullName": "Rep. Evans, Dwight [D-PA-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Evans",
      "party": "D",
      "sponsorshipDate": "2026-01-06",
      "state": "PA"
    },
    {
      "bioguideId": "T000193",
      "district": "2",
      "firstName": "Bennie",
      "fullName": "Rep. Thompson, Bennie G. [D-MS-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Thompson",
      "middleName": "G.",
      "party": "D",
      "sponsorshipDate": "2026-01-06",
      "state": "MS"
    },
    {
      "bioguideId": "N000147",
      "district": "0",
      "firstName": "Eleanor",
      "fullName": "Del. Norton, Eleanor Holmes [D-DC-At Large]",
      "isOriginalCosponsor": "False",
      "lastName": "Norton",
      "middleName": "Holmes",
      "party": "D",
      "sponsorshipDate": "2026-01-06",
      "state": "DC"
    },
    {
      "bioguideId": "K000375",
      "district": "9",
      "firstName": "William",
      "fullName": "Rep. Keating, William R. [D-MA-9]",
      "isOriginalCosponsor": "False",
      "lastName": "Keating",
      "middleName": "R.",
      "party": "D",
      "sponsorshipDate": "2026-01-06",
      "state": "MA"
    },
    {
      "bioguideId": "N000015",
      "district": "1",
      "firstName": "Richard",
      "fullName": "Rep. Neal, Richard E. [D-MA-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Neal",
      "middleName": "E.",
      "party": "D",
      "sponsorshipDate": "2026-01-07",
      "state": "MA"
    },
    {
      "bioguideId": "L000397",
      "district": "18",
      "firstName": "Zoe",
      "fullName": "Rep. Lofgren, Zoe [D-CA-18]",
      "isOriginalCosponsor": "False",
      "lastName": "Lofgren",
      "party": "D",
      "sponsorshipDate": "2026-01-07",
      "state": "CA"
    },
    {
      "bioguideId": "S001205",
      "district": "5",
      "firstName": "Mary Gay",
      "fullName": "Rep. Scanlon, Mary Gay [D-PA-5]",
      "isOriginalCosponsor": "False",
      "lastName": "Scanlon",
      "party": "D",
      "sponsorshipDate": "2026-01-07",
      "state": "PA"
    },
    {
      "bioguideId": "P000034",
      "district": "6",
      "firstName": "Frank",
      "fullName": "Rep. Pallone, Frank [D-NJ-6]",
      "isOriginalCosponsor": "False",
      "lastName": "Pallone",
      "party": "D",
      "sponsorshipDate": "2026-01-08",
      "state": "NJ"
    },
    {
      "bioguideId": "G000559",
      "district": "8",
      "firstName": "John",
      "fullName": "Rep. Garamendi, John [D-CA-8]",
      "isOriginalCosponsor": "False",
      "lastName": "Garamendi",
      "party": "D",
      "sponsorshipDate": "2026-01-14",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hres/BILLS-119hres973ih.xml",
      "text": "IV\n119th CONGRESS\n1st Session\nH. RES. 973\nIN THE HOUSE OF REPRESENTATIVES\nDecember 30, 2025 Mr. Lynch submitted the following resolution; which was referred to the Committee on Transportation and Infrastructure\nRESOLUTION\nExpressing the sense of the House of Representatives that the designation of the Donald J. Trump and the John F. Kennedy Memorial Center for the Performing Arts constitutes a violation of Federal law, and for other purposes.\nThat it is the sense of the House of Representatives that\u2014\n**(1)**\nthe designation of The Donald J. Trump and the John F. Kennedy Memorial Center for the Performing Arts by the Board of Trustees constitutes a violation of Federal law and contravenes the express intent of Congress to solely honor, with a national monument, President John F. Kennedy and his appreciation and promotion of the arts;\n**(2)**\nthe original signage for the John F. Kennedy Center for the Performing Arts should be immediately restored; and\n**(3)**\nall officers and members appointed by President Trump to the Board of Trustees should promptly resign their positions.",
      "versionDate": "2025-12-30",
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
        "name": "Arts, Culture, Religion",
        "updateDate": "2026-01-05T15:53:26Z"
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
      "date": "2025-12-30",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hres/BILLS-119hres973ih.xml"
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
      "title": "Expressing the sense of the House of Representatives that the designation of the \"Donald J. Trump and the John F. Kennedy Memorial Center for the Performing Arts\" constitutes a violation of Federal law, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-12-31T09:18:13Z"
    },
    {
      "title": "Expressing the sense of the House of Representatives that the designation of the \"Donald J. Trump and the John F. Kennedy Memorial Center for the Performing Arts\" constitutes a violation of Federal law, and for other purposes.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-12-31T09:05:19Z"
    }
  ]
}
```
