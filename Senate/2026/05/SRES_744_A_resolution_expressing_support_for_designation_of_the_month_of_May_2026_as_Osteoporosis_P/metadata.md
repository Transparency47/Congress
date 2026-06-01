# Metadata

- API URL: https://api.congress.gov/v3/bill/119/sres/744?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-resolution/744
- Title: A resolution expressing support for designation of the month of May 2026 as "Osteoporosis Prevention and Awareness Month".
- Congress: 119
- Bill type: SRES
- Bill number: 744
- Origin chamber: Senate
- Introduced date: 2026-05-20
- Update date: 2026-05-22T14:58:31Z
- Update date including text: 2026-05-22T14:58:31Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, text, titles

## Timeline

- 2026-05-20: Introduced in Senate
- 2026-05-20 - IntroReferral: Referred to the Committee on the Judiciary. (text: CR S2420)
- 2026-05-20 - IntroReferral: Submitted in Senate
- Latest action: 2026-05-20: Submitted in Senate

## Actions

- 2026-05-20 - IntroReferral: Referred to the Committee on the Judiciary. (text: CR S2420)
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
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-resolution/744",
    "number": "744",
    "originChamber": "Senate",
    "policyArea": {},
    "sponsors": [
      {
        "bioguideId": "C001035",
        "district": "",
        "firstName": "Susan",
        "fullName": "Sen. Collins, Susan M. [R-ME]",
        "lastName": "Collins",
        "party": "R",
        "state": "ME"
      }
    ],
    "title": "A resolution expressing support for designation of the month of May 2026 as \"Osteoporosis Prevention and Awareness Month\".",
    "type": "SRES",
    "updateDate": "2026-05-22T14:58:31Z",
    "updateDateIncludingText": "2026-05-22T14:58:31Z"
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
          "name": "Judiciary Committee",
          "systemCode": "ssju00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Referred to the Committee on the Judiciary. (text: CR S2420)",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10025",
      "actionDate": "2026-05-20",
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
          "date": "2026-05-20T20:08:35Z",
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

## API Data: fullTexts

```json
{
  "fullTexts": [
    {
      "fetchError": null,
      "sourceFormat": "Formatted XML",
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/sres/BILLS-119sres744is.xml",
      "text": "III\n119th CONGRESS\n2d Session\nS. RES. 744\nIN THE SENATE OF THE UNITED STATES\nMay 20, 2026 Ms. Collins submitted the following resolution; which was referred to the Committee on the Judiciary\nRESOLUTION\nExpressing support for designation of the month of May 2026 as Osteoporosis Prevention and Awareness Month .\nThat the Senate\u2014\n**(1)**\ndesignates May 2026 as Osteoporosis Prevention and Awareness Month ;\n**(2)**\naffirms the dedication of the Senate to\u2014\n**(A)**\nraising awareness among the public and health professionals about the importance of bone health throughout a person's lifespan and steps that can be taken to reduce the risk of osteoporotic fractures; and\n**(B)**\nreducing the toll that osteoporosis and osteoporotic fractures take on individuals, the United States, and taxpayers; and\n**(3)**\ncommends the dedication of the States, localities, family members, friends, organizations, volunteers, researchers, and caregivers across the United States who are working to raise awareness about bone health and osteoporosis, provide optimal care for those with osteoporosis, and reduce the toll osteoporosis takes on the United States.",
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
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/sres/BILLS-119sres744is.xml"
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
      "title": "A resolution expressing support for designation of the month of May 2026 as \"Osteoporosis Prevention and Awareness Month\".",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-05-22T10:18:45Z"
    },
    {
      "title": "A resolution expressing support for designation of the month of May 2026 as \"Osteoporosis Prevention and Awareness Month\".",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-05-21T10:56:30Z"
    }
  ]
}
```
