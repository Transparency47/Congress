# Metadata

- API URL: https://api.congress.gov/v3/bill/119/sres/630?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-resolution/630
- Title: A resolution honoring the lives of fallen Missouri police officers and expressing condolences to their families.
- Congress: 119
- Bill type: SRES
- Bill number: 630
- Origin chamber: Senate
- Introduced date: 2026-03-10
- Update date: 2026-03-13T15:19:56Z
- Update date including text: 2026-03-13T15:19:56Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2026-03-10: Introduced in Senate
- 2026-03-10 - IntroReferral: Referred to the Committee on the Judiciary. (text: CR S960)
- 2026-03-10 - IntroReferral: Submitted in Senate
- Latest action: 2026-03-10: Submitted in Senate

## Actions

- 2026-03-10 - IntroReferral: Referred to the Committee on the Judiciary. (text: CR S960)
- 2026-03-10 - IntroReferral: Submitted in Senate

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-03-10",
    "latestAction": {
      "actionDate": "2026-03-10",
      "text": "Submitted in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-resolution/630",
    "number": "630",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Crime and Law Enforcement"
    },
    "sponsors": [
      {
        "bioguideId": "H001089",
        "district": "",
        "firstName": "Josh",
        "fullName": "Sen. Hawley, Josh [R-MO]",
        "lastName": "Hawley",
        "party": "R",
        "state": "MO"
      }
    ],
    "title": "A resolution honoring the lives of fallen Missouri police officers and expressing condolences to their families.",
    "type": "SRES",
    "updateDate": "2026-03-13T15:19:56Z",
    "updateDateIncludingText": "2026-03-13T15:19:56Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-03-10",
      "committees": {
        "item": {
          "name": "Judiciary Committee",
          "systemCode": "ssju00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Referred to the Committee on the Judiciary. (text: CR S960)",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10025",
      "actionDate": "2026-03-10",
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
          "date": "2026-03-10T15:11:31Z",
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
      "bioguideId": "S001227",
      "firstName": "Eric",
      "fullName": "Sen. Schmitt, Eric [R-MO]",
      "isOriginalCosponsor": "True",
      "lastName": "Schmitt",
      "middleName": "S.",
      "party": "R",
      "sponsorshipDate": "2026-03-10",
      "state": "MO"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/sres/BILLS-119sres630is.xml",
      "text": "III\n119th CONGRESS\n2d Session\nS. RES. 630\nIN THE SENATE OF THE UNITED STATES\nMarch 10, 2026 Mr. Hawley (for himself and Mr. Schmitt ) submitted the following resolution; which was referred to the Committee on the Judiciary\nRESOLUTION\nHonoring the lives of fallen Missouri police officers and expressing condolences to their families.\nThat the Senate\u2014\n**(1)**\nexpresses deep condolences for\u2014\n**(A)**\nthe Missouri police officers who made the ultimate sacrifice in the line of duty; and\n**(B)**\ntheir families;\n**(2)**\nrecognizes the countless selfless and heroic actions carried out by Missouri law enforcement officers every day;\n**(3)**\nexpresses strong support for police officers and law enforcement officers across the United States that serve and protect their local communities;\n**(4)**\nacknowledges the importance of honoring and remembering fallen police and local law enforcement officers killed in the line of duty;\n**(5)**\ncondemns all violent acts taken against law enforcement officers; and\n**(6)**\ncommits to supporting law enforcement officers in their work to fulfil their duty of making our communities safer.",
      "versionDate": "2026-03-10",
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
        "updateDate": "2026-03-13T15:19:55Z"
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
      "date": "2026-03-10",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/sres/BILLS-119sres630is.xml"
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
      "title": "A resolution honoring the lives of fallen Missouri police officers and expressing condolences to their families.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-03-12T04:18:26Z"
    },
    {
      "title": "A resolution honoring the lives of fallen Missouri police officers and expressing condolences to their families.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-03-11T10:56:24Z"
    }
  ]
}
```
