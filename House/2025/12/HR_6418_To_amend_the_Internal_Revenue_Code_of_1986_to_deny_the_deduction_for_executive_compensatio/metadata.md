# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/6418?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/6418
- Title: Employee Profit-Sharing Encouragement Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 6418
- Origin chamber: House
- Introduced date: 2025-12-03
- Update date: 2026-01-23T23:26:15Z
- Update date including text: 2026-01-23T23:26:15Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-12-03: Introduced in House
- 2025-12-03 - IntroReferral: Introduced in House
- 2025-12-03 - IntroReferral: Introduced in House
- 2025-12-03 - IntroReferral: Referred to the House Committee on Ways and Means.
- Latest action: 2025-12-03: Introduced in House

## Actions

- 2025-12-03 - IntroReferral: Introduced in House
- 2025-12-03 - IntroReferral: Introduced in House
- 2025-12-03 - IntroReferral: Referred to the House Committee on Ways and Means.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-12-03",
    "latestAction": {
      "actionDate": "2025-12-03",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/6418",
    "number": "6418",
    "originChamber": "House",
    "policyArea": {
      "name": "Taxation"
    },
    "sponsors": [
      {
        "bioguideId": "W000822",
        "district": "12",
        "firstName": "Bonnie",
        "fullName": "Rep. Watson Coleman, Bonnie [D-NJ-12]",
        "lastName": "Watson Coleman",
        "party": "D",
        "state": "NJ"
      }
    ],
    "title": "Employee Profit-Sharing Encouragement Act of 2025",
    "type": "HR",
    "updateDate": "2026-01-23T23:26:15Z",
    "updateDateIncludingText": "2026-01-23T23:26:15Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-12-03",
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
      "actionDate": "2025-12-03",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-12-03",
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
          "date": "2025-12-03T15:02:40Z",
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
      "bioguideId": "O000173",
      "district": "5",
      "firstName": "Ilhan",
      "fullName": "Rep. Omar, Ilhan [D-MN-5]",
      "isOriginalCosponsor": "False",
      "lastName": "Omar",
      "party": "D",
      "sponsorshipDate": "2025-12-17",
      "state": "MN"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6418ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 6418\nIN THE HOUSE OF REPRESENTATIVES\nDecember 3, 2025 Mrs. Watson Coleman introduced the following bill; which was referred to the Committee on Ways and Means\nA BILL\nTo amend the Internal Revenue Code of 1986 to deny the deduction for executive compensation unless the employer maintains profit-sharing distributions for employees.\n#### 1. Short title\nThis Act may be cited as the Employee Profit-Sharing Encouragement Act of 2025 .\n#### 2. Denial of deduction for executive compensation unless employer maintains profit-sharing distributions\n##### (a) In general\nSection 162 of the Internal Revenue Code of 1986 is amended by redesignating subsection (s) as subsection (t) and by inserting after subsection (r) the following new subsection:\n(s) Executive compensation paid by employers who do not maintain profit-Sharing distributions (1) In general In the case of a specified employer, no deduction shall be allowed under this chapter for applicable employee remuneration with respect to any highly compensated individual (within the meaning of section 105(h)) for any taxable year unless qualified profit-sharing distributions are made during such taxable year. (2) Qualified profit-sharing distributions For purposes of this subsection\u2014 (A) In general The term qualified profit-sharing distributions means a cash distribution made pursuant to a written plan of the employer under which\u2014 (i) employees (including part-time employees) who have been employed for at least 1 year as of the date of the distribution have a right to such distribution, and (ii) the amount of such distributions are defined under such plan on the basis of a measure of the receipts, profit, revenues, or earnings of such employer. (B) Minimum distribution requirements Such term shall not include any distributions made pursuant to such plan during the taxable year if the aggregate distributions made pursuant to such plan during such taxable year are less than 5 percent of the employer\u2019s net income for the taxable year as determined pursuant to the employer\u2019s books and records prepared in accordance with the employer\u2019s accounting procedures. (C) Nondiscrimination Such term shall not include any distributions made pursuant to such plan during the taxable year unless such plan satisfies requirements similar to the requirements of section 401(k)(3)(A)(ii) applied by treating the distributions made pursuant to the plan as though such distributions were contributions paid over to the trust referred to in such section. (D) Exception if distributions would jeopardize the business An employer shall not fail to be treated as making qualified profit-sharing distributions during the taxable year to the extent that such employer establishes to the satisfaction of the Secretary by clear and convincing evidence that making such distributions would jeopardize the ability of the employer to continue as a going concern. (3) Specified employer For purposes of this subsection\u2014 (A) In general The term specified employer means, with respect to any taxable year, any employer which meets the gross receipts test of section 448(c) (determined without regard to paragraph (4) thereof) for such taxable year. (B) Application of gross receipts test to individuals, etc For purposes of subparagraph (A), in the case of any employer which is not a corporation or a partnership, the gross receipts test referred to in such subparagraph shall be applied in the same manner as if each trade or business of such employer were a corporation or partnership. (4) Applicable employee remuneration For purposes of this subsection, the term applicable employee remuneration has the meaning given such term by subsection (m)(4), determined without regard to subparagraph (B) thereof. (5) Controlled groups For purposes of this subsection, all persons treated as a single employer under subsection (b), (c), (m), or (o) of section 414 shall be treated as one employer. (6) Coordination Rules similar to the rules of subparagraphs (D) and (E) of subsection (m)(4) shall apply for purposes of this subsection. (7) Authority to address abuse The Secretary shall have the authority to address any abuses by employers under this subsection, including, but not limited to, a reduction in employee compensation or benefits in conjunction with the payment of qualified profit-sharing distributions. .\n##### (b) Effective date\nThe amendments made by this section shall apply to taxable years beginning after the date of the enactment of this Act.",
      "versionDate": "2025-12-03",
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
        "name": "Taxation",
        "updateDate": "2026-01-06T15:58:01Z"
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
      "date": "2025-12-03",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6418ih.xml"
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
      "title": "Employee Profit-Sharing Encouragement Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-12-23T08:23:16Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Employee Profit-Sharing Encouragement Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-12-23T08:23:15Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Internal Revenue Code of 1986 to deny the deduction for executive compensation unless the employer maintains profit-sharing distributions for employees.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-12-23T08:18:30Z"
    }
  ]
}
```
