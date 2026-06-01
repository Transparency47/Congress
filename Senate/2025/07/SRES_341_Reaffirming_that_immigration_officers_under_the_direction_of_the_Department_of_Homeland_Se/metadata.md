# Metadata

- API URL: https://api.congress.gov/v3/bill/119/sres/341?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-resolution/341
- Title: A resolution reaffirming that immigration officers under the direction of the Department of Homeland Security are not authorized to arrest, detain, interrogate, or deport United States citizens and must implement stronger measures to prevent future wrongful enforcement actions against such citizens.
- Congress: 119
- Bill type: SRES
- Bill number: 341
- Origin chamber: Senate
- Introduced date: 2025-07-29
- Update date: 2025-12-17T11:56:23Z
- Update date including text: 2025-12-17T11:56:23Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-07-29: Introduced in Senate
- 2025-07-29 - IntroReferral: Introduced in Senate
- 2025-07-29 - IntroReferral: Referred to the Committee on the Judiciary. (text: CR S4829)
- Latest action: 2025-07-29: Introduced in Senate

## Actions

- 2025-07-29 - IntroReferral: Introduced in Senate
- 2025-07-29 - IntroReferral: Referred to the Committee on the Judiciary. (text: CR S4829)

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-07-29",
    "latestAction": {
      "actionDate": "2025-07-29",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-resolution/341",
    "number": "341",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Immigration"
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
    "title": "A resolution reaffirming that immigration officers under the direction of the Department of Homeland Security are not authorized to arrest, detain, interrogate, or deport United States citizens and must implement stronger measures to prevent future wrongful enforcement actions against such citizens.",
    "type": "SRES",
    "updateDate": "2025-12-17T11:56:23Z",
    "updateDateIncludingText": "2025-12-17T11:56:23Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-07-29",
      "committees": {
        "item": {
          "name": "Judiciary Committee",
          "systemCode": "ssju00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Referred to the Committee on the Judiciary. (text: CR S4829)",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-07-29",
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
          "date": "2025-07-29T21:16:37Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Judiciary Committee",
      "systemCode": "ssju00",
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
      "bioguideId": "S001150",
      "firstName": "Adam",
      "fullName": "Sen. Schiff, Adam B. [D-CA]",
      "isOriginalCosponsor": "False",
      "lastName": "Schiff",
      "middleName": "B.",
      "party": "D",
      "sponsorshipDate": "2025-12-16",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/sres/BILLS-119sres341is.xml",
      "text": "III\n119th CONGRESS\n1st Session\nS. RES. 341\nIN THE SENATE OF THE UNITED STATES\nJuly 29, 2025 Mr. Gallego submitted the following resolution; which was referred to the Committee on the Judiciary\nRESOLUTION\nReaffirming that immigration officers under the direction of the Department of Homeland Security are not authorized to arrest, detain, interrogate, or deport United States citizens and must implement stronger measures to prevent future wrongful enforcement actions against such citizens.\nThat the Senate reaffirms that U.S. Immigration and Customs Enforcement and other immigration officers under the direction of the Department of Homeland Security\u2014\n**(1)**\nare not authorized to arrest, detain, interrogate, or deport United States citizens; and\n**(2)**\nmust implement stronger measures to prevent future wrongful enforcement actions against such citizens.",
      "versionDate": "2025-07-29",
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
        "name": "Immigration",
        "updateDate": "2025-09-05T16:37:28Z"
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
      "date": "2025-07-29",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/sres/BILLS-119sres341is.xml"
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
      "title": "A resolution reaffirming that immigration officers under the direction of the Department of Homeland Security are not authorized to arrest, detain, interrogate, or deport United States citizens and must implement stronger measures to prevent future wrongful enforcement actions against such citizens.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-07-31T04:18:22Z"
    },
    {
      "title": "A resolution reaffirming that immigration officers under the direction of the Department of Homeland Security are not authorized to arrest, detain, interrogate, or deport United States citizens and must implement stronger measures to prevent future wrongful enforcement actions against such citizens.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-07-30T12:45:23Z"
    }
  ]
}
```
