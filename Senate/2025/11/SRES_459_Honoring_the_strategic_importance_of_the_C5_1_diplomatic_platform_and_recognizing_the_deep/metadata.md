# Metadata

- API URL: https://api.congress.gov/v3/bill/119/sres/459?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-resolution/459
- Title: A resolution honoring the strategic importance of the C5+1 diplomatic platform and recognizing the deepening partnership between the United States and the nations of Kazakhstan, Kyrgyzstan, Tajikistan, Turkmenistan, and Uzbekistan.
- Congress: 119
- Bill type: SRES
- Bill number: 459
- Origin chamber: Senate
- Introduced date: 2025-10-21
- Update date: 2025-12-02T19:10:32Z
- Update date including text: 2025-12-02T19:10:32Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-10-21: Introduced in Senate
- 2025-10-21 - IntroReferral: Introduced in Senate
- 2025-10-21 - IntroReferral: Referred to the Committee on Foreign Relations.
- 2025-11-04 - Floor: Passed/agreed to in Senate: Resolution agreed to in Senate without amendment and with a preamble by Unanimous Consent.
- 2025-11-04 - Floor: Resolution agreed to in Senate without amendment and with a preamble by Unanimous Consent. (consideration: CR S7905; text: CR 10/21/2025 S7188)
- 2025-11-04 - Discharge: Senate Committee on Foreign Relations discharged by Unanimous Consent.
- 2025-11-04 - Committee: Senate Committee on Foreign Relations discharged by Unanimous Consent.
- Latest action: 2025-10-21: Introduced in Senate

## Actions

- 2025-10-21 - IntroReferral: Introduced in Senate
- 2025-10-21 - IntroReferral: Referred to the Committee on Foreign Relations.
- 2025-11-04 - Floor: Passed/agreed to in Senate: Resolution agreed to in Senate without amendment and with a preamble by Unanimous Consent.
- 2025-11-04 - Floor: Resolution agreed to in Senate without amendment and with a preamble by Unanimous Consent. (consideration: CR S7905; text: CR 10/21/2025 S7188)
- 2025-11-04 - Discharge: Senate Committee on Foreign Relations discharged by Unanimous Consent.
- 2025-11-04 - Committee: Senate Committee on Foreign Relations discharged by Unanimous Consent.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-10-21",
    "latestAction": {
      "actionDate": "2025-10-21",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-resolution/459",
    "number": "459",
    "originChamber": "Senate",
    "policyArea": {
      "name": "International Affairs"
    },
    "sponsors": [
      {
        "bioguideId": "D000618",
        "district": "",
        "firstName": "Steve",
        "fullName": "Sen. Daines, Steve [R-MT]",
        "lastName": "Daines",
        "party": "R",
        "state": "MT"
      }
    ],
    "title": "A resolution honoring the strategic importance of the C5+1 diplomatic platform and recognizing the deepening partnership between the United States and the nations of Kazakhstan, Kyrgyzstan, Tajikistan, Turkmenistan, and Uzbekistan.",
    "type": "SRES",
    "updateDate": "2025-12-02T19:10:32Z",
    "updateDateIncludingText": "2025-12-02T19:10:32Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-11-04",
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Resolution agreed to in Senate without amendment and with a preamble by Unanimous Consent. (consideration: CR S7905; text: CR 10/21/2025 S7188)",
      "type": "Floor"
    },
    {
      "actionCode": "17000",
      "actionDate": "2025-11-04",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Passed/agreed to in Senate: Resolution agreed to in Senate without amendment and with a preamble by Unanimous Consent.",
      "type": "Floor"
    },
    {
      "actionDate": "2025-11-04",
      "committees": {
        "item": {
          "name": "Foreign Relations Committee",
          "systemCode": "ssfr00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Senate Committee on Foreign Relations discharged by Unanimous Consent.",
      "type": "Discharge"
    },
    {
      "actionCode": "14500",
      "actionDate": "2025-11-04",
      "committees": {
        "item": {
          "name": "Foreign Relations Committee",
          "systemCode": "ssfr00"
        }
      },
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Senate Committee on Foreign Relations discharged by Unanimous Consent.",
      "type": "Committee"
    },
    {
      "actionDate": "2025-10-21",
      "committees": {
        "item": {
          "name": "Foreign Relations Committee",
          "systemCode": "ssfr00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Referred to the Committee on Foreign Relations.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-10-21",
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
            "date": "2025-11-05T00:26:11Z",
            "name": "Discharged From"
          },
          {
            "date": "2025-10-21T18:32:01Z",
            "name": "Referred To"
          }
        ]
      },
      "chamber": "Senate",
      "name": "Foreign Relations Committee",
      "systemCode": "ssfr00",
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
      "bioguideId": "P000595",
      "firstName": "Gary",
      "fullName": "Sen. Peters, Gary C. [D-MI]",
      "isOriginalCosponsor": "True",
      "lastName": "Peters",
      "party": "D",
      "sponsorshipDate": "2025-10-21",
      "state": "MI"
    },
    {
      "bioguideId": "M001169",
      "firstName": "Christopher",
      "fullName": "Sen. Murphy, Christopher [D-CT]",
      "isOriginalCosponsor": "True",
      "lastName": "Murphy",
      "middleName": "S.",
      "party": "D",
      "sponsorshipDate": "2025-10-21",
      "state": "CT"
    },
    {
      "bioguideId": "M001243",
      "firstName": "David",
      "fullName": "Sen. McCormick, David [R-PA]",
      "isOriginalCosponsor": "True",
      "lastName": "McCormick",
      "middleName": "H.",
      "party": "R",
      "sponsorshipDate": "2025-10-21",
      "state": "PA"
    },
    {
      "bioguideId": "R000608",
      "firstName": "Jacky",
      "fullName": "Sen. Rosen, Jacky [D-NV]",
      "isOriginalCosponsor": "True",
      "lastName": "Rosen",
      "party": "D",
      "sponsorshipDate": "2025-10-21",
      "state": "NV"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/sres/BILLS-119sres459is.xml",
      "text": "III\n119th CONGRESS\n1st Session\nS. RES. 459\nIN THE SENATE OF THE UNITED STATES\nOctober 21, 2025 Mr. Daines (for himself, Mr. Peters , Mr. Murphy , Mr. McCormick , and Ms. Rosen ) submitted the following resolution; which was referred to the Committee on Foreign Relations\nRESOLUTION\nHonoring the strategic importance of the C5+1 diplomatic platform and recognizing the deepening partnership between the United States and the nations of Kazakhstan, Kyrgyzstan, Tajikistan, Turkmenistan, and Uzbekistan.\nThat the Senate\u2014\n**(1)**\naffirms the strategic importance of the C5+1 platform in promoting regional sovereignty, stability, and shared security interests with the United States;\n**(2)**\nappreciates expanded cooperation on energy and critical minerals through transport corridor development;\n**(3)**\nrecognizes the unwavering commitment of the Central Asian nations to counterterrorism coordination under the C5+1; and\n**(4)**\nhopes for a reduction in strategic trade barriers and increase in continued prosperity and friendship.",
      "versionDate": "2025-10-21",
      "versionType": "IS"
    },
    {
      "fetchError": null,
      "sourceFormat": "Formatted XML",
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/sres/BILLS-119sres459ats.xml",
      "text": "III\n119th CONGRESS\n1st Session\nS. RES. 459\nIN THE SENATE OF THE UNITED STATES\nOctober 21, 2025 Mr. Daines (for himself, Mr. Peters , Mr. Murphy , Mr. McCormick , and Ms. Rosen ) submitted the following resolution; which was referred to the Committee on Foreign Relations\nNovember 4, 2025 Committee discharged; considered and agreed to\nRESOLUTION\nHonoring the strategic importance of the C5+1 diplomatic platform and recognizing the deepening partnership between the United States and the nations of Kazakhstan, Kyrgyzstan, Tajikistan, Turkmenistan, and Uzbekistan.\nThat the Senate\u2014\n**(1)**\naffirms the strategic importance of the C5+1 platform in promoting regional sovereignty, stability, and shared security interests with the United States;\n**(2)**\nappreciates expanded cooperation on energy and critical minerals through transport corridor development;\n**(3)**\nrecognizes the unwavering commitment of the Central Asian nations to counterterrorism coordination under the C5+1; and\n**(4)**\nhopes for a reduction in strategic trade barriers and increase in continued prosperity and friendship.",
      "versionDate": "2025-11-04",
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
            "name": "Asia",
            "updateDate": "2025-12-02T19:09:50Z"
          },
          {
            "name": "Diplomacy, foreign officials, Americans abroad",
            "updateDate": "2025-12-02T19:09:56Z"
          },
          {
            "name": "International organizations and cooperation",
            "updateDate": "2025-12-02T19:10:09Z"
          },
          {
            "name": "Kazakhstan",
            "updateDate": "2025-12-02T19:09:16Z"
          },
          {
            "name": "Kyrgyzstan",
            "updateDate": "2025-12-02T19:09:23Z"
          },
          {
            "name": "Tajikistan",
            "updateDate": "2025-12-02T19:09:29Z"
          },
          {
            "name": "Turkmenistan",
            "updateDate": "2025-12-02T19:09:37Z"
          },
          {
            "name": "Uzbekistan",
            "updateDate": "2025-12-02T19:09:44Z"
          }
        ]
      },
      "policyArea": {
        "name": "International Affairs",
        "updateDate": "2025-11-19T21:15:11Z"
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
      "date": "2025-10-21",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/sres/BILLS-119sres459is.xml"
        }
      ],
      "type": "IS"
    },
    {
      "date": "2025-11-04",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/sres/BILLS-119sres459ats.xml"
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
      "title": "A resolution honoring the strategic importance of the C5+1 diplomatic platform and recognizing the deepening partnership between the United States and the nations of Kazakhstan, Kyrgyzstan, Tajikistan, Turkmenistan, and Uzbekistan.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-10-23T12:32:04Z"
    },
    {
      "title": "A resolution honoring the strategic importance of the C5+1 diplomatic platform and recognizing the deepening partnership between the United States and the nations of Kazakhstan, Kyrgyzstan, Tajikistan, Turkmenistan, and Uzbekistan.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-10-23T10:56:20Z"
    }
  ]
}
```
