# Metadata

- API URL: https://api.congress.gov/v3/bill/119/sres/699?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-resolution/699
- Title: A resolution expressing support for the recognition of April as "National Language Access Month".
- Congress: 119
- Bill type: SRES
- Bill number: 699
- Origin chamber: Senate
- Introduced date: 2026-04-29
- Update date: 2026-05-15T22:44:00Z
- Update date including text: 2026-05-15T22:44:00Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2026-04-29: Introduced in Senate
- 2026-04-29 - IntroReferral: Referred to the Committee on Homeland Security and Governmental Affairs. (text: CR S2133-2134)
- 2026-04-29 - IntroReferral: Submitted in Senate
- Latest action: 2026-04-29: Submitted in Senate

## Actions

- 2026-04-29 - IntroReferral: Referred to the Committee on Homeland Security and Governmental Affairs. (text: CR S2133-2134)
- 2026-04-29 - IntroReferral: Submitted in Senate

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-04-29",
    "latestAction": {
      "actionDate": "2026-04-29",
      "text": "Submitted in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-resolution/699",
    "number": "699",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Government Operations and Politics"
    },
    "sponsors": [
      {
        "bioguideId": "P000145",
        "district": "",
        "firstName": "Alex",
        "fullName": "Sen. Padilla, Alex [D-CA]",
        "lastName": "Padilla",
        "party": "D",
        "state": "CA"
      }
    ],
    "title": "A resolution expressing support for the recognition of April as \"National Language Access Month\".",
    "type": "SRES",
    "updateDate": "2026-05-15T22:44:00Z",
    "updateDateIncludingText": "2026-05-15T22:44:00Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-04-29",
      "committees": {
        "item": {
          "name": "Homeland Security and Governmental Affairs Committee",
          "systemCode": "ssga00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Referred to the Committee on Homeland Security and Governmental Affairs. (text: CR S2133-2134)",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10025",
      "actionDate": "2026-04-29",
      "committees": {
        "item": {
          "name": "Homeland Security and Governmental Affairs Committee",
          "systemCode": "ssga00"
        }
      },
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Submitted in Senate",
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
          "date": "2026-04-29T20:22:44Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Homeland Security and Governmental Affairs Committee",
      "systemCode": "ssga00",
      "type": "Standing"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/sres/BILLS-119sres699is.xml",
      "text": "III\n119th CONGRESS\n2d Session\nS. RES. 699\nIN THE SENATE OF THE UNITED STATES\nApril 29, 2026 Mr. Padilla submitted the following resolution; which was referred to the Committee on Homeland Security and Governmental Affairs\nRESOLUTION\nExpressing support for the recognition of April as National Language Access Month .\nThat the Senate\u2014\n**(1)**\nsupports the recognition of National Language Access Month ;\n**(2)**\naffirms the importance of meaningful language access in ensuring equitable participation in Federal programs and services;\n**(3)**\nencourages Federal agencies, States, local governments, and community organizations to promote awareness of language access rights and resources; and\n**(4)**\nencourages the people of the United States to observe National Language Access Month with appropriate ceremonies, programs, and activities.",
      "versionDate": "2026-04-29",
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
        "actionDate": "2026-03-30",
        "text": "Referred to the House Committee on Education and Workforce."
      },
      "number": "1148",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Expressing support for the recognition of April as \"National Language Access Month\".",
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
        "name": "Government Operations and Politics",
        "updateDate": "2026-05-15T22:43:59Z"
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
      "date": "2026-04-29",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/sres/BILLS-119sres699is.xml"
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
      "title": "A resolution expressing support for the recognition of April as \"National Language Access Month\".",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-05-02T03:33:34Z"
    },
    {
      "title": "A resolution expressing support for the recognition of April as \"National Language Access Month\".",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-04-30T10:56:22Z"
    }
  ]
}
```
