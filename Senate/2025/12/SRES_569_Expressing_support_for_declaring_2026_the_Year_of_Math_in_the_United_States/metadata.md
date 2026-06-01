# Metadata

- API URL: https://api.congress.gov/v3/bill/119/sres/569?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-resolution/569
- Title: A resolution expressing support for declaring 2026 the "Year of Math" in the United States.
- Congress: 119
- Bill type: SRES
- Bill number: 569
- Origin chamber: Senate
- Introduced date: 2025-12-18
- Update date: 2026-03-04T15:55:38Z
- Update date including text: 2026-03-04T15:55:38Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-12-18: Introduced in Senate
- 2025-12-18 - IntroReferral: Introduced in Senate
- 2025-12-18 - IntroReferral: Referred to the Committee on Commerce, Science, and Transportation. (text: CR S8924-8925)
- Latest action: 2025-12-18: Introduced in Senate

## Actions

- 2025-12-18 - IntroReferral: Introduced in Senate
- 2025-12-18 - IntroReferral: Referred to the Committee on Commerce, Science, and Transportation. (text: CR S8924-8925)

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-12-18",
    "latestAction": {
      "actionDate": "2025-12-18",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-resolution/569",
    "number": "569",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Science, Technology, Communications"
    },
    "sponsors": [
      {
        "bioguideId": "H000273",
        "district": "",
        "firstName": "John",
        "fullName": "Sen. Hickenlooper, John W. [D-CO]",
        "lastName": "Hickenlooper",
        "party": "D",
        "state": "CO"
      }
    ],
    "title": "A resolution expressing support for declaring 2026 the \"Year of Math\" in the United States.",
    "type": "SRES",
    "updateDate": "2026-03-04T15:55:38Z",
    "updateDateIncludingText": "2026-03-04T15:55:38Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-12-18",
      "committees": {
        "item": {
          "name": "Commerce, Science, and Transportation Committee",
          "systemCode": "sscm00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Referred to the Committee on Commerce, Science, and Transportation. (text: CR S8924-8925)",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-12-18",
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
          "date": "2025-12-18T20:16:55Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Commerce, Science, and Transportation Committee",
      "systemCode": "sscm00",
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
      "bioguideId": "C001047",
      "firstName": "Shelley",
      "fullName": "Sen. Capito, Shelley Moore [R-WV]",
      "isOriginalCosponsor": "True",
      "lastName": "Capito",
      "middleName": "Moore",
      "party": "R",
      "sponsorshipDate": "2025-12-18",
      "state": "WV"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/sres/BILLS-119sres569is.xml",
      "text": "III\n119th CONGRESS\n1st Session\nS. RES. 569\nIN THE SENATE OF THE UNITED STATES\nDecember 18, 2025 Mr. Hickenlooper (for himself and Mrs. Capito ) submitted the following resolution; which was referred to the Committee on Commerce, Science, and Transportation\nRESOLUTION\nExpressing support for declaring 2026 the Year of Math in the United States.\nThat the Senate\u2014\n**(1)**\nexpresses support for the declaration of a Year of Math in the United States;\n**(2)**\ncelebrates the United States being selected as host of the International Congress of Mathematicians 2026 and using this platform to increase the visibility of mathematical sciences as fields of study and to communicate the myriad benefits of education in mathematics and statistics;\n**(3)**\nrecognizes that mathematics underpins all of the STEM (science, technology, engineering, and mathematics) disciplines, which are critical to the national security and economic prosperity of the United States; and\n**(4)**\ncelebrates the role that mathematics and statistics play in the everyday lives of all people of the United States, including in technology, news, games, literature, and music.",
      "versionDate": "2025-12-18",
      "versionType": "IS"
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
        "actionDate": "2026-03-02",
        "text": "Referred to the House Committee on Science, Space, and Technology."
      },
      "number": "1091",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Expressing support for declaring 2026 the \"Year of Math\" in the United States.",
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
      "legislativeSubjects": "",
      "policyArea": {
        "name": "Science, Technology, Communications",
        "updateDate": "2026-01-06T19:25:19Z"
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
      "date": "2025-12-18",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/sres/BILLS-119sres569is.xml"
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
      "title": "A resolution expressing support for declaring 2026 the \"Year of Math\" in the United States.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-12-20T05:48:20Z"
    },
    {
      "title": "A resolution expressing support for declaring 2026 the \"Year of Math\" in the United States.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-12-19T11:56:21Z"
    }
  ]
}
```
