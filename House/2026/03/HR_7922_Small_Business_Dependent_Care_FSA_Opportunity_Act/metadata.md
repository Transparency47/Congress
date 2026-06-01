# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/7922?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/7922
- Title: Small Business Dependent Care FSA Opportunity Act
- Congress: 119
- Bill type: HR
- Bill number: 7922
- Origin chamber: House
- Introduced date: 2026-03-12
- Update date: 2026-03-31T21:28:25Z
- Update date including text: 2026-03-31T21:28:25Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2026-03-12: Introduced in House
- 2026-03-12 - IntroReferral: Introduced in House
- 2026-03-12 - IntroReferral: Introduced in House
- 2026-03-12 - IntroReferral: Referred to the House Committee on Ways and Means.
- Latest action: 2026-03-12: Introduced in House

## Actions

- 2026-03-12 - IntroReferral: Introduced in House
- 2026-03-12 - IntroReferral: Introduced in House
- 2026-03-12 - IntroReferral: Referred to the House Committee on Ways and Means.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-03-12",
    "latestAction": {
      "actionDate": "2026-03-12",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/7922",
    "number": "7922",
    "originChamber": "House",
    "policyArea": {
      "name": "Taxation"
    },
    "sponsors": [
      {
        "bioguideId": "S001172",
        "district": "3",
        "firstName": "Adrian",
        "fullName": "Rep. Smith, Adrian [R-NE-3]",
        "lastName": "Smith",
        "party": "R",
        "state": "NE"
      }
    ],
    "title": "Small Business Dependent Care FSA Opportunity Act",
    "type": "HR",
    "updateDate": "2026-03-31T21:28:25Z",
    "updateDateIncludingText": "2026-03-31T21:28:25Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2026-03-12",
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
      "actionDate": "2026-03-12",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-03-12",
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
          "date": "2026-03-12T13:33:35Z",
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
      "bioguideId": "D000096",
      "district": "7",
      "firstName": "Danny",
      "fullName": "Rep. Davis, Danny K. [D-IL-7]",
      "isOriginalCosponsor": "True",
      "lastName": "Davis",
      "middleName": "K.",
      "party": "D",
      "sponsorshipDate": "2026-03-12",
      "state": "IL"
    },
    {
      "bioguideId": "M001224",
      "district": "1",
      "firstName": "Nathaniel",
      "fullName": "Rep. Moran, Nathaniel [R-TX-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Moran",
      "party": "R",
      "sponsorshipDate": "2026-03-12",
      "state": "TX"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7922ih.xml",
      "text": "I\n119th CONGRESS\n2d Session\nH. R. 7922\nIN THE HOUSE OF REPRESENTATIVES\nMarch 12, 2026 Mr. Smith of Nebraska (for himself, Mr. Davis of Illinois , and Mr. Moran ) introduced the following bill; which was referred to the Committee on Ways and Means\nA BILL\nTo amend the Internal Revenue Code of 1986 to provide a credit to certain small employers for the startup costs of dependent care flexible spending plans.\n#### 1. Short title\nThis Act may be cited as the Small Business Dependent Care FSA Opportunity Act .\n#### 2. Small employer dependent care flexible spending plan startup costs\n##### (a) In general\nSubpart D of part IV of subchapter A of chapter 1 of the Internal Revenue Code of 1986 is amended by adding at the end the following new section:\n45BB. Small employer dependent care flexible spending plan startup costs (a) In general For purposes of section 38, in the case of an eligible employer, the small employer dependent care flexible spending plan startup cost credit determined under this section for any taxable year is an amount equal to the qualified startup costs paid or incurred by the taxpayer during the taxable year. (b) Dollar limitation The amount of the credit determined under this section for any taxable year shall not exceed\u2014 (1) for the first credit year and each of the 2 taxable years immediately following the first credit year, the greater of\u2014 (A) $500, or (B) the lesser of\u2014 (i) $250 for each employee of the eligible employer who is not a highly compensated employee (as defined in section 414(q)) and who is eligible to participate in the dependent care flexible spending plan maintained by the eligible employer, or (ii) $5,000, and (2) zero for any other taxable year. (c) Eligible employer For purposes of this section\u2014 (1) In general The term eligible employer has the meaning given such term by section 408(p)(2)(C)(i). (2) Requirement for new dependent care flexible spending plans Such term shall not include an employer if, during the 3-taxable year period immediately preceding the 1st taxable year for which the credit under this section is otherwise allowable for a dependent care flexible spending plan of the employer, the employer or any member of any controlled group including the employer (or any predecessor of either) established or maintained a dependent care flexible spending plan for substantially the same employees as the employees for whom the dependent care flexible spending plan with respect to which such credit is otherwise allowable is established or maintained. (d) Other definitions For purposes of this section\u2014 (1) In general The term qualified startup costs means any ordinary and necessary expenses of an eligible employer which are paid or incurred in connection with\u2014 (A) the establishment or administration of a dependent care flexible spending plan, or (B) education of employees with respect to such plan. (2) Plan must have at least 1 participant Such term shall not include any expense in connection with a plan that does not have at least 1 employee eligible to participate who is not a highly compensated employee (as defined in section 414(q)). (3) Dependent care flexible spending plan The term dependent care flexible spending plan means so much of any plan of an employer as consists of dependent care flexible spending arrangements. For purposes of the preceding sentence, an arrangement shall be treated as a dependent care flexible spending arrangement only if employer contributions to such arrangement are excludible from the gross income of an employee under section 129. (4) First credit year The term first credit year means, with respect to any qualified startup costs\u2014 (A) the taxable year which includes the date that the dependent care flexible spending plan to which such costs relate becomes effective, or (B) at the election of the eligible employer, the taxable year preceding the taxable year referred to in subparagraph (A). (e) Special rules Rules similar to the rules of section 45E(e) shall apply for purposes of this section. .\n##### (b) Credit To be part of general business credit\nSection 38(b) of such Code is amended by striking plus at the end of paragraph (40), by striking the period at the end of paragraph (41) and inserting , plus , and by adding at the end the following new paragraph:\n(42) in the case of an eligible employer (as defined in section 45BB(c)), the small employer dependent care flexible spending plan startup cost credit determined under section 45BB. .\n##### (c) Clerical amendment\nThe table of sections for subpart D of part IV of subchapter A of chapter 1 of such Code is amended by adding at the end the following new item:\nSec. 45BB. Small employer dependent care flexible spending plan startup costs. .\n##### (d) Effective date\nThe amendments made by this section shall apply to amounts paid or incurred after the date of the enactment of this Act, in taxable years ending after such date.",
      "versionDate": "2026-03-12",
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
        "updateDate": "2026-03-31T21:28:24Z"
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
      "date": "2026-03-12",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7922ih.xml"
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
      "title": "Small Business Dependent Care FSA Opportunity Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-03-28T12:23:31Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Small Business Dependent Care FSA Opportunity Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-03-28T12:23:30Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Internal Revenue Code of 1986 to provide a credit to certain small employers for the startup costs of dependent care flexible spending plans.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-03-28T12:18:25Z"
    }
  ]
}
```
