# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/5690?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/5690
- Title: Emergency Relief for Federal Contractors Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 5690
- Origin chamber: House
- Introduced date: 2025-10-03
- Update date: 2025-12-05T21:34:42Z
- Update date including text: 2025-12-05T21:34:42Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-10-03: Introduced in House
- 2025-10-03 - IntroReferral: Introduced in House
- 2025-10-03 - IntroReferral: Introduced in House
- 2025-10-03 - IntroReferral: Referred to the House Committee on Ways and Means.
- Latest action: 2025-10-03: Introduced in House

## Actions

- 2025-10-03 - IntroReferral: Introduced in House
- 2025-10-03 - IntroReferral: Introduced in House
- 2025-10-03 - IntroReferral: Referred to the House Committee on Ways and Means.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-10-03",
    "latestAction": {
      "actionDate": "2025-10-03",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/5690",
    "number": "5690",
    "originChamber": "House",
    "policyArea": {
      "name": "Taxation"
    },
    "sponsors": [
      {
        "bioguideId": "S001230",
        "district": "10",
        "firstName": "Suhas",
        "fullName": "Rep. Subramanyam, Suhas [D-VA-10]",
        "lastName": "Subramanyam",
        "party": "D",
        "state": "VA"
      }
    ],
    "title": "Emergency Relief for Federal Contractors Act of 2025",
    "type": "HR",
    "updateDate": "2025-12-05T21:34:42Z",
    "updateDateIncludingText": "2025-12-05T21:34:42Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-10-03",
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
      "actionDate": "2025-10-03",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-10-03",
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
          "date": "2025-10-03T19:32:25Z",
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
      "bioguideId": "W000831",
      "district": "11",
      "firstName": "James",
      "fullName": "Rep. Walkinshaw, James R. [D-VA-11]",
      "isOriginalCosponsor": "True",
      "lastName": "Walkinshaw",
      "middleName": "R.",
      "party": "D",
      "sponsorshipDate": "2025-10-03",
      "state": "VA"
    },
    {
      "bioguideId": "B001292",
      "district": "8",
      "firstName": "Donald",
      "fullName": "Rep. Beyer, Donald S. [D-VA-8]",
      "isOriginalCosponsor": "True",
      "lastName": "Beyer",
      "middleName": "S.",
      "party": "D",
      "sponsorshipDate": "2025-10-03",
      "state": "VA"
    },
    {
      "bioguideId": "M001227",
      "district": "4",
      "firstName": "Jennifer",
      "fullName": "Rep. McClellan, Jennifer L. [D-VA-4]",
      "isOriginalCosponsor": "True",
      "lastName": "McClellan",
      "middleName": "L.",
      "party": "D",
      "sponsorshipDate": "2025-10-03",
      "state": "VA"
    },
    {
      "bioguideId": "E000301",
      "district": "3",
      "firstName": "Sarah",
      "fullName": "Rep. Elfreth, Sarah [D-MD-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Elfreth",
      "party": "D",
      "sponsorshipDate": "2025-10-03",
      "state": "MD"
    },
    {
      "bioguideId": "N000147",
      "district": "0",
      "firstName": "Eleanor",
      "fullName": "Del. Norton, Eleanor Holmes [D-DC-At Large]",
      "isOriginalCosponsor": "True",
      "lastName": "Norton",
      "middleName": "Holmes",
      "party": "D",
      "sponsorshipDate": "2025-10-03",
      "state": "DC"
    },
    {
      "bioguideId": "S001193",
      "district": "14",
      "firstName": "Eric",
      "fullName": "Rep. Swalwell, Eric [D-CA-14]",
      "isOriginalCosponsor": "True",
      "lastName": "Swalwell",
      "party": "D",
      "sponsorshipDate": "2025-10-03",
      "state": "CA"
    },
    {
      "bioguideId": "H001066",
      "district": "4",
      "firstName": "Steven",
      "fullName": "Rep. Horsford, Steven [D-NV-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Horsford",
      "party": "D",
      "sponsorshipDate": "2025-10-03",
      "state": "NV"
    },
    {
      "bioguideId": "B001324",
      "district": "1",
      "firstName": "Wesley",
      "fullName": "Rep. Bell, Wesley [D-MO-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Bell",
      "party": "D",
      "sponsorshipDate": "2025-10-08",
      "state": "MO"
    },
    {
      "bioguideId": "L000557",
      "district": "1",
      "firstName": "John",
      "fullName": "Rep. Larson, John B. [D-CT-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Larson",
      "middleName": "B.",
      "party": "D",
      "sponsorshipDate": "2025-10-21",
      "state": "CT"
    },
    {
      "bioguideId": "V000138",
      "district": "7",
      "firstName": "Eugene",
      "fullName": "Rep. Vindman, Eugene Simon [D-VA-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Vindman",
      "middleName": "Simon",
      "party": "D",
      "sponsorshipDate": "2025-10-21",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr5690ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 5690\nIN THE HOUSE OF REPRESENTATIVES\nOctober 3, 2025 Mr. Subramanyam (for himself, Mr. Walkinshaw , Mr. Beyer , Ms. McClellan , Ms. Elfreth , Ms. Norton , Mr. Swalwell , and Mr. Horsford ) introduced the following bill; which was referred to the Committee on Ways and Means\nA BILL\nTo allow penalty-free distributions from retirement accounts in the case of certain Federal contractors impacted by Federal Government shutdowns.\n#### 1. Short title\nThis Act may be cited as the Emergency Relief for Federal Contractors Act of 2025 .\n#### 2. Tax-favored withdrawals from retirement plans\n##### (a) In general\nSection 72(t) of the Internal Revenue Code of 1986 shall not apply to any Federal Government shutdown distribution.\n##### (b) Aggregate dollar limitation\n**(1) In general**\n**(A) Limitation**\nFor purposes of this section, the aggregate amount of distributions received by an individual which may be treated as Federal Government shutdown distributions for any taxable year shall not exceed $30,000.\n**(B) Inflation adjustment**\nIn the case of any taxable year beginning after 2025, the $30,000 amount under subparagraph (A) shall be increased by an amount equal to\u2014\n**(i)**\nsuch dollar amount, multiplied by\n**(ii)**\nthe cost-of-living adjustment determined under section 1(f)(3) of the Internal Revenue Code of 1986 for the calendar year in which the taxable year begins, determined by substituting calendar year 2024 for calendar year 2016 in subparagraph (A)(ii) thereof.\nIf any amount as adjusted\n              under the preceding sentence is not a multiple of $500, such amount shall be rounded\n              to the nearest multiple of $500.\n**(2) Treatment of plan distributions**\nIf a distribution to an individual would (without regard to paragraph (1)) be a Federal Government shutdown distribution, a plan shall not be treated as violating any provision of law merely because the plan treats such distribution as a Federal Government shutdown distribution, unless the aggregate amount of such distributions from all plans maintained by the employer (and any member of any controlled group which includes the employer) to such individual for any taxable year exceeds the dollar amount in effect under paragraph (1)(A).\n**(3) Controlled group**\nFor purposes of paragraph (2), the term controlled group means any group treated as a single employer under subsection (b), (c), (m), or (o) of section 414 of the Internal Revenue Code of 1986.\n##### (c) Amount distributed may be repaid\n**(1) In general**\nAny individual who receives a Federal Government shutdown distribution may, at any time during the 3-year period beginning on the day after the date on which such distribution was received, make 1 or more contributions in an aggregate amount not to exceed the amount of such distribution to an eligible retirement plan of which such individual is a beneficiary and to which a rollover contribution of such distribution could be made under section 402(c), 403(a)(4), 403(b)(8), 408(d)(3), or 457(e)(16) of the Internal Revenue Code of 1986, as the case may be.\n**(2) Treatment of repayments of distributions from eligible retirement plans other than IRAs**\nFor purposes of the Internal Revenue Code of 1986, if a contribution is made pursuant to paragraph (1) with respect to a Federal Government shutdown distribution from an eligible retirement plan other than an individual retirement plan, then the taxpayer shall, to the extent of the amount of the contribution, be treated as having received the Federal Government shutdown distribution in an eligible rollover distribution (as defined in section 402(c)(4) of such Code) and as having transferred the amount to the eligible retirement plan in a direct trustee to trustee transfer within 60 days of the distribution.\n**(3) Treatment of repayments of distributions from IRAs**\nFor purposes of the Internal Revenue Code of 1986, if a contribution is made pursuant to paragraph (1) with respect to a Federal Government shutdown distribution from an individual retirement plan (as defined by section 7701(a)(37) of such Code), then, to the extent of the amount of the contribution, the Federal Government shutdown distribution shall be treated as a distribution described in section 408(d)(3) of such Code and as having been transferred to the eligible retirement plan in a direct trustee to trustee transfer within 60 days of the distribution.\n##### (d) Definitions\nFor purposes of this section\u2014\n**(1) Federal Government shutdown distribution**\nThe term Federal Government shutdown distribution means any distribution which is\u2014\n**(A)**\nreceived by an applicable individual from an eligible retirement plan; and\n**(B)**\nmade during a Federal appropriations lapse with respect to such individual.\n**(2) Applicable individual**\nThe term applicable individual means any individual\u2014\n**(A)**\nwho\u2014\n**(i)**\nis a Federal contractor or an employee of a Federal contractor, and\n**(ii)**\nis placed on unpaid leave or working without pay due to a Federal appropriations lapse,\n**(B)**\nwho\u2014\n**(i)**\nis an employee of a Federal grantee or of a State,\n**(ii)**\nwhose compensation is advanced or reimbursed in whole or in part by the Federal Government, and\n**(iii)**\nis furloughed, working without pay, or working with a decrease in pay due to a Federal appropriations lapse, or\n**(C)**\nwho\u2014\n**(i)**\nis an employee of\u2014\n**(I)**\nthe District of Columbia Courts,\n**(II)**\nthe Public Defender Service for the District of Columbia, or\n**(III)**\nthe District of Columbia Government, and\n**(ii)**\nis furloughed or working without pay due to a Federal appropriations lapse.\n**(3) Federal appropriations lapse**\n**(A) In general**\nThe term Federal appropriations lapse means any continuous period of at least 2 weeks during which there is a lapse in Federal appropriations (including a partial lapse).\n**(B) Period of lapse**\nA period of lapse in Federal appropriations shall not be a Federal appropriations lapse with respect to an individual for longer than the period during which the individual is furloughed, on unpaid leave, or performing work without pay (or working with a decrease in pay in the case of an applicable individual described in paragraph (2)(B)(iii)) due to such lapse.\n**(4) Eligible retirement plan**\nThe term eligible retirement plan has the meaning given such term by section 402(c)(8)(B) of the Internal Revenue Code of 1986.\n##### (e) Income inclusion spread over 3-Year period\n**(1) In general**\nUnless the taxpayer elects not to have this paragraph apply for any taxable year, any amount required to be included in gross income for such taxable year with respect to any Federal Government shutdown distribution shall be so included ratably over the 3-taxable-year period beginning with such taxable year.\n**(2) Special rule**\nFor purposes of paragraph (1), rules similar to the rules of subparagraph (E) of section 408A(d)(3) of the Internal Revenue Code of 1986 shall apply.\n##### (f) Special rules\n**(1) Exemption of distributions from trustee to trustee transfer and withholding rules**\nFor purposes of sections 401(a)(31), 402(f), and 3405 of the Internal Revenue Code of 1986, a Federal Government shutdown distribution shall not be treated as an eligible rollover distribution.\n**(2) Federal Government shutdown distributions treated as meeting plan distribution requirements**\nFor purposes of the Internal Revenue Code of 1986, a Federal Government shutdown distribution shall be treated as meeting the requirements of sections 401(k)(2)(B)(i), 403(b)(7)(A)(i), 403(b)(11), and 457(d)(1)(A) of such Code.",
      "versionDate": "2025-10-03",
      "versionType": "Introduced in House"
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
        "actionDate": "2025-10-01",
        "text": "Read twice and referred to the Committee on Finance."
      },
      "number": "2964",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Emergency Relief for Federal Contractors Act of 2025",
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
        "name": "Taxation",
        "updateDate": "2025-10-17T12:47:19Z"
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
      "date": "2025-10-03",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr5690ih.xml"
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
      "title": "Emergency Relief for Federal Contractors Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-10-16T09:38:15Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Emergency Relief for Federal Contractors Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-10-16T09:38:13Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To allow penalty-free distributions from retirement accounts in the case of certain Federal contractors impacted by Federal Government shutdowns.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-10-16T09:33:17Z"
    }
  ]
}
```
