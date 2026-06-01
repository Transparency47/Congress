# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/584?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/584
- Title: Tax Fairness for Survivors Act
- Congress: 119
- Bill type: S
- Bill number: 584
- Origin chamber: Senate
- Introduced date: 2025-02-13
- Update date: 2025-12-06T07:02:09Z
- Update date including text: 2025-12-06T07:02:09Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-02-13: Introduced in Senate
- 2025-02-13 - IntroReferral: Introduced in Senate
- 2025-02-13 - IntroReferral: Read twice and referred to the Committee on Finance.
- Latest action: 2025-02-13: Introduced in Senate

## Actions

- 2025-02-13 - IntroReferral: Introduced in Senate
- 2025-02-13 - IntroReferral: Read twice and referred to the Committee on Finance.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-02-13",
    "latestAction": {
      "actionDate": "2025-02-13",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/584",
    "number": "584",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Taxation"
    },
    "sponsors": [
      {
        "bioguideId": "G000555",
        "district": "",
        "firstName": "Kirsten",
        "fullName": "Sen. Gillibrand, Kirsten E. [D-NY]",
        "lastName": "Gillibrand",
        "party": "D",
        "state": "NY"
      }
    ],
    "title": "Tax Fairness for Survivors Act",
    "type": "S",
    "updateDate": "2025-12-06T07:02:09Z",
    "updateDateIncludingText": "2025-12-06T07:02:09Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-02-13",
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
      "actionDate": "2025-02-13",
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
          "date": "2025-02-13T18:10:42Z",
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

## API Data: cosponsors

```json
{
  "cosponsors": [
    {
      "bioguideId": "B001243",
      "firstName": "Marsha",
      "fullName": "Sen. Blackburn, Marsha [R-TN]",
      "isOriginalCosponsor": "True",
      "lastName": "Blackburn",
      "party": "R",
      "sponsorshipDate": "2025-02-13",
      "state": "TN"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s584is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 584\nIN THE SENATE OF THE UNITED STATES\nFebruary 13, 2025 Mrs. Gillibrand (for herself and Mrs. Blackburn ) introduced the following bill; which was read twice and referred to the Committee on Finance\nA BILL\nTo amend the Internal Revenue Code of 1986 to exclude from gross income any judgments, awards, and settlements with respect to sexual assault or sexual harassment claims, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Tax Fairness for Survivors Act .\n#### 2. Exempting from Federal income taxation payments allocable to sexual assault or sexual harassment claims\n##### (a) In general\nPart III of subchapter B of chapter 1 of the Internal Revenue Code of 1986 is amended by inserting before section 140 the following new section:\n139J. Amounts received as judgments, awards, and settlements with respect to sexual assault or sexual harassment claims (a) In general In the case of an individual, gross income shall not include any amount received as a judgment, award, or settlement (including back pay, front pay, punitive damages, reimbursement of attorney's fees, or any payments made in connection with a release of claims or to resolve or settle claims), whether by lump sum or periodic payments, from\u2014 (1) a claim involving such individual as the victim of an alleged nonconsensual sexual act or sexual contact, as such terms are defined in section 2246 of title 18, United States Code, or similar applicable Tribal, State, or local law, including when the victim lacks capacity to consent, or (2) a claim involving conduct that is alleged to constitute sexual harassment of such individual under applicable Federal, Tribal, State, or local law. (b) Regulations and guidance The Secretary shall issue such regulations or other guidance as the Secretary determines necessary to carry out the purposes of this section, including regulations or other guidance to distinguish amounts received in connection with a claim described in subsection (a) from other amounts received as part of a judgment, award, or settlement. .\n##### (b) Social security taxes\nSection 3121(a) of such Code is amended by striking or at the end of paragraph (22), by striking the period at the end of paragraph (23) and inserting ; or , and by inserting after paragraph (23) the following new paragraph:\n(24) any amount received which is excludable from the gross income of the employee under section 139J. .\n##### (c) Railroad retirement tax\nSection 3231(e) of such Code is amended by adding at the end the following new paragraph:\n(13) Amounts received as judgments, awards, and settlements with respect to sexual assault or sexual harassment claims The term compensation shall not include any amount received which is excludable from the gross income of the employee under section 139J. .\n##### (d) Unemployment taxes\nSection 3306(b) of such Code is amended by striking or at the end of paragraph (19), by striking the period at the end of paragraph (20) and inserting ; or , and by inserting after paragraph (20) the following new paragraph:\n(21) any amount received which is excludable from the gross income of the employee under section 139J. .\n##### (e) Wage withholding\nSection 3401 of such Code is amended by striking or at the end of paragraph (22), by striking the period at the end of paragraph (23) and inserting , or , and by inserting after paragraph (23) the following new paragraph:\n(24) any amount received which is excludable from the gross income of the employee under section 139J. .\n##### (f) Clerical amendment\nThe table of sections for part III of subchapter B of chapter 1 of the Internal Revenue Code of 1986 is amended by inserting before the item relating to section 140 the following new item:\nSec. 139J. Amounts received as judgments, awards, and settlements with respect to sexual assault or sexual harassment claims. .\n##### (g) Effective date\nThe amendments made by this section shall apply to taxable years beginning after the date of the enactment of this Act.",
      "versionDate": "2025-02-13",
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
        "actionDate": "2025-02-13",
        "text": "Referred to the House Committee on Ways and Means."
      },
      "number": "1306",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Tax Fairness for Survivors Act",
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
        "name": "Taxation",
        "updateDate": "2025-05-06T16:35:52Z"
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
      "date": "2025-02-13",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s584is.xml"
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
      "title": "Tax Fairness for Survivors Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-03-12T02:38:28Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Tax Fairness for Survivors Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-12T02:38:22Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend the Internal Revenue Code of 1986 to exclude from gross income any judgements, awards, and settlements with respect to sexual assault or sexual harassment claims, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-12T02:33:23Z"
    }
  ]
}
```
