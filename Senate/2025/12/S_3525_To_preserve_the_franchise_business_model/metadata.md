# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/3525?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/3525
- Title: American Franchise Act
- Congress: 119
- Bill type: S
- Bill number: 3525
- Origin chamber: Senate
- Introduced date: 2025-12-17
- Update date: 2026-03-30T18:22:45Z
- Update date including text: 2026-03-30T18:22:45Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-12-17: Introduced in Senate
- 2025-12-17 - IntroReferral: Introduced in Senate
- 2025-12-17 - IntroReferral: Read twice and referred to the Committee on Health, Education, Labor, and Pensions.
- 2026-03-19 - Committee: Committee on Health, Education, Labor, and Pensions. Hearings held.
- Latest action: 2025-12-17: Introduced in Senate

## Actions

- 2025-12-17 - IntroReferral: Introduced in Senate
- 2025-12-17 - IntroReferral: Read twice and referred to the Committee on Health, Education, Labor, and Pensions.
- 2026-03-19 - Committee: Committee on Health, Education, Labor, and Pensions. Hearings held.

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
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/3525",
    "number": "3525",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Labor and Employment"
    },
    "sponsors": [
      {
        "bioguideId": "M001198",
        "district": "",
        "firstName": "Roger",
        "fullName": "Sen. Marshall, Roger [R-KS]",
        "lastName": "Marshall",
        "party": "R",
        "state": "KS"
      }
    ],
    "title": "American Franchise Act",
    "type": "S",
    "updateDate": "2026-03-30T18:22:45Z",
    "updateDateIncludingText": "2026-03-30T18:22:45Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-03-19",
      "committees": {
        "item": {
          "name": "Health, Education, Labor, and Pensions Committee",
          "systemCode": "sshr00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Committee on Health, Education, Labor, and Pensions. Hearings held.",
      "type": "Committee"
    },
    {
      "actionDate": "2025-12-17",
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
        "item": [
          {
            "date": "2026-03-19T14:01:10Z",
            "name": "Hearings By (full committee)"
          },
          {
            "date": "2025-12-17T18:09:23Z",
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
      "bioguideId": "K000383",
      "firstName": "Angus",
      "fullName": "Sen. King, Angus S., Jr. [I-ME]",
      "isOriginalCosponsor": "True",
      "lastName": "King",
      "middleName": "S.",
      "party": "I",
      "sponsorshipDate": "2025-12-17",
      "state": "ME"
    },
    {
      "bioguideId": "L000575",
      "firstName": "James",
      "fullName": "Sen. Lankford, James [R-OK]",
      "isOriginalCosponsor": "True",
      "lastName": "Lankford",
      "party": "R",
      "sponsorshipDate": "2025-12-17",
      "state": "OK"
    },
    {
      "bioguideId": "S001232",
      "firstName": "Tim",
      "fullName": "Sen. Sheehy, Tim [R-MT]",
      "isOriginalCosponsor": "True",
      "lastName": "Sheehy",
      "party": "R",
      "sponsorshipDate": "2025-12-17",
      "state": "MT"
    },
    {
      "bioguideId": "C001035",
      "firstName": "Susan",
      "fullName": "Sen. Collins, Susan M. [R-ME]",
      "isOriginalCosponsor": "True",
      "lastName": "Collins",
      "middleName": "M.",
      "party": "R",
      "sponsorshipDate": "2025-12-17",
      "state": "ME"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s3525is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 3525\nIN THE SENATE OF THE UNITED STATES\nDecember 17, 2025 Mr. Marshall (for himself, Mr. King , Mr. Lankford , Mr. Sheehy , and Ms. Collins ) introduced the following bill; which was read twice and referred to the Committee on Health, Education, Labor, and Pensions\nA BILL\nTo preserve the franchise business model.\n#### 1. Short title\nThis Act may be cited as the American Franchise Act .\n#### 2. Findings\nCongress finds the following:\n**(1)**\nA franchise is a commercial relationship under which a franchisee acquires the right to operate an independent business that offers, sells, or distributes goods or services using a franchisor\u2019s system of operations, which typically includes the franchisor\u2019s business system and marketing plan, and its service mark, trademark, trade dress, or trade name.\n**(2)**\nTo protect the integrity of its system of operations, a franchisor must set and enforce uniform quality, marketing, and operational standards that govern its use. Doing so helps maintain consistency and uniformity in the nature and quality of the goods and services distributed under the franchisor\u2019s trademarks. That consistency and uniformity, in turn, help ensure that consumer expectations are satisfied, increase the value of the franchisor\u2019s brand, and enhance the recognition and profitability of individual franchises.\n**(3)**\nAlthough franchisees must comply with these standards, franchisees are independent business owners. It is the franchisee who determines how to implement the franchisor\u2019s standards, controlling on a day-to-day basis the operations of its franchise and its labor relations.\n**(4)**\nThe economic impact of this business model has been profound. According to a September 2023 report from Oxford Economics, in 2022, the economic output of franchise establishments in the United States was approximately $825,000,000,000. During that year, franchises employed approximately 5 percent of all workers in the United States, which was approximately 8,400,000 workers.\n**(5)**\nInconsistent views of what constitutes a joint employer have impacted the viability of franchising by creating joint employer liability based on the franchisor\u2019s exercise of appropriate levels of control that is inherent in franchise relationships.\n#### 3. Clarification of joint employment for franchising\n##### (a) National Labor Relations Act\nThe National Labor Relations Act ( 29 U.S.C. 151 et seq. ) is amended by adding at the end the following:\n20. Clarification of joint employment for franchising (a) Definitions In this section: (1) Direct and immediate control The term direct and immediate control means the following with respect to each respective essential term and condition of employment: (A) Wages A franchisor exercises direct and immediate control over wages if it actually determines the wage rates, salary, or other rate of pay that is paid to individual employees of a franchisee or job classifications of employees of a franchisee. (B) Benefits A franchisor exercises direct and immediate control over benefits if it actually determines the fringe benefits to be provided or offered to a franchisee\u2019s employees. Such direct and immediate control does not include permitting a franchisee, under an arm\u2019s-length contract, to participate in a benefits plan of the franchisor (such as a health insurance plan, pension plan, or tuition assistance). (C) Hours of work A franchisor exercises direct and immediate control over hours of work if it actually determines work schedules or the work hours, including overtime, of a franchisee\u2019s employees. Such direct and immediate control does not include\u2014 (i) establishing a franchisee\u2019s operating hours; or (ii) establishing minimum staffing levels to satisfy the franchise\u2019s service standards. (D) Hiring A franchisor exercises direct and immediate control over hiring if it actually determines which particular employees will be hired or which employees will not be hired. Such direct and immediate control does not include\u2014 (i) encouraging or recommending changes in staffing levels; or (ii) setting minimal recruiting and hiring standards, such as those required by law, for consumer or employee safety, or for brand protection. (E) Discharge A franchisor exercises direct and immediate control over discharge if it actually decides to terminate the employment of an employee of a franchisee. Such direct and immediate control does not include\u2014 (i) bringing misconduct or poor performance to the attention of a franchisee that makes the actual discharge decision; (ii) expressing a negative opinion of a franchisee\u2019s employee; or (iii) setting minimal standards of performance or conduct, such as those required by law, for consumer or employee safety, or for brand protection. (F) Discipline A franchisor exercises direct and immediate control over discipline if it actually decides to suspend or otherwise discipline a franchisee\u2019s employee. Such direct and immediate control does not include\u2014 (i) bringing misconduct or poor performance to the attention of a franchisee that makes the actual disciplinary decision; (ii) expressing a negative opinion of a franchisee\u2019s employee; or (iii) setting minimal standards of performance or conduct, such as those required by law, for consumer or employee safety or for brand protection. (G) Supervision A franchisor exercises direct and immediate control over supervision by consistently and directly instructing a franchisee\u2019s employees how to perform their work or by actually issuing employee performance appraisals. Such direct and immediate control does not include\u2014 (i) providing instructions to a franchisee's employees that are limited and routine; (ii) setting brand standards for the performance of the work; (iii) offering training materials (including training demonstrations) for a franchisee to use to train the employees of the franchisee; (iv) establishing minimum training requirements for the employees of a franchisee; or (v) providing operational support, guidance, and assistance to the franchisee to promote and protect the brand\u2019s goodwill and quality of products and services provided to the consumer. (H) Direction A franchisor exercises direct and immediate control over direction by assigning particular employees of a franchisee their individual work schedules, positions, and tasks. Such direct and immediate control does not include offering resources and tools for a franchisee to consider using to direct the work schedules, positions, and tasks of the employees of the franchisee. (2) Essential terms and conditions of employment The term essential terms and conditions of employment means wages, benefits, hours of work, hiring, discharge, discipline, supervision, and direction. (3) Franchise; franchisee; franchisor The terms franchise , franchisee , and franchisor \u2014 (A) have the meanings given such terms in section 436.1 of title 16, Code of Federal Regulations, as in effect on the date of enactment of this section; and (B) notwithstanding subparagraph (A), include a franchise, franchisee, and franchisor, respectively, as defined in section 101 of the Petroleum Marketing Practices Act ( 15 U.S.C. 2801 ). (4) Substantial direct and immediate control The term substantial direct and immediate control \u2014 (A) means direct and immediate control that has a regular or continuous consequential effect on an essential term and condition of employment of a franchisee\u2019s employees; and (B) does not include direct and immediate control that is only exercised on a sporadic, isolated, or de minimis basis. (b) Joint employment For the purposes of this Act, a franchisor may be considered a joint employer of the employees of a franchisee only if the franchisor possesses and exercises substantial direct and immediate control over one or more essential terms and conditions of employment of the employees of the franchisee. .\n##### (b) Fair Labor Standards Act of 1938\nThe Fair Labor Standards Act of 1938 ( 29 U.S.C. 201 et seq. ) is amended by adding at the end of the following:\n20. Clarification of joint employment for franchising (a) In general For purposes of this Act, a franchisor may be considered a joint employer of the employees of a franchisee only if the franchisor meets the criteria for a joint employer with a franchisee under section 20 of the National Labor Relations Act, except that, for purposes of determining joint-employer status under this Act, the terms employee and employer referenced in section 20 of the National Labor Relations Act shall have the meanings given such terms in section 3 of this Act. (b) Definitions In this section, the terms franchisor and franchisee have the meanings given such terms in section 20(a) of the National Labor Relations Act. .\n#### 4. Applicability\nThis Act, and the amendments made by this Act, shall not apply to any proceeding that is commenced before the date of enactment of this Act.",
      "versionDate": "2025-12-17",
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
        "actionDate": "2025-09-10",
        "text": "Referred to the House Committee on Education and Workforce."
      },
      "number": "5267",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "American Franchise Act",
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
      "legislativeSubjects": {
        "item": [
          {
            "name": "Employee benefits and pensions",
            "updateDate": "2026-03-30T18:22:31Z"
          },
          {
            "name": "Employee hiring",
            "updateDate": "2026-03-30T18:22:40Z"
          },
          {
            "name": "Employee performance",
            "updateDate": "2026-03-30T18:22:45Z"
          },
          {
            "name": "Labor standards",
            "updateDate": "2026-03-30T18:22:36Z"
          },
          {
            "name": "Small business",
            "updateDate": "2026-03-30T18:22:21Z"
          },
          {
            "name": "Wages and earnings",
            "updateDate": "2026-03-30T18:22:26Z"
          }
        ]
      },
      "policyArea": {
        "name": "Labor and Employment",
        "updateDate": "2026-01-12T16:36:34Z"
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
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s3525is.xml"
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
      "title": "American Franchise Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-03-20T11:03:19Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "American Franchise Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-01-10T09:53:34Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to preserve the franchise business model.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-01-10T09:48:32Z"
    }
  ]
}
```
