# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/968?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/s/968
- Title: Rent Relief Act of 2025
- Congress: 119
- Bill type: S
- Bill number: 968
- Origin chamber: Senate
- Introduced date: 2025-03-11
- Update date: 2025-05-08T19:12:31Z
- Update date including text: 2025-05-08T19:12:31Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, subjects, text, titles

## Timeline

- 2025-03-11: Introduced in Senate
- 2025-03-11 - IntroReferral: Introduced in Senate
- 2025-03-11 - IntroReferral: Read twice and referred to the Committee on Finance.
- Latest action: 2025-03-11: Introduced in Senate

## Actions

- 2025-03-11 - IntroReferral: Introduced in Senate
- 2025-03-11 - IntroReferral: Read twice and referred to the Committee on Finance.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-03-11",
    "latestAction": {
      "actionDate": "2025-03-11",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/s/968",
    "number": "968",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Taxation"
    },
    "sponsors": [
      {
        "bioguideId": "W000790",
        "district": "",
        "firstName": "Raphael",
        "fullName": "Sen. Warnock, Raphael G. [D-GA]",
        "lastName": "Warnock",
        "party": "D",
        "state": "GA"
      }
    ],
    "title": "Rent Relief Act of 2025",
    "type": "S",
    "updateDate": "2025-05-08T19:12:31Z",
    "updateDateIncludingText": "2025-05-08T19:12:31Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-03-11",
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
      "actionDate": "2025-03-11",
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
          "date": "2025-03-11T22:30:50Z",
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

## API Data: fullTexts

```json
{
  "fullTexts": [
    {
      "fetchError": null,
      "sourceFormat": "Formatted XML",
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s968is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 968\nIN THE SENATE OF THE UNITED STATES\nMarch 11 (legislative day, March 10), 2025 Mr. Warnock introduced the following bill; which was read twice and referred to the Committee on Finance\nA BILL\nTo amend the Internal Revenue Code of 1986 to allow for a credit against tax for rent paid on the personal residence of the taxpayer.\n#### 1. Short title\nThis Act may be cited as the Rent Relief Act of 2025 .\n#### 2. Refundable credit for rent paid for principal residence\n##### (a) In general\nSubpart C of part IV of subchapter A of chapter 1 of the Internal Revenue Code of 1986 is amended by inserting after section 36B the following new section:\n36C. Rent paid for principal residence (a) In general In the case of an individual who leases the individual\u2019s principal residence (within the meaning of section 121) during the taxable year and who pays rent with respect to such residence in excess of 30 percent of the taxpayer\u2019s gross income for such taxable year, there shall be allowed as a credit against the tax imposed by this subtitle for such taxable year an amount equal to the applicable percentage of such excess. (b) Credit limited by 100 percent of small area fair market rent Solely for purposes of determining the amount of the credit allowed under subsection (a) with respect to a residence for the taxable year, there shall not be taken into account rent in excess of an amount equal to 100 percent of the small area fair market rent (including the utility allowance) applicable to the residence involved (as most recently published, as of the beginning of the taxable year, by the Department of Housing and Urban Development). (c) Definitions and special rules For purposes of this section\u2014 (1) Applicable percentage (A) In general Except as provided in subparagraph (B), the applicable percentage shall be determined in accordance with the following table: The applicable If gross income is: percentage is: Not over $25,000 100 percent Over $25,000, but not over $50,000 75 percent Over $50,000, but not over $75,000 50 percent Over $75,000, but not over $100,000 25 percent Over $100,000 0 percent. (B) High-cost areas In the case of an individual whose principal residence is located in an area designated by the Secretary of Housing and Urban Development as an area which has high construction, land, or utility costs relative to area median gross income for purposes of section 42(d)(5), each of the dollar amounts in the table contained in subparagraph (A) shall be increased by $25,000. (2) Partial year residence The Secretary shall prescribe such rules as are necessary to carry out the purposes of this section for taxpayers with respect to whom a residence is a principal residence for only a portion of the taxable year. (3) Special rule for individuals residing in government-subsidized housing In the case of a principal residence\u2014 (A) the rent with respect to which is subsidized under a Federal, State, local, or tribal program, and (B) with respect to which the taxpayer elects the application of this paragraph, in lieu of the credit determined under subsection (a), there shall be allowed as a credit against the tax imposed by this subtitle for such taxable year an amount equal to 1/12 of the amount of rent paid by the taxpayer (and not subsidized under any such program) during the taxable year with respect to such residence. (4) Rent The term rent includes any amount paid for utilities of a type taken into account for purposes of determining the utility allowance under section 42(g)(2)(B)(ii). (d) Reconciliation of credit and advance payments The amount of the credit allowed under this section for any taxable year shall be reduced (but not below zero) by the aggregate amount of any advance payments of such credit under section 7527A for such taxable year. .\n##### (b) Advance payment\nChapter 77 of the Internal Revenue Code of 1986 is amended by inserting after section 7527 the following new section:\n7527A. Advance payment of rent credit (a) In general Not later than 6 months after the date of the enactment of the Rent Relief Act of 2025 , the Secretary shall establish a program for making advance payments of the credit allowed under section 36C on a monthly basis to any taxpayer who\u2014 (1) the Secretary has determined will be allowed such credit for the taxable year, and (2) has made an election under subsection (c). (b) Amount of advance payment (1) In general For purposes of subsection (a), the amount of the monthly advance payment of the credit provided to a taxpayer during the applicable period shall be equal to the lesser of\u2014 (A) an amount equal to\u2014 (i) the amount of the credit which the Secretary has determined will be allowed to such taxpayer under section 36C for the taxable year ending in such applicable period, divided by (ii) 12, or (B) such other amount as is elected by the taxpayer. (2) Applicable period For purposes of this section, the term applicable period means the 12-month period from the month of July of the taxable year through the month of June of the subsequent taxable year. (c) Election of advance payment A taxpayer may elect to receive an advance payment of the credit allowed under section 36C for any taxable year by including such election on a timely filed return for the preceding taxable year. (d) Internal Revenue Service notification The Internal Revenue Service shall take such steps as may be appropriate to ensure that taxpayers who are eligible to receive the credit under section 36C are aware of the availability of the advance payment of such credit under this section. (e) Authority The Secretary may prescribe such regulations or other guidance as may be appropriate or necessary for the purposes of carrying out this section. .\n##### (c) Conforming amendments\n**(1)**\nSection 6211(b)(4)(A) of the Internal Revenue Code of 1986 is amended by inserting , 36C after 36B .\n**(2)**\nParagraph (2) of section 1324(b) of title 31, United States Code, is amended by inserting , 36C after 36B .\n##### (d) Clerical amendments\n**(1) In general**\nThe table of sections for subpart C of part IV of subchapter A of chapter 1 of the Internal Revenue Code of 1986 is amended by inserting after the item relating to section 36B the following new item:\nSec. 36C. Rent paid for principal residence. .\n**(2) Advance payment**\nThe table of sections for chapter 77 of such Code is amended by inserting after the item relating to section 7527 the following new item:\nSec. 7527A. Advance payment of middle class tax credit. .\n##### (e) Effective date\nThe amendments made by this section shall apply to taxable years beginning after December 31, 2025.",
      "versionDate": "2025-03-11",
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
        "name": "Taxation",
        "updateDate": "2025-05-08T19:12:31Z"
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
      "date": "2025-03-11",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s968is.xml"
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
      "title": "Rent Relief Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-03-29T02:23:22Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Rent Relief Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-29T02:23:19Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend the Internal Revenue Code of 1986 to allow for a credit against tax for rent paid on the personal residence of the taxpayer.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-29T02:18:48Z"
    }
  ]
}
```
