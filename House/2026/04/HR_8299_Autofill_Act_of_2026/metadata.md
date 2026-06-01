# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/8299?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/8299
- Title: Autofill Act of 2026
- Congress: 119
- Bill type: HR
- Bill number: 8299
- Origin chamber: House
- Introduced date: 2026-04-15
- Update date: 2026-04-27T22:30:21Z
- Update date including text: 2026-04-27T22:30:21Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2026-04-15: Introduced in House
- 2026-04-15 - IntroReferral: Introduced in House
- 2026-04-15 - IntroReferral: Introduced in House
- 2026-04-15 - IntroReferral: Referred to the House Committee on Ways and Means.
- Latest action: 2026-04-15: Introduced in House

## Actions

- 2026-04-15 - IntroReferral: Introduced in House
- 2026-04-15 - IntroReferral: Introduced in House
- 2026-04-15 - IntroReferral: Referred to the House Committee on Ways and Means.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-04-15",
    "latestAction": {
      "actionDate": "2026-04-15",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/8299",
    "number": "8299",
    "originChamber": "House",
    "policyArea": {
      "name": "Taxation"
    },
    "sponsors": [
      {
        "bioguideId": "F000454",
        "district": "11",
        "firstName": "Bill",
        "fullName": "Rep. Foster, Bill [D-IL-11]",
        "lastName": "Foster",
        "party": "D",
        "state": "IL"
      }
    ],
    "title": "Autofill Act of 2026",
    "type": "HR",
    "updateDate": "2026-04-27T22:30:21Z",
    "updateDateIncludingText": "2026-04-27T22:30:21Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2026-04-15",
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
      "actionDate": "2026-04-15",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-04-15",
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
          "date": "2026-04-15T14:03:05Z",
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
      "bioguideId": "T000481",
      "district": "12",
      "firstName": "Rashida",
      "fullName": "Rep. Tlaib, Rashida [D-MI-12]",
      "isOriginalCosponsor": "True",
      "lastName": "Tlaib",
      "party": "D",
      "sponsorshipDate": "2026-04-15",
      "state": "MI"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr8299ih.xml",
      "text": "I\n119th CONGRESS\n2d Session\nH. R. 8299\nIN THE HOUSE OF REPRESENTATIVES\nApril 15, 2026 Mr. Foster (for himself and Ms. Tlaib ) introduced the following bill; which was referred to the Committee on Ways and Means\nA BILL\nTo amend the Internal Revenue Code of 1986 to establish a program to populate downloadable tax forms with taxpayer return information.\n#### 1. Short title\nThis Act may be cited as the Autofill Act of 2026 .\n#### 2. Automated partially pre-populated tax returns\n##### (a) In general\nChapter 77 of the Internal Revenue Code of 1986 is amended by adding at the end the following new section:\n7531. Automated partially pre-populated tax returns (a) Establishment of program The Secretary shall establish a program under which taxpayers may download forms relating to the individual income tax returns that are populated with return information reported to the Secretary under chapter 61 and reported to the Secretary pursuant to section 232 of the Social Security Act. (b) Requirements relating to information (1) Deadline for making information available The Secretary shall make such return information available under the program established under subsection (a) not later than 15 days after the Secretary receives such information. (2) Format of information made available Return information shall be made available under the program established under subsection (a) in both a printable document file suitable for manual completion and filing and in a computer-readable form suitable for use by automated tax preparation software. (c) Autofill service deadlines (1) Standards Not later than October 31, 2026, the Secretary shall\u2014 (A) establish standards for data download to tax preparation software, and (B) provide a demonstration server for downloading the partially populated printable document file. (2) Tax forms Not later than February 15, 2027, and annually thereafter, the Secretary shall provide on the Secretary\u2019s website a secure function that allows a taxpayer to download, as both a printable document file and in a form suitable for input to automatic tax preparation software, the 1040, 1040A, and 1040EZ forms that are populated with information with respect to the taxpayer that is reported under chapter 61 or any other provision of this title under which reporting of information is required. (d) Taxpayer responsibility Nothing in this section shall be construed to absolve the taxpayer from full responsibility for the accuracy or completeness of his return of tax. (e) Disclaimer Before any form can be downloaded under the program established under subsection (a), taxpayer must acknowledge that\u2014 (1) the taxpayer is responsible for the accuracy of his return, and (2) all information provided in the downloadable form under such program needs to be verified. (f) Information provided for wage and self employment income For purposes of subsection (a)\u2014 (1) Information related to calendar year 2026 In the case of information relating to wages paid, and amounts of self-employment income, for calendar year 2026 required to be provided to the Commissioner of Social Security under section 205(c)(2)(A) of the Social Security Act ( 42 U.S.C. 405(c)(2)(A) ), the Commissioner shall, using best efforts, make such information available to the Secretary not later than January 31, 2027. (2) Information related to calendar year 2027 and thereafter In the case of information relating to wages paid, and amounts of self-employment income, for any calendar year after 2026 required to be provided to the Commissioner of Social Security under section 205(c)(2)(A) of the Social Security Act ( 42 U.S.C. 405(c)(2)(A) ), the Commissioner shall make such information available to the Secretary not later than the January 31 of the calendar year following the calendar year to which such wages and self-employment income relate. .\n##### (b) Filing deadline for information returns\nSection 6071(b) of such Code is amended to read as follows:\n(b) Information returns Returns made under part III of this subchapter shall be filed on or before January 31 of the year following the calendar year to which such returns relate. Section 6081 shall not apply to returns under such part III. .\n##### (c) Conforming amendment to social security act\nSection 205(c)(2)(A) of the Social Security Act ( 42 U.S.C. 405(c)(2)(A) ) is amended by adding at the end the following new sentence: For purposes of the preceding sentence, the Commissioner shall require that information relating to wages paid, and amounts of self-employment income, be provided to the Commissioner not later than January 31 of the year following the calendar year to which such wages and self-employment income relate. .\n##### (d) Clerical amendment\nThe table of sections for chapter 77 of such Code is amended by adding at the end the following new item:\nSec. 7531. Automated partially pre-populated tax returns. .\n##### (e) Effective date\nThe amendments made by this section shall apply to returns for taxable years beginning after December 31, 2025.",
      "versionDate": "2026-04-15",
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
        "updateDate": "2026-04-27T22:30:20Z"
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
      "date": "2026-04-15",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr8299ih.xml"
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
      "title": "Autofill Act of 2026",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-04-21T06:08:27Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Autofill Act of 2026",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-04-21T06:08:26Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Internal Revenue Code of 1986 to establish a program to populate downloadable tax forms with taxpayer return information.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-04-21T06:03:36Z"
    }
  ]
}
```
