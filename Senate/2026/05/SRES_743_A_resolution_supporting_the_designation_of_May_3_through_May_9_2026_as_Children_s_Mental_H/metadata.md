# Metadata

- API URL: https://api.congress.gov/v3/bill/119/sres/743?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-resolution/743
- Title: A resolution supporting the designation of May 3 through May 9, 2026, as "Children's Mental Health Awareness Week".
- Congress: 119
- Bill type: SRES
- Bill number: 743
- Origin chamber: Senate
- Introduced date: 2026-05-20
- Update date: 2026-05-22T19:45:19Z
- Update date including text: 2026-05-22T19:45:19Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, text, titles

## Timeline

- 2026-05-20: Introduced in Senate
- 2026-05-20 - IntroReferral: Referred to the Committee on Health, Education, Labor, and Pensions. (text: CR S2419-2420)
- 2026-05-20 - IntroReferral: Submitted in Senate
- Latest action: 2026-05-20: Submitted in Senate

## Actions

- 2026-05-20 - IntroReferral: Referred to the Committee on Health, Education, Labor, and Pensions. (text: CR S2419-2420)
- 2026-05-20 - IntroReferral: Submitted in Senate

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-05-20",
    "latestAction": {
      "actionDate": "2026-05-20",
      "text": "Submitted in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-resolution/743",
    "number": "743",
    "originChamber": "Senate",
    "policyArea": {},
    "sponsors": [
      {
        "bioguideId": "H001104",
        "district": "",
        "firstName": "Jon",
        "fullName": "Sen. Husted, Jon [R-OH]",
        "lastName": "Husted",
        "party": "R",
        "state": "OH"
      }
    ],
    "title": "A resolution supporting the designation of May 3 through May 9, 2026, as \"Children's Mental Health Awareness Week\".",
    "type": "SRES",
    "updateDate": "2026-05-22T19:45:19Z",
    "updateDateIncludingText": "2026-05-22T19:45:19Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-05-20",
      "committees": {
        "item": {
          "name": "Health, Education, Labor, and Pensions Committee",
          "systemCode": "sshr00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Referred to the Committee on Health, Education, Labor, and Pensions. (text: CR S2419-2420)",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10025",
      "actionDate": "2026-05-20",
      "committees": {
        "item": {
          "name": "Health, Education, Labor, and Pensions Committee",
          "systemCode": "sshr00"
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
          "date": "2026-05-20T17:59:42Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Health, Education, Labor, and Pensions Committee",
      "systemCode": "sshr00",
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
      "sponsorshipDate": "2026-05-20",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/sres/BILLS-119sres743is.xml",
      "text": "III\n119th CONGRESS\n2d Session\nS. RES. 743\nIN THE SENATE OF THE UNITED STATES\nMay 20, 2026 Mr. Husted (for himself and Mr. Fetterman ) submitted the following resolution; which was referred to the Committee on Health, Education, Labor, and Pensions\nRESOLUTION\nSupporting the designation of May 3 through May 9, 2026, as Children's Mental Health Awareness Week .\nThat the Senate\u2014\n**(1)**\nsupports the designation of May 3 through May 9, 2026, as Children's Mental Health Awareness Week to raise awareness of the mental health conditions facing our children and the importance of early detection, treatment, intervention, and prevention strategies;\n**(2)**\nrecognizes the relationship between children\u2019s mental well-being and plenty of outdoor recreation, a healthy diet, regular socialization with peers, and adequate sleep;\n**(3)**\nurges youth mental health be categorized as a national priority and calls for the continued promotion of mental health in schools and communities;\n**(4)**\napplauds the collaboration of local, State, and Federal organizations in promoting awareness of youth mental health and providing support for those in need;\n**(5)**\nadvocates for individuals, families, and communities to participate in activities during Children's Mental Health Awareness Week to promote mental health initiatives, reduce stigma, and facilitate access to essential services and resources; and\n**(6)**\nreaffirms the importance of mental health as a necessary aspect of overall well-being and urges continued efforts to facilitate access to mental health care for the children of the United States.",
      "versionDate": "2026-05-20",
      "versionType": "IS"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2026-05-20",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/sres/BILLS-119sres743is.xml"
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
      "title": "A resolution supporting the designation of May 3 through May 9, 2026, as \"Children's Mental Health Awareness Week\".",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-05-22T10:18:31Z"
    },
    {
      "title": "A resolution supporting the designation of May 3 through May 9, 2026, as \"Children's Mental Health Awareness Week\".",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-05-21T10:56:28Z"
    }
  ]
}
```
