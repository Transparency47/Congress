# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/1662?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/1662
- Title: LEAP Act
- Congress: 119
- Bill type: HR
- Bill number: 1662
- Origin chamber: House
- Introduced date: 2025-02-27
- Update date: 2026-01-28T09:05:37Z
- Update date including text: 2026-01-28T09:05:37Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-02-27: Introduced in House
- 2025-02-27 - IntroReferral: Introduced in House
- 2025-02-27 - IntroReferral: Introduced in House
- 2025-02-27 - IntroReferral: Referred to the Committee on Ways and Means, and in addition to the Committee on Oversight and Government Reform, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-02-27 - IntroReferral: Referred to the Committee on Ways and Means, and in addition to the Committee on Oversight and Government Reform, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- Latest action: 2025-02-27: Introduced in House

## Actions

- 2025-02-27 - IntroReferral: Introduced in House
- 2025-02-27 - IntroReferral: Introduced in House
- 2025-02-27 - IntroReferral: Referred to the Committee on Ways and Means, and in addition to the Committee on Oversight and Government Reform, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-02-27 - IntroReferral: Referred to the Committee on Ways and Means, and in addition to the Committee on Oversight and Government Reform, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-02-27",
    "latestAction": {
      "actionDate": "2025-02-27",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/1662",
    "number": "1662",
    "originChamber": "House",
    "policyArea": {
      "name": "Taxation"
    },
    "sponsors": [
      {
        "bioguideId": "B001315",
        "district": "13",
        "firstName": "Nikki",
        "fullName": "Rep. Budzinski, Nikki [D-IL-13]",
        "lastName": "Budzinski",
        "party": "D",
        "state": "IL"
      }
    ],
    "title": "LEAP Act",
    "type": "HR",
    "updateDate": "2026-01-28T09:05:37Z",
    "updateDateIncludingText": "2026-01-28T09:05:37Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-02-27",
      "committees": {
        "item": {
          "name": "Oversight and Government Reform Committee",
          "systemCode": "hsgo00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the Committee on Ways and Means, and in addition to the Committee on Oversight and Government Reform, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-02-27",
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
      "text": "Referred to the Committee on Ways and Means, and in addition to the Committee on Oversight and Government Reform, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-02-27",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-02-27",
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
          "date": "2025-02-27T14:11:40Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Oversight and Government Reform Committee",
      "systemCode": "hsgo00",
      "type": "Standing"
    },
    {
      "activities": {
        "item": {
          "date": "2025-02-27T14:11:35Z",
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
      "bioguideId": "C001126",
      "district": "15",
      "firstName": "Mike",
      "fullName": "Rep. Carey, Mike [R-OH-15]",
      "isOriginalCosponsor": "True",
      "lastName": "Carey",
      "party": "R",
      "sponsorshipDate": "2025-02-27",
      "state": "OH"
    },
    {
      "bioguideId": "H001094",
      "district": "4",
      "firstName": "Val",
      "fullName": "Rep. Hoyle, Val T. [D-OR-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Hoyle",
      "middleName": "T.",
      "party": "D",
      "sponsorshipDate": "2025-02-27",
      "state": "OR"
    },
    {
      "bioguideId": "K000391",
      "district": "8",
      "firstName": "Raja",
      "fullName": "Rep. Krishnamoorthi, Raja [D-IL-8]",
      "isOriginalCosponsor": "True",
      "lastName": "Krishnamoorthi",
      "party": "D",
      "sponsorshipDate": "2025-02-27",
      "state": "IL"
    },
    {
      "bioguideId": "M000317",
      "district": "11",
      "firstName": "Nicole",
      "fullName": "Rep. Malliotakis, Nicole [R-NY-11]",
      "isOriginalCosponsor": "False",
      "lastName": "Malliotakis",
      "party": "R",
      "sponsorshipDate": "2025-03-05",
      "state": "NY"
    },
    {
      "bioguideId": "S001225",
      "district": "17",
      "firstName": "Eric",
      "fullName": "Rep. Sorensen, Eric [D-IL-17]",
      "isOriginalCosponsor": "False",
      "lastName": "Sorensen",
      "party": "D",
      "sponsorshipDate": "2025-06-12",
      "state": "IL"
    },
    {
      "bioguideId": "R000622",
      "district": "19",
      "firstName": "Josh",
      "fullName": "Rep. Riley, Josh [D-NY-19]",
      "isOriginalCosponsor": "False",
      "lastName": "Riley",
      "party": "D",
      "sponsorshipDate": "2025-07-23",
      "state": "NY"
    },
    {
      "bioguideId": "B001278",
      "district": "1",
      "firstName": "Suzanne",
      "fullName": "Rep. Bonamici, Suzanne [D-OR-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Bonamici",
      "party": "D",
      "sponsorshipDate": "2025-11-04",
      "state": "OR"
    },
    {
      "bioguideId": "D000623",
      "district": "10",
      "firstName": "Mark",
      "fullName": "Rep. DeSaulnier, Mark [D-CA-10]",
      "isOriginalCosponsor": "False",
      "lastName": "DeSaulnier",
      "party": "D",
      "sponsorshipDate": "2025-11-25",
      "state": "CA"
    },
    {
      "bioguideId": "R000620",
      "district": "29",
      "firstName": "Luz",
      "fullName": "Rep. Rivas, Luz M. [D-CA-29]",
      "isOriginalCosponsor": "False",
      "lastName": "Rivas",
      "middleName": "M.",
      "party": "D",
      "sponsorshipDate": "2026-01-27",
      "state": "CA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1662ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 1662\nIN THE HOUSE OF REPRESENTATIVES\nFebruary 27, 2025 Ms. Budzinski (for herself, Mr. Carey , Ms. Hoyle of Oregon , and Mr. Krishnamoorthi ) introduced the following bill; which was referred to the Committee on Ways and Means , and in addition to the Committee on Oversight and Government Reform , for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned\nA BILL\nTo amend the Internal Revenue Code of 1986 to allow employers a credit against income tax for employees who participate in qualified apprenticeship programs.\n#### 1. Short title\nThis Act may be cited as the Leveraging and Energizing America\u2019s Apprenticeship Programs Act or the LEAP Act .\n#### 2. Credit for employees participating in qualified apprenticeship programs\n##### (a) In general\nSubpart D of part IV of subchapter A of chapter 1 of the Internal Revenue Code of 1986 is amended by adding at the end the following new section:\n45BB. Employees participating in qualified apprenticeship programs (a) In general For purposes of section 38, the apprenticeship credit determined under this section for the taxable year is an amount equal to $1,500 for each of the apprenticeship employees of the employer that exceeds the applicable apprenticeship level (as determined under subsection (d)) during such taxable year. (b) Limitation on number of years with respect to which credit may be taken into account The apprenticeship credit shall not be allowed for more than 2 taxable years with respect to any apprenticeship employee. (c) Apprenticeship employee For purposes of this section\u2014 (1) In general The term apprenticeship employee means any employee who is\u2014 (A) employed by the employer in an officially recognized apprenticeable occupation, as determined by the Office of Apprenticeship of the Employment and Training Administration of the Department of Labor, and (B) currently enrolled in an apprenticeship program. (2) Apprenticeship program The term apprenticeship program means a registered apprenticeship program defined in section 3131(e)(3)(B). (d) Applicable apprenticeship level (1) In general For purposes of this section, the applicable apprenticeship level shall be equal to the amount equal to 80 percent of the average number of such apprenticeship employees of the employer for the 3 taxable years preceding the taxable year for which the credit is being determined, rounded to the next lower whole number. (2) First year of new apprenticeship programs In the case of an employer which did not have any apprenticeship employees during any taxable year in the 3 taxable years preceding the taxable year for which the credit is being determined, the applicable apprenticeship level shall be equal to zero. (e) Exclusion for certain industries (1) In general No credit may be allowed under this section with respect to an individual employed by an employer in any sector described in the North American Industry Classification System code beginning with 23 unless\u2014 (A) such individual is a pre-apprenticeship graduate currently enrolled in an apprenticeship program, and (B) such employer participates in or sponsors an apprenticeship program. (2) Pre-apprenticeship graduate For purposes of this subsection, the term pre-apprenticeship graduate means any individual who has completed a pre-apprenticeship program. (3) Pre-apprenticeship program For purposes of this subsection, the term pre-apprenticeship program means a program that\u2014 (A) is designed to prepare participants to enter an apprenticeship program, (B) is carried out by a sponsor that has a documented partnership with 1 or more sponsors of apprenticeship programs, and (C) includes each of the following: (i) Training (including a curriculum for the training) and theoretical education for participants that\u2014 (I) is aligned with industry standards related to an apprenticeship program and reviewed and approved annually by sponsors of the apprenticeship program within the documented partnership that will prepare participants by teaching the skills and competencies needed to enter 1 or more apprenticeship programs, and (II) does not displace a paid employee. (ii) A formal agreement with a sponsor of an apprenticeship program that will facilitate or expedite entry of pre-apprenticeship graduates into the apprenticeship program, provided that a place in the apprenticeship program is available and that the pre-apprenticeship graduate meets the qualifications of such program. (f) Coordination with other credits The amount of credit otherwise allowable under sections 45A, 51(a), and 1396(a) with respect to any employee shall be reduced by the credit allowed by this section with respect to such employee. (g) Certain rules To apply Rules similar to the rules of subsections (i)(1) and (k) of section 51 shall apply for purposes of this section. .\n##### (b) Credit made part of general business credit\nSubsection (b) of section 38 of such Code is amended by striking the period at the end of paragraph (40) and inserting a comma, by striking the period at the end of paragraph (41) and inserting , plus , and by adding at the end the following new paragraph:\n(42) the apprenticeship credit determined under section 45BB(a). .\n##### (c) Denial of double benefit\nSubsection (a) of section 280C of such Code is amended by inserting 45BB(a), after 45S(a), .\n##### (d) Clerical amendment\nThe table of sections for subpart D of part IV of subchapter A of chapter 1 of such Code is amended by adding at the end the following new item:\nSec. 45BB. Employees participating in qualified apprenticeship programs.\n##### (e) Effective date\nThe amendments made by this section shall apply to individuals commencing apprenticeship programs after the date of the enactment of this Act.\n#### 3. Limitation on government printing costs\nNot later than 90 days after the date of enactment of this Act, the Director of the Office of Management and Budget shall coordinate with the heads of Federal departments and independent agencies to\u2014\n**(1)**\ndetermine which Government publications could be available on Government websites and no longer printed and to devise a strategy to reduce overall Government printing costs over the 10-year period beginning with fiscal year 2026, except that the Director shall ensure that essential printed documents prepared for social security recipients, Medicare beneficiaries, and other populations in areas with limited internet access or use continue to remain available;\n**(2)**\nestablish government-wide Federal guidelines on employee printing; and\n**(3)**\nissue guidelines requiring every department, agency, commission, or office to list at a prominent place near the beginning of each publication distributed to the public and issued or paid for by the Federal Government\u2014\n**(A)**\nthe name of the issuing agency, department, commission, or office;\n**(B)**\nthe total number of copies of the document printed;\n**(C)**\nthe collective cost of producing and printing all of the copies of the document; and\n**(D)**\nthe name of the entity publishing the document.",
      "versionDate": "2025-02-27",
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
        "updateDate": "2025-05-07T14:13:15Z"
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
      "date": "2025-02-27",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1662ih.xml"
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
      "title": "LEAP Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-03-18T04:38:23Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "LEAP Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-18T04:38:22Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Leveraging and Energizing America\u2019s Apprenticeship Programs Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-18T04:38:22Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Internal Revenue Code of 1986 to allow employers a credit against income tax for employees who participate in qualified apprenticeship programs.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-18T04:33:23Z"
    }
  ]
}
```
