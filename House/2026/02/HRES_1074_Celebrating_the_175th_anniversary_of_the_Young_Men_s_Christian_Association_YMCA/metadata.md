# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hres/1074?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-resolution/1074
- Title: Celebrating the 175th anniversary of the Young Men's Christian Association (YMCA).
- Congress: 119
- Bill type: HRES
- Bill number: 1074
- Origin chamber: House
- Introduced date: 2026-02-23
- Update date: 2026-03-25T08:05:53Z
- Update date including text: 2026-03-25T08:05:53Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2026-02-23: Introduced in House
- 2026-02-23 - IntroReferral: Referred to the House Committee on Education and Workforce.
- 2026-02-23 - IntroReferral: Submitted in House
- 2026-02-23 - IntroReferral: Submitted in House
- Latest action: 2026-02-23: Submitted in House

## Actions

- 2026-02-23 - IntroReferral: Referred to the House Committee on Education and Workforce.
- 2026-02-23 - IntroReferral: Submitted in House
- 2026-02-23 - IntroReferral: Submitted in House

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-02-23",
    "latestAction": {
      "actionDate": "2026-02-23",
      "text": "Submitted in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-resolution/1074",
    "number": "1074",
    "originChamber": "House",
    "policyArea": {
      "name": "Sports and Recreation"
    },
    "sponsors": [
      {
        "bioguideId": "Q000023",
        "district": "5",
        "firstName": "Mike",
        "fullName": "Rep. Quigley, Mike [D-IL-5]",
        "lastName": "Quigley",
        "party": "D",
        "state": "IL"
      }
    ],
    "title": "Celebrating the 175th anniversary of the Young Men's Christian Association (YMCA).",
    "type": "HRES",
    "updateDate": "2026-03-25T08:05:53Z",
    "updateDateIncludingText": "2026-03-25T08:05:53Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2026-02-23",
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
      "actionDate": "2026-02-23",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Submitted in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1025",
      "actionDate": "2026-02-23",
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
          "date": "2026-02-23T17:01:35Z",
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
      "bioguideId": "E000246",
      "district": "11",
      "firstName": "Chuck",
      "fullName": "Rep. Edwards, Chuck [R-NC-11]",
      "isOriginalCosponsor": "True",
      "lastName": "Edwards",
      "party": "R",
      "sponsorshipDate": "2026-02-23",
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
      "sponsorshipDate": "2026-02-23",
      "state": "NH"
    },
    {
      "bioguideId": "S001145",
      "district": "9",
      "firstName": "Janice",
      "fullName": "Rep. Schakowsky, Janice D. [D-IL-9]",
      "isOriginalCosponsor": "False",
      "lastName": "Schakowsky",
      "middleName": "D.",
      "party": "D",
      "sponsorshipDate": "2026-03-05",
      "state": "IL"
    },
    {
      "bioguideId": "G000583",
      "district": "5",
      "firstName": "Josh",
      "fullName": "Rep. Gottheimer, Josh [D-NJ-5]",
      "isOriginalCosponsor": "False",
      "lastName": "Gottheimer",
      "party": "D",
      "sponsorshipDate": "2026-03-24",
      "state": "NJ"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hres/BILLS-119hres1074ih.xml",
      "text": "IV\n119th CONGRESS\n2d Session\nH. RES. 1074\nIN THE HOUSE OF REPRESENTATIVES\nFebruary 23, 2026 Mr. Quigley (for himself, Mr. Edwards , and Mr. Pappas ) submitted the following resolution; which was referred to the Committee on Education and Workforce\nRESOLUTION\nCelebrating the 175th anniversary of the Young Men\u2019s Christian Association (YMCA).\nThat the House of Representatives\u2014\n**(1)**\ncongratulates and expresses appreciation to the Young Men's Christian Association (YMCA) for 175 years of service to the United States;\n**(2)**\nrecognizes the YMCA\u2019s role in responding to community needs, connecting people, fostering support, and building relationships and a sense of belonging;\n**(3)**\ncommends the hundreds of thousands of staff and volunteers who create connected communities and advance the YMCA\u2019s mission to build healthy spirits, minds, and bodies for all; and\n**(4)**\nencourages continued support for the efforts to address social isolation and loneliness by creating places and spaces that promote achievement, well-being, and connection and help people build relationships and thrive.",
      "versionDate": "2026-02-23",
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
        "actionDate": "2026-03-12",
        "text": "Submitted in the Senate, considered, and agreed to without amendment and with a preamble by Unanimous Consent. (consideration: CR S1051; text: CR S1051)"
      },
      "number": "642",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "A resolution celebrating the 175th anniversary of the Young Men's Christian Association (YMCA).",
      "type": "SRES"
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
        "name": "Sports and Recreation",
        "updateDate": "2026-02-25T18:38:35Z"
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
      "date": "2026-02-23",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hres/BILLS-119hres1074ih.xml"
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
      "title": "Celebrating the 175th anniversary of the Young Men's Christian Association (YMCA).",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-02-24T09:18:29Z"
    },
    {
      "title": "Celebrating the 175th anniversary of the Young Men's Christian Association (YMCA).",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-02-24T09:05:33Z"
    }
  ]
}
```
