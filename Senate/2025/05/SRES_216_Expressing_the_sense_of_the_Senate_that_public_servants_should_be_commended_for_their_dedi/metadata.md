# Metadata

- API URL: https://api.congress.gov/v3/bill/119/sres/216?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/sres/216
- Title: A resolution expressing the sense of the Senate that public servants should be commended for their dedication and continued service to the United States during Public Service Recognition Week and throughout the year.
- Congress: 119
- Bill type: SRES
- Bill number: 216
- Origin chamber: Senate
- Introduced date: 2025-05-12
- Update date: 2025-06-11T14:51:49Z
- Update date including text: 2025-06-11T14:51:49Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-05-12: Introduced in Senate
- 2025-05-12 - IntroReferral: Introduced in Senate
- 2025-05-12 - IntroReferral: Referred to the Committee on Homeland Security and Governmental Affairs. (text: CR S2865)
- Latest action: 2025-05-12: Introduced in Senate

## Actions

- 2025-05-12 - IntroReferral: Introduced in Senate
- 2025-05-12 - IntroReferral: Referred to the Committee on Homeland Security and Governmental Affairs. (text: CR S2865)

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-05-12",
    "latestAction": {
      "actionDate": "2025-05-12",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/sres/216",
    "number": "216",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Government Operations and Politics"
    },
    "sponsors": [
      {
        "bioguideId": "L000575",
        "district": "",
        "firstName": "James",
        "fullName": "Sen. Lankford, James [R-OK]",
        "lastName": "Lankford",
        "party": "R",
        "state": "OK"
      }
    ],
    "title": "A resolution expressing the sense of the Senate that public servants should be commended for their dedication and continued service to the United States during Public Service Recognition Week and throughout the year.",
    "type": "SRES",
    "updateDate": "2025-06-11T14:51:49Z",
    "updateDateIncludingText": "2025-06-11T14:51:49Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-05-12",
      "committees": {
        "item": {
          "name": "Homeland Security and Governmental Affairs Committee",
          "systemCode": "ssga00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Referred to the Committee on Homeland Security and Governmental Affairs. (text: CR S2865)",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-05-12",
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
          "date": "2025-05-12T22:59:20Z",
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

## API Data: cosponsors

```json
{
  "cosponsors": [
    {
      "bioguideId": "F000479",
      "firstName": "John",
      "fullName": "Sen. Fetterman, John [D-PA]",
      "isOriginalCosponsor": "True",
      "lastName": "Fetterman",
      "middleName": "K.",
      "party": "D",
      "sponsorshipDate": "2025-05-12",
      "state": "PA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/sres/BILLS-119sres216is.xml",
      "text": "III\n119th CONGRESS\n1st Session\nS. RES. 216\nIN THE SENATE OF THE UNITED STATES\nMay 12, 2025 Mr. Lankford (for himself and Mr. Fetterman ) submitted the following resolution; which was referred to the Committee on Homeland Security and Governmental Affairs\nRESOLUTION\nExpressing the sense of the Senate that public servants should be commended for their dedication and continued service to the United States during Public Service Recognition Week and throughout the year.\nThat the Senate\u2014\n**(1)**\nsupports the designation of the week of May 4 through May 10, 2025, as Public Service Recognition Week ;\n**(2)**\ncommends public servants during Public Service Recognition Week for their outstanding contributions to the United States throughout the year;\n**(3)**\nsalutes government employees and members of the uniformed services for their unyielding dedication to, and enthusiasm for, the public whom they serve;\n**(4)**\nhonors government employees and members of the uniformed services who have given their lives in service to their communities and the United States;\n**(5)**\nencourages efforts to promote and celebrate public service careers at every level of government;\n**(6)**\nexpresses gratitude to the public servants who have selflessly answered the call to serve the United States, their State, and their communities; and\n**(7)**\nexpresses gratitude to the Federal workers who have selflessly answered the call to serve the United States.",
      "versionDate": "2025-05-12",
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
        "name": "Government Operations and Politics",
        "updateDate": "2025-06-11T14:51:49Z"
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
      "date": "2025-05-12",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/sres/BILLS-119sres216is.xml"
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
      "title": "A resolution expressing the sense of the Senate that public servants should be commended for their dedication and continued service to the United States during Public Service Recognition Week and throughout the year.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-05-14T04:18:50Z"
    },
    {
      "title": "A resolution expressing the sense of the Senate that public servants should be commended for their dedication and continued service to the United States during Public Service Recognition Week and throughout the year.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-05-13T10:56:18Z"
    }
  ]
}
```
