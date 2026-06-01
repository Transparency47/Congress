# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/3712?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/3712
- Title: BO’s Act
- Congress: 119
- Bill type: S
- Bill number: 3712
- Origin chamber: Senate
- Introduced date: 2026-01-28
- Update date: 2026-03-13T11:03:18Z
- Update date including text: 2026-03-13T11:03:18Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2026-01-28: Introduced in Senate
- 2026-01-28 - IntroReferral: Introduced in Senate
- 2026-01-28 - IntroReferral: Read twice and referred to the Committee on Health, Education, Labor, and Pensions.
- Latest action: 2026-01-28: Introduced in Senate

## Actions

- 2026-01-28 - IntroReferral: Introduced in Senate
- 2026-01-28 - IntroReferral: Read twice and referred to the Committee on Health, Education, Labor, and Pensions.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-01-28",
    "latestAction": {
      "actionDate": "2026-01-28",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/3712",
    "number": "3712",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Health"
    },
    "sponsors": [
      {
        "bioguideId": "H001079",
        "district": "",
        "firstName": "Cindy",
        "fullName": "Sen. Hyde-Smith, Cindy [R-MS]",
        "lastName": "Hyde-Smith",
        "party": "R",
        "state": "MS"
      }
    ],
    "title": "BO\u2019s Act",
    "type": "S",
    "updateDate": "2026-03-13T11:03:18Z",
    "updateDateIncludingText": "2026-03-13T11:03:18Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-01-28",
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
      "actionDate": "2026-01-28",
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
          "date": "2026-01-28T17:42:28Z",
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
      "bioguideId": "C001113",
      "firstName": "Catherine",
      "fullName": "Sen. Cortez Masto, Catherine [D-NV]",
      "isOriginalCosponsor": "True",
      "lastName": "Cortez Masto",
      "party": "D",
      "sponsorshipDate": "2026-01-28",
      "state": "NV"
    },
    {
      "bioguideId": "B001319",
      "firstName": "Katie",
      "fullName": "Sen. Britt, Katie Boyd [R-AL]",
      "isOriginalCosponsor": "False",
      "lastName": "Britt",
      "party": "R",
      "sponsorshipDate": "2026-02-04",
      "state": "AL"
    },
    {
      "bioguideId": "O000174",
      "firstName": "Jon",
      "fullName": "Sen. Ossoff, Jon [D-GA]",
      "isOriginalCosponsor": "False",
      "lastName": "Ossoff",
      "party": "D",
      "sponsorshipDate": "2026-03-05",
      "state": "GA"
    },
    {
      "bioguideId": "W000437",
      "firstName": "Roger",
      "fullName": "Sen. Wicker, Roger F. [R-MS]",
      "isOriginalCosponsor": "False",
      "lastName": "Wicker",
      "middleName": "F.",
      "party": "R",
      "sponsorshipDate": "2026-03-12",
      "state": "MS"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s3712is.xml",
      "text": "II\n119th CONGRESS\n2d Session\nS. 3712\nIN THE SENATE OF THE UNITED STATES\nJanuary 28, 2026 Mrs. Hyde-Smith (for herself and Ms. Cortez Masto ) introduced the following bill; which was read twice and referred to the Committee on Health, Education, Labor, and Pensions\nA BILL\nTo direct the Secretary of Health and Human Services to conduct, and submit to Congress a report describing the results of, a study on the use of home cardiorespiratory monitors for infants, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Baby Observation Act or the BO\u2019s Act .\n#### 2. Study and report on home cardiorespiratory monitors for infants\n##### (a) Study\nThe Secretary of Health and Human Services (in this section referred to as the Secretary ), pursuant to section 1121(a) of the Public Health Service Act ( 42 U.S.C. 300c\u201311(a) ), shall conduct a study on the use of home cardiorespiratory monitors for infants in relation to the prevention of sudden unexpected infant death (as defined in section 1121(e) of such Act ( 42 U.S.C. 300c\u201311(e) )).\n##### (b) Report\nNot later than 1 year after the date of enactment of this Act, the Secretary shall submit to Congress a report describing the results of the study under subsection (a). Such report shall include the following:\n**(1)**\nEvidence on the effectiveness, performance, and accuracy of home cardiorespiratory monitors that track the heart rate, blood oxygen levels, and other vital signs of an infant, particularly those infants who are high-risk.\n**(2)**\nNew models of care to improve the home sleeping environment of an infant, including the use of cardiorespiratory monitors.\n**(3)**\nHealth care plan criteria for medically appropriate coverage for a home cardiorespiratory monitor.\n**(4)**\nRecommendations on whether home cardiorespiratory monitors have shown product efficacy supporting coverage under public or private health insurance plans.",
      "versionDate": "2026-01-28",
      "versionType": "Introduced in Senate"
    }
  ]
}
```

## API Data: relatedbills

```json
{
  "relatedBills": [
    {
      "congress": "119",
      "latestAction": {
        "actionDate": "2025-03-14",
        "text": "Referred to the House Committee on Energy and Commerce."
      },
      "number": "2168",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "BO\u2019s Act",
      "type": "HR"
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
        "updateDate": "2026-02-25T16:27:04Z"
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
      "date": "2026-01-28",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s3712is.xml"
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
      "title": "BO\u2019s Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-03-13T11:03:18Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "BO\u2019s Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-02-19T03:53:20Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Baby Observation Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-02-19T03:53:20Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to direct the Secretary of Health and Human Services to conduct, and submit to Congress a report describing the results of, a study on the use of home cardiorespiratory monitors for infants, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-02-19T03:48:34Z"
    }
  ]
}
```
