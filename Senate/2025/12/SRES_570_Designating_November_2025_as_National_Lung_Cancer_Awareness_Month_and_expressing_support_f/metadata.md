# Metadata

- API URL: https://api.congress.gov/v3/bill/119/sres/570?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-resolution/570
- Title: A resolution designating November 2025 as "National Lung Cancer Awareness Month" and expressing support for early detection and treatment of lung cancer.
- Congress: 119
- Bill type: SRES
- Bill number: 570
- Origin chamber: Senate
- Introduced date: 2025-12-18
- Update date: 2026-01-13T15:37:30Z
- Update date including text: 2026-01-13T15:37:30Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-12-18: Introduced in Senate
- 2025-12-18 - IntroReferral: Introduced in Senate
- 2025-12-18 - IntroReferral: Referred to the Committee on the Judiciary.
- 2026-01-12 - Floor: Passed/agreed to in Senate: Resolution agreed to in Senate without amendment and with a preamble by Unanimous Consent.
- 2026-01-12 - Floor: Resolution agreed to in Senate without amendment and with a preamble by Unanimous Consent. (consideration: CR S140; text: CR 12/18/2025 S8925)
- 2026-01-12 - Discharge: Senate Committee on the Judiciary discharged by Unanimous Consent.
- 2026-01-12 - Committee: Senate Committee on the Judiciary discharged by Unanimous Consent.
- Latest action: 2025-12-18: Introduced in Senate

## Actions

- 2025-12-18 - IntroReferral: Introduced in Senate
- 2025-12-18 - IntroReferral: Referred to the Committee on the Judiciary.
- 2026-01-12 - Floor: Passed/agreed to in Senate: Resolution agreed to in Senate without amendment and with a preamble by Unanimous Consent.
- 2026-01-12 - Floor: Resolution agreed to in Senate without amendment and with a preamble by Unanimous Consent. (consideration: CR S140; text: CR 12/18/2025 S8925)
- 2026-01-12 - Discharge: Senate Committee on the Judiciary discharged by Unanimous Consent.
- 2026-01-12 - Committee: Senate Committee on the Judiciary discharged by Unanimous Consent.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-12-18",
    "latestAction": {
      "actionDate": "2025-12-18",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-resolution/570",
    "number": "570",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Health"
    },
    "sponsors": [
      {
        "bioguideId": "S001203",
        "district": "",
        "firstName": "Tina",
        "fullName": "Sen. Smith, Tina [D-MN]",
        "lastName": "Smith",
        "party": "D",
        "state": "MN"
      }
    ],
    "title": "A resolution designating November 2025 as \"National Lung Cancer Awareness Month\" and expressing support for early detection and treatment of lung cancer.",
    "type": "SRES",
    "updateDate": "2026-01-13T15:37:30Z",
    "updateDateIncludingText": "2026-01-13T15:37:30Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-01-12",
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Resolution agreed to in Senate without amendment and with a preamble by Unanimous Consent. (consideration: CR S140; text: CR 12/18/2025 S8925)",
      "type": "Floor"
    },
    {
      "actionCode": "17000",
      "actionDate": "2026-01-12",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Passed/agreed to in Senate: Resolution agreed to in Senate without amendment and with a preamble by Unanimous Consent.",
      "type": "Floor"
    },
    {
      "actionDate": "2026-01-12",
      "committees": {
        "item": {
          "name": "Judiciary Committee",
          "systemCode": "ssju00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Senate Committee on the Judiciary discharged by Unanimous Consent.",
      "type": "Discharge"
    },
    {
      "actionCode": "14500",
      "actionDate": "2026-01-12",
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
      "text": "Senate Committee on the Judiciary discharged by Unanimous Consent.",
      "type": "Committee"
    },
    {
      "actionDate": "2025-12-18",
      "committees": {
        "item": {
          "name": "Judiciary Committee",
          "systemCode": "ssju00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Referred to the Committee on the Judiciary.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-12-18",
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
        "item": [
          {
            "date": "2026-01-12T23:53:59Z",
            "name": "Discharged From"
          },
          {
            "date": "2025-12-18T22:57:50Z",
            "name": "Referred To"
          }
        ]
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
      "bioguideId": "C001047",
      "firstName": "Shelley",
      "fullName": "Sen. Capito, Shelley Moore [R-WV]",
      "isOriginalCosponsor": "True",
      "lastName": "Capito",
      "middleName": "Moore",
      "party": "R",
      "sponsorshipDate": "2025-12-18",
      "state": "WV"
    },
    {
      "bioguideId": "H001042",
      "firstName": "Mazie",
      "fullName": "Sen. Hirono, Mazie K. [D-HI]",
      "isOriginalCosponsor": "True",
      "lastName": "Hirono",
      "middleName": "K.",
      "party": "D",
      "sponsorshipDate": "2025-12-18",
      "state": "HI"
    },
    {
      "bioguideId": "R000122",
      "firstName": "John",
      "fullName": "Sen. Reed, Jack [D-RI]",
      "isOriginalCosponsor": "True",
      "lastName": "Reed",
      "middleName": "F.",
      "party": "D",
      "sponsorshipDate": "2025-12-18",
      "state": "RI"
    },
    {
      "bioguideId": "M001176",
      "firstName": "Jeff",
      "fullName": "Sen. Merkley, Jeff [D-OR]",
      "isOriginalCosponsor": "True",
      "lastName": "Merkley",
      "party": "D",
      "sponsorshipDate": "2025-12-18",
      "state": "OR"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/sres/BILLS-119sres570is.xml",
      "text": "III\n119th CONGRESS\n1st Session\nS. RES. 570\nIN THE SENATE OF THE UNITED STATES\nDecember 18, 2025 Ms. Smith (for herself, Mrs. Capito , Ms. Hirono , Mr. Reed , and Mr. Merkley ) submitted the following resolution; which was referred to the Committee on the Judiciary\nRESOLUTION\nDesignating November 2025 as National Lung Cancer Awareness Month and expressing support for early detection and treatment of lung cancer.\nThat the Senate\u2014\n**(1)**\ndesignates November 2025 as National Lung Cancer Awareness Month ;\n**(2)**\ndesignates the first week of November 2025 as National Women's Lung Cancer Awareness Week ;\n**(3)**\ndesignates the second Saturday of November 2025 as National Lung Cancer Screening Day ;\n**(4)**\nsupports the purposes and ideals of National Lung Cancer Awareness Month;\n**(5)**\npromotes efforts to increase awareness of, education about, and research on\u2014\n**(A)**\nmitigation of risk factors for lung cancer;\n**(B)**\nlung cancer screening;\n**(C)**\ntreatment of lung cancer; and\n**(D)**\nlung cancer affecting minorities and individuals who have never smoked; and\n**(6)**\nencourages the people of the United States to observe National Lung Cancer Awareness Month with appropriate awareness and educational activities.",
      "versionDate": "2025-12-18",
      "versionType": "IS"
    },
    {
      "fetchError": null,
      "sourceFormat": "Formatted XML",
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/sres/BILLS-119sres570ats.xml",
      "text": "III\n119th CONGRESS\n2d Session\nS. RES. 570\nIN THE SENATE OF THE UNITED STATES\nDecember 18, 2025 Ms. Smith (for herself, Mrs. Capito , Ms. Hirono , Mr. Reed , and Mr. Merkley ) submitted the following resolution; which was referred to the Committee on the Judiciary\nJanuary 12, 2026 Committee discharged; considered and agreed to\nRESOLUTION\nDesignating November 2025 as National Lung Cancer Awareness Month and expressing support for early detection and treatment of lung cancer.\nThat the Senate\u2014\n**(1)**\ndesignates November 2025 as National Lung Cancer Awareness Month ;\n**(2)**\ndesignates the first week of November 2025 as National Women's Lung Cancer Awareness Week ;\n**(3)**\ndesignates the second Saturday of November 2025 as National Lung Cancer Screening Day ;\n**(4)**\nsupports the purposes and ideals of National Lung Cancer Awareness Month;\n**(5)**\npromotes efforts to increase awareness of, education about, and research on\u2014\n**(A)**\nmitigation of risk factors for lung cancer;\n**(B)**\nlung cancer screening;\n**(C)**\ntreatment of lung cancer; and\n**(D)**\nlung cancer affecting minorities and individuals who have never smoked; and\n**(6)**\nencourages the people of the United States to observe National Lung Cancer Awareness Month with appropriate awareness and educational activities.",
      "versionDate": "2026-01-12",
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
      "legislativeSubjects": "",
      "policyArea": {
        "name": "Health",
        "updateDate": "2026-01-06T18:59:45Z"
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
      "date": "2025-12-18",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/sres/BILLS-119sres570is.xml"
        }
      ],
      "type": "IS"
    },
    {
      "date": "2026-01-12",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/sres/BILLS-119sres570ats.xml"
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
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A resolution designating November 2025 as \"National Lung Cancer Awareness Month\" and expressing support for early detection and treatment of lung cancer.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-12-20T05:48:18Z"
    },
    {
      "title": "A resolution designating November 2025 as \"National Lung Cancer Awareness Month\" and expressing support for early detection and treatment of lung cancer.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-12-19T11:56:22Z"
    }
  ]
}
```
