# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/4949?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/4949
- Title: Apprenticeships for Small Businesses Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 4949
- Origin chamber: House
- Introduced date: 2025-08-12
- Update date: 2025-09-16T08:06:19Z
- Update date including text: 2025-09-16T08:06:19Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-08-12: Introduced in House
- 2025-08-12 - IntroReferral: Introduced in House
- 2025-08-12 - IntroReferral: Introduced in House
- 2025-08-12 - IntroReferral: Referred to the House Committee on Ways and Means.
- Latest action: 2025-08-12: Introduced in House

## Actions

- 2025-08-12 - IntroReferral: Introduced in House
- 2025-08-12 - IntroReferral: Introduced in House
- 2025-08-12 - IntroReferral: Referred to the House Committee on Ways and Means.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-08-12",
    "latestAction": {
      "actionDate": "2025-08-12",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/4949",
    "number": "4949",
    "originChamber": "House",
    "policyArea": {
      "name": "Taxation"
    },
    "sponsors": [
      {
        "bioguideId": "H001090",
        "district": "9",
        "firstName": "Josh",
        "fullName": "Rep. Harder, Josh [D-CA-9]",
        "lastName": "Harder",
        "party": "D",
        "state": "CA"
      }
    ],
    "title": "Apprenticeships for Small Businesses Act of 2025",
    "type": "HR",
    "updateDate": "2025-09-16T08:06:19Z",
    "updateDateIncludingText": "2025-09-16T08:06:19Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-08-12",
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
      "actionDate": "2025-08-12",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-08-12",
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
          "date": "2025-08-12T13:02:25Z",
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
      "bioguideId": "K000399",
      "district": "2",
      "firstName": "Jennifer",
      "fullName": "Rep. Kiggans, Jennifer A. [R-VA-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Kiggans",
      "middleName": "A.",
      "party": "R",
      "sponsorshipDate": "2025-08-12",
      "state": "VA"
    },
    {
      "bioguideId": "F000466",
      "district": "1",
      "firstName": "Brian",
      "fullName": "Rep. Fitzpatrick, Brian K. [R-PA-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Fitzpatrick",
      "middleName": "K.",
      "party": "R",
      "sponsorshipDate": "2025-09-15",
      "state": "PA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr4949ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 4949\nIN THE HOUSE OF REPRESENTATIVES\nAugust 12, 2025 Mr. Harder of California (for himself and Mrs. Kiggans of Virginia ) introduced the following bill; which was referred to the Committee on Ways and Means\nA BILL\nTo amend the Internal Revenue Code of 1986 to establish a credit for certain employers of qualifying career and technical education students.\n#### 1. Short title\nThis Act may be cited as the Apprenticeships for Small Businesses Act of 2025 .\n#### 2. Career and technical education credit\n##### (a) In general\nSubpart D of part IV of subchapter A of chapter 1 of the Internal Revenue Code of 1986 is amended by adding at the end the following new section:\n45U. Career and technical education credit (a) In general For the purposes of section 38, in the case of a small business concern (as such term is defined under section 3 of the Small Business Act), the career and technical education credit determined under this section for any taxable year is an amount equal to the sum of\u2014 (1) the amount equal to 50 percent of the qualified wages paid by the taxpayer during the taxable year, plus (2) the amount equal to the qualified workmen\u2019s compensation expenses of the taxpayer for the taxable year. (b) Limitation (1) In general The amount of credit determined under subsection (a) shall not exceed $10,000 for any taxpayer in any taxable year. (2) Related party For purposes of paragraph (1), taxpayers which are treated as a single employer under subsection (a) or (b) of section 52 or subsection (m) or (o) of section 414 shall be treated as a single taxpayer. (c) Qualified employee For purposes of this section, the term qualified employee means, with respect to an employer, an employee who\u2014 (1) has not attained the age of 21 as of the last day of the taxable year, or (2) is\u2014 (A) participating in a registered apprenticeship program, as defined in section 3131(e)(3)(B), or (B) enrolled, during such taxable year, in\u2014 (i) any course of study relating to the trade or business of such employer at a community college which complies with any applicable State or local licensing requirements necessary to issue associate\u2019s degrees, or (ii) any career training or vocational program (including career and technical education programs of a high school) relating to the trade or business of the employer. (d) Qualified workmen\u2019s compensation expenses For purposes of this section, the term qualified workmen\u2019s compensation expenses means amounts paid or incurred by the taxpayer during the taxable year for premiums relating to an insurance policy (or the appropriate portion of such policy) which insures the taxpayer against claims under a workmen's compensation law of the United States, any State, the District of Columbia, or the Commonwealth of Puerto Rico in relation to the employment of a qualified employee. .\n##### (b) Credit To be part of general business credit\nSection 38(b) of such Code is amended by striking plus at the end of paragraph (32), by striking the period at the end of paragraph (33) and inserting , plus , and by adding at the end the following new paragraph:\n(34) in the case of small business concern (as such term is defined under section 3 of the Small Business Act), the career and technical education credit determined under section 45U(a). .\n##### (c) Clerical amendment\nThe table of sections for subpart D of part IV of subchapter A of chapter 1 of such Code is amended by inserting after the item relating to section 45T the following new item:\nSec. 45U. Career and technical education credit. .\n##### (d) Effective date\nThe amendments made by this section shall apply amounts paid or incurred in taxable years beginning after December 31, 2025.",
      "versionDate": "2025-08-12",
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
        "updateDate": "2025-09-05T16:05:17Z"
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
      "date": "2025-08-12",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr4949ih.xml"
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
      "title": "Apprenticeships for Small Businesses Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-08-13T08:23:20Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Apprenticeships for Small Businesses Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-08-13T08:23:19Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Internal Revenue Code of 1986 to establish a credit for certain employers of qualifying career and technical education students.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-08-13T08:18:20Z"
    }
  ]
}
```
