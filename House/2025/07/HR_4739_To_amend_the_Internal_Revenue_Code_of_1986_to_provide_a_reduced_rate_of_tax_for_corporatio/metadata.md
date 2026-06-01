# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/4739?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/4739
- Title: SHARE Plan Act
- Congress: 119
- Bill type: HR
- Bill number: 4739
- Origin chamber: House
- Introduced date: 2025-07-23
- Update date: 2025-11-29T09:05:19Z
- Update date including text: 2025-11-29T09:05:19Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-07-23: Introduced in House
- 2025-07-23 - IntroReferral: Introduced in House
- 2025-07-23 - IntroReferral: Introduced in House
- 2025-07-23 - IntroReferral: Referred to the House Committee on Ways and Means.
- Latest action: 2025-07-23: Introduced in House

## Actions

- 2025-07-23 - IntroReferral: Introduced in House
- 2025-07-23 - IntroReferral: Introduced in House
- 2025-07-23 - IntroReferral: Referred to the House Committee on Ways and Means.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-07-23",
    "latestAction": {
      "actionDate": "2025-07-23",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/4739",
    "number": "4739",
    "originChamber": "House",
    "policyArea": {
      "name": "Taxation"
    },
    "sponsors": [
      {
        "bioguideId": "S001201",
        "district": "3",
        "firstName": "Thomas",
        "fullName": "Rep. Suozzi, Thomas R. [D-NY-3]",
        "lastName": "Suozzi",
        "party": "D",
        "state": "NY"
      }
    ],
    "title": "SHARE Plan Act",
    "type": "HR",
    "updateDate": "2025-11-29T09:05:19Z",
    "updateDateIncludingText": "2025-11-29T09:05:19Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-07-23",
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
      "actionDate": "2025-07-23",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-07-23",
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
          "date": "2025-07-23T14:17:05Z",
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
      "bioguideId": "K000376",
      "district": "16",
      "firstName": "Mike",
      "fullName": "Rep. Kelly, Mike [R-PA-16]",
      "isOriginalCosponsor": "True",
      "lastName": "Kelly",
      "party": "R",
      "sponsorshipDate": "2025-07-23",
      "state": "PA"
    },
    {
      "bioguideId": "T000460",
      "district": "4",
      "firstName": "Mike",
      "fullName": "Rep. Thompson, Mike [D-CA-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Thompson",
      "party": "D",
      "sponsorshipDate": "2025-07-23",
      "state": "CA"
    },
    {
      "bioguideId": "F000466",
      "district": "1",
      "firstName": "Brian",
      "fullName": "Rep. Fitzpatrick, Brian K. [R-PA-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Fitzpatrick",
      "middleName": "K.",
      "party": "R",
      "sponsorshipDate": "2025-07-23",
      "state": "PA"
    },
    {
      "bioguideId": "L000557",
      "district": "1",
      "firstName": "John",
      "fullName": "Rep. Larson, John B. [D-CT-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Larson",
      "middleName": "B.",
      "party": "D",
      "sponsorshipDate": "2025-07-23",
      "state": "CT"
    },
    {
      "bioguideId": "M000317",
      "district": "11",
      "firstName": "Nicole",
      "fullName": "Rep. Malliotakis, Nicole [R-NY-11]",
      "isOriginalCosponsor": "True",
      "lastName": "Malliotakis",
      "party": "R",
      "sponsorshipDate": "2025-07-23",
      "state": "NY"
    },
    {
      "bioguideId": "P000613",
      "district": "19",
      "firstName": "Jimmy",
      "fullName": "Rep. Panetta, Jimmy [D-CA-19]",
      "isOriginalCosponsor": "True",
      "lastName": "Panetta",
      "party": "D",
      "sponsorshipDate": "2025-07-23",
      "state": "CA"
    },
    {
      "bioguideId": "T000478",
      "district": "24",
      "firstName": "Claudia",
      "fullName": "Rep. Tenney, Claudia [R-NY-24]",
      "isOriginalCosponsor": "True",
      "lastName": "Tenney",
      "party": "R",
      "sponsorshipDate": "2025-07-23",
      "state": "NY"
    },
    {
      "bioguideId": "S001185",
      "district": "7",
      "firstName": "Terri",
      "fullName": "Rep. Sewell, Terri A. [D-AL-7]",
      "isOriginalCosponsor": "True",
      "lastName": "Sewell",
      "middleName": "A.",
      "party": "D",
      "sponsorshipDate": "2025-07-23",
      "state": "AL"
    },
    {
      "bioguideId": "S001199",
      "district": "11",
      "firstName": "Lloyd",
      "fullName": "Rep. Smucker, Lloyd [R-PA-11]",
      "isOriginalCosponsor": "True",
      "lastName": "Smucker",
      "party": "R",
      "sponsorshipDate": "2025-07-23",
      "state": "PA"
    },
    {
      "bioguideId": "H001066",
      "district": "4",
      "firstName": "Steven",
      "fullName": "Rep. Horsford, Steven [D-NV-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Horsford",
      "party": "D",
      "sponsorshipDate": "2025-07-23",
      "state": "NV"
    },
    {
      "bioguideId": "N000147",
      "district": "0",
      "firstName": "Eleanor",
      "fullName": "Del. Norton, Eleanor Holmes [D-DC-At Large]",
      "isOriginalCosponsor": "False",
      "lastName": "Norton",
      "middleName": "Holmes",
      "party": "D",
      "sponsorshipDate": "2025-07-29",
      "state": "DC"
    },
    {
      "bioguideId": "B001257",
      "district": "12",
      "firstName": "Gus",
      "fullName": "Rep. Bilirakis, Gus M. [R-FL-12]",
      "isOriginalCosponsor": "False",
      "lastName": "Bilirakis",
      "middleName": "M.",
      "party": "R",
      "sponsorshipDate": "2025-08-29",
      "state": "FL"
    },
    {
      "bioguideId": "N000193",
      "district": "3",
      "firstName": "Zachary",
      "fullName": "Rep. Nunn, Zachary [R-IA-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Nunn",
      "party": "R",
      "sponsorshipDate": "2025-11-28",
      "state": "IA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr4739ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 4739\nIN THE HOUSE OF REPRESENTATIVES\nJuly 23, 2025 Mr. Suozzi (for himself, Mr. Kelly of Pennsylvania , Mr. Thompson of California , Mr. Fitzpatrick , Mr. Larson of Connecticut , Ms. Malliotakis , Mr. Panetta , Ms. Tenney , Ms. Sewell , Mr. Smucker , and Mr. Horsford ) introduced the following bill; which was referred to the Committee on Ways and Means\nA BILL\nTo amend the Internal Revenue Code of 1986 to provide a reduced rate of tax for corporations that maintain a plan for distributing equity to employees, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Share Holder Allocation for Rewards to Employees Plan Act or as the SHARE Plan Act .\n#### 2. Reduced rate of tax for corporations that maintain a plan for distributing equity to employees\n##### (a) In general\nPart II of subchapter A of chapter 1 of the Internal Revenue Code of 1986 is amended by redesignating section 12 as section 13 and by inserting after section 11 the following new new section:\n12. Reduced rate of tax for corporations maintaining SHARE plans (a) In general In the case of any corporation which is a SHARE corporation for any taxable year, the rate of tax under section 11(b) shall be 3 percentage points less than the rate of tax otherwise in effect under such section. The preceding sentence shall not apply to any SHARE corporation for any taxable year, if the application of such sentence to such taxable year would cause the aggregate income tax reductions for such taxable year and all preceding taxable years of such corporation by reason of this section to exceed the aggregate market value of stock described in subsection (c)(1)(A) (determined as of the date of issue of such stock) with respect to such corporation. (b) SHARE corporation For purposes of this section\u2014 (1) In general The term SHARE corporation means, with respect to any taxable year, any corporation\u2014 (A) which has an average of 500 or more full-time employees resident in the United States during such taxable year, (B) which (as of the close of such taxable year) is domiciled in the United States, (C) which demonstrates to the satisfaction of the Secretary that such corporation (as of the close of such taxable year) has\u2014 (i) a SHARE ratio of not less than 5 percent, or (ii) made distributions of common stock of such corporation to employees of such corporation pursuant to a SHARE plan during such taxable year which in the aggregate equals or exceeds 1 percent of the aggregate outstanding shares of common stock of such corporation (other than shares held by such corporation), and (D) in the case of any corporation the common stock of which is not (as of the close of such taxable year) regularly traded on an established securities market, which demonstrates to the satisfaction of the Secretary that such corporation has\u2014 (i) conducted (as of the close of such taxable year) a valid market valuation of such corporation, and (ii) provided employees with adequate opportunities during such taxable year to liquidate the employee\u2019s holdings of such corporation\u2019s stock at the fair market value of such stock. (2) Safe harbor for elective limitation on amount of stock granted to each employee (A) In general A corporation shall not be treated as failing to meet the requirement of paragraph (1)(C) solely because the SHARE plan of such corporation provides that the amount of common stock of such corporation distributed under such plan to each employee shall not exceed $250,000 (determined on the basis of the fair market value of each share on the date of issuance of such share). (B) Adjustment In the case of any taxable year beginning after December 31, 2025, the Secretary shall annually adjust the $250,000 amount specified in subparagraph (A) to take into account national private sector wage growth (determined with respect to a base year of 2024). (c) SHARE ratio For purposes of this section\u2014 (1) In general The term SHARE ratio means, with respect to any corporation for any taxable year, the ratio (expressed as a percentage) of\u2014 (A) the aggregate shares of common stock of such corporation which have been granted to participating employees of such corporation pursuant to a SHARE plan during such taxable year or any prior taxable year, divided by (B) the aggregate outstanding shares of common stock of such corporation (other than shares held by such corporation). (2) Treatment of certain grants before establishment of SHARE plan If such corporation demonstrates to the satisfaction of the Secretary that, during the 10 years preceding the date of the enactment of this section, such corporation made grants of common stock to eligible employees of such corporation which were not in exchange for compensation (other than service as an employee), such stock shall be taken into account under paragraph (1)(A). (3) Treatment of convertible stock In the case of any class of stock of any corporation which may be converted to common stock, such stock shall be taken into account as common stock under paragraphs (1)(B) and (2) on a fully diluted basis. (4) Exclusion of incentive equity (A) In general Incentive equity shall not be taken into account under subparagraph (A) or (B) of paragraph (1) (including any stock which would otherwise be so taken into account by reason of paragraph (2) or (3)). (B) Incentive equity For purposes of this paragraph, the term incentive equity means any performance-based restricted stock granted to an employee of the corporation, any stock acquired pursuant to a performance-based incentive stock option granted to an employee of the corporation, or any similar grant of performance-based stock or convertible equity. (5) Treatment of forfeited stock In the case of any stock which is forfeited (by reason of a failure to vest or otherwise), such stock shall not be taken into account under paragraph (1) after the second calendar year following the calendar year in which such stock is so forfeited. (d) SHARE plan For purposes of this section\u2014 (1) In general The term SHARE plan means, with respect to any corporation, a plan which provides for making periodic distributions of common stock of such corporation to each participating employee of such corporation (determined as the date of each such periodic distribution). (2) Participating employees (A) In general The term participating employee means, with respect to any corporation, any eligible employee of such corporation who is treated as a participating employee under the terms of the plan. (B) 80-percent requirement A plan shall not be treated as a SHARE plan unless, with respect to each periodic distribution made under such plan, the lowest compensated 80 percent of eligible employees of such corporation are participating employees with respect to such distribution. (3) Eligible employee The term eligible employee means, with respect to any corporation, any full-time employee who is based in the United States and who does not receive $250,000 or more in annual cash compensation from such corporation (determined without regard to SHARE plan stock). The $250,000 amount specified in the preceding sentence shall be adjusted as provided in subsection (b)(2)(B). (4) Common stock (A) In general The term common stock means, with respect to any corporation, stock which has the same economic and voting rights as the most widely held (determined without regard to any stock issued under the SHARE plan) common stock of such corporation which has both economic and voting rights. (B) Substitution of index-based mutual funds or ETFs Shares of an index-based mutual fund or exchange traded fund shall be treated for purposes of this section in the same manner as shares of common stock issued by the corporation referred to in subparagraph (A) in the same ratio that the fair market value of such shares of the index-based mutual fund or exchange traded fund bears to the fair market value of such shares of common stock, determined as of the date that such shares of the index-based mutual fund or exchange traded fund are distributed to the employee. (5) Distribution requirements (A) In general A plan shall not be treated as a SHARE plan unless the distributions made under such plan\u2014 (i) are made without compensation (other than service as an employee), (ii) except as provided in subparagraph (B), are made in equal amounts to each participating employee (determined in the aggregate with respect to any calendar year and properly adjusted with respect any employee not employed at all times during such calendar year), (iii) vest in the employee after such period of employment of the employee by the distributing corporation as may be specified in such plan, except that the period so specified\u2014 (I) may not exceed 5 years and the employer may elect whether to treat periods of employment occurring before the establishment of the plan as counting toward such period, and (II) shall be treated as satisfied upon retirement, termination of employment without cause, or change in control of the corporation, and (iv) may be sold or transferred without restriction once vested. (B) Adjustments for period of service The requirement of subparagraph (A)(ii) shall be treated as met if such requirement is met when applied separately to groups of participating employees divided (under the terms of the corporation\u2019s SHARE plan) on the basis of the period for which such employees have been employed by the distributing corporation. (e) Publication by Treasury The Secretary shall make publicly available with respect to each taxable year a list of corporations which the Secretary has identified as SHARE corporations. (f) Deduction for SHARE plan stock distributions SHARE corporations shall be allowed a deduction equal to the fair market value (determined as of distribution) of stock distributed pursuant to a SHARE plan during the taxable year. (g) Corporate right To implement SHARE plan Notwithstanding any other provision of Federal, State, or local law, a corporation shall not be prevented or enjoined from, or subject to any monetary or other penalty or damages for, establishing, maintaining, or making distributions of stock pursuant to, a SHARE plan. (h) Aggregation rules In the case of any controlled group (within the meaning of section 1563(a)), the Secretary may issue such regulations or other guidance as the Secretary determines to be appropriate for purposes of applying the provisions of this section to such group, including regulations or other guidance that coordinates or consolidates the SHARE plans of the corporations in such group or allows or requires employees of any corporation in such group to receive stock of another corporation in such group pursuant to such SHARE plans. .\n##### (b) Clerical amendment\nThe table of sections for part II of subchapter A of chapter 1 of the Internal Revenue Code of 1986 is amended by redesignating the item relating to section 12 as an item relating to section 13 and by inserting after the item relating to section 11 the following new item:\nSec. 12. Reduced rate of tax for corporations maintaining SHARE plans. .\n##### (c) Effective date\nThe amendments made by this section shall apply to taxable years beginning more than 1 year after the date of the enactment of this Act.\n#### 3. Distributions of stock issued under SHARE plans excluded from gross income\n##### (a) In general\nPart III of subchapter B of chapter 1 of the Internal Revenue Code of 1986 is amended by inserting after section 139I the following new section:\n139J. SHARE plan distributions (a) In general Gross income shall not include any SHARE plan stock received by an employee under a SHARE plan. (b) Definitions related to SHARE plans For purposes of this section\u2014 (1) SHARE plan The term SHARE plan has the meaning given such term in section 12. (2) SHARE plan stock The term SHARE plan stock means, with respect to any employee, stock received by such employee under a SHARE plan. .\n##### (b) Clerical amendment\nThe table of sections for part III of subchapter B of chapter 1 of the Internal Revenue Code of 1986 is amended by inserting after the item relating to section 139I the following new item:\nSec. 139J. SHARE plan distributions. .\n##### (c) Effective date\nThe amendments made by this section shall apply to stock received after the date of the enactment of this Act.",
      "versionDate": "2025-07-23",
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
        "updateDate": "2025-08-06T18:36:46Z"
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
      "date": "2025-07-23",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr4739ih.xml"
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
      "title": "SHARE Plan Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-08-05T12:23:22Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "SHARE Plan Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-08-05T12:23:20Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Share Holder Allocation for Rewards to Employees Plan Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-08-05T12:23:20Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Internal Revenue Code of 1986 to provide a reduced rate of tax for corporations that maintain a plan for distributing equity to employees, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-08-05T12:18:19Z"
    }
  ]
}
```
