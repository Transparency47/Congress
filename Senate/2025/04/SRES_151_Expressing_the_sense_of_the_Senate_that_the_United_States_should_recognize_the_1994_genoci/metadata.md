# Metadata

- API URL: https://api.congress.gov/v3/bill/119/sres/151?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/sres/151
- Title: A resolution expressing the sense of the Senate that the United States should recognize the 1994 genocide in Rwanda as "the genocide against the Tutsi in Rwanda".
- Congress: 119
- Bill type: SRES
- Bill number: 151
- Origin chamber: Senate
- Introduced date: 2025-04-01
- Update date: 2025-05-23T13:28:51Z
- Update date including text: 2025-05-23T13:28:51Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-04-01: Introduced in Senate
- 2025-04-01 - IntroReferral: Introduced in Senate
- 2025-04-01 - IntroReferral: Referred to the Committee on Foreign Relations. (text: CR S2097-2098)
- Latest action: 2025-04-01: Introduced in Senate

## Actions

- 2025-04-01 - IntroReferral: Introduced in Senate
- 2025-04-01 - IntroReferral: Referred to the Committee on Foreign Relations. (text: CR S2097-2098)

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-04-01",
    "latestAction": {
      "actionDate": "2025-04-01",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/sres/151",
    "number": "151",
    "originChamber": "Senate",
    "policyArea": {
      "name": "International Affairs"
    },
    "sponsors": [
      {
        "bioguideId": "R000605",
        "district": "",
        "firstName": "Mike",
        "fullName": "Sen. Rounds, Mike [R-SD]",
        "lastName": "Rounds",
        "party": "R",
        "state": "SD"
      }
    ],
    "title": "A resolution expressing the sense of the Senate that the United States should recognize the 1994 genocide in Rwanda as \"the genocide against the Tutsi in Rwanda\".",
    "type": "SRES",
    "updateDate": "2025-05-23T13:28:51Z",
    "updateDateIncludingText": "2025-05-23T13:28:51Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-04-01",
      "committees": {
        "item": {
          "name": "Foreign Relations Committee",
          "systemCode": "ssfr00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Referred to the Committee on Foreign Relations. (text: CR S2097-2098)",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-04-01",
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
          "date": "2025-04-01T21:38:39Z",
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
      "bioguideId": "C001088",
      "firstName": "Christopher",
      "fullName": "Sen. Coons, Christopher A. [D-DE]",
      "isOriginalCosponsor": "True",
      "lastName": "Coons",
      "middleName": "A.",
      "party": "D",
      "sponsorshipDate": "2025-04-01",
      "state": "DE"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/sres/BILLS-119sres151is.xml",
      "text": "III\n119th CONGRESS\n1st Session\nS. RES. 151\nIN THE SENATE OF THE UNITED STATES\nApril 1 (legislative day, March 31), 2025 Mr. Rounds (for himself and Mr. Coons ) submitted the following resolution; which was referred to the Committee on Foreign Relations\nRESOLUTION\nExpressing the sense of the Senate that the United States should recognize the 1994 genocide in Rwanda as the genocide against the Tutsi in Rwanda .\nThat it is the sense of the Senate that\u2014\n**(1)**\nthe United States should recognize the 1994 genocide in Rwanda as the genocide against the Tutsi in Rwanda ;\n**(2)**\nthe Secretary of State should publicly affirm that terminology; and\n**(3)**\nother types of atrocities occurred alongside the genocide against the Tutsi, and the history of the genocide should clearly affirm the other experiences of mass violence against Rwandans during the same period, including the killings and other violence experienced by Hutus and the Indigenous Twa community, perpetrated by Hutu extremist militias.",
      "versionDate": "2025-04-01",
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
        "updateDate": "2025-05-23T13:28:51Z"
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
      "date": "2025-04-01",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/sres/BILLS-119sres151is.xml"
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
      "title": "A resolution expressing the sense of the Senate that the United States should recognize the 1994 genocide in Rwanda as \"the genocide against the Tutsi in Rwanda\".",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-04-03T13:33:31Z"
    },
    {
      "title": "A resolution expressing the sense of the Senate that the United States should recognize the 1994 genocide in Rwanda as \"the genocide against the Tutsi in Rwanda\".",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-04-02T10:56:20Z"
    }
  ]
}
```
