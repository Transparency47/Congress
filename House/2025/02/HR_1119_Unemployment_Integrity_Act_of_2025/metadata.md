# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/1119?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/1119
- Title: Unemployment Integrity Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 1119
- Origin chamber: House
- Introduced date: 2025-02-07
- Update date: 2026-02-27T21:41:19Z
- Update date including text: 2026-02-27T21:41:19Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-02-07: Introduced in House
- 2025-02-07 - IntroReferral: Introduced in House
- 2025-02-07 - IntroReferral: Introduced in House
- 2025-02-07 - IntroReferral: Referred to the House Committee on Ways and Means.
- Latest action: 2025-02-07: Introduced in House

## Actions

- 2025-02-07 - IntroReferral: Introduced in House
- 2025-02-07 - IntroReferral: Introduced in House
- 2025-02-07 - IntroReferral: Referred to the House Committee on Ways and Means.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-02-07",
    "latestAction": {
      "actionDate": "2025-02-07",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/1119",
    "number": "1119",
    "originChamber": "House",
    "policyArea": {
      "name": "Labor and Employment"
    },
    "sponsors": [
      {
        "bioguideId": "E000246",
        "district": "11",
        "firstName": "Chuck",
        "fullName": "Rep. Edwards, Chuck [R-NC-11]",
        "lastName": "Edwards",
        "party": "R",
        "state": "NC"
      }
    ],
    "title": "Unemployment Integrity Act of 2025",
    "type": "HR",
    "updateDate": "2026-02-27T21:41:19Z",
    "updateDateIncludingText": "2026-02-27T21:41:19Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-02-07",
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
      "actionDate": "2025-02-07",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-02-07",
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
          "date": "2025-02-07T14:02:25Z",
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
      "bioguideId": "F000472",
      "district": "18",
      "firstName": "Scott",
      "fullName": "Rep. Franklin, Scott [R-FL-18]",
      "isOriginalCosponsor": "True",
      "lastName": "Franklin",
      "party": "R",
      "sponsorshipDate": "2025-02-07",
      "state": "FL"
    },
    {
      "bioguideId": "S001189",
      "district": "8",
      "firstName": "Austin",
      "fullName": "Rep. Scott, Austin [R-GA-8]",
      "isOriginalCosponsor": "True",
      "lastName": "Scott",
      "party": "R",
      "sponsorshipDate": "2025-02-07",
      "state": "GA"
    },
    {
      "bioguideId": "G000576",
      "district": "6",
      "firstName": "Glenn",
      "fullName": "Rep. Grothman, Glenn [R-WI-6]",
      "isOriginalCosponsor": "False",
      "lastName": "Grothman",
      "party": "R",
      "sponsorshipDate": "2025-02-11",
      "state": "WI"
    },
    {
      "bioguideId": "C001118",
      "district": "6",
      "firstName": "Ben",
      "fullName": "Rep. Cline, Ben [R-VA-6]",
      "isOriginalCosponsor": "False",
      "lastName": "Cline",
      "party": "R",
      "sponsorshipDate": "2025-02-11",
      "state": "VA"
    },
    {
      "bioguideId": "W000806",
      "district": "11",
      "firstName": "Daniel",
      "fullName": "Rep. Webster, Daniel [R-FL-11]",
      "isOriginalCosponsor": "False",
      "lastName": "Webster",
      "party": "R",
      "sponsorshipDate": "2025-04-29",
      "state": "FL"
    },
    {
      "bioguideId": "M001218",
      "district": "7",
      "firstName": "Richard",
      "fullName": "Rep. McCormick, Richard [R-GA-7]",
      "isOriginalCosponsor": "False",
      "lastName": "McCormick",
      "party": "R",
      "sponsorshipDate": "2025-05-07",
      "state": "GA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1119ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 1119\nIN THE HOUSE OF REPRESENTATIVES\nFebruary 7, 2025 Mr. Edwards (for himself, Mr. Scott Franklin of Florida , and Mr. Austin Scott of Georgia ) introduced the following bill; which was referred to the Committee on Ways and Means\nA BILL\nTo amend titles III and IX of the Social Security Act to require individuals receiving unemployment compensation to fulfill certain requirements in relation to suitable work, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Unemployment Integrity Act of 2025 .\n#### 2. Reform of unemployment compensation to promote work\n##### (a) Interview requirement\n**(1) In general**\nSection 303(a) of the Social Security Act ( 42 U.S.C. 503(a) ) is amended by adding at the end the following new paragraph:\n(13) A requirement that, as a condition of eligibility for regular compensation for any week, a claimant must, if requested, in relation to work that may be available\u2014 (A) respond to requests; (B) schedule and attend an interview and participate in reemployment services at an agreed upon time; and (C) comply with any other reasonable request, including any request that an individual undergo drug testing or skill assessments. .\n**(2) Reporting of noncompliance**\nSection 303(a) of such Act ( 42 U.S.C. 503(a) ), as amended by paragraph (1), is further amended by adding at the end the following new paragraph:\n(14) A method by which a person with whom a claimant is seeking employment may voluntarily report to the State the failure of a claimant to comply with the State law provisions described in paragraphs (12) and (13). .\n##### (b) Audit requirement\n**(1) Report**\nNot later than 2 years after the date of enactment of this Act, the Secretary of Labor shall conduct a study on the effect of increasing the number of random audits under the Beneficiary Accuracy Management program on the administration of State unemployment compensation laws.\n**(2) Audit program adjustments**\nNot later than 1 year after submitting the report required under paragraph (1), if such report indicates that increasing the number of random audits under the Benefit Accuracy Measurement program (or any successor audit program) will improve the administration of State unemployment compensation laws, the Secretary shall prescribe regulations to increase the number of such audits in accordance with such report.\n##### (c) Effective dates\n**(1) In general**\nSubject to subparagraph (B), the amendments made by subsections (a) and (b) shall, with respect to a State, apply to weeks beginning after the date that is 1 year after the date of enactment of this Act.\n**(2) States with biennial legislative sessions**\nIn the case of a State whose legislature is not in session during the 1-year period beginning on the date of enactment of this Act, the amendments made by subsections (a) and (b) shall, with respect to such State, apply to weeks beginning after the end of the first session of the State legislature which begins after the date of enactment of this Act.\n#### 3. Work requirements for extended and emergency unemployment compensation\n##### (a) In general\nSection 905 of the Social Security Act ( 42 U.S.C. 1105 ) is amended\u2014\n**(1)**\nin subsection (c), by striking Amounts and inserting Subject to subsection (e), amounts ; and\n**(2)**\nby adding at the end the following new subsection:\n(e) Limitation on funds transfers (1) Amounts in the extended unemployment compensation account may not be transferred to a State account for the purposes of any unemployment compensation law unless the Secretary of Labor certifies that the State law under which such unemployment compensation will be administered includes the provisions required by paragraphs (13) and (14) of section 303(a). (2) The provisions of this subsection shall apply notwithstanding any other provision of law enacted after the date of enactment of the Unemployment Integrity Act of 2025 , unless such other provision of law specifically cites this subsection. .\n##### (b) Effective date\n**(1) In general**\nSubject to paragraph (2), the amendments made by subsection (a) shall, with respect to a State, apply to weeks beginning after the date that is 1 year after the date of enactment of this Act.\n**(2) States with biennial legislative sessions**\nIn the case of a State whose legislature is not in session during the 1-year period beginning on the date of enactment of this Act, the amendments made by subsection (a) shall, with respect to such State, apply to weeks beginning after the end of the first session of the State legislature which begins after the date of enactment of this Act.",
      "versionDate": "2025-02-07",
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
        "name": "Labor and Employment",
        "updateDate": "2025-03-12T12:11:55Z"
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
      "date": "2025-02-07",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1119ih.xml"
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
      "title": "Unemployment Integrity Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-03-11T04:23:33Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Unemployment Integrity Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-11T04:23:23Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend titles III and IX of the Social Security Act to require individuals receiving unemployment compensation to fulfill certain requirements in relation to suitable work, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-11T04:19:38Z"
    }
  ]
}
```
