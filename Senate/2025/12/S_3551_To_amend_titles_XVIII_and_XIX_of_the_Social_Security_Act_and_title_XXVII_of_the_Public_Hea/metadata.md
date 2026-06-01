# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/3551?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/3551
- Title: PROTECT for Rare Act
- Congress: 119
- Bill type: S
- Bill number: 3551
- Origin chamber: Senate
- Introduced date: 2025-12-17
- Update date: 2026-01-20T15:11:19Z
- Update date including text: 2026-01-20T15:11:19Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-12-17: Introduced in Senate
- 2025-12-17 - IntroReferral: Introduced in Senate
- 2025-12-17 - IntroReferral: Read twice and referred to the Committee on Finance.
- Latest action: 2025-12-17: Introduced in Senate

## Actions

- 2025-12-17 - IntroReferral: Introduced in Senate
- 2025-12-17 - IntroReferral: Read twice and referred to the Committee on Finance.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-12-17",
    "latestAction": {
      "actionDate": "2025-12-17",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/3551",
    "number": "3551",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Health"
    },
    "sponsors": [
      {
        "bioguideId": "T000476",
        "district": "",
        "firstName": "Thomas",
        "fullName": "Sen. Tillis, Thomas [R-NC]",
        "lastName": "Tillis",
        "party": "R",
        "state": "NC"
      }
    ],
    "title": "PROTECT for Rare Act",
    "type": "S",
    "updateDate": "2026-01-20T15:11:19Z",
    "updateDateIncludingText": "2026-01-20T15:11:19Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-12-17",
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
      "actionDate": "2025-12-17",
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
          "date": "2025-12-17T22:44:51Z",
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
      "bioguideId": "H001046",
      "firstName": "Martin",
      "fullName": "Sen. Heinrich, Martin [D-NM]",
      "isOriginalCosponsor": "True",
      "lastName": "Heinrich",
      "party": "D",
      "sponsorshipDate": "2025-12-17",
      "state": "NM"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s3551is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 3551\nIN THE SENATE OF THE UNITED STATES\nDecember 17, 2025 Mr. Tillis (for himself and Mr. Heinrich ) introduced the following bill; which was read twice and referred to the Committee on Finance\nA BILL\nTo amend titles XVIII and XIX of the Social Security Act and title XXVII of the Public Health Service Act to provide for coverage of certain drugs used in the treatment or management of a rare disease or condition, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Providing Realistic Opportunity To Equal and Comparable Treatment for Rare Act or the PROTECT for Rare Act .\n#### 2. Coverage of certain drugs used in treatment or management of a rare disease or condition\n##### (a) Medicare\n**(1) Definition**\n**(A) In general**\nSection 1861(t)(2) of the Social Security Act ( 42 U.S.C. 1395x(t)(2) ) is amended\u2014\n**(i)**\nin subparagraph (A), by inserting after regimen the following: , or used in the treatment or management of a disease or condition affecting 200,000 or fewer individuals in the United States, ; and\n**(ii)**\nin subparagraph (B)(ii)\u2014\n**(I)**\nin subclause (I), by striking , or at the end and inserting a semicolon;\n**(II)**\nin subclause (II), by striking the period at the end and inserting ; or ; and\n**(III)**\nby adding at the end the following new subclause:\n(III) in the case of a drug that is used in the treatment or management of a disease or condition affecting 200,000 or fewer individuals in the United States, such use is supported by peer-reviewed medical literature, including clinical guidelines, and is not specifically listed as not indicated in one or more of the compendia described in section 1927(g)(1)(B)(i), or listed as contraindicated in the labeling approved by the Food and Drug Administration. .\n**(B) Effective date**\nThe amendments made by subparagraph (A) shall apply to items and services furnished on or after January 1, 2027..\n**(2) Medically accepted uses of covered part D drugs in treating rare conditions**\n**(A) In general**\nSection 1860D\u20132(e)(4)(A)(i) of the Social Security Act ( 42 U.S.C. 1395w\u2013104(e)(4)(A)(i) ) is amended, in the matter preceding subclause (I), by inserting or in the case of a covered part D drug used in the treatment or management of a disease or condition affecting 200,000 or fewer individuals in the United States, after regimen,\n**(B) Effective date**\nThe amendment made by subparagraph (A) shall apply to plan years beginning on or after January 1, 2027.\n##### (b) Medicaid\n**(1) In general**\nSection 1927(k)(6) of the Social Security Act ( 42 U.S.C. 1396r\u20138(k)(6) ) is amended to read as follows:\n(6) Medically accepted indication The term medically accepted indication means any use for a covered outpatient drug\u2014 (A) which is approved under the Federal Food, Drug, and Cosmetic Act; (B) which is supported by one or more citations included or approved for inclusion in any of the compendia described in subsection (g)(1)(B)(i); or (C) which, in the case of a drug used to treat or manage a disease or condition affecting 200,000 or fewer individuals in the United States\u2014 (i) is a use of such drug that is supported by peer-reviewed medical literature, clinical guidelines, or an expert in such disease or condition, as identified by a medical society involved in the treatment or management of such disease or condition; and (ii) is a use of such drug that is not listed as not indicated in the compendia described in subsection (g)(1)(B)(i), or listed as contraindicated in the labeling approved by the Food and Drug Administration. .\n**(2) Conforming amendment**\nSection 1927(d)(4)(C) of the Social Security Act ( 42 U.S.C. 1396r\u20138(d)(4)(C) ) is amended by striking compendia and inserting sources .\n**(3) Effective date**\nThe amendments made by this subsection shall apply with respect to covered outpatient drugs furnished on or after January 1, 2027.\n##### (c) Private health insurance\n**(1) In general**\n**(A) PHSA**\nPart D of title XXVII of the Public Health Service Act ( 42 U.S.C. 300gg\u2013111 et seq. ) is amended by adding at the end the following new section:\n2799A\u201311. Expedited process for review associated with certain drugs used in treatment or management of a rare disease or condition A group health plan or a health insurance issuer offering group or individual health insurance coverage shall provide an expedited process pursuant to section 2719 by which a participant, beneficiary, or enrollee, or a designee or prescribing physician (or other prescriber, as appropriate) of the participant, beneficiary, or enrollee, may appeal any denial of coverage for a drug or biological product\u2014 (1) approved under section 505 of the Federal Food, Drug, and Cosmetic Act or licensed under section 351; (2) for which the use is related to treatment or management of a disease or condition affecting 200,000 or fewer individuals in the United States; and (3) the use of which is supported by\u2014 (A) the labeling for the drug or biological product approved pursuant to such section 505 or 351; or (B) peer-reviewed literature, including clinical guidelines, and that is not reviewed unfavorably in the compendia described in section 1927(g)(1)(B)(i) of the Social Security Act and is not listed as a contraindication in such approved labeling. .\n**(B) ERISA**\n**(i) In general**\nSubpart B of part 7 of subtitle B of title I of the Employee Retirement Income Security Act of 1974 ( 29 U.S.C. 1185 et seq. ) is amended by adding at the end the following new section:\n736. Expedited process for review associated with certain drugs used in treatment or management of a rare disease or condition A group health plan or a health insurance issuer offering group health insurance coverage shall provide an expedited process pursuant to section 2719 of the Public Health Service Act ( 42 U.S.C. 300gg\u201319 ) by which a participant or beneficiary, or a designee or prescribing physician (or other prescriber, as appropriate) of the participant or beneficiary, may appeal any denial of coverage for a drug or biological product\u2014 (1) approved under section 505 of the Federal Food, Drug, and Cosmetic Act ( 21 U.S.C. 355 ) or licensed under section 351 of the Public Health Service Act ( 42 U.S.C. 262 ); (2) for which the use is related to treatment or management of a disease or condition affecting 200,000 or fewer individuals in the United States; and (3) the use of which is supported by\u2014 (A) the labeling for the drug or biological product approved pursuant to such section 505 or 351; or (B) peer-reviewed literature, including clinical guidelines, and that is not reviewed unfavorably in the compendia described in section 1927(g)(1)(B)(i) of the Social Security Act ( 42 U.S.C. 1396r\u20138(g)(1)(B)(i) ) and is not listed as a contraindication in such approved labeling. .\n**(ii) Clerical amendment**\nThe table of contents in section 1 of the Employee Retirement Income Security Act of 1974 ( 29 U.S.C. 1001 et seq. ) is amended by inserting after the item relating to section 725 the following new item:\nSec. 726. Expedited process for review associated with certain drugs used in treatment or management of a rare disease or condition. .\n**(C) IRC**\n**(i) In general**\nSubchapter B of chapter 100 of the Internal Revenue Code of 1986 is amended by adding at the end the following new section:\n9826. Expedited process for review associated with certain drugs used in treatment or management of a rare disease or condition A group health plan shall provide an expedited process pursuant to section 2719 of the Public Health Service Act ( 42 U.S.C. 300gg\u201319 ) by which a participant or beneficiary, or a designee or prescribing physician (or other prescriber, as appropriate) of the participant or beneficiary, may appeal any denial of coverage for a drug or biological product\u2014 (1) approved under section 505 of the Federal Food, Drug, and Cosmetic Act ( 21 U.S.C. 355 ) or licensed under section 351 of the Public Health Service Act ( 42 U.S.C. 262 ); (2) for which the use is related to treatment or management of a disease or condition affecting 200,000 or fewer individuals in the United States; and (3) the use of which is supported by\u2014 (A) the labeling for the drug or biological product approved pursuant to such section 505 or 351; or (B) peer-reviewed literature, including clinical guidelines, and that is not reviewed unfavorably in the compendia described in section 1927(g)(1)(B)(i) of the Social Security Act ( 42 U.S.C. 1396r\u20138(g)(1)(B)(i) ) and is not listed as a contraindication in such approved labeling. .\n**(ii) Clerical amendment**\nThe table of sections for subchapter B of chapter 100 of the Internal Revenue Code of 1986 is amended by adding at the end the following new item:\nSec. 9826. Expedited process for review associated with certain drugs used in treatment or management of a rare disease or condition.\n**(2) Effective date**\nThe amendments made by this subsection shall apply with respect to plan years beginning on or after January 1, 2027.",
      "versionDate": "2025-12-17",
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
        "updateDate": "2026-01-20T15:11:19Z"
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
      "date": "2025-12-17",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s3551is.xml"
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
      "title": "PROTECT for Rare Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-01-17T05:53:16Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "PROTECT for Rare Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-01-17T05:53:16Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Providing Realistic Opportunity To Equal and Comparable Treatment for Rare Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-01-17T05:53:16Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend titles XVIII and XIX of the Social Security Act and title XXVII of the Public Health Service Act to provide for coverage of certain drugs used in the treatment or management of a rare disease or condition, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-01-17T05:48:17Z"
    }
  ]
}
```
