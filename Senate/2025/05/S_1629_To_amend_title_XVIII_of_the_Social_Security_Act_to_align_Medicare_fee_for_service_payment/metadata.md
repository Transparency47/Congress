# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/1629?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/s/1629
- Title: Same Care, Lower Cost Act
- Congress: 119
- Bill type: S
- Bill number: 1629
- Origin chamber: Senate
- Introduced date: 2025-05-06
- Update date: 2025-05-28T12:30:06Z
- Update date including text: 2025-05-28T12:30:06Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, subjects, text, titles

## Timeline

- 2025-05-06: Introduced in Senate
- 2025-05-06 - IntroReferral: Introduced in Senate
- 2025-05-06 - IntroReferral: Read twice and referred to the Committee on Finance.
- Latest action: 2025-05-06: Introduced in Senate

## Actions

- 2025-05-06 - IntroReferral: Introduced in Senate
- 2025-05-06 - IntroReferral: Read twice and referred to the Committee on Finance.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-05-06",
    "latestAction": {
      "actionDate": "2025-05-06",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/s/1629",
    "number": "1629",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Health"
    },
    "sponsors": [
      {
        "bioguideId": "K000393",
        "district": "",
        "firstName": "John",
        "fullName": "Sen. Kennedy, John [R-LA]",
        "lastName": "Kennedy",
        "party": "R",
        "state": "LA"
      }
    ],
    "title": "Same Care, Lower Cost Act",
    "type": "S",
    "updateDate": "2025-05-28T12:30:06Z",
    "updateDateIncludingText": "2025-05-28T12:30:06Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-05-06",
      "committees": {
        "item": {
          "name": "Finance Committee",
          "systemCode": "ssfi00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Finance.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-05-06",
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
          "date": "2025-05-06T21:12:04Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Finance Committee",
      "systemCode": "ssfi00",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1629is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 1629\nIN THE SENATE OF THE UNITED STATES\nMay 6, 2025 Mr. Kennedy introduced the following bill; which was read twice and referred to the Committee on Finance\nA BILL\nTo amend title XVIII of the Social Security Act to align Medicare fee-for-service payment rates across ambulatory settings.\n#### 1. Short title\nThis Act may be cited as the Same Care, Lower Cost Act .\n#### 2. Aligning Medicare fee-for-service payment rates across ambulatory settings\n##### (a) In general\nSection 1834 of the Social Security Act ( 42 U.S.C. 1395m ) is amended by adding at the end the following new subsection:\n(aa) Site neutral payments for certain services furnished in ambulatory settings (1) In general For items and services furnished in a specified ambulatory setting during 2027 or a subsequent year and included in an ambulatory payment classifications identified pursuant to paragraph (2) for such year, payment under this part shall be made at the applicable site neutral payment rate under this part (as determined by the Secretary) if the requirements for such payment are otherwise met. (2) Identification of services to which site neutral payments apply For 2027 and subsequent years: (A) Identification (i) In general The Secretary shall identify not fewer than 66 ambulatory payment classifications for site neutral payments which are appropriately furnished in either a hospital outpatient department, ambulatory surgical center, or other setting determined appropriate by the Secretary. (ii) Additional APCs The Secretary may add additional ambulatory payment classifications to those identified under clause (i) as the Secretary determines clinically appropriate (B) Exception The Secretary shall reclassify the ambulatory payment classifications for emergency department visits, critical care visits, and trauma care visits at a hospital outpatient department as Comprehensive APCs, in which all the items and services on the same claim are packaged into a single payment unit. Any item or service that is provided with such a visit so reclassified shall not be treated as an item or service identified under subparagraph (A), and shall not be subject to the provisions of paragraph (1). The Secretary may, pursuant to rulemaking, specify exceptions to any reclassification under the first sentence of this subparagraph. (3) Consideration of MedPAC recommendations In carrying out this subsection (including the identification of services under paragraph (2)), the Secretary shall take into consideration the recommendations of the Medicare Payment Advisory Commission in Chapter 8 (entitled Aligning fee-for-service payment rates across ambulatory settings ) of its Medicare and the Health Care Delivery System report submitted to Congress in June 2023. (4) Definition of specified ambulatory setting In this subsection, the term specified ambulatory setting means a hospital outpatient department, ambulatory surgical center, or other setting determined appropriate by the Secretary. .\n##### (b) Conforming amendments\n**(1) Payment system for ambulatory surgical center services**\nSection 1833(i)(2)(D)(i) of the Social Security Act ( 42 U.S.C. 1395l(i)(2)(D)(i) ) is amended by striking for payment and inserting for, subject to section 1834(aa), payment .\n**(2) HOPD fee schedule**\nSection 1833(t) of the Social Security Act ( 42 U.S.C. 1395l(t) ) is amended\u2014\n**(A)**\nin paragraph (1)(A), by striking the amount of payment and inserting subject to section 1834(aa), the amount of payment ; and\n**(B)**\nin paragraph (9)(B), by adding at the end the following: In determining adjustments under this subparagraph for 2027 or a subsequent year, the Secretary shall not take into account under this subparagraph or paragraph (2)(E) any changes in expenditures as a result of the application of section 1834(aa).\n**(3) Physician fee schedule**\nSection 1848(a)(1)(B) of the Social Security Act ( 42 U.S.C. 1395w\u20134(a)(1)(B) ) is amended by inserting and section 1834(aa) after succeeding provisions of this subsection .",
      "versionDate": "2025-05-06",
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
        "updateDate": "2025-05-28T12:30:06Z"
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
      "date": "2025-05-06",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1629is.xml"
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
      "title": "Same Care, Lower Cost Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-05-21T04:08:22Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Same Care, Lower Cost Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-05-21T04:08:19Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend title XVIII of the Social Security Act to align Medicare fee-for-service payment rates across ambulatory settings.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-05-21T04:03:29Z"
    }
  ]
}
```
