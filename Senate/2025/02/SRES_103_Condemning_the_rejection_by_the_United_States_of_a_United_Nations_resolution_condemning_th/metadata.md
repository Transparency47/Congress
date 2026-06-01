# Metadata

- API URL: https://api.congress.gov/v3/bill/119/sres/103?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/sres/103
- Title: A resolution condemning the rejection by the United States of a United Nations resolution condemning the illegal invasion of Ukraine by the Russian Federation.
- Congress: 119
- Bill type: SRES
- Bill number: 103
- Origin chamber: Senate
- Introduced date: 2025-02-27
- Update date: 2025-05-06T15:36:53Z
- Update date including text: 2025-05-06T15:36:53Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-02-27: Introduced in Senate
- 2025-02-27 - IntroReferral: Introduced in Senate
- 2025-02-27 - IntroReferral: Referred to the Committee on Foreign Relations. (text: CR S1433)
- Latest action: 2025-02-27: Introduced in Senate

## Actions

- 2025-02-27 - IntroReferral: Introduced in Senate
- 2025-02-27 - IntroReferral: Referred to the Committee on Foreign Relations. (text: CR S1433)

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-02-27",
    "latestAction": {
      "actionDate": "2025-02-27",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/sres/103",
    "number": "103",
    "originChamber": "Senate",
    "policyArea": {
      "name": "International Affairs"
    },
    "sponsors": [
      {
        "bioguideId": "G000574",
        "district": "",
        "firstName": "Ruben",
        "fullName": "Sen. Gallego, Ruben [D-AZ]",
        "lastName": "Gallego",
        "party": "D",
        "state": "AZ"
      }
    ],
    "title": "A resolution condemning the rejection by the United States of a United Nations resolution condemning the illegal invasion of Ukraine by the Russian Federation.",
    "type": "SRES",
    "updateDate": "2025-05-06T15:36:53Z",
    "updateDateIncludingText": "2025-05-06T15:36:53Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-02-27",
      "committees": {
        "item": {
          "name": "Foreign Relations Committee",
          "systemCode": "ssfr00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Referred to the Committee on Foreign Relations. (text: CR S1433)",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-02-27",
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
          "date": "2025-02-27T18:49:27Z",
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
      "bioguideId": "D000563",
      "firstName": "Richard",
      "fullName": "Sen. Durbin, Richard J. [D-IL]",
      "isOriginalCosponsor": "True",
      "lastName": "Durbin",
      "middleName": "J.",
      "party": "D",
      "sponsorshipDate": "2025-02-27",
      "state": "IL"
    },
    {
      "bioguideId": "P000145",
      "firstName": "Alex",
      "fullName": "Sen. Padilla, Alex [D-CA]",
      "isOriginalCosponsor": "True",
      "lastName": "Padilla",
      "party": "D",
      "sponsorshipDate": "2025-02-27",
      "state": "CA"
    },
    {
      "bioguideId": "B001267",
      "firstName": "Michael",
      "fullName": "Sen. Bennet, Michael F. [D-CO]",
      "isOriginalCosponsor": "True",
      "lastName": "Bennet",
      "party": "D",
      "sponsorshipDate": "2025-02-27",
      "state": "CO"
    },
    {
      "bioguideId": "S001150",
      "firstName": "Adam",
      "fullName": "Sen. Schiff, Adam B. [D-CA]",
      "isOriginalCosponsor": "True",
      "lastName": "Schiff",
      "middleName": "B.",
      "party": "D",
      "sponsorshipDate": "2025-02-27",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/sres/BILLS-119sres103is.xml",
      "text": "III\n119th CONGRESS\n1st Session\nS. RES. 103\nIN THE SENATE OF THE UNITED STATES\nFebruary 27, 2025 Mr. Gallego (for himself, Mr. Durbin , Mr. Padilla , Mr. Bennet , and Mr. Schiff ) submitted the following resolution; which was referred to the Committee on Foreign Relations\nRESOLUTION\nCondemning the rejection by the United States of a United Nations resolution condemning the illegal invasion of Ukraine by the Russian Federation.\nThat the Senate condemns the rejection by the United States of United Nations General Assembly Resolution A/ES\u201311/L.10 (2025), titled Advancing a comprehensive, just and lasting peace in Ukraine , condemning the illegal invasion of Ukraine by the Russian Federation.",
      "versionDate": "2025-02-27",
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
        "updateDate": "2025-05-06T15:36:53Z"
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
      "date": "2025-02-27",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/sres/BILLS-119sres103is.xml"
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
      "title": "A resolution condemning the rejection by the United States of a United Nations resolution condemning the illegal invasion of Ukraine by the Russian Federation.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-01T04:33:24Z"
    },
    {
      "title": "A resolution condemning the rejection by the United States of a United Nations resolution condemning the illegal invasion of Ukraine by the Russian Federation.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-02-28T11:56:29Z"
    }
  ]
}
```
