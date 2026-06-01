# Metadata

- API URL: https://api.congress.gov/v3/bill/119/sres/332?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/sres/332
- Title: A resolution designating July 26, 2025, as "National Day of the American Cowboy".
- Congress: 119
- Bill type: SRES
- Bill number: 332
- Origin chamber: Senate
- Introduced date: 2025-07-22
- Update date: 2025-08-06T13:51:21Z
- Update date including text: 2025-08-06T13:51:21Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-07-22: Introduced in Senate
- 2025-07-22 - IntroReferral: Introduced in Senate
- 2025-07-22 - Floor: Passed/agreed to in Senate: Submitted in the Senate, considered, and agreed to without amendment and with a preamble by Unanimous Consent.
- 2025-07-22 - Floor: Submitted in the Senate, considered, and agreed to without amendment and with a preamble by Unanimous Consent. (consideration: CR S4573: 2; text: CR S4533: 1)
- 2025-07-28 - Floor: Star Print ordered on the resolution.
- Latest action: 2025-07-22: Introduced in Senate

## Actions

- 2025-07-22 - IntroReferral: Introduced in Senate
- 2025-07-22 - Floor: Passed/agreed to in Senate: Submitted in the Senate, considered, and agreed to without amendment and with a preamble by Unanimous Consent.
- 2025-07-22 - Floor: Submitted in the Senate, considered, and agreed to without amendment and with a preamble by Unanimous Consent. (consideration: CR S4573: 2; text: CR S4533: 1)
- 2025-07-28 - Floor: Star Print ordered on the resolution.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-07-22",
    "latestAction": {
      "actionDate": "2025-07-22",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/sres/332",
    "number": "332",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Arts, Culture, Religion"
    },
    "sponsors": [
      {
        "bioguideId": "B001261",
        "district": "",
        "firstName": "John",
        "fullName": "Sen. Barrasso, John [R-WY]",
        "lastName": "Barrasso",
        "party": "R",
        "state": "WY"
      }
    ],
    "title": "A resolution designating July 26, 2025, as \"National Day of the American Cowboy\".",
    "type": "SRES",
    "updateDate": "2025-08-06T13:51:21Z",
    "updateDateIncludingText": "2025-08-06T13:51:21Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-07-28",
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Star Print ordered on the resolution.",
      "type": "Floor"
    },
    {
      "actionDate": "2025-07-22",
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Submitted in the Senate, considered, and agreed to without amendment and with a preamble by Unanimous Consent. (consideration: CR S4573: 2; text: CR S4533: 1)",
      "type": "Floor"
    },
    {
      "actionCode": "17000",
      "actionDate": "2025-07-22",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Passed/agreed to in Senate: Submitted in the Senate, considered, and agreed to without amendment and with a preamble by Unanimous Consent.",
      "type": "Floor"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-07-22",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in Senate",
      "type": "IntroReferral"
    }
  ]
}
```

## API Data: cosponsors

```json
{
  "cosponsors": [
    {
      "bioguideId": "H000273",
      "firstName": "John",
      "fullName": "Sen. Hickenlooper, John W. [D-CO]",
      "isOriginalCosponsor": "True",
      "lastName": "Hickenlooper",
      "middleName": "W.",
      "party": "D",
      "sponsorshipDate": "2025-07-22",
      "state": "CO"
    },
    {
      "bioguideId": "L000571",
      "firstName": "Cynthia",
      "fullName": "Sen. Lummis, Cynthia M. [R-WY]",
      "isOriginalCosponsor": "True",
      "lastName": "Lummis",
      "middleName": "M.",
      "party": "R",
      "sponsorshipDate": "2025-07-22",
      "state": "WY"
    },
    {
      "bioguideId": "C001113",
      "firstName": "Catherine",
      "fullName": "Sen. Cortez Masto, Catherine [D-NV]",
      "isOriginalCosponsor": "True",
      "lastName": "Cortez Masto",
      "party": "D",
      "sponsorshipDate": "2025-07-22",
      "state": "NV"
    },
    {
      "bioguideId": "R000584",
      "firstName": "James",
      "fullName": "Sen. Risch, James E. [R-ID]",
      "isOriginalCosponsor": "True",
      "lastName": "Risch",
      "middleName": "E.",
      "party": "R",
      "sponsorshipDate": "2025-07-22",
      "state": "ID"
    },
    {
      "bioguideId": "C001096",
      "firstName": "Kevin",
      "fullName": "Sen. Cramer, Kevin [R-ND]",
      "isOriginalCosponsor": "True",
      "lastName": "Cramer",
      "party": "R",
      "sponsorshipDate": "2025-07-22",
      "state": "ND"
    },
    {
      "bioguideId": "R000618",
      "firstName": "Pete",
      "fullName": "Sen. Ricketts, Pete [R-NE]",
      "isOriginalCosponsor": "True",
      "lastName": "Ricketts",
      "party": "R",
      "sponsorshipDate": "2025-07-22",
      "state": "NE"
    },
    {
      "bioguideId": "C001098",
      "firstName": "Ted",
      "fullName": "Sen. Cruz, Ted [R-TX]",
      "isOriginalCosponsor": "True",
      "lastName": "Cruz",
      "party": "R",
      "sponsorshipDate": "2025-07-22",
      "state": "TX"
    },
    {
      "bioguideId": "C001056",
      "firstName": "John",
      "fullName": "Sen. Cornyn, John [R-TX]",
      "isOriginalCosponsor": "True",
      "lastName": "Cornyn",
      "party": "R",
      "sponsorshipDate": "2025-07-22",
      "state": "TX"
    },
    {
      "bioguideId": "H001061",
      "firstName": "John",
      "fullName": "Sen. Hoeven, John [R-ND]",
      "isOriginalCosponsor": "True",
      "lastName": "Hoeven",
      "party": "R",
      "sponsorshipDate": "2025-07-22",
      "state": "ND"
    },
    {
      "bioguideId": "C000880",
      "firstName": "Mike",
      "fullName": "Sen. Crapo, Mike [R-ID]",
      "isOriginalCosponsor": "True",
      "lastName": "Crapo",
      "party": "R",
      "sponsorshipDate": "2025-07-22",
      "state": "ID"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/sres/BILLS-119sres332ats.xml",
      "text": "III\n119th CONGRESS\n1st Session\nS. RES. 332\nIN THE SENATE OF THE UNITED STATES\nJuly 22, 2025 Mr. Barrasso (for himself, Mr. Hickenlooper , Ms. Lummis , Ms. Cortez Masto , Mr. Risch , Mr. Cramer , Mr. Ricketts , Mr. Cruz , Mr. Cornyn , Mr. Hoeven , and Mr. Crapo ) submitted the following resolution; which was considered and agreed to\nRESOLUTION\nDesignating July 26, 2025, as National Day of the American Cowboy .\nThat the Senate\u2014\n**(1)**\ndesignates July 26, 2025, as National Day of the American Cowboy ; and\n**(2)**\nencourages the people of the United States to observe the day with appropriate ceremonies and activities.",
      "versionDate": "2025-07-22",
      "versionType": "ATS"
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
            "name": "Commemorative events and holidays",
            "updateDate": "2025-08-06T13:49:02Z"
          },
          {
            "name": "Migrant, seasonal, agricultural labor",
            "updateDate": "2025-08-06T13:51:21Z"
          },
          {
            "name": "U.S. history",
            "updateDate": "2025-08-06T13:49:46Z"
          }
        ]
      },
      "policyArea": {
        "name": "Arts, Culture, Religion",
        "updateDate": "2025-08-01T15:02:51Z"
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
      "date": "2025-07-22",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/sres/BILLS-119sres332ats.xml"
        }
      ],
      "type": "ATS"
    }
  ]
}
```

## API Data: titles

```json
{
  "titles": [
    {
      "title": "A resolution designating July 26, 2025, as \"National Day of the American Cowboy\".",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-07-23T10:56:18Z"
    },
    {
      "title": "A resolution designating July 26, 2025, as \"National Day of the American Cowboy\".",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-07-23T10:56:18Z"
    }
  ]
}
```
