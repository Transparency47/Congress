# Metadata

- API URL: https://api.congress.gov/v3/bill/119/sres/109?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-resolution/109
- Title: A resolution expressing the sense of the Senate that Russian President Vladimir Putin should immediately withdraw Russian forces from Ukraine.
- Congress: 119
- Bill type: SRES
- Bill number: 109
- Origin chamber: Senate
- Introduced date: 2025-03-05
- Update date: 2026-05-14T13:02:32Z
- Update date including text: 2026-05-14T13:02:32Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-03-05: Introduced in Senate
- 2025-03-05 - IntroReferral: Introduced in Senate
- 2025-03-05 - IntroReferral: Referred to the Committee on Foreign Relations. (text: CR S1583)
- Latest action: 2025-03-05: Introduced in Senate

## Actions

- 2025-03-05 - IntroReferral: Introduced in Senate
- 2025-03-05 - IntroReferral: Referred to the Committee on Foreign Relations. (text: CR S1583)

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-03-05",
    "latestAction": {
      "actionDate": "2025-03-05",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-resolution/109",
    "number": "109",
    "originChamber": "Senate",
    "policyArea": {
      "name": "International Affairs"
    },
    "sponsors": [
      {
        "bioguideId": "S000033",
        "district": "",
        "firstName": "Bernie",
        "fullName": "Sen. Sanders, Bernard [I-VT]",
        "lastName": "Sanders",
        "party": "I",
        "state": "VT"
      }
    ],
    "title": "A resolution expressing the sense of the Senate that Russian President Vladimir Putin should immediately withdraw Russian forces from Ukraine.",
    "type": "SRES",
    "updateDate": "2026-05-14T13:02:32Z",
    "updateDateIncludingText": "2026-05-14T13:02:32Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-03-05",
      "committees": {
        "item": {
          "name": "Foreign Relations Committee",
          "systemCode": "ssfr00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Referred to the Committee on Foreign Relations. (text: CR S1583)",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-03-05",
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
          "date": "2025-03-05T23:08:12Z",
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

## API Data: fullTexts

```json
{
  "fullTexts": [
    {
      "fetchError": null,
      "sourceFormat": "Formatted XML",
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/sres/BILLS-119sres109is.xml",
      "text": "III\n119th CONGRESS\n1st Session\nS. RES. 109\nIN THE SENATE OF THE UNITED STATES\nMarch 5, 2025 Mr. Sanders submitted the following resolution; which was referred to the Committee on Foreign Relations\nRESOLUTION\nExpressing the sense of the Senate that Russian President Vladimir Putin should immediately withdraw Russian forces from Ukraine.\nThat it is the sense of the Senate that the Russian Federation must\u2014\n**(1)**\nimmediately, completely, and unconditionally withdraw all of its military forces from any territory within the internationally recognized borders of Ukraine; and\n**(2)**\nimmediately cease its attacks against Ukraine.",
      "versionDate": "2025-03-05",
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
        "updateDate": "2025-05-15T00:08:19Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-03-05",
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
          "measure-id": "id119sres109",
          "measure-number": "109",
          "measure-type": "sres",
          "orig-publish-date": "2025-03-05",
          "originChamber": "SENATE",
          "update-date": "2026-05-14"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "SENATE",
            "summary-id": "id119sres109v00",
            "update-date": "2026-05-14"
          },
          "action-date": "2025-03-05",
          "action-desc": "Introduced in Senate",
          "summary-text": "<p>This resolution expresses the sense that Russian forces must immediately cease attacks on Ukraine and withdraw unconditionally.\u00a0</p>"
        },
        "title": "A resolution expressing the sense of the Senate that Russian President Vladimir Putin should immediately withdraw Russian forces from Ukraine."
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/sres/BILLSUM-119sres109.xml",
    "summary": {
      "actionDate": "2025-03-05",
      "actionDesc": "Introduced in Senate",
      "text": "<p>This resolution expresses the sense that Russian forces must immediately cease attacks on Ukraine and withdraw unconditionally.\u00a0</p>",
      "updateDate": "2026-05-14",
      "versionCode": "id119sres109"
    },
    "title": "A resolution expressing the sense of the Senate that Russian President Vladimir Putin should immediately withdraw Russian forces from Ukraine."
  },
  "summaries": [
    {
      "actionDate": "2025-03-05",
      "actionDesc": "Introduced in Senate",
      "text": "<p>This resolution expresses the sense that Russian forces must immediately cease attacks on Ukraine and withdraw unconditionally.\u00a0</p>",
      "updateDate": "2026-05-14",
      "versionCode": "id119sres109"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-03-05",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/sres/BILLS-119sres109is.xml"
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
      "title": "A resolution expressing the sense of the Senate that Russian President Vladimir Putin should immediately withdraw Russian forces from Ukraine.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-07T04:18:36Z"
    },
    {
      "title": "A resolution expressing the sense of the Senate that Russian President Vladimir Putin should immediately withdraw Russian forces from Ukraine.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-03-06T11:56:16Z"
    }
  ]
}
```
