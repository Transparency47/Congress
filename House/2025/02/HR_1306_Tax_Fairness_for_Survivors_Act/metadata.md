# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/1306?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/1306
- Title: Tax Fairness for Survivors Act
- Congress: 119
- Bill type: HR
- Bill number: 1306
- Origin chamber: House
- Introduced date: 2025-02-13
- Update date: 2025-12-06T06:58:42Z
- Update date including text: 2025-12-06T06:58:42Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-02-13: Introduced in House
- 2025-02-13 - IntroReferral: Introduced in House
- 2025-02-13 - IntroReferral: Introduced in House
- 2025-02-13 - IntroReferral: Referred to the House Committee on Ways and Means.
- Latest action: 2025-02-13: Introduced in House

## Actions

- 2025-02-13 - IntroReferral: Introduced in House
- 2025-02-13 - IntroReferral: Introduced in House
- 2025-02-13 - IntroReferral: Referred to the House Committee on Ways and Means.

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
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/1306",
    "number": "1306",
    "originChamber": "House",
    "policyArea": {
      "name": "Taxation"
    },
    "sponsors": [
      {
        "bioguideId": "F000462",
        "district": "22",
        "firstName": "Lois",
        "fullName": "Rep. Frankel, Lois [D-FL-22]",
        "lastName": "Frankel",
        "party": "D",
        "state": "FL"
      }
    ],
    "title": "Tax Fairness for Survivors Act",
    "type": "HR",
    "updateDate": "2025-12-06T06:58:42Z",
    "updateDateIncludingText": "2025-12-06T06:58:42Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-02-13",
      "committees": {
        "item": {
          "name": "Ways and Means Committee",
          "systemCode": "hswm00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Ways and Means.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-02-13",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-02-13",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
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
          "date": "2025-02-13T14:08:35Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Ways and Means Committee",
      "systemCode": "hswm00",
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
      "bioguideId": "T000478",
      "district": "24",
      "firstName": "Claudia",
      "fullName": "Rep. Tenney, Claudia [R-NY-24]",
      "isOriginalCosponsor": "True",
      "lastName": "Tenney",
      "party": "R",
      "sponsorshipDate": "2025-02-13",
      "state": "NY"
    },
    {
      "bioguideId": "N000193",
      "district": "3",
      "firstName": "Zachary",
      "fullName": "Rep. Nunn, Zachary [R-IA-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Nunn",
      "party": "R",
      "sponsorshipDate": "2025-03-24",
      "state": "IA"
    },
    {
      "bioguideId": "D000624",
      "district": "6",
      "firstName": "Debbie",
      "fullName": "Rep. Dingell, Debbie [D-MI-6]",
      "isOriginalCosponsor": "False",
      "lastName": "Dingell",
      "party": "D",
      "sponsorshipDate": "2025-03-24",
      "state": "MI"
    },
    {
      "bioguideId": "L000599",
      "district": "17",
      "firstName": "Michael",
      "fullName": "Rep. Lawler, Michael [R-NY-17]",
      "isOriginalCosponsor": "False",
      "lastName": "Lawler",
      "party": "R",
      "sponsorshipDate": "2025-04-03",
      "state": "NY"
    },
    {
      "bioguideId": "R000305",
      "district": "2",
      "firstName": "Deborah",
      "fullName": "Rep. Ross, Deborah K. [D-NC-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Ross",
      "middleName": "K.",
      "party": "D",
      "sponsorshipDate": "2025-04-03",
      "state": "NC"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1306ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 1306\nIN THE HOUSE OF REPRESENTATIVES\nFebruary 13, 2025 Ms. Lois Frankel of Florida (for herself and Ms. Tenney ) introduced the following bill; which was referred to the Committee on Ways and Means\nA BILL\nTo amend the Internal Revenue Code of 1986 to exclude from gross income any judgments, awards, and settlements with respect to sexual assault or sexual harassment claims, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Tax Fairness for Survivors Act .\n#### 2. Exempting from Federal income taxation payments allocable to sexual assault or sexual harassment claims\n##### (a) In general\nPart III of subchapter B of chapter 1 of the Internal Revenue Code of 1986 is amended by inserting before section 140 the following new section:\n139J. Amounts received as judgments, awards, and settlements with respect to sexual assault or sexual harassment claims (a) In general In the case of an individual, gross income shall not include any amount received as a judgment, award, or settlement (including backpay, frontpay, punitive damages, reimbursement of attorney\u2019s fees, or any payments made in connection with a release of claims or to resolve or settle claims) whether by lump sum or periodic payments from\u2014 (1) a claim involving the individual as the victim of an alleged nonconsensual sexual act or sexual contact, as such terms are defined in section 2246 of title 18, United States Code, or similar applicable Tribal, State, or local law, including when the victim lacks capacity to consent, or (2) a claim involving conduct that is alleged to constitute sexual harassment of the individual under applicable Federal, Tribal, State, or local law. (b) Regulations The Secretary shall prescribe such regulations and other guidance as are necessary to carry out the purposes of section, including regulations and other guidance to distinguish amounts received in connection with a claim described in subsection (a) from other amounts received. .\n##### (b) Social security taxes\nSection 3121(a) of such Code is amended by striking or at the end of paragraph (22), by striking the period at the end of paragraph (23) and inserting ; or , and by inserting after paragraph (23) the following new paragraph:\n(24) any amount received which is excludable from the gross income of the employee under section 139J. .\n##### (c) Railroad retirement tax\nSection 3231(e) of such Code is amended by adding at the end the following new paragraph:\n(13) Amounts received as judgments, awards, and settlements with respect to sexual assault or sexual harassment claims The term compensation shall not include any amount received which is excludable from the gross income of the employee under section 139J. .\n##### (d) Unemployment taxes\nSection 3306(b) of such Code is amended by striking or at the end of paragraph (19), by striking the period at the end of paragraph (20) and inserting , or , and by inserting after paragraph (20) the following new paragraph:\n(21) any amount received which is excludable from the gross income of the employee under section 139J. .\n##### (e) Wage withholding\nSection 3401 of such Code is amended by striking or at the end of paragraph (22), by striking the period at the end of paragraph (23) and inserting , or , and by inserting after paragraph (23) the following new paragraph:\n(24) any amount received which is excludable from the gross income of the employee under section 139J. .\n##### (f) Clerical amendment\nThe table of sections for part III of subchapter B of chapter 1 of the Internal Revenue Code of 1986 is amended by inserting before the item relating to section 140 the following new item:\nSec. 139J. Amounts received as judgments, awards, and settlements with respect to sexual assault or sexual harassment claims. .\n##### (g) Effective date\nThe amendments made by this section shall apply to taxable years beginning after the date of the enactment of this Act.",
      "versionDate": "2025-02-13",
      "versionType": "Introduced in House"
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
        "text": "Read twice and referred to the Committee on Finance."
      },
      "number": "584",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Tax Fairness for Survivors Act",
      "type": "S"
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
        "updateDate": "2025-05-06T15:42:31Z"
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
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1306ih.xml"
        }
      ],
      "type": "Introduced in House"
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
      "updateDate": "2025-03-12T15:08:22Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Tax Fairness for Survivors Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-12T15:08:21Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Internal Revenue Code of 1986 to exclude from gross income any judgments, awards, and settlements with respect to sexual assault or sexual harassment claims, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-12T15:03:33Z"
    }
  ]
}
```
