# Metadata

- API URL: https://api.congress.gov/v3/bill/119/sres/625?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-resolution/625
- Title: A resolution designating February 2026 as "Hawaiian Language Month" or "Olelo Hawai'i Month".
- Congress: 119
- Bill type: SRES
- Bill number: 625
- Origin chamber: Senate
- Introduced date: 2026-03-02
- Update date: 2026-03-05T18:27:54Z
- Update date including text: 2026-03-05T18:27:54Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2026-03-02: Introduced in Senate
- 2026-03-02 - IntroReferral: Referred to the Committee on the Judiciary. (text: CR S735)
- 2026-03-02 - IntroReferral: Submitted in Senate
- Latest action: 2026-03-02: Submitted in Senate

## Actions

- 2026-03-02 - IntroReferral: Referred to the Committee on the Judiciary. (text: CR S735)
- 2026-03-02 - IntroReferral: Submitted in Senate

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-03-02",
    "latestAction": {
      "actionDate": "2026-03-02",
      "text": "Submitted in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-resolution/625",
    "number": "625",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Native Americans"
    },
    "sponsors": [
      {
        "bioguideId": "S001194",
        "district": "",
        "firstName": "Brian",
        "fullName": "Sen. Schatz, Brian [D-HI]",
        "lastName": "Schatz",
        "party": "D",
        "state": "HI"
      }
    ],
    "title": "A resolution designating February 2026 as \"Hawaiian Language Month\" or \"Olelo Hawai'i Month\".",
    "type": "SRES",
    "updateDate": "2026-03-05T18:27:54Z",
    "updateDateIncludingText": "2026-03-05T18:27:54Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-03-02",
      "committees": {
        "item": {
          "name": "Judiciary Committee",
          "systemCode": "ssju00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Referred to the Committee on the Judiciary. (text: CR S735)",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10025",
      "actionDate": "2026-03-02",
      "committees": {
        "item": {
          "name": "Judiciary Committee",
          "systemCode": "ssju00"
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
          "date": "2026-03-02T23:35:17Z",
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
      "bioguideId": "H001042",
      "firstName": "Mazie",
      "fullName": "Sen. Hirono, Mazie K. [D-HI]",
      "isOriginalCosponsor": "True",
      "lastName": "Hirono",
      "middleName": "K.",
      "party": "D",
      "sponsorshipDate": "2026-03-02",
      "state": "HI"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/sres/BILLS-119sres625is.xml",
      "text": "III\n119th CONGRESS\n2d Session\nS. RES. 625\nIN THE SENATE OF THE UNITED STATES\nMarch 2, 2026 Mr. Schatz (for himself and Ms. Hirono ) submitted the following resolution; which was referred to the Committee on the Judiciary\nRESOLUTION\nDesignating February 2026 as Hawaiian Language Month or \u2018\u014clelo Hawai\u2018i Month .\nThat the Senate\u2014\n**(1)**\ndesignates February 2026 as Hawaiian Language Month or \u2018\u014clelo Hawai\u2018i Month ;\n**(2)**\ncommits to preserving, protecting, and promoting the use, practice, and development of \u2018\u014clelo Hawai\u2018i in alignment with the Native American Languages Act ( 25 U.S.C. 2901 et seq. ); and\n**(3)**\nurges the people of the United States and interested groups to celebrate \u2018\u014clelo Hawai\u2018i Month with appropriate activities and programs to demonstrate support for \u2018\u014clelo Hawai\u2018i.",
      "versionDate": "2026-03-02",
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
        "name": "Native Americans",
        "updateDate": "2026-03-05T18:27:54Z"
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
      "date": "2026-03-02",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/sres/BILLS-119sres625is.xml"
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
      "title": "A resolution designating February 2026 as \"Hawaiian Language Month\" or \"Olelo Hawai'i Month\".",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-03-04T03:03:22Z"
    },
    {
      "title": "A resolution designating February 2026 as \"Hawaiian Language Month\" or \"Olelo Hawai'i Month\".",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-03-03T11:56:22Z"
    }
  ]
}
```
