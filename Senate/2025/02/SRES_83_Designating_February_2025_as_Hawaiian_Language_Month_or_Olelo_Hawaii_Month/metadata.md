# Metadata

- API URL: https://api.congress.gov/v3/bill/119/sres/83?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-resolution/83
- Title: A resolution designating February 2025 as "Hawaiian Language Month" or "'Ōlelo Hawai'i Month".
- Congress: 119
- Bill type: SRES
- Bill number: 83
- Origin chamber: Senate
- Introduced date: 2025-02-19
- Update date: 2026-03-05T18:26:09Z
- Update date including text: 2026-03-05T18:26:09Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-02-19: Introduced in Senate
- 2025-02-19 - IntroReferral: Introduced in Senate
- 2025-02-19 - IntroReferral: Referred to the Committee on the Judiciary. (text: CR S1042)
- Latest action: 2025-02-19: Introduced in Senate

## Actions

- 2025-02-19 - IntroReferral: Introduced in Senate
- 2025-02-19 - IntroReferral: Referred to the Committee on the Judiciary. (text: CR S1042)

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-02-19",
    "latestAction": {
      "actionDate": "2025-02-19",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-resolution/83",
    "number": "83",
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
    "title": "A resolution designating February 2025 as \"Hawaiian Language Month\" or \"'\u014clelo Hawai'i Month\".",
    "type": "SRES",
    "updateDate": "2026-03-05T18:26:09Z",
    "updateDateIncludingText": "2026-03-05T18:26:09Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-02-19",
      "committees": {
        "item": {
          "name": "Judiciary Committee",
          "systemCode": "ssju00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Referred to the Committee on the Judiciary. (text: CR S1042)",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-02-19",
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
          "date": "2025-02-19T19:24:09Z",
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
      "sponsorshipDate": "2025-02-19",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/sres/BILLS-119sres83is.xml",
      "text": "III\n119th CONGRESS\n1st Session\nS. RES. 83\nIN THE SENATE OF THE UNITED STATES\nFebruary 19, 2025 Mr. Schatz (for himself and Ms. Hirono ) submitted the following resolution; which was referred to the Committee on the Judiciary\nRESOLUTION\nDesignating February 2025 as Hawaiian Language Month or \u2018\u014clelo Hawai\u2018i Month .\nThat the Senate\u2014\n**(1)**\ndesignates February 2025 as Hawaiian Language Month or \u2018\u014clelo Hawai\u2018i Month ;\n**(2)**\ncommits to preserving, protecting, and promoting the use, practice, and development of \u2018\u014clelo Hawai\u2018i in alignment with the Native American Languages Act ( 25 U.S.C. 2901 et seq. ); and\n**(3)**\nurges the people of the United States and interested groups to celebrate \u2018\u014clelo Hawai\u2018i Month with appropriate activities and programs to demonstrate support for \u2018\u014clelo Hawai\u2018i.",
      "versionDate": "2025-02-19",
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
        "actionDate": "2025-02-13",
        "text": "Referred to the House Committee on Education and Workforce."
      },
      "number": "136",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Expressing support for the designation of February 2025 as \"Hawaiian Language Month\" or \"'\u014clelo Hawai'i Month\".",
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
        "name": "Native Americans",
        "updateDate": "2025-06-24T18:22:54Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-02-19",
    "originChamber": "Senate",
    "payload": {
      "dublinCore": {
        "contributor": "Congressional Research Service, Library of Congress",
        "description": "This file contains bill summaries for federal legislation. A bill summary describes the most significant provisions of a piece of legislation and details the effects the legislative text may have on current law and federal programs. Bill summaries are authored by the Congressional Research Service (CRS) of the Library of Congress. As stated in Public Law 91-510 (2 USC 166 (d)(6)), one of the duties of CRS is \"to prepare summaries and digests of bills and resolutions of a public general nature introduced in the Senate or House of Representatives\". For more information, refer to the User Guide that accompanies this file.",
        "format": "text/xml",
        "language": "EN",
        "rights": "Pursuant to Title 17 Section 105 of the United States Code, this file is not subject to copyright protection and is in the public domain."
      },
      "item": {
        "@attributes": {
          "congress": "119",
          "measure-id": "id119sres83",
          "measure-number": "83",
          "measure-type": "sres",
          "orig-publish-date": "2025-02-19",
          "originChamber": "SENATE",
          "update-date": "2025-06-24"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "SENATE",
            "summary-id": "id119sres83v00",
            "update-date": "2025-06-24"
          },
          "action-date": "2025-02-19",
          "action-desc": "Introduced in Senate",
          "summary-text": "<p>This resolution designates February 2025 as Hawaiian Language Month or '\u014clelo Hawai'i Month.</p>"
        },
        "title": "A resolution designating February 2025 as \"Hawaiian Language Month\" or \"'Olelo Hawai'i Month\"."
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/sres/BILLSUM-119sres83.xml",
    "summary": {
      "actionDate": "2025-02-19",
      "actionDesc": "Introduced in Senate",
      "text": "<p>This resolution designates February 2025 as Hawaiian Language Month or '\u014clelo Hawai'i Month.</p>",
      "updateDate": "2025-06-24",
      "versionCode": "id119sres83"
    },
    "title": "A resolution designating February 2025 as \"Hawaiian Language Month\" or \"'Olelo Hawai'i Month\"."
  },
  "summaries": [
    {
      "actionDate": "2025-02-19",
      "actionDesc": "Introduced in Senate",
      "text": "<p>This resolution designates February 2025 as Hawaiian Language Month or '\u014clelo Hawai'i Month.</p>",
      "updateDate": "2025-06-24",
      "versionCode": "id119sres83"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-02-19",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/sres/BILLS-119sres83is.xml"
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
      "title": "A resolution designating February 2025 as \"Hawaiian Language Month\" or \"'\u014clelo Hawai'i Month\".",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-01-26T22:18:40Z"
    },
    {
      "title": "A resolution designating February 2025 as \"Hawaiian Language Month\" or \"'\u014clelo Hawai'i Month\".",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-01-26T22:18:33Z"
    }
  ]
}
```
