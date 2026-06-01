# Metadata

- API URL: https://api.congress.gov/v3/bill/119/sres/752?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-resolution/752
- Title: A resolution expressing support for the designation of the month of May 2026 as "Progressive Supranuclear Palsy and Corticobasal Degeneration Awareness Month".
- Congress: 119
- Bill type: SRES
- Bill number: 752
- Origin chamber: Senate
- Introduced date: 2026-05-21
- Update date: 2026-05-23T06:48:28Z
- Update date including text: 2026-05-23T06:48:28Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, text, titles

## Timeline

- 2026-05-21: Introduced in Senate
- 2026-05-21 - IntroReferral: Referred to the Committee on Health, Education, Labor, and Pensions. (text: CR S2447)
- 2026-05-21 - IntroReferral: Submitted in Senate
- Latest action: 2026-05-21: Submitted in Senate

## Actions

- 2026-05-21 - IntroReferral: Referred to the Committee on Health, Education, Labor, and Pensions. (text: CR S2447)
- 2026-05-21 - IntroReferral: Submitted in Senate

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-05-21",
    "latestAction": {
      "actionDate": "2026-05-21",
      "text": "Submitted in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-resolution/752",
    "number": "752",
    "originChamber": "Senate",
    "policyArea": {},
    "sponsors": [
      {
        "bioguideId": "B001277",
        "district": "",
        "firstName": "Richard",
        "fullName": "Sen. Blumenthal, Richard [D-CT]",
        "lastName": "Blumenthal",
        "party": "D",
        "state": "CT"
      }
    ],
    "title": "A resolution expressing support for the designation of the month of May 2026 as \"Progressive Supranuclear Palsy and Corticobasal Degeneration Awareness Month\".",
    "type": "SRES",
    "updateDate": "2026-05-23T06:48:28Z",
    "updateDateIncludingText": "2026-05-23T06:48:28Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-05-21",
      "committees": {
        "item": {
          "name": "Health, Education, Labor, and Pensions Committee",
          "systemCode": "sshr00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Referred to the Committee on Health, Education, Labor, and Pensions. (text: CR S2447)",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10025",
      "actionDate": "2026-05-21",
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
          "date": "2026-05-21T18:21:31Z",
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

## API Data: fullTexts

```json
{
  "fullTexts": [
    {
      "fetchError": null,
      "sourceFormat": "Formatted XML",
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/sres/BILLS-119sres752is.xml",
      "text": "III\n119th CONGRESS\n2d Session\nS. RES. 752\nIN THE SENATE OF THE UNITED STATES\nMay 21, 2026 Mr. Blumenthal submitted the following resolution; which was referred to the Committee on Health, Education, Labor, and Pensions\nRESOLUTION\nExpressing support for the designation of the month of May 2026 as Progressive Supranuclear Palsy and Corticobasal Degeneration Awareness Month .\nThat the Senate\u2014\n**(1)**\nsupports the designation of May 2026 as Progressive Supranuclear Palsy and Corticobasal Degeneration Awareness Month ;\n**(2)**\nsupports the goals and ideals of Progressive Supranuclear Palsy and Corticobasal Degeneration Awareness Month;\n**(3)**\nsupports research on diagnosis, prevention, treatments, and cures for progressive supranuclear palsy and corticobasal degeneration;\n**(4)**\nrecognizes the strength and resilience of the communities affected by progressive supranuclear palsy and corticobasal degeneration; and\n**(5)**\ncommends the individuals, families, volunteers, healthcare professionals, researchers, and organizations across the country who are working to improve the lives of people living with progressive supranuclear palsy and corticobasal degeneration.",
      "versionDate": "2026-05-21",
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
      "date": "2026-05-21",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/sres/BILLS-119sres752is.xml"
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
      "title": "A resolution expressing support for the designation of the month of May 2026 as \"Progressive Supranuclear Palsy and Corticobasal Degeneration Awareness Month\".",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-05-23T06:48:28Z"
    },
    {
      "title": "A resolution expressing support for the designation of the month of May 2026 as \"Progressive Supranuclear Palsy and Corticobasal Degeneration Awareness Month\".",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-05-22T10:56:35Z"
    }
  ]
}
```
