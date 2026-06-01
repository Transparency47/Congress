# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/1641?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/1641
- Title: RESTORE Act
- Congress: 119
- Bill type: S
- Bill number: 1641
- Origin chamber: Senate
- Introduced date: 2025-05-07
- Update date: 2025-12-05T22:59:13Z
- Update date including text: 2025-12-05T22:59:13Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-05-07: Introduced in Senate
- 2025-05-07 - IntroReferral: Introduced in Senate
- 2025-05-07 - IntroReferral: Read twice and referred to the Committee on Armed Services.
- Latest action: 2025-05-07: Introduced in Senate

## Actions

- 2025-05-07 - IntroReferral: Introduced in Senate
- 2025-05-07 - IntroReferral: Read twice and referred to the Committee on Armed Services.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-05-07",
    "latestAction": {
      "actionDate": "2025-05-07",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/1641",
    "number": "1641",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Armed Forces and National Security"
    },
    "sponsors": [
      {
        "bioguideId": "C001098",
        "district": "",
        "firstName": "Ted",
        "fullName": "Sen. Cruz, Ted [R-TX]",
        "lastName": "Cruz",
        "party": "R",
        "state": "TX"
      }
    ],
    "title": "RESTORE Act",
    "type": "S",
    "updateDate": "2025-12-05T22:59:13Z",
    "updateDateIncludingText": "2025-12-05T22:59:13Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-05-07",
      "committees": {
        "item": {
          "name": "Armed Services Committee",
          "systemCode": "ssas00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Armed Services.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-05-07",
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
          "date": "2025-05-07T19:14:58Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Armed Services Committee",
      "systemCode": "ssas00",
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
      "bioguideId": "B001319",
      "firstName": "Katie",
      "fullName": "Sen. Britt, Katie Boyd [R-AL]",
      "isOriginalCosponsor": "True",
      "lastName": "Britt",
      "party": "R",
      "sponsorshipDate": "2025-05-07",
      "state": "AL"
    },
    {
      "bioguideId": "L000577",
      "firstName": "Mike",
      "fullName": "Sen. Lee, Mike [R-UT]",
      "isOriginalCosponsor": "True",
      "lastName": "Lee",
      "party": "R",
      "sponsorshipDate": "2025-05-07",
      "state": "UT"
    },
    {
      "bioguideId": "S001217",
      "firstName": "Rick",
      "fullName": "Sen. Scott, Rick [R-FL]",
      "isOriginalCosponsor": "True",
      "lastName": "Scott",
      "party": "R",
      "sponsorshipDate": "2025-05-07",
      "state": "FL"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1641is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 1641\nIN THE SENATE OF THE UNITED STATES\nMay 7, 2025 Mr. Cruz (for himself, Mrs. Britt , Mr. Lee , and Mr. Scott of Florida ) introduced the following bill; which was read twice and referred to the Committee on Armed Services\nA BILL\nTo restore fairness to service members who filed religious accommodation requests and ensure their career progression is justly reviewed.\n#### 1. Short title\nThis Act may be cited as the Reaffirming Every Servicemembers' Trust Of Religious Exemptions Act or the RESTORE Act .\n#### 2. Establishment of the special review board for impacted service members\n##### (a) Establishment of review board\nThe Secretary of Defense shall convene a special review board under the Deputy Under Secretary of Defense for Personnel and Readiness to audit religious accommodation requests and disposition and review the personnel records of each service member who filed a religious accommodation request specifically for the COVID\u201319 vaccine and remained in service (in this section referred to as the Special Review Board ).\n##### (b) Duties of the review board\nThe Special Review Board shall perform the following duties:\n**(1) Audit scope of religious accommodation decisions since 2020**\nConduct a Department of Defense-wide audit to assess full number of submissions, approvals, and consistency of compliance with the Religious freedom Restoration Act of 1993 (RFRA) ( 42 U.S.C. 2000bb et seq. ).\n**(2) Assess career impact**\nDetermine whether the service member\u2019s career progression, promotions, assignments, retention, or professional development opportunities were negatively affected by their religious accommodation request or COVID\u201319 vaccine refusal.\n**(3) Adjudicate career restorations**\nDetermine and take corrective action if the service member is eligible for\u2014\n**(A)**\nbackdated promotion to the rank they would have achieved absent the adverse impact;\n**(B)**\ncorrection of their Date of Rank (DOR) to align with their peer group;\n**(C)**\nrestoration of lost pay and benefits, including back pay, retirement contributions, and applicable bonuses; and\n**(D)**\nreinstatement to service if they left service due to denial of religious accommodation that has since been determined as unlawful.\n**(4) Expungement of adverse actions**\nEnsure that all adverse administrative actions related to refusal of the COVID\u201319 vaccine (or other protected religious accommodation) are expunged from the service member\u2019s record, including\u2014\n**(A)**\nadministrative reprimands;\n**(B)**\nnegative or inconsistent evaluations;\n**(C)**\npromotion delays or denials;\n**(D)**\nissuance of Inactive Duty Training points to reserve component personnel so that if affected they shall receive a satisfactory year for participation; and\n**(E)**\ncareer assignment considerations to improve service-member competitiveness previously impacted solely due to vaccine refusal (or religious accommodation).\n**(5) Review process**\nEstablish a mechanism for service members to request review of decisions if they previously submitted a religious accommodation and believe their records or career progression were adversely impacted regardless of accommodation request outcome.\n##### (c) Timeline for review and reporting\n**(1) Review**\nThe Special Review Board shall complete a full review of all affected military personnel not later than one year after the date of the enactment of this Act.\n**(2) Report**\nNot later than 60 days after the review is completed, the Deputy Under Secretary of Defense for Personnel and Readiness shall submit to the Committee on Armed Services of the Senate and the Committee on Armed Services of the House of Representatives a report detailing\u2014\n**(A)**\nthe Special Review Board\u2019s findings;\n**(B)**\nthe number of cases reviewed; and\n**(C)**\ncorrective actions taken.\n##### (d) Deadline for compensation\nThe Secretary of Defense shall ensure that service members determined by the Special Review Board to be eligible for backdated reinstatements, promotions, pay, and benefits receive such compensation not later than 60 days after their case-review under subsection (c)(1) is completed.\n#### 3. Congressional oversight and accountability\n##### (a) Report of initial findings\nNot later than 90 days after the date of the enactment of this Act, the Secretary of Defense shall submit to the Committee on Armed Services of the Senate and the Committee on Armed Services of the House of Representatives a report with initial findings of the audit directed in section 2(a). The report should provide statistical analysis of affected service member population, assess compliance of Department of Defense with RFRA, and provide plans to address identified areas of opportunity.\n##### (b) Quarterly reports\nThe Secretary of Defense shall provide quarterly reports to the Committee on Armed Services of the Senate and the Committee on Armed Services of the House of Representatives detailing\u2014\n**(1)**\nthe number of cases reviewed by the Special Review Board;\n**(2)**\nthe number of service members granted back pay, promotions, or restored benefits;\n**(3)**\nthe number of adverse actions expunged from military records;\n**(4)**\nstatistics on the performance of identified service member populations with respect to boards, career progression, and competitive assignment; and\n**(5)**\nrecommendations for further legislative action to ensure fairness in military personnel policies.\n##### (c) Inspector general audit\nNot later than 18 months after the date of the enactment of this Act, the Department of Defense Inspector General shall conduct an independent audit and compliance review of the implementation of this Act. The Inspector General shall review overall data of religious accommodations and determine if RFRA was applied consistently across the Department of Defense.\n#### 4. Definitions\nIn this Act:\n**(1) Adverse action**\nThe term adverse action includes\u2014\n**(A)**\nadministrative reprimands;\n**(B)**\ndenial or delay of promotions;\n**(C)**\nnegative performance evaluations;\n**(D)**\nforced involuntary separation;\n**(E)**\ncoerced voluntary separation; and\n**(F)**\ndenial of career-enhancing assignments.\n**(2) Religious accommodation**\nThe term religious accommodation refers to a formally submitted request for exemption from a military order, policy, or directive on religious grounds, in accordance with the respective service branch\u2019s religious accommodation policies.\n**(3) Service member**\nThe term service member means a member of the Armed Forces total force serving on active duty, reserve (to include Individual Ready Reserve (IRR)), or National Guard status in any branch of the Department of Defense.\n#### 5. Authorization of appropriations\nThere is authorized to be appropriated such sums as may be necessary to carry out this Act. The Secretary of Defense shall allocate necessary resources to support the Special Review Board.",
      "versionDate": "2025-05-07",
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
        "actionDate": "2025-05-07",
        "text": "Referred to the House Committee on Armed Services."
      },
      "number": "3240",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "RESTORE Act",
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
        "name": "Armed Forces and National Security",
        "updateDate": "2025-05-22T17:34:01Z"
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
      "date": "2025-05-07",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1641is.xml"
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
      "title": "RESTORE Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-05-21T04:08:23Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "RESTORE Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-05-21T04:08:20Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Reaffirming Every Servicemembers' Trust Of Religious Exemptions Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-05-21T04:08:20Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to restore fairness to service members who filed religious accommodation requests and ensure their career progression is justly reviewed.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-05-21T04:03:42Z"
    }
  ]
}
```
