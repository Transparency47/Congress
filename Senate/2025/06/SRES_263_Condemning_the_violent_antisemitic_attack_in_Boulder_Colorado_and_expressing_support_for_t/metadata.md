# Metadata

- API URL: https://api.congress.gov/v3/bill/119/sres/263?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-resolution/263
- Title: A resolution condemning the violent antisemitic attack in Boulder, Colorado, and expressing support for the survivors and their families.
- Congress: 119
- Bill type: SRES
- Bill number: 263
- Origin chamber: Senate
- Introduced date: 2025-06-04
- Update date: 2025-12-06T06:57:20Z
- Update date including text: 2025-12-06T06:57:20Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

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
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-resolution/263",
    "number": "263",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Crime and Law Enforcement"
    },
    "sponsors": [
      {
        "bioguideId": "B001267",
        "district": "",
        "firstName": "Michael",
        "fullName": "Sen. Bennet, Michael F. [D-CO]",
        "lastName": "Bennet",
        "party": "D",
        "state": "CO"
      }
    ],
    "title": "A resolution condemning the violent antisemitic attack in Boulder, Colorado, and expressing support for the survivors and their families.",
    "type": "SRES",
    "updateDate": "2025-12-06T06:57:20Z",
    "updateDateIncludingText": "2025-12-06T06:57:20Z"
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
          "date": "2025-06-04T23:22:23Z",
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
      "bioguideId": "H000273",
      "firstName": "John",
      "fullName": "Sen. Hickenlooper, John W. [D-CO]",
      "isOriginalCosponsor": "True",
      "lastName": "Hickenlooper",
      "middleName": "W.",
      "party": "D",
      "sponsorshipDate": "2025-06-04",
      "state": "CO"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/sres/BILLS-119sres263is.xml",
      "text": "III\n119th CONGRESS\n1st Session\nS. RES. 263\nIN THE SENATE OF THE UNITED STATES\nJune 4, 2025 Mr. Bennet (for himself and Mr. Hickenlooper ) submitted the following resolution; which was referred to the Committee on the Judiciary\nRESOLUTION\nCondemning the violent antisemitic attack in Boulder, Colorado, and expressing support for the survivors and their families.\nThat the Senate\u2014\n**(1)**\ncondemns the antisemitic attack that occurred on June 1, 2025, in Boulder, Colorado;\n**(2)**\nexpresses solidarity with the survivors and their families;\n**(3)**\nrecognizes the resilience of the Boulder community and commends their continued efforts to promote peace, safety, and inclusion;\n**(4)**\ncalls for continued vigilance and Federal resources to counter rising antisemitism, investigate hate crimes, and support targeted communities;\n**(5)**\nstands with the Jewish community, for freedom of speech and religion and against fear; and\n**(6)**\naffirms that hate and violence have no place in the United States and that all people, regardless of faith or belief, deserve to live free from fear and persecution.",
      "versionDate": "2025-06-04",
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
        "actionDate": "2025-06-11",
        "text": "Sponsor introductory remarks on measure. (CR H2632)"
      },
      "number": "476",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Condemning the violent antisemitic attack in Boulder, Colorado, and expressing support for the survivors and their families.",
      "type": "HRES"
    },
    {
      "congress": "119",
      "latestAction": {
        "actionDate": "2025-06-12",
        "text": "Submitted in the Senate, considered, and agreed to without amendment and with a preamble by Unanimous Consent. (consideration: CR S3396; text: CR S3394)"
      },
      "number": "278",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "A resolution condemning the violent antisemitic attack in Boulder, Colorado, and expressing support for the survivors and their families.",
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
      "legislativeSubjects": {
        "item": [
          {
            "name": "Colorado",
            "updateDate": "2025-07-22T19:37:52Z"
          },
          {
            "name": "Crime victims",
            "updateDate": "2025-07-22T19:37:52Z"
          },
          {
            "name": "Racial and ethnic relations",
            "updateDate": "2025-07-22T19:37:52Z"
          },
          {
            "name": "Religion",
            "updateDate": "2025-07-22T19:37:52Z"
          }
        ]
      },
      "policyArea": {
        "name": "Crime and Law Enforcement",
        "updateDate": "2025-07-18T13:00:14Z"
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
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/sres/BILLS-119sres263is.xml"
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
      "title": "A resolution condemning the violent antisemitic attack in Boulder, Colorado, and expressing support for the survivors and their families.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-06-07T04:18:19Z"
    },
    {
      "title": "A resolution condemning the violent antisemitic attack in Boulder, Colorado, and expressing support for the survivors and their families.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-06-05T10:56:22Z"
    }
  ]
}
```
