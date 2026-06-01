# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/2542?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/2542
- Title: Old Drugs, New Cures Act
- Congress: 119
- Bill type: HR
- Bill number: 2542
- Origin chamber: House
- Introduced date: 2025-04-01
- Update date: 2026-05-04T15:17:50Z
- Update date including text: 2026-05-04T15:17:50Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-04-01: Introduced in House
- 2025-04-01 - IntroReferral: Introduced in House
- 2025-04-01 - IntroReferral: Introduced in House
- 2025-04-01 - IntroReferral: Referred to the Committee on Energy and Commerce, and in addition to the Committee on Ways and Means, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-04-01 - IntroReferral: Referred to the Committee on Energy and Commerce, and in addition to the Committee on Ways and Means, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- Latest action: 2025-04-01: Introduced in House

## Actions

- 2025-04-01 - IntroReferral: Introduced in House
- 2025-04-01 - IntroReferral: Introduced in House
- 2025-04-01 - IntroReferral: Referred to the Committee on Energy and Commerce, and in addition to the Committee on Ways and Means, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-04-01 - IntroReferral: Referred to the Committee on Energy and Commerce, and in addition to the Committee on Ways and Means, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-04-01",
    "latestAction": {
      "actionDate": "2025-04-01",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/2542",
    "number": "2542",
    "originChamber": "House",
    "policyArea": {
      "name": "Health"
    },
    "sponsors": [
      {
        "bioguideId": "D000230",
        "district": "1",
        "firstName": "Donald",
        "fullName": "Rep. Davis, Donald G. [D-NC-1]",
        "lastName": "Davis",
        "party": "D",
        "state": "NC"
      }
    ],
    "title": "Old Drugs, New Cures Act",
    "type": "HR",
    "updateDate": "2026-05-04T15:17:50Z",
    "updateDateIncludingText": "2026-05-04T15:17:50Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-04-01",
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
      "text": "Referred to the Committee on Energy and Commerce, and in addition to the Committee on Ways and Means, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-04-01",
      "committees": {
        "item": {
          "name": "Energy and Commerce Committee",
          "systemCode": "hsif00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the Committee on Energy and Commerce, and in addition to the Committee on Ways and Means, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-04-01",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-04-01",
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
          "date": "2025-04-01T14:02:50Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Ways and Means Committee",
      "systemCode": "hswm00",
      "type": "Standing"
    },
    {
      "activities": {
        "item": {
          "date": "2025-04-01T14:02:45Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Energy and Commerce Committee",
      "systemCode": "hsif00",
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
      "bioguideId": "P000048",
      "district": "11",
      "firstName": "August",
      "fullName": "Rep. Pfluger, August [R-TX-11]",
      "isOriginalCosponsor": "True",
      "lastName": "Pfluger",
      "party": "R",
      "sponsorshipDate": "2025-04-01",
      "state": "TX"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr2542ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 2542\nIN THE HOUSE OF REPRESENTATIVES\nApril 1, 2025 Mr. Davis of North Carolina (for himself and Mr. Pfluger ) introduced the following bill; which was referred to the Committee on Energy and Commerce , and in addition to the Committee on Ways and Means , for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned\nA BILL\nTo amend titles XVIII and XIX of the Social Security Act to provide that priority research drugs shall not be treated as line extensions of existing drugs for purposes of calculating manufacturer rebates under the Medicare and Medicaid programs, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Old Drugs, New Cures Act .\n#### 2. Priority research drugs\n##### (a) In general\nSection 1927(c)(2)(C) of the Social Security Act ( 42 U.S.C. 1396r\u20138(c)(2)(C) ) is amended by inserting the following new clause before the flush matter at the end:\n(iv) Priority research drug (I) Request for designation Not later than 90 days following the date of enactment of this clause, the Secretary shall establish and make effective a process for the manufacturer of a covered outpatient drug to request that the Secretary designate the drug as a priority research drug. (II) Designation Not later than 60 calendar days after the receipt of a request under subclause (I), the Secretary shall designate a covered outpatient drug as a priority research drug so long as it meets the following criteria: (aa) As of the date of submission of such request, at least 10 years have elapsed since the date the drug was approved under section 505(c) of the Federal Food, Drug, and Cosmetic Act or section 351(a) of the Public Health Service Act. (bb) The manufacturer of the drug is investigating such drug under section 505(i) of the Federal Food, Drug, and Cosmetic Act or section 351(a)(3) of the Public Health Service Act for a new indication that would address a significant unmet medical need because there is no alternative drug approved under section 505 of the Federal Food, Drug, and Cosmetic Act or licensed under section 351 of the Public Health Service Act for such indication on the date that the request under subclause (I) was submitted to the Secretary. (cc) The new indication described in item (bb) is for a disease or condition that has a high prevalence among beneficiaries of Federal health care programs. For purposes of this clause, a disease or condition has a high prevalence among beneficiaries of Federal health care programs if at least 33 percent of claims in the population targeted by the new indication during the prior calendar year were paid for under\u2014 (AA) a State plan under this title or a State child health plan under title XXI; (BB) part D of title XVIII with respect to an individual who is eligible for subsidies under section 1860D\u201314; (CC) the drug discount program under section 340B of the Public Health Service Act ( 42 U.S.C. 256b ; or (DD) a health care program administered by the Department of Veterans Affairs. .\n##### (b) Exclusion of priority research drugs from Medicaid definition of line extension\nThe flush matter at the end of section 1927(c)(2)(C) of the Social Security Act ( 42 U.S.C. 1396r\u20138(c)(2)(C) ) is amended by inserting a priority research drug (as designated under clause (iv)) or after does not include .\n##### (c) Exclusion of priority research drugs from Medicaid best price special rule for selected drugs\nSection 1927(c)(1)(C)(ii)(V) of the Social Security Act ( 42 U.S.C. 1396r\u20138(c)(1)(C)(ii)(V) ) is amended by inserting unless such drug is also designated as a priority research drug under paragraph (2)(C)(iv) during such period before the period.\n##### (d) Exclusion of priority research drugs from Medicare definition of line extension\nSection 1860D\u201314B(b)(5)(B)(ii) of the Social Security Act (42 U.S.C. 1395w\u2013114b(b)(5)(B)(ii)) is amended by inserting a priority research drug (as designated under section 1927(c)(2)(C)(iv)) or after does not include .",
      "versionDate": "2025-04-01",
      "versionType": "Introduced in House"
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
        "updateDate": "2025-04-08T12:55:26Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-04-01",
    "originChamber": "House",
    "payload": {
      "dublinCore": {
        "contributor": "Congressional Research Service, Library of Congress",
        "description": "This file contains bill summaries for federal legislation. A bill summary describes the most significant provisions of a piece of legislation and details the effects the legislative text may have on current law and federal programs. Bill summaries are authored by the Congressional Research Service (CRS) of the Library of Congress. As stated in Public Law 91-510 (2 USC 166 (d)(6)), one of the duties of CRS is \"to prepare summaries and digests of bills and resolutions of a public general nature introduced in the Senate or House of Representatives\". For more information, refer to the User Guide that accompanies this file.",
        "format": "text/xml",
        "language": "EN",
        "rights": "Pursuant to Title 17 Section 105 of the United States Code, this file is not subject to copyright protection and is in the public domain."
      },
      "item": {
        "@attributes": {
          "congress": "119",
          "measure-id": "id119hr2542",
          "measure-number": "2542",
          "measure-type": "hr",
          "orig-publish-date": "2025-04-01",
          "originChamber": "HOUSE",
          "update-date": "2026-05-04"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr2542v00",
            "update-date": "2026-05-04"
          },
          "action-date": "2025-04-01",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Old Drugs, New Cures Act</strong></p><p>This bill exempts manufacturers of certain long-standing drugs from paying specialized rebates under the Medicaid Drug Rebate Program and the Medicare Prescription Drug Inflation Rebate Program. (Under these programs, drug manufacturers pay rebates to state Medicaid programs for certain drugs covered under Medicaid and to the Centers for Medicare & Medicaid Services for certain drugs covered under Medicare.)</p><p>Specifically, manufacturers may request that a drug that would otherwise be considered a line extension under the Medicaid and Medicare rebate programs to instead be designated as a priority research drug. (A <em>line extension</em> refers to an oral dose of a new formulation of an existing drug, such as an extended release formulation, that would subject the drug to specialized rebates under the Medicaid and Medicare drug rebate programs.)</p><p>Under the bill, a drug qualifies as a <em>priority research\u00a0drug</em> if (1) at least 10 years have elapsed since the drug was first approved, (2) the manufacturer is investigating a new use of the drug that would address a significant unmet need, and (3) the new use addresses a disease or condition that has a high prevalence among beneficiaries of Medicaid, Medicare, or other federal health care programs.\u00a0</p>"
        },
        "title": "Old Drugs, New Cures Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr2542.xml",
    "summary": {
      "actionDate": "2025-04-01",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Old Drugs, New Cures Act</strong></p><p>This bill exempts manufacturers of certain long-standing drugs from paying specialized rebates under the Medicaid Drug Rebate Program and the Medicare Prescription Drug Inflation Rebate Program. (Under these programs, drug manufacturers pay rebates to state Medicaid programs for certain drugs covered under Medicaid and to the Centers for Medicare & Medicaid Services for certain drugs covered under Medicare.)</p><p>Specifically, manufacturers may request that a drug that would otherwise be considered a line extension under the Medicaid and Medicare rebate programs to instead be designated as a priority research drug. (A <em>line extension</em> refers to an oral dose of a new formulation of an existing drug, such as an extended release formulation, that would subject the drug to specialized rebates under the Medicaid and Medicare drug rebate programs.)</p><p>Under the bill, a drug qualifies as a <em>priority research\u00a0drug</em> if (1) at least 10 years have elapsed since the drug was first approved, (2) the manufacturer is investigating a new use of the drug that would address a significant unmet need, and (3) the new use addresses a disease or condition that has a high prevalence among beneficiaries of Medicaid, Medicare, or other federal health care programs.\u00a0</p>",
      "updateDate": "2026-05-04",
      "versionCode": "id119hr2542"
    },
    "title": "Old Drugs, New Cures Act"
  },
  "summaries": [
    {
      "actionDate": "2025-04-01",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Old Drugs, New Cures Act</strong></p><p>This bill exempts manufacturers of certain long-standing drugs from paying specialized rebates under the Medicaid Drug Rebate Program and the Medicare Prescription Drug Inflation Rebate Program. (Under these programs, drug manufacturers pay rebates to state Medicaid programs for certain drugs covered under Medicaid and to the Centers for Medicare & Medicaid Services for certain drugs covered under Medicare.)</p><p>Specifically, manufacturers may request that a drug that would otherwise be considered a line extension under the Medicaid and Medicare rebate programs to instead be designated as a priority research drug. (A <em>line extension</em> refers to an oral dose of a new formulation of an existing drug, such as an extended release formulation, that would subject the drug to specialized rebates under the Medicaid and Medicare drug rebate programs.)</p><p>Under the bill, a drug qualifies as a <em>priority research\u00a0drug</em> if (1) at least 10 years have elapsed since the drug was first approved, (2) the manufacturer is investigating a new use of the drug that would address a significant unmet need, and (3) the new use addresses a disease or condition that has a high prevalence among beneficiaries of Medicaid, Medicare, or other federal health care programs.\u00a0</p>",
      "updateDate": "2026-05-04",
      "versionCode": "id119hr2542"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-04-01",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr2542ih.xml"
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
      "title": "Old Drugs, New Cures Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-04-08T04:23:16Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Old Drugs, New Cures Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-04-08T04:23:15Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend titles XVIII and XIX of the Social Security Act to provide that priority research drugs shall not be treated as line extensions of existing drugs for purposes of calculating manufacturer rebates under the Medicare and Medicaid programs, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-04-08T04:18:26Z"
    }
  ]
}
```
