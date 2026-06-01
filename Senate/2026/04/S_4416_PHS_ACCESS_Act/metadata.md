# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/4416?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/4416
- Title: PHS ACCESS Act
- Congress: 119
- Bill type: S
- Bill number: 4416
- Origin chamber: Senate
- Introduced date: 2026-04-28
- Update date: 2026-05-18T18:47:21Z
- Update date including text: 2026-05-18T18:47:21Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2026-04-28: Introduced in Senate
- 2026-04-28 - IntroReferral: Introduced in Senate
- 2026-04-28 - IntroReferral: Read twice and referred to the Committee on Health, Education, Labor, and Pensions.
- Latest action: 2026-04-28: Introduced in Senate

## Actions

- 2026-04-28 - IntroReferral: Introduced in Senate
- 2026-04-28 - IntroReferral: Read twice and referred to the Committee on Health, Education, Labor, and Pensions.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-04-28",
    "latestAction": {
      "actionDate": "2026-04-28",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/4416",
    "number": "4416",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Health"
    },
    "sponsors": [
      {
        "bioguideId": "M001153",
        "district": "",
        "firstName": "Lisa",
        "fullName": "Sen. Murkowski, Lisa [R-AK]",
        "lastName": "Murkowski",
        "party": "R",
        "state": "AK"
      }
    ],
    "title": "PHS ACCESS Act",
    "type": "S",
    "updateDate": "2026-05-18T18:47:21Z",
    "updateDateIncludingText": "2026-05-18T18:47:21Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-04-28",
      "committees": {
        "item": {
          "name": "Health, Education, Labor, and Pensions Committee",
          "systemCode": "sshr00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Health, Education, Labor, and Pensions.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2026-04-28",
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
          "date": "2026-04-28T21:22:19Z",
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
      "bioguideId": "M001169",
      "firstName": "Christopher",
      "fullName": "Sen. Murphy, Christopher [D-CT]",
      "isOriginalCosponsor": "True",
      "lastName": "Murphy",
      "middleName": "S.",
      "party": "D",
      "sponsorshipDate": "2026-04-28",
      "state": "CT"
    },
    {
      "bioguideId": "T000476",
      "firstName": "Thomas",
      "fullName": "Sen. Tillis, Thomas [R-NC]",
      "isOriginalCosponsor": "True",
      "lastName": "Tillis",
      "middleName": "Roland",
      "party": "R",
      "sponsorshipDate": "2026-04-28",
      "state": "NC"
    },
    {
      "bioguideId": "C001113",
      "firstName": "Catherine",
      "fullName": "Sen. Cortez Masto, Catherine [D-NV]",
      "isOriginalCosponsor": "True",
      "lastName": "Cortez Masto",
      "party": "D",
      "sponsorshipDate": "2026-04-28",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s4416is.xml",
      "text": "II\n119th CONGRESS\n2d Session\nS. 4416\nIN THE SENATE OF THE UNITED STATES\nApril 28, 2026 Ms. Murkowski (for herself, Mrs. Murray , Mr. Tillis , and Ms. Cortez Masto ) introduced the following bill; which was read twice and referred to the Committee on Health, Education, Labor, and Pensions\nA BILL\nTo establish procedures for the detailing of Public Health Service officers for purposes of advancing care in underserved communities.\n#### 1. Short title\nThis Act may be cited as the Public Health Services for Advancing Care and Creating Efficient Support Systems in Underserved Communities Act or the PHS ACCESS Act .\n#### 2. Detail of personnel\n##### (a) In general\nSection 214 of the Public Health Service Act ( 42 U.S.C. 215 ) is amended\u2014\n**(1)**\nby redesignating subsections (d) and (e) as subsections (e) and (f), respectively;\n**(2)**\nby inserting after subsection (c) the following:\n(d) The Secretary may detail Public Health Service Commissioned Corps officers to Urban Indian organizations, as defined in section 4 of the Indian Health Care Improvement Act, to cooperate in or conduct work related to the functions of the Department of Health and Human Services. ; and\n**(3)**\nin subsection (e), as so redesignated\u2014\n**(A)**\nby striking subsections (b) and (c) and inserting subsection (b) or (c) ; and\n**(B)**\nby striking subsections (b) or (c) and inserting subsection (b) or (c) .\n##### (b) Appointment of personnel\nSection 207(d) of the Public Health Service Act ( 42 U.S.C. 209(d) ) is amended\u2014\n**(1)**\nin paragraph (1), by striking shall, and inserting may, at the discretion of the Secretary, after consideration of the criteria described in paragraph (5), ; and\n**(2)**\nby adding at the end the following:\n(5) (A) The Secretary shall develop objective, transparent criteria for purposes of determining whether to grant a person appointed under subsection (a) constructive credit for length of service as described in paragraph (1). Such criteria shall\u2014 (i) give preference to appointees who\u2014 (I) serve in a rural or remote (as determined by the Secretary in accordance with objective and transparent criteria established by the Secretary) agency for which the Service is statutorily required to provide services; (II) are specialists in an area with a demonstrated workforce shortage; (III) serve in an area with significant access to care challenges; or (IV) serve with an Indian tribe, tribal organization, or Urban Indian organization (as such terms are defined in section 4 of the Indian Health Care Improvement Act); and (ii) consider established Federal designation systems and workforce assessments. (B) The Secretary shall review and update the criteria established under subparagraph (A) periodically to reflect current workforce needs. .",
      "versionDate": "2026-04-28",
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
        "name": "Health",
        "updateDate": "2026-05-18T18:47:20Z"
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
      "date": "2026-04-28",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s4416is.xml"
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
      "title": "PHS ACCESS Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-05-06T04:23:25Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Public Health Services for Advancing Care and Creating Efficient Support Systems in Underserved Communities Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-05-06T04:23:25Z"
    },
    {
      "title": "PHS ACCESS Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-05-06T04:23:25Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to establish procedures for the detailing of Public Health Service Officers for purposes of advancing care in underserved communities.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-05-06T04:18:26Z"
    }
  ]
}
```
