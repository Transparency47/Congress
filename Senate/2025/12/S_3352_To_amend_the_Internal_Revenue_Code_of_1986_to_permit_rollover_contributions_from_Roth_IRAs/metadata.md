# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/3352?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/3352
- Title: Retirement Rollover Flexibility Act
- Congress: 119
- Bill type: S
- Bill number: 3352
- Origin chamber: Senate
- Introduced date: 2025-12-04
- Update date: 2026-01-07T17:08:43Z
- Update date including text: 2026-01-07T17:08:43Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-12-04: Introduced in Senate
- 2025-12-04 - IntroReferral: 
- 2025-12-04 - IntroReferral: Introduced in Senate
- 2025-12-04 - IntroReferral: Read twice and referred to the Committee on Finance. (text: CR S8512-8513)
- Latest action: 2025-12-04: Introduced in Senate

## Actions

- 2025-12-04 - IntroReferral: 
- 2025-12-04 - IntroReferral: Introduced in Senate
- 2025-12-04 - IntroReferral: Read twice and referred to the Committee on Finance. (text: CR S8512-8513)

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-12-04",
    "latestAction": {
      "actionDate": "2025-12-04",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/3352",
    "number": "3352",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Taxation"
    },
    "sponsors": [
      {
        "bioguideId": "B001261",
        "district": "",
        "firstName": "John",
        "fullName": "Sen. Barrasso, John [R-WY]",
        "lastName": "Barrasso",
        "party": "R",
        "state": "WY"
      }
    ],
    "title": "Retirement Rollover Flexibility Act",
    "type": "S",
    "updateDate": "2026-01-07T17:08:43Z",
    "updateDateIncludingText": "2026-01-07T17:08:43Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-12-04",
      "committees": {
        "item": {
          "name": "Finance Committee",
          "systemCode": "ssfi00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Finance. (text: CR S8512-8513)",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-S",
      "actionDate": "2025-12-04",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-12-04",
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
          "date": "2025-12-04T20:18:00Z",
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
      "bioguideId": "B001267",
      "firstName": "Michael",
      "fullName": "Sen. Bennet, Michael F. [D-CO]",
      "isOriginalCosponsor": "True",
      "lastName": "Bennet",
      "party": "D",
      "sponsorshipDate": "2025-12-04",
      "state": "CO"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s3352is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 3352\nIN THE SENATE OF THE UNITED STATES\nDecember 4, 2025 Mr. Barrasso (for himself and Mr. Bennet ) introduced the following bill; which was read twice and referred to the Committee on Finance\nA BILL\nTo amend the Internal Revenue Code of 1986 to permit rollover contributions from Roth IRAs to designated Roth accounts.\n#### 1. Short title\nThis Act may be cited as the Retirement Rollover Flexibility Act .\n#### 2. Rollover contributions from Roth IRAs to designated Roth accounts\n##### (a) Treatment as rollover distribution for purposes of Roth IRA\n**(1) In general**\nSection 408(d)(3)(A) of the Internal Revenue Code of 1986 is amended by striking ; or at the end of clause (i) and inserting a comma, by striking the period at the end of clause (ii) and inserting , or and by inserting after clause (ii) the following new clause:\n(iii) the entire amount received (including money and any other property) is paid in a direct trustee-to-trustee transfer to a designated Roth account (within the meaning of section 402A)\u2014 (I) from an eligible Roth IRA, or (II) in an automatic portability transaction (as defined in section 4975(f)(12)(A)(i)). .\n**(2) Eligible Roth IRA**\nSection 408(d)(3) is amended by adding at the end the following new subparagraph:\n(J) ELigible Roth IRA For purposes of subparagraph (A)(iii), the term eligible Roth IRA means a Roth IRA which\u2014 (i) is the only Roth IRA (other than a Roth IRA established under section 401(a)(31)(B)(i)) maintained for the benefit of the individual during the taxable year of the taxpayer in which the distribution or payment described in subparagraph (A)(iii) is made, and (ii) has a balance at the time of the payment or distribution which is not in excess of the amount described in section 401(a)(31)(B)(ii). .\n##### (b) Treatment as rollover contribution for purposes of designated Roth account\n**(1) In general**\nSection 402A(c)(3)(B) of the Internal Revenue Code of 1986 is amended by inserting or under section 408(d)(3)(A)(iii) after subparagraph (A) .\n**(2) Treatment of earnings in case of taxable distributions**\nSection 402A(d) of such Code is amended by adding at the end the following new paragraph:\n(6) Treatment of Roth IRA rollover contributions Notwithstanding section 72, the total amount of any rollover contribution to a designated Roth account under section 408(d)(3)(A)(iii) shall be treated as investment in the contract. .\n##### (c) Coordination with nonexclusion period\nSection 402A(d)(2)(B) of such Code is amended\u2014\n**(1)**\nby striking earlier in the matter preceding subclause (i) and inserting earliest ,\n**(2)**\nby striking or at the end of clause (i),\n**(3)**\nby striking the period at the end of clause (ii), and\n**(4)**\nby adding at the end the following:\n(iii) if a rollover contribution was made to such designated Roth account from a Roth IRA under section 408(d)(3)(A)(iii)(II) and the automatic portability provider (as defined in section 4975(f)(12)(A)(ii)) provides the first taxable year to which a contribution was made to the source plan, the first taxable year in which the individual made contributions to the source plan. For purposes of clause (iii), the term source plan means the eligible retirement plan (as defined in section 401(a)(31)(B)(ii)) from which amounts were transferred to the Roth IRA as described in section 4975(f)(12)(A)(i)(I). .\n##### (d) Effective date\nThe amendments made by this section shall apply to amounts paid or distributed after the date of the enactment of this Act.",
      "versionDate": "2025-12-04",
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
        "actionDate": "2025-12-04",
        "text": "Referred to the House Committee on Ways and Means."
      },
      "number": "6450",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Retirement Rollover Flexibility Act",
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
        "updateDate": "2026-01-06T16:07:01Z"
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
      "date": "2025-12-04",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s3352is.xml"
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
      "title": "Retirement Rollover Flexibility Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-12-30T05:38:18Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Retirement Rollover Flexibility Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-12-30T05:38:18Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend the Internal Revenue Code of 1986 to permit rollover contributions from Roth IRAs to designated Roth accounts.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-12-30T05:33:24Z"
    }
  ]
}
```
