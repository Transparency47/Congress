# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/1831?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/1831
- Title: Auto Reenroll Act of 2025
- Congress: 119
- Bill type: S
- Bill number: 1831
- Origin chamber: Senate
- Introduced date: 2025-05-21
- Update date: 2026-02-11T12:03:24Z
- Update date including text: 2026-02-11T12:03:24Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-05-21: Introduced in Senate
- 2025-05-21 - IntroReferral: Introduced in Senate
- 2025-05-21 - IntroReferral: Read twice and referred to the Committee on Health, Education, Labor, and Pensions.
- Latest action: 2025-05-21: Introduced in Senate

## Actions

- 2025-05-21 - IntroReferral: Introduced in Senate
- 2025-05-21 - IntroReferral: Read twice and referred to the Committee on Health, Education, Labor, and Pensions.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-05-21",
    "latestAction": {
      "actionDate": "2025-05-21",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/1831",
    "number": "1831",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Taxation"
    },
    "sponsors": [
      {
        "bioguideId": "K000384",
        "district": "",
        "firstName": "Timothy",
        "fullName": "Sen. Kaine, Tim [D-VA]",
        "lastName": "Kaine",
        "party": "D",
        "state": "VA"
      }
    ],
    "title": "Auto Reenroll Act of 2025",
    "type": "S",
    "updateDate": "2026-02-11T12:03:24Z",
    "updateDateIncludingText": "2026-02-11T12:03:24Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-05-21",
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
      "actionDate": "2025-05-21",
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
        "item": [
          {
            "date": "2025-05-21T17:54:30Z",
            "name": "Referred To"
          },
          {
            "date": "2025-05-21T17:54:30Z",
            "name": "Referred To"
          }
        ]
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
      "bioguideId": "C001075",
      "firstName": "Bill",
      "fullName": "Sen. Cassidy, Bill [R-LA]",
      "isOriginalCosponsor": "True",
      "lastName": "Cassidy",
      "party": "R",
      "sponsorshipDate": "2025-05-21",
      "state": "LA"
    },
    {
      "bioguideId": "C001035",
      "firstName": "Susan",
      "fullName": "Sen. Collins, Susan M. [R-ME]",
      "isOriginalCosponsor": "False",
      "lastName": "Collins",
      "middleName": "M.",
      "party": "R",
      "sponsorshipDate": "2026-01-06",
      "state": "ME"
    },
    {
      "bioguideId": "A000382",
      "firstName": "Angela",
      "fullName": "Sen. Alsobrooks, Angela D. [D-MD]",
      "isOriginalCosponsor": "False",
      "lastName": "Alsobrooks",
      "party": "D",
      "sponsorshipDate": "2026-02-10",
      "state": "MD"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1831is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 1831\nIN THE SENATE OF THE UNITED STATES\nMay 21, 2025 Mr. Kaine (for himself and Mr. Cassidy ) introduced the following bill; which was read twice and referred to the Committee on Health, Education, Labor, and Pensions\nA BILL\nTo amend the Internal Revenue Code of 1986 and the Employee Retirement Income Security Act of 1974 to allow for periodic automatic reenrollment under qualified automatic contribution arrangements, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Auto Reenroll Act of 2025 .\n#### 2. Automatic reenrollment under qualified automatic contribution arrangements and eligible automatic contribution arrangements\n##### (a) Qualified automatic contribution arrangements\n**(1) In general**\nSection 401(k)(13)(C) of the Internal Revenue Code of 1986 is amended by adding at the end the following new clause:\n(v) Periodic automatic deferral permitted A qualified automatic contribution arrangement shall not fail to be treated as meeting the requirements of this subparagraph solely by reason of the fact that, under the arrangement\u2014 (I) an election by an employee under clause (ii)(I) terminates after not more than 3 years (but not less than 1 year), and (II) such employee is treated as having made an election under clause (i) after such termination unless such employee makes a new affirmative election under clause (ii). A termination described in subclause (I) may be made at one time for a plan year for all employees who have made an election described in such subclause. .\n**(2) Coordination with rule for current employees**\n**(A) In general**\nClause (iv) of section 401(k)(13)(C) of such Code is amended by striking either to participate in the arrangement or not to participate in the arrangement and inserting to participate in the arrangement .\n**(B) Special rule for previously disregarded employees**\n**(i) In general**\nFor purposes of applying section 401(k)(13)(C)(v) of the Internal Revenue Code of 1986 (as added by paragraph (1)), a previously disregarded employee may be treated as an employee who has made an election under section 401(k)(13)(C)(ii)(I) of such Code.\n**(ii) Previously disregarded employee**\nFor purposes of this subparagraph, the term previously disregarded employee means any employee who was not taken into account under section 401(k)(13)(C)(i) of the Internal Revenue Code of 1986 by reason of an election described in section 401(k)(13)(C)(iv)(II) of such Code (as in effect for plan years beginning on or before the date of the enactment of this Act) to not participate in an arrangement described in section 401(k)(13)(C)(iv)(I) of such Code.\n##### (b) Eligible automatic contribution arrangements\nSection 414(w)(3) of the Internal Revenue Code of 1986 is amended\u2014\n**(1)**\nby redesignating subparagraphs (A) through (C) as clauses (i) through (iii), respectively, and moving the margins of such clauses 2 ems to the right;\n**(2)**\nby striking arrangement .\u2014For purposes of and inserting the following: \u201c arrangement .\u2014\n(A) In general For purposes of ; and\n**(3)**\nby adding at the end the following new subparagraph:\n(B) Periodic automatic deferral permitted An arrangement shall not fail to be treated as an eligible automatic contribution arrangement under this subsection solely by reason of the fact that, under the arrangement\u2014 (i) an election by a participant under subparagraph (A)(ii) not to have contributions made terminates after not more than 3 years (but not less than 1 year), and (ii) such participant is treated as having made an election under subparagraph (A)(ii) to make contributions at the uniform percentage level described in such subparagraph after such termination unless such participant makes a new election not to so make such contributions. A termination described in clause (i) may be made at one time for a plan year for all participants who have made an election described in such clause. .\n##### (c) Conforming amendment\nSection 514(e)(2) of the Employee Retirement Income Security Act of 1974 ( 29 U.S.C. 1144(e)(2) ) is amended\u2014\n**(1)**\nby redesignating subparagraphs (A) through (C) as clauses (i) through (iii), respectively;\n**(2)**\nby striking (2) For purposes of and inserting (2)(A) For purposes of ; and\n**(3)**\nby adding at the end the following:\n(B) An arrangement shall not fail to be treated as an automatic contribution arrangement under this subsection solely by reason of the fact that under the arrangement\u2014 (i) an election by a participant under subparagraph (A)(ii) not to have contributions made terminates after not more than 3 years (but not less than 1 year), and (ii) such participant is treated as having made an election under subparagraph (A)(ii) to make contributions at the uniform percentage level described in such subparagraph after such termination unless such participant makes a new election not to so make such contributions. A termination described in clause (i) may be made at one time for a plan year for all participants who have made an election described in such clause, regardless of individual participant dates of enrollment. .\n##### (d) Effective date\nThe amendments made by this section shall apply to plan years beginning after the date of the enactment of this Act.\n##### (e) No inference\nThe amendments made by this section shall not be construed to create any inference with respect to\u2014\n**(1)**\nthe application of section 401(k)(13)(C) of the Internal Revenue Code of 1986, section 414(w)(3) of such Code, or section 514(e)(2) of the Employee Retirement Income Security Act of 1974 to plan years beginning before the date of the enactment of this Act, or\n**(2)**\nthe application of section 401(k)(13)(C)(v) of the Internal Revenue Code of 1986 (as added by subsection (a)), section 414(w)(3)(B) of such Code (as amended by subsection (b)), or section 514(e)(2)(B) of the Employee Retirement Income Security Act of 1974 (as amended by subsection (c)) to arrangements terminating elections not to have contributions made after more than 3 years.",
      "versionDate": "2025-05-21",
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
        "actionDate": "2025-12-15",
        "text": "Referred to the Committee on Ways and Means, and in addition to the Committee on Education and Workforce, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned."
      },
      "number": "6729",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Auto Reenroll Act of 2025",
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
        "updateDate": "2025-06-06T20:40:45Z"
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
      "date": "2025-05-21",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1831is.xml"
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
      "title": "Auto Reenroll Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-02-11T12:03:24Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Auto Reenroll Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-06-04T03:23:25Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend the Internal Revenue Code of 1986 and the Employee Retirement Income Security Act of 1974 to allow for periodic automatic reenrollment under qualified automatic contribution arrangements, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-06-04T03:18:32Z"
    }
  ]
}
```
