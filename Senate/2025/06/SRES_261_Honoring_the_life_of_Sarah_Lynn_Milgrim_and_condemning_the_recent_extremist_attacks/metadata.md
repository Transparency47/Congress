# Metadata

- API URL: https://api.congress.gov/v3/bill/119/sres/261?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/sres/261
- Title: A resolution honoring the life of Sarah Lynn Milgrim and condemning the recent extremist attacks.
- Congress: 119
- Bill type: SRES
- Bill number: 261
- Origin chamber: Senate
- Introduced date: 2025-06-04
- Update date: 2025-07-21T19:32:26Z
- Update date including text: 2025-07-21T19:32:26Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-06-04: Introduced in Senate
- 2025-06-04 - IntroReferral: Introduced in Senate
- 2025-06-04 - IntroReferral: Referred to the Committee on the Judiciary. (text: CR S3236)
- Latest action: 2025-06-04: Introduced in Senate

## Actions

- 2025-06-04 - IntroReferral: Introduced in Senate
- 2025-06-04 - IntroReferral: Referred to the Committee on the Judiciary. (text: CR S3236)

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-06-04",
    "latestAction": {
      "actionDate": "2025-06-04",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/sres/261",
    "number": "261",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Crime and Law Enforcement"
    },
    "sponsors": [
      {
        "bioguideId": "M001198",
        "district": "",
        "firstName": "Roger",
        "fullName": "Sen. Marshall, Roger [R-KS]",
        "lastName": "Marshall",
        "party": "R",
        "state": "KS"
      }
    ],
    "title": "A resolution honoring the life of Sarah Lynn Milgrim and condemning the recent extremist attacks.",
    "type": "SRES",
    "updateDate": "2025-07-21T19:32:26Z",
    "updateDateIncludingText": "2025-07-21T19:32:26Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-06-04",
      "committees": {
        "item": {
          "name": "Judiciary Committee",
          "systemCode": "ssju00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Referred to the Committee on the Judiciary. (text: CR S3236)",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-06-04",
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
          "date": "2025-06-04T22:41:17Z",
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
      "bioguideId": "M000934",
      "firstName": "Jerry",
      "fullName": "Sen. Moran, Jerry [R-KS]",
      "isOriginalCosponsor": "True",
      "lastName": "Moran",
      "party": "R",
      "sponsorshipDate": "2025-06-04",
      "state": "KS"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/sres/BILLS-119sres261is.xml",
      "text": "III\n119th CONGRESS\n1st Session\nS. RES. 261\nIN THE SENATE OF THE UNITED STATES\nJune 4, 2025 Mr. Marshall (for himself and Mr. Moran ) submitted the following resolution; which was referred to the Committee on the Judiciary\nRESOLUTION\nHonoring the life of Sarah Lynn Milgrim and condemning the recent extremist attacks.\nThat the Senate\u2014\n**(1)**\nstrongly condemns violence targeted at religious groups;\n**(2)**\nremembers the life of Sarah Milgrim and celebrates her work;\n**(3)**\ndenounces the senseless violence that resulted in the deaths of Sarah Milgrim and Yaron Lischinsky; and\n**(4)**\nsupports the full prosecution of the individual who committed this extremist attack.",
      "versionDate": "2025-06-04",
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
        "name": "Crime and Law Enforcement",
        "updateDate": "2025-07-18T13:01:41Z"
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
      "date": "2025-06-04",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/sres/BILLS-119sres261is.xml"
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
      "title": "A resolution honoring the life of Sarah Lynn Milgrim and condemning the recent extremist attacks.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-06-07T04:18:17Z"
    },
    {
      "title": "A resolution honoring the life of Sarah Lynn Milgrim and condemning the recent extremist attacks.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-06-05T10:56:23Z"
    }
  ]
}
```
