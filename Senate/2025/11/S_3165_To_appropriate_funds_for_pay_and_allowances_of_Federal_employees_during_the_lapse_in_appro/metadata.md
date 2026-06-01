# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/3165?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/3165
- Title: True Shutdown Fairness Act
- Congress: 119
- Bill type: S
- Bill number: 3165
- Origin chamber: Senate
- Introduced date: 2025-11-07
- Update date: 2026-01-14T15:55:20Z
- Update date including text: 2026-01-14T15:55:20Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-11-07: Introduced in Senate
- 2025-11-07 - IntroReferral: Introduced in Senate
- 2025-11-07 - IntroReferral: Read twice and referred to the Committee on Homeland Security and Governmental Affairs.
- Latest action: 2025-11-07: Introduced in Senate

## Actions

- 2025-11-07 - IntroReferral: Introduced in Senate
- 2025-11-07 - IntroReferral: Read twice and referred to the Committee on Homeland Security and Governmental Affairs.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-11-07",
    "latestAction": {
      "actionDate": "2025-11-07",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/3165",
    "number": "3165",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Government Operations and Politics"
    },
    "sponsors": [
      {
        "bioguideId": "V000128",
        "district": "",
        "firstName": "Chris",
        "fullName": "Sen. Van Hollen, Chris [D-MD]",
        "lastName": "Van Hollen",
        "party": "D",
        "state": "MD"
      }
    ],
    "title": "True Shutdown Fairness Act",
    "type": "S",
    "updateDate": "2026-01-14T15:55:20Z",
    "updateDateIncludingText": "2026-01-14T15:55:20Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-11-07",
      "committees": {
        "item": {
          "name": "Homeland Security and Governmental Affairs Committee",
          "systemCode": "ssga00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Homeland Security and Governmental Affairs.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-11-07",
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
          "date": "2025-11-07T21:57:09Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Homeland Security and Governmental Affairs Committee",
      "systemCode": "ssga00",
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
      "bioguideId": "A000382",
      "firstName": "Angela",
      "fullName": "Sen. Alsobrooks, Angela D. [D-MD]",
      "isOriginalCosponsor": "True",
      "lastName": "Alsobrooks",
      "party": "D",
      "sponsorshipDate": "2025-11-07",
      "state": "MD"
    },
    {
      "bioguideId": "K000384",
      "firstName": "Timothy",
      "fullName": "Sen. Kaine, Tim [D-VA]",
      "isOriginalCosponsor": "False",
      "lastName": "Kaine",
      "middleName": "M.",
      "party": "D",
      "sponsorshipDate": "2025-11-18",
      "state": "VA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s3165is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 3165\nIN THE SENATE OF THE UNITED STATES\nNovember 7, 2025 Mr. Van Hollen (for himself and Ms. Alsobrooks ) introduced the following bill; which was read twice and referred to the Committee on Homeland Security and Governmental Affairs\nA BILL\nTo appropriate funds for pay and allowances of Federal employees during the lapse in appropriations that began on October 1, 2025, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the True Shutdown Fairness Act .\n#### 2. Appropriations\n##### (a) Definitions\nIn this section\u2014\n**(1)**\nthe term agency means\u2014\n**(A)**\neach authority of the executive, legislative, or judicial branch of the Government of the United States; and\n**(B)**\neach District of Columbia public employer described in clause (i) or (ii) of section 1341(c)(1)(B) of title 31, United States Code (as in effect on the day before the date of enactment of this Act);\n**(2)**\nthe term contract employee means a contract employee for which the lapse of appropriation suspended, delayed, or interrupted all or part of the work of the contract, or stopped all or part of the work called for in such contract, including\u2014\n**(A)**\na service employee, as defined in section 6701(3) of title 41, United States Code, except that an individual covered under this subparagraph includes an individual described in subparagraph (C) of such section 6701(3);\n**(B)**\na laborer or mechanic with respect to whom section 3142 of title 40, United States Code, applies; and\n**(C)**\nan employee of a business concern that holds a contract, subcontract, or other agreement with an agency that provides for services or supplies, including a service contract under chapter 67 of title 41, United States Code;\n**(3)**\nthe term covered individual \u2014\n**(A)**\nmeans each employee of an agency, without regard to whether, during the period of the covered lapse in appropriations with respect to that agency occurring before the date of enactment of this Act\u2014\n**(i)**\nthe head of that agency determined that the individual was an excepted employee or an employee performing emergency work, as those terms are defined by the Office of Personnel Management or the appropriate District of Columbia public employer, as applicable; or\n**(ii)**\nthe individual was subject to furlough; and\n**(B)**\nincludes\u2014\n**(i)**\na contract employee;\n**(ii)**\na member of the Armed Forces on active duty; and\n**(iii)**\na member of a reserve component who, during the covered lapse in appropriations with respect to the applicable agency, performs active service or inactive-duty training;\n**(4)**\nthe term covered lapse in appropriations means, with respect to an agency, the lapse in appropriations with respect to that agency beginning on October 1, 2025, and ending on the termination date; and\n**(5)**\nthe term termination date means the date on which, after the start of the covered lapse in appropriations\u2014\n**(A)**\nthere are enacted into law appropriations for the agency (including a continuing appropriation) that provide amounts for the purposes for which amounts are made available under subsection (b); or\n**(B)**\nthere are enacted into law appropriations for the agency (including a continuing appropriation) without any appropriation for such purposes.\n##### (b) Appropriations\nFor fiscal year 2026, there are appropriated to the head of each agency with respect to which there is a covered lapse in appropriations, out of any money in the Treasury not otherwise appropriated, such sums as are necessary to provide, with respect to the covered lapse in appropriations, standard rates of pay, allowances, pay differentials, benefits, and other payments otherwise payable on a regular basis to covered individuals with respect to the agency, subject to the limitation under paragraph (2).\n##### (c) Price adjustment\n**(1) In general**\nAs soon as practicable after the date of the enactment of this Act, the head of any agency subject to the covered lapse in appropriations shall adjust the price of any contract described in paragraph (2) to compensate the contractor for reasonable costs incurred as described in paragraph (3), regardless of whether the contract provides for, or otherwise prohibits, the contractor to incur such reasonable costs or receive such an adjustment for incurring such reasonable costs.\n**(2) Contract described**\nA contract is described in this paragraph if it is a contract of an agency for which the contractor suspended, delayed, or interrupted all or part of the work under such contract, or stopped all or any part of the work called for in such contract, as a result of the covered lapse in appropriations.\n**(3) Reasonable costs described**\nReasonable costs described in this paragraph are costs actually incurred by the contractor\u2014\n**(A)**\nto provide compensation for the period of the covered lapse in appropriations, at an employee\u2019s standard rate of compensation, to any employee who, as a result of the lapse in appropriations\u2014\n**(i)**\nwas furloughed or laid off;\n**(ii)**\nwas otherwise not working;\n**(iii)**\nexperienced a reduction of hours; or\n**(iv)**\nexperienced a reduction in compensation; or\n**(B)**\nto restore paid leave taken by any employee during the lapse in appropriations, if the contractor required or permitted employees to use paid leave as a result of the lapse in appropriations.\n**(4) Evidence**\nA contractor seeking an adjustment under paragraph (1) shall provide the head of the applicable agency any evidence of the reasonable costs incurred by the contractor as described in paragraph (3) as the head of the agency, in consultation with the Administrator of the Office of Federal Procurement Policy, considers appropriate.\n##### (d) Termination\nAppropriations and funds made available and authority granted under subsection (b) shall be available to the head of an agency until the termination date.\n##### (e) Charge to future appropriations\nExpenditures made pursuant to this Act shall be charged to the applicable appropriation, fund, or authorization whenever a bill in which such applicable appropriation, fund, or authorization is enacted into law.\n##### (f) Retroactive effective date\nThis section shall take effect as if enacted on September 30, 2025.\n#### 3. Limitation on reductions in force\n##### (a) Definitions\nIn this section, the terms agency and covered lapse in appropriations have the meanings given those terms in section 2(a).\n##### (b) Prohibition\nDuring the covered lapse in appropriations, none of the funds made available by this or any other Act may be used to\u2014\n**(1)**\npropose or implement a reduction in force, or any similar effort, to permanently reduce the number of employees employed by an agency; or\n**(2)**\nplace any employee of an agency in administrative leave for more than 10 work days in any calendar year.\n##### (c) Rule of construction\nNothing in this section may be construed to affect a voluntary separation payment offered to an employee under section 3523 of title 5, United States Code.",
      "versionDate": "2025-11-07",
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
        "actionDate": "2025-10-23",
        "text": "Read twice and referred to the Committee on Homeland Security and Governmental Affairs."
      },
      "number": "3039",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "True Shutdown Fairness Act",
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
        "name": "Government Operations and Politics",
        "updateDate": "2026-01-14T15:55:20Z"
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
      "date": "2025-11-07",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s3165is.xml"
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
      "title": "True Shutdown Fairness Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-11-19T12:03:18Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "True Shutdown Fairness Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-11-13T12:08:14Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to appropriate funds for pay and allowances of Federal employees during the lapse in appropriations that began on October 1, 2025, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-11-13T12:03:24Z"
    }
  ]
}
```
