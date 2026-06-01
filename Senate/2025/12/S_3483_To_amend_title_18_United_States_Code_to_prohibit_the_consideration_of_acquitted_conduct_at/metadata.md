# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/3483?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/3483
- Title: A bill to amend title 18, United States Code, to prohibit the consideration of acquitted conduct at sentencing.
- Congress: 119
- Bill type: S
- Bill number: 3483
- Origin chamber: Senate
- Introduced date: 2025-12-15
- Update date: 2026-01-12T16:02:35Z
- Update date including text: 2026-01-12T16:02:35Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-12-15: Introduced in Senate
- 2025-12-15 - IntroReferral: Introduced in Senate
- 2025-12-15 - IntroReferral: Read twice and referred to the Committee on the Judiciary. (text: CR S8737)
- Latest action: 2025-12-15: Introduced in Senate

## Actions

- 2025-12-15 - IntroReferral: Introduced in Senate
- 2025-12-15 - IntroReferral: Read twice and referred to the Committee on the Judiciary. (text: CR S8737)

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-12-15",
    "latestAction": {
      "actionDate": "2025-12-15",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/3483",
    "number": "3483",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Crime and Law Enforcement"
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
    "title": "A bill to amend title 18, United States Code, to prohibit the consideration of acquitted conduct at sentencing.",
    "type": "S",
    "updateDate": "2026-01-12T16:02:35Z",
    "updateDateIncludingText": "2026-01-12T16:02:35Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-12-15",
      "committees": {
        "item": {
          "name": "Judiciary Committee",
          "systemCode": "ssju00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on the Judiciary. (text: CR S8737)",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-12-15",
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
          "date": "2025-12-16T00:03:40Z",
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
      "bioguideId": "G000386",
      "firstName": "Chuck",
      "fullName": "Sen. Grassley, Chuck [R-IA]",
      "isOriginalCosponsor": "True",
      "lastName": "Grassley",
      "party": "R",
      "sponsorshipDate": "2025-12-15",
      "state": "IA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s3483is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 3483\nIN THE SENATE OF THE UNITED STATES\nDecember 15, 2025 Mr. Durbin (for himself and Mr. Grassley ) introduced the following bill; which was read twice and referred to the Committee on the Judiciary\nA BILL\nTo amend title 18, United States Code, to prohibit the consideration of acquitted conduct at sentencing.\n#### 1. Prohibiting punishment of acquitted conduct\n##### (a) Use of information for sentencing\n**(1) Amendment**\nSection 3661 of title 18, United States Code, is amended by inserting , except that a court of the United States shall not consider, except for purposes of mitigating a sentence, acquitted conduct under this section before the period at the end.\n**(2) Applicability**\nThe amendment made by paragraph (1) shall apply only to a judgment entered on or after the date of enactment of this section.\n##### (b) Definitions\nSection 3673 of title 18, United States Code, is amended\u2014\n**(1)**\nin the matter preceding paragraph (1), by striking As and inserting the following:\n(a) As ; and\n**(2)**\nby adding at the end the following:\n(b) As used in this chapter, the term acquitted conduct means\u2014 (1) an act\u2014 (A) for which a person was criminally charged and adjudicated not guilty after trial in a Federal, State, or Tribal court; or (B) in the case of a juvenile, that was charged and for which the juvenile was found not responsible after a juvenile adjudication hearing; or (2) any act underlying a criminal charge or juvenile information dismissed\u2014 (A) in a Federal court upon a motion for acquittal under rule 29 of the Federal Rules of Criminal Procedure; or (B) in a State or Tribal court upon a motion for acquittal or an analogous motion under the applicable State or Tribal rule of criminal procedure. .",
      "versionDate": "2025-12-15",
      "versionType": "Introduced in Senate"
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
        "updateDate": "2026-01-12T16:02:35Z"
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
      "date": "2025-12-15",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s3483is.xml"
        }
      ],
      "type": "Introduced in Senate"
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
      "title": "A bill to amend title 18, United States Code, to prohibit the consideration of acquitted conduct at sentencing.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-01-09T03:18:20Z"
    },
    {
      "title": "A bill to amend title 18, United States Code, to prohibit the consideration of acquitted conduct at sentencing.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-12-16T11:56:17Z"
    }
  ]
}
```
