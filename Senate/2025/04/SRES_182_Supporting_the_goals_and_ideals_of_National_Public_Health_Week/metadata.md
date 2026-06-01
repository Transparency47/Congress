# Metadata

- API URL: https://api.congress.gov/v3/bill/119/sres/182?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/sres/182
- Title: A resolution supporting the goals and ideals of National Public Health Week.
- Congress: 119
- Bill type: SRES
- Bill number: 182
- Origin chamber: Senate
- Introduced date: 2025-04-10
- Update date: 2025-05-02T13:21:22Z
- Update date including text: 2025-05-02T13:21:22Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, subjects, text, titles

## Timeline

- 2025-04-10: Introduced in Senate
- 2025-04-10 - IntroReferral: Introduced in Senate
- 2025-04-10 - IntroReferral: Referred to the Committee on Health, Education, Labor, and Pensions.
- Latest action: 2025-04-10: Introduced in Senate

## Actions

- 2025-04-10 - IntroReferral: Introduced in Senate
- 2025-04-10 - IntroReferral: Referred to the Committee on Health, Education, Labor, and Pensions.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-04-10",
    "latestAction": {
      "actionDate": "2025-04-10",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/sres/182",
    "number": "182",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Health"
    },
    "sponsors": [
      {
        "bioguideId": "L000570",
        "district": "",
        "firstName": "Ben",
        "fullName": "Sen. Lujan, Ben Ray [D-NM]",
        "lastName": "Lujan",
        "party": "D",
        "state": "NM"
      }
    ],
    "title": "A resolution supporting the goals and ideals of National Public Health Week.",
    "type": "SRES",
    "updateDate": "2025-05-02T13:21:22Z",
    "updateDateIncludingText": "2025-05-02T13:21:22Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-04-10",
      "committees": {
        "item": {
          "name": "Health, Education, Labor, and Pensions Committee",
          "systemCode": "sshr00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Referred to the Committee on Health, Education, Labor, and Pensions.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-04-10",
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
          "date": "2025-04-10T22:01:33Z",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/sres/BILLS-119sres182is.xml",
      "text": "III\n119th CONGRESS\n1st Session\nS. RES. 182\nIN THE SENATE OF THE UNITED STATES\nApril 10, 2025 Mr. Luj\u00e1n submitted the following resolution; which was referred to the Committee on Health, Education, Labor, and Pensions\nRESOLUTION\nSupporting the goals and ideals of National Public Health Week.\nThat the Senate\u2014\n**(1)**\nsupports the goals and ideals of National Public Health Week;\n**(2)**\nrecognizes the efforts of public health professionals, the Federal Government, States, Tribes, municipalities, local communities, and individuals in preventing disease and injury;\n**(3)**\nrecognizes the role of public health in\u2014\n**(A)**\npreventing and responding to infectious disease outbreaks, such as the COVID\u201319 pandemic and the ongoing measles outbreak;\n**(B)**\nmitigating the short-term and long-term impacts of infectious disease outbreaks on the health and wellness of individuals in the United States;\n**(C)**\naddressing social and other determinants of health, including health disparities experienced by minority populations; and\n**(D)**\nimproving the overall health of individuals and communities in the United States;\n**(4)**\nencourages increased efforts and resources to\u2014\n**(A)**\nimprove the health of individuals in the United States; and\n**(B)**\nmake the United States, in 1 generation, the healthiest Nation in the world by\u2014\n**(i)**\nproviding greater opportunities to improve community health and prevent disease and injury; and\n**(ii)**\nstrengthening the public health system and workforce in the United States; and\n**(5)**\nencourages the people of the United States to learn about the role of the public health system in improving health across the United States.",
      "versionDate": "2025-04-10",
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
        "name": "Health",
        "updateDate": "2025-05-02T13:21:22Z"
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
      "date": "2025-04-10",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/sres/BILLS-119sres182is.xml"
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
      "title": "A resolution supporting the goals and ideals of National Public Health Week.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-04-16T03:03:27Z"
    },
    {
      "title": "A resolution supporting the goals and ideals of National Public Health Week.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-04-11T10:56:16Z"
    }
  ]
}
```
