# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hres/1126?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-resolution/1126
- Title: Recognizing the role of Mae Krier and her contributions as she celebrates her 100th birthday.
- Congress: 119
- Bill type: HRES
- Bill number: 1126
- Origin chamber: House
- Introduced date: 2026-03-19
- Update date: 2026-04-07T14:13:28Z
- Update date including text: 2026-04-07T14:13:28Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, subjects, summaries, text, titles

## Timeline

- 2026-03-19: Introduced in House
- 2026-03-19 - IntroReferral: Referred to the House Committee on Education and Workforce.
- 2026-03-19 - IntroReferral: Submitted in House
- 2026-03-19 - IntroReferral: Submitted in House
- Latest action: 2026-03-19: Submitted in House

## Actions

- 2026-03-19 - IntroReferral: Referred to the House Committee on Education and Workforce.
- 2026-03-19 - IntroReferral: Submitted in House
- 2026-03-19 - IntroReferral: Submitted in House

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-03-19",
    "latestAction": {
      "actionDate": "2026-03-19",
      "text": "Submitted in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-resolution/1126",
    "number": "1126",
    "originChamber": "House",
    "policyArea": {
      "name": "Transportation and Public Works"
    },
    "sponsors": [
      {
        "bioguideId": "F000466",
        "district": "1",
        "firstName": "Brian",
        "fullName": "Rep. Fitzpatrick, Brian K. [R-PA-1]",
        "lastName": "Fitzpatrick",
        "party": "R",
        "state": "PA"
      }
    ],
    "title": "Recognizing the role of Mae Krier and her contributions as she celebrates her 100th birthday.",
    "type": "HRES",
    "updateDate": "2026-04-07T14:13:28Z",
    "updateDateIncludingText": "2026-04-07T14:13:28Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2026-03-19",
      "committees": {
        "item": {
          "name": "Education and Workforce Committee",
          "systemCode": "hsed00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Education and Workforce.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2026-03-19",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Submitted in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1025",
      "actionDate": "2026-03-19",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Submitted in House",
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
          "date": "2026-03-19T13:02:20Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Education and Workforce Committee",
      "systemCode": "hsed00",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hres/BILLS-119hres1126ih.xml",
      "text": "IV\n119th CONGRESS\n2d Session\nH. RES. 1126\nIN THE HOUSE OF REPRESENTATIVES\nMarch 19, 2026 Mr. Fitzpatrick submitted the following resolution; which was referred to the Committee on Education and Workforce\nRESOLUTION\nRecognizing the role of Mae Krier and her contributions as she celebrates her 100th birthday.\nThat the House of Representatives recognizes and thanks Mae Krier on her 100th birthday for her contributions to the Nation as a Rosie the Riveter and trailblazer.",
      "versionDate": "2026-03-19",
      "versionType": "IH"
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
        "name": "Transportation and Public Works",
        "updateDate": "2026-03-27T20:22:40Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2026-03-19",
    "originChamber": "House",
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
          "measure-id": "id119hres1126",
          "measure-number": "1126",
          "measure-type": "hres",
          "orig-publish-date": "2026-03-19",
          "originChamber": "HOUSE",
          "update-date": "2026-04-07"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hres1126v00",
            "update-date": "2026-04-07"
          },
          "action-date": "2026-03-19",
          "action-desc": "Introduced in House",
          "summary-text": "<p>This resolution recognizes and thanks Mae Krier on her 100<sup>th</sup> birthday for her contributions to the United States as a trailblazer and a Rosie the Riveter (a term used to describe women who joined the workforce during World War II).</p>"
        },
        "title": "Recognizing the role of Mae Krier and her contributions as she celebrates her 100th birthday."
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hres/BILLSUM-119hres1126.xml",
    "summary": {
      "actionDate": "2026-03-19",
      "actionDesc": "Introduced in House",
      "text": "<p>This resolution recognizes and thanks Mae Krier on her 100<sup>th</sup> birthday for her contributions to the United States as a trailblazer and a Rosie the Riveter (a term used to describe women who joined the workforce during World War II).</p>",
      "updateDate": "2026-04-07",
      "versionCode": "id119hres1126"
    },
    "title": "Recognizing the role of Mae Krier and her contributions as she celebrates her 100th birthday."
  },
  "summaries": [
    {
      "actionDate": "2026-03-19",
      "actionDesc": "Introduced in House",
      "text": "<p>This resolution recognizes and thanks Mae Krier on her 100<sup>th</sup> birthday for her contributions to the United States as a trailblazer and a Rosie the Riveter (a term used to describe women who joined the workforce during World War II).</p>",
      "updateDate": "2026-04-07",
      "versionCode": "id119hres1126"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2026-03-19",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hres/BILLS-119hres1126ih.xml"
        }
      ],
      "type": "IH"
    }
  ]
}
```

## API Data: titles

```json
{
  "titles": [
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Recognizing the role of Mae Krier and her contributions as she celebrates her 100th birthday.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-03-20T08:18:20Z"
    },
    {
      "title": "Recognizing the role of Mae Krier and her contributions as she celebrates her 100th birthday.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-03-20T08:07:01Z"
    }
  ]
}
```
