# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/3954?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/3954
- Title: No Lifeline for Dead People Act
- Congress: 119
- Bill type: S
- Bill number: 3954
- Origin chamber: Senate
- Introduced date: 2026-02-26
- Update date: 2026-03-23T15:09:20Z
- Update date including text: 2026-03-23T15:09:20Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, subjects, text, titles

## Timeline

- 2026-02-26: Introduced in Senate
- 2026-02-26 - IntroReferral: Introduced in Senate
- 2026-02-26 - IntroReferral: Read twice and referred to the Committee on Commerce, Science, and Transportation.
- Latest action: 2026-02-26: Introduced in Senate

## Actions

- 2026-02-26 - IntroReferral: Introduced in Senate
- 2026-02-26 - IntroReferral: Read twice and referred to the Committee on Commerce, Science, and Transportation.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-02-26",
    "latestAction": {
      "actionDate": "2026-02-26",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/3954",
    "number": "3954",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Science, Technology, Communications"
    },
    "sponsors": [
      {
        "bioguideId": "E000295",
        "district": "",
        "firstName": "Joni",
        "fullName": "Sen. Ernst, Joni [R-IA]",
        "lastName": "Ernst",
        "party": "R",
        "state": "IA"
      }
    ],
    "title": "No Lifeline for Dead People Act",
    "type": "S",
    "updateDate": "2026-03-23T15:09:20Z",
    "updateDateIncludingText": "2026-03-23T15:09:20Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-02-26",
      "committees": {
        "item": {
          "name": "Commerce, Science, and Transportation Committee",
          "systemCode": "sscm00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Commerce, Science, and Transportation.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2026-02-26",
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
          "date": "2026-02-26T19:49:40Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Commerce, Science, and Transportation Committee",
      "systemCode": "sscm00",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s3954is.xml",
      "text": "II\n119th CONGRESS\n2d Session\nS. 3954\nIN THE SENATE OF THE UNITED STATES\nFebruary 26, 2026 Ms. Ernst introduced the following bill; which was read twice and referred to the Committee on Commerce, Science, and Transportation\nA BILL\nTo terminate the ability of eligible telecommunications carriers in certain States to use State eligibility determination processes in place of the National Verifier to determine the eligibility of consumers for Lifeline service.\n#### 1. Short title\nThis Act may be cited as the No Lifeline for Dead People Act .\n#### 2. Mandatory use of National Verifier to determine Lifeline eligibility\n##### (a) Definitions\nIn this section:\n**(1) Eligible telecommunications carrier**\nThe term eligible telecommunications carrier means a common carrier designated as an eligible telecommunications carrier under section 214(e) of the Communications Act of 1934 ( 47 U.S.C. 214(e) ).\n**(2) Lifeline service**\nThe term Lifeline service means voice telephony service or broadband internet access service provided under the program set forth in subpart E of part 54 of title 47, Code of Federal Regulations, or any successor regulation.\n**(3) National Verifier**\nThe term National Verifier has the meaning given the term in section 54.400 of title 47, Code of Federal Regulations, or any successor regulation.\n##### (b) Mandatory use of National Verifier\nAn eligible telecommunications carrier may not provide Lifeline service to a consumer unless the carrier has used the National Verifier to verify the eligibility of the consumer for Lifeline service.",
      "versionDate": "2026-02-26",
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
        "name": "Science, Technology, Communications",
        "updateDate": "2026-03-23T15:09:20Z"
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
      "date": "2026-02-26",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s3954is.xml"
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
      "title": "No Lifeline for Dead People Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-03-19T03:23:27Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "No Lifeline for Dead People Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-03-19T03:23:25Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to terminate the ability of eligible telecommunications carriers in certain States to use State eligibility determination processes in place of the National Verifier to determine the eligibility of consumers for Lifeline service.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-03-19T03:18:32Z"
    }
  ]
}
```
