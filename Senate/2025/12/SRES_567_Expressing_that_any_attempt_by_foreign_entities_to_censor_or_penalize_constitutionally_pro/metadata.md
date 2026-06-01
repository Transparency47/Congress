# Metadata

- API URL: https://api.congress.gov/v3/bill/119/sres/567?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-resolution/567
- Title: A resolution expressing that any attempt by foreign entities to censor or penalize constitutionally protected speech of United States persons shall be opposed.
- Congress: 119
- Bill type: SRES
- Bill number: 567
- Origin chamber: Senate
- Introduced date: 2025-12-17
- Update date: 2026-01-06T21:51:25Z
- Update date including text: 2026-01-06T21:51:25Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-12-17: Introduced in Senate
- 2025-12-17 - IntroReferral: Introduced in Senate
- 2025-12-17 - IntroReferral: Referred to the Committee on Foreign Relations.
- Latest action: 2025-12-17: Introduced in Senate

## Actions

- 2025-12-17 - IntroReferral: Introduced in Senate
- 2025-12-17 - IntroReferral: Referred to the Committee on Foreign Relations.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-12-17",
    "latestAction": {
      "actionDate": "2025-12-17",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-resolution/567",
    "number": "567",
    "originChamber": "Senate",
    "policyArea": {
      "name": "International Affairs"
    },
    "sponsors": [
      {
        "bioguideId": "L000577",
        "district": "",
        "firstName": "Mike",
        "fullName": "Sen. Lee, Mike [R-UT]",
        "lastName": "Lee",
        "party": "R",
        "state": "UT"
      }
    ],
    "title": "A resolution expressing that any attempt by foreign entities to censor or penalize constitutionally protected speech of United States persons shall be opposed.",
    "type": "SRES",
    "updateDate": "2026-01-06T21:51:25Z",
    "updateDateIncludingText": "2026-01-06T21:51:25Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-12-17",
      "committees": {
        "item": {
          "name": "Foreign Relations Committee",
          "systemCode": "ssfr00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Referred to the Committee on Foreign Relations.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-12-17",
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

## API Data: committees

```json
{
  "committees": [
    {
      "activities": {
        "item": {
          "date": "2025-12-18T00:43:14Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Foreign Relations Committee",
      "systemCode": "ssfr00",
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
      "bioguideId": "C001098",
      "firstName": "Ted",
      "fullName": "Sen. Cruz, Ted [R-TX]",
      "isOriginalCosponsor": "False",
      "lastName": "Cruz",
      "party": "R",
      "sponsorshipDate": "2025-12-18",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/sres/BILLS-119sres567is.xml",
      "text": "III\n119th CONGRESS\n1st Session\nS. RES. 567\nIN THE SENATE OF THE UNITED STATES\nDecember 17, 2025 Mr. Lee submitted the following resolution; which was referred to the Committee on Foreign Relations\nRESOLUTION\nExpressing that any attempt by foreign entities to censor or penalize constitutionally protected speech of United States persons shall be opposed.\nThat the Senate\u2014\n**(1)**\nreaffirms its commitment to protecting the commercial interests and free speech rights of United States persons;\n**(2)**\nrecognizes that the Digital Services Act is incompatible with the free speech tradition of the United States and the commitments that technology companies have made to hosting a diversity of opinions;\n**(3)**\ndisapproves of any attempt by a foreign entity to export censorship or limit the exercise of free speech by United States persons;\n**(4)**\ndisapproves of any attempt by a foreign entity to levy fines or other penalties against United States persons participating in constitutionally protected activities;\n**(5)**\ndisapproves of the attempts by the European Union to force United States entities to develop or use products and technology in ways that undermine free speech or foster censorship;\n**(6)**\ncommits to oppose any implementation of disapproved activities; and\n**(7)**\nurges the Trump administration to ensure swift and firm rejoinders to any implementation of disapproved activities.",
      "versionDate": "2025-12-17",
      "versionType": "IS"
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
        "name": "International Affairs",
        "updateDate": "2026-01-06T21:51:25Z"
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
      "date": "2025-12-17",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/sres/BILLS-119sres567is.xml"
        }
      ],
      "type": "IS"
    }
  ]
}
```

## API Data: titles

```json
{
  "titles": [
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A resolution expressing that any attempt by foreign entities to censor or penalize constitutionally protected speech of United States persons shall be opposed.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-12-19T06:51:44Z"
    },
    {
      "title": "A resolution expressing that any attempt by foreign entities to censor or penalize constitutionally protected speech of United States persons shall be opposed.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-12-18T11:56:26Z"
    }
  ]
}
```
