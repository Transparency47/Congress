# Metadata

- API URL: https://api.congress.gov/v3/bill/119/sres/87?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/sres/87
- Title: A resolution designating February 2025 as "American Heart Month".
- Congress: 119
- Bill type: SRES
- Bill number: 87
- Origin chamber: Senate
- Introduced date: 2025-02-21
- Update date: 2025-03-05T16:37:25Z
- Update date including text: 2025-03-05T16:37:25Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-02-21: Introduced in Senate
- 2025-02-21 - IntroReferral: Introduced in Senate
- 2025-02-21 - Floor: Passed/agreed to in Senate: Submitted in the Senate, considered, and agreed to without amendment and with a preamble by Unanimous Consent.
- 2025-02-21 - Floor: Submitted in the Senate, considered, and agreed to without amendment and with a preamble by Unanimous Consent. (consideration: CR S1303; text: CR S1136)
- Latest action: 2025-02-21: Introduced in Senate

## Actions

- 2025-02-21 - IntroReferral: Introduced in Senate
- 2025-02-21 - Floor: Passed/agreed to in Senate: Submitted in the Senate, considered, and agreed to without amendment and with a preamble by Unanimous Consent.
- 2025-02-21 - Floor: Submitted in the Senate, considered, and agreed to without amendment and with a preamble by Unanimous Consent. (consideration: CR S1303; text: CR S1136)

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-02-21",
    "latestAction": {
      "actionDate": "2025-02-21",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/sres/87",
    "number": "87",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Health"
    },
    "sponsors": [
      {
        "bioguideId": "D000563",
        "district": "",
        "firstName": "Richard",
        "fullName": "Sen. Durbin, Richard J. [D-IL]",
        "lastName": "Durbin",
        "party": "D",
        "state": "IL"
      }
    ],
    "title": "A resolution designating February 2025 as \"American Heart Month\".",
    "type": "SRES",
    "updateDate": "2025-03-05T16:37:25Z",
    "updateDateIncludingText": "2025-03-05T16:37:25Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-02-21",
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Submitted in the Senate, considered, and agreed to without amendment and with a preamble by Unanimous Consent. (consideration: CR S1303; text: CR S1136)",
      "type": "Floor"
    },
    {
      "actionCode": "17000",
      "actionDate": "2025-02-21",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Passed/agreed to in Senate: Submitted in the Senate, considered, and agreed to without amendment and with a preamble by Unanimous Consent.",
      "type": "Floor"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-02-21",
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

## API Data: cosponsors

```json
{
  "cosponsors": [
    {
      "bioguideId": "C000880",
      "firstName": "Mike",
      "fullName": "Sen. Crapo, Mike [R-ID]",
      "isOriginalCosponsor": "True",
      "lastName": "Crapo",
      "party": "R",
      "sponsorshipDate": "2025-02-21",
      "state": "ID"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/sres/BILLS-119sres87ats.xml",
      "text": "III\n119th CONGRESS\n1st Session\nS. RES. 87\nIN THE SENATE OF THE UNITED STATES\nFebruary 21 (legislative day, February 20), 2025 Mr. Durbin (for himself and Mr. Crapo ) submitted the following resolution; which was considered and agreed to\nRESOLUTION\nDesignating February 2025 as American Heart Month .\nThat the Senate\u2014\n**(1)**\ndesignates February 2025 as American Heart Month ;\n**(2)**\nsupports the goals and ideals of American Heart Month;\n**(3)**\nrecognizes and reaffirms the commitment of the United States to fighting cardiovascular disease (referred to in this resolution as CVD ) by\u2014\n**(A)**\npromoting awareness about the causes, risks, and prevention of CVD;\n**(B)**\nsupporting research on CVD; and\n**(C)**\ntaking other steps to improve health outcomes associated with CVD and reduce associated long-term disability and mortality;\n**(4)**\ncommends the efforts of States, territories, and possessions of the United States, localities, nonprofit organizations, businesses, other entities, and the people of the United States who support American Heart Month; and\n**(5)**\nencourages every individual in the United States to learn about their risk for CVD.",
      "versionDate": "2025-02-21",
      "versionType": "ATS"
    }
  ]
}
```

## API Data: subjects

```json
{
  "subjects": [
    {
      "legislativeSubjects": {
        "item": [
          {
            "name": "Cardiovascular and respiratory health",
            "updateDate": "2025-03-05T16:37:25Z"
          },
          {
            "name": "Commemorative events and holidays",
            "updateDate": "2025-03-05T16:37:21Z"
          },
          {
            "name": "Health promotion and preventive care",
            "updateDate": "2025-03-05T16:37:17Z"
          }
        ]
      },
      "policyArea": {
        "name": "Health",
        "updateDate": "2025-03-05T13:55:59Z"
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
      "date": "2025-02-21",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/sres/BILLS-119sres87ats.xml"
        }
      ],
      "type": "ATS"
    }
  ]
}
```

## API Data: titles

```json
{
  "titles": [
    {
      "title": "A resolution designating February 2025 as \"American Heart Month\".",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-02-21T11:56:15Z"
    },
    {
      "title": "A resolution designating February 2025 as \"American Heart Month\".",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-02-21T11:56:15Z"
    }
  ]
}
```
