# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/4507?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/4507
- Title: TUTOR Act
- Congress: 119
- Bill type: HR
- Bill number: 4507
- Origin chamber: House
- Introduced date: 2025-07-17
- Update date: 2025-12-10T09:05:32Z
- Update date including text: 2025-12-10T09:05:32Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-07-17: Introduced in House
- 2025-07-17 - IntroReferral: Introduced in House
- 2025-07-17 - IntroReferral: Introduced in House
- 2025-07-17 - IntroReferral: Referred to the House Committee on Ways and Means.
- Latest action: 2025-07-17: Introduced in House

## Actions

- 2025-07-17 - IntroReferral: Introduced in House
- 2025-07-17 - IntroReferral: Introduced in House
- 2025-07-17 - IntroReferral: Referred to the House Committee on Ways and Means.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-07-17",
    "latestAction": {
      "actionDate": "2025-07-17",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/4507",
    "number": "4507",
    "originChamber": "House",
    "policyArea": {
      "name": "Taxation"
    },
    "sponsors": [
      {
        "bioguideId": "K000399",
        "district": "2",
        "firstName": "Jennifer",
        "fullName": "Rep. Kiggans, Jennifer A. [R-VA-2]",
        "lastName": "Kiggans",
        "party": "R",
        "state": "VA"
      }
    ],
    "title": "TUTOR Act",
    "type": "HR",
    "updateDate": "2025-12-10T09:05:32Z",
    "updateDateIncludingText": "2025-12-10T09:05:32Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-07-17",
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
      "actionDate": "2025-07-17",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-07-17",
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
          "date": "2025-07-17T13:05:15Z",
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
      "bioguideId": "V000138",
      "district": "7",
      "firstName": "Eugene",
      "fullName": "Rep. Vindman, Eugene Simon [D-VA-7]",
      "isOriginalCosponsor": "True",
      "lastName": "Vindman",
      "middleName": "Simon",
      "party": "D",
      "sponsorshipDate": "2025-07-17",
      "state": "VA"
    },
    {
      "bioguideId": "M001208",
      "district": "6",
      "firstName": "Lucy",
      "fullName": "Rep. McBath, Lucy [D-GA-6]",
      "isOriginalCosponsor": "False",
      "lastName": "McBath",
      "party": "D",
      "sponsorshipDate": "2025-09-30",
      "state": "GA"
    },
    {
      "bioguideId": "G000602",
      "district": "4",
      "firstName": "Laura",
      "fullName": "Rep. Gillen, Laura [D-NY-4]",
      "isOriginalCosponsor": "False",
      "lastName": "Gillen",
      "party": "D",
      "sponsorshipDate": "2025-12-09",
      "state": "NY"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr4507ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 4507\nIN THE HOUSE OF REPRESENTATIVES\nJuly 17, 2025 Mrs. Kiggans of Virginia (for herself and Mr. Vindman ) introduced the following bill; which was referred to the Committee on Ways and Means\nA BILL\nTo amend the Internal Revenue Code of 1986 to establish a temporary tax credit for eligible teachers who provide tutoring services, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Teachers Utilizing Tutoring Opportunities for Relief Act or the TUTOR Act .\n#### 2. Tutoring credit\n##### (a) In general\nSubpart A of part IV of subchapter A of chapter 1 of the Internal Revenue Code of 1986 is amended by inserting after section 25E the following new section:\n25F. Tutoring credit (a) Allowance of credit In the case of an eligible teacher, there shall be allowed as a credit against the tax imposed by this chapter for the taxable year an amount equal to the sum of\u2014 (1) $500, plus (2) the supplemental amount. (b) Supplemental amount (1) In general For purposes of subsection (a), the supplemental amount is the amount which bears the same ratio to $500 as\u2014 (A) the number of qualified tutoring hours provided by the eligible teacher during the taxable year in excess of 150, bears to (B) 50 such hours. (2) Limitation The supplemental amount for any taxable year shall not exceed $500. (c) Eligible teacher For purposes of this section\u2014 (1) In general The term eligible teacher means, with respect to any taxable year, an individual who\u2014 (A) is employed as a teacher at a preschool, an elementary school, or a secondary school, (B) meets the State certification and licensure requirements for such employment, and (C) provides at least 150 hours of qualified tutoring during the taxable year to students enrolled at the same type of school that the teacher is employed at. (2) Qualified tutoring The term qualified tutoring means academic tutoring\u2014 (A) that occurs during hours in which school is not in session, and (B) which focuses on mathematics, reading and writing, or science. (3) Preschool The term preschool has the meaning given the term early childhood education program under section 103 of the Higher Education Act of 1965. (4) Elementary school The term elementary school has the meaning given such term in section 8101 of the Elementary and Secondary Education Act of 1965, except that such term includes public or private kindergarten, as determined under State law. (5) Secondary school The term secondary school has the meaning given such term in section 8101 of the Elementary and Secondary Education Act of 1965. (d) Special rule for married couples In the case of a joint return, this section shall be applied separately with respect to each spouse who is an eligible teacher. (e) Regulations The Secretary shall issue such regulations or other guidance as may be necessary or appropriate to carry out the purposes of this section. (f) Termination No credit shall be allowed under this section with respect to any taxable year beginning after December 31, 2032. .\n##### (b) Report\nWith respect to taxable years which begin in a calendar year for which section 25F of such Code applies, the Secretary of the Treasury shall annually transmit to Congress a written report that includes\u2014\n**(1)**\nthe number of individuals claiming the credit described in section 25F of such Code,\n**(2)**\nthe total and average number of qualified tutoring hours provided by such individuals,\n**(3)**\nthe geographic distribution of such individuals, and\n**(4)**\nsuch other information as the Secretary may require.\n##### (c) Clerical amendment\nThe table of sections for subpart A of part IV of subchapter A of chapter 1 of such Code is amended by inserting after the item relating to section 25E the following new item:\nSec. 25F. Tutoring credit. .\n##### (d) Effective date\nThe amendments made by this section shall apply with respect to taxable years beginning after December 31, 2025.",
      "versionDate": "2025-07-17",
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
        "updateDate": "2025-09-12T16:19:00Z"
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
      "date": "2025-07-17",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr4507ih.xml"
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
      "title": "TUTOR Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-07-31T04:23:22Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "TUTOR Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-07-31T04:23:20Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Teachers Utilizing Tutoring Opportunities for Relief Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-07-31T04:23:20Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Internal Revenue Code of 1986 to establish a temporary tax credit for eligible teachers who provide tutoring services, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-07-31T04:18:35Z"
    }
  ]
}
```
